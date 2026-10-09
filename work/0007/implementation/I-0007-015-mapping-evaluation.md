---
id: I-0007-015
kind: implementation
granularity: milestone
change_kind: requirement
title: Complete mapping evaluation and portable budgets
status: open
spec: SPEC-0007
requirements: [R-0007-354, R-0007-357]
depends_on: [I-0007-014, I-0007-013, I-0007-004]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-015: Mapping Evaluation

## Objective and coverage

Phase 5C: every selected operator, conversions and checked failures, expression/
collection/memory/output budgets and deterministic accounting.

## Entry gates

Mapping inference, instance validation and actual evaluation/failure vectors.

## File and ownership manifest

Pending capability-group slices with exact evaluator/helper/test files.

## Design and integration

No executable source, general interpreter facilities or incomplete v1 operator claim.

## Tests and validation

All deterministic evaluation, conversion, portable-limit boundaries, runtime
failures and exact budget vectors.

## Exit criteria

- [ ] Complete instance/compatibility/mapping/transform-failure suites pass.
- [ ] Exact budget behavior and human delivery review are verified.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No operator implementation or partial conformance declared.
