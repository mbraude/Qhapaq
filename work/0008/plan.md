---
spec: SPEC-0008
sources:
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 2a5f9e29ff61626bd6185e99df66722643781764
    content_sha256: 7a1f61e8de54ba3dc9e789075c93445d4bd72703c0dd3b8bb41889120d32addb
  - path: SPEC.md
    revision: 733f879fb7872fd692c0661af8e6eb62708a7e38
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
    revision: 9df3f2d89fd255132a3c6122bd41890212409060
    content_sha256: 782e590a86419f9001469bc9faa0c2491e93a11728c0da1df0eaf4bbf70f7305
  - path: docs/development/spec-driven-workflow.md
    revision: b8271f0f10cab61831ea6bcba81e801224a8fca3
    content_sha256: 574d0e18efb42b5701b148a68a62fbd4be7b748e3f276bb6424a056c152507f4
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: d6cf2c053ee259d51f641da3c27cdbcea4a2c243
    content_sha256: d384fa75572c08d86a46911a54c4792905511c01c3cb047d01774a0132cf6704
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
- Date: 2026-10-10. Reconciled the workflow guide from
  `34fbe88fb9d4857adc6db5390cc623c210c71540` to
  `b8271f0f10cab61831ea6bcba81e801224a8fca3`. The source change separates
  branch and Git delivery from work-item lifecycle and adds the branch-start
  entry point; it does not change product requirements, phase membership,
  item scope, dependencies, acceptance criteria, readiness, or approval
  evidence. The current named branch already satisfies the added coordination
  guidance. No item was created, changed, cancelled, approved, or executed.
  Reconciliation is complete for this source change, and readiness remains not
  assessed.
- Date: 2026-10-10. D-0008-002 accepted common and specialized engineering
  policy ownership in R-0008-004. The common baseline remains
  `docs/development/coding-conventions.md`; real specializations belong beneath
  `docs/development/conventions/`; applicability is cumulative; and
  path-specific instructions route to policy rather than becoming a competing
  authority. I-0008-001 now covers R-0008-004 and records this target structure
  while remaining a non-executable milestone blocked by D-0008-003,
  D-0008-008, readiness, and concrete slice planning. No item was added,
  cancelled, approved, or executed, and no dependency changed.
- Readiness remains not assessed. The policy-ownership scope has a resolved
  requirement draft but lacks review and approval; unrelated SPEC-0008 scopes
  and the approved D-0008-001 snapshot are unaffected. Reconciliation is
  complete for D-0008-002 and its downstream milestone.
- Date: 2026-10-10. D-0008-003 resolved the normative-content categories in
  R-0008-005. Portable requirements remain implementation-neutral; normative
  language contracts belong in explicitly scoped numbered implementation
  specifications; and requirement-block boundaries plus required labels
  distinguish normative examples from non-normative illustrative examples.
  ADR-0003 records the corresponding labeling clarification without changing
  identifier or fingerprint algorithms.
- Downstream impact: I-0008-002 now covers R-0008-005 and inventories the
  specification and traceability surfaces for a future bounded audit.
  D-0008-008 now treats the accepted content-ownership model as an input while
  retaining its separate marker-placement and checker decision. D-0008-004
  remains open and blocked on review and completion of D-0008-003; no
  conformance profile semantics were resolved.
- Source baseline: the edited SPEC-0008 and ADR-0003 inputs use committed
  baseline `f84c895d0bdcdf7d7c8c515e341a159d75433609` and record the exact
  reviewed working-copy byte hashes. Other source records remain unchanged
  because their bytes and impact are unchanged.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-003 snapshot, authorize the content audit, alter implementation code,
  or publish any contract. D-0008-001 and D-0008-002 approvals remain
  unaffected.
- Date: 2026-10-10. D-0008-004 drafted the initial profile boundaries in
  R-0008-006 and the corresponding claim restrictions in R-0008-007. The
  initial set is `qhapaq.runtime`, `qhapaq.cli.local`, `qhapaq.mcp.host`, and
  `qhapaq.dotnet.in-process`; each surface profile requires the portable runtime
  baseline. CLI and MCP are independent siblings, and remote-client profiles
  remain deferred.
- Downstream impact: D-0008-005 through D-0008-007 and D-0008-013 now reference
  the applicable profile or claim requirements while retaining their existing
  scopes and dependencies. I-0008-003 now covers R-0008-006 and R-0008-007 but
  remains a non-executable milestone blocked by the four downstream decisions,
  publication policy, readiness, and concrete slice planning. No item was
  created, cancelled, approved, or executed, and no dependency changed.
