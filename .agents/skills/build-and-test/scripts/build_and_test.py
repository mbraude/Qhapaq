#!/usr/bin/env python3
"""Locked .NET build and unit tests for the build-and-test skill.

Builds implementations/dotnet/Qhapaq.slnx with locked restore, runs every unit
test project under tests/unit/ (never integration tests) with the build's
outputs, and prints a compact summary. When every change since HEAD is on the
documentation and workflow allowlist below, it skips the build and reports
why; --force always builds. It does not run the specification trace check,
which the skill performs first.

Exit code 0 means skipped or passed; 1 means a precondition, build, or test
failure.

Usage:
  python .agents/skills/build-and-test/scripts/build_and_test.py [--force]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
import qhapaq_work as q  # noqa: E402

DOTNET = q.ROOT / "implementations" / "dotnet"
REQUIRED = ["global.json", "Qhapaq.slnx", "NuGet.Config"]
NON_BUILD_RE = re.compile(r"^(work|specs|docs|\.agents|\.github)/|^[^/]+\.md$|^\.git(ignore|attributes)$")
DIAGNOSTIC_RE = re.compile(r": (error|warning) [A-Z]+\d+:")
TEST_SUMMARY_RE = re.compile(
    r"(Passed|Failed)!\s+-\s+Failed:\s+(\d+),\s+Passed:\s+(\d+),\s+Skipped:\s+(\d+),\s+Total:\s+(\d+)")


def run(args: list[str]) -> tuple[int, str, float]:
    start = time.monotonic()
    result = subprocess.run(args, cwd=DOTNET, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return result.returncode, result.stdout + result.stderr, time.monotonic() - start


def tail(output: str, lines: int = 40) -> str:
    return "\n".join("  " + line for line in output.rstrip().splitlines()[-lines:])


def build_inputs_changed() -> list[str]:
    paths = []
    for entry in q.status_entries():
        paths += [p for p in (entry["path"], entry["original"]) if p]
    return sorted({p for p in paths if not NON_BUILD_RE.search(p)})


def main() -> int:
    q.utf8_stdio()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="build and test even when no build input changed")
    args = parser.parse_args()

    changed = build_inputs_changed()
    if not args.force and not changed:
        print("build: skipped - no build inputs changed since HEAD (all changes are documentation or workflow files)")
        print("tests: skipped")
        print("result: PASS (skipped)")
        return 0
    if changed:
        print(f"build inputs changed: {len(changed)} (first: {changed[0]})")

    missing = [name for name in REQUIRED if not (DOTNET / name).is_file()]
    if missing:
        print("precondition: missing " + ", ".join(f"implementations/dotnet/{m}" for m in missing))
        print("result: FAIL")
        return 1
    code, output, _ = run(["dotnet", "--version"])
    if code != 0:
        print("precondition: the .NET SDK selected by global.json is not available")
        print(tail(output, 15))
        print("result: FAIL")
        return 1
    print(f"sdk: {output.strip().splitlines()[-1]}")

    code, output, seconds = run(["dotnet", "build", "Qhapaq.slnx", "-p:RestoreLockedMode=true", "-nologo",
                                 "-tl:off", "-v:minimal", "-clp:Summary"])
    diagnostics = sorted({line.strip() for line in output.splitlines() if DIAGNOSTIC_RE.search(line)})
    errors = [d for d in diagnostics if ": error " in d]
    warnings = [d for d in diagnostics if ": warning " in d]
    print(f"build: {'succeeded' if code == 0 else 'FAILED'} in {seconds:.0f}s   "
          f"warnings {len(warnings)}   errors {len(errors)}")
    for line in (errors + warnings)[:30]:
        print(f"  {line}")
    if code != 0:
        if not errors:
            print(tail(output))
        print("result: FAIL")
        return 1

    projects = sorted(p.relative_to(DOTNET).as_posix() for p in (DOTNET / "tests" / "unit").glob("*/*.csproj"))
    if not projects:
        print("tests: no unit test projects found under implementations/dotnet/tests/unit/")
        print("result: FAIL")
        return 1
    totals = [0, 0, 0, 0]
    failed = False
    for project in projects:
        code, output, seconds = run(["dotnet", "test", project, "--no-build", "--no-restore", "--nologo"])
        match = TEST_SUMMARY_RE.search(output)
        if match:
            counts = [int(match.group(i)) for i in (3, 2, 4, 5)]
            totals = [a + b for a, b in zip(totals, counts)]
            line = f"passed {counts[0]}   failed {counts[1]}   skipped {counts[2]}   total {counts[3]}"
        else:
            line = "no test summary found"
        ok = code == 0 and match is not None
        failed |= not ok
        print(f"test {Path(project).stem}: {'ok' if ok else 'FAILED'} in {seconds:.0f}s   {line}")
        if not ok:
            failures = [l for l in output.splitlines() if re.search(r"^\s*(Failed |error )", l)]
            print("\n".join("  " + l.strip() for l in failures[:20]) if failures else tail(output))
    print(f"tests total: passed {totals[0]}   failed {totals[1]}   skipped {totals[2]}   total {totals[3]}")
    print(f"result: {'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
