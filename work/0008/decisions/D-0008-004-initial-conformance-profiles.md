---
id: D-0008-004
kind: decision
title: Define initial conformance profiles and dependencies
status: open
spec: SPEC-0008
requirements: [R-0000-007, R-0000-009]
depends_on: [D-0008-003]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-004: Define Initial Conformance Profiles and Dependencies

## Objective

Define the smallest coherent initial profiles, mandatory runtime baseline,
applicability, prerequisite relationships, and permitted compatibility claims.

## Scope and exclusions

Profiles select existing obligations and cannot fork portable semantics, waive
mandatory rules, or imply support for an unimplemented runtime.

## Questions to resolve

Choose initial profile identities and boundaries; define prerequisite profiles,
optional capabilities, remote-client distinctions, and prohibited partial claims.

## Acceptance criteria

- [ ] Each profile has coherent scope, applicability, and explicit prerequisites.
- [ ] Mandatory requirements cannot be downgraded through capability declarations.
- [ ] Claim language is precise and testable.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Add accepted profile requirements to SPEC-0008.

## Validation and review

No validation or approval recorded.
