---
id: I-0007-009
kind: implementation
granularity: milestone
change_kind: requirement
title: Registry core and explicit native bindings
status: open
spec: SPEC-0007
requirements: [R-0007-350, R-0007-413]
depends_on: [D-0007-005, I-0007-008, I-0007-007]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-009: Registry and Native Bindings

## Objective and coverage

Phase 3: immutable exact ID/version/digest lookup; separate implementation/native
identities; explicit generated ingestion; runtime revalidation; conflict/version/
generic agreement; safe availability states and registry generation identity;
and separate immutable contract and implementation-artifact identities.

## Entry gates

Generated contracts and runtime descriptor/manifest/digest validation; reviewed scope.

## File and ownership manifest

Pending concrete registry/native binding and test slice manifests.

## Design and integration

No assembly scanning. Core registry is not a conforming trusted host;
effective-source selection and policy are I-0007-010.

## Tests and validation

Registry/native/version/conflict rejection, clean generated-registration consumer,
supported trimming/AOT, cache-generation identity and build-and-test.

## Exit criteria

- [ ] Exact identities resolve to explicit bindings; ambiguity is unavailable.
- [ ] Required vectors, consumer checks and exact delivery review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No registry or trusted-host conformance claimed.
