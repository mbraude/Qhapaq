#!/usr/bin/env python3
"""Collect deterministic runbook facts for the work-runbook-sync skill.

The script reads plans, work items, readiness records, and their recorded
sources once, then reports parsing, hashing, currentness, dependency, ordering,
and evidence facts. It keeps no state between runs. Only `--write` writes a
file: the runbook itself, rendered deterministically from these facts, the
suggested commands and gates that the facts fully determine, and the calling
skill's overrides. When selected plans are stale and no overrides are given it
emits `SYNC` gates and blocks every open row.

Usage:
  python .agents/skills/work-runbook-sync/scripts/runbook_facts.py SPEC-0008 --judgments-template --out FILE
  python ... SPEC-0008 --write [--judgments FILE|-]
  python ... SPEC-0008 --open
  python ... SPEC-0008 --include SPEC-0007 --check
"""

from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))

from qhapaq_work import (  # noqa: E402
    GUIDE,
    PATH_HASH_ROW_RE,
    ROOT,
    WORK,
    Snapshot,
    git,
    parse_frontmatter,
    process_state,
    rel,
    sections,
    source_kind,
    source_material_sha256,
    source_state,
    utf8_stdio,
)

ITEM_DIRS = ("decisions", "implementation")
ID_RE = re.compile(r"\b([DI]-\d{4}-\d{3})\b")
REQ_RE = re.compile(r"\bR-\d{4}-\d{3}\b")
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
SPEC_DOC_RE = re.compile(r"^(SPEC\.md|specs/(components/)?[^/]+\.md)$")
ROW_RE = re.compile(r"^\|\s*(\d+(?:\.\d+)*)\s*\|(?:[^|\[]*\|)*?\s*\[([DI]-\d{4}-\d{3})\]\(([^)]+)\)")
PLANNING_ONLY_RE = re.compile(r"planning[- ]only|permits planning|authori[sz]es planning", re.I)
# A sentence describing another or an older record is not this record's own limitation.
OTHER_RECORD_RE = re.compile(r"\b(?:earlier|older|previous|prior|former|historical|existing|superseded)\b", re.I)
SENTENCE_END_RE = re.compile(r"(?<=[.!?;])\s+")
AUTHORIZES = ("implementation", "planning")
APPROVAL_RE = re.compile(r"approv", re.I)
EXPLICIT_APPROVAL_RE = re.compile(
    r"explicitly\s+approved|approved\s+explicitly|user\s+approved|approval\s+(?:was\s+)?(?:explicitly\s+)?(?:given|recorded)",
    re.I,
)


def planning_limit(text: str, authorizes, other_scopes: set[str]) -> str | None:
    """Why a readiness record may authorize planning only, or None.

    An explicit `authorizes` field decides. Otherwise a heuristic flags sentences with
    planning-only language, skipping sentences about another or an older record.
    """
    if authorizes is not None:
        return None if authorizes == "implementation" else f"authorizes: {authorizes}"
    paragraph: list[tuple[int, str]] = []
    paragraphs: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip():
            paragraph.append((number, line.strip()))
        elif paragraph:
            paragraphs.append((paragraph[0][0], " ".join(t for _, t in paragraph)))
            paragraph = []
    if paragraph:
        paragraphs.append((paragraph[0][0], " ".join(t for _, t in paragraph)))
    for number, body in paragraphs:
        for sentence in SENTENCE_END_RE.split(body):
            if not PLANNING_ONLY_RE.search(sentence) or OTHER_RECORD_RE.search(sentence):
                continue
            if any(f"`{scope}`" in sentence for scope in other_scopes):
                continue
            return f"L{number}: {sentence[:160]}"
    return None


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

    def source_status(self, sources: list, process_version=False) -> list[dict]:
        result = []
        if process_version is not False:
            self.use(GUIDE)
            state = process_state(self.snap, process_version)
            if state != "current":
                result.append({"path": "process_version", "state": state})
        for source in sources if isinstance(sources, list) else []:
            if not isinstance(source, dict) or not source.get("path"):
                result.append({"path": None, "state": "malformed"})
                continue
            path = source["path"]
            kind = source_kind(path)
            if kind in ("derived-view", "reconciliation-record"):
                result.append({"path": path, "state": kind})
                continue
            self.use(path)
            state = source_state(self.snap, path, source.get("content_sha256"), source.get("revision"),
                                 source.get("material_sha256"))
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
            "requirements": [r for r in meta.get("requirements") or [] if r],
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
                mismatches = []
                for match, offset in rows:
                    if not match or match.group(1) == path or match.group(1).endswith("/runbook.md"):
                        continue
                    dependency, basis, recorded = match.group(1), (match.group(2) or "bytes").lower(), match.group(3)
                    actual = (source_material_sha256(dependency, self.snap.read(dependency))
                              if basis == "material" and self.snap.read(dependency) is not None
                              else self.snap.sha(dependency) if basis == "bytes" else None)
                    if actual != recorded:
                        mismatches.append({"path": dependency, "line": start + offset + 1})
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
        return {"spec": spec, "path": path, "order": order,
                "sources": self.source_status(meta.get("sources") or [], meta.get("process_version"))}

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
                sources = self.source_status(meta.get("sources") or [], meta.get("process_version"))
                readiness.append({
                    "path": path,
                    "spec": meta.get("spec"),
                    "scope": meta.get("scope"),
                    "assessment": meta.get("assessment"),
                    "authorizes": meta.get("authorizes"),
                    "stale_sources": [f"{s['path']}({s['state']})" for s in sources if s["state"] != "current"],
                    "_text": text,
                    "_source_paths": {s["path"] for s in sources if s["path"]},
                    "_mentions": set(ID_RE.findall(text)),
                    "_requirements": set(REQ_RE.findall(text)),
                })
        scopes = {r["scope"] for r in readiness if r["scope"]}
        for record in readiness:
            excerpt = planning_limit(record.pop("_text"), record["authorizes"], scopes - {record["scope"]})
            record["planning_only_language"] = excerpt is not None
            record["planning_only_excerpt"] = excerpt

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
                        "stale_sources": record["stale_sources"],
                        "uncovered_manifest_spec_docs": [
                            d for d in item["manifest_spec_docs"] if d not in record["_source_paths"]
                        ],
                        "unmentioned_requirements": [
                            r for r in item["requirements"] if r not in record["_requirements"]
                        ],
                        "planning_only_language": record["planning_only_language"],
                        "planning_only_excerpt": record["planning_only_excerpt"],
                    })
            item["readiness_candidates"] = candidates

        paths = {item["path"]: item_id for item_id, item in items.items()}
        for item_id in selected:
            item = items[item_id]
            item["child_items"] = sorted(paths[a] for a in item["artifacts"] if a in paths and paths[a] != item_id)

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


