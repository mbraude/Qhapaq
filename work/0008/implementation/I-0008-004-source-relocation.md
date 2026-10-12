---
id: I-0008-004
kind: implementation
granularity: milestone
change_kind: refactor
title: Relocate maintained software into the approved taxonomy
status: open
spec: SPEC-0008
requirements:
  - R-0000-009
  - R-0000-017
  - R-0000-019
  - R-0000-020
  - R-0008-001
  - R-0008-002
  - R-0008-003
  - R-0008-019
  - R-0008-027
  - R-0008-028
  - R-0008-029
depends_on: [D-0008-001, D-0008-009, D-0008-010, D-0008-012, D-0008-015, I-0008-008]
artifacts:
  - src
  - .agents/skills/build-and-test/SKILL.md
  - .github/instructions/dotnet.instructions.md
---

# I-0008-004: Relocate Maintained Software into the Approved Taxonomy

## Objective and coverage

Relocate approved software workspaces without implicitly changing namespaces,
assemblies, packages, public behavior, or portable contracts. This includes
moving the shared portable-validation project into
`src/common/dotnet/src/` with its tests under `src/common/dotnet/tests/`.
Exact move manifests remain pending.

## Entry gates

The taxonomy, terminology, common-library ownership, and migration decisions
are complete; the separately reviewed Entry Point identity migration is
delivered and approved; R-0000-009, R-0000-019, R-0000-020, and affected
SPEC-0006 requirements are amended; and readiness and the concrete move plan
are approved.

## File and ownership manifest

Pending D-0008-012. Concrete slices must list every move and every path update,
including preserved files and excluded repository-root assets.

## Design and integration

Use version-control-preserving moves, maintain self-contained workspaces, and
keep cross-artifact dependencies on supported contracts. Update the
build-and-test skill, workspace build/test entry points, path instructions,
and CI filters atomically where they must recognize the new workspace roots.

## Tests and validation

Run before-and-after restore, build, architecture, test, package, discovery,
instruction, and link checks plus the approved recovery exercise.

## Exit criteria

- [ ] Every approved move and only those moves is complete.
- [ ] Public identities and behavior are preserved unless separately amended.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
