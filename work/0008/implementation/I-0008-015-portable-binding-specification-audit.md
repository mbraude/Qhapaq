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

Explicitly approved in this session on 2026-10-14 for this exact slice,
manifest, dependencies, entry gates, tests, validation, and exclusions. This
approval authorizes execution of the reviewed plan only; it does not change
this item's status, satisfy its entry gates, approve delivery, or authorize a
behavioral or conformance change.

Material SHA-256: `a633715c795a26662eab7e9d45cc3f423a1f328639f4ecfb55303c17089c4c51`.

Material input snapshot:

| Path | Basis | SHA-256 |
| --- | --- | --- |
| `work/0008/readiness/portable-binding-specification-audit-implementation.md` | material | `fbc321553f64dfb0746fd9d77ba56fa1fc4a5a090446ac80c0fc4c9db5aeb0a2` |
| `work/0008/plan.md` | bytes | `529dc639f6b64614f288aa457e78de8005da7fd6af311eeeaead46e023863a98` |
| `SPEC.md` | bytes | `998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | bytes | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | bytes | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | bytes | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | bytes | `83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b` |

The prior plan approval applied to its earlier reviewed input snapshot and is
superseded by this approval. This approval does not satisfy dependencies or
entry gates, approve delivery, publish a contract, or claim whole-v1
conformance.

## Delivery evidence and review

No audit inventory, edits, validation, or delivery approval recorded.