def print_text(facts: dict, open_only: bool = False) -> None:
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
    omitted = 0
    for item in facts["items"]:
        settled = item["status"] == "cancelled" or (
            item["status"] == "complete" and item.get("completion_date") and item.get("completion_evidence_explicit"))
        if open_only and settled:
            omitted += 1
            continue
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
                line += (f"\n    readiness {c['scope']} [{c['match']}] assessment={c['assessment']} "
                         f"current={c['current']} uncovered-spec-edits={gaps}{flag}")
        print(line)
    if omitted:
        print(f"({omitted} settled complete/cancelled items omitted; `--rows` prints their exact table rows)")
    print("\n# Structural findings")
    for finding in facts["findings"] or ["none"]:
        print(f"- {finding}")


SETTLED_STATUS = {"complete": "Complete", "cancelled": "Cancelled"}
TABLE_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
ITEM_CELL_RE = re.compile(r"^\[([DI]-\d{4}-\d{3})\]\(([^)]+)\)$")
COMMAND_RE = re.compile(r"`(/[a-z0-9-]+)(?:\s[^`]*)?`")


def cell(text: str) -> str:
    return (text or "").replace("|", "\\|").strip()


def item_link(item: dict, base: str = "") -> str:
    target = os.path.relpath(item["path"], base).replace(os.sep, "/") if base else item["path"]
    return f"[{item['id']}]({target})"


def resolve_link(target: str, base: str) -> str:
    """Accept runbook-relative links, and repository-root links used by older runbooks."""
    target = target.split("#")[0]
    relative = os.path.normpath(os.path.join(base, target)).replace(os.sep, "/")
    return relative if (ROOT / relative).exists() or not (ROOT / target).exists() else target


def item_row(item: dict, by_id: dict[str, dict], base: str = "") -> str:
    """Exact row for a settled item; placeholder command and status cells for open items."""
    prereqs = "<br>".join(item_link(by_id[d], base) if d in by_id else f"`{d}` (missing)" for d in item["depends_on"]) or "—"
    if item["status"] == "complete":
        command, status, date = "", "Complete", item.get("completion_date") or "Unknown - evidence missing"
    elif item["status"] == "cancelled":
        command, status, date = "", "Cancelled", "—"
    else:
        command, status, date = "<command>", "<status>", "—"
    return f"| {item_link(item, base)} | {cell(item['title'])} | {command} | {status} | {date} | {prereqs} |"


def print_rows(facts: dict) -> None:
    base = os.path.dirname(facts["runbook"]["path"])
    by_id = {item["id"]: item for item in facts["items"]}
    print("| Work item | Description | Skill command | Status | Date Completed | Pre-requisites / blocked by |")
    print("| --- | --- | --- | --- | --- | --- |")
    for item in facts["items"]:
        print(item_row(item, by_id, base))


def split_row(line: str) -> list[str]:
    cells = re.split(r"(?<!\\)\|", line.strip())
    return [c.strip() for c in cells[1:-1]]


