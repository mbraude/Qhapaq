#!/usr/bin/env python3
"""Deterministic facts for the spec-trace-check skill.

Computes steps 1-4 of the trace check and the inputs to step 5: scope
classification, identifier and block checks for changed specifications,
changed and retired blocks with stale references, and reference and waiver
grammar in changed code. It reports facts and mechanical errors only; change
classification beyond the documented fast path, component version semantics,
warnings that need judgment, and the semantic review remain with the skill.
Read-only and stateless.

Usage:
  python .agents/scripts/trace_facts.py [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys

import qhapaq_work as q

PRODUCT_RE = re.compile(r"(^|/)(Qhapaq\.Service\.V[^/]*|Qhapaq\.Business|Qhapaq\.DAL|Qhapaq\.Implementations\.[^/]+)/")
TEST_RE = re.compile(r"^implementations/[^/]+/tests/")
GENERATED_RE = re.compile(r"(^|/)(bin|obj|artifacts)/")
LOCK_RE = re.compile(r"(^|/)(packages\.lock\.json|package-lock\.json|yarn\.lock|pnpm-lock\.yaml|Cargo\.lock|poetry\.lock)$")
CODE_EXT = {".cs", ".fs", ".vb", ".csproj", ".props", ".targets", ".py", ".ps1", ".psm1", ".sh", ".js", ".mjs",
            ".ts", ".java", ".go", ".rs", ".c", ".cpp", ".h"}
TAG_LIKE_RE = re.compile(r"\*\*\[\s*[Rr]-[^\]]*\]\*\*")
STRICT_TAG_RE = re.compile(r"^\*\*\[R-(C?\d{4})-(\d{3,})\]\*\*")
REF_TOKEN_RE = re.compile(r"^R-(C?\d{4})-(\d{3,})@([0-9a-f]{6})$")
SPEC_COMMENT_RE = re.compile(r"(?://|<remarks>).*?\bspec:\s*(.*)$")
WAIVE_RE = re.compile(r"(?://|<remarks>).*?\bspec-waive:\s*(.*)$")
WAIVABLE = {"untraced-behavior", "conformance", "unsupported-reference", "invariant-marker", "test-reference"}
PLACEHOLDER_RE = re.compile(r"^(tbd|todo|n/?a|none|\.\.\.|-+|xxx)$", re.I)


def status_entries() -> list[dict]:
    return q.status_entries()


def classify(path: str) -> str:
    if q.is_spec_path(path):
        return "component-specification" if path.startswith("specs/components/") else "specification"
    suffix = "." + path.rsplit(".", 1)[-1] if "." in path.rsplit("/", 1)[-1] else ""
    if suffix in CODE_EXT:
        if TEST_RE.match(path):
            return "test-code"
        if PRODUCT_RE.search(path):
            return "product-code"
        return "other-code"
    return "other"


def is_binary(path: str) -> bool:
    file = q.ROOT / path
    return file.is_file() and b"\0" in file.read_bytes()[:8192]


def added_lines(entry: dict) -> list[tuple[int, str]]:
    """New-side (line, text) pairs added or changed relative to HEAD; every line for new files."""
    path = entry["path"]
    file = q.ROOT / path
    if not file.is_file():
        return []
    if entry["code"] in ("??", "A ", "AM") or q.head_text(entry["original"] or path) is None:
        return list(enumerate(file.read_text(encoding="utf-8", errors="replace").splitlines(), 1))
    diff = q.git("diff", "HEAD", "-U0", "--no-color", "--no-ext-diff", "-M", "--", path)
    result, number = [], 0
    for line in diff.splitlines():
        hunk = re.match(r"^@@ -\S+ \+(\d+)(?:,\d+)? @@", line)
        if hunk:
            number = int(hunk.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            result.append((number, line[1:]))
            number += 1
    return result


def tag_findings(path: str, text: str) -> list[dict]:
    """Identifier placement and grammar errors in a specification's current text."""
    expected = q.spec_number(path)
    errors: list[dict] = []
    seen: dict[str, int] = {}
    lines = re.split(r"\r?\n", text)
    fence = False
    for number, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        for match in TAG_LIKE_RE.finditer(line):
            where = f"{path}:{number}"
            if fence:
                errors.append({"at": where, "error": f"tag {match.group(0)} inside a code fence"})
                continue
            if match.start() != 0:
                errors.append({"at": where, "error": f"tag {match.group(0)} not at the start of a top-level paragraph"})
                continue
            strict = STRICT_TAG_RE.match(line)
            if not strict:
                errors.append({"at": where, "error": f"malformed identifier {match.group(0)}"})
                continue
            key = f"R-{strict.group(1)}-{strict.group(2)}"
            if expected and strict.group(1) != expected:
                errors.append({"at": where, "error": f"{key} uses specification number {strict.group(1)}; expected {expected}"})
            if key in seen:
                errors.append({"at": where, "error": f"{key} duplicates the tag at line {seen[key]}"})
            seen.setdefault(key, number)
            rest = line[strict.end():]
            if rest and not (rest.startswith(" ") and rest.strip()):
                errors.append({"at": where, "error": f"{key} must be followed by one space and text, or by nothing and a blank line"})
            if not rest and number < len(lines) and lines[number].strip():
                errors.append({"at": where, "error": f"{key} has no text on its line and is not followed by a blank line"})
    return errors


