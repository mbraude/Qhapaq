---
id: I-0007-022
kind: implementation
granularity: milestone
change_kind: requirement
title: Bounded loops and item/chunk collection execution
status: open
spec: SPEC-0007
requirements: [R-0007-366]
depends_on: [I-0007-021]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-022: Loops and Collections

## Objective and coverage

Phase 7E: bounded loop and forEach item/chunk modes; isolated iteration/invocation
frames, final loop result and ordered collection aggregation.

## Entry gates

Phase 7D and relevant collection/loop limits, failure and scope vectors.

## File and ownership manifest

Pending exact loop/collection scheduling, frames and test slices.

## Design and integration

Preserve isolation, deterministic ordering, concurrency and invocation bounds.

## Tests and validation

Empty inputs, cardinality, chunks, nested scopes, ordering, concurrency, failures,
cancellation and invocation ceilings.

## Exit criteria

- [ ] All bounded loop/collection vectors match specified results.
- [ ] Checks and explicit human delivery review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No loop or collection execution delivered here.
