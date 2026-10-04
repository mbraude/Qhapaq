# Build-and-Test Skill Evaluation

## Capability

Evaluate whether the
[build-and-test skill](../../.agents/skills/build-and-test/SKILL.md) performs a
locked build of the Qhapaq .NET solution and runs every unit test project
without running integration tests.

## Test environment

Use a Qhapaq working tree with the SDK pinned by
`implementations/dotnet/global.json` installed and package lock files present.
Do not use private package sources or credentials.

## Required behavior

An invocation passes when it:

1. reads the repository instructions and inspects working-tree status;
2. runs the locked solution build from `implementations/dotnet/`;
3. stops without testing if the build fails;
4. runs each of the four projects under `tests/unit/` with `--no-build` and
   `--no-restore`;
5. does not run any project under `tests/integration/`;
6. stops at the first failed unit-test project; and
7. accurately reports build diagnostics and per-project and overall test
   totals.

## Failure cases

Evaluate each case independently. The invocation must report failure without
modifying repository files when:

- the pinned SDK is unavailable;
- locked restore detects an out-of-date lock file;
- compilation fails;
- a unit test fails; or
- a required unit-test project is missing.

The invocation must not install an SDK, update dependencies or lock files,
change build configuration, or claim that unrun checks passed.

## Regression expectations

- Integration tests are not run.
- Source and configuration files are not modified.
- Build output is not committed.
- A successful report requires all defined steps to succeed.
