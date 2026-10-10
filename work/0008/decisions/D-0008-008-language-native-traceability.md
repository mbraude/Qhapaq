---
id: D-0008-008
kind: decision
title: Define language-native traceability placement and checking
status: open
spec: SPEC-0008
requirements: []
depends_on: [D-0008-002, D-0008-003]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - docs/development/coding-conventions.md
---

# D-0008-008: Define Language-Native Traceability Placement and Checking

## Objective

Define language-native placements and checker architecture for the portable
`spec: <requirement-id>@<fingerprint>` payload without weakening ADR-0003 or
existing waiver and reverse-impact rules.

## Scope and exclusions

No SPEC-0008 requirement exists yet, so the requirement list is empty. This
item does not require C# XML documentation in every language or waive current
traceability obligations.

## Questions to resolve

Define supported comment/documentation constructs, parser boundaries,
invariant and test placement, multi-language scanning, diagnostics, and
extension of current waiver handling.

## Acceptance criteria

- [ ] The marker payload remains portable and exact.
- [ ] Each supported language has unambiguous invariant and test placement.
- [ ] Fingerprint, reverse-impact, and waiver behavior is not weakened.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Record accepted product requirements, policy, and any necessary
superseding ADR in their proper authorities.

## Validation and review

No validation or approval recorded.
