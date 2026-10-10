---
spec: SPEC-0008
sources:
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 79fd70dc972b6cbd12b17268316f31641ca89eaf
    content_sha256: 21c6c203c228218a67a076545513b31cc3d5a737e6d3078a935a620a5c50d8fa
  - path: SPEC.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 9f49ea636b86865933bdd4b175ca90287e470625d4be5e8db79751475817ca78
  - path: specs/0005-build-release-and-website-delivery.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 5186656c64c3f4d651d8236bd416d7cf29659669737cc65013136cbf9bc3fdc4
  - path: specs/0006-dotnet-layered-architecture.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: e5a35871ce14aa37d7169ac35d824c910bb0494a01e419dc7895a69dd0092eb9
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: 8fbf725e0fda9697c3eff44435481d7755141272
    content_sha256: 7b3c946a9fd554e9b7129bc391dc68957633716f6a3264cdd659954704413249
  - path: docs/development/coding-conventions.md
    revision: 79fd70dc972b6cbd12b17268316f31641ca89eaf
    content_sha256: 4a220949c98bbedd805f376409a6ff65b05a59fe49be37f4e336b213c1ce6533
  - path: docs/development/spec-driven-workflow.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 2f04cd9e4cc28dbae1cc55593ef7fe29b293911f34175c85faab19c061c8743b
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 07d7b41d910f9dc7a65fea1cb05fb4c62bf6e7cb
    content_sha256: 461eb3aeb9e8a7dd1f1418b3765edfece911a113daeb58e1d13d89ca1aab56af
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

This plan extracts the unresolved decisions and future delivery milestones from
[SPEC-0008](../../specs/0008-multi-language-conformance-and-repository-organization.md).
The specification remains a discussion draft: this plan does not accept its
proposals, allocate requirement identifiers, authorize implementation, relocate
source, rename assemblies, publish profiles, or promise another runtime.

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
| 3 | [I-0008-001](implementation/I-0008-001-engineering-policy-separation.md) | Separate common and specialized engineering policy |
| 4 | [I-0008-002](implementation/I-0008-002-requirement-example-audit.md) | Audit portable requirements, .NET contracts, and examples |
| 5 | [I-0008-003](implementation/I-0008-003-conformance-artifacts.md) | Deliver profile, declaration, and evidence artifacts |
| 6 | [I-0008-004](implementation/I-0008-004-source-relocation.md) | Relocate source without implicit identity or behavior changes |
| 7 | [I-0008-005](implementation/I-0008-005-dependent-surface-updates.md) | Update automation, instructions, documentation, and plans |
| 8 | [I-0008-006](implementation/I-0008-006-future-workspaces.md) | Add future workspaces only for approved consumers |

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

## Reconciliation evidence

- Date: 2026-10-10.
- Baseline: `79fd70dc972b6cbd12b17268316f31641ca89eaf`; the worktree was clean
  before synchronization. Every recorded source hash is the SHA-256 of exact
  working-copy bytes, and every source matched its recorded committed revision.
- Created D-0008-001 through D-0008-013 and I-0008-001 through I-0008-006.
  The 13 specification questions map one-to-one to decision items. Rollout
  steps that repeat those questions were deduplicated into the same decisions;
  only persistent delivery outcomes became implementation milestones.
- No item is complete, approved, cancelled, or executed. No readiness record
  exists. The implementation milestones are non-executable and intentionally
  lack requirement coverage and exact file manifests until decisions produce
  accepted requirements.
- No source relocation, policy extraction, rename, profile publication, or
  normative migration was performed. SPEC-0008 retains its open-question table
  and candidate rollout because migration was not requested; those sections
  remain source evidence while this plan is the operational backlog.
- Readiness impact: all SPEC-0008 scopes remain not assessed. The draft has no
  accepted requirement blocks, so no implementation scope can be approved.
- Validation: inspected all 20 new Markdown artifacts. Checked 19 unique item
  identities and ownership, required metadata and body sections, one phase
  membership per item, resolvable non-retired requirement references, complete
  dependencies, and an acyclic graph. Checked 11 exact source byte hashes and
  full baseline revisions, repository-relative links, ASCII text, whitespace,
  placeholder absence, and absence of inferred completion or approval.
  Specification trace review classified all changed files as planning
  documentation, inferred `maintenance`, found no changed requirement blocks or
  product code requiring reverse-impact review, found no waivers, and passed.
- Reconciliation is complete for the current draft and sources. Human review
  of this exact planning snapshot is still required and is not inferred from
  synchronization.
- Date: 2026-10-10. D-0008-001 accepted a responsibility-based `src/` taxonomy,
  lifecycle-based root exceptions, self-contained workspaces, public
  cross-artifact boundaries, and generated-output rules in R-0008-001 through
  R-0008-003. R-0000-009, R-0000-017, R-0000-019, R-0000-020, and R-0000-031
  were amended consistently. The recorded hashes for `SPEC.md` and SPEC-0008
  now cover the reviewed working-copy bytes while retaining their committed
  baseline revisions.
- Downstream impact: D-0008-010 remains open for concrete generator and
  integration ownership; D-0008-012 remains open for migration sequencing;
  I-0008-004 through I-0008-006 now reference the adopted taxonomy requirements
  but remain non-executable milestones. Existing .NET paths, SPEC-0006,
  path-specific instructions, automation, and work-plan snapshots are migration
  inputs, not silently updated implementation.
- Readiness remains not assessed. This reconciliation resolves no other
  decision, approves no specification snapshot, creates no workspace, and
  authorizes no relocation.
