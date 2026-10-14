#!/usr/bin/env python3
"""Hash and verify Qhapaq work-record snapshots without ad hoc scripts.

Commands (all read-only; exit 1 when a verification finds a mismatch):
  files PATH...          Full-byte SHA-256 of each file.
  sources PATH...        Ready-to-paste frontmatter `sources` entries.
  material ITEM...       Material SHA-256 as defined in the workflow guide.
  verify RECORD...       Check each record's frontmatter `sources` hashes.
  evidence ITEM...       Check recorded material and path/hash evidence tables.

Usage:
  python .agents/scripts/work_hashes.py material work/0008/implementation/I-0008-013-*.md
  python .agents/scripts/work_hashes.py sources SPEC.md work/0008/plan.md
  python .agents/scripts/work_hashes.py evidence --section "Plan approval" <item>
"""

from __future__ import annotations

import argparse
import glob
import json
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
            "material_sha256": q.material_sha256(data) if data is not None and q.WORK_ITEM_RE.match(path) else None,
            "working_copy_differs": path in dirty,
        })
    return rows, all(r["content_sha256"] for r in rows)


def cmd_material(snap: q.Snapshot, paths: list[str]) -> tuple[list[dict], bool]:
    rows = []
    for path in paths:
        data = snap.read(path)
        rows.append({"path": path, "material_sha256": None if data is None else q.material_sha256(data)})
    return rows, all(r["material_sha256"] for r in rows)


def cmd_verify(snap: q.Snapshot, paths: list[str]) -> tuple[list[dict], bool]:
    rows, ok = [], True
    for record in paths:
        sources = q.parse_frontmatter(snap.text(record)).get("sources") or []
        if snap.read(record) is None:
            rows.append({"record": record, "path": None, "state": "record-missing"})
            ok = False
            continue
        for source in sources if isinstance(sources, list) else []:
            if not isinstance(source, dict) or not source.get("path"):
                rows.append({"record": record, "path": None, "state": "malformed"})
                ok = False
                continue
            actual = snap.sha(source["path"])
            recorded = source.get("content_sha256")
            material = source.get("material_sha256")
            state = q.source_state(snap, source["path"], recorded, source.get("revision"), material)
            ok &= state == "current"
            if material and q.WORK_ITEM_RE.match(source["path"]):
                recorded, actual = material, q.material_sha256(snap.read(source["path"]) or b"")
            rows.append({"record": record, "path": source["path"], "revision": source.get("revision"),
                         "basis": "material" if material and q.WORK_ITEM_RE.match(source["path"]) else "bytes",
                         "recorded": recorded, "actual": actual, "state": state})
    return rows, ok


def cmd_evidence(snap: q.Snapshot, paths: list[str], wanted: list[str]) -> tuple[list[dict], bool]:
    rows, ok = [], True
    for item in paths:
        text = snap.text(item)
        if snap.read(item) is None:
            rows.append({"item": item, "kind": "item-missing", "state": "missing"})
            ok = False
            continue
        material = q.material_sha256(snap.read(item))
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
            detail = "" if r["state"] in ("current", "malformed", "record-missing") else f" recorded={r['recorded']} actual={r['actual']}"
            basis = " (material)" if r.get("basis") == "material" else ""
            print(f"{r['state']:<8} {r['record']} -> {r['path']}{basis}{detail}")
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
    evidence = sub.add_parser("evidence")
    evidence.add_argument("paths", nargs="+")
    evidence.add_argument("--section", action="append", default=[], help="limit to a level-2 section; repeatable")
    args = parser.parse_args()
    q.utf8_stdio()

    snap = q.Snapshot()
    paths = expand(args.paths)
    if args.command == "evidence":
        rows, ok = cmd_evidence(snap, paths, args.section)
    else:
        rows, ok = {"files": cmd_files, "sources": cmd_sources, "material": cmd_material, "verify": cmd_verify}[args.command](snap, paths)
    if args.json:
        print(json.dumps({"command": args.command, "ok": ok, "rows": rows}, indent=2))
    else:
        print_text(args.command, rows)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