def normalize_links(cells: list[str], base: str) -> list[str]:
    return [TABLE_LINK_RE.sub(lambda m: m.group(0).replace(m.group(1), resolve_link(m.group(1), base)), c) for c in cells]


def check_runbook(facts: dict) -> list[str]:
    """Structural validation of the existing runbook against current facts."""
    path = facts["runbook"]["path"]
    base = os.path.dirname(path)
    file = ROOT / path
    if not file.is_file():
        return [f"{path}: missing"]
    text = file.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    problems: list[str] = []
    if meta.get("source_set_sha256") != facts["source_set_sha256"]:
        problems.append(f"source_set_sha256 {meta.get('source_set_sha256')} != current {facts['source_set_sha256']} (inputs changed; refresh required)")
    if str(meta.get("source_file_count")) != str(facts["source_file_count"]):
        problems.append(f"source_file_count {meta.get('source_file_count')} != current {facts['source_file_count']}")
    for key, expected in (("primary_spec", facts["primary"]),):
        if meta.get(key) != expected:
            problems.append(f"{key} {meta.get(key)!r} != {expected!r}")

    by_id = {item["id"]: item for item in facts["items"]}
    rows: list[tuple[int, list[str], str]] = []
    in_table = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("| Work item |"):
            in_table = True
            continue
        if in_table and line.startswith("|"):
            if not line.startswith("| ---"):
                rows.append((number, normalize_links(split_row(line), base), line))
        elif in_table:
            in_table = False

    seen: dict[str, int] = {}
    commands: set[str] = set()
    for number, cells, line in rows:
        if len(cells) != 6:
            problems.append(f"L{number}: expected 6 columns, found {len(cells)}")
            continue
        commands.update(m.group(0) for m in COMMAND_RE.finditer(cells[2]))
        for target in TABLE_LINK_RE.findall(line):
            if not (ROOT / resolve_link(target, base)).exists():
                problems.append(f"L{number}: link target {target} does not exist")
        match = ITEM_CELL_RE.match(cells[0])
        if not match:
            continue
        item_id, link = match.groups()
        if item_id in seen:
            problems.append(f"L{number}: {item_id} duplicates row L{seen[item_id]}")
            continue
        seen[item_id] = number
        item = by_id.get(item_id)
        if item is None:
            problems.append(f"L{number}: {item_id} is not in the selected scope")
            continue
        if link != item["path"]:
            problems.append(f"L{number}: {item_id} links {link}, expected {item['path']}")
        if item["status"] in SETTLED_STATUS:
            expected = normalize_links(split_row(item_row(item, by_id)), "")
            empty = {"", "—", "-", "None"}
            mismatched = [
                name for name, ok in (
                    ("command", cells[2] in empty),
                    ("status", cells[3] == expected[3]),
                    ("date", cells[4] == expected[4] or (expected[4] == "—" and cells[4] in empty)),
                    ("prerequisites", sorted(ID_RE.findall(cells[5])) == sorted(ID_RE.findall(expected[5]))),
                ) if not ok
            ]
            if mismatched:
                problems.append(f"L{number}: {item_id} settled row differs in {', '.join(mismatched)}; expected:\n      {item_row(item, by_id, base)}")
        else:
            if cells[3].split(" ")[0] in SETTLED_STATUS.values():
                problems.append(f"L{number}: {item_id} has persisted status {item['status']} but row says {cells[3]!r}")
            for dep in item["deps_incomplete"]:
                if dep not in cells[5]:
                    problems.append(f"L{number}: {item_id} omits incomplete prerequisite {dep}")
        for dep in item["depends_on"]:
            if dep in seen or dep not in by_id:
                continue
            problems.append(f"L{number}: {item_id} precedes its prerequisite {dep}")
    for item_id in by_id:
        if item_id not in seen:
            problems.append(f"{item_id}: no runbook row")

    skills = {p.name for p in (ROOT / ".agents" / "skills").iterdir() if p.is_dir()}
    for command in sorted(commands):
        problems += command_problems("runbook", command, by_id, skills)
    next_match = re.search(r"^\*\*Next command:\*\*\s*(.+)$", text, re.M)
    if not next_match:
        problems.append("missing **Next command:** line")
    else:
        value = next_match.group(1).strip()
        if value not in ("None", "`None`") and value not in commands:
            problems.append(f"Next command {value} does not appear in any row's Skill command cell")
    also = re.search(r"^\*\*Also eligible:\*\*\s*(.+)$", text, re.M)
    if also:
        for command in COMMAND_RE.finditer(also.group(1)):
            if command.group(0) not in commands:
                problems.append(f"Also eligible {command.group(0)} does not appear in any row's Skill command cell")
    return problems


def spec_arg(spec: str) -> str:
    return spec.split("-", 1)[1] if spec.startswith("SPEC-") else spec


