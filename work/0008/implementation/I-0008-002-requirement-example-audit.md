---
id: I-0008-002
kind: implementation
granularity: milestone
change_kind: editorial
title: Audit portable requirements, language contracts, and examples
status: open
spec: SPEC-0008
requirements:
  - R-0000-007
  - R-0008-005
depends_on:
  - D-0008-003
  - I-0008-013
  - I-0008-014
  - I-0008-015
  - I-0008-016
artifacts:
  - SPEC.md
  - specs
  - docs/architecture/decisions/0003-enforce-specification-traceability.md
  - work/0008/implementation/I-0008-013-portable-core-example-audit.md
  - work/0008/implementation/I-0008-014-remaining-portable-specification-audit.md
  - work/0008/implementation/I-0008-015-portable-binding-specification-audit.md
  - work/0008/implementation/I-0008-016-language-contract-and-traceability-audit.md
---

# I-0008-002: Audit Portable Requirements, Language Contracts, and Examples

## Objective and coverage

Review the full platform specification library and its traceability guidance,
then apply the approved separation of portable requirements, language-specific
contracts, rationale, illustrative examples, and normative examples defined by
R-0008-005. Four disjoint child slices audit SPEC.md and specs/0001 through
specs/0008. The audit records a disposition for every example and default that
could affect conformance, including the R-0001-011, R-0001-052, and R-0002-017
candidates. Existing conformance vectors and schemas are checked for boundary
consistency; they are not reclassified as prose examples.

## Entry gates

D-0008-003 is complete; the four child plans are approved; affected requirement
fingerprints and reverse-impact scope are known; and current readiness is
approved for each specification that an implementation slice will edit. The
approved requirement-example-audit readiness record permits planning only and
does not by itself authorize specification edits.

## File and ownership manifest

Concrete slices name disjoint specification sets and their directly affected
traceability or conformance documentation. Their delivery evidence records the
reviewed example/default inventory and disposition, exact edited blocks and
fingerprints, reverse-impact references, and validation results. Changes that
would alter required product behavior, rather than clarify its expression,
remain outside this milestone pending a separately approved amendment.

## Design and integration

Keep portable requirements implementation-neutral, keep language contracts in
explicitly scoped implementation specifications, and apply the required
illustrative or normative example labels. An example inside a requirement
block is normative unless review determines that it only explains already
specified behavior and can be moved without changing conformance expectations.
Preserve stable requirement identifiers and update every fingerprint
reference when requirement-block text changes. If the correct classification
requires a behavior or conformance change, stop that edit for an approved
specification amendment and reassessed scope.

## Tests and validation

For every child slice, run specification traceability, relative-link checks,
requirement-identifier and fingerprint validation, and a whole-repository
reverse-impact review for changed blocks. Run only documented tests applicable
to an approved normative change; documentation-only classification or
editorial corrections do not require product build or unit tests. No
undocumented command is introduced by this audit.

## Exit criteria

- [ ] Audited content uses the approved categories consistently.
- [ ] Requirement identities and references remain valid.
- [ ] Every example/default in the assigned source set has an explicit recorded disposition.
- [ ] Any changed requirement block has reviewed reverse-impact evidence and current references.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

The aggregate requires all four child slices complete. A proposed material
requirement amendment is not counted as complete until its separate decision,
readiness, implementation, and review gates are satisfied.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
