---
spec: SPEC-0008
scope: portable-core-example-audit-implementation
assessment: approved
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
  - path: docs/development/spec-driven-workflow.md
    revision: b627023baef4d16d8c1c3598b24ba9d66f9e96bb
    content_sha256: da0d7ea110236bddcebc9607b435721ecf53d00dff7694a2f43a402f819b3ea2
  - path: .github/instructions/specifications.instructions.md
    revision: 911ede5a759d7288dc569002ab2bbb136caeb52d
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: work/templates/readiness.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 707d334f40feb8e3462f8ee814c55ce3a8f66c32a860a4b8557d5eaa2f672bf2
  - path: work/0008/plan.md
    revision: 9396b5567d753f80057164527185d6faa37f0c8e
    content_sha256: 3cffe3e26f15fd00ffccc1907382b79920205773216625c71a2f7585b57ad121
  - path: work/0008/implementation/I-0008-013-portable-core-example-audit.md
    revision: 6b47ffe9e002a3a10a40bcaab2c2cbf7ac6cffdf
    content_sha256: 5188a6e7259b6ddd97069cf427920b20ec5512bf7a7287a23da33ca5595d7880
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: 6b47ffe9e002a3a10a40bcaab2c2cbf7ac6cffdf
    content_sha256: 83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: e6e57f0a4ddec76228cb7e3a1a738ff401134997
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: 77cbd9e62a3a5c512f6d4a86fb6a024220a58f3a
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
  - path: work/0008/readiness/requirement-example-audit.md
    revision: d812bf214b5856dd0e21f23e7736fdfd4a8aa4c9
    content_sha256: 5186fbba33d1810efc047a7f14715a998980630b32112c23c116898239f8c9cf
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

D-0008-003 is complete and its accepted labeling rule governs this audit. ADR-0003 supplies stable requirement-block and fingerprint mechanics; ADR-0004 distinguishes editorial restatement from behavior-changing amendment. The current fingerprints were independently recomputed from the exact source bytes using the trace-check helper: R-0000-007@ce715f, R-0001-011@dc130a, R-0001-052@bca5b5, R-0002-017@8e4312, and R-0008-005@107883.

The known classification/conformance risk is in SPEC-0002: the “Illustrative shape” JSON appears within R-0002-016's requirement block, while R-0002-017 describes its Windows paths as illustrative. R-0008-005 makes examples inside blocks normative and requires **Normative example** labeling, while examples outside blocks are illustrative and require **Illustrative example** labeling. The audit must determine from the complete surrounding requirements whether the shape or only its path values illustrates already specified behavior and whether any relocation/rewording preserves every required field and portability expectation. No classification is resolved here. If evidence does not establish behavior-preserving editorial treatment, the audit must stop for a separate specification decision/readiness assessment.

R-0001-011's in-block example is within the normative block and must be assessed as such, not dismissed as explanation. R-0001-052 sets a clear boundary for exported documentation and schema-defined semantics; the audit must not infer defaults from examples. R-0000-007 prevents importing .NET behavior as portable authority. The slice's stop rule and narrow manifest make the work bounded, but completion still requires an exhaustive source inventory and reverse-impact review; this readiness assessment does not claim that audit has been performed.

No new product or architectural decision was discovered as a prerequisite to conducting the bounded audit. The R-0002-017 classification question is a known audit finding requiring evidence-based disposition, not an accepted answer. The aggregate I-0008-002 milestone currently assigns SPEC.md and SPEC-0001/0002 to this child within its four disjoint audits; its prior readiness was planning-only and is not execution authority.

## Conformance and prerequisite artifacts

This documentation-only slice requires accurate requirement identity/fingerprint inventory, explicit dispositions, link review for affected material, and whole-repository reverse-impact review for any changed requirement block. No product schema or vector is an entry prerequisite: they are explicitly excluded and no audited requirement requires their production to perform this classification audit. If an audit outcome changes normative behavior or conformance, that outcome needs a separate approved specification decision and readiness gate before editing.

D-0008-003 is complete. The readiness record and exact I-0008-013 plan each require explicit human approval before implementation; both approvals are absent for this assessed snapshot. The current plan source records were independently checked before assessment (22/22 exact recorded hashes match current bytes), so no `work-plan-sync` source-input reconciliation is a prerequisite. The item-level inventory, proposed edits, fingerprints, reverse-impact findings, validation and delivery review remain execution outputs, not prerequisites that this readiness record can substitute for.

## Blockers

No missing source reconciliation or unresolved prerequisite prevents this bounded audit from being ready for human review. There is no new decision to reconcile. The classification issue around R-0002-017 remains an explicit implementation stop condition if its disposition cannot be shown behavior-preserving; it is not permission to choose or change semantics.

Implementation remains blocked until this exact readiness snapshot is explicitly approved, the exact slice plan is approved, and the audited source and aggregate scope remain current at execution. The earlier readiness approval is not inherited. The aggregate I-0008-002 milestone remains open and must eventually be satisfied by its required child slices; it does not replace this slice's own gates.

## Validation and approval

Assessed against the exact source snapshots listed above. Verified current hashes for all 22 source records in `work/0008/plan.md`; verified all five requirement fingerprints from source bytes; reviewed the exact I-0008-013 manifest, dependencies, entry/exit gates, current D-0008-003 resolution, the four-child I-0008-002 scope, and the historical approvals. The previously approved I-0008-013 readiness snapshot had full-file SHA-256 `f5ab81db478183336e70db2e96b1a5c396d603069764e1e0e48b173f23f4c4ab` and recorded material SHA-256 `b42fad67e286d0f77c97c8ab31c99f6c9288d2fed3f81fb2969f49055fb105dc`; it is stale because its recorded plan hash `b602977cd2f1d5ccc617f5d54ef049c0f5c615f0f6dab7d333481ab44a0d6f20` differs from the reconciled current plan hash `3cffe3e26f15fd00ffccc1907382b79920205773216625c71a2f7585b57ad121`. The earlier I-0008-002 readiness is also limited to planning and its recorded I-0008-002 item and plan snapshots are historical; neither approval is carried forward.

Relative-link review passed (one repository-relative link checked), `git diff --check` passed, and all 18 readiness source hashes and recorded baseline revisions matched their current bytes. `/spec-trace-check` classified the changed readiness record and related runbook as other documentation (`maintenance`), found no specification/code/test hunks, derived no `Spec:` trailer, and passed. A final trace check was run after recording this result. No build or product unit tests apply to this documentation-only readiness assessment; none is claimed.

The user explicitly approved this exact readiness snapshot in this session on
2026-10-13. Approval is limited to I-0008-013 implementation readiness for the
scope, conditional three-specification-file manifest, five requirements, and
exclusions stated above. The exact pre-approval readiness-record full-byte
SHA-256 was
`da601d0b504fc07c1e77dcb3d5faa959ce52804bc91f3bf759344e74132670ce`.
All 18 assessed source hashes and their recorded baseline revisions above were
verified against current file bytes. This approval does not approve the
I-0008-013 slice plan, authorize implementation, make any behavior or
conformance change, publish a contract, or claim whole-v1 conformance.