def stale_plan_gates(facts: dict) -> list[dict]:
    """Deterministic `SYNC` gates for selected plans that are missing or record non-current sources."""
    gates = []
    present = {p["spec"] for p in facts["plans"]}
    for spec in [facts["primary"], *facts["included"], *facts["transitive_owners"]]:
        plan = next((p for p in facts["plans"] if p["spec"] == spec), None)
        if plan is None and spec not in present:
            reason = "Plan is missing."
        elif plan and plan["stale_sources"]:
            reason = f"`{plan['path']}` records non-current sources: " + ", ".join(f"`{s}`" for s in plan["stale_sources"])
        else:
            continue
        role = "transitive prerequisite" if spec in facts["transitive_owners"] else "selected"
        gates.append({"id": f"SYNC {spec}", "description": f"Reconcile the {role} plan against its current sources.",
                      "command": f"/work-plan-sync {spec_arg(spec)}", "status": "Gate - refresh required",
                      "blockers": [reason], "before": None})
    return gates


def open_items(facts: dict) -> list[dict]:
    return [i for i in facts["items"] if i["status"] not in SETTLED_STATUS]


JUDGE = {"command": "<judge>", "status": "<judge>", "blockers": []}


def readiness_gate(item: dict, scope: str, command: str, status: str, reason: str) -> dict:
    spec = item["spec"]
    covers = ", ".join(item["requirements"]) or "its governing requirements"
    edits = ", ".join(item["manifest_spec_docs"])
    return {
        "id": f"READINESS {spec} {scope}",
        "before": item["id"],
        "description": f"{reason} implementation readiness for {item['id']} covering {covers}"
                       + (f" and planned edits to {edits}" if edits else "") + ".",
        "command": command,
        "status": status,
        "blockers": [],
    }


def suggest(item: dict, by_id: dict[str, dict]) -> tuple[dict, list[dict]]:
    """Deterministic row suggestion plus any gates it needs, or `<judge>` where the skill must decide.

    Implements the work-runbook-sync command table for the cases the facts fully determine;
    every other case is left to the skill's judgment.
    """
    spec = spec_arg(item["spec"] or "")
    if not item["deps_ready"]:
        return {"command": "", "status": "Open - blocked", "blockers": []}, []
    if item["status"] == "ready-for-review":
        return {"command": f"/approve {item['id']}", "status": "Ready for review", "blockers": []}, []
    if item["kind"] == "decision":
        return {"command": f"/spec-next {spec} item={item['id']}", "status": "Open - ready", "blockers": []}, []
    if item["kind"] != "implementation" or item["status"] != "open":
        return dict(JUDGE), []
    if item["granularity"] == "milestone":
        if item.get("child_items"):
            return dict(JUDGE), []  # aggregate milestone whose slices exist: awaiting verification
        return {"command": f"/implementation-plan {spec} item={item['id']}", "status": "Open - ready",
                "blockers": [], "basis": "milestone without planned child slices"}, []
    if item["granularity"] != "slice":
        return dict(JUDGE), []
    candidates = item.get("readiness_candidates", [])
    scoped = [c for c in candidates if c["match"] == "scope"]
    if not candidates:
        scope = f"{item['slug']}-implementation"
        gate = readiness_gate(item, scope, f"/spec-readiness {spec} scope={scope}",
                              "Gate - assessment required", "Assess")
        return {"command": "", "status": "Open - blocked", "blockers": [gate["id"]],
                "basis": "no readiness record names or mentions this slice"}, [gate]
    if len(scoped) != 1:
        return dict(JUDGE), []
    record = scoped[0]
    blocked = {"command": "", "status": "Open - blocked", "blockers": []}
    pa = item["plan_approval"]
    renew = ["Existing plan approval has changed reviewed hashes and must be renewed after readiness is current."] \
        if pa.get("reviewed_hash_mismatches") else []
    if not record["current"] or record["assessment"] == "not-assessed":
        gate = readiness_gate(item, record["scope"], f"/spec-readiness {spec} scope={record['scope']}",
                              "Gate - reassessment required" if not record["current"] else "Gate - assessment required",
                              "Reassess" if not record["current"] else "Assess")
        if not record["current"]:
            gate["blockers"] = ["Non-current sources: " + ", ".join(record["stale_sources"])]
        blocked["blockers"] = [gate["id"], *renew]
        blocked["basis"] = f"{record['path']} is {'stale' if not record['current'] else 'not assessed'}"
        return blocked, [gate]
    if record["assessment"] == "ready-for-review":
        gate = readiness_gate(item, record["scope"], f"/approve {record['path']}", "Gate - ready for review", "Approve")
        blocked["blockers"] = [gate["id"], *renew]
        blocked["basis"] = f"{record['path']} awaits approval"
        return blocked, [gate]
    if record["assessment"] == "blocked":
        gate = readiness_gate(item, record["scope"], f"/spec-readiness {spec} scope={record['scope']}",
                              "Gate - blocked", "Resolve the recorded blockers and reassess")
        gate["blockers"] = [f"{record['path']} records assessment: blocked"]
        blocked["blockers"] = [gate["id"], *renew]
        blocked["basis"] = f"{record['path']} is current but blocked"
        return blocked, [gate]
    if (record["assessment"] != "approved" or record["uncovered_manifest_spec_docs"]
            or record["unmentioned_requirements"] or record["planning_only_language"]):
        return dict(JUDGE), []
    if pa["state"] == "recorded" and not pa.get("reviewed_hash_mismatches"):
        command, basis = f"/implement-next {spec} item={item['id']}", "readiness current and approved; plan approved"
    else:
        command, basis = f"/approve-implementation-plan {spec} item={item['id']}", \
            "readiness current, approved, and covers requirements and spec edits; plan approval " \
            + ("has changed reviewed hashes" if pa.get("reviewed_hash_mismatches") else pa["state"])
    return {"command": command, "status": "Open - ready", "blockers": [], "basis": basis}, []


