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
depends_on: [D-0008-002, D-0008-003, D-0008-008, D-0008-014]
artifacts:
  - docs/development/coding-conventions.md
  - .github/instructions
---

# I-0008-001: Separate Common and Specialized Engineering Policy

## Objective and coverage

Deliver the common, language-specific, and artifact-specific policy structure
defined by R-0008-004 and applicable instruction links, including explicit
language-native reference, waiver, invariant, whole-member, and test
placements. Policy may be delivered before a matching checker, but does not
register an extractor or claim language traceability support. This milestone
does not implement or register the checker.

## Entry gates

D-0008-002, D-0008-003, D-0008-008, and D-0008-014 are complete; affected
specification and ADR amendments are approved; scope readiness is approved.

## File and ownership manifest

The common source remains `docs/development/coding-conventions.md`.
Specialized guides, if required by real consumers, belong beneath
`docs/development/conventions/`, and path routing remains under
`.github/instructions/`. Concrete slices must name the actual guides and
instruction files after the remaining decisions close; no empty guide or
directory is delivered.

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
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
