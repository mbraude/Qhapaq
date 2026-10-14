#!/usr/bin/env python3
"""Hash and verify Qhapaq work-record snapshots without ad hoc scripts.

Commands (exit 1 when a verification finds a mismatch):
  files PATH...          Full-byte SHA-256 of each file.
  sources PATH...        Ready-to-paste frontmatter `sources` entries.
  material ITEM...       Material SHA-256 as defined in the workflow guide for the record's kind
                         (work item, plan, or readiness record).
  verify RECORD...       Check each record's frontmatter `sources` hashes.
  diff RECORD...         Unified diff of each non-current source since its recorded snapshot.
  refresh RECORD [PATH...] [--stale] [--add PATH...] [--remove PATH...]
                         Rewrite frontmatter `sources` entries in place with current
                         revision and hashes; --add appends new entries and --remove
                         deletes entries. The only writing command; run it only after
                         judging the change, as the calling skill requires.
  approval TARGET [--files PATH...]
                         Verify a work item, plan, or readiness record is approvable and
                         print its ready-to-paste approval evidence block.
  evidence ITEM...       Check recorded material and path/hash evidence tables.

Usage:
  python .agents/scripts/work_hashes.py material work/0008/implementation/I-0008-013-*.md
  python .agents/scripts/work_hashes.py sources SPEC.md work/0008/plan.md
  python .agents/scripts/work_hashes.py diff work/0007/plan.md
  python .agents/scripts/work_hashes.py refresh work/0007/plan.md docs/development/spec-driven-workflow.md
  python .agents/scripts/work_hashes.py evidence --section "Plan approval" <item>
"""

from __future__ import annotations

import argparse
import difflib
import glob
import json
import re
import sys

import qhapaq_work as q


def expand(paths: list[str]) -> list[str]:
    result: list[str] = []
    for value in paths:
        matches = sorted(glob.glob(str(q.ROOT / value))) if any(c in value for c in "*?[") else []
        result.extend(q.repo_path(m) for m in matches) if matches else result.append(q.repo_path(value))
    return result


def cmd_files(snap: q.Snapshot, paths: list[str]) -> tuple[list[dict], bool]:
    rows = [{"path": p, "sha256": snap.sha(p)} for p in paths]
    return rows, all(r["sha256"] for r in rows)


def cmd_sources(snap: q.Snapshot, paths: list[str]) -> tuple[list[dict], bool]:
    dirty = set(line[3:] for line in q.git("status", "--porcelain=v1", "--untracked-files=all", "--", *paths).splitlines())
    rows = []
    for path in paths:
        tracked = q.is_tracked(path)
        data = snap.read(path)
        rows.append({
            "path": path,
            "revision": q.last_commit(path) if tracked else None,
            "content_sha256": snap.sha(path),
            "material_sha256": q.source_material_sha256(path, data) if data is not None else None,
            "working_copy_differs": path in dirty,
        })
    return rows, all(r["content_sha256"] for r in rows)


def material_of(path: str, data: bytes) -> str:
    """Material SHA-256 by record kind: plan and readiness records use their own
    definition; work items and other files use the work-item definition."""
    return q.source_material_sha256(path, data) or q.material_sha256(data)


def cmd_material(snap: q.Snapshot, paths: list[str]) -> tuple[list[dict], bool]:
    rows = []
    for path in paths:
        data = snap.read(path)
        rows.append({"path": path, "material_sha256": None if data is None else material_of(path, data)})
    return rows, all(r["material_sha256"] for r in rows)


