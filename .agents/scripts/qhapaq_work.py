"""Shared, read-only helpers for Qhapaq workflow skill scripts.

Parses work-record frontmatter and sections, hashes exact file bytes, and
computes the workflow guide's material SHA-256 and requirement fingerprints.
Nothing here writes repository files or keeps state between runs.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work"
PATH_HASH_ROW_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|(?:\s*(material|bytes|baseline)\s*\|)?\s*`([0-9a-f]{64})`\s*\|",
    re.I,
)
MATERIAL_LINE_RE = re.compile(r"material\s+SHA-256[^`]*`([0-9a-f]{64})`", re.I)
MATERIAL_EXCLUDED_SECTIONS = {"Validation and review", "Plan approval", "Delivery evidence and review"}
REQUIREMENT_TAG_RE = re.compile(r"^\*\*\[(R-C?\d{4}-\d{3,})\]\*\*", re.I)
CHECKBOX_RE = re.compile(r"(?m)^(\s*(?:[-*+]|\d+[.)])\s+)\[[ xX]\]\s*")


def utf8_stdio() -> None:
    """Emit UTF-8 regardless of the console code page, so dashes and quotes survive on Windows."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def repo_path(value: str) -> str:
    """Normalize a user-supplied path to a repository-relative POSIX path."""
    path = Path(value)
    return rel(path if path.is_absolute() else ROOT / path)


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    return result.stdout.rstrip() if result.returncode == 0 else ""


def git_bytes(*args: str) -> bytes | None:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    return result.stdout if result.returncode == 0 else None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def status_entries() -> list[dict]:
    """Working-tree changes since HEAD as {code, path, original}, including untracked files and renames."""
    data = git_bytes("status", "--porcelain=v1", "-z", "--untracked-files=all") or b""
    parts = data.decode("utf-8").split("\0")
    entries, i = [], 0
    while i < len(parts):
        part = parts[i]
        i += 1
        if len(part) < 4:
            continue
        code, path = part[:2], part[3:]
        original = None
        if "R" in code or "C" in code:
            original = parts[i]
            i += 1
        entries.append({"code": code, "path": path, "original": original})
    return entries


class Snapshot:
    """Reads each repository file once per run and retains its bytes and digest."""

    def __init__(self) -> None:
        self._bytes: dict[str, bytes | None] = {}
        self._sha: dict[str, str | None] = {}
        self.states: dict[tuple, str] = {}

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
            self._sha[path] = None if data is None else sha256_bytes(data)
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
    """Return (heading, heading line number, body lines) for each level-2 section outside code fences."""
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


