---
spec: SPEC-0008
scope: portable-core-example-audit-implementation
assessment: approved
process_version: 1
sources:
  - path: AGENTS.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: 71bf914cd8edf48b6af94544c342c4ad2c906929
    content_sha256: fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e
  - path: specs/0001-core-pipeline-model.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e
  - path: specs/0002-operation-catalogs-and-host-configuration.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 71bf914cd8edf48b6af94544c342c4ad2c906929
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 77cbd9e62a3a5c512f6d4a86fb6a024220a58f3a
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 07d7b41d910f9dc7a65fea1cb05fb4c62bf6e7cb
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: a3242861598a02c89ffabfb047130d4dd4290127
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/specifications.md
    revision: 911ede5a759d7288dc569002ab2bbb136caeb52d
    content_sha256: 9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a
  - path: .github/instructions/specifications.instructions.md
    revision: 911ede5a759d7288dc569002ab2bbb136caeb52d
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: work/0008/plan.md
    revision: a8c81232c4cf4c3f2d2ff1d0817bb78f4be30b7f
    content_sha256: e54cdcc250aa7a680b74c81c2d2b8c97483feb933e6162f90c14ff84e7d2e646
    material_sha256: 6a79348b7686002e8a03592ef3a76b50e737a5cdb03e5e6f24dee8a0485a9890
  - path: work/0008/implementation/I-0008-013-portable-core-example-audit.md
    revision: c4f0eeea1710845daa1948dda4470a5fe15196d8
    content_sha256: f7e07579ec06fdad346884601770293f7073202c079f960712638883ccef39d0
    material_sha256: 9a4bba8d11db0377d23ddd7b0c74f6e5b65168ef5aca68d57e236b1a1e7b8ab7
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: 6b47ffe9e002a3a10a40bcaab2c2cbf7ac6cffdf
    content_sha256: 83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b
    material_sha256: 95f90d0395b8a86df7cd0e500b143f6694e7a24ca23e705d414cab9230a76cdf
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: e6e57f0a4ddec76228cb7e3a1a738ff401134997
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
    material_sha256: 8dd62a8d33871880f7c6281433c337c2213e0afed73d59595af53504ef48ccaf
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: 77cbd9e62a3a5c512f6d4a86fb6a024220a58f3a
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
    material_sha256: c8ae60bf1bdbb10277b47160a7a645cf1bbae969352a032942ec05dc6b910b26
  - path: work/0008/readiness/requirement-example-audit.md
    revision: a8c81232c4cf4c3f2d2ff1d0817bb78f4be30b7f
    content_sha256: f06524c898bf8165251fd8ef89c9f939d5a97e943ccc8441f438e3ad759d0b5d
    material_sha256: 02f56e89e8b1197fde3e9b558d5027b63520cf12080f526d2b46733d57a5a730
---

# SPEC-0008: Portable Core Example Audit Implementation Readiness

## Assessed scope

This is implementation-readiness assessment for [I-0008-013](../implementation/I-0008-013-portable-core-example-audit.md), limited to its exact editorial audit scope and five requirements:

- **R-0000-007** — portable CLI/MCP contracts, canonical JSON, execution semantics, and conformance data are language-neutral and normative; .NET is the v1 reference implementation, not the semantic authority.
- **R-0001-011** — decorator nesting order is semantically significant; code and JSON preserve explicit nesting, with the retry/timeout example inside the requirement block.
- **R-0001-052** — exported examples/defaults are non-authoritative absent input-schema semantics; generators do not invent required values or silently replace invalid input.
- **R-0002-017** — Windows paths are described as illustrative while portable path and URI handling remains normative.
- **R-0008-005** — specifications classify content by authority, scope, and requirement-block boundaries; portable rules remain language-independent, scoped language contracts stay outside portable blocks, rationale stays non-normative, and examples inside/outside blocks receive their respective normative/illustrative treatment and labels.

