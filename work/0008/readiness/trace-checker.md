---
spec: SPEC-0008
scope: trace-checker
assessment: ready-for-review
authorizes: planning
process_version: 1
sources:
  - path: .agents/skills/spec-trace-check/SKILL.md
    revision: 3235ba5b6bfc1ccdd05c97407a84bd7d7dfd9d97
    content_sha256: 4aa125b6bd3bd6738668a3aa99ef4fd18b3ceb385d634d2e6dc0ea5bf2adc7bd
  - path: AGENTS.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: c5e1c6b1e3c8c4fb1ae61ecd2f1547986f90d65d
    content_sha256: 998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/documentation.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: ee1ab8d0f2237adb5a1fd986ce5c925eb1b0d6bafa51bd5c700bfd3436e7f657
  - path: docs/development/conventions/dotnet.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: d590f92c5e151ae4eb02540d48a7e029863346715204c18ebe3afdc7394d7336
  - path: docs/development/conventions/schemas.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2
  - path: docs/development/conventions/specifications.md
    revision: bf53966bc7a98a62c2c1e0692434de6ee16c1d7d
    content_sha256: cedd8481133460d1a2f8ad1ed5d7c02d1981d83c837cda88b13c18d1b7fd19f8
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
  - path: specs/0005-build-release-and-website-delivery.md
    revision: cb6a46d81b52b3728d67008e9ffbda6da61f4815
    content_sha256: 8bdd26b4572fa99041587451e580818e9a540d4d64d5a2484d856b867f8345e9
  - path: specs/0006-dotnet-layered-architecture.md
    revision: bf53966bc7a98a62c2c1e0692434de6ee16c1d7d
    content_sha256: 7e8b252a96cbfef18eaa92d7d742234a626dfbf2758dbbdd63feac055925f58a
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: eb88479ffe90c6f3def182aa78307ca3f1a60f3d
    content_sha256: 5cff3784f6bfc9ddb64b6bcf3f15a14d09c50d97bb25e7702ff65e01496f0d24
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: bf53966bc7a98a62c2c1e0692434de6ee16c1d7d
    content_sha256: 51566da6fc6521022146426661004112ee133e3600656a68a59c71e4f040c779
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
  - path: work/0008/decisions/D-0008-011-build-ci-release-orchestration.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: 85eb2f440d89f38a77abe64ad4c76cdc926f34d6586e0b445920c57ea3643dc4
  - path: work/0008/decisions/D-0008-014-policy-checker-delivery-boundary.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: 434ba2c039eada0798d92776b1e7bc51e50c6995d0fed7292974e9e651e23b44
  - path: work/0008/implementation/I-0008-001-engineering-policy-separation.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: e6e45f8fd659e0f10dfd137df74015269631c899d4d59733b8934e42d513ac48
  - path: work/0008/implementation/I-0008-007-trace-checker.md
    revision: c4cb62ffda867c83a53e7c621892a3db23f36f61
    content_sha256: adf32cc1512357ad44a4128b1f0191fcc3617f53d52aef2c5796847095697951
    material_sha256: 06fd6ab6f6397612a2878f4747d53a8502f01eebe7ac97d40b6efdc647c248d9
  - path: work/0008/implementation/I-0008-009-migration-validation-orchestration.md
    revision: 9396b5567d753f80057164527185d6faa37f0c8e
    content_sha256: a1675cc1b398765f1d2809a76eee2dcec6232c84a925db213af5b933008402fe
    material_sha256: d5ce8f8a6bee4b09f13f8ff336009488acb4d9a4c00cd407fd73ebb8e7b365b1
  - path: work/0008/plan.md
    revision: bc64ea0128052fce377772dce87ca0d961a56c2b
    content_sha256: 049e35381b904042f6fc4934bd72fb723d1ef5c2ae768d4f80781a7bbdce426d
    material_sha256: df9435cef8e584ec0ab2d05d7befde76dca0f6531d3c1feececd841e829d7852
  - path: work/0008/decisions/D-0008-016-trace-checker-architecture.md
    revision: 30e660e621ebdbfc5ef8fd7c5854df65250eaa16
    content_sha256: 8122045b01f196866ebb01c7102d9f7ae499ae796349ab41a00e23b1b7b0dba0
    material_sha256: 588d2f53c633f32f16d6b8d6f5bdb18f51cc6817b771da51901d17f8bdda7846
  - path: docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md
    revision: 30e660e621ebdbfc5ef8fd7c5854df65250eaa16
    content_sha256: 759dc91c963cfdba47901afdcd0113d5f42e259c0533c63d9d24eb649da184a0
  - path: specs/0009-repository-validation-derived-state.md
    revision: 62cf5878eba2fb5e9674ea41c2aaacd0135949ce
    content_sha256: 59a20f67e18d9ed1653a301919d7ad2eeb047e80e35630789377dba2ec2f6d1b
---

# SPEC-0008: Trace Checker Readiness

## Assessed scope

Assess readiness to create concrete delivery slices for
[I-0008-007](../implementation/I-0008-007-trace-checker.md), covering
R-0008-016 through R-0008-018: portable traceability and waiver payloads,
registered language-native extractors, their shared rules engine, diagnostics,
reverse-impact checks, and support registration. R-0008-021 is included only
for the boundary that makes the checker a required, non-bypassable validation
group. Root orchestration and CI integration are owned separately by
[I-0008-009](../implementation/I-0008-009-migration-validation-orchestration.md).

## Exclusions