def material_text(text: str) -> str:
    """The workflow guide's material view: LF line endings, without the frontmatter
    status line or the evidence sections named in MATERIAL_EXCLUDED_SECTIONS."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    out: list[str] = []
    in_front = skip = False
    for index, line in enumerate(text.splitlines(keepends=True)):
        stripped = line.rstrip("\n")
        if index == 0 and stripped == "---":
            in_front = True
            out.append(line)
            continue
        if in_front:
            if stripped == "---":
                in_front = False
                out.append(line)
            elif not re.match(r"^status\s*:", stripped):
                out.append(line)
            continue
        heading = re.match(r"^##\s+(.+?)\s*$", stripped)
        if heading:
            skip = heading.group(1) in MATERIAL_EXCLUDED_SECTIONS
            if skip:
                continue
        if not skip:
            out.append(line)
    return "".join(out)


def material_sha256(data: bytes) -> str:
    return sha256_bytes(material_text(data.decode("utf-8")).encode("utf-8"))


def progress_material_sha256(data: bytes) -> str:
    """Hash work-item scope and criteria while ignoring checklist completion state."""
    text = material_text(data.decode("utf-8"))
    text = re.sub(
        r"(?m)^(\s*(?:[-*+]|\d+[.)])\s+)\[[ xX]\]",
        r"\1[ ]",
        text,
    )
    return sha256_bytes(text.encode("utf-8"))


PLAN_RE = re.compile(r"^work/(?:components/)?\d{4}/plan\.md$")
READINESS_RE = re.compile(r"^work/(?:components/)?\d{4}/readiness/[^/]+\.md$")
DERIVED_VIEW_RE = re.compile(r"^work/(?:(?:components/)?\d{4}/runbook\.md$|diagrams/)")
RECONCILIATION_RECORD_RE = re.compile(
    r"^work/(?:components/)?\d{4}/reconciliations/(?:index|[^/]+)\.md$"
)
PROCESS_SOURCE_RE = re.compile(r"^(?:docs/development/spec-driven-workflow\.md|work/templates/)")
PLAN_EXCLUDED_HEADING_RE = re.compile(r"reconciliation|impact review|evidence", re.I)
GUIDE = "docs/development/spec-driven-workflow.md"
PROCESS_VERSION_RE = re.compile(r"^\*\*Process version:\*\*\s*(\d+)", re.M)


def plan_material_text(text: str, readiness: bool = False) -> str:
    """A plan's material view: LF line endings, without its frontmatter `sources`
    list or `process_version`, and without level-2 sections whose headings match
    PLAN_EXCLUDED_HEADING_RE (reconciliation and review evidence). With
    `readiness`, also without the `assessment` field and the
    `Validation and approval` section."""
    excluded_keys = {"sources", "process_version"} | ({"assessment"} if readiness else set())
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    out: list[str] = []
    in_front = in_sources = skip = False
    for index, line in enumerate(text.splitlines(keepends=True)):
        stripped = line.rstrip("\n")
        if index == 0 and stripped == "---":
            in_front = True
            out.append(line)
            continue
        if in_front:
            if stripped == "---":
                in_front = in_sources = False
                out.append(line)
            elif re.match(r"^[A-Za-z_][\w-]*\s*:", stripped):
                key = stripped.split(":", 1)[0].strip()
                in_sources = key == "sources"
                if key not in excluded_keys:
                    out.append(line)
            elif not in_sources:
                out.append(line)
            continue
        heading = re.match(r"^##\s+(.+?)\s*$", stripped)
        if heading:
            skip = bool(PLAN_EXCLUDED_HEADING_RE.search(heading.group(1))) or (
                readiness and heading.group(1) == "Validation and approval")
            if skip:
                continue
        if not skip:
            out.append(line)
    return "".join(out)


def has_material(path: str) -> bool:
    """Whether a cited source of this kind records `material_sha256`."""
    return bool(WORK_ITEM_RE.match(path) or PLAN_RE.match(path) or READINESS_RE.match(path))


def source_material_sha256(path: str, data: bytes) -> str | None:
    """The material SHA-256 recorded for a work-item, plan, or readiness source; None otherwise."""
    if WORK_ITEM_RE.match(path):
        return material_sha256(data)
    if PLAN_RE.match(path) or READINESS_RE.match(path):
        text = plan_material_text(data.decode("utf-8"), readiness=bool(READINESS_RE.match(path)))
        return sha256_bytes(text.encode("utf-8"))
    return None


def source_kind(path: str) -> str:
    """Classify a path as non-source evidence, a derived view, a process source,
    or an authoritative input."""
    if RECONCILIATION_RECORD_RE.match(path):
        return "reconciliation-record"
    if DERIVED_VIEW_RE.match(path):
        return "derived-view"
    if PROCESS_SOURCE_RE.match(path):
        return "process"
    return "input"


def process_version(snap: "Snapshot") -> int | None:
    match = PROCESS_VERSION_RE.search(snap.text(GUIDE))
    return int(match.group(1)) if match else None


def process_state(snap: "Snapshot", recorded) -> str:
    """`current`, `process-missing`, or `process-outdated` for a record's `process_version`."""
    current = process_version(snap)
    if recorded in (None, ""):
        return "process-missing"
    try:
        value = int(recorded)
    except (TypeError, ValueError):
        return "process-missing"
    return "current" if current is None or value >= current else "process-outdated"


