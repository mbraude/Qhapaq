---
id: I-0008-002
kind: implementation
granularity: milestone
change_kind: editorial
title: Audit portable requirements, language contracts, and examples
status: ready-for-review
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

- [x] Audited content uses the approved categories consistently.
- [x] Requirement identities and references remain valid.
- [x] Every example/default in the assigned source set has an explicit recorded disposition.
- [x] Any changed requirement block has reviewed reverse-impact evidence and current references.
- [x] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

The aggregate requires all four child slices complete. A proposed material
requirement amendment is not counted as complete until its separate decision,
readiness, implementation, and review gates are satisfied.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

### Aggregate delivery evidence

The four child slices are complete, and each has explicit delivery approval
for its exact outcome. Together they cover the platform specification library
assigned to this milestone: `SPEC.md` and SPEC-0001 through SPEC-0008. The
records document their audit inventories, classifications, output snapshots,
fingerprint and reverse-impact reviews, validation, exclusions, and delivery
approvals.

| Child slice | Audited output scope | Approved material SHA-256 |
| --- | --- | --- |
| [I-0008-013](I-0008-013-portable-core-example-audit.md) | `SPEC.md`, SPEC-0001, and SPEC-0002 | `9a4bba8d11db0377d23ddd7b0c74f6e5b65168ef5aca68d57e236b1a1e7b8ab7` |
| [I-0008-014](I-0008-014-remaining-portable-specification-audit.md) | SPEC-0003 through SPEC-0005 | `845155260f298315d5ebf1e443c723d82b3990f00ccc344da06e48257e6d6966` |
| [I-0008-015](I-0008-015-portable-binding-specification-audit.md) | SPEC-0007 | `a633715c795a26662eab7e9d45cc3f423a1f328639f4ecfb55303c17089c4c51` |
| [I-0008-016](I-0008-016-language-contract-and-traceability-audit.md) | SPEC-0006, SPEC-0008, and traceability guidance | `798f810a11b98d61cea36ed0ceb2b07885e1d2f42c8f3891596bdd2df5fb4fd8` |

The child delivery approvals remain scoped to their respective outcomes and
are not an aggregate approval. No behavioral or conformance change, contract
publication, or whole-v1 conformance claim is included in this aggregate.

### Aggregate delivery review

This milestone is `ready-for-review`. Explicit review and approval of the
aggregate snapshot remain outstanding; completion is not claimed.
