---
id: D-0008-015
kind: decision
title: Define common-library workspace ownership and dependencies
status: complete
spec: SPEC-0008
requirements:
  - R-0000-019
  - R-0000-020
  - R-0006-024
  - R-0006-041
  - R-0008-001
  - R-0008-002
  - R-0008-003
  - R-0008-019
  - R-0008-027
depends_on: [D-0008-001, D-0008-010, D-0008-012, D-0007-012]
artifacts:
  - SPEC.md
  - specs/0006-dotnet-layered-architecture.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - specs/README.md
  - docs/development/conventions/dotnet.md
  - .github/instructions/dotnet.instructions.md
  - docs/architecture/diagrams/dotnet-layered-components.mmd
  - work/0007/decisions/D-0007-012-generator-runtime-reuse.md
  - work/0007/implementation/I-0007-001-architecture-enforcement.md
  - work/0007/implementation/I-0007-007-portable-validation-foundations.md
  - work/0007/implementation/I-0007-008-descriptor-generation.md
  - work/0007/plan.md
  - work/0008/decisions/D-0008-009-dotnet-adapter-terminology.md
  - work/0008/decisions/D-0008-010-artifact-ownership-boundaries.md
  - work/0008/decisions/D-0008-012-migration-sequencing.md
  - work/0008/implementation/I-0008-004-source-relocation.md
  - work/0008/implementation/I-0008-005-dependent-surface-updates.md
  - work/0008/plan.md
  - work/diagrams/spec-0007-0008.mmd
---

# D-0008-015: Define Common-Library Workspace Ownership and Dependencies

## Objective

Correct the previously selected physical ownership of `Qhapaq.Portable.Validation`
and define a repeatable workspace layout for shared production libraries in
multiple implementation languages.

## Scope and exclusions

This decision amends the repository taxonomy, cross-workspace dependency
boundary, and migration plan. It preserves the portable-validation assembly
identity, algorithms, logical Business ownership, runtime/build-time
consumers, and distribution decided by SPEC-0006 and D-0007-012.

It does not move files, create workspaces, select additional common libraries,
add a public package, or authorize implementation. Exact build orchestration
and skill updates belong to approved migration slices.

## Questions to resolve

- Which repository category owns libraries deliberately shared across
  implementation and tooling workspaces?
- What source and test layout does each language-specific common workspace use?
- How may another workspace depend on a common library without authorizing
  arbitrary private cross-workspace outputs?

## Acceptance criteria

- [x] The authoritative specifications identify a language-specific common
  library workspace with separate source and test directories.
- [x] The shared .NET validation library's new source and test ownership is
  recorded without changing its assembly, algorithm, or distribution contract.
- [x] Explicit common-library dependencies are bounded and do not permit
  arbitrary private workspace-output dependencies.
- [x] The staged migration and affected future implementation milestones
  include the common workspace and its consumers.
- [x] The .NET path instruction applies to the common workspace and both the
  existing and target implementation workspace paths.
- [x] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

SPEC-0008 R-0008-001, R-0008-002, and R-0008-003 define
`src/common/<language>/` as a self-contained workspace for production
libraries deliberately shared across Qhapaq workspaces. Each language
workspace has `src/` and `tests/` directories, plus its own applicable
dependency manifests and pinned toolchain.

SPEC-0006 R-0006-041 locates the `Qhapaq.Portable.Validation` project at
`src/common/dotnet/src/Qhapaq.Portable.Validation/`; its tests belong under
`src/common/dotnet/tests/`. R-0006-024 shows that workspace separately from
the .NET implementation workspace. The assembly name, root namespace,
algorithm ownership, permitted consumers, and distribution remain unchanged.

SPEC.md R-0000-019 and R-0000-020 now include the common .NET source and test
paths and the common-library workspace category. SPEC-0008 R-0008-019 assigns
this common-library ownership while retaining the Roslyn generator in the
.NET implementation workspace. Common-library dependencies require explicit
project references or documented package/release-artifact references; this
does not permit consuming arbitrary private source or build outputs.

SPEC-0008 R-0008-027 places the common-library extraction in the separately
approved source-relocation stage, coordinated with moving the implementation
workspace and its dependent consumers. I-0008-004's concrete migration slice
must atomically update the build-and-test skill and path consumers required by
the new workspace roots; I-0008-005 covers remaining non-atomic consumers.

## Validation and review

Validation performed 2026-10-11:

- Requirement integrity: PASS. SPEC.md retains 46 requirement identifiers,
  SPEC-0006 retains 41, and SPEC-0008 retains 29; identifiers and their order
  are unchanged. Revised fingerprints are recorded below. Earlier fingerprints
  found in D-0007-012, D-0008-009, D-0008-010, D-0008-012, and prior
  reconciliation evidence remain historical snapshots, not current code or
  test markers; the affected ownership records explicitly clarify
  supersession.
- Source reconciliation: PASS. SPEC-0007 and SPEC-0008 plans each record 18
  authoritative inputs. Every source hash matches its current exact bytes and
  every baseline revision resolves. The committed baseline blobs for SPEC.md,
  SPEC-0006, SPEC-0008, and .NET conventions were verified against the
  pre-amendment source hashes before the plans advanced those baseline
  revisions to `7178f84c93d8393c30a5a5cf57f3c923d36274fc`. The new .NET
  instruction source uses the same pre-amendment baseline revision.
- Work-plan structure: PASS. The combined SPEC-0007/SPEC-0008 graph has 75
  unique work items and 216 dependency edges with no missing prerequisites,
  cancelled dependency, or cycle. The renderer generated the 75-item
  cross-plan diagram.