def cmd_verify(snap: q.Snapshot, paths: list[str]) -> tuple[list[dict], bool]:
    rows, ok = [], True
    for record in paths:
        meta = q.parse_frontmatter(snap.text(record))
        sources = meta.get("sources") or []
        if snap.read(record) is None:
            rows.append({"record": record, "path": None, "state": "record-missing"})
            ok = False
            continue
        if not q.WORK_ITEM_RE.match(record):
            state = q.process_state(snap, meta.get("process_version"))
            ok &= state == "current"
            rows.append({"record": record, "path": "process_version", "basis": "process",
                         "recorded": meta.get("process_version"), "actual": q.process_version(snap), "state": state})
        for source in sources if isinstance(sources, list) else []:
            if not isinstance(source, dict) or not source.get("path"):
                rows.append({"record": record, "path": None, "state": "malformed"})
                ok = False
                continue
            actual = snap.sha(source["path"])
            recorded = source.get("content_sha256")
            material = source.get("material_sha256")
            kind = q.source_kind(source["path"])
            state = "derived-view" if kind == "derived-view" else q.source_state(
                snap, source["path"], recorded, source.get("revision"), material)
            ok &= state == "current"
            by_material = bool(material) and q.has_material(source["path"])
            if by_material:
                recorded, actual = material, q.source_material_sha256(source["path"], snap.read(source["path"]) or b"")
            rows.append({"record": record, "path": source["path"], "revision": source.get("revision"),
                         "basis": "material" if by_material else "bytes", "kind": kind,
                         "recorded": recorded, "actual": actual, "state": state})
    return rows, ok


def recorded_sources(snap: q.Snapshot, record: str) -> list[dict]:
    sources = q.parse_frontmatter(snap.text(record)).get("sources") or []
    return [s for s in sources if isinstance(s, dict) and s.get("path")] if isinstance(sources, list) else []


def cmd_diff(snap: q.Snapshot, paths: list[str], max_lines: int) -> tuple[list[dict], bool]:
    rows = []
    for record in paths:
        if snap.read(record) is None:
            rows.append({"record": record, "path": None, "state": "record-missing", "basis": None, "diff": []})
            continue
        for source in recorded_sources(snap, record):
            path = source["path"]
            state = q.source_state(snap, path, source.get("content_sha256"), source.get("revision"),
                                   source.get("material_sha256"))
            if state == "current":
                continue
            old, basis = None, "recorded bytes"
            if source.get("content_sha256"):
                old = q.recover_bytes(path, source["content_sha256"], source.get("revision"))
            if old is None and source.get("revision"):
                old = q.git_bytes("show", f"{source['revision']}:{path}")
                basis = f"revision {source['revision'][:12]} (recorded bytes not in history)"
            new = snap.read(path)
            if old is None:
                lines = ["(no prior bytes recoverable; review the whole file)"]
            else:
                lines = list(difflib.unified_diff(
                    old.decode("utf-8", errors="replace").splitlines(),
                    (new or b"").decode("utf-8", errors="replace").splitlines(),
                    f"a/{path}", f"b/{path}", n=2, lineterm=""))
            added = sum(1 for l in lines if l.startswith("+") and not l.startswith("+++"))
            removed = sum(1 for l in lines if l.startswith("-") and not l.startswith("---"))
            truncated = max(0, len(lines) - max_lines) if max_lines else 0
            rows.append({"record": record, "path": path, "state": state, "basis": basis, "added": added,
                         "removed": removed, "truncated": truncated,
                         "diff": lines[:max_lines] if max_lines else lines})
    return rows, all(r["state"] != "record-missing" for r in rows)


SOURCE_ENTRY_RE = re.compile(r"^(\s*)-\s+path:\s*(.*)$")
SOURCE_FIELD_RE = re.compile(r"^(\s+)(revision|content_sha256|material_sha256):\s*(.*)$")


def set_value(old: str, value: str | None) -> str:
    """Format `value`, keeping the quoting style of the value it replaces."""
    if value is None:
        return "null"
    quote = old.strip()[:1] if old.strip()[:1] in "\"'" else ""
    return f"{quote}{value}{quote}"


def source_values(snap: q.Snapshot, path: str, content: str) -> dict:
    return {
        "revision": q.last_commit(path) if q.is_tracked(path) else None,
        "content_sha256": content,
        "material_sha256": q.source_material_sha256(path, snap.read(path)),
    }


