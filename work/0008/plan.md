---
spec: SPEC-0008
sources:
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 5c166ff223ad2d5c57824de534d409bcac22b090
    content_sha256: 1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a
  - path: SPEC.md
    revision: 4e24e1b0e293691eb731bbc8429671aaf20cbb43
    content_sha256: c68a0e3c08b3d6c1baa7b5753cf4d3630f94fe5f7936bfede002e2e9f662c908
  - path: specs/0005-build-release-and-website-delivery.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 42bc95d2ef871b191b09242561fed3fa812670f4eb410482d557c0413c193a3f
  - path: specs/0006-dotnet-layered-architecture.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: 8fbf725e0fda9697c3eff44435481d7755141272
    content_sha256: 1e66c0780d5c9cc271007d0d838f32d287782c45f75bb2927d6433e0596ff4a9
  - path: docs/development/coding-conventions.md
    revision: a3028eddae623df0fd7420bb9644363b8344cdb3
    content_sha256: 5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b
  - path: docs/development/spec-driven-workflow.md
    revision: b8271f0f10cab61831ea6bcba81e801224a8fca3
    content_sha256: 574d0e18efb42b5701b148a68a62fbd4be7b748e3f276bb6424a056c152507f4
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: d6cf2c053ee259d51f641da3c27cdbcea4a2c243
    content_sha256: 1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83
  - path: docs/architecture/decisions/0001-use-microsoft-dependency-injection.md
    revision: d3ff6bf9df744c63fc776775956ce41a907a5bcf
    content_sha256: f7855b81e87db15f89326d7a297cc983eb8ba1a4f250aed380a999e5f87de217
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
| 3 | [D-0008-014](decisions/D-0008-014-policy-checker-delivery-boundary.md) | Resolve the policy and trace-checker delivery boundary |
| 4 | [I-0008-012](implementation/I-0008-012-conformance-artifact-planning.md) | Plan conformance artifact delivery before SPEC-0007 artifact production |
| 5 | [I-0008-010](implementation/I-0008-010-dotnet-policy-extraction.md) | Extract .NET policy and route its path instructions |
| 6 | [I-0008-011](implementation/I-0008-011-artifact-policy-routing.md) | Separate artifact-authoring policy from path instructions |
| 7 | [I-0008-001](implementation/I-0008-001-engineering-policy-separation.md) | Complete the aggregate common and specialized policy outcome |
| 8 | [I-0008-002](implementation/I-0008-002-requirement-example-audit.md) | Audit portable requirements, .NET contracts, and examples |
| 9 | [I-0008-007](implementation/I-0008-007-trace-checker.md) | Implement the deterministic multi-language trace checker |
| 10 | [I-0008-003](implementation/I-0008-003-conformance-artifacts.md) | Deliver profile, declaration, and evidence artifacts |
| 11 | [I-0008-009](implementation/I-0008-009-migration-validation-orchestration.md) | Establish root migration validation and recovery orchestration |
| 12 | [I-0008-008](implementation/I-0008-008-entry-point-identity-migration.md) | Apply the matched .NET Entry Point identities |
| 13 | [I-0008-004](implementation/I-0008-004-source-relocation.md) | Relocate source without implicit identity or behavior changes |
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

## SPEC-0007/SPEC-0008 artifact sequencing reconciliation

- Date: 2026-10-11. Baseline: clean worktree at
  `3ef71768659562d7e82951493b0b6b3671405d49`.
- The user selected a sequencing boundary in which relevant SPEC-0008
  conformance decisions and concrete implementation planning precede SPEC-0007
  Phase 1 artifact production, while SPEC-0008 artifact delivery follows its
  SPEC-0007 foundation outputs. This does not require full SPEC-0008 delivery
  before SPEC-0007 can resume.
- Added [I-0008-012](implementation/I-0008-012-conformance-artifact-planning.md)
  to plan exact, reviewable delivery slices for I-0008-003 before production
  starts. It is ordered before SPEC-0008 delivery work and depends on the
  relevant conformance/publication decisions plus SPEC-0007's portable
  envelope and test-artifact decisions.
