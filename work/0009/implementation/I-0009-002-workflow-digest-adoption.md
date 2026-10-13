---
id: I-0009-002
kind: implementation
granularity: milestone
change_kind: requirement
title: Adopt central derived state in repository workflows
status: open
spec: SPEC-0009
requirements:
  - R-0009-004
  - R-0009-005
  - R-0009-007
depends_on: [I-0009-001]
artifacts: []
---

# I-0009-002: Adopt Central Derived State in Repository Workflows

## Objective and coverage

Migrate repository workflows that directly compute requirement fingerprints,
reverse-reference indexes, exact-byte source hashes, material hashes, or
source-set digests to the central validated interface. Preserve each
workflow's authoritative input selection, ordering, digest, approval, and
failure semantics.

## Entry gates

I-0009-001 is complete. Every affected workflow has current scoped readiness
and approved concrete slices with exact manifests. Existing workflow evidence
and approvals remain bound to their historical snapshots.

## File and ownership manifest

Pending a complete consumer inventory, scoped readiness, and concrete slice
planning. Skills that only delegate to a central validation skill should not
duplicate cache-specific behavior.

## Design and integration

Centralize derivation and cache validation while leaving orchestration,
material-input selection, semantic review, and approval decisions with their
owning workflows. Migrate bounded consumer groups incrementally and preserve an
uncached recovery path.

## Tests and validation

For each consumer, compare before-and-after selected inputs, exact digest
values, ordering, diagnostics, pass/fail outcomes, and persisted evidence.
Include cache miss, invalidation, deletion, and recovery cases.

## Exit criteria

- [ ] Direct consumers use the central interface without duplicated cache rules.
- [ ] Exact workflow hashes and material-selection semantics are preserved.
- [ ] Existing historical approvals and evidence are not rewritten.
- [ ] Required tests and validation pass.
- [ ] Explicit delivery review covers each exact implemented snapshot.

## Plan approval

Absent. This milestone requires consumer inventory and approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