def judge_hints(item: dict) -> dict:
    pa = item["plan_approval"]
    candidates = item.get("readiness_candidates", [])
    if any(c["match"] == "scope" for c in candidates):
        candidates = [c for c in candidates if c["match"] == "scope"]
    return {
        "granularity": item["granularity"],
        "requirements": item["requirements"],
        "child_items": item.get("child_items", []),
        "plan_approval": pa["state"] + (f" {pa['date']}" if pa.get("date") else ""),
        "reviewed_hashes_changed": [m["path"] for m in pa.get("reviewed_hash_mismatches", [])],
        "manifest_spec_edits": item["manifest_spec_docs"],
        "readiness": [
            f"{c['path']} scope={c['scope']} [{c['match']}] assessment={c['assessment']} current={c['current']}"
            + (f" stale={brief(c['stale_sources'])}" if c["stale_sources"] else "")
            + (f" uncovered_edits={','.join(c['uncovered_manifest_spec_docs'])}" if c["uncovered_manifest_spec_docs"] else "")
            + (f" unmentioned_requirements={','.join(c['unmentioned_requirements'])}" if c["unmentioned_requirements"] else "")
            + (f" planning-only-language {c['planning_only_excerpt']!r}" if c["planning_only_language"] else "")
            for c in candidates
        ],
    }


def brief(values: list[str], limit: int = 3) -> str:
    return ",".join(values[:limit]) + (f",+{len(values) - limit} more" if len(values) > limit else "")


def judgments_template(facts: dict) -> dict:
    by_id = {item["id"]: item for item in facts["items"]}
    items, gates = {}, []
    for item in open_items(facts):
        entry, item_gates = suggest(item, by_id)
        if entry["command"] == "<judge>":
            entry["hints"] = judge_hints(item)
        items[item["id"]] = entry
        gates += [g for g in item_gates if g["id"] not in {x["id"] for x in gates}]
    return {
        "_usage": "Suggestions follow the skill's command table; override only what you judge differently. "
                  "Pass only overrides with --write --judgments FILE|-: listed items merge over suggestions, "
                  "listed gates replace same-id suggested gates, and {\"id\": ..., \"drop\": true} removes one. "
                  "SYNC gates for stale plans are added automatically.",
        "auto_gates": [g["id"] for g in stale_plan_gates(facts)],
        "items": items,
        "gates": gates,
        "notes": "",
    }


def normalize_overrides(raw) -> dict:
    """Validate the override shape; a list of `{"id": ...}` items is accepted as the mapping form."""
    if not isinstance(raw, dict):
        raise ValueError('expected a JSON object such as {"items": {...}, "gates": [...]}')
    result = dict(raw)
    items = result.get("items") or {}
    if isinstance(items, list):
        if not all(isinstance(e, dict) and e.get("id") for e in items):
            raise ValueError('"items" must map item IDs to entries, or list entries that each have an "id"')
        items = {e["id"]: {k: v for k, v in e.items() if k != "id"} for e in items}
    if not isinstance(items, dict) or not all(isinstance(v, dict) for v in items.values()):
        raise ValueError('"items" must map item IDs to objects such as {"command": ..., "status": ...}')
    gates = result.get("gates") or []
    if not isinstance(gates, list) or not all(isinstance(g, dict) and g.get("id") for g in gates):
        raise ValueError('"gates" must be a list of objects that each have an "id"')
    for key in ("next", "also"):
        if key in result and not isinstance(result[key], (str, list, type(None))):
            raise ValueError(f'"{key}" must be a string or list')
    result["items"], result["gates"] = items, gates
    return result


def effective_judgments(facts: dict, overrides: dict | None) -> dict:
    """Suggestions overlaid with the skill's overrides; overrides win field by field."""
    result = judgments_template(facts)
    overrides = overrides or {}
    for item_id, entry in (overrides.get("items") or {}).items():
        if isinstance(entry, dict):
            base = {k: v for k, v in result["items"].get(item_id, {}).items() if k != "hints"}
            result["items"][item_id] = base | entry
        else:
            result["items"][item_id] = entry
    gates = {g["id"]: g for g in result["gates"]}
    for gate in overrides.get("gates") or []:
        if gate.get("drop"):
            gates.pop(gate.get("id"), None)
        else:
            gates[gate.get("id")] = gate
    result["gates"] = list(gates.values())
    for key in ("next", "also", "scope", "notes"):
        if overrides.get(key):
            result[key] = overrides[key]
    return result


