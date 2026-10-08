# Repository Skills

This directory contains portable, self-contained skills for repeatable
repository capabilities. Each skill belongs in a named subdirectory with a
`SKILL.md` file and may include bounded `scripts/`, `references/`, or `assets/`.

Skills must:

- Have a documented consumer and activation scenario.
- Implement a repeatable capability rather than general repository policy.
- Avoid secrets, private data, machine-specific paths, and undeclared network
  dependencies.
- Defer to [SPEC.md](../../SPEC.md) and future repository-wide guidance.
- Include validation or evaluation material appropriate to their behavior.

Generated pipeline invocation skills are product artifacts governed by
[SPEC-0001](../../specs/0001-core-pipeline-model.md), not repository policy
skills stored here by default.

## Available skills

| Skill | Purpose |
|---|---|
| [Build and test](build-and-test/SKILL.md) | Run the specification trace check, build the .NET solution with locked dependencies, and run every unit test project. |
| [Specification trace check](spec-trace-check/SKILL.md) | AI-led inspection of files changed since `HEAD` that classifies the change, proposes `Change-Kind` and `Spec:` commit trailers, checks identifiers and reference fingerprints, and reviews changed code against the requirements in scope. |
| [Fix bug](fix-bug/SKILL.md) | Fix a defect as a `bug` change: find the governing requirements, add a referencing regression test, apply a minimal fix, and validate. |
| [Commit and push](commit-and-push/SKILL.md) | Review all working-tree changes since `HEAD`, create a representative commit with specification trailers, and push the current branch to `origin`. |
| [Commit and push without build and test](commit-and-push-without-build-and-test/SKILL.md) | Invoke the commit-and-push workflow with build and unit-test validation explicitly skipped. |