The exact conditional edit manifest is only `SPEC.md`, `specs/0001-core-pipeline-model.md`, and `specs/0002-operation-catalogs-and-host-configuration.md`; modification is allowed only for editorial classification that preserves existing behavior and conformance. The audit must inventory the assigned sources' examples, rationale, and behavior-affecting defaults, record their dispositions, identify proposed edits and affected requirement fingerprints/reverse references, and stop rather than decide a behavior change.

## Exclusions

No other numbered specification, schema, conformance vector, implementation code, trace-checker behavior, or release/publication claim is assessed. No behavior or conformance amendment is authorized. Language-native traceability placements and checker ownership remain outside this slice under D-0008-008. This is not a whole-v1 conformance assessment.

## Completeness and consistency

D-0008-003 is complete and its accepted labeling rule governs this audit. ADR-0003 supplies stable requirement-block and fingerprint mechanics; ADR-0004 distinguishes editorial restatement from behavior-changing amendment. The five fingerprints were reverified against the assessed source snapshot: R-0000-007@ce715f, R-0001-011@dc130a, R-0001-052@bca5b5, R-0002-017@8e4312, and R-0008-005@107883.

The known classification/conformance risk is in SPEC-0002: the “Illustrative shape” JSON appears within R-0002-016's requirement block, while R-0002-017 describes its Windows paths as illustrative. R-0008-005 makes examples inside blocks normative and requires **Normative example** labeling, while examples outside blocks are illustrative and require **Illustrative example** labeling. The audit must determine from the complete surrounding requirements whether the shape or only its path values illustrates already specified behavior and whether any relocation/rewording preserves every required field and portability expectation. No classification is resolved here. If evidence does not establish behavior-preserving editorial treatment, the audit must stop for a separate specification decision/readiness assessment.

R-0001-011's in-block example is within the normative block and must be assessed as such, not dismissed as explanation. R-0001-052 sets a clear boundary for exported documentation and schema-defined semantics; the audit must not infer defaults from examples. R-0000-007 prevents importing .NET behavior as portable authority. The slice's stop rule and narrow manifest make the work bounded, but completion still requires an exhaustive source inventory and reverse-impact review; this readiness assessment does not claim that audit has been performed.

No new product or architectural decision was discovered as a prerequisite to conducting the bounded audit. The current SPEC-0002 text labels its host-configuration JSON block “Illustrative shape”; because R-0008-005 requires an outside-block example to be introduced as **Illustrative example**, and R-0002-017 follows that block while describing its Windows paths, the audit must determine and record the exact classification without presuming the whole shape or only its paths are illustrative. This is a known audit finding requiring evidence-based disposition, not an accepted answer or an implementation blocker. The aggregate I-0008-002 milestone assigns SPEC.md and SPEC-0001/0002 to this child within its four disjoint audits; its earlier readiness authorized planning only and is not execution authority.

## Conformance and prerequisite artifacts

This documentation-only slice requires accurate requirement identity/fingerprint inventory, explicit dispositions, link review for affected material, and whole-repository reverse-impact review for any changed requirement block. No product schema or vector is an entry prerequisite: they are explicitly excluded and no audited requirement requires their production to perform this classification audit. If an audit outcome changes normative behavior or conformance, that outcome needs a separate approved specification decision and readiness gate before editing.

D-0008-003 is complete. The exact I-0008-013 plan has previously recorded approval, but its reviewed hashes changed and must be renewed after this readiness snapshot is approved. The previous readiness approval is not carried forward: the I-0008-013 source had changed in its plan-approval evidence, and the prior readiness snapshot recorded only that item's full-byte hash rather than a material hash. This reassessment records both the exact current bytes and material hash; the plan's material hash remains unchanged. Current plan sources were verified, so no `work-plan-sync` source-input reconciliation is a prerequisite. The item-level inventory, proposed edits, fingerprints, reverse-impact findings, validation, and delivery review remain execution outputs, not prerequisites that this readiness record can substitute for.

## Blockers

No missing source reconciliation or unresolved prerequisite prevents this bounded audit from being ready for human review. There is no new decision to reconcile. The classification issue around R-0002-017 remains an explicit implementation stop condition if its disposition cannot be shown behavior-preserving; it is not permission to choose or change semantics.

