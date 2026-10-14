#!/usr/bin/env python3
"""Collect deterministic runbook facts for the work-runbook-sync skill.

The script reads plans, work items, readiness records, and their recorded
sources once, then reports parsing, hashing, currentness, dependency, ordering,
and evidence facts. It never writes repository files and keeps no state between
runs. Judgments such as readiness coverage, synthetic gates, descriptions, and
the final command remain with the calling skill.

Usage:
  python .agents/skills/work-runbook-sync/scripts/runbook_facts.py SPEC-0008
  python ... SPEC-0008 --include SPEC-0007 --json
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "work"
ITEM_DIRS = ("decisions", "implementation")
ID_RE = re.compile(r"\b([DI]-\d{4}-\d{3})\b")
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
SPEC_DOC_RE = re.compile(r"^(SPEC\.md|specs/(components/)?[^/]+\.md)$")
ROW_RE = re.compile(r"^\|\s*(\d+(?:\.\d+)*)\s*\|(?:[^|\[]*\|)*?\s*\[([DI]-\d{4}-\d{3})\]\(([^)]+)\)")
PATH_HASH_ROW_RE = re.compile(r"^\|\s*`([^`]+)`[^|]*\|\s*`([0-9a-f]{64})`\s*\|")
PLANNING_ONLY_RE = re.compile(r"planning[- ]only|permits planning|authori[sz]es planning", re.I)
APPROVAL_RE = re.compile(r"approv", re.I)
EXPLICIT_APPROVAL_RE = re.compile(
    r"explicitly\s+approved|approved\s+explicitly|user\s+approved|approval\s+(?:was\s+)?(?:explicitly\s+)?(?:given|recorded)",
    re.I,
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


class Snapshot:
    """Reads each repository file once per run and retains its bytes and digest."""

    def __init__(self) -> None:
        self._bytes: dict[str, bytes | None] = {}
        self._sha: dict[str, str | None] = {}

    def read(self, path: str) -> bytes | None:
        if path not in self._bytes:
            file = ROOT / path
            self._bytes[path] = file.read_bytes() if file.is_file() else None
        return self._bytes[path]

    def text(self, path: str) -> str:
        data = self.read(path)
        return "" if data is None else data.decode("utf-8", errors="replace")

    def sha(self, path: str) -> str | None:
        if path not in self._sha:
            data = self.read(path)
            self._sha[path] = None if data is None else hashlib.sha256(data).hexdigest()
        return self._sha[path]


def unquote(value: str) -> str | None:
    value = value.strip()
    if value in ("null", "~"):
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict:
    """Parse the YAML subset used by work records: scalars, inline lists, and lists of scalars or maps."""
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {}
    data: dict = {}
    key = None
    current: dict | None = None
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        top = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if top:
            key, value = top.group(1), top.group(2).strip()
            current = None
            if value.startswith("[") and value.endswith("]"):
                data[key] = [unquote(v) for v in value[1:-1].split(",") if v.strip()]
            elif value == "":
                data[key] = []
            else:
                data[key] = unquote(value)
            continue
        item = re.match(r"^\s*-\s*(.*)$", raw)
        if item and key is not None and isinstance(data.get(key), list):
            pair = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", item.group(1))
            if pair:
                current = {pair.group(1): unquote(pair.group(2))}
                data[key].append(current)
            else:
                current = None
                data[key].append(unquote(item.group(1)))
            continue
        pair = re.match(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if pair and current is not None:
            current[pair.group(1)] = unquote(pair.group(2))
    return data


def sections(text: str) -> list[tuple[str, int, list[str]]]:
    """Return (heading, heading line number, body lines) for each level-2 section."""
    result: list[tuple[str, int, list[str]]] = []
    heading, start, lines = "", 0, []
    fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            result.append((heading, start, lines))
            heading, start, lines = line[3:].strip(), number, []
        else:
            lines.append(line)
    result.append((heading, start, lines))
    return result


def evidence_dates(lines: list[str], start: int) -> list[dict]:
    """Dates in paragraphs or list entries that mention approval."""
    found: list[dict] = []
    block: list[tuple[int, str]] = []

    def flush() -> None:
        joined = " ".join(text for _, text in block)
        if block and APPROVAL_RE.search(joined):
            explicit = bool(EXPLICIT_APPROVAL_RE.search(joined))
            for offset, text in block:
                found.extend(
                    {"date": d, "line": start + offset + 1, "explicit": explicit} for d in DATE_RE.findall(text)
                )
        block.clear()

    for offset, line in enumerate(lines):
        if not line.strip() or re.match(r"^\s*([-*+]|\d+\.)\s", line) or line.startswith("|"):
            flush()
        if line.strip():
            block.append((offset, line))
    flush()
    return found


def normalize_spec(value: str) -> str:
    value = value.strip().upper()
    return f"SPEC-{value}" if re.fullmatch(r"\d{4}", value) else value


def spec_dir(spec: str) -> Path | None:
    match = re.fullmatch(r"SPEC-(\d{4})", spec or "")
    return WORK / match.group(1) if match else None


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return result.stdout.rstrip() if result.returncode == 0 else ""


class Facts:
    def __init__(self, primary: str, included: list[str]) -> None:
        self.snap = Snapshot()
        self.used: set[str] = set()
        self.findings: list[str] = []
        self.primary = primary
        self.requested = [primary] + [s for s in included if s != primary]

    def use(self, path: str) -> None:
        # Runbooks are derived views, never source inputs to their own digest.
        if not path.endswith("/runbook.md"):
            self.used.add(path)

    def source_status(self, sources: list) -> list[dict]:
        result = []
        for source in sources if isinstance(sources, list) else []:
            if not isinstance(source, dict) or not source.get("path"):
                result.append({"path": None, "state": "malformed"})
                continue
            path = source["path"]
            self.use(path)
            actual = self.snap.sha(path)
            if actual is None:
                state = "missing"
            elif actual != source.get("content_sha256"):
                state = "stale"
            else:
                state = "current"
            result.append({"path": path, "state": state})
        return result

    def load_item(self, path: str) -> dict:
        text = self.snap.text(path)
        meta = parse_frontmatter(text)
        item = {
            "id": meta.get("id"),
            "path": path,
            "kind": meta.get("kind"),
            "granularity": meta.get("granularity"),
            "status": meta.get("status"),
            "spec": meta.get("spec"),
            "title": meta.get("title"),
            "depends_on": [d for d in meta.get("depends_on") or [] if d],
            "artifacts": [a for a in meta.get("artifacts") or [] if a],
            "findings": [],
            "slug": Path(path).stem[11:],
        }
        manifest = set(item["artifacts"])
        plan_approval: dict = {"state": "not-recorded"}
        review_dates: list[dict] = []
        other_dates: list[dict] = []
        for heading, start, lines in sections(text):
            lowered = heading.lower()
            if lowered.startswith("file and ownership manifest"):
                for line in lines:
                    if line.startswith("|"):
                        manifest.update(re.findall(r"`([^`\s]+)`", line))
            elif lowered == "plan approval":
                first = next((l.strip() for l in lines if l.strip()), "")
                rows = [(PATH_HASH_ROW_RE.match(l), n) for n, l in enumerate(lines)]
                mismatches = [
                    {"path": m.group(1), "line": start + n + 1}
                    for m, n in rows
                    if m and m.group(1) != path and not m.group(1).endswith("/runbook.md")
                    and self.snap.sha(m.group(1)) != m.group(2)
                ]
                dates = evidence_dates(lines, start)
                if first.lower().startswith("absent"):
                    plan_approval = {"state": "absent", "line": start}
                elif APPROVAL_RE.search(first):
                    plan_approval = {
                        "state": "recorded",
                        "line": start,
                        "date": dates[0]["date"] if dates else None,
                        "reviewed_hash_mismatches": mismatches,
                    }
                else:
                    plan_approval = {"state": "unknown", "line": start}
                other_dates.extend(dates)
            elif "review" in lowered or "approval" in lowered:
                review_dates.extend(evidence_dates(lines, start))
        item["plan_approval"] = plan_approval
        item["manifest_spec_docs"] = sorted(p for p in manifest if SPEC_DOC_RE.match(p))
        if item["status"] == "complete":
            candidates = review_dates or other_dates
            explicit = [d for d in candidates if d["explicit"]]
            latest = max(explicit or candidates, key=lambda d: d["date"]) if candidates else None
            item["completion_date"] = latest["date"] if latest else None
            item["completion_evidence_line"] = latest["line"] if latest else None
            item["completion_evidence_explicit"] = bool(explicit)
        if item["id"] and Path(path).name[:10] != item["id"]:
            item["findings"].append(f"id {item['id']} does not match file name {Path(path).name}")
        return item

    def load_plan(self, spec: str) -> dict | None:
        directory = spec_dir(spec)
        if directory is None or not (directory / "plan.md").is_file():
            return None
        path = rel(directory / "plan.md")
        self.use(path)
        text = self.snap.text(path)
        meta = parse_frontmatter(text)
        order: dict[str, tuple] = {}
        # Ordered rows belong to "## Phase" sections or to any H2 group's "### Ordered items" table.
        phase, in_phase, in_ordered = -1, False, False
        for line in text.splitlines():
            if line.startswith("## "):
                in_phase, in_ordered = line.startswith("## Phase"), False
                phase += 1
            elif line.startswith("### "):
                in_ordered = line.strip() == "### Ordered items"
            elif (in_phase or in_ordered) and (row := ROW_RE.match(line)):
                position = tuple(int(part) for part in row.group(1).split("."))
                order.setdefault(row.group(2), (phase, position))
        if meta.get("spec") != spec:
            self.findings.append(f"{path}: frontmatter spec {meta.get('spec')!r} does not match {spec}")
        return {"spec": spec, "path": path, "sources": self.source_status(meta.get("sources") or []), "order": order}

    def collect(self) -> dict:
        items: dict[str, dict] = {}
        for directory in sorted(p for p in WORK.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}", p.name)):
            for kind_dir in ITEM_DIRS:
                for file in sorted((directory / kind_dir).glob("*.md")):
                    item = self.load_item(rel(file))
                    if not item["id"]:
                        self.findings.append(f"{item['path']}: missing id")
                    elif item["id"] in items:
                        self.findings.append(f"duplicate id {item['id']}: {items[item['id']]['path']}, {item['path']}")
                    else:
                        items[item["id"]] = item

        plans: dict[str, dict | None] = {spec: self.load_plan(spec) for spec in self.requested}
        for spec, plan in plans.items():
            if plan is None:
                self.findings.append(f"{spec}: plan missing; requires `/work-plan-sync {spec}` gate")

        selected = {i for i, item in items.items() if item["spec"] in self.requested}
        pending = list(selected)
        while pending:
            for dep in items[pending.pop()]["depends_on"]:
                if dep in items and dep not in selected:
                    selected.add(dep)
                    pending.append(dep)
        transitive = sorted({items[i]["spec"] for i in selected} - set(self.requested))
        for spec in transitive:
            plans[spec] = self.load_plan(spec)

        for spec, plan in plans.items():
            if not plan:
                continue
            for item_id in plan["order"]:
                if item_id not in items:
                    self.findings.append(f"{plan['path']}: ordered item {item_id} has no record")
            if spec in self.requested:
                for item_id in sorted(i for i in selected if items[i]["spec"] == spec and i not in plan["order"]
                                      and items[i]["status"] != "cancelled"):
                    self.findings.append(f"{item_id}: not listed in {plan['path']} ordered-item tables")

        for item_id in sorted(selected):
            item = items[item_id]
            self.use(item["path"])
            item["deps_missing"] = [d for d in item["depends_on"] if d not in items]
            item["deps_cancelled"] = [d for d in item["depends_on"] if d in items and items[d]["status"] == "cancelled"]
            item["deps_incomplete"] = [
                d for d in item["depends_on"] if d in items and items[d]["status"] not in ("complete", "cancelled")
            ]
            item["deps_ready"] = not (item["deps_missing"] or item["deps_cancelled"] or item["deps_incomplete"])
            self.findings += [f"{item_id}: dependency {d} does not exist" for d in item["deps_missing"]]
            self.findings += [f"{item_id}: dependency {d} is cancelled" for d in item["deps_cancelled"]]
            self.findings += [f"{item_id}: {f}" for f in item["findings"]]
            for mismatch in item["plan_approval"].get("reviewed_hash_mismatches", []):
                self.use(mismatch["path"])

        spec_rank = {spec: n for n, spec in enumerate(self.requested + transitive)}

        def sort_key(item_id: str) -> tuple:
            item = items[item_id]
            plan = plans.get(item["spec"]) or {"order": {}}
            phase, position = plan["order"].get(item_id, (10_000, (10_000,)))
            return (spec_rank.get(item["spec"], 999), phase, position, item_id)

        indegree = {i: 0 for i in selected}
        dependents: dict[str, list[str]] = {i: [] for i in selected}
        for item_id in selected:
            for dep in items[item_id]["depends_on"]:
                if dep in selected:
                    indegree[item_id] += 1
                    dependents[dep].append(item_id)
        heap = [(sort_key(i), i) for i, n in indegree.items() if n == 0]
        heapq.heapify(heap)
        order: list[str] = []
        while heap:
            _, item_id = heapq.heappop(heap)
            order.append(item_id)
            for child in dependents[item_id]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    heapq.heappush(heap, (sort_key(child), child))
        cycle = sorted((i for i, n in indegree.items() if n > 0), key=sort_key)
        if cycle:
            self.findings.append("dependency cycle among: " + ", ".join(cycle))

        readiness: list[dict] = []
        for spec in self.requested + transitive:
            directory = spec_dir(spec)
            for file in sorted((directory / "readiness").glob("*.md")) if directory else []:
                path = rel(file)
                self.use(path)
                text = self.snap.text(path)
                meta = parse_frontmatter(text)
                sources = self.source_status(meta.get("sources") or [])
                readiness.append({
                    "path": path,
                    "spec": meta.get("spec"),
                    "scope": meta.get("scope"),
                    "assessment": meta.get("assessment"),
                    "stale_sources": [f"{s['path']}({s['state']})" for s in sources if s["state"] != "current"],
                    "planning_only_language": bool(PLANNING_ONLY_RE.search(text)),
                    "_source_paths": {s["path"] for s in sources if s["path"]},
                    "_mentions": set(ID_RE.findall(text)),
                })

        for item_id in order + cycle:
            item = items[item_id]
            if item["kind"] != "implementation":
                continue
            candidates = []
            for record in readiness:
                by_scope = record["scope"] in (f"{item['slug']}-implementation", item["slug"])
                if by_scope or item_id in record["_mentions"]:
                    candidates.append({
                        "path": record["path"],
                        "scope": record["scope"],
                        "match": "scope" if by_scope else "mention",
                        "assessment": record["assessment"],
                        "current": not record["stale_sources"],
                        "uncovered_manifest_spec_docs": [
                            d for d in item["manifest_spec_docs"] if d not in record["_source_paths"]
                        ],
                        "planning_only_language": record["planning_only_language"],
                    })
            item["readiness_candidates"] = candidates

        digest = hashlib.sha256()
        for path in sorted(self.used):
            digest.update(f"{path}\n{self.snap.sha(path) or 'MISSING'}\n".encode("utf-8"))
        status = git("status", "--porcelain=v1", "--untracked-files=all", "--", *sorted(self.used))
        runbook_path = f"work/{self.primary.split('-')[-1]}/runbook.md"
        runbook_file = ROOT / runbook_path
        runbook_meta = parse_frontmatter(runbook_file.read_text(encoding="utf-8")) if runbook_file.is_file() else {}

        hidden = ("artifacts", "slug", "findings", "depends_on")
        return {
            "primary": self.primary,
            "included": self.requested[1:],
            "transitive_owners": transitive,
            "branch": git("branch", "--show-current"),
            "head": git("rev-parse", "HEAD"),
            "source_file_count": len(self.used),
            "source_set_sha256": digest.hexdigest(),
            "source_set_rule": "SHA-256 over sorted lines '<repository-relative path>\\n<SHA-256 of exact bytes or MISSING>\\n'",
            "working_copy_inputs": sorted(line[3:] for line in status.splitlines()),
            "runbook": {
                "path": runbook_path,
                "exists": runbook_file.is_file(),
                "recorded_source_set_sha256": runbook_meta.get("source_set_sha256"),
                "inputs_unchanged": runbook_meta.get("source_set_sha256") == digest.hexdigest(),
            },
            "plans": [
                {"spec": p["spec"], "path": p["path"],
                 "stale_sources": [f"{s['path']}({s['state']})" for s in p["sources"] if s["state"] != "current"]}
                for p in plans.values() if p
            ],
            "readiness": [{k: v for k, v in r.items() if not k.startswith("_")} for r in readiness],
            "items": [
                {k: v for k, v in items[i].items() if k not in hidden} | {"depends_on": items[i]["depends_on"]}
                for i in order + cycle
            ],
            "cycle": cycle,
            "findings": self.findings,
        }


def print_text(facts: dict) -> None:
    rb = facts["runbook"]
    print(f"primary={facts['primary']} included={facts['included']} transitive_owners={facts['transitive_owners']}")
    print(f"branch={facts['branch']} head={facts['head']}")
    print(f"source_file_count={facts['source_file_count']} source_set_sha256={facts['source_set_sha256']}")
    print(f"source_set_rule: {facts['source_set_rule']}")
    print(f"runbook={rb['path']} exists={rb['exists']} recorded_digest_matches={rb['inputs_unchanged']}")
    print(f"working_copy_inputs: {', '.join(facts['working_copy_inputs']) or 'none'}")
    print("\n# Plans")
    for plan in facts["plans"]:
        print(f"{plan['spec']} {plan['path']} sources: {', '.join(plan['stale_sources']) or 'all current'}")
    print("\n# Readiness records")
    for r in facts["readiness"]:
        flag = " | planning-only-language" if r["planning_only_language"] else ""
        print(f"{r['path']} | scope={r['scope']} | assessment={r['assessment']} | sources: {', '.join(r['stale_sources']) or 'all current'}{flag}")
    print("\n# Items in stable dependency order")
    print("id | status | kind/granularity | dependencies | title")
    for item in facts["items"]:
        waiting = item["deps_incomplete"] + [f"{d}(missing)" for d in item["deps_missing"]] + [f"{d}(cancelled)" for d in item["deps_cancelled"]]
        deps = "ready" if item["deps_ready"] else "waiting " + ",".join(waiting)
        line = f"{item['id']} | {item['status']} | {item['kind']}/{item['granularity'] or '-'} | {deps} | {item['title']}"
        if item["status"] == "complete":
            date = item.get("completion_date")
            weak = "" if item.get("completion_evidence_explicit") else ", confirm: no explicit approval wording"
            line += f" | completed {date} (evidence L{item['completion_evidence_line']}{weak})" if date else " | completed Unknown - evidence missing"
        line += f"\n    path {item['path']}"
        if item["depends_on"]:
            line += f"\n    depends_on {', '.join(item['depends_on'])}"
        if item["kind"] == "implementation" and item["status"] not in ("complete", "cancelled"):
            pa = item["plan_approval"]
            detail = f" {pa['date']}" if pa.get("date") else ""
            changed = ", ".join(m["path"] for m in pa.get("reviewed_hash_mismatches", []))
            line += f"\n    plan-approval {pa['state']}{detail} (L{pa.get('line', '-')})" + (f" reviewed-hashes-changed: {changed}" if changed else "")
            if item["manifest_spec_docs"]:
                line += f"\n    manifest-spec-edits {', '.join(item['manifest_spec_docs'])}"
            for c in item.get("readiness_candidates", []):
                flag = " planning-only-language" if c["planning_only_language"] else ""
                gaps = ", ".join(c["uncovered_manifest_spec_docs"]) or "none"
                line += (f"\n    readiness {c['path']} [{c['match']}] assessment={c['assessment']} "
                         f"current={c['current']} uncovered-spec-edits={gaps}{flag}")
        print(line)
    print("\n# Structural findings")
    for finding in facts["findings"] or ["none"]:
        print(f"- {finding}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect deterministic work-runbook facts.")
    parser.add_argument("primary", help="primary specification, for example SPEC-0008")
    parser.add_argument("--include", default="", help="comma-separated additional specifications")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of compact text")
    args = parser.parse_args()
    included = [normalize_spec(s) for s in args.include.split(",") if s.strip()]
    facts = Facts(normalize_spec(args.primary), included).collect()
    if args.json:
        json.dump(facts, sys.stdout, indent=1)
        print()
    else:
        print_text(facts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