def requirement_blocks(text: str) -> dict[str, str]:
    """Requirement block text keyed by identifier, using the trace-check block grammar."""
    blocks: dict[str, list[str]] = {}
    current = None
    fence = False
    for line in re.split(r"\r?\n", text):
        tag = REQUIREMENT_TAG_RE.match(line)
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and tag:
            current = tag.group(1)
            blocks[current] = []
            line = line[tag.end():]
        elif not fence and re.match(r"^#{1,6} ", line):
            current = None
        if current:
            blocks[current].append(line)
    return {key: "\n".join(lines) + "\n" for key, lines in blocks.items()}


def fingerprint(block: str) -> str:
    text = CHECKBOX_RE.sub(r"\1", block)
    text = re.sub(r"\s+", " ", text).strip()
    return sha256_bytes(text.encode("utf-8"))[:6]


def fingerprints(text: str) -> dict[str, str]:
    """Requirement identifier to six-hex fingerprint, in document order."""
    return {key: fingerprint(block) for key, block in requirement_blocks(text).items()}


SPEC_FILE_RE = re.compile(r"^(SPEC\.md|specs/(?:components/)?[^/]+\.md)$")
RETIRED_RE = re.compile(r"^\s*\*Retired\b")


def is_spec_path(path: str) -> bool:
    return bool(SPEC_FILE_RE.match(path)) and not path.endswith("README.md")


def spec_number(path: str) -> str | None:
    """Identifier prefix a specification file must use: 0000 for SPEC.md, NNNN or CNNNN otherwise."""
    if path == "SPEC.md":
        return "0000"
    match = re.match(r"^specs/(components/)?C?(\d{4})-", path)
    if not match:
        return None
    return ("C" if match.group(1) else "") + match.group(2)


def spec_paths() -> list[str]:
    paths = ["SPEC.md"] if (ROOT / "SPEC.md").is_file() else []
    paths += sorted(rel(p) for p in (ROOT / "specs").rglob("*.md"))
    return [p for p in paths if is_spec_path(p)]


def requirement_index(text: str) -> dict[str, dict]:
    """Identifier to {line, fingerprint, retired} for every block, using the trace-check grammar."""
    lines: dict[str, int] = {}
    fence = False
    for number, line in enumerate(re.split(r"\r?\n", text), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and (tag := REQUIREMENT_TAG_RE.match(line)):
            lines.setdefault(tag.group(1), number)
    return {
        key: {"line": lines.get(key), "fingerprint": fingerprint(block), "retired": bool(RETIRED_RE.match(block.strip("\n ")))}
        for key, block in requirement_blocks(text).items()
    }


def head_text(path: str, rev: str = "HEAD") -> str | None:
    data = git_bytes("show", f"{rev}:{path}")
    return None if data is None else data.decode("utf-8", errors="replace")


def last_commit(path: str) -> str | None:
    return git("log", "-1", "--format=%H", "--", path) or None


def is_tracked(path: str) -> bool:
    return bool(git("ls-files", "--", path))


WORK_ITEM_RE = re.compile(r"^work/\d{4}/(decisions|implementation)/[DI]-\d{4}-\d{3}[^/]*\.md$")


_WORK_HISTORY: dict[str, list[str]] | None = None


def work_history(path: str) -> list[str]:
    """Commits touching `path`, newest first, from one shared `git log` over `work/`."""
    global _WORK_HISTORY
    if _WORK_HISTORY is None:
        _WORK_HISTORY = {}
        commit = None
        for line in git("log", "--format=%x00%H", "--name-only", "--no-renames", "--", "work").splitlines():
            if line.startswith("\x00"):
                commit = line[1:]
            elif line and commit:
                _WORK_HISTORY.setdefault(line, []).append(commit)
    return _WORK_HISTORY.get(path, [])


def recover_bytes(path: str, sha: str, revision: str | None, depth: int = 50) -> bytes | None:
    """Find committed bytes of `path` whose SHA-256 equals `sha`, trying `revision` first."""
    history = work_history(path) if path.startswith("work/") else git("log", "--format=%H", "--", path).splitlines()
    candidates = list(dict.fromkeys(([revision] if revision else []) + history[:depth]))
    if not candidates:
        return None
    request = "".join(f"{candidate}:{path}\n" for candidate in candidates).encode("utf-8")
    result = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, input=request, capture_output=True)
    if result.returncode != 0:
        return None
    out, pos = result.stdout, 0
    for _ in candidates:
        end = out.index(b"\n", pos)
        header = out[pos:end].split()
        pos = end + 1
        if len(header) == 3 and header[1] == b"blob":
            size = int(header[2])
            data = out[pos:pos + size]
            pos += size + 1
            if sha256_bytes(data) == sha:
                return data
            # Records hashed on a Windows checkout cover CRLF working-copy bytes of an LF blob.
            crlf = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
            if crlf != data and sha256_bytes(crlf) == sha:
                return crlf
    return None