Implementation remains blocked until this exact readiness snapshot is explicitly approved, the exact slice plan approval is renewed for its current reviewed hashes, and the audited source and aggregate scope remain current at execution. The earlier readiness approval is historical and is not inherited. The aggregate I-0008-002 milestone remains open and must eventually be satisfied by its required child slices; it does not replace this slice's own gates.

## Validation and approval

Reassessed against the exact source snapshots listed above. `python .agents/scripts/work_hashes.py verify work/0008/plan.md` reported every plan source current; verifying this readiness record reported every assessed source current, including material-based work-item and readiness inputs. The current requirements, exact conditional manifest, dependencies, entry/exit gates, D-0008-003 resolution, four-child I-0008-002 scope, and historical approvals were reviewed. The five requirement fingerprints were verified: R-0000-007@ce715f, R-0001-011@dc130a, R-0001-052@bca5b5, R-0002-017@8e4312, and R-0008-005@107883. The earlier readiness snapshot was explicitly approved on 2026-10-13 (pre-approval full-byte SHA-256 `da601d0b504fc07c1e77dcb3d5faa959ce52804bc91f3bf759344e74132670ce`); that approval remains historical and does not approve this reassessment. This snapshot is `ready-for-review`; no new approval is recorded.

The record's source list includes current full-byte hashes and baseline revisions. Work-item, plan, and readiness sources include their material hashes to distinguish lifecycle/evidence-only updates from scope changes. The relative link to I-0008-013 exists; `git diff --check` passed. `/spec-trace-check` passed with `Change-Kind: maintenance` and no `Spec:` trailer; only this readiness documentation changed. No build or product unit tests apply to this documentation-only readiness assessment; none is claimed.

Approval history: The user explicitly approved the previous exact readiness snapshot in this session on 2026-10-13 for I-0008-013 implementation readiness, its conditional three-specification-file manifest, five requirements, and stated exclusions. Its approval did not approve the slice plan, authorize implementation, make a behavior or conformance change, publish a contract, or claim whole-v1 conformance. It is not approval of this reassessed snapshot.

The user explicitly approved this exact readiness snapshot in this session on 2026-10-13. Approval is limited to I-0008-013 implementation readiness for the scope, conditional three-specification-file manifest, five requirements, and exclusions stated above. The approved pre-approval full-byte SHA-256 is `afe3b663a61c4373c63f4c59fb53de790545fecd6881486624e4114c2a6b0659`; the readiness-material digest for this assessed snapshot (computed by `work_hashes.py sources`) is `17d2ecaa5911a6ce59f79e029feb735408191edbd7ac9456c87a6236c0aeab53`. Every exact assessed source hash and baseline revision in the `sources` frontmatter above was verified current. This approval does not approve the I-0008-013 slice plan, authorize implementation, make any behavior or conformance change, publish a contract, or claim whole-v1 conformance.

Approved source snapshot (full-byte SHA-256):

| Path | SHA-256 |
| --- | --- |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `SPEC.md` | `fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e` |
| `specs/0001-core-pipeline-model.md` | `38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e` |
| `specs/0002-operation-catalogs-and-host-configuration.md` | `c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `docs/architecture/decisions/0003-enforce-specification-traceability.md` | `da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411` |
| `docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md` | `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| `docs/development/coding-conventions.md` | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/conventions/specifications.md` | `9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a` |
| `.github/instructions/specifications.instructions.md` | `7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2` |
| `work/0008/plan.md` | `e54cdcc250aa7a680b74c81c2d2b8c97483feb933e6162f90c14ff84e7d2e646` |
| `work/0008/implementation/I-0008-013-portable-core-example-audit.md` | `f7e07579ec06fdad346884601770293f7073202c079f960712638883ccef39d0` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | `83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/decisions/D-0008-008-language-native-traceability.md` | `a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5` |
| `work/0008/readiness/requirement-example-audit.md` | `f06524c898bf8165251fd8ef89c9f939d5a97e943ccc8441f438e3ad759d0b5d` |
