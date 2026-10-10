---
id: D-0008-006
kind: decision
title: Define capability and conformance declarations
status: open
spec: SPEC-0008
requirements: [R-0000-009]
depends_on: [D-0008-004, D-0008-005]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-006: Define Capability and Conformance Declarations

## Objective

Define machine-readable and human-readable declarations for profile support,
capabilities, unsupported behavior, partial progress, and exact evidence.

## Scope and exclusions

A declaration reports support; it does not itself prove conformance or make a
mandatory profile obligation optional. No schema is published by this decision.

## Questions to resolve

Define identities, required fields, capability relationships, unsupported and
partial states, evidence links, failure representation, and validation rules.

## Acceptance criteria

- [ ] Full claims, progress, unsupported behavior, and failures are distinguishable.
- [ ] Declarations bind exact profile and implementation versions.
- [ ] Mandatory obligations cannot be hidden by capability omission.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Add accepted declaration requirements to SPEC-0008.

## Validation and review

No validation or approval recorded.
