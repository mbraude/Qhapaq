---
id: I-0007-018
kind: implementation
granularity: milestone
change_kind: requirement
title: Private execution frame and primitive/sequence runner
status: open
spec: SPEC-0007
requirements: [R-0007-361, R-0007-362]
depends_on: [I-0007-017, I-0007-010, I-0007-006]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-018: Frame and Primitive Runner

## Objective and coverage

Phase 7A: validate boundary input and invocation execution/disclosure permission
before effects; private immutable write-once slots; primitive/sequences with
native validation, structured failures and cancellation.

## Entry gates

Completely bound plan, real invocation policy, relevant execution/failure vectors
and approved scope readiness.

## File and ownership manifest

Pending exact frame/runner/policy integration and test slices.

## Design and integration

One non-durable invocation. No frame persistence, ambient inspection or automatic
payload logging, from the first runner slice.

## Tests and validation

Denied permission, invalid boundary input and incomplete plans start no operation;
primitive/sequence frame/failure/cancellation conformance.

## Exit criteria

- [ ] Complete pre-execution safety path and private frame behavior are verified.
- [ ] Required checks and exact-snapshot review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No public execution enablement or runner implementation claimed.