- I-0008-003 now depends on I-0008-012 as well as D-0007-015, I-0007-002, and
  I-0007-005. Therefore conformance artifact delivery follows both completed
  planning and the actual SPEC-0007 shared-tooling and validation-foundation
  outputs. The later SPEC-0007 CI, distribution, and website/release
  dependencies on I-0008-003 remain unchanged.
- No requirement, source specification, or existing item scope was changed.
  The new planning gate and affected delivery items remain open; no schemas,
  vectors, tooling, reports, profiles, or claims were produced or approved.
  Relevant decisions and planning can be completed before Phase 1 artifacts
  begin, with no dependency cycle.
- No source snapshot was advanced: this reconciliation changes only work-plan
  and work-item records, not their authoritative specification or policy
  inputs. Validation of source hashes, item ownership and references,
  dependency acyclicity, changed-file links, and whitespace passes: all 12
  recorded SPEC-0008 source hashes match current bytes; 77 work-item IDs are
  unique and all dependencies resolve; the combined graph has no cycles; and
  all checked local links resolve. `git diff --check` passes with only the
  repository's existing CRLF-to-LF warnings. I-0008-012 appears once in this
  plan.
- Specification trace review: PASS. All nine changed files are planning
  records classified as `Other`; the inferred change kind is `maintenance`.
  No specification blocks, product code, tests, inline references, or waivers
  changed, so no `Spec:` trailer applies and behavioral reverse-impact review
  is not applicable.

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
- Date: 2026-10-10. D-0008-008 drafted language-neutral traceability placement
  and checking semantics in R-0008-016 through R-0008-018. Exact portable
  marker and waiver payloads remain common; each maintained implementation
  language registers native placements and a language-aware extractor; one
  shared rules engine owns grammar, resolution, fingerprints, placement,
  reverse-impact review, waiver scope, and explicit diagnostics.
- Downstream impact: I-0008-001 now covers the placement-policy and extractor
  registration requirements. D-0008-011 now depends on D-0008-008 and covers
  R-0008-017 where root and CI orchestration invoke the checker. New
  I-0008-007 owns deterministic checker delivery for R-0008-016 through
  R-0008-018 but remains a non-executable milestone blocked by orchestration,
  readiness, an exact manifest, and concrete slice planning. D-0008-012 retains
  its existing dependency on D-0008-008. No item was cancelled, approved, or
  executed.
- Source baseline: SPEC-0008, ADR-0003, and the coding conventions retain their
  recorded committed baselines and now record exact reviewed working-copy byte
  hashes `4dab808ab9bd25ae591120a583e1b4d607fb8f28b66fdf2aa39ad711f7602d46`,
  `1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83`,
  and `604a6173250960aabdf3fd7c16c60c111f9e36ceb946baff1c28033c2654e454`
  respectively. Other source records remain unchanged because their bytes and
  impact are unchanged. Reconciliation is complete for D-0008-008 and its
  affected downstream work.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-008 snapshot, implement or integrate the checker, authorize another
  runtime, migrate policy, or affect earlier completed decisions.
- Date: 2026-10-10. D-0008-009 drafted the .NET **Entry Points** terminology
  and matched `Qhapaq.EntryPoints.<EntryPoint>` directory, project, assembly,
  root-namespace, and derived source-namespace identities across the affected
  SPEC-0006 architecture requirements. Executable filenames and distribution
  package IDs remain separate identities. SPEC-0008 records the resolved
  question, ADR-0001 uses the new hosting identity, and the architecture
  diagram and coding conventions remain consistent with the amended source.
- Downstream impact: new I-0008-008 owns the coordinated identity migration
  without conflating it with repository relocation. D-0008-012 now covers the
  rename's sequencing, compatibility validation, and recovery. I-0008-005
  depends on both the identity migration and source relocation before it closes
  remaining consumer updates. No existing item was cancelled, approved, or
  executed, and no implementation was changed.
