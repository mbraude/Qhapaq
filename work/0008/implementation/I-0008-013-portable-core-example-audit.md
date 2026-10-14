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

Explicitly approved in this session on 2026-10-13 for this exact slice,
manifest, dependencies, entry gates, tests, validation, and exclusions. This
approval authorizes execution of the reviewed plan only; it does not change
this item's status, satisfy its entry gates, approve delivery, or authorize a
behavioral or conformance change.

Material SHA-256: `9a4bba8d11db0377d23ddd7b0c74f6e5b65168ef5aca68d57e236b1a1e7b8ab7`.

Full-byte SHA-256 hashes of the pre-approval material input snapshot:

| Path | SHA-256 |
| --- | --- |
| `SPEC.md` | `fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e` |
| `specs/0001-core-pipeline-model.md` | `38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e` |
| `specs/0002-operation-catalogs-and-host-configuration.md` | `c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | `83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b` |
| `work/0008/plan.md` | `3cffe3e26f15fd00ffccc1907382b79920205773216625c71a2f7585b57ad121` |
| `work/0008/readiness/portable-core-example-audit-implementation.md` | `eaa9c7392a7dc2819c42588e8c7184674f491a7bbf2307fe1efc8d68d631a7b1` |

## Delivery evidence and review

No audit inventory, edits, validation, or delivery approval recorded.
