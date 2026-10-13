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

Explicitly approved in this session on 2026-10-12 for this exact slice,
manifest, dependencies, entry gates, tests, validation, and exclusions. This
approval authorizes execution of the reviewed plan only; it does not change
this item's status, satisfy its entry gates, approve delivery, or authorize a
behavioral or conformance change.

Material SHA-256: `a633715c795a26662eab7e9d45cc3f423a1f328639f4ecfb55303c17089c4c51`.

Full-byte SHA-256 hashes of the pre-approval material input snapshot:

| Path | SHA-256 |
| --- | --- |
| `.github/instructions/specifications.instructions.md` | `7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2` |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `SPEC.md` | `fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e` |
| `conformance/README.md` | `0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307` |
| `docs/architecture/decisions/0003-enforce-specification-traceability.md` | `da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411` |
| `docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md` | `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| `docs/development/coding-conventions.md` | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/conventions/schemas.md` | `efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2` |
| `docs/development/conventions/specifications.md` | `9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a` |
| `docs/development/spec-driven-workflow.md` | `da0d7ea110236bddcebc9607b435721ecf53d00dff7694a2f43a402f819b3ea2` |
| `schemas/README.md` | `9735bf13164fda904d9d926a1ef896038360c7334e8ad831cac195dfc59ab0a1` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | `83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b` |
| `work/0008/implementation/I-0008-015-portable-binding-specification-audit.md` | `607d7caef3b548d6f05273a79f810e2b33135245c9bb8580c81306c85a0faaac` |
| `work/0008/plan.md` | `b602977cd2f1d5ccc617f5d54ef049c0f5c615f0f6dab7d333481ab44a0d6f20` |
| `work/0008/readiness/requirement-example-audit.md` | `5186fbba33d1810efc047a7f14715a998980630b32112c23c116898239f8c9cf` |
| `work/templates/readiness.md` | `707d334f40feb8e3462f8ee814c55ce3a8f66c32a860a4b8557d5eaa2f672bf2` |
| `work/0008/readiness/portable-binding-specification-audit-implementation.md` | `809a6c43966d0a42276c2012515bc870e1b71b253b54a2408b6569e75bd3d791` |

## Delivery evidence and review

No audit inventory, edits, validation, or delivery approval recorded.