def command_problems(name: str, command: str, by_id: dict[str, dict], skills: set[str]) -> list[str]:
    """Skill exists; `item=<id>` names a selected item and the command's spec argument is that item's spec."""
    tokens = command.strip("`").split()
    if not tokens or not tokens[0].startswith("/") or tokens[0][1:] not in skills:
        return [f"{name}: command {command!r} names an unknown skill"]
    problems = []
    for token in tokens[1:]:
        if token.startswith("item="):
            target = by_id.get(token[5:])
            if target is None:
                problems.append(f"{name}: command {command!r} names unknown item {token[5:]}")
            elif len(tokens) < 3 or tokens[1] != spec_arg(target["spec"] or ""):
                problems.append(f"{name}: command {command!r} must name spec {spec_arg(target['spec'] or '')} for {token[5:]}")
    return problems


def template_summary(template: dict, facts: dict) -> str:
    lines = [f"plans with non-current sources: {', '.join(template['auto_gates']) or 'none'}"]
    if facts["findings"]:
        lines.append("structural findings: " + "; ".join(facts["findings"]))
    if facts["cycle"]:
        lines.append("dependency cycle: " + ", ".join(facts["cycle"]))
    lines.append(f"working-copy inputs: {', '.join(facts['working_copy_inputs']) or 'none'}")
    lines.append(f"runbook inputs unchanged: {facts['runbook']['inputs_unchanged']}")
    judge = [i for i, e in template["items"].items() if e.get("command") == "<judge>"]
    lines.append(f"open rows: {len(template['items'])}; <judge>: {', '.join(judge) or 'none'}")
    for gate in template["gates"]:
        lines.append(f"gate {gate['id']} -> {gate['command']} [{gate['status']}] before {gate['before']}")
    for item_id, entry in template["items"].items():
        if entry.get("command") == "<judge>":
            hints = entry["hints"]
            lines.append(f"{item_id} <judge> {hints['granularity']} plan_approval={hints['plan_approval']}"
                         + (f" reviewed_hashes_changed={brief(hints['reviewed_hashes_changed'])}" if hints["reviewed_hashes_changed"] else "")
                         + (f" child_items={','.join(hints['child_items'])}" if hints["child_items"] else "")
                         + (f" spec_edits={','.join(hints['manifest_spec_edits'])}" if hints["manifest_spec_edits"] else ""))
            lines += [f"    readiness {r}" for r in hints["readiness"]]
        elif entry.get("command") or entry.get("blockers"):
            lines.append(f"{item_id} {entry.get('command') or '-'} [{entry['status']}]"
                         + (f" blockers={'; '.join(entry['blockers'])}" if entry.get("blockers") else "")
                         + (f" ({entry['basis']})" if entry.get("basis") else ""))
    blocked = sum(1 for e in template["items"].values() if e.get("status") == "Open - blocked" and not e.get("blockers"))
    lines.append(f"{blocked} further rows are blocked only by incomplete prerequisites")
    return "\n".join(lines)


