---
id: I-0007-023
kind: implementation
granularity: milestone
change_kind: requirement
title: Integrated runner budgets, failures and privacy
status: open
spec: SPEC-0007
requirements: [R-0007-367]
depends_on: [I-0007-018, I-0007-019, I-0007-020, I-0007-021, I-0007-022, I-0007-006]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-023: Integrated Runner

## Objective and coverage

Phase 7F: enforce nested frame/transform/collection/loop/parallel/output budgets,
duration/operation/attempt/iteration limits, failures, cancellation and privacy.

## Entry gates

All runner milestones and applicable Phase 1 vectors are delivered and reviewed.

## File and ownership manifest

Pending integrated limits and cross-composition test slices.

## Design and integration

Reuse existing typed composition only where semantics match. No partial success,
payload leaks, or side effects before complete validation/binding/permission.

## Tests and validation

Complete runner execution/cancellation/aggregate/budget/privacy vectors and
pre-execution negative tests; documented build-and-test.

## Exit criteria

- [ ] Complete execution suite and cross-composition budgets pass.
- [ ] Safety path, checks and exact human delivery review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No public execution enabled by this extraction.
