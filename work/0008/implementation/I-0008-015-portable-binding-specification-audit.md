---
id: I-0008-015
kind: implementation
granularity: slice
change_kind: editorial
title: Audit portable binding specification examples
status: open
spec: SPEC-0008
requirements:
  - R-0000-007
  - R-0008-005
depends_on:
  - D-0008-003
artifacts:
  - specs/0007-portable-pipeline-definitions-and-binding.md
---

# I-0008-015: Audit Portable Binding Specification Examples

## Objective and coverage

Inventory normative and non-normative content throughout SPEC-0007. Record
the disposition of each example, rationale block, and default that could alter
portable behavior or conformance. Apply R-0008-005 and preserve R-0000-007's
language-neutral boundary. Review links to schemas and conformance material
only to confirm that their ownership and normative status are represented
consistently; those artifacts are not prose examples and are not reclassified
or edited by this slice.

This slice does not assess other numbered specifications, implementation
code, or checker behavior. It does not authorize a behavioral change. If an
audit finding requires a new or changed behavior, stop and raise it for a
separate specification decision and readiness assessment.

## Entry gates

- [ ] D-0008-003 is complete.
- [ ] This exact slice plan has explicit approval.
- [ ] Current implementation readiness is approved for SPEC-0007 if it is
  proposed for editing; planning-readiness for I-0008-002 is insufficient.
- [ ] The audited source snapshot and the aggregate I-0008-002 scope remain
  current.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Modify, only if required for R-0008-005 editorial classification | `specs/0007-portable-pipeline-definitions-and-binding.md` | Audit portable definition and binding requirements, defaults, and examples | Not applicable | Not applicable |

Record the complete inventory, disposition, proposed edits, fingerprints,
reverse-impact references, and validation results in this item's delivery
evidence. Schemas, vectors, profiles, conformance tools, and their README
artifacts remain under their existing owners and are not modified.

## Design and integration

Treat examples inside requirement blocks as normative. A move or rewording is
permitted only when review establishes that it preserves existing required
behavior and conformance expectations; update fingerprints and review all
references for any changed block. Examples outside requirement blocks must be
explicitly illustrative and must not add, relax, or contradict a requirement.
Do not make portable definitions or conformance semantics depend on CLR
implementation details. Any material behavior change is excluded and requires
a separately approved specification amendment.

## Tests and validation

- Run `/spec-trace-check` on the exact changed snapshot; require a passing
  requirement-identity, fingerprint, classification, and reverse-impact
  review.
- Review relative links affected by changed content and `git diff --check`.
- No product build or unit tests apply to a documentation-only editorial
  change. If a behavior change is proposed, stop this slice rather than
  treating product tests as authorization.

## Exit criteria

- [ ] Every example, rationale block, and potentially behavior-affecting
  default in SPEC-0007 has a recorded disposition.
- [ ] Schema and conformance-artifact ownership is preserved.
- [ ] No unapproved behavior or conformance change is included.
- [ ] Changed requirement fingerprints and reverse-impact references are
  verified, if applicable.
- [ ] Required validation passes and explicit delivery review covers the exact
  output snapshot.

## Plan approval

Absent. Approval must cover this exact slice, manifest, dependencies, and
entry gates.

## Delivery evidence and review

No audit inventory, edits, validation, or delivery approval recorded.
