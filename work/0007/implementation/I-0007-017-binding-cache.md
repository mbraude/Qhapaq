---
id: I-0007-017
kind: implementation
granularity: milestone
change_kind: requirement
title: Complete immutable binding and cache invalidation
status: open
spec: SPEC-0007
requirements: [R-0007-358, R-0007-360]
depends_on: [I-0007-009, I-0007-010, I-0007-012, I-0007-013, I-0007-014, I-0007-015, I-0007-016]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-017: Binding and Cache

## Objective and coverage

Phase 6B: exact resolution/configuration, all-node schema propagation and lexical
sources, compatible connections/native bindings, pre-bound factories/projectors/
materializers/evaluators, slot consumers, nested bounds, effect/capability/
idempotency/connection aggregation, policy and every Section 19 cache input.

## Entry gates

All R-0007-360 prerequisites and exact artifact groups, including failure/control
semantics used by plans. No partial-plan execution permission.

## File and ownership manifest

Pending reviewed binding/analysis/cache/test slice manifests.

## Design and integration

Immutable plans record exact portable and implementation identities. Account for
forEach invocations/aggregation and tryCatch attempt/recovery worst-case resources.

## Tests and validation

All validation stages, lexical scope/dominance, native agreement, policy,
partial rejection and each specified stale-cache invalidation input.

## Exit criteria

- [ ] Section 14 completes before any plan returns.
- [ ] Stale plans cannot be reused; required checks and review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No plan binding or cache delivered during extraction.
