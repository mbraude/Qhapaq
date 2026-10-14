---
spec: "SPEC-0008"
scope: remaining-portable-specification-audit-implementation
assessment: approved
process_version: 1
sources:
  - path: AGENTS.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e
  - path: specs/0003-product-evolution-roadmap.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 2b5fced51668b8bd2d586e377adbf667deabc3cb48c8569890ec7e709992ce32
  - path: specs/0004-ai-assisted-connections.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 39625b975496c96ae55c21785fd632f75d10096349acc82a4d277fc93c698e57
  - path: specs/0005-build-release-and-website-delivery.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 8259be3d7e256d77ab18e96c35906ce64c01d25eb7a22f45a911c0727d1a1679
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825
  - path: docs/development/coding-conventions.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/specifications.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a
  - path: .github/instructions/specifications.instructions.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: work/0008/plan.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 3cffe3e26f15fd00ffccc1907382b79920205773216625c71a2f7585b57ad121
    material_sha256: 6a79348b7686002e8a03592ef3a76b50e737a5cdb03e5e6f24dee8a0485a9890
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b
  - path: work/0008/implementation/I-0008-014-remaining-portable-specification-audit.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: e97bab3e05e3815836ba75b423a27fae07bf30a8ab98e79033299b742205d5f2
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
  - path: work/0008/readiness/requirement-example-audit.md
    revision: 910e5fd40bfdea4ab9bf73a6ce06418633114996
    content_sha256: 5186fbba33d1810efc047a7f14715a998980630b32112c23c116898239f8c9cf
---

# SPEC-0008: Remaining Portable Specification Audit Implementation Readiness

## Assessed scope

Assess implementation readiness for [I-0008-014](../implementation/I-0008-014-remaining-portable-specification-audit.md), limited to an exhaustive inventory and evidence-based disposition of normative/non-normative content, examples, rationale, and behavior-affecting defaults in:

- `specs/0003-product-evolution-roadmap.md` — R-0003-001 through R-0003-023 (23 requirement blocks).
- `specs/0004-ai-assisted-connections.md` — R-0004-001 through R-0004-043 (43 requirement blocks).
- `specs/0005-build-release-and-website-delivery.md` — R-0005-001 through R-0005-033, plus R-0005-034 and R-0005-035 (35 requirement blocks; all 35 identifiers are present).

The governing requirements are SPEC.md R-0000-007 and SPEC-0008 R-0008-005. The exact conditional edit manifest is only these three source files; edits are permitted only for editorial classification that demonstrably preserves behavior and conformance. Delivery evidence must inventory each example, rationale block, and potentially behavior-affecting default; record its disposition, any proposed edit and affected fingerprint, reverse-impact references, and validation. This readiness assesses the scope; it does not perform that delivery audit.

## Exclusions

No change to behavior, requirement meaning or identity, conformance expectations, security policy, compatibility, release gates, implementation, schema, vector, checker, or publication is authorized. Excluded targets are SPEC.md, SPEC-0001/0002, SPEC-0006/0007/0008, source code, schemas, conformance vectors/profiles, trace-checker behavior, and language-native traceability placement. SPEC-0008 R-0008-005, D-0008-003, D-0008-008, ADR-0003, ADR-0004, and the engineering policies are governing inputs, not edit targets. This is not a whole-v1 conformance claim.

## Completeness and consistency

R-0000-007 makes portable CLI/MCP contracts, canonical JSON, execution semantics, and conformance data language-neutral and normative; the .NET v1 implementation is not semantic authority. R-0008-005 and D-0008-003 provide a determinate classification rule: rationale and future direction stay outside requirement blocks; examples outside blocks are illustrative and must be labeled; examples inside blocks are normative, labeled accordingly, and part of the requirement fingerprint and conformance expectations. ADR-0003 defines block boundaries and fingerprinting; ADR-0004 separates editorial clarification from behavior amendments and requires reverse-impact review for changed blocks.

