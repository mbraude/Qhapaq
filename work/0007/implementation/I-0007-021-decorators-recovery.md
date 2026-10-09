---
id: I-0007-021
kind: implementation
granularity: milestone
change_kind: requirement
title: Decorator attempts and lexical recovery
status: open
spec: SPEC-0007
requirements: [R-0007-365]
depends_on: [I-0007-020, I-0007-006]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-021: Decorators and Recovery

## Objective and coverage

Phase 7D: decorator order/attempt/failure/idempotency/unsafe-retry rules; tryCatch,
lexical caught-failure projection, nested recovery and bounded causal trees.

## Entry gates

Phase 7C and exact registered decorator contracts for each enabled slice.
Concrete planning must identify any component decision/implementation prerequisite.

## File and ownership manifest

Pending exact decorator/recovery and test slices; no speculative component types.

## Design and integration

Do not expose raw exceptions, partial try outputs or undeclared frames.
Retained side effects are not rolled back; policy/cancellation remain non-catchable.

## Tests and validation

Nested recovery, cancellation exclusions, retained effects, recovery failure,
attempt bounds, unsafe retry and causal-tree limits.

## Exit criteria

- [ ] Decorator/recovery vectors pass with exact policy and failure preservation.
- [ ] Checks and explicit human review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No rollback or decorator capability claim made during extraction.
