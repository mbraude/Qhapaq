#!/usr/bin/env python3
"""Render selected Qhapaq work plans as a validated Mermaid dependency graph."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import subprocess
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
ITEM_ID = re.compile(r"^[DI]-\d{4}-\d{3,}$")
SPEC_ID = re.compile(r"^\d{4}$")
STATUSES = {
    "open": "open",
    "in-progress": "inprogress",
    "ready-for-review": "review",
    "complete": "complete",
    "blocked": "blocked",
    "cancelled": "cancelled",
}


def parse_item(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: work item is missing YAML frontmatter")

    fields: dict[str, object] = {}
    lines = match.group(1).splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        scalar = re.match(r"^([a-z_]+):\s*(.*?)\s*$", line)
        if not scalar:
            index += 1
            continue

        key, value = scalar.groups()
        if key in ("depends_on", "artifacts"):
            dependencies: list[str] = []
            inline = re.fullmatch(r"\[(.*)\]", value)
            if inline:
                dependencies = [
                    entry.strip().strip("'\"")
                    for entry in inline.group(1).split(",")
                    if entry.strip()
                ]
            elif not value:
                cursor = index + 1
                while cursor < len(lines):
                    entry = re.match(r"^\s+-\s+(.+?)\s*$", lines[cursor])
                    if not entry:
                        if lines[cursor].strip() and not lines[cursor].startswith(" "):
                            break
                        if lines[cursor].strip():
                            raise ValueError(
                                f"{path}: unsupported prerequisite entry "
                                f"{lines[cursor].strip()!r}"
                            )
                        cursor += 1
                        continue
                    dependencies.append(entry.group(1).strip("'\""))
                    cursor += 1
                index = cursor - 1
            else:
                raise ValueError(f"{path}: unsupported {key} value {value!r}")
            fields[key] = dependencies
        else:
            fields[key] = value.strip("'\"")
        index += 1

    required = ("id", "kind", "title", "status", "spec", "depends_on", "artifacts")
    missing = [key for key in required if key not in fields]
    if missing:
        raise ValueError(f"{path}: missing required metadata: {', '.join(missing)}")
    if not ITEM_ID.fullmatch(str(fields["id"])):
        raise ValueError(f"{path}: invalid item ID {fields['id']!r}")
    if fields["kind"] not in ("decision", "implementation"):
        raise ValueError(f"{path}: unsupported kind {fields['kind']!r}")
    if fields["status"] not in STATUSES:
        raise ValueError(f"{path}: unsupported status {fields['status']!r}")
    if not str(fields["title"]).strip():
        raise ValueError(f"{path}: title must not be empty")
    if not isinstance(fields["depends_on"], list):
        raise ValueError(f"{path}: depends_on must be a list")
    if any(
        not isinstance(prerequisite, str) or not ITEM_ID.fullmatch(prerequisite)
        for prerequisite in fields["depends_on"]
    ):
        raise ValueError(f"{path}: prerequisite IDs must be valid work-item IDs")
    if len(fields["depends_on"]) != len(set(fields["depends_on"])):
        raise ValueError(f"{path}: duplicate prerequisite IDs")
    if fields["id"].startswith("D-") != (fields["kind"] == "decision"):
        raise ValueError(f"{path}: item ID and kind do not agree")
    return fields


def digest_sources(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths):
        relative = path.relative_to(ROOT).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def check_acyclic(records: dict[str, dict[str, object]]) -> None:
    dependents: dict[str, list[str]] = defaultdict(list)
    indegree = {item_id: 0 for item_id in records}
    for item_id, record in records.items():
        for prerequisite in record["depends_on"]:
            if prerequisite not in records:
                raise ValueError(
                    f"{item_id}: prerequisite {prerequisite} is not in the selected plans"
                )
            dependents[prerequisite].append(item_id)
            indegree[item_id] += 1

    ready = deque(sorted(item_id for item_id, count in indegree.items() if count == 0))
    visited = 0
    while ready:
        prerequisite = ready.popleft()
        visited += 1
        for dependent in dependents[prerequisite]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)
    if visited != len(records):
        cyclic = sorted(item_id for item_id, count in indegree.items() if count)
        raise ValueError(f"dependency cycle detected involving: {', '.join(cyclic)}")


def render(spec_ids: list[str], generated_at: str) -> tuple[str, Path, int, int]:
    records: dict[str, dict[str, object]] = {}
    sources: list[Path] = []
    plans: dict[str, Path] = {}

    for spec_id in spec_ids:
        owner = f"SPEC-{spec_id}"
        spec_dir = ROOT / "work" / spec_id
        plan = spec_dir / "plan.md"
        if not plan.is_file():
            raise ValueError(f"missing work plan: {plan.relative_to(ROOT)}")
        plans[spec_id] = plan
        sources.append(plan)
        for category in ("decisions", "implementation"):
            item_dir = spec_dir / category
            if not item_dir.is_dir():
                continue
            for path in sorted(item_dir.rglob("*.md")):
                record = parse_item(path)
                if record["spec"] != owner:
                    raise ValueError(
                        f"{path.relative_to(ROOT)}: owner {record['spec']!r} "
                        f"does not match {owner}"
                    )
                item_id = str(record["id"])
                if item_id in records:
                    raise ValueError(f"duplicate item ID: {item_id}")
                expected_kind = "decision" if category == "decisions" else "implementation"
                if record["kind"] != expected_kind:
                    raise ValueError(
                        f"{path.relative_to(ROOT)}: kind {record['kind']!r} "
                        f"does not match its {category} directory"
                    )
                records[item_id] = record
                sources.append(path)

    if not records:
        raise ValueError("no work items found in the selected plans")
    check_acyclic(records)

    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.PIPE
        ).strip()
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=ROOT, text=True, stderr=subprocess.PIPE
        ).strip()
    except (OSError, subprocess.CalledProcessError) as error:
        raise ValueError(f"could not resolve repository HEAD: {error}") from error

    source_digest = digest_sources(sources)
    output_name = "spec-" + "-".join(spec_ids) + ".mmd"
    output_path = ROOT / "work" / "diagrams" / output_name
    edge_count = sum(len(record["depends_on"]) for record in records.values())
    lines = [
        "%% Generated by .agents/skills/work-plan-diagram/scripts/render.py; do not edit.",
        f"%% Generated at: {generated_at}",
        f"%% HEAD: {revision}",
        f"%% Branch: {branch}",
        f"%% Source files: {len(sources)}",
        f"%% Source-set SHA-256: {source_digest}",
    ]
    for spec_id, plan in plans.items():
        lines.append(
            f"%% SPEC-{spec_id} plan SHA-256: "
            f"{hashlib.sha256(plan.read_bytes()).hexdigest()}"
        )
    lines.extend(
        [
            f"%% Items: {len(records)}",
            f"%% Dependencies: {edge_count}",
            "flowchart TB",
            '  subgraph SNAPSHOT["Generated work-plan snapshot - not an approval"]',
            '    META["' + " and ".join(f"SPEC-{sid}" for sid in spec_ids)
            + f"<br/>Generated UTC: {generated_at}"
            + f"<br/>Branch: {html.escape(branch, quote=True)}"
            + f"<br/>HEAD: {revision[:12]}"
            + f"<br/>Source snapshot: {source_digest[:12]}"
            + f"<br/>{len(sources)} source files; {len(records)} items; {edge_count} dependencies"
            + '<br/>Arrows: prerequisite to dependent<br/>Artifacts: recorded output paths, not proof of publication"]',
            "  end",
            "  subgraph STATUS_KEY[\"Status key\"]",
            '    KEY_OPEN["Open"]',
            '    KEY_PROGRESS["In progress"]',
            '    KEY_REVIEW["Ready for review"]',
            '    KEY_COMPLETE["Complete"]',
            '    KEY_BLOCKED["Blocked"]',
            '    KEY_CANCELLED["Cancelled"]',
            "  end",
        ]
    )

    sorted_ids = sorted(records)
    node_names = {item_id: f"N{index}" for index, item_id in enumerate(sorted_ids)}
    for spec_id in spec_ids:
        owner = f"SPEC-{spec_id}"
        lines.append(f'  subgraph S{spec_id}["{owner}"]')
        for item_id in sorted_ids:
            record = records[item_id]
            if record["spec"] != owner:
                continue
            node = node_names[item_id]
            title = html.escape(str(record["title"]), quote=True).replace("\n", " ")
            label = (
                f"{item_id}<br/>{record['kind']}: {title}"
                f"<br/>Status: {record['status']}"
            )
            if record["artifacts"]:
                label += "<br/>Artifacts:<br/>" + "<br/>".join(
                    html.escape(artifact, quote=True) for artifact in record["artifacts"]
                )
            lines.append(f'    {node}["{label}"]')
        lines.append("  end")

    lines.extend(
        f"  {node_names[prerequisite]} --> {node_names[item_id]}"
        for item_id in sorted_ids
        for prerequisite in sorted(records[item_id]["depends_on"])
    )
    lines.extend(
        [
            "  classDef open fill:#1565c0,stroke:#0d47a1,color:#ffffff,stroke-width:2px",
            "  classDef inprogress fill:#fff2cc,stroke:#bf9000,color:#222222",
            "  classDef review fill:#cfe2f3,stroke:#3d85c6,color:#222222",
            "  classDef complete fill:#2e7d32,stroke:#1b5e20,color:#ffffff,stroke-width:2px",
            "  classDef blocked fill:#f4cccc,stroke:#cc0000,color:#222222",
            "  classDef cancelled fill:#eeeeee,stroke:#999999,color:#666666,stroke-dasharray:5 5",
            "  class KEY_OPEN open",
            "  class KEY_PROGRESS inprogress",
            "  class KEY_REVIEW review",
            "  class KEY_COMPLETE complete",
            "  class KEY_BLOCKED blocked",
            "  class KEY_CANCELLED cancelled",
        ]
    )
    for item_id in sorted_ids:
        status_class = STATUSES[str(records[item_id]["status"])]
        lines.append(f"  class {node_names[item_id]} {status_class}")

    return "\n".join(lines) + "\n", output_path, len(records), edge_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec_ids", nargs="+", help="four-digit work-plan IDs, e.g. 0007")
    parser.add_argument(
        "--check", action="store_true", help="fail if the generated file is missing or stale"
    )
    args = parser.parse_args()
    if len(set(args.spec_ids)) != len(args.spec_ids):
        parser.error("specification IDs must be unique")
    if any(not SPEC_ID.fullmatch(spec_id) for spec_id in args.spec_ids):
        parser.error("each specification ID must contain exactly four digits")

    try:
        generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        if args.check:
            existing_path = ROOT / "work" / "diagrams" / (
                "spec-" + "-".join(args.spec_ids) + ".mmd"
            )
            if not existing_path.is_file():
                raise ValueError(f"{existing_path.relative_to(ROOT)} is missing; regenerate it")
            timestamp = re.search(
                r"^%% Generated at: (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$",
                existing_path.read_text(encoding="utf-8"), re.MULTILINE
            )
            if not timestamp:
                raise ValueError("export timestamp is missing or malformed; regenerate it")
            generated_at = timestamp.group(1)
            datetime.strptime(generated_at, "%Y-%m-%dT%H:%M:%SZ")
        content, output_path, item_count, edge_count = render(args.spec_ids, generated_at)
        relative_output = output_path.relative_to(ROOT)
        if args.check:
            if not output_path.is_file() or output_path.read_text(encoding="utf-8") != content:
                raise ValueError(f"{relative_output} is missing or stale; regenerate it")
            print(f"Current: {relative_output}")
        else:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding="utf-8", newline="\n")
            print(f"Wrote {relative_output}")
            print(f"Items: {item_count}")
            print(f"Dependencies: {edge_count}")
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
if __name__ == "__main__":
    raise SystemExit(main())