The complete target files are bounded, implementation-neutral specifications with stable requirement ranges recorded above. SPEC-0003 mixes requirements with post-v1 direction, defaults, provider examples, and an evolution sequence. SPEC-0004 contains security-sensitive connection, consent, authentication, policy, and disclosure contracts, plus JSON and tool-name examples. SPEC-0005 specifies CI, build, release, website, credential, provenance, recovery, and publication behavior through extensive lists and tables. Lists, tables, and code inside requirement blocks are not presumed illustrative; defaults, "should" language, named examples, failure behavior, limits, privacy/security rules, and compatibility constraints all require block-level review.

Known audit candidates include the provider examples in R-0003-003; the project-catalog JSON preceding R-0004-013; the host-profile JSON inside R-0004-013 while R-0004-014 calls the property names illustrative; and the MCP tool list inside R-0004-015 followed by prose that calls tool names illustrative. These are inventory/disposition questions, not pre-approved edits or new product decisions. Classify them using R-0008-005 and established surrounding requirements; if an editorial treatment cannot be shown to preserve required meaning or conformance, stop and raise a separate specification decision/readiness assessment rather than resolving the behavior here. SPEC-0003/0004/0005 open questions remain unresolved and out of scope unless a finding makes an accepted requirement indeterminate.

Cross-spec consistency is adequately bounded: preserve R-0000-007 portability, R-0008-005 authority labels, SPEC-0004's independent execution/disclosure permissions and default-deny boundary, and SPEC-0005's protected publication, immutable artifacts, and recovery gates. No issue was found that prevents the bounded audit from inventorying all target material under its stop rule. Scope is disjoint from I-0008-013 (SPEC.md/SPEC-0001/0002), I-0008-015 (SPEC-0007), and I-0008-016 (SPEC-0006/SPEC-0008 and traceability guidance).

## Conformance and prerequisite artifacts

The delivery must preserve requirement identifiers; classify content consistently with R-0008-005; treat in-block examples as normative and fingerprint-relevant; verify any changed block fingerprints and all reverse-impact references; and stop at any behavior/conformance amendment. I-0008-014 requires specification traceability review, affected relative-link review, and `git diff --check`; it explicitly excludes product builds and unit tests for this documentation-only editorial slice.

No schema, vector, profile, release artifact, or published conformance vector is an entry prerequisite for this audit. Distinguish specified expectations (including any normative example in a requirement block) from separately published vectors; do not infer that every example must have its own vector. D-0008-003 is complete and present. The approved `requirement-example-audit` readiness applies only to planning the I-0008-002 aggregate and does not authorize editing. The parent I-0008-002 scope remains an aggregate over four disjoint child audits; the current plan preserves the I-0008-014 slice and its assigned files.

## Blockers

No unresolved decision or missing product/conformance artifact prevents review of this bounded readiness scope. The audit's named mixed-content candidates are not resolved here; the item's stop condition governs if classification would change meaning.

Execution remains gated on **both** (1) explicit approval of this exact current readiness record and (2) separate explicit approval of the exact I-0008-014 plan. I-0008-014 currently says plan approval is absent. The readiness approval previously recorded for the older assessment does not approve this reassessed snapshot or the plan and does not authorize implementation.

## Validation and approval