def spec_facts(entry: dict, current_index: dict[str, dict]) -> dict:
    path = entry["path"]
    old_text = q.head_text(entry["original"] or path) or ""
    new_text = (q.ROOT / path).read_text(encoding="utf-8") if (q.ROOT / path).is_file() else ""
    old = q.requirement_index(old_text)
    new = q.requirement_index(new_text)
    errors = tag_findings(path, new_text) if new_text else []
    removed = [k for k in old if k not in new]
    for key in removed:
        errors.append({"at": f"{path}", "error": f"{key} present at HEAD was removed; retire it with a tombstone instead"})
    added = [k for k in new if k not in old]
    if added:
        prefix = q.spec_number(path)
        sequences = [int(k.rsplit("-", 1)[1]) for k in old if prefix and k.startswith(f"R-{prefix}-")]
        next_seq = max(sequences, default=0) + 1
        for key in sorted(added, key=lambda k: new[k]["line"] or 0):
            if not key.startswith(f"R-{prefix}-"):
                continue
            seq = int(key.rsplit("-", 1)[1])
            if seq != next_seq:
                errors.append({"at": f"{path}:{new[key]['line']}", "error": f"new {key} is not the next unused sequence number (expected {next_seq:03d})"})
            next_seq = max(next_seq, seq) + 1
    changed = [k for k in new if k in old and new[k]["fingerprint"] != old[k]["fingerprint"]]
    retired_now = [k for k in new if new[k]["retired"] and not (k in old and old[k]["retired"])]
    reinstated = [k for k in new if k in old and old[k]["retired"] and not new[k]["retired"]]
    for key in reinstated:
        errors.append({"at": f"{path}:{new[key]['line']}", "error": f"{key} was retired at HEAD and is reused"})
    return {
        "path": path,
        "added": [f"{k}@{new[k]['fingerprint']}" for k in added],
        "changed": [{"id": k, "old": old[k]["fingerprint"], "new": new[k]["fingerprint"], "line": new[k]["line"]} for k in changed],
        "retired": retired_now,
        "removed": removed,
        "errors": errors,
        "_old": old,
    }


def stale_references(specs: list[dict], current_index: dict[str, dict]) -> list[dict]:
    targets: dict[str, set[str]] = {}
    for spec in specs:
        for change in spec["changed"]:
            targets.setdefault(change["id"], set()).add(change["old"])
        for key in spec["retired"] + spec["removed"]:
            targets.setdefault(key, set())
    if not targets:
        return []
    args = ["grep", "-n", "-I", "--untracked", "--no-color"]
    for key in targets:
        args += ["-e", f"{key}@"]
    rows = []
    for line in q.git(*args).splitlines():
        path, number, content = line.split(":", 2)
        for key, fp in re.findall(r"\b(R-C?\d{4}-\d{3,})@([0-9a-f]{6})\b", content):
            if key not in targets:
                continue
            info = current_index.get(key)
            if info is None or info["retired"]:
                problem = "references a retired or removed requirement"
            elif fp != info["fingerprint"]:
                problem = f"carries fingerprint {fp}; current is {info['fingerprint']}"
            else:
                continue
            rows.append({"at": f"{path}:{number}", "id": key, "problem": problem, "markdown": path.endswith(".md")})
    return rows


def code_facts(entry: dict, current_index: dict[str, dict]) -> dict:
    path = entry["path"]
    refs, errors, waivers = [], [], []
    for number, line in added_lines(entry):
        where = f"{path}:{number}"
        spec = SPEC_COMMENT_RE.search(line)
        if spec:
            value = re.sub(r"</remarks>.*$", "", spec.group(1)).strip()
            for token in [t.strip() for t in value.split(",")]:
                match = REF_TOKEN_RE.match(token)
                if not match:
                    errors.append({"at": where, "error": f"reference {token!r} does not match R-<spec>-<seq>@<fingerprint>"})
                    continue
                key = token.split("@")[0]
                info = current_index.get(key)
                if info is None:
                    errors.append({"at": where, "error": f"{key} does not exist"})
                elif info["retired"]:
                    errors.append({"at": where, "error": f"{key} is retired"})
                elif match.group(3) != info["fingerprint"]:
                    errors.append({"at": where, "error": f"{token} is stale; current fingerprint is {info['fingerprint']}"})
                refs.append({"at": where, "ref": token})
        waive = WAIVE_RE.search(line)
        if waive:
            body = re.sub(r"</remarks>.*$", "", waive.group(1)).strip()
            parts = re.split(r"\s*—\s*|\s+--?\s+|\s+--?$", body, maxsplit=1)
            rules = [r.strip() for r in parts[0].split(",") if r.strip()]
            justification = parts[1].strip() if len(parts) > 1 else ""
            bad = [r for r in rules if r not in WAIVABLE]
            if not rules or bad:
                errors.append({"at": where, "error": f"spec-waive names unknown or non-waivable rule(s): {', '.join(bad) or '(none)'}"})
            if not justification or PLACEHOLDER_RE.match(justification):
                errors.append({"at": where, "error": "spec-waive has no justification"})
            waivers.append({"at": where, "rules": rules, "justification": justification})
    return {"path": path, "references": refs, "waivers": waivers, "errors": errors}