- Documentation: PASS. Local links and anchors in all 16 changed Markdown
  files resolve. `git diff --check` reports no whitespace errors; Git emitted
  only line-ending normalization warnings for the README and generated diagram.
- Specification trace check: PASS with warnings. The change is an `amendment`.
  No product or test code changed and no inline code/test marker was stale.
  Warnings reflect the deliberately implementation-specific .NET project and
  workspace paths in the governing architecture and repository requirements.
  No build or unit tests apply to this specification, documentation,
  instructions, diagrams, and planning-only change; no build/test command was
  introduced.

Changed requirement fingerprints:

| Requirement | HEAD | Current |
| --- | --- | --- |
| R-0000-019 | `063540` | `878ed8` |
| R-0000-020 | `a7a404` | `3ff067` |
| R-0006-024 | `c4e735` | `7bba32` |
| R-0006-041 | `2c2d4a` | `a98508` |
| R-0008-001 | `469f59` | `3f463d` |
| R-0008-002 | `2188f7` | `abe581` |
| R-0008-003 | `7266de` | `6b0312` |
| R-0008-019 | `571f96` | `051e56` |
| R-0008-027 | `4468fb` | `7c081d` |

Proposed commit trailers:

```text
Change-Kind: amendment
Spec: R-0000-019@878ed8, R-0000-020@3ff067, R-0006-024@7bba32, R-0006-041@a98508
Spec: R-0008-001@3f463d, R-0008-002@abe581, R-0008-003@6b0312, R-0008-019@051e56, R-0008-027@7c081d
```

Exact ready-for-review snapshot (approval absent):

| Material | SHA-256 |
| --- | --- |
| This decision's material content | `167ebcaa174e8656ccb5ef6767b9b798bee325e6d27bbf765702bc272084bf03` |
| `SPEC.md` | `fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e` |
| `.github/instructions/dotnet.instructions.md` | `97fa3163316d35c1a7ccac75293f896652f7f7b150cc4fbff83ab4d67ee9d05e` |
| `specs/0006-dotnet-layered-architecture.md` | `785bc5aba6b82f1aa3e73a84d86d91fcf4c7d0a3bb0425f2a389d1d874940732` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `specs/README.md` | `fcf2a02e8f341b91a06f7f1f174c0379868af2adf007688e4d0d592cee8b9d12` |
| `docs/development/conventions/dotnet.md` | `9389c4cf18b6674497f79e0caef7059928369a935aef5a6ced53046ea5295d36` |
| `docs/architecture/diagrams/dotnet-layered-components.mmd` | `9b9693758a46962c1ba48ffb9b8f35402858677eb34a09c11b66cb110d306303` |
| `work/0007/decisions/D-0007-012-generator-runtime-reuse.md` | `7a81a618265d57960737a97a778beb363fdb909c7c62aaea64c50d0db8146a5e` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | `bd5659ff9ad32e9fbdff9910599c4940a0b8eb5c5ca15c40c2824af80de9e4f9` |
| `work/0007/implementation/I-0007-007-portable-validation-foundations.md` | `1421bd28962d6e474c9e4ab90a870afe6e5b32d09fefdabd12bf88cafaa638f8` |
| `work/0007/implementation/I-0007-008-descriptor-generation.md` | `4c8310530963b39f558262d1c5087677e05f2f7b3d8653870828b952d96e5636` |
| `work/0007/plan.md` | `b6e9b6d5a1b7c6aaaf7a8df7b248f28d046b5e2952ac8382edc9d366e7849485` |
| `work/0008/decisions/D-0008-009-dotnet-adapter-terminology.md` | `114a53b4dc4062ec4607f46dc75882de6c3dc57bf5c0f2430b808f46318f2b35` |
| `work/0008/decisions/D-0008-010-artifact-ownership-boundaries.md` | `e9ebd7831f81c6641b5f730d5c69a50b601f388813f9de11054760b0244dddb0` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | `51f8160525272673826baac8418e87154986bf1cc172476617c21d1061dd43d3` |
| `work/0008/implementation/I-0008-004-source-relocation.md` | `55f174936da2f81b2114aa698612452a4af84a5d2d59442fcf677f4e46f54b2c` |
| `work/0008/implementation/I-0008-005-dependent-surface-updates.md` | `5d229cf3d3a572c22804583ae8e76a6e4dba1a35ef81517d2609e31c3c473a87` |
| `work/0008/plan.md` | `994a9b4c5b12410c78754ea0e64851f762c544b6c9b3a927ed01017fd4d463c8` |
| `work/diagrams/spec-0007-0008.mmd` | Generated from the exact work-plan source set; generated snapshot metadata and freshness are verified by the renderer. |

Approval recorded 2026-10-12: the user explicitly approved this exact
snapshot in this session. The approved scope is the common-library workspace
taxonomy, explicit dependency boundary, placement of
`Qhapaq.Portable.Validation` and its tests, and the reconciled specifications,
instructions, documentation, diagrams, and future work items listed above.
Physical relocation, implementation, public package creation, migration
readiness, and component-contract publication are excluded.

The generated dependency diagram is refreshed from the completed plan status;
its snapshot metadata and freshness are verified by the renderer. The approved
decision material SHA-256 is
`167ebcaa174e8656ccb5ef6767b9b798bee325e6d27bbf765702bc272084bf03`, with the
exact input/output hashes recorded in the snapshot table above.