def render_runbook(facts: dict, judgments: dict | None) -> tuple[str, list[str]]:
    """Complete runbook text, or errors when judgments are incomplete or malformed."""
    base = os.path.dirname(facts["runbook"]["path"])
    by_id = {item["id"]: item for item in facts["items"]}
    skills = {p.name for p in (ROOT / ".agents" / "skills").iterdir() if p.is_dir()}
    sync = stale_plan_gates(facts)
    errors: list[str] = []
    gate_mode = judgments is None and bool(sync)
    if gate_mode:
        judgments = {"items": {i["id"]: {"command": "", "status": "Open - blocked",
                                         "blockers": ["Blocked until stale plan sources are synchronized."]}
                               for i in open_items(facts)}, "gates": []}
    else:
        judgments = effective_judgments(facts, judgments)
    item_judgments: dict = judgments.get("items") or {}
    gates = sync + list(judgments.get("gates") or [])
    for item in open_items(facts):
        entry = item_judgments.get(item["id"])
        if not isinstance(entry, dict):
            errors.append(f"{item['id']}: missing judgment")
        elif "<judge>" in (entry.get("command"), entry.get("status")) or not entry.get("status"):
            errors.append(f"{item['id']}: unresolved command or status")
    for key in item_judgments:
        if key not in by_id or by_id[key]["status"] in SETTLED_STATUS:
            errors.append(f"{key}: judgment for an item that is not an open row")
    for gate in gates:
        if not gate.get("id") or not gate.get("status"):
            errors.append(f"gate {gate.get('id')!r}: id and status are required")
        if gate.get("before") and gate["before"] not in by_id:
            errors.append(f"gate {gate.get('id')}: before {gate['before']} is not a runbook row")
    for name, entry in [(g.get("id"), g) for g in gates] + list(item_judgments.items()):
        command = entry.get("command") or "" if isinstance(entry, dict) else ""
        if command and command != "<judge>":
            errors += command_problems(name, command, by_id, skills)
    if errors:
        return "", errors

    def gate_row(gate: dict) -> str:
        command = f"`{gate['command']}`" if gate.get("command") else ""
        blockers = "<br>".join(cell(b) for b in gate.get("blockers") or []) or "—"
        return f"| {cell(gate['id'])} | {cell(gate.get('description', ''))} | {command} | {cell(gate['status'])} | — | {blockers} |"

    rows: list[tuple[str, str, str]] = []
    for gate in gates:
        if not gate.get("before"):
            rows.append((gate.get("command") or "", gate["status"], gate_row(gate)))
    for item in facts["items"]:
        for gate in gates:
            if gate.get("before") == item["id"]:
                rows.append((gate.get("command") or "", gate["status"], gate_row(gate)))
        line = item_row(item, by_id, base)
        if item["status"] in SETTLED_STATUS:
            rows.append(("", SETTLED_STATUS[item["status"]], line))
            continue
        entry = item_judgments[item["id"]]
        command = entry.get("command") or ""
        line = line.replace("| <command> |", f"| {f'`{command}`' if command else ''} |", 1)
        line = line.replace("| <status> |", f"| {cell(entry['status'])} |", 1)
        extra = "<br>".join(cell(b) for b in entry.get("blockers") or [])
        if extra:
            head, prereqs = line[:-2].rsplit("| ", 1)
            prereqs = extra if prereqs.strip() == "—" else f"{prereqs.strip()}<br>{extra}"
            line = f"{head}| {prereqs} |"
        rows.append((command, entry["status"], line))

    actionable = [c for c, status, _ in rows if c and not status.startswith(("Open - blocked", "Complete", "Cancelled"))]
    actionable = list(dict.fromkeys(actionable))
    nxt = (judgments or {}).get("next") or (actionable[0] if actionable else None)
    also = (judgments or {}).get("also") or [c for c in actionable if c != nxt]

    counts: dict[str, int] = {}
    for _, status, _ in rows:
        counts[status] = counts.get(status, 0) + 1
    included = ", ".join(facts["included"]) or None
    owners = ", ".join(facts["transitive_owners"])
    scope = (judgments or {}).get("scope") or (
        f"Primary scope: {facts['primary']}, with "
        + (f"{included} explicitly included." if included else "no explicitly included specifications.")
        + (f"\n{owners} {'is' if len(facts['transitive_owners']) == 1 else 'are'} included only as the owner of "
           f"transitive prerequisites; unrelated {owners} work is excluded." if owners else ""))
    notes = [
        f"Rows: {len(rows)} ({', '.join(f'{n} {s}' for s, n in sorted(counts.items()))}).",
        "Plans with non-current sources: " + (", ".join(g["id"][5:] for g in sync) or "none") + ".",
        f"Readiness records with non-current sources: {sum(1 for r in facts['readiness'] if r['stale_sources'])} "
        f"of {len(facts['readiness'])}.",
        "Structural findings: " + ("; ".join(facts["findings"]) or "none") + ".",
        "Working-copy inputs: " + (", ".join(f"`{p}`" for p in facts["working_copy_inputs"]) or "none (clean)") + ".",
        "Next command is the first row in dependency order with a safe command; gates precede the rows they unblock.",
    ]
    if gate_mode:
        notes.append("Open rows are blocked until the stale plans are synchronized; regenerate this runbook afterwards.")
    if judgments.get("notes"):
        notes.append(judgments["notes"].strip())
    front = [
        "---",
        f'primary_spec: "{facts["primary"]}"',
        "included_specs:" + ("" if facts["included"] else " []"),
        *[f'  - "{s}"' for s in facts["included"]],
        "transitive_spec_owners:" + ("" if facts["transitive_owners"] else " []"),
        *[f'  - "{s}"' for s in facts["transitive_owners"]],
        'generated_at: "<generated_at>"',
        f'branch: "{facts["branch"]}"',
        f'head: "{facts["head"]}"',
        f"source_file_count: {facts['source_file_count']}",
        f'source_set_sha256: "{facts["source_set_sha256"]}"',
        "---",
    ]
    body = [
        "", f"# {facts['primary']}: Work Runbook", "",
        "> Generated by `work-runbook-sync`. This tracked file is a derived workflow",
        "> view, not a status or eligibility authority. Regenerate it after plans, work",
        "> items, readiness, approvals, dependencies, or authoritative sources change.",
        "", "## Scope", "", scope, "", "## Next action", "",
        f"**Next command:** {f'`{nxt}`' if nxt else 'None'}", "",
        "**Also eligible:** " + ("<br>".join(f"`{c}`" for c in also) if also else "None"), "",
        "## Runbook", "",
        "| Work item | Description | Skill command | Status | Date Completed | Pre-requisites / blocked by |",
        "| --- | --- | --- | --- | --- | --- |",
        *[line for _, _, line in rows], "",
        "## Snapshot notes", "",
        *[f"- {n}" for n in notes], "",
    ]
    return "\n".join(front + body), []