def cmd_refresh(snap: q.Snapshot, record: str, wanted: list[str], stale: bool,
                add: list[str] | None = None, remove: list[str] | None = None) -> tuple[list[dict], bool]:
    add, remove = add or [], remove or []
    data = snap.read(record)
    if data is None:
        return [{"record": record, "path": None, "state": "record-missing"}], False
    if record in wanted + add:
        return [{"record": record, "path": record, "state": "refused: a record is never its own source"}], False
    if conflict := sorted(set(remove) & set(wanted + add)):
        return [{"record": record, "path": p, "state": "refused: both removed and refreshed"} for p in conflict], False
    text = data.decode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(newline)
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return [{"record": record, "path": None, "state": "no frontmatter"}], False
    end = lines.index("---", 1)
    entries: list[dict] = []
    in_sources = False
    sources_key = sources_last = None
    for index in range(1, end):
        line = lines[index]
        if re.match(r"^[A-Za-z_][\w-]*:", line):
            in_sources = line.startswith("sources:")
            if in_sources:
                sources_key = sources_last = index
            continue
        if in_sources:
            sources_last = index
        entry = SOURCE_ENTRY_RE.match(line) if in_sources else None
        if entry:
            entries.append({"path": q.unquote(entry.group(2)), "indent": len(entry.group(1)) + 2,
                            "dash": entry.group(1), "raw_path": entry.group(2), "path_line": index, "fields": {}})
        elif in_sources and entries and (field := SOURCE_FIELD_RE.match(line)):
            entries[-1]["fields"][field.group(2)] = (index, field.group(3))
    by_path = {e["path"]: e for e in entries}
    unknown = [p for p in wanted + remove if p not in by_path]
    if unknown:
        return [{"record": record, "path": p, "state": "not a recorded source"} for p in unknown], False
    derived = [p for p in wanted + add if q.source_kind(p) == "derived-view"]
    if derived:
        return [{"record": record, "path": p, "state": "derived view; never a source"} for p in derived], False
    missing = [p for p in add if snap.sha(p) is None]
    if missing:
        return [{"record": record, "path": p, "state": "missing"} for p in missing], False
    edits: list[tuple[int, int, list[str] | int]] = []  # (position, order, inserted lines | delete-through index)
    rows: list[dict] = []
    for position, e in enumerate(entries):
        if e["path"] in remove:
            last = entries[position + 1]["path_line"] - 1 if position + 1 < len(entries) else sources_last
            edits.append((e["path_line"], 2, last))
            rows.append({"record": record, "path": e["path"], "state": "removed"})
    new = [p for p in dict.fromkeys(add) if p not in by_path]
    if new:
        model = entries[0] if entries else None
        dash = model["dash"] if model else "  "
        quote = model["raw_path"].strip()[:1] if model and model["raw_path"].strip()[:1] in "\"'" else ""
        style = next(iter(model["fields"].values()), (0, ""))[1] if model else ""
        block: list[str] = []
        for path in new:
            values = source_values(snap, path, snap.sha(path))
            block.append(f"{dash}- path: {quote}{path}{quote}")
            block += [f"{dash}  {k}: {set_value(style, v)}" for k, v in values.items()
                      if v is not None or k == "revision"]
            state = "added (process artifact: cite only when the scope governs it)" \
                if q.source_kind(path) == "process" else "added"
            rows.append({"record": record, "path": path, "state": state, **values})
        if sources_key is None:
            edits.append((end, 1, ["sources:", *block]))
        else:
            if re.match(r"^sources:\s*\[\s*\]\s*$", lines[sources_key]):
                lines[sources_key] = "sources:"
            edits.append((sources_last + 1, 1, block))
    targets = list(dict.fromkeys(wanted + [p for p in add if p in by_path]))
    if stale:
        for e in entries:
            fields = {k: q.unquote(v) for k, (_, v) in e["fields"].items()}
            if e["path"] not in targets and e["path"] not in remove and q.source_kind(e["path"]) != "derived-view" \
                    and q.source_state(snap, e["path"], fields.get("content_sha256"), fields.get("revision"),
                                       fields.get("material_sha256")) != "current":
                targets.append(e["path"])
    ok = True
    for path in targets:
        e = by_path[path]
        content = snap.sha(path)
        if content is None:
            rows.append({"record": record, "path": path, "state": "missing"})
            ok = False
            continue
        values = source_values(snap, path, content)
        for key, value in values.items():
            if key in e["fields"]:
                index, old = e["fields"][key]
                if key == "material_sha256" and value is None:
                    continue
                lines[index] = f"{' ' * e['indent']}{key}: {set_value(old, value)}"
            elif value is not None:
                anchor = max([i for i, _ in e["fields"].values()] + [e["path_line"]])
                style = next(iter(e["fields"].values()), (0, ""))[1]
                edits.append((anchor + 1, 0, [f"{' ' * e['indent']}{key}: {set_value(style, value)}"]))
        rows.append({"record": record, "path": path, "state": "refreshed", **values})
    # Apply bottom-up; at one position delete first, then the appended block, then field lines, so
    # a refreshed last entry keeps its new fields ahead of appended entries.
    for position, _, change in sorted(edits, key=lambda e: (e[0], e[1]), reverse=True):
        if isinstance(change, int):
            del lines[position:change + 1]
        else:
            lines[position:position] = change
    if rows and ok:
        (q.ROOT / record).write_bytes(newline.join(lines).encode("utf-8"))
    return rows, ok