- Source baseline: SPEC-0008 and the coding conventions use committed baseline
  `130919358da2c7c9918e0eff6caa82fd7bc9b44b`; SPEC-0006 uses
  `66c43b3d030e84a4ac055b6853946c401d7a9b8c`; and ADR-0001 uses
  `d3ff6bf9df744c63fc776775956ce41a907a5bcf`. Their exact reviewed
  working-copy SHA-256 values are respectively
  `3efd22dbdfea9783141fda61e8625340ea67224663b07ca63c32fb86155dba02`,
  `8cd098f3f9bd877ef9f1c77a77c4b1a895b28ae92ace65299ff05daa4a859b05`,
  `62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653`,
  and `f7855b81e87db15f89326d7a297cc983eb8ba1a4f250aed380a999e5f87de217`.
  Other source records remain unchanged because their bytes and impact are
  unchanged. Reconciliation is complete for D-0008-009 and its affected
  downstream work.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-009 snapshot, rename projects or namespaces, move source, change
  package or executable identities, or authorize implementation.
- Date: 2026-10-10. D-0008-010 drafted responsibility-based artifact ownership
  and dependency directions in R-0008-019. The .NET implementation workspace
  owns the independently versioned Roslyn generator package as build tooling;
  product integrations and maintained contributor tools remain separate
  workspaces even when written in .NET; and private outputs or accidental
  runtime dependencies do not cross those boundaries.
- Downstream impact: D-0008-011 now depends on D-0008-010 and covers
  R-0008-019 when defining workspace orchestration. D-0008-012 and I-0008-004
  through I-0008-006 cover the ownership requirement for migration, dependent
  consumer updates, and future real workspaces. The SPEC-0007 D-0007-012 and
  I-0007-008 items now treat R-0008-019 and D-0008-010 as inputs while
  retaining their separate shared-algorithm, package-boundary, implementation,
  and test decisions.
- Source baseline: SPEC-0008 uses committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` and exact reviewed working-copy
  byte hash
  `433b67c0cb12370756258192e57f5e42298eb7f8879160966cc3d52734f4cbbc`.
  Other authoritative source bytes and records remain unchanged.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-010 snapshot, resolve D-0007-012, create or relocate a workspace,
  select an integration platform, implement or package the generator, or
  authorize implementation. Reconciliation is complete for D-0008-010 and its
  affected downstream work.
- Date: 2026-10-10. D-0008-011 drafted workspace capability and root-adapter
  contracts, root-owned fail-closed transitive impact selection, immutable
  digest-bound conformance-report transport, and exact coordinated release
  assembly in R-0008-020 through R-0008-022 and R-0005-034.
- Downstream impact: D-0008-013 now depends on D-0008-011 and covers the
  publication boundary established by R-0008-022 and R-0005-034. D-0008-012
  covers all four new requirements when sequencing release and migration
  gates. I-0008-003 covers report and evidence production, I-0008-007 covers
  root invocation of the trace checker, and I-0008-005 and I-0008-006 cover
  orchestration consumers and future workspace contracts. No item was created,
  cancelled, approved, or executed.
- Source baseline: SPEC-0008 retains committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` and records exact reviewed
  working-copy SHA-256
  `56ae226939c2378aa1949437f9864fbd3978b35ae33f5a9480e2b3f5ccbb7bb6`.
  SPEC-0005 retains committed baseline
  `66c43b3d030e84a4ac055b6853946c401d7a9b8c` and records exact reviewed
  working-copy SHA-256
  `da4d393724f268b03a21fe2e36beb1d4cd01c9c73ae0c9d370e6f8a6d33aefa2`.
  Other authoritative source bytes and records remain unchanged.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-011 snapshot, define concrete commands or schemas, publish a claim,
  select a toolchain, implement workflows, assemble a release, or authorize
  implementation. Reconciliation is complete for D-0008-011 and its affected
  downstream work.
- Date: 2026-10-10. D-0008-013 drafted exact-snapshot approval and protected
  release promotion for profile versions and conformance claims, immutable
  publication records, closed append-only lifecycle states, correction and
  withdrawal behavior, declaration-lifetime evidence availability, and
  indefinite audit records in R-0008-023 through R-0008-026 and R-0005-035.
