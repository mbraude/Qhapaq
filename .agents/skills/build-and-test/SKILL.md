---
name: build-and-test
description: Check specification traceability of changed files, restore locked dependencies, build the Qhapaq .NET solution, and run every unit test project, skipping the build when only documentation or workflow files changed. Use when the user asks to build and run unit tests or before committing repository changes.
---

# Build and Test

Use this skill in the Qhapaq repository to verify that changed files trace to
the specifications, the .NET solution builds, and all unit tests pass.
Integration tests are outside this skill's scope.

## Arguments

- `skip-semantic-review` (optional boolean, default: `false`): Passed through
  to `spec-trace-check`. Honor it only when the user explicitly supplies it;
  never infer it.
- `change-kind` (optional): Passed through to `spec-trace-check` when the user
  states the kind of change.

## Preconditions

1. Read and follow the repository's contributor and agent instructions.
2. Inspect the complete working-tree status so the report can distinguish
   validation from unrelated or concurrent changes.

The build script checks that `implementations/dotnet/global.json`,
`Qhapaq.slnx`, and `NuGet.Config` exist and that the .NET SDK selected by
`global.json` is available, and fails when they are not.

Do not modify source files, dependency manifests, lock files, or build
configuration as part of this skill. Do not install or update an SDK or restore
tool unless the user explicitly requests it.

## Workflow

Stop at the first failing step, preserve its output, and report the failure
without claiming later steps passed.

### 1. Check specification traceability

Invoke the repository's `spec-trace-check` skill on the current working tree,
passing `skip-semantic-review` and `change-kind` when the user supplied them.
It inspects only files changed since `HEAD`. If its verdict is `FAIL`, stop
and report its errors without building. Carry its warnings, change kind, and
proposed commit trailers into the final report.

### 2. Build and run unit tests

Run the build script once from the repository root:

```text
python .agents/skills/build-and-test/scripts/build_and_test.py
```

It runs, from `implementations/dotnet/`:

```text
dotnet build Qhapaq.slnx -p:RestoreLockedMode=true
dotnet test tests/unit/<project>/<project>.csproj --no-build --no-restore
```

The build performs locked restore and fails when a dependency manifest and its
lock file disagree. The script runs every project under `tests/unit/`, even
one without substantive behavioral tests, and never runs a solution-wide test,
because that would also run integration tests. It prints build warning and
error counts, per-project and overall test totals, and a final `result:` line;
exit code `1` means failure. Do not rerun these commands by hand or reparse
the full logs; read the failure excerpt the script prints.

When every change since `HEAD` is a documentation or workflow file (under
`work/`, `specs/`, `docs/`, `.agents/`, or `.github/`, a root Markdown file,
`.gitignore`, or `.gitattributes`), nothing the build consumes changed, so the
script skips the build and tests and reports `result: PASS (skipped)`. Pass
`--force` when the user asks for a full build regardless.

### 3. Report

Report:

- the specification trace-check verdict, its findings, the change kind, and
  the proposed commit trailers;
- whether the locked build succeeded, or that it was skipped because no build
  input changed;
- the warning and error counts reported by the build;
- the pass, fail, and skip totals for each unit test project;
- the overall unit-test totals; and
- the first failed command and relevant error output when validation stops.

Do not report success unless the trace check did not fail and the build script
reported `PASS` or `PASS (skipped)`.