def cmd_approval(snap: q.Snapshot, target: str, files: list[str]) -> tuple[list[dict], bool]:
    """Everything approval evidence needs, verified in one pass: the target's material SHA-256,
    its recorded sources (plans and readiness records), and full-byte hashes of `files`."""
    data = snap.read(target)
    if data is None:
        return [{"kind": "target", "path": target, "state": "missing"}], False
    rows = [{"kind": "material", "path": target, "sha256": material_of(target, data), "state": "current"}]
    ok = True
    if not q.WORK_ITEM_RE.match(target) and q.parse_frontmatter(snap.text(target)).get("sources") is not None:
        verified, ok = cmd_verify(snap, [target])
        rows += [{"kind": "source", "path": r["path"], "state": r["state"], "recorded": r.get("recorded"),
                  "actual": r.get("actual")} for r in verified]
    for path in files:
        sha = snap.sha(path)
        ok &= sha is not None
        rows.append({"kind": "file", "path": path, "sha256": sha, "state": "current" if sha else "missing"})
    return rows, ok


def cmd_evidence(snap: q.Snapshot, paths: list[str], wanted: list[str]) -> tuple[list[dict], bool]:
    rows, ok = [], True
    for item in paths:
        text = snap.text(item)
        if snap.read(item) is None:
            rows.append({"item": item, "kind": "item-missing", "state": "missing"})
            ok = False
            continue
        material = material_of(item, snap.read(item))
        for heading, start, lines in q.sections(text):
            if wanted and heading not in wanted:
                continue
            for offset, line in enumerate(lines, 1):
                line_no = start + offset
                for recorded in q.MATERIAL_LINE_RE.findall(line):
                    state = "current" if recorded == material else "stale"
                    ok &= state == "current"
                    rows.append({"item": item, "section": heading, "line": line_no, "kind": "material",
                                 "path": item, "recorded": recorded, "actual": material, "state": state})
                row = q.PATH_HASH_ROW_RE.match(line)
                if row:
                    path, recorded = row.group(1), row.group(2)
                    actual = snap.sha(path)
                    state = "missing" if actual is None else "current" if actual == recorded else "stale"
                    ok &= state == "current"
                    rows.append({"item": item, "section": heading, "line": line_no, "kind": "file",
                                 "path": path, "recorded": recorded, "actual": actual, "state": state})
    return rows, ok


