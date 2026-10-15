---
spec: SPEC-0008
process_version: 1
sources:
  - path: SPEC.md
    revision: c5e1c6b1e3c8c4fb1ae61ecd2f1547986f90d65d
    content_sha256: 998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6
  - path: specs/0001-core-pipeline-model.md
    revision: c5e1c6b1e3c8c4fb1ae61ecd2f1547986f90d65d
    content_sha256: 1ccc40bf3335b1b957b679e5d8439a2abcfebf3a4338583e8aaa024340e7400e
  - path: specs/0002-operation-catalogs-and-host-configuration.md
    revision: c5e1c6b1e3c8c4fb1ae61ecd2f1547986f90d65d
    content_sha256: ca889260cd2445fc3a285c978389d0d31a0541d0d2b2d5830af47cfc6b73c2f4
  - path: specs/0003-product-evolution-roadmap.md
    revision: cb6a46d81b52b3728d67008e9ffbda6da61f4815
    content_sha256: d9b5e8c81c676961f49edd4adf0a191a75bc2d5032320d65e0051955dd8cc62d
  - path: specs/0004-ai-assisted-connections.md
    revision: cb6a46d81b52b3728d67008e9ffbda6da61f4815
    content_sha256: 7c0df89cec4bf526e22137718f80ee562b424a71efbe1856bc6337ccd63ca07b
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 71bf914cd8edf48b6af94544c342c4ad2c906929
    content_sha256: 51566da6fc6521022146426661004112ee133e3600656a68a59c71e4f040c779
  - path: specs/0005-build-release-and-website-delivery.md
    revision: cb6a46d81b52b3728d67008e9ffbda6da61f4815
    content_sha256: 8bdd26b4572fa99041587451e580818e9a540d4d64d5a2484d856b867f8345e9
  - path: specs/0006-dotnet-layered-architecture.md
    revision: ff91861578d0d4368836d05d1039bbd93fca4efa
    content_sha256: 7e8b252a96cbfef18eaa92d7d742234a626dfbf2758dbbdd63feac055925f58a
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: 1267f9c0475eda05ef1f118437ef64a4a2f2a859
    content_sha256: 5cff3784f6bfc9ddb64b6bcf3f15a14d09c50d97bb25e7702ff65e01496f0d24
  - path: docs/development/coding-conventions.md
    revision: 8a534afd2e4a4cbd28e30de6e115967977862727
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/specifications.md
    revision: 911ede5a759d7288dc569002ab2bbb136caeb52d
    content_sha256: cedd8481133460d1a2f8ad1ed5d7c02d1981d83c837cda88b13c18d1b7fd19f8
  - path: docs/development/conventions/dotnet.md
    revision: 7178f84c93d8393c30a5a5cf57f3c923d36274fc
    content_sha256: d590f92c5e151ae4eb02540d48a7e029863346715204c18ebe3afdc7394d7336
  - path: .github/instructions/dotnet.instructions.md
    revision: 7178f84c93d8393c30a5a5cf57f3c923d36274fc
    content_sha256: 97fa3163316d35c1a7ccac75293f896652f7f7b150cc4fbff83ab4d67ee9d05e
  - path: docs/development/conventions/schemas.md
    revision: 911ede5a759d7288dc569002ab2bbb136caeb52d
    content_sha256: efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 8a534afd2e4a4cbd28e30de6e115967977862727
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0001-use-microsoft-dependency-injection.md
    revision: 8a534afd2e4a4cbd28e30de6e115967977862727
    content_sha256: 663bc361c4799b69e700c6161311d60e010b89c0f65a6065be5acf9d20358173
  - path: conformance/README.md
    revision: 8a534afd2e4a4cbd28e30de6e115967977862727
    content_sha256: 0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307
  - path: schemas/README.md
    revision: 8a534afd2e4a4cbd28e30de6e115967977862727
    content_sha256: 9735bf13164fda904d9d926a1ef896038360c7334e8ad831cac195dfc59ab0a1
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 07d7b41d910f9dc7a65fea1cb05fb4c62bf6e7cb
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825
  - path: AGENTS.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
---

# SPEC-0008: Work Plan

## Scope and authority

