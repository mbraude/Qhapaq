#!/usr/bin/env python3
"""Extract and validate non-material reconciliation records for work plans."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import qhapaq_work as q


INDEX_HEADING = "Reconciliation index"
INDEX_PATH = "reconciliations/index.md"
DATE_RE = re.compile(r"^- Date:\s+(\d{4}-\d{2}-\d{2})\b")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*(?:\r?\n)?$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")


@dataclass(frozen=True)
class Record:
    section: str
    date: str | None
    path: str
    text: str


@dataclass(frozen=True)
class Migration:
    plan_path: str
    plan_text: str
    index_path: str
    index_text: str
    records: tuple[Record, ...]
    material_sha256: str


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return result or "record"


def level_two_sections(lines: list[str]) -> list[tuple[int, int, str]]:
    headings = [
        (index, match.group(1))
        for index, line in enumerate(lines)
        if (match := HEADING_RE.match(line))
    ]
    return [
        (start, headings[position + 1][0] if position + 1 < len(headings) else len(lines), title)
        for position, (start, title) in enumerate(headings)
    ]


def split_records(body: list[str]) -> list[tuple[str | None, list[str]]]:
    starts = [
        index
        for index, line in enumerate(body)
        if DATE_RE.match(line.rstrip("\r\n"))
    ]
    if not starts:
        return [(None, body)]

    records: list[tuple[str | None, list[str]]] = []
    prefix = body[:starts[0]]
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(body)
        segment = body[start:end]
        if position == 0:
            segment = prefix + segment
        date = DATE_RE.match(body[start].rstrip("\r\n"))
        records.append((date.group(1) if date else None, segment))
    return records


def unique_record_path(
    date: str | None,
    section: str,
    counters: dict[str, int],
) -> str:
    stem = f"{date or 'undated'}-{slug(section)}"
    counters[stem] = counters.get(stem, 0) + 1
    suffix = "" if counters[stem] == 1 else f"-{counters[stem]:02d}"
    return f"reconciliations/{stem}{suffix}.md"


def record_text(section: str, body: list[str]) -> str:
    content = "".join(body).replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    return (
        f"# {section}\n\n"
        "[Reconciliation index](index.md) | [Work plan](../plan.md)\n\n"
        f"{content}\n"
    )


def index_text(spec: str, records: list[Record]) -> str:
    grouped: list[tuple[str, list[Record]]] = []
    for record in records:
        if not grouped or grouped[-1][0] != record.section:
            grouped.append((record.section, []))
        grouped[-1][1].append(record)

    lines = [
        f"# {spec} Reconciliation Index",
        "",
        "These records preserve non-material source-impact and workflow history for",
        "the [authoritative work plan](../plan.md). They do not own scope, phase",
        "membership, ordering, status, dependencies, gates, readiness, or approval.",
        "",
    ]
    for section, entries in grouped:
        lines.extend((f"## {section}", ""))
        for entry in entries:
            label = entry.date or "Undated legacy record"
            lines.append(f"- [{label}]({Path(entry.path).name})")
        lines.append("")
    return "\n".join(lines)


def transform(plan_path: str, text: str) -> Migration:
    lines = text.splitlines(keepends=True)
    sections = level_two_sections(lines)
    extractable = [
        section for section in sections
        if q.PLAN_EXCLUDED_HEADING_RE.search(section[2])
        and section[2] != INDEX_HEADING
    ]
    if not extractable:
        raise ValueError(f"{plan_path}: no extractable reconciliation sections")
    if any(title == INDEX_HEADING for _, _, title in sections):
        raise ValueError(f"{plan_path}: already contains a reconciliation index")

    eol = "\r\n" if "\r\n" in text else "\n"
    counters: dict[str, int] = {}
    records: list[Record] = []
    for start, end, section in extractable:
        for date, body in split_records(lines[start + 1:end]):
            if not any(line.strip() for line in body):
                continue
            path = unique_record_path(date, section, counters)
            records.append(Record(section, date, path, record_text(section, body)))

    index_start = extractable[-1][0]
    output: list[str] = []
    cursor = 0
    for start, end, _ in extractable:
        output.extend(lines[cursor:start])
        if start == index_start:
            output.extend((
                f"## {INDEX_HEADING}{eol}",
                eol,
                "Historical source-impact and workflow evidence is stored in the "
                f"[reconciliation index]({INDEX_PATH}).{eol}",
                "The linked records are non-material and do not own current plan "
                f"state.{eol}",
            ))
        cursor = end
    output.extend(lines[cursor:])
    updated = "".join(output)

    before = q.source_material_sha256(plan_path, text.encode("utf-8"))
    after = q.source_material_sha256(plan_path, updated.encode("utf-8"))
    if before is None or before != after:
        raise ValueError(
            f"{plan_path}: material SHA-256 changed from {before} to {after}"
        )

    spec = q.parse_frontmatter(text).get("spec") or Path(plan_path).parent.name
    index_path = f"{Path(plan_path).parent.as_posix()}/{INDEX_PATH}"
    return Migration(
        plan_path=plan_path,
        plan_text=updated,
        index_path=index_path,
        index_text=index_text(str(spec), records),
        records=tuple(records),
        material_sha256=before,
    )


def move_index_to_end(plan_path: str, text: str) -> str:
    lines = text.splitlines(keepends=True)
    indexes = [
        section for section in level_two_sections(lines)
        if section[2] == INDEX_HEADING
    ]
    if len(indexes) != 1:
        raise ValueError(f"{plan_path}: expected one '{INDEX_HEADING}' section")
    start, end, _ = indexes[0]

    index_lines = lines[start:end]
    while index_lines and not index_lines[-1].strip():
        index_lines.pop()
    updated = "".join(lines[:start] + lines[end:] + index_lines)
    before = q.source_material_sha256(plan_path, text.encode("utf-8"))
    after = q.source_material_sha256(plan_path, updated.encode("utf-8"))
    if before is None or before != after:
        raise ValueError(
            f"{plan_path}: moving index changed material SHA-256 from {before} to {after}"
        )
    return updated


def validate(plan_path: str) -> list[str]:
    findings: list[str] = []
    plan = q.ROOT / plan_path
    if not plan.is_file():
        return [f"{plan_path}: missing plan"]
    text = plan.read_text(encoding="utf-8")
    sections = level_two_sections(text.splitlines(keepends=True))
    indexes = [section for section in sections if section[2] == INDEX_HEADING]
    legacy = [
        title for _, _, title in sections
        if q.PLAN_EXCLUDED_HEADING_RE.search(title) and title != INDEX_HEADING
    ]
    if len(indexes) != 1:
        findings.append(f"{plan_path}: expected one '{INDEX_HEADING}' section")
    elif indexes[0][1] != len(text.splitlines(keepends=True)):
        findings.append(f"{plan_path}: reconciliation index must be the final section")
    if legacy:
        findings.append(f"{plan_path}: unextracted sections: {', '.join(legacy)}")
    if f"]({INDEX_PATH})" not in text:
        findings.append(f"{plan_path}: missing reconciliation index link")

    directory = plan.parent / "reconciliations"
    index = directory / "index.md"
    if not index.is_file():
        findings.append(f"{q.rel(index)}: missing index")
        return findings
    index_body = index.read_text(encoding="utf-8")
    linked = {
        target for target in LINK_RE.findall(index_body)
        if "/" not in target and target != "index.md"
    }
    actual = {path.name for path in directory.glob("*.md") if path.name != "index.md"}
    for name in sorted(linked - actual):
        findings.append(f"{q.rel(index)}: missing linked record {name}")
    for name in sorted(actual - linked):
        findings.append(f"{q.rel(index)}: unindexed record {name}")
    for name in sorted(actual):
        body = (directory / name).read_text(encoding="utf-8")
        if "[Reconciliation index](index.md)" not in body or "[Work plan](../plan.md)" not in body:
            findings.append(f"{q.rel(directory / name)}: missing navigation links")
    return findings


def expand_plans(values: list[str]) -> list[str]:
    if values:
        return [q.repo_path(value) for value in values]
    platform = q.WORK.glob("[0-9][0-9][0-9][0-9]/plan.md")
    components = (q.WORK / "components").glob("[0-9][0-9][0-9][0-9]/plan.md")
    return sorted(q.rel(path) for path in [*platform, *components])


def extract(plans: list[str]) -> tuple[list[Migration], list[str]]:
    migrations: list[Migration] = []
    findings: list[str] = []
    targets: set[str] = set()
    for plan_path in plans:
        plan = q.ROOT / plan_path
        try:
            migration = transform(plan_path, plan.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as error:
            findings.append(str(error))
            continue
        paths = {migration.index_path} | {
            f"{Path(plan_path).parent.as_posix()}/{record.path}"
            for record in migration.records
        }
        collisions = [
            path for path in paths
            if path in targets or (q.ROOT / path).exists()
        ]
        if collisions:
            findings.extend(f"{path}: target already exists" for path in sorted(collisions))
        targets.update(paths)
        migrations.append(migration)
    return migrations, findings


def write_migrations(migrations: list[Migration]) -> None:
    for migration in migrations:
        (q.ROOT / migration.plan_path).write_bytes(migration.plan_text.encode("utf-8"))
        (q.ROOT / migration.index_path).parent.mkdir(parents=True, exist_ok=True)
        (q.ROOT / migration.index_path).write_text(
            migration.index_text, encoding="utf-8", newline="\n"
        )
        for record in migration.records:
            target = q.ROOT / Path(migration.plan_path).parent / record.path
            target.write_text(record.text, encoding="utf-8", newline="\n")


def main() -> int:
    q.utf8_stdio()
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("extract", "normalize", "check"):
        command = subparsers.add_parser(name)
        command.add_argument("plans", nargs="*", help="plan paths; defaults to work/*/plan.md")
    args = parser.parse_args()
    plans = expand_plans(args.plans)

    if args.command == "extract":
        migrations, findings = extract(plans)
        if findings:
            print("\n".join(findings), file=sys.stderr)
            return 1
        write_migrations(migrations)
        for migration in migrations:
            print(
                f"{migration.plan_path}: extracted {len(migration.records)} records; "
                f"material SHA-256 {migration.material_sha256}"
            )
        return 0

    if args.command == "normalize":
        updates: list[tuple[str, str]] = []
        findings: list[str] = []
        for plan_path in plans:
            try:
                text = (q.ROOT / plan_path).read_text(encoding="utf-8")
                updates.append((plan_path, move_index_to_end(plan_path, text)))
            except (OSError, UnicodeError, ValueError) as error:
                findings.append(str(error))
        if findings:
            print("\n".join(findings), file=sys.stderr)
            return 1
        for plan_path, text in updates:
            (q.ROOT / plan_path).write_bytes(text.encode("utf-8"))
            print(f"{plan_path}: reconciliation index normalized")
        return 0

    findings = [finding for plan in plans for finding in validate(plan)]
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    print(f"{len(plans)} plans: reconciliation indexes and records valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