def print_text(command: str, rows: list[dict]) -> None:
    if command == "files":
        for r in rows:
            print(f"{r['sha256'] or 'MISSING'}  {r['path']}")
    elif command == "material":
        for r in rows:
            print(f"{r['material_sha256'] or 'MISSING'}  {r['path']}  (material)")
    elif command == "sources":
        print("sources:")
        for r in rows:
            revision = r["revision"] or "null"
            print(f"  - path: {r['path']}\n    revision: {revision}\n    content_sha256: {r['content_sha256'] or 'MISSING'}")
            if r["material_sha256"]:
                print(f"    material_sha256: {r['material_sha256']}")
        notes = [r["path"] for r in rows if r["working_copy_differs"]]
        if notes:
            print("# working copy differs from revision (hash covers working-copy bytes): " + ", ".join(notes), file=sys.stderr)
    elif command == "verify":
        for r in rows:
            detail = "" if r["state"] in ("current", "malformed", "record-missing", "derived-view") else f" recorded={r['recorded']} actual={r['actual']}"
            basis = " (material)" if r.get("basis") == "material" else " (process source)" if r.get("kind") == "process" else ""
            print(f"{r['state']:<8} {r['record']} -> {r['path']}{basis}{detail}")
    elif command == "diff":
        for r in rows:
            if r["state"] == "record-missing":
                print(f"record-missing  {r['record']}")
                continue
            print(f"## {r['record']} -> {r['path']}  [{r['state']}; +{r['added']} -{r['removed']} vs {r['basis']}]")
            for line in r["diff"]:
                print(line)
            if r["truncated"]:
                print(f"... {r['truncated']} more diff lines (raise --max-lines to see them)")
        if not rows:
            print("all recorded sources current")
    elif command == "refresh":
        for r in rows:
            print(f"{r['state']:<9} {r['record']} -> {r['path']}")
        if not rows:
            print("nothing to refresh")
    elif command == "approval":
        problems = [r for r in rows if r["state"] != "current"]
        if problems:
            print("not approvable; renew assessment or review first:")
            for r in problems:
                detail = f" recorded={r['recorded']} actual={r['actual']}" if r.get("recorded") else ""
                print(f"  {r['state']:<8} {r['kind']} {r['path']}{detail}")
            return
        sources = sum(1 for r in rows if r["kind"] == "source")
        if sources:
            print(f"# {sources} recorded source and process checks current; paste the block below as evidence")
        material = rows[0]
        print(f"Approved material SHA-256: `{material['sha256']}` (`{material['path']}`).")
        files = [r for r in rows if r["kind"] == "file"]
        if files:
            print("\n| Path | SHA-256 |\n| --- | --- |")
            for r in files:
                print(f"| `{r['path']}` | `{r['sha256']}` |")
    elif command == "evidence":
        for r in rows:
            if r["kind"] == "item-missing":
                print(f"missing  {r['item']}")
                continue
            detail = "" if r["state"] == "current" else f" recorded={r['recorded']} actual={r['actual']}"
            print(f"{r['state']:<8} {r['item']}:{r['line']} [{r['section']}] {r['kind']} {r['path']}{detail}")
        if not rows:
            print("no recorded evidence hashes found")


def main() -> int:
    parser = argparse.ArgumentParser(description="Hash and verify Qhapaq work-record snapshots.")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("files", "sources", "material", "verify"):
        sub.add_parser(name).add_argument("paths", nargs="+")
    diff = sub.add_parser("diff")
    diff.add_argument("paths", nargs="+")
    diff.add_argument("--max-lines", type=int, default=200, help="diff lines per source; 0 for all")
    refresh = sub.add_parser("refresh")
    refresh.add_argument("record")
    refresh.add_argument("paths", nargs="*", help="recorded source paths to refresh")
    refresh.add_argument("--stale", action="store_true", help="also refresh every non-current source")
    refresh.add_argument("--add", nargs="+", default=[], metavar="PATH",
                         help="append new source entries (refreshes ones already recorded)")
    refresh.add_argument("--remove", nargs="+", default=[], metavar="PATH", help="delete recorded source entries")
    approval = sub.add_parser("approval")
    approval.add_argument("target")
    approval.add_argument("--files", nargs="+", default=[], metavar="PATH",
                          help="material input/output files to list with full-byte hashes")
    evidence = sub.add_parser("evidence")
    evidence.add_argument("paths", nargs="+")
    evidence.add_argument("--section", action="append", default=[], help="limit to a level-2 section; repeatable")
    args = parser.parse_args()
    q.utf8_stdio()

    snap = q.Snapshot()
    if args.command == "refresh":
        if not (args.paths or args.stale or args.add or args.remove):
            parser.error("refresh needs source paths, --stale, --add, or --remove")
        rows, ok = cmd_refresh(snap, q.repo_path(args.record), [q.repo_path(p) for p in args.paths], args.stale,
                               expand(args.add), [q.repo_path(p) for p in args.remove])
    elif args.command == "approval":
        rows, ok = cmd_approval(snap, q.repo_path(args.target), expand(args.files))
    elif args.command == "evidence":
        rows, ok = cmd_evidence(snap, expand(args.paths), args.section)
    elif args.command == "diff":
        rows, ok = cmd_diff(snap, expand(args.paths), args.max_lines)
    else:
        paths = expand(args.paths)
        rows, ok = {"files": cmd_files, "sources": cmd_sources, "material": cmd_material, "verify": cmd_verify}[args.command](snap, paths)
    if args.json:
        print(json.dumps({"command": args.command, "ok": ok, "rows": rows}, indent=2))
    else:
        print_text(args.command, rows)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