This plan extracts unresolved decisions and future delivery milestones from
[SPEC-0008](../../specs/0008-multi-language-conformance-and-repository-organization.md).
The specification remains a partially resolved draft: this plan does not
accept remaining proposals, allocate requirement identifiers outside reviewed
decisions, authorize implementation, relocate source, rename assemblies,
publish profiles, or promise another runtime.

[SPEC.md](../../SPEC.md), [SPEC-0005](../../specs/0005-build-release-and-website-delivery.md),
[SPEC-0006](../../specs/0006-dotnet-layered-architecture.md), and
[SPEC-0007](../../specs/0007-portable-pipeline-definitions-and-binding.md)
remain authoritative for existing portability, repository, architecture,
conformance, and release obligations. Decision items must amend those sources
when an accepted outcome would change them.

## Phase 0: Establish taxonomy and policy boundaries

### Entry gates

R-0000-007 and R-0000-009 preserve language-neutral semantics, shared vectors,
declared conformance, and the target `src/implementations/<language>/` location.
Existing software remains unmoved until separately approved migration work.
R-0006-001 through R-0006-034 continue to govern the .NET architecture and
names until explicitly amended.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0008-001](decisions/D-0008-001-artifact-taxonomy.md) | Adopt an artifact taxonomy and source layout |
| 2 | [D-0008-002](decisions/D-0008-002-convention-ownership.md) | Assign common, language, and artifact conventions |
| 3 | [D-0008-003](decisions/D-0008-003-normative-content-labeling.md) | Separate portable requirements, language contracts, and examples |
| 4 | [D-0008-009](decisions/D-0008-009-dotnet-adapter-terminology.md) | Resolve .NET layer and assembly terminology |
| 5 | [D-0008-010](decisions/D-0008-010-artifact-ownership-boundaries.md) | Assign generator and integration ownership boundaries |
| 6 | [D-0008-015](decisions/D-0008-015-common-library-workspaces.md) | Define common-library workspace ownership and dependencies |

### Exit gates

Accepted outcomes are recorded in authoritative requirement blocks and, where
architectural, ADRs. The R-0000-009 amendment must complete review, and affected
SPEC-0006 requirements must be amended, before a conflicting source move or
rename can be planned. No directory or placeholder is created merely to
demonstrate the taxonomy.

## Phase 1: Define conformance and traceability claims

### Entry gates

Portable claims remain subordinate to R-0000-007, R-0000-009, ADR-0003, and
applicable SPEC-0007 conformance obligations. A profile cannot make a mandatory
requirement optional or replace exact requirement identities and fingerprints.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0008-004](decisions/D-0008-004-initial-conformance-profiles.md) | Define initial profile boundaries and dependencies |
| 2 | [D-0008-005](decisions/D-0008-005-profile-version-compatibility.md) | Define profile version and compatibility rules |
| 3 | [D-0008-006](decisions/D-0008-006-conformance-declarations.md) | Define capability and conformance declarations |
| 4 | [D-0008-007](decisions/D-0008-007-conformance-evidence.md) | Define sufficient conformance evidence |
| 5 | [D-0008-008](decisions/D-0008-008-language-native-traceability.md) | Define language-native traceability placement and checking |
| 6 | [D-0008-013](decisions/D-0008-013-claim-publication.md) | Define profile and claim review and publication |

### Exit gates

Profiles, declarations, evidence, compatibility, traceability, failure
reporting, and publication rules are cohesive and testable. Missing, skipped,
unsupported, and failed obligations remain distinguishable from conformance.
No passing vector suite or self-declaration alone implies complete conformance.

## Phase 2: Plan coordinated delivery

### Entry gates

