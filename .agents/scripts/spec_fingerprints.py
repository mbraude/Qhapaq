#!/usr/bin/env python3
"""Compute requirement fingerprints and check fingerprinted references.

Replaces hand-run fingerprint helpers. Uses the block grammar in the
spec-trace-check skill; read-only and stateless.

Usage:
  python .agents/scripts/spec_fingerprints.py                      # every block in SPEC.md and specs/
  python .agents/scripts/spec_fingerprints.py specs/0008-*.md      # selected specifications
  python .agents/scripts/spec_fingerprints.py --rev HEAD SPEC.md   # text at a revision
  python .agents/scripts/spec_fingerprints.py --id R-0008-001 R-0007-012
  python .agents/scripts/spec_fingerprints.py --refs R-0008-001    # references and whether each is current
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys

import qhapaq_work as q

REF_RE = re.compile(r"\b(R-C?\d{4}-\d{3,})@([0-9a-fA-F]+)\b")


def load(paths: list[str], rev: str | None) -> list[dict]:
    rows = []
    for path in paths:
        text = q.head_text(path, rev) if rev else (q.ROOT / path).read_text(encoding="utf-8") if (q.ROOT / path).is_file() else None
        if text is None:
            rows.append({"path": path, "id": None, "error": "missing"})
            continue
        for key, info in q.requirement_index(text).items():
            rows.append({"path": path, "id": key, **info})
    return rows


def references(ids: list[str], current: dict[str, dict]) -> list[dict]:
    if not ids:
        return []
    args = ["grep", "-n", "-I", "--untracked", "--no-color"]
    for key in ids:
        args += ["-e", f"{key}@"]
    rows = []
    for line in q.git(*args).splitlines():
        path, number, content = line.split(":", 2)
        for key, fp in REF_RE.findall(content):
            if key not in ids:
                continue
            info = current.get(key)
            state = "unknown-id" if info is None else "retired" if info["retired"] else "current" if fp == info["fingerprint"] else "stale"
            rows.append({"path": path, "line": int(number), "id": key, "fingerprint": fp,
                         "current_fingerprint": info and info["fingerprint"], "state": state,
                         "markdown": path.endswith(".md")})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Requirement fingerprints and reference checks.")
    parser.add_argument("paths", nargs="*", help="specification paths or globs (default: all)")
    parser.add_argument("--rev", help="read text at this Git revision instead of the working copy")
    parser.add_argument("--id", nargs="+", default=[], help="only these identifiers")
    parser.add_argument("--refs", nargs="+", default=[], help="list repository references to these identifiers")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    q.utf8_stdio()

    paths: list[str] = []
    for value in args.paths:
        matches = sorted(glob.glob(str(q.ROOT / value)))
        paths += [q.repo_path(m) for m in matches] if matches else [q.repo_path(value)]
    rows = load(paths or q.spec_paths(), args.rev)

    if args.refs:
        current = {r["id"]: r for r in load(q.spec_paths(), None) if r.get("id")}
        refs = references(args.refs, current)
        if args.json:
            print(json.dumps(refs, indent=1))
        else:
            for r in refs:
                note = "" if r["state"] == "current" else f" (current {r['current_fingerprint']})"
                kind = " [markdown]" if r["markdown"] else ""
                print(f"{r['state']:<10} {r['path']}:{r['line']} {r['id']}@{r['fingerprint']}{note}{kind}")
            if not refs:
                print("no references found")
        return 1 if any(r["state"] != "current" and not r["markdown"] for r in refs) else 0

    wanted = set(args.id)
    rows = [r for r in rows if not wanted or r.get("id") in wanted]
    if args.json:
        print(json.dumps(rows, indent=1))
    else:
        for r in rows:
            if r.get("error"):
                print(f"MISSING {r['path']}")
            else:
                print(f"{r['id']}@{r['fingerprint']}  {r['path']}:{r['line']}{'  retired' if r['retired'] else ''}")
    missing = wanted - {r.get("id") for r in rows}
    for key in sorted(missing):
        print(f"UNKNOWN {key}", file=sys.stderr)
    return 1 if missing or any(r.get("error") for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