VOLATILE_RE = re.compile(r'^(generated_at|branch|head): .*$', re.M)


def write_runbook(facts: dict, judgments: dict | None) -> int:
    text, errors = render_runbook(facts, judgments)
    if errors:
        for error in errors:
            print(f"- {error}")
        print("runbook not written")
        return 2
    for label in ("Next command", "Also eligible"):
        match = re.search(rf"^\*\*{label}:\*\* (.*)$", text, re.M)
        print(f"{label}: {match.group(1).replace('<br>', ', ') if match else 'None'}")
    path = ROOT / facts["runbook"]["path"]
    old = path.read_text(encoding="utf-8").replace("\r\n", "\n") if path.is_file() else None
    if old is not None and VOLATILE_RE.sub("", old) == VOLATILE_RE.sub("", text):
        print(f"{facts['runbook']['path']}: no-op (rendered content unchanged)")
        return 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path.write_bytes(text.replace("<generated_at>", now).encode("utf-8"))
    problems = check_runbook(facts)
    for problem in problems:
        print(f"- {problem}")
    print(f"{facts['runbook']['path']}: written; check {'FAIL' if problems else 'PASS'} ({len(problems)} findings)")
    return 1 if problems else 0


def inherited_include(primary: str, value: str | None) -> str:
    """An explicit --include wins; otherwise keep the existing runbook's declared included scope."""
    if value is not None:
        return value
    runbook = ROOT / f"work/{primary.split('-')[-1]}/runbook.md"
    if not runbook.is_file():
        return ""
    declared = parse_frontmatter(runbook.read_text(encoding="utf-8")).get("included_specs") or []
    return ",".join(str(s) for s in declared) if isinstance(declared, list) else str(declared)


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect deterministic work-runbook facts.")
    parser.add_argument("primary", help="primary specification, for example SPEC-0008")
    parser.add_argument("--include", default=None,
                        help="comma-separated additional specifications; defaults to the existing runbook's "
                             "included_specs, and an empty value clears them")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--json", action="store_true", help="emit JSON instead of compact text")
    mode.add_argument("--open", action="store_true", help="omit settled complete/cancelled items from text output")
    mode.add_argument("--rows", action="store_true", help="print table rows: exact for settled items, placeholders for open items")
    mode.add_argument("--check", action="store_true", help="validate the existing runbook; exit 1 on any finding")
    mode.add_argument("--judgments-template", action="store_true",
                      help="print a JSON judgments skeleton for open rows, with deterministic suggestions, gates, and hints")
    mode.add_argument("--write", action="store_true",
                      help="render and write the complete runbook from suggestions plus any --judgments overrides, "
                           "then check it; no-op when content is unchanged")
    parser.add_argument("--judgments", metavar="FILE",
                        help="with --write: JSON overrides of suggested rows and gates; '-' reads standard input")
    parser.add_argument("--out", metavar="FILE",
                        help="with --judgments-template: write the JSON to FILE and print a compact summary instead")
    args = parser.parse_args()
    if args.judgments and not args.write:
        parser.error("--judgments requires --write")
    if args.out and not args.judgments_template:
        parser.error("--out requires --judgments-template")
    utf8_stdio()
    included = [normalize_spec(s) for s in inherited_include(normalize_spec(args.primary), args.include).split(",")
                if s.strip()]
    facts = Facts(normalize_spec(args.primary), included).collect()
    if args.write:
        judgments = None
        if args.judgments:
            raw = sys.stdin.buffer.read() if args.judgments == "-" else Path(args.judgments).read_bytes()
            try:
                judgments = normalize_overrides(json.loads(raw.decode("utf-8-sig") or "{}"))
            except ValueError as error:
                print(f"invalid --judgments: {error}", file=sys.stderr)
                return 2
        return write_runbook(facts, judgments)
    if args.judgments_template:
        template = judgments_template(facts)
        if args.out:
            Path(args.out).write_text(json.dumps(template, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print(template_summary(template, facts))
            print(f"template written to {args.out}")
            return 0
        json.dump(template, sys.stdout, indent=1)
        print()
        return 0
    if args.json:
        json.dump(facts, sys.stdout, indent=1)
        print()
    elif args.rows:
        print_rows(facts)
    elif args.check:
        problems = check_runbook(facts)
        for problem in problems:
            print(f"- {problem}")
        print(f"{facts['runbook']['path']}: {'FAIL' if problems else 'PASS'} ({len(problems)} findings)")
        return 1 if problems else 0
    else:
        print_text(facts, open_only=args.open)
    return 0


if __name__ == "__main__":
    sys.exit(main())