The relevant Phase 0 and Phase 1 decisions are accepted in authoritative
sources. SPEC-0005 release and recovery obligations and affected SPEC-0006 and
SPEC-0007 gates remain in force.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0008-011](decisions/D-0008-011-build-ci-release-orchestration.md) | Define workspace commands and cross-artifact orchestration |
| 2 | [D-0008-012](decisions/D-0008-012-migration-sequencing.md) | Define migration order, validation, and recovery |
| 3 | [D-0008-014](decisions/D-0008-014-policy-checker-delivery-boundary.md) | Resolve the policy and trace-checker delivery boundary |
| 4 | [I-0008-012](implementation/I-0008-012-conformance-artifact-planning.md) | Plan conformance artifact delivery before SPEC-0007 artifact production |
| 5 | [I-0008-010](implementation/I-0008-010-dotnet-policy-extraction.md) | Extract .NET policy and route its path instructions |
| 6 | [I-0008-011](implementation/I-0008-011-artifact-policy-routing.md) | Separate artifact-authoring policy from path instructions |
| 7 | [I-0008-001](implementation/I-0008-001-engineering-policy-separation.md) | Complete the aggregate common and specialized policy outcome |
| 8 | [I-0008-002](implementation/I-0008-002-requirement-example-audit.md) | Aggregate portable requirement, language-contract, and example audit |
| 8.1 | [I-0008-013](implementation/I-0008-013-portable-core-example-audit.md) | Audit SPEC.md and core portable examples |
| 8.2 | [I-0008-014](implementation/I-0008-014-remaining-portable-specification-audit.md) | Audit roadmap, AI, and release specification examples |
| 8.3 | [I-0008-015](implementation/I-0008-015-portable-binding-specification-audit.md) | Audit SPEC-0007 portable binding examples and defaults |
| 8.4 | [I-0008-016](implementation/I-0008-016-language-contract-and-traceability-audit.md) | Audit SPEC-0006/SPEC-0008 and traceability guidance boundaries |
| 9 | [I-0008-007](implementation/I-0008-007-trace-checker.md) | Implement the deterministic multi-language trace checker |
| 10 | [I-0008-003](implementation/I-0008-003-conformance-artifacts.md) | Aggregate profile, declaration, evidence, and publication delivery |
| 10.1 | [I-0008-017](implementation/I-0008-017-conformance-contract-schemas.md) | Deliver portable conformance contract schemas |
| 10.2 | [I-0008-018](implementation/I-0008-018-profile-definitions.md) | Deliver the four candidate profile definitions and evidence matrices |
| 10.3 | [I-0008-019](implementation/I-0008-019-conformance-contract-vectors.md) | Deliver portable conformance contract and lifecycle vectors |
| 10.4 | [I-0008-020](implementation/I-0008-020-dotnet-conformance-evidence.md) | Connect .NET profile adapters and immutable evidence |
| 11 | [I-0008-009](implementation/I-0008-009-migration-validation-orchestration.md) | Establish root migration validation and recovery orchestration after report producers exist |
| 11.1 | [I-0008-021](implementation/I-0008-021-conformance-publication-integration.md) | Enforce protected conformance publication through root release manifests |
| 12 | [I-0008-008](implementation/I-0008-008-entry-point-identity-migration.md) | Apply the matched .NET Entry Point identities |
| 13 | [I-0008-004](implementation/I-0008-004-source-relocation.md) | Relocate implementation and common-library source without implicit identity or behavior changes |
| 14 | [I-0008-005](implementation/I-0008-005-dependent-surface-updates.md) | Update automation, instructions, documentation, and plans |
| 15 | [I-0008-006](implementation/I-0008-006-future-workspaces.md) | Add future workspaces only for approved consumers |

### Exit gates

Each implementation milestone is split or promoted into approved slices with
governing requirements, exact manifests, tests, and recovery gates before
execution. Relocation preserves public identity and behavior unless a separate
approved amendment says otherwise. Future workspace creation requires a real
consumer and approved scope.

## External prerequisites

- The [SPEC-0007 plan](../0007/plan.md) owns existing portable schema, vector,
  conformance-tooling, CI, distribution, and website milestones. This plan does
  not copy those items. Future detailed slices must link actual completed or
  approved SPEC-0007 prerequisites where they consume those artifacts.
- SPEC-0005 and SPEC-0006 have no owning plans. Their normative requirements
  remain direct gates until companion plans are created.
- Any accepted change to ADR-0003 traceability or ADR-0004 change
  classification requires an explicit superseding ADR or amendment; this plan
  does not make that architectural decision.

## Reconciliation index

Historical source-impact and workflow evidence is stored in the [reconciliation index](reconciliations/index.md).
The linked records are non-material and do not own current plan state.
