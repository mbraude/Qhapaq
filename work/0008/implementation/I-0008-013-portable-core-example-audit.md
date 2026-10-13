---
id: I-0008-013
kind: implementation
granularity: slice
change_kind: editorial
title: Audit portable core requirements and examples
status: open
spec: SPEC-0008
requirements:
  - R-0000-007
  - R-0001-011
  - R-0001-052
  - R-0002-017
  - R-0008-005
depends_on:
  - D-0008-003
artifacts:
  - SPEC.md
  - specs/0001-core-pipeline-model.md
  - specs/0002-operation-catalogs-and-host-configuration.md
---

# I-0008-013: Audit Portable Core Requirements and Examples

## Objective and coverage

Inventory normative and non-normative content in `SPEC.md` and SPEC-0001 and
SPEC-0002. Record the disposition of each example, rationale block, and
default that could alter portable behavior or conformance. In particular,
assess R-0001-011, R-0001-052, and R-0002-017 without presuming that moving or
relabeling their examples preserves meaning. Keep portable semantics
language-neutral under R-0000-007 and apply R-0008-005.

This slice does not assess other numbered specifications, schemas, conformance
vectors, implementation code, or checker behavior. It does not authorize a
behavioral change. If an audit finding requires a new or changed behavior,
stop and raise it for a separate specification decision and readiness
assessment.

## Entry gates

- [ ] D-0008-003 is complete.
- [ ] This exact slice plan has explicit approval.
- [ ] Current implementation readiness is approved for every specification
  file proposed for editing; planning-readiness for I-0008-002 is insufficient.
- [ ] The audited source snapshots and the aggregate I-0008-002 scope remain
  current.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Modify, only if required for R-0008-005 editorial classification | `SPEC.md` | Audit and clarify portable platform requirements and examples | Not applicable | Not applicable |
| Modify, only if required for R-0008-005 editorial classification | `specs/0001-core-pipeline-model.md` | Audit core pipeline requirements and examples | Not applicable | Not applicable |
| Modify, only if required for R-0008-005 editorial classification | `specs/0002-operation-catalogs-and-host-configuration.md` | Audit catalog and host-configuration requirements and examples | Not applicable | Not applicable |

Record the complete inventory, disposition, proposed edits, fingerprints,
reverse-impact references, and validation results in this item's delivery
evidence. No separate worksheet or production artifact is created.

## Design and integration

Treat examples inside requirement blocks as normative. A move or rewording is
permitted only when review establishes that it preserves existing required
behavior and conformance expectations; update fingerprints and review all
references for any changed block. Examples outside requirement blocks must be
explicitly illustrative and must not add, relax, or contradict a requirement.
Do not transfer implementation-specific contracts into portable requirements.
Any material behavior change is excluded and requires a separately approved
specification amendment.

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
  default in the assigned files has a recorded disposition.
- [ ] The named candidate requirements have explicit evidence-based
  classifications, whether or not edits are warranted.
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