- Downstream impact: D-0008-012 now covers the publication requirements when
  sequencing profile artifacts, release changes, validation, and recovery.
  I-0008-003 now covers publication records, status history, evidence
  availability, withdrawal, audit, and protected-release integration. No item
  was created, cancelled, approved, or executed, and no dependency changed.
- Source baseline: SPEC-0008 retains committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` and records exact reviewed
  working-copy SHA-256
  `5097e7f8921b5e865feccbb304f890840a9b929e33fc159d468c8b089212bdc1`.
  SPEC-0005 retains committed baseline
  `66c43b3d030e84a4ac055b6853946c401d7a9b8c` and records exact reviewed
  working-copy SHA-256
  `42bc95d2ef871b191b09242561fed3fa812670f4eb410482d557c0413c193a3f`.
  Other authoritative source bytes and records remain unchanged.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-013 snapshot, define publication schemas or storage, publish a
  profile or claim, implement release automation, assemble a release, or
  authorize implementation. Reconciliation is complete for D-0008-013 and
  its affected downstream work.
- Date: 2026-10-10. D-0008-012 drafted staged migration, validation, impact
  review, user-change preservation, and non-destructive recovery semantics in
  R-0008-027 through R-0008-029. Prerequisite policy, audit, traceability,
  conformance, and root-orchestration delivery precedes an Entry Point identity
  migration at existing paths; separately approved source relocation follows
  only after that identity snapshot passes validation and review.
- Downstream impact: new I-0008-009 owns the previously untracked root
  migration-validation and recovery orchestration prerequisite. I-0008-008 now
  depends on I-0008-001, I-0008-002, I-0008-003, I-0008-007, and I-0008-009;
  I-0008-004 now depends on I-0008-008. I-0008-004, I-0008-005, I-0008-006,
  and I-0008-008 cover the applicable new migration requirements. Existing
  item identities and unrelated dependencies remain unchanged.
- Source baseline: SPEC-0008 retains committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090`; its exact reviewed working-copy
  SHA-256 is recorded in the source header. Other authoritative source bytes
  and records remain unchanged.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-012 snapshot or any implementation plan, execute a rename or move,
  alter public behavior or identity, assemble a release, publish a profile or
  claim, or authorize future workspace creation. Reconciliation is complete
  for D-0008-012 and its affected downstream work.
- Date: 2026-10-10. Reconciled the SPEC.md and common coding-conventions
  snapshots after commit `4e24e1b0e293691eb731bbc8429671aaf20cbb43`. SPEC.md
  now prefers rebase integration to preserve independently validated commits
  and prohibits automatic source-branch rewriting when opening pull requests.
  The common conventions require preserving every included commit's
  traceability, describe rebase preservation, and retain complete `Spec:`
  coverage if squash is explicitly selected. Entry Points terminology in the
  conventions remains consistent with D-0008-009.
- Impact review: these edits change repository integration and commit
  traceability guidance, not SPEC-0008 requirements, profile semantics,
  conformance claims, or migration requirements. I-0008-001 and I-0008-005
  remain valid with unchanged scope, requirements, dependencies, and manifests;
  no new item or dependency is needed. D-0008-009's approved Entry Points
  wording is unchanged; its recorded conventions snapshot is retained as
  historical approval evidence and is not extended to approve the separate
  integration-policy change. No code/test references or SPEC-0008 requirement
  fingerprints are affected. The R-0000-045 amendment is separately tracked
  by the SPEC-0000 plan.
- Source baseline: both changed inputs are committed at
  `4e24e1b0e293691eb731bbc8429671aaf20cbb43`. Their exact current SHA-256
  values are `c68a0e3c08b3d6c1baa7b5753cf4d3630f94fe5f7936bfede002e2e9f662c908`
  for `SPEC.md` and
  `49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834` for
  `docs/development/coding-conventions.md`. The former uncommitted snapshots
  are recoverable: the recorded SPEC.md hash matches the CRLF form of its
  recorded baseline, and the recorded conventions hash matches the CRLF form
  of the previously committed conventions file. The remaining delta is
  reviewed against those exact texts.
