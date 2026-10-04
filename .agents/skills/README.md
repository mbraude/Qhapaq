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
| [Build and test](build-and-test/SKILL.md) | Build the .NET solution with locked dependencies and run every unit test project. |
| [Commit and push](commit-and-push/SKILL.md) | Review all working-tree changes since `HEAD`, create a representative commit, and push the current branch to `origin`. |
