#!/usr/bin/env python3
"""Deterministic Git preflight facts for the commit, push, and approval skills.

Reports the branch, default branch, upstream divergence, unresolved
operations, the selected commit snapshot (staged index, or every change when
nothing is staged), excluded changes, and review hints for that snapshot:
likely secrets on added lines, and large, binary, or generated files. With
--push it instead reports the origin remote, upstream naming, and the commits
a push would publish. Divergence reflects the last fetch unless --fetch first
fetches the current branch from origin. After a push, --verify-pushed fetches
and confirms that the upstream now equals HEAD.

Facts only: it never stages, commits, or pushes, fetches only when asked, and a
clean result does not replace the skill's own review of the snapshot. Exit
code 1 means a blocking finding.

Usage:
  python .agents/scripts/git_preflight.py [--push [--fetch] | --verify-pushed] [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

import qhapaq_work as q

LARGE_BYTES = 512 * 1024
GENERATED_RE = re.compile(r"(^|/)(bin|obj|artifacts|node_modules|__pycache__|TestResults)/|\.(pyc|dll|exe|pdb|nupkg)$")
SECRET_PATTERNS = [
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})\b")),
    ("slack-token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("azure-key", re.compile(r"(AccountKey|SharedAccessKey)=[A-Za-z0-9+/=]{20,}")),
    ("connection-password", re.compile(r"(?i)\b(password|pwd)=[^;\s'\"]{6,}")),
    ("assigned-secret", re.compile(
        r"(?i)\b(api[_-]?key|secret|token|password|passwd|client[_-]?secret)\b[\"']?\s*[:=]\s*[\"']([^\"'\s]{12,})[\"']")),
]
PLACEHOLDER_RE = re.compile(r"(?i)^(<.*>|\$\{.*\}|\{\{.*\}\}|x+|\*+|example.*|changeme|redacted|your[_-].*)$")
UNRESOLVED = {"MERGE_HEAD": "merge", "rebase-merge": "rebase", "rebase-apply": "rebase or am",
              "CHERRY_PICK_HEAD": "cherry-pick", "REVERT_HEAD": "revert", "BISECT_LOG": "bisect"}


def branch_facts() -> dict:
    header = dict(line[2:].split(" ", 1) for line in q.git("status", "--porcelain=v2", "--branch",
                                                         "--untracked-files=no").splitlines()
                  if line.startswith("# ") and " " in line[2:])
    branch = header.get("branch.head")
    branch = None if branch in (None, "(detached)") else branch
    default = q.git("symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD") or None
    upstream = header.get("branch.upstream")
    ahead = behind = None
    if upstream and "branch.ab" in header:
        plus, minus = header["branch.ab"].split()
        ahead, behind = int(plus), -int(minus)
    git_dir = q.ROOT / q.git("rev-parse", "--git-dir")
    unresolved = [name for marker, name in UNRESOLVED.items() if (git_dir / marker).exists()]
    log = q.git("log", "-8", "--format=%h %s").splitlines()
    return {
        "branch": branch,
        "head": log[0] if log else "",
        "origin": q.git("remote", "get-url", "origin") or None,
        "default_branch": default.split("/", 1)[1] if default and "/" in default else default,
        "upstream": upstream,
        "ahead": ahead,
        "behind": behind,
        "unresolved": unresolved,
        "recent_subjects": [line.split(" ", 1)[1] if " " in line else "" for line in log],
    }


def added_lines_by_path(paths: list[str], staged: bool) -> dict[str, list[tuple[int, str]]]:
    """New-side added lines for tracked paths from one diff invocation."""
    if not paths:
        return {}
    args = ["-c", "core.quotePath=false", "diff", "--cached" if staged else "HEAD", "-U0", "--no-color", "--no-ext-diff", "--no-renames",
            "--", *paths]
    result: dict[str, list[tuple[int, str]]] = {}
    current, number = None, 0
    for line in q.git(*args).splitlines():
        if line.startswith("+++ "):
            current = line[6:] if line.startswith("+++ b/") else None
            if current is not None:
                result.setdefault(current, [])
        elif line.startswith("@@"):
            match = re.search(r"\+(\d+)", line)
            number = int(match.group(1)) if match else 0
        elif current is not None and line.startswith("+"):
            result[current].append((number, line[1:]))
            number += 1
    return result


def untracked_lines(path: str) -> list[tuple[int, str]]:
    try:
        return list(enumerate((q.ROOT / path).read_text(encoding="utf-8").splitlines(), 1))
    except (OSError, UnicodeDecodeError):
        return []


def secret_hits(path: str, lines: list[tuple[int, str]]) -> list[dict]:
    hits = []
    for number, text in lines:
        for name, pattern in SECRET_PATTERNS:
            match = pattern.search(text)
            if not match:
                continue
            value = match.groups()[-1] if match.groups() else match.group(0)
            if name == "assigned-secret" and PLACEHOLDER_RE.match(value or ""):
                continue
            hits.append({"at": f"{path}:{number}", "pattern": name})
            break
    return hits


def snapshot_id(paths: list[tuple[str, bool]], use_index: bool) -> str:
    """SHA-256 over sorted 'path<TAB>blob' lines; equal before and after `git add` of the same content."""
    live = sorted(p for p, deleted in paths if not deleted)
    blobs: dict[str, str] = {}
    if use_index:
        for record in (q.git_bytes("ls-files", "-s", "-z", "--", *live) or b"").decode("utf-8").split("\0"):
            if "\t" in record:
                meta, path = record.split("\t", 1)
                blobs[path] = meta.split()[1]
    elif live:
        result = subprocess.run(["git", "hash-object", "--stdin-paths"], cwd=q.ROOT, capture_output=True,
                                input="\n".join(live) + "\n", text=True, encoding="utf-8")
        blobs = dict(zip(live, result.stdout.split()))
    lines = sorted(f"{p}\t{'DELETED' if deleted else blobs.get(p, 'UNKNOWN')}\n" for p, deleted in paths)
    return q.sha256_bytes("".join(lines).encode("utf-8"))


def snapshot_facts() -> dict:
    entries = q.status_entries()
    staged = [e for e in entries if e["code"][0] not in " ?"]
    unstaged = [e for e in entries if e["code"][1] not in " ?"]
    untracked = [e for e in entries if e["code"] == "??"]
    unmerged = [e["path"] for e in entries if "U" in e["code"] or e["code"] in ("AA", "DD")]
    use_index = bool(staged)
    selected = staged if use_index else entries
    excluded = sorted({e["path"] for e in unstaged + untracked}) if use_index else []
    files, secrets, identity, scan = [], [], [], []
    for entry in selected:
        path, code = entry["path"], entry["code"]
        file = q.ROOT / path
        deleted = "D" in (code[0] if use_index else code)
        identity.append((path, deleted))
        if entry["original"]:
            identity.append((entry["original"], True))
        size = file.stat().st_size if file.is_file() and not deleted else 0
        binary = bool(size) and b"\0" in file.read_bytes()[:8192]
        notes = []
        if size > LARGE_BYTES:
            notes.append(f"large {size // 1024} KiB")
        if binary:
            notes.append("binary")
        if GENERATED_RE.search(path):
            notes.append("generated?")
        status = code[0] if use_index else ("?" if code == "??" else (code[0] if code[0] != " " else code[1]))
        files.append({"status": status, "path": path, "original": entry["original"], "notes": notes})
        if not deleted and not binary:
            scan.append((path, code == "??"))
    diffs = added_lines_by_path([p for p, untracked in scan if not untracked], use_index)
    for path, untracked in scan:
        secrets += secret_hits(path, untracked_lines(path) if untracked else diffs.get(path, []))
    return {
        "mode": "staged index" if use_index else "all changes (nothing staged)",
        "files": files,
        "excluded": excluded,
        "unmerged": unmerged,
        "secrets": secrets,
        "shortstat": q.git("diff", "--cached" if use_index else "HEAD", "--shortstat"),
        "snapshot_id": snapshot_id(identity, use_index) if identity else None,
    }


def push_facts(facts: dict) -> dict:
    target = facts["upstream"] or "--remotes"
    rev = [f"{facts['upstream']}..HEAD"] if facts["upstream"] else ["HEAD", "--not", "--remotes"]
    commits = []
    for line in q.git("log", "--format=%h%x09%s%x09%(trailers:key=Change-Kind,valueonly,separator=%x2C)", *rev).splitlines():
        sha, subject, kind = (line.split("\t") + ["", ""])[:3]
        commits.append({"sha": sha, "subject": subject, "change_kind": kind.strip() or None})
    return {"compare": target, "commits": commits}


def fetch_branch() -> str | None:
    """Fetch the current branch from origin; return an error message on failure."""
    branch = q.git("branch", "--show-current")
    if not branch:
        return "cannot fetch: HEAD is detached"
    result = subprocess.run(["git", "fetch", "--quiet", "origin", branch], cwd=q.ROOT,
                            capture_output=True, text=True, encoding="utf-8")
    return None if result.returncode == 0 else f"git fetch origin {branch} failed: {result.stderr.strip()}"


def verify_pushed(facts: dict) -> list[str]:
    if not facts["upstream"]:
        return ["no upstream to verify against"]
    head, remote = q.git("rev-parse", "HEAD"), q.git("rev-parse", facts["upstream"])
    facts["verified"] = {"head": head, "upstream_head": remote}
    return [] if head and head == remote else [f"{facts['upstream']} is {remote[:12] or 'unknown'}, HEAD is {head[:12]}"]


def blocking(facts: dict, push: bool) -> list[str]:
    found = [facts["fetch_error"]] if facts.get("fetch_error") else []
    if not facts["branch"]:
        found.append("HEAD is detached")
    found += [f"unresolved {name} in progress" for name in facts["unresolved"]]
    if "verify_failed" in facts:
        return found + facts["verify_failed"]
    if push:
        if not facts["origin"]:
            found.append("no origin remote")
        if facts["branch"] and facts["upstream"] and facts["upstream"] != f"origin/{facts['branch']}":
            found.append(f"upstream {facts['upstream']} is not origin/{facts['branch']}")
        if facts["behind"]:
            found.append(f"branch is {facts['behind']} commit(s) behind {facts['upstream']}; a push would not fast-forward")
        if not facts["push"]["commits"]:
            found.append("nothing to push")
    else:
        snap = facts["snapshot"]
        if snap["unmerged"]:
            found.append("unmerged paths: " + ", ".join(snap["unmerged"]))
        if not snap["files"]:
            found.append("no changes since HEAD")
        found += [f"possible secret ({hit['pattern']}) at {hit['at']}" for hit in snap["secrets"]]
    return found


def print_text(facts: dict, push: bool) -> None:
    print(f"branch: {facts['branch'] or 'DETACHED'}   default: {facts['default_branch'] or 'unknown'}"
          f"{'   (on default branch)' if facts['branch'] and facts['branch'] == facts['default_branch'] else ''}")
    print(f"head: {facts['head']}")
    print(f"origin: {facts['origin'] or 'NONE'}")
    if facts["upstream"]:
        when = "fetched now" if facts.get("fetched") else "as of last fetch"
        print(f"upstream: {facts['upstream']}   ahead {facts['ahead']}   behind {facts['behind']}   ({when})")
    else:
        print("upstream: none")
    if "verify_failed" in facts:
        verified = facts.get("verified")
        if verified and not facts["verify_failed"]:
            print(f"verified: HEAD {verified['head']} == {facts['upstream']} {verified['upstream_head']}")
        else:
            print("verified: NO")
    elif push:
        print(f"commits to push ({len(facts['push']['commits'])}, compared with {facts['push']['compare']}):")
        for commit in facts["push"]["commits"]:
            print(f"  {commit['sha']}  {commit['subject']}   [Change-Kind: {commit['change_kind'] or 'MISSING'}]")
    else:
        snap = facts["snapshot"]
        print(f"snapshot: {snap['mode']}   {snap['shortstat'] or ''}".rstrip())
        print(f"snapshot_id: {snap['snapshot_id']}")
        for file in snap["files"]:
            origin = f" (from {file['original']})" if file["original"] else ""
            notes = f"   [{'; '.join(file['notes'])}]" if file["notes"] else ""
            print(f"  {file['status']} {file['path']}{origin}{notes}")
        if snap["excluded"]:
            print(f"excluded (unstaged or untracked, not in snapshot): {len(snap['excluded'])}")
            for path in snap["excluded"]:
                print(f"  {path}")
        print("recent subjects:")
        for subject in facts["recent_subjects"]:
            print(f"  {subject}")
    print("blocking:" if facts["blocking"] else "blocking: none")
    for finding in facts["blocking"]:
        print(f"  {finding}")


def main() -> int:
    q.utf8_stdio()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--push", action="store_true", help="report the commits a push would publish")
    mode.add_argument("--verify-pushed", action="store_true",
                      help="after a push: fetch, then confirm the upstream equals HEAD")
    parser.add_argument("--fetch", action="store_true", help="with --push: fetch the current branch from origin first")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.fetch and not args.push:
        parser.error("--fetch requires --push")
    fetch_error = fetch_branch() if args.fetch or args.verify_pushed else None
    facts = branch_facts()
    facts["fetch_error"] = fetch_error
    facts["fetched"] = (args.fetch or args.verify_pushed) and not fetch_error
    if args.verify_pushed:
        facts["verify_failed"] = [] if fetch_error else verify_pushed(facts)
    elif args.push:
        facts["push"] = push_facts(facts)
    else:
        facts["snapshot"] = snapshot_facts()
    facts["blocking"] = blocking(facts, args.push)
    if args.json:
        print(json.dumps(facts, indent=2))
    else:
        print_text(facts, args.push)
    return 1 if facts["blocking"] else 0


if __name__ == "__main__":
    sys.exit(main())
