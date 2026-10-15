---
id: I-0008-007
kind: implementation
granularity: milestone
change_kind: extension
planning_readiness_scope: trace-checker-implementation
title: Implement the deterministic multi-language trace checker
status: open
spec: SPEC-0008
requirements:
  - R-0008-016
  - R-0008-017
  - R-0008-018
  - R-0008-021
depends_on: [D-0008-008, D-0008-011, D-0008-014, D-0008-016, I-0008-001]
artifacts: []
---

# I-0008-007: Implement the Deterministic Multi-language Trace Checker

## Objective and coverage

Deliver registered language-aware extractors and one shared rules engine for
portable reference and waiver payloads, native placement, fingerprints,
reverse-impact inspection, and explicit diagnostics. This milestone owns
extractor registration and evidence that registered extractors match the
approved language-placement policies delivered by I-0008-001. A language is
not supported for traceability until both its policy placements and matching
extractor are registered. This milestone does not add another implementation
language or define CI orchestration.

## Entry gates

D-0008-008, D-0008-011, D-0008-014, and I-0008-001 are complete. D-0008-016
must select and approve the checker architecture and ownership; the affected
specification, ADR, and language-placement policies must remain approved; and
the `trace-checker-implementation` readiness scope must be current and approved
for implementation before concrete slices are created. A planning-only
readiness approval does not satisfy this gate. Each concrete slice must then
have its own current, approved implementation-readiness assessment covering its
exact manifest and specification edits before plan approval or execution.

## File and ownership manifest

Pending approved D-0008-016 selection of tool ownership, implementation
language, package boundary, dependency direction, and commands, followed by a
current approved implementation-readiness assessment and a bounded inventory
of the checker, extractor registrations, fixtures, and integration surfaces.
This milestone owns the registration and policy-match evidence outcomes;
concrete slices must name every production and test file.

## Design and integration

Keep native syntax parsing in registered language extractors. Feed normalized
payload, span, attachment, and production-or-test information into one shared
engine that owns all portable validation and waiver rules. Verify that each
registered extractor accepts exactly the native constructs and attachment
rules in its approved policy. Unsupported placements and extraction failures
must remain explicit failures.

## Tests and validation

Cover valid and malformed payloads, source spans, invariant and test placement,
strings and unsupported constructs, unresolved and retired requirements, stale
fingerprints, changed-requirement reverse impact, waiver scope, extractor
failure, and stable diagnostics for every registered language.

## Exit criteria

- [ ] Registered language extractors and the shared rules engine exist.
- [ ] Each registered extractor is evidenced to match its approved placement
  policy; support is claimed only when both are registered.
- [ ] Portable validation and waiver behavior are not duplicated by extractors.
- [ ] Required checks fail explicitly for every specified invalid condition.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