- Source baseline: SPEC-0008 uses committed baseline
  `d6cf2c053ee259d51f641da3c27cdbcea4a2c243` and exact reviewed working-copy
  byte hash
  `d1649a3335e0034049538af508b6c7712cfa4ae3d1271a3a5fa73edcf55f0915`.
  The unchanged SPEC.md, coding-conventions, and ADR-0003 byte snapshots now
  record their newer exact committed baselines; other source records remain
  unchanged because their bytes and provenance are unchanged.
- Readiness remains not assessed. This reconciliation does not approve
  D-0008-004, define profile versions or declaration and evidence formats,
  publish a profile or conformance claim, authorize remote clients, or alter
  implementation code. Earlier completed decisions remain unaffected.
- Date: 2026-10-10. D-0008-005 drafted immutable `MAJOR.MINOR` profile
  identities in R-0008-008. Publishable versions begin at `1.0` and bind exact
  prerequisite versions, authoritative specification revisions, and mandatory
  requirement ID and fingerprint pairs. Minor versions permit only
  semantics-preserving corrections and non-mandatory additions; mandatory,
  applicability, or prerequisite changes require a new major version. Claims
  never migrate automatically, and version numbers imply no support period.
- Downstream impact: D-0008-006, D-0008-007, D-0008-013, and I-0008-003 now
  cover R-0008-008 while retaining their existing scopes and dependencies.
  Declaration formats, evidence sufficiency, publication and support
  procedures, concrete profile publication, readiness, and implementation
  remain unresolved. No item was created, cancelled, approved, or executed,
  and no dependency changed.
- Source baseline: SPEC-0008 uses committed baseline
  `b940a05718427619bdbb24e8baec4e4e9b5c250c` and exact reviewed working-copy
  byte hash
  `41646c6cc180d77734607990bf9aa9c836bfe7ec6e6916e19573529f326dc88d`.
  Other source records remain unchanged because their bytes and impact are
  unchanged. Reconciliation is complete for D-0008-005 and its affected
  downstream work.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-005 snapshot, publish a profile or conformance claim, define a
  declaration schema or evidence threshold, set a support duration, authorize
  implementation, or affect earlier completed decisions.
- Date: 2026-10-10. D-0008-006 drafted the declaration envelope and assessment
  semantics in R-0008-009 and R-0008-010. One versioned closed envelope
  distinguishes exact full claims, exhaustive progress, and unsupported
  targets; binds one exact profile and implementation artifact set; reports
  optional capabilities without partial claims; and references an immutable
  assessment manifest for requirement-level dispositions and evidence mappings.
- Downstream impact: D-0008-007 now covers the assessment-manifest evidence
  boundary; D-0008-013 now covers publication of declarations governed by
  R-0008-009 and R-0008-010; and I-0008-003 covers both new requirements.
  Their existing scope and dependencies remain correct. No item was created,
  cancelled, approved, or executed, and no dependency changed.
- Source baseline: SPEC-0008 uses committed baseline
  `b874b547f9282fe4ee8366f946428894cd08b91e` and exact reviewed working-copy
  byte hash
  `f275062e9abf2c1ce67a23055549a26e98e33f1c1a7852851345fbdd1227ce5d`.
  Other source records remain unchanged because their bytes and impact are
  unchanged. Reconciliation is complete for D-0008-006 and its affected
  downstream work.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-006 snapshot, define evidence sufficiency or publication procedures,
  publish a schema, profile, declaration, or claim, authorize implementation,
  or affect earlier completed decisions.
- Date: 2026-10-10. D-0008-007 drafted profile-version evidence matrices and
  closed evidence recipes in R-0008-011 through R-0008-015. Portable evidence
  kinds, profile-fixed conjunctions and alternatives, exact executable bounds,
  independently rerunnable build and test identity, auditable self-review,
  explicit unsuccessful outcomes, synthetic data, sensitive-data exclusions,
  and declaration-lifetime evidence availability now define sufficiency.
- Downstream impact: D-0008-013 now covers the remaining publication,
  discoverability, withdrawal, and audit procedures within the evidence
  availability rule. I-0008-003 now covers the five evidence requirements but
  remains a non-executable milestone blocked by publication policy, readiness,
  concrete profile matrices and schemas, and slice planning. No item was
  created, cancelled, approved, or executed, and no dependency changed.
- Source baseline: SPEC-0008 uses committed baseline
  `2a5f9e29ff61626bd6185e99df66722643781764` and exact reviewed working-copy
  byte hash
  `7a1f61e8de54ba3dc9e789075c93445d4bd72703c0dd3b8bb41889120d32addb`.
  Other source records remain unchanged because their bytes and impact are
  unchanged. Reconciliation is complete for D-0008-007 and its affected
  downstream work.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-007 snapshot, publish a profile, declaration, evidence bundle, or
  claim, impose independent review, authorize implementation, or affect
  earlier completed decisions.
