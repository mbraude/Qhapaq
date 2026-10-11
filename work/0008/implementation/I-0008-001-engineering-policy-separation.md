---
id: I-0008-001
kind: implementation
granularity: milestone
change_kind: maintenance
title: Separate common and specialized engineering policy
status: open
spec: SPEC-0008
requirements:
  - R-0008-004
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on:
  - D-0008-002
  - D-0008-003
  - D-0008-008
  - D-0008-014
  - I-0008-010
  - I-0008-011
artifacts:
  - docs/development/coding-conventions.md
  - docs/development/conventions/dotnet.md
  - docs/development/conventions/documentation.md
  - docs/development/conventions/schemas.md
  - docs/development/conventions/specifications.md
  - .github/instructions/dotnet.instructions.md
  - .github/instructions/documentation.instructions.md
  - .github/instructions/schemas.instructions.md
  - .github/instructions/specifications.instructions.md
---

# I-0008-001: Separate Common and Specialized Engineering Policy

## Objective and coverage

Deliver the common, language-specific, and artifact-specific policy structure
defined by R-0008-004 and applicable instruction links, including explicit
language-native reference, waiver, invariant, whole-member, and test
placements. Policy may be delivered before a matching checker, but does not
register an extractor or claim language traceability support. This milestone
does not implement or register the checker. It is an aggregate gate, not an
executable slice; its policy outcome depends on both child slices:
[I-0008-010](I-0008-010-dotnet-policy-extraction.md) and
[I-0008-011](I-0008-011-artifact-policy-routing.md).

## Entry gates

D-0008-002, D-0008-003, D-0008-008, and D-0008-014 are complete; affected
specification and ADR amendments are approved; scope readiness is approved.

## File and ownership manifest

The common source remains `docs/development/coding-conventions.md`.
Specialized guides, if required by real consumers, belong beneath
`docs/development/conventions/`, and path routing remains under
`.github/instructions/`. The child slices name the .NET and maintained
artifact-authoring guides and their exact routing files. No guide for an
unselected language or other speculative consumer is delivered.

## Design and integration

Apply common and specialized policies cumulatively. A specialized guide may
explicitly replace a common Default or Recommendation within its declared
scope, but it cannot weaken a common Required rule or override a specification
or ADR. Policy owns each maintained implementation language's unambiguous
native placements; I-0008-007 owns extractor registration and evidence that
the registered extractor matches the approved policy. Policy delivery alone
does not make a language supported for traceability. Link portable
requirements instead of copying them, and keep path-specific instructions as
routing and tool-execution guidance rather than a competing policy source.

## Tests and validation

Validate links, applicability patterns, absence of contradictory duplicate
rules, traceability checks, and any documented policy validation command.

## Exit criteria

- [ ] Approved policy sources and instruction links exist.
- [ ] Native placements and attachment rules are explicit, without claiming
  traceability support before a matching extractor is registered.
- [ ] No portable behavior is duplicated as language policy.
- [ ] Both child slices are complete and their exact output snapshots have
  passed the required validation and explicit delivery review.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
