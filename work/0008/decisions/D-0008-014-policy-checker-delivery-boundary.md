---
id: D-0008-014
kind: decision
title: Resolve engineering-policy and trace-checker delivery boundary
status: open
spec: SPEC-0008
requirements:
  - R-0008-004
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on: [D-0008-008, D-0008-011]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - work/0008/implementation/I-0008-001-engineering-policy-separation.md
  - work/0008/implementation/I-0008-007-trace-checker.md
---

# D-0008-014: Resolve Engineering-Policy and Trace-Checker Delivery Boundary

## Objective

Resolve the delivery boundary between publishing language-specific traceability
policy and delivering the matching extractor and shared checker, so no policy
milestone implies language support before its required checker exists.

## Scope and exclusions

R-0008-004 and R-0008-016 through R-0008-018 govern policy ownership,
language-native placements, extractor registration, and checker behavior.
This item must not weaken the requirement that a language is unsupported for
traceability until both its placements and a matching extractor are
registered. It does not implement or select a checker technology.

## Questions to resolve

- May common and specialized policy artifacts be delivered before the checker,
  provided they make no claim that the language is supported?
- Which item owns policy authoring, extractor registration, and evidence that
  the registered placements match the extractor?
- Should I-0008-001 and I-0008-007 be split into ordered child slices or remain
  separate milestones with an explicit dependency?
- Do the existing requirements fully define the support boundary, or does the
  authoritative specification or ADR need amendment?

## Acceptance criteria

- [ ] The policy-only and traceability-support completion boundaries are
  explicit and consistent with R-0008-016 through R-0008-018.
- [ ] Ownership, dependencies, and acceptance gates for I-0008-001 and
  I-0008-007 are reconciled without a cycle or duplicate work.
- [ ] Any newly discovered product or architectural semantics are recorded in
  the governing specification or ADR, not only in the work plan.
- [ ] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

Unresolved. Record the accepted outcome through links to any amended
requirements or ADR and the reconciled implementation items. Do not duplicate
normative semantics here.

## Validation and review

Not started. No implementation, approval, or language-support claim is
authorized by this decision item.
