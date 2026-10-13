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
  - R-0009-011
  - R-0009-012
  - R-0009-013
  - R-0009-014
depends_on: [I-0009-001]
artifacts: []
---

# I-0009-002: Adopt Central Derived State in Repository Workflows

## Objective and coverage

Migrate repository workflows that directly compute requirement fingerprints,
reverse-reference indexes, exact-byte source hashes, material hashes, or
source-set digests to the central validated interface. Add validated runbook
freshness, conditional reuse of stored next commands, incremental dependency
invalidation, one final refresh after composed mutations, and exact-snapshot
validation receipts. Preserve each workflow's authoritative input selection,
ordering, digest, approval, and failure semantics.

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
uncached recovery path. Retain mutation-specific preflight for plan approval
and implementation even when global runbook selection is reused.

## Tests and validation

For each consumer, compare before-and-after selected inputs, exact digest
values, ordering, diagnostics, pass/fail outcomes, and persisted evidence.
Include cache miss, invalidation, deletion, and recovery cases.
Cover complete and stale runbook manifests, changed dependency closures,
targeted preflight failures, deferred intermediate rendering, final refresh,
and receipt invalidation after material or environment changes.

## Exit criteria

- [ ] Direct consumers use the central interface without duplicated cache rules.
- [ ] Exact workflow hashes and material-selection semantics are preserved.
- [ ] Stored next commands are used only after complete freshness validation.
- [ ] Incremental invalidation reaches every affected dependent.
- [ ] Composed mutations produce one final current runbook without bypassing
  intermediate review gates.
- [ ] Reused validation receipts bind every required material and environment
  identity.
- [ ] Existing historical approvals and evidence are not rewritten.
- [ ] Required tests and validation pass.
- [ ] Explicit delivery review covers each exact implemented snapshot.

## Plan approval

Absent. This milestone requires consumer inventory and approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
