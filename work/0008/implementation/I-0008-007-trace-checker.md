---
id: I-0008-007
kind: implementation
granularity: milestone
change_kind: extension
title: Implement the deterministic multi-language trace checker
status: open
spec: SPEC-0008
requirements:
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on: [D-0008-008, D-0008-011]
artifacts: []
---

# I-0008-007: Implement the Deterministic Multi-language Trace Checker

## Objective and coverage

Deliver registered language-aware extractors and one shared rules engine for
portable reference and waiver payloads, native placement, fingerprints,
reverse-impact inspection, and explicit diagnostics. This milestone does not
add another implementation language or define CI orchestration.

## Entry gates

D-0008-008 and D-0008-011 are complete; the affected specification, ADR, and
language-placement policies are approved; scope readiness and concrete slices
are approved.

## File and ownership manifest

Pending an approved tool ownership decision, implementation language, and
bounded inventory of the checker, extractor registrations, fixtures, and
integration surfaces. Concrete slices must name every production and test file.

## Design and integration

Keep native syntax parsing in registered language extractors. Feed normalized
payload, span, attachment, and production-or-test information into one shared
engine that owns all portable validation and waiver rules. Unsupported
placements and extraction failures must remain explicit failures.

## Tests and validation

Cover valid and malformed payloads, source spans, invariant and test placement,
strings and unsupported constructs, unresolved and retired requirements, stale
fingerprints, changed-requirement reverse impact, waiver scope, extractor
failure, and stable diagnostics for every registered language.

## Exit criteria

- [ ] Registered language extractors and the shared rules engine exist.
- [ ] Portable validation and waiver behavior are not duplicated by extractors.
- [ ] Required checks fail explicitly for every specified invalid condition.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