- Readiness remains not assessed; no implementation milestone gains execution
  eligibility or plan approval. The separate SPEC-0007 plan also has stale
  snapshots for SPEC-0008 and the coding conventions and needs its own bounded
  synchronization. SPEC-0000's two shared-source hashes match the current
  bytes. Reconciliation is complete for this SPEC-0008 source drift; no
  duplicate R-0000-045 decision work is created here.
- Validation: all 12 recorded source hashes match current bytes; all 22 work
  items have unique identities and exactly one plan membership, with resolved
  requirements and dependencies and no dependency cycle. All 28 relative
  Markdown links resolve, and `git diff --check` passes (with Git's existing
  CRLF-to-LF normalization warning). The specification trace check classified
  this work-plan-only change as `maintenance` and passed; no normative
  requirement block or code/test reference changed. Proposed trailer:
  `Change-Kind: maintenance`; no `Spec:` trailer applies.
- No readiness was reassessed and no approval was inferred. Human review of
  this reconciled plan snapshot remains required.

## SPEC-0007 conformance-envelope reconciliation

- Date: 2026-10-11. The committed SPEC-0007 baseline is
  `8fbf725e0fda9697c3eff44435481d7755141272`; the source header records the
  exact working-copy hash reviewed for the D-0007-015 decision.
- D-0007-015 specifies the portable envelope conventions under R-0007-347
  and awaits approval of its exact ready-for-review snapshot. I-0008-003 now
  references R-0007-347 in addition to its existing SPEC-0005 and SPEC-0008
  requirements, and retains the explicit prerequisites D-0007-015,
  I-0007-002, and I-0007-005.
- The prerequisite decision and artifact/tooling milestones remain open or
  incomplete. I-0008-003 remains a non-executable milestone; no profile,
  vector, evidence schema, claim, or publication is produced by this sync.
- Readiness remains not assessed and approval of this changed plan/item
  snapshot is pending. This reconciliation does not approve implementation
  slices or delivery.
- Date: 2026-10-10. Added D-0008-014 after scoped engineering-policy readiness
  identified an unresolved delivery boundary between policy authoring and the
  matching trace-checker extractor. The item asks whether policy artifacts may
  be delivered before the checker without claiming language support, assigns
  policy/extractor registration ownership, and reconciles I-0008-001 and
  I-0008-007 acceptance and dependency gates. It must preserve R-0008-016
  through R-0008-018 and amend an authoritative source if review finds missing
  semantics.
- D-0008-014 depends on completed D-0008-008 and D-0008-011. I-0008-001 and
  I-0008-007 now depend on D-0008-014 so neither can proceed with an
  unreconciled delivery boundary. No requirement semantics were changed.
- The engineering-policy readiness record remains blocked and is no longer
  current for the modified plan and implementation-item snapshots; it must be
  reassessed after D-0008-014 is resolved. No readiness or implementation-plan
  approval is inferred. The plan source records remain current because none of
  their authoritative inputs changed.
- Validation: all 23 decision and implementation item IDs are unique and have
  exactly one phase membership; every dependency resolves and the cross-plan
  graph remains acyclic. All requirement references resolve, all relative
  links in the edited plan, decision, and readiness record resolve, and
  `git diff --check` passes with the existing CRLF normalization warnings.
  Specification trace review classified the plan, work-item metadata, and
  readiness record as documentation (`maintenance`); no requirement block or
  code/test reference changed. Proposed trailer:
  `Change-Kind: maintenance`; no `Spec:` trailer applies.
- No implementation, readiness, or decision approval was granted. Exact
  review of D-0008-014 is the next gate.
- Date: 2026-10-10. D-0008-014 resolved the policy/checker delivery boundary
  under existing R-0008-016 and R-0008-017. Policy authoring and placement
  definitions belong to I-0008-001 and may be delivered without claiming
  traceability support. I-0008-007 owns extractor registration and evidence
  that registrations match the approved policies; it now depends on I-0008-001.
  The support condition remains unchanged: both policy placements and a
  matching registered extractor are required. The milestones remain separate;
  executable child slices are deferred to implementation planning after scoped
  readiness. No specification or ADR change was needed, and no tool ownership
  or implementation technology was selected.
