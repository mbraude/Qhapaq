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
| [Commit](commit/SKILL.md) | Review the selected staged snapshot, or all working-tree changes when nothing is staged, and create a representative local commit with specification trailers without pushing. |
| [Commit without build and test](commit-without-build-and-test/SKILL.md) | Invoke the local commit workflow with build and unit-test validation explicitly skipped. |
| [Push](push/SKILL.md) | Push existing commits from the current branch to the same-named branch on `origin` without committing, integrating, or changing lifecycle state. |
| [Commit and push](commit-and-push/SKILL.md) | Review the selected staged snapshot, or all working-tree changes when nothing is staged, create a representative commit with specification trailers, and push the current branch to `origin`. |
| [Commit and push without build and test](commit-and-push-without-build-and-test/SKILL.md) | Invoke the commit-and-push workflow with build and unit-test validation explicitly skipped. |
| [Open pull request](open-pull-request/SKILL.md) | Validate and publish the current branch, then open one GitHub pull request to the remote default branch for rebase merge without rewriting the source branch. |
| [Approve and commit](approve-commit/SKILL.md) | Resolve a unique ready-for-review target from an ID/path or prompt/editor context, require explicit snapshot approval, record it, and create a local commit without pushing. |
| [Approve, commit, and push](approve-commit-push/SKILL.md) | Resolve a unique ready-for-review target from an ID/path or prompt/editor context, require explicit snapshot approval, default to trace-only validation for design work, and require build/tests for implementation/code before commit and push. |
| [Start work branch](work-branch-start/SKILL.md) | Create or select a safe branch for disruptive or multi-commit work without changing work-item lifecycle state, committing, stashing, or pushing. |
| [Create specification](spec-create/SKILL.md) | Draft or amend platform/component requirements and create initial decision work. |
| [Synchronize work plan](work-plan-sync/SKILL.md) | Bootstrap or reconcile work items from specification changes without executing them. |
| [Edit work plan](work-plan-edit/SKILL.md) | Make bounded planning-only edits while preserving coverage, dependencies, and history. |
| [Show work plan](work-plan-show/SKILL.md) | Display remaining work, blockers, review gates, and a dependency graph without modifying files. |
| [Work-plan diagram](work-plan-diagram/SKILL.md) | Generate a validated, snapshot-stamped Mermaid dependency diagram from selected work plans without changing their status or dependencies. |
| [Next specification decision](spec-next/SKILL.md) | Resolve one eligible decision and stop for review. |
| [Specification readiness](spec-readiness/SKILL.md) | Assess a named scope and exact source snapshot for completeness and prerequisites. |
| [Implementation plan](implementation-plan/SKILL.md) | Detail or revise concrete file, namespace, test, and dependency manifests for delivery slices. |
| [Next implementation slice](implement-next/SKILL.md) | Implement and validate one approved eligible slice, then stop for delivery review. |

The [specification-driven workflow](../../docs/development/spec-driven-workflow.md)
owns the lifecycle and artifact contracts. The skills reuse its
[templates](../../work/templates/); they do not define parallel policy.
`work-plan-sync` handles first-time extraction as well as later reconciliation.
Existing specifications are not migrated until requested. These are AI-led
procedures; deterministic work-plan validation and CI enforcement are not yet
implemented.
