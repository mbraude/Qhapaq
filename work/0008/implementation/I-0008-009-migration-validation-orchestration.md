---
id: I-0008-009
kind: implementation
granularity: milestone
change_kind: extension
title: Establish root migration validation and recovery orchestration
status: open
spec: SPEC-0008
requirements:
  - R-0005-034
  - R-0008-017
  - R-0008-020
  - R-0008-021
  - R-0008-022
  - R-0008-027
  - R-0008-028
  - R-0008-029
depends_on:
  - D-0008-011
  - D-0008-012
  - I-0008-003
  - I-0008-007
artifacts:
  - build
  - scripts
---

# I-0008-009: Establish Root Migration Validation and Recovery Orchestration

## Objective and coverage

Deliver the root adapters, fail-closed impact selection, immutable report
aggregation, and migration checkpoint and recovery entry points required before
the Entry Point identity migration. This milestone does not rename or relocate
source, select concrete command syntax, assemble a release, or publish a
profile or claim.

## Entry gates

D-0008-011 and D-0008-012 are complete; the trace checker and required
conformance artifacts exist; the exact workspace capabilities, impact graph,
report contracts, migration validation matrix, recovery exercise, scope
readiness, and concrete slices are approved.

## File and ownership manifest

Pending concrete command, impact-map, report, and recovery formats. Concrete
slices must enumerate every root adapter, workspace adapter, declarative impact
mapping, validation group, report aggregator, fixture, and documentation
surface without absorbing workspace-native toolchain behavior.

## Design and integration

Root adapters dispatch documented workspace capabilities, expand impact
selection transitively, and fail closed on missing or ambiguous mappings.
Migration entry points record exact before-and-after snapshots, preserve
user-owned changes, aggregate immutable evidence by digest, and reverse only
slice-owned changes through documented non-destructive recovery.

## Tests and validation

Cover each applicable workspace capability, inapplicable declarations,
transitive shared-input fan-out, stale and ambiguous mappings, missing and
digest-mismatched evidence, equivalent before-and-after validation, user-change
preservation, inverse move and dedicated-commit recovery, and prohibition of
history rewriting or destructive resets.

## Exit criteria

- [ ] Root adapters and the declarative impact graph cover every migration validation surface.
- [ ] Required reports and recovery checkpoints are immutable, exact, and independently verifiable.
- [ ] Missing, ambiguous, skipped, unavailable, or unsuccessful validation fails closed.
- [ ] The approved recovery exercise restores the recorded baseline without changing user-owned work.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
