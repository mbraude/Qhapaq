---
id: I-0007-013
kind: implementation
granularity: milestone
change_kind: requirement
title: Portable instance validation and conservative compatibility
status: open
spec: SPEC-0007
requirements: [R-0007-354, R-0007-355]
depends_on: [I-0007-002, I-0007-005, I-0007-007]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-013: Schema Engine

## Objective and coverage

Phase 5A: instance validation and structural-subtype compatibility, exact numeric
constraint comparisons, narrowing and indeterminate rejection.

## Entry gates

Published relevant schema/compatibility vectors and shared profile foundations.

## File and ownership manifest

Pending approved concrete engine/test files under decided helper ownership.

## Design and integration

Reuse bounded pattern/format algorithms; no host-specific acceptance extensions.

## Tests and validation

Shared instance, compatibility, narrowing-boundary and indeterminate cases,
plus documented build-and-test.

## Exit criteria

- [ ] Specified portable results match all applicable vectors.
- [ ] Required checks and exact human delivery review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No schema engine implemented during extraction.
