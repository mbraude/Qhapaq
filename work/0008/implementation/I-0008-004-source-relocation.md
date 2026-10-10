---
id: I-0008-004
kind: implementation
granularity: milestone
change_kind: refactor
title: Relocate maintained software into the approved taxonomy
status: open
spec: SPEC-0008
requirements: []
depends_on: [D-0008-001, D-0008-009, D-0008-010, D-0008-012]
artifacts:
  - src
---

# I-0008-004: Relocate Maintained Software into the Approved Taxonomy

## Objective and coverage

Relocate approved software workspaces without implicitly changing namespaces,
assemblies, packages, public behavior, or portable contracts. Governing
requirements and the exact move manifest are pending.

## Entry gates

The taxonomy, terminology, ownership, and migration decisions are complete;
R-0000-009 and affected SPEC-0006 requirements are amended; readiness and the
concrete move plan are approved.

## File and ownership manifest

Pending D-0008-012. Concrete slices must list every move and every path update,
including preserved files and excluded repository-root assets.

## Design and integration

Use version-control-preserving moves, maintain self-contained workspaces, and
keep cross-artifact dependencies on supported contracts.

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