This assessment grants planning authority only. It does not grant
implementation authority, approve concrete slices or the I-0008-007 manifest,
implement or register an extractor, claim support for any language, publish a
contract, or assert whole-v1 conformance. Exact package versions, entry-point
syntax, fixture inventory, and root manifest contents remain
I-0008-007 and I-0008-009 planning details. R-0008-021's root impact graph and
report aggregation remain outside I-0008-007.

## Completeness and consistency

R-0008-016 through R-0008-018 define the portable marker and waiver syntax,
language-policy registration boundary, extractor output, shared validation
responsibilities, diagnostic fields, hard failures, and prohibited waiver
scope. D-0008-008 resolves native placement and shared-engine ownership.
D-0008-014 assigns policy authoring to I-0008-001 and extractor registration
and policy-match evidence to I-0008-007, without claiming traceability support
before both exist. I-0008-001 is complete and its approved policy outputs
remain the prerequisites for the first registered extractor.

D-0008-014 left checker tool ownership and implementation technology open. That
question is now resolved by
[D-0008-016](../decisions/D-0008-016-trace-checker-architecture.md), which
selects [ADR-0006](../../../docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md):
a Roslyn-based C# extractor under `src/tools/trace-checker/dotnet/`, a shared
Python rules engine under `src/tools/trace-checker/python/`, and a generic
helper `.agents/scripts/trace_check.py` exposing a JSON CLI contract. Each
workspace owns its toolchain and `bin/` output. The decision names the
dependency direction and package boundaries that I-0008-007 planning must
follow, so the earlier tool-ownership and language blockers no longer apply.

The requirements otherwise provide testable behavior for parsing permitted
constructs, recognizing malformed or unsupported markers, resolving
requirements and fingerprints, enforcing invariant and test placement,
checking changed-requirement impact, scoping waivers, and reporting stable
diagnostics. No unresolved product-semantics question was found within those
boundaries. The existing interim AI-led trace-check skill is not a
deterministic checker or a registered language extractor.

## Conformance and prerequisite artifacts

- D-0008-008, D-0008-011, D-0008-014, and I-0008-001 are complete.
- The .NET native placements and artifact-authoring policies are present.
  ADR-0006 approves Python and C# (Roslyn) only as the checker's own
  implementation languages. It does not register traceability support for any
  product language; support must not be implied for unregistered languages.
- No schema or published vector is a prerequisite specified by R-0008-016
  through R-0008-018. I-0008-007 requires focused tests for valid and malformed
  payloads, spans, attachment classes, unresolved and retired requirements,
  stale fingerprints, reverse impact, waiver scope, extractor failures, and
  stable diagnostics after a tool and language boundary is approved.
- I-0008-009 depends on I-0008-007 and owns root adapters, impact selection,
  and validation orchestration. It explicitly requires the checker to exist
  before that later integration; this does not make CI integration part of
  I-0008-007.
- Repository inspection found no deterministic checker implementation or
  registered extractor. This is expected delivery work, not an existing
  conformance artifact that readiness can substitute for.

## Blockers

No blocking findings. The prior blocker, checker architecture and tool
ownership, is resolved by D-0008-016 and ADR-0006.

Non-blocking findings for human review:

- ADR-0006 still carries `Status: Proposed` although D-0008-016 records it as
  the approved architecture output. Changing the status to Accepted changes
  the ADR content hash and requires refreshing this record's sources.
- ADR-0006 places the CI-invoked `.agents/scripts/trace_check.py` entry point
  under `.agents/scripts/`. R-0008-019 describes root `scripts/` and `build/`
  as automation entry points. `.agents/scripts/` already hosts repository
  workflow helpers, so this is probably acceptable, but the placement is an
  open consistency question for I-0008-007 and I-0008-009 planning.
- Planning-only readiness does not authorize implementation. Plan approval
  and implementation readiness remain separate gates. I-0008-007's entry gate
  requires readiness to be approved before concrete slices are created or
  approved, so a human must approve this assessment before slice planning. Plan
  approval for any slice then needs a readiness scope that authorizes
  implementation.

No amendment to R-0008-016 through R-0008-018 or R-0008-021 is indicated by
this assessment. The sole source changes since `d812bf2` affect non-requirement
wording in SPEC-0008 and SPEC.md, and SPEC-0009 states that it does not change
the checker or marker syntax. The requirement fingerprints are unchanged.

## Validation and approval

Validated at HEAD `c4cb62ffda867c83a53e7c621892a3db23f36f61`. Refreshed the
source snapshots with `work_hashes.py refresh --stale` and confirmed every
source reports `current` with `work_hashes.py verify`, including the three
added sources (D-0008-016, ADR-0006, SPEC-0009). Re-ran
`spec_fingerprints.py` for R-0008-016, R-0008-017, R-0008-018, and
R-0008-021; each fingerprint is unchanged from the snapshot
(`cfe5f4`, `4e753a`, `2cb676`, `d6279f`). Verified that the record's relative
links resolve, and that `git diff --check` reports no whitespace errors.

`trace_facts.py` reported no mechanical errors and classified the
documentation-only change as `maintenance`, with no `Spec:` trailer. Because
the change touches no specification or product code, steps 2 to 4 and the
semantic review were not applicable. No build or unit tests were run because
this is a documentation-only readiness record and no repository build/test
command is documented.

This assessment is `ready-for-review` with `authorizes: planning`. It
requires explicit human approval before any slice planning begins. It does not
authorize implementation, approve the I-0008-007 manifest, establish language
traceability support, publish a contract, or claim full v1 conformance.