Currentness/impact review (2026-10-13): the current target-specification SHA-256 values equal the hashes already recorded in the reconciled SPEC-0008 plan. I-0008-014, D-0008-003, I-0008-002, and the parent planning-readiness bytes also match their recorded snapshots. Since the prior readiness assessment, `work/0008/plan.md` changed (`f6ba2d2` to current HEAD) only by further detailing/decomposing I-0008-003 conformance-artifact delivery; the bounded diff and current item/phase links show no change to I-0008-014 requirements, dependencies, scope, manifest, entry gates, or acceptance criteria. The parent I-0008-002 scope remains the same four disjoint child slices. The refreshed runbook was inspected only as derived navigation to this scope; it is not an authoritative readiness input. Its source hash is intentionally omitted below because `work-runbook-sync` includes readiness records in its runbook source-set digest and excludes the runbook itself. Recording the generated runbook as a readiness source would create a cycle: changing this record changes the digest, regeneration changes the runbook bytes, and that change would invalidate this record's runbook hash. The workflow guide identifies the runbook as a derived view and the plans, work items, readiness records, approvals, and authoritative sources as status/eligibility authority. Excluding the runbook therefore preserves the established authority boundary rather than weakening the assessment. The observed prior recorded hash `6ef9a6c3e2b878d2bc9c8058c612fda945bb04357b05f604523cd5b8d4d4110e` did not match the working-copy runbook inspected for this reassessment (file-byte SHA-256 `39cc17f3ca75a6811d6078e3a743173879e4342fa02735e3d0b67f444dcbd308`); this is not a readiness blocker because the generated view is not an assessed source. The runbook source-set digest must be regenerated to reflect this reassessment, but that derived-view refresh does not feed back into readiness currentness. The other source changes require reassessment but do not invalidate the bounded I-0008-014 scope.

Current assessed revision is repository HEAD `910e5fd40bfdea4ab9bf73a6ce06418633114996`; all listed committed inputs are hashed by exact bytes at that revision. The prior readiness artifact currently had SHA-256 `4b927fd7bd992fe255a90bea2a5d7c35a7cd865b0c37b12341b03cfdfa1251a3`; its pre-approval exact record hash was `771bb1d1907bf5ea0145228a2e4c903aa38035bc73612c580c34aadc771aa519`. Explicit approval on 2026-10-12 applied only to that earlier assessed snapshot and remains historical evidence, not approval of this record.

Validation performed 2026-10-13: `/spec-trace-check` returned `PASS`; this readiness record is a maintenance work artifact with no changed requirement blocks, code/tests, references, or waivers. All 20 listed source paths, exact-byte hashes, and committed revisions were verified; the generated runbook is intentionally excluded for the documented source-cycle reason. The 22 source records in `work/0008/plan.md` were also verified against current bytes and resolving revisions. The one repository-relative Markdown link in this record resolves. The three target-source requirement-block counts and exact identifiers were checked (23, 43, and 35; 101 total), hashes match the recorded target snapshots, and `git diff --check` passed. No product build or unit tests apply. Readiness is scoped to I-0008-014 and does not publish a contract, authorize implementation, or assert whole-v1 conformance.

### Approval evidence

The user explicitly approved this exact readiness snapshot in this session on
2026-10-13. No approver name was supplied.

- Scope: SPEC-0008 readiness for I-0008-014, governing requirements
  R-0000-007 and R-0008-005, with conditional editorial-only edits limited to
  SPEC-0003, SPEC-0004, and SPEC-0005.
- Exclusions: no behavior, requirement meaning or identity, conformance,
  security policy, compatibility, release gates, implementation, schema,
  vector, checker, or publication changes; no edits to SPEC.md,
  SPEC-0001/0002, SPEC-0006/0007/0008, source code, schemas, conformance
  vectors/profiles, trace-checker behavior, or language-native traceability
  placement; no whole-v1 conformance claim.
- Reviewed readiness record, before this evidence was recorded (full-byte
  SHA-256): `d5aad04555194201ad3eaceb6d86c2bae62322cbbdb0a82cbcd1f6e59c430f83`.
- Other approved commit file, `work/0008/runbook.md` (full-byte SHA-256):
  `29231ec0fb87fb697a3420a760b2532ecdbfcf7cac3009bdba75fe8b025e3230`.
- Assessed source/input hashes and revisions: the 20 source records above,
  each at revision `910e5fd40bfdea4ab9bf73a6ce06418633114996`; all current
  file hashes and revision contents were reverified on 2026-10-13.
- Final approval validation: `/spec-trace-check` passed with the maintenance
  classification and no changed requirement blocks or code; `git diff --check`
  passed. Build and unit tests were omitted because this is documentation-only.

This approval applies only to the reviewed readiness scope and snapshot.
Separate approval of the I-0008-014 implementation plan is still required
before implementation; no component contract is published.