def collect() -> dict:
    files, excluded = [], []
    for entry in status_entries():
        path = entry["path"]
        if GENERATED_RE.search(path) or LOCK_RE.search(path) or is_binary(path):
            excluded.append(path)
            continue
        entry["class"] = classify(path)
        entry["deleted"] = "D" in entry["code"]
        files.append(entry)
    current_index: dict[str, dict] = {}
    for path in q.spec_paths():
        for key, info in q.requirement_index((q.ROOT / path).read_text(encoding="utf-8")).items():
            current_index.setdefault(key, {**info, "path": path})

    specs = [spec_facts(e, current_index) for e in files if e["class"] in ("specification", "component-specification")]
    code = [code_facts(e, current_index) for e in files if e["class"].endswith("code") and not e["deleted"]]
    stale = stale_references(specs, current_index)
    errors = [e for s in specs for e in s["errors"]] + [e for c in code for e in c["errors"]]
    reported = {(e["at"], e["error"].split("@")[0].split(" ")[0]) for e in errors}
    errors += [{"at": r["at"], "error": f"{r['id']} {r['problem']}"} for r in stale
               if not r["markdown"] and (r["at"], r["id"]) not in reported]
    classes = {e["class"] for e in files}
    fast_path = bool(files) and classes <= {"other", "other-code"} and not errors
    return {
        "head": q.git("rev-parse", "HEAD"),
        "files": [{"path": e["path"], "status": e["code"].strip(), "class": e["class"],
                   **({"original": e["original"]} if e["original"] else {})} for e in files],
        "excluded": excluded,
        "specifications": [{k: v for k, v in s.items() if not k.startswith("_")} for s in specs],
        "stale_references": stale,
        "code": [c for c in code if c["references"] or c["waivers"] or c["errors"]],
        "new_waivers": [w for c in code for w in c["waivers"]],
        "mechanical_errors": errors,
        "fast_path": fast_path,
        "result": ("PASS (no changes)" if not files else
                   "PASS - Change-Kind: maintenance; no Spec trailer; steps 2-4 and 6 not applicable" if fast_path else
                   "FAIL - mechanical errors" if errors else
                   "INCOMPLETE - complete step 2 judgment checks, step 5 classification, and step 6 review"),
    }


def print_text(facts: dict) -> None:
    print(f"head={facts['head']}")
    print("\n# Scope")
    for f in facts["files"]:
        origin = f" (from {f['original']})" if f.get("original") else ""
        print(f"{f['status']:<3} {f['class']:<24} {f['path']}{origin}")
    if facts["excluded"]:
        print("excluded: " + ", ".join(facts["excluded"]))
    for spec in facts["specifications"]:
        print(f"\n# Specification {spec['path']}")
        print("added: " + (", ".join(spec["added"]) or "none"))
        print("changed: " + (", ".join(f"{c['id']}@{c['old']}->{c['new']} (L{c['line']})" for c in spec["changed"]) or "none"))
        print("retired: " + (", ".join(spec["retired"]) or "none"))
        print("removed: " + (", ".join(spec["removed"]) or "none"))
    if facts["stale_references"]:
        print("\n# References to changed or retired blocks")
        for r in facts["stale_references"]:
            print(f"{'markdown (illustrative; judge)' if r['markdown'] else 'error':<30} {r['at']} {r['id']} {r['problem']}")
    if facts["code"]:
        print("\n# Code references and waivers in changed lines")
        for c in facts["code"]:
            for r in c["references"]:
                print(f"ref    {r['at']} {r['ref']}")
            for w in c["waivers"]:
                print(f"waiver {w['at']} rules={','.join(w['rules'])} justification={w['justification']!r}")
    print("\n# Mechanical errors")
    for e in facts["mechanical_errors"] or [{"at": "", "error": "none"}]:
        print(f"- {e['at']} {e['error']}".replace("-  ", "- "))
    print(f"\nresult: {facts['result']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic spec-trace-check facts for changes since HEAD.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    q.utf8_stdio()
    facts = collect()
    if args.json:
        print(json.dumps(facts, indent=1))
    else:
        print_text(facts)
    return 1 if facts["mechanical_errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