- Readiness impact: the engineering-policy readiness record remains historical
  and stale; reassess it against the resolved boundary and current milestone
  snapshots before implementation planning. No readiness or implementation
  approval is inferred.
- Reconciliation is bounded to D-0008-014 and I-0008-001/I-0008-007. Phase
  membership and all other work items remain unchanged. D-0008-014 and its
  affected milestones are prepared for exact-snapshot review; no implementation
  or language-support claim is authorized.
- Validation: all 12 plan source hashes match current bytes; all 74 repository
  work-item IDs are unique, dependencies resolve, and the graph is acyclic.
  Relative Markdown links in the four changed files resolve and `git diff
  --check` passes. The specification trace check passes as maintenance; only
  planning/work-item documentation changed, with no requirement block, code,
  or test edits. Exact review inputs and outputs are recorded in D-0008-014.
- Date: 2026-10-10. Phase 2 implementation planning was requested after the
  `engineering-policy` readiness record was approved and pushed. The recorded
  baseline was `089ccbaca8e17bf89b3a53ec893d20389dba02e1` with a clean
  worktree; all 12 recorded plan-source hashes match current bytes. The
  readiness approval covered I-0008-001 at material SHA-256
  `581295daad8283bf22b5b8039053895acf672e561dc7e547f8954abac88a40a8`;
  the approved readiness-record bytes had SHA-256
  `61388cb21205410af8f993e4c0c3f050f469e70632cd0af0d542bd5993ba9190`.
  This plan now retains I-0008-001 as an aggregate gate over two policy
  slices, so that readiness evidence requires impact review and reassessment
  before the revised plan or either slice can be approved for execution.
- I-0008-010 and I-0008-011 detail only the policy work covered by the scoped
  readiness. The remaining Phase 2 milestones stay non-executable; each still
  needs its own current scope readiness, exact slices, and plan approval. No
  production files, policy guides, or implementation code were created, and
  no plan approval or execution authorization is inferred.
- Cross-plan validation also found that I-0008-007's dependency metadata had
  not recorded the I-0008-001 prerequisite already required by D-0008-014 and
  its entry gates. That dependency is restored in I-0008-007; checker scope
  and acceptance criteria are unchanged.
- Phase membership and dependency reconciliation are complete. Readiness
  reassessment for the materially revised I-0008-001 snapshot and explicit
  review/approval of this exact plan remain outstanding gates.
- Date: 2026-10-11. Reconciled the common coding-conventions source after the
  approved I-0008-010 delivery extracted .NET-specific rules into its
  specialization. The prior recorded source hash
  `49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834` matched
  the pre-extraction source at `4e24e1b0e293691eb731bbc8429671aaf20cbb43`;
  the current source is committed at
  `a3028eddae623df0fd7420bb9644363b8344cdb3` with hash
  `5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b`.
- Impact review: the source change moves approved .NET-specific policy out of
  the common guide without changing its remaining common policy or governing
  requirements. I-0008-011's objective, manifest, requirements, dependencies,
  and exit criteria remain applicable; the readiness source inventory and
  assessment nevertheless require refresh against the delivered policy and
  current slice snapshots. No item, dependency, or phase membership changed.
  This source-record update changes the exact plan bytes, so explicit approval
  of the current plan snapshot is required before I-0008-011 resumes.
- Validation: all 12 recorded plan source hashes and committed baseline
  revisions match current bytes; plan-relative links and anchors resolve; and
  `git diff --check` passes. The specification trace check classifies the
  changed work-plan, slice metadata, and policy documentation as `maintenance`
  and passes; no requirement block, product code, or test changed. No item ID,
  phase membership, or dependency edge changed in this reconciliation; the
  prior cross-plan dependency validation remains applicable. Readiness
  reassessment and explicit review of this exact plan snapshot remain pending.
