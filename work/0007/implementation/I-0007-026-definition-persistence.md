---
id: I-0007-026
kind: implementation
granularity: milestone
change_kind: requirement
title: Canonical definition persistence and exact resolution
status: open
spec: SPEC-0007
requirements: [R-0007-370]
depends_on: [I-0007-016]
artifacts: [implementations/dotnet, conformance]
---

# I-0007-026: Definition Persistence

## Objective and coverage

Track the first companion obligation: canonical persistence and exact definition
ID/version/digest resolution after normalization.

## Entry gates

Phase 6A and exact governing persistence contracts under SPEC-0001/0006, assessed
before slice planning. This item tracks integration, not ownership of those contracts.

## File and ownership manifest

Pending concrete persistence/resolution and consumer/test slices.

## Design and integration

Never persist execution frames or treat disposable cached plans as portable definitions.

## Tests and validation

Canonical byte/digest integrity, exact resolution, absence/conflicts, persistence
boundaries and applicable store/Service conformance.

## Exit criteria

- [ ] Exact canonical store behavior conforms to its governing sources.
- [ ] Required artifacts, checks and explicit review exist before advertisement.

## Plan approval

Absent; companion milestone only.

## Delivery evidence and review

No store or durable execution capability delivered here.
