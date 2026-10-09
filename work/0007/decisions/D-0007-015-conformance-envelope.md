---
id: D-0007-015
kind: decision
title: Portable conformance envelope and expected-result conventions
status: open
spec: SPEC-0007
requirements: [R-0007-347]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md, conformance/README.md]
---

# D-0007-015: Conformance Envelope

## Objective

Separate Phase 1's unresolved envelope/procedure decisions from tooling delivery.

## Scope and exclusions

Versioned language-neutral vector envelope, expected results, capability grouping,
and golden regeneration. Initial descriptor fixtures are structural only, not
contract-digest goldens. No .NET-dependent portable expected-result semantics.

## Questions to resolve

What are exact vector/version identities, input and expected-result shapes,
capability grouping, and deterministic regeneration/review conventions?

## Acceptance criteria

- [ ] Normative portable contract and required boundary/error cases are specified.
- [ ] Procedures distinguish authored vectors from generated golden results.
- [ ] Existing descriptor alpha vectors are preserved and accurately labelled.
- [ ] Coordinate .NET consumption with D-0007-013 without coupling portable shape.
- [ ] Checks pass and explicit exact-snapshot review is recorded.

## Resolution

Unresolved. Tooling and published families are subsequent implementation milestones.

## Validation and review

Phase 1 includes this open decision; no envelope format invented during bootstrap.