def recover_material_bytes(path: str, material: str, depth: int = 50) -> bytes | None:
    """Find committed bytes of a work item whose material hash equals `material`."""
    candidates = work_history(path)[:depth]
    if not candidates:
        return None
    request = "".join(f"{candidate}:{path}\n" for candidate in candidates).encode("utf-8")
    result = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, input=request, capture_output=True)
    if result.returncode != 0:
        return None
    output, position = result.stdout, 0
    for _ in candidates:
        end = output.index(b"\n", position)
        header = output[position:end].split()
        position = end + 1
        if len(header) != 3 or header[1] != b"blob":
            continue
        size = int(header[2])
        data = output[position:position + size]
        position += size + 1
        if material_sha256(data) == material:
            return data
    return None


def source_state(snap: Snapshot, path: str, recorded: str | None, revision: str | None = None,
                 material: str | None = None) -> str:
    """Classify a recorded source snapshot against current bytes.

    A work-item, plan, or readiness source that records `material_sha256` is
    `current` when its current material SHA-256 equals that value, as the
    workflow guide defines. For work items only, checklist-state changes are
    progress metadata and remain current when the approved material version is
    recoverable and all other material text matches.

    For a legacy work-item source without a recorded material hash, compare
    recoverable recorded bytes (or the recorded revision when the bytes are
    unavailable) with the current material view. Matching material is current:
    lifecycle status and review-evidence changes do not invalidate a consumer.
    A changed material view remains stale.
    """
    actual = snap.sha(path)
    if actual is None:
        return "missing"
    if material and has_material(path):
        current_bytes = snap.read(path) or b""
        current_material = source_material_sha256(path, current_bytes)
        if current_material == material:
            return "current"
        if WORK_ITEM_RE.match(path):
            approved = recover_material_bytes(path, material)
            if approved is not None and progress_material_sha256(approved) == progress_material_sha256(current_bytes):
                return "current"
        return "stale"
    if actual == recorded:
        return "current"
    key = (path, recorded, revision)
    cache = snap.states
    if key not in cache:
        cache[key] = "stale"
        if recorded and WORK_ITEM_RE.match(path):
            current_bytes = snap.read(path) or b""
            current = material_sha256(current_bytes)
            old = recover_bytes(path, recorded, revision)
            if old is not None:
                if material_sha256(old) == current:
                    cache[key] = "current"
                elif progress_material_sha256(old) == progress_material_sha256(current_bytes):
                    cache[key] = "current"
            elif revision:
                base = git_bytes("show", f"{revision}:{path}")
                if base is not None:
                    if material_sha256(base) == current:
                        cache[key] = "current"
                    elif progress_material_sha256(base) == progress_material_sha256(current_bytes):
                        cache[key] = "current"
    return cache[key]
