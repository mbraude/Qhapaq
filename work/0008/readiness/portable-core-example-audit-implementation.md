---
spec: SPEC-0008
scope: portable-core-example-audit-implementation
assessment: approved
sources:
  - path: AGENTS.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e
  - path: specs/0001-core-pipeline-model.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e
  - path: specs/0002-operation-catalogs-and-host-configuration.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825
  - path: docs/development/coding-conventions.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/specifications.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a
  - path: docs/development/spec-driven-workflow.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: da0d7ea110236bddcebc9607b435721ecf53d00dff7694a2f43a402f819b3ea2
  - path: .github/instructions/specifications.instructions.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: work/templates/readiness.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 707d334f40feb8e3462f8ee814c55ce3a8f66c32a860a4b8557d5eaa2f672bf2
  - path: work/0008/plan.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: b602977cd2f1d5ccc617f5d54ef049c0f5c615f0f6dab7d333481ab44a0d6f20
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b
  - path: work/0008/implementation/I-0008-013-portable-core-example-audit.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 5188a6e7259b6ddd97069cf427920b20ec5512bf7a7287a23da33ca5595d7880
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
  - path: work/0008/readiness/requirement-example-audit.md
    revision: 52177dc892fae1fca8a34901f9f498345bef0a69
    content_sha256: 5186fbba33d1810efc047a7f14715a998980630b32112c23c116898239f8c9cf
---

# SPEC-0008: Portable Core Example Audit Implementation Readiness

## Assessed scope

Assess implementation readiness for [I-0008-013](../implementation/I-0008-013-portable-core-example-audit.md): audit `SPEC.md`, SPEC-0001, and SPEC-0002 for normative and illustrative content, examples, and behavior-affecting defaults under R-0008-005. The governing requirements are R-0000-007, R-0001-011, R-0001-052, R-0002-017, and R-0008-005. The slice may make only editorial clarifications that preserve existing behavior and conformance expectations.

The exact edit manifest is limited to `SPEC.md`, `specs/0001-core-pipeline-model.md`, and `specs/0002-operation-catalogs-and-host-configuration.md`. The files are in the slice manifest conditionally: modify them only when required for the approved editorial classification. The aggregate audit scope and other specification files are excluded.

## Exclusions

This assessment does not authorize requirement or conformance changes, edits outside the three-file manifest, implementation or checker changes, conformance-vector or schema production, or publication of any contract. Language-native traceability placement and checker behavior remain under D-0008-008 and their separate delivery scope. Whole-v1 conformance is not assessed.

## Completeness and consistency

The governing boundary is explicit: R-0000-007 makes portable contracts language-neutral, and R-0008-005 distinguishes portable requirements, explicitly scoped language contracts, rationale, illustrative examples outside requirement blocks, and normative examples inside them. D-0008-003 is complete and accepted R-0008-005. ADR-0003 supplies stable requirement-block and fingerprint rules; ADR-0004 requires editorial changes to cite reworded requirements and distinguishes them from behavior-changing amendments.

The five assessed requirements currently resolve to these fingerprints: R-0000-007@ce715f, R-0001-011@dc130a, R-0001-052@bca5b5, R-0002-017@8e4312, and R-0008-005@107883. The candidate R-0001-011 example occurs within its requirement block; the audit must classify it under R-0008-005 rather than assume it is merely explanatory. R-0001-052 governs when exported examples and defaults are authoritative and forbids inventing omitted required values. R-0002-017 combines a Windows-path example described as illustrative with a requirement for portable path and URI handling, while R-0008-005 makes examples inside requirement blocks normative. This is a classification issue to document and assess; do not silently move, relabel, or otherwise change its conformance meaning. If resolution requires a behavior or conformance change, stop for a separate specification decision and reassessment.

The slice has a defined boundary and safe stopping rule for unresolved material behavior. No additional product decision is required to conduct the bounded audit and record dispositions. Current SPEC-0008 and SPEC-0007 plan source records were checked in the refreshed runbook; the current plan and slice snapshots are included above. The earlier `requirement-example-audit` readiness authorizes planning I-0008-002 only and is not used as implementation authorization here.

## Conformance and prerequisite artifacts

The audit must preserve requirement identities and current fingerprints, distinguish specified expectations from published examples, and review every changed requirement block's references and reverse impact. The current work is documentation-only and does not require product schemas or conformance vectors as entry artifacts: I-0008-013 explicitly excludes them, and the referenced requirements define the classification and portability criteria needed for this audit. If the audit identifies a need to change required behavior, it must stop rather than treat a future artifact or this assessment as authorization.

The slice also requires completed D-0008-003, explicit approval of this readiness scope, and later approval of the exact I-0008-013 plan before execution. D-0008-003 is complete; this readiness assessment itself is not approved.

## Blockers

No unresolved prerequisite prevents the bounded audit from being planned for review. The potential R-0002-017 classification conflict is an explicit audit finding to resolve or escalate within the slice's stop rule, not permission to alter conformance. Any material resolution requires a separate specification decision and reassessment. Implementation remains blocked until this exact readiness snapshot and the concrete slice plan receive explicit approval.

## Validation and approval

Assessed against the source hashes in the frontmatter at HEAD `52177dc892fae1fca8a34901f9f498345bef0a69`. Verified the five requirement fingerprints with the repository trace-check fingerprint algorithm; checked the slice manifest against its three named specification files; confirmed D-0008-003 is complete and the existing planning-readiness scope does not authorize implementation; and reviewed the cross-specification portability and example-classification rules. The refreshed runbook source snapshot covers 70 inputs and was checked against their sorted paths and exact bytes.

The specification trace check covered the changed runbook and readiness record. Both are other documentation/workflow files, classified as maintenance; no specification requirement blocks or product code changed, so there were no requirement references or semantic code-review targets. No waivers were added. The check returned PASS with proposed trailer `Change-Kind: maintenance` and no `Spec:` trailer. `git diff --check`, changed-file whitespace checks, and relative-link checks passed. No build or product unit tests apply to this documentation/workflow assessment. This assessment is scoped and does not establish full v1 conformance.

Explicitly approved in this session on 2026-10-12 for the readiness record SHA-256 `b42fad67e286d0f77c97c8ab31c99f6c9288d2fed3f81fb2969f49055fb105dc` and the 19 exact source snapshots listed above, verified at HEAD `52177dc892fae1fca8a34901f9f498345bef0a69`. Approval covers only the `portable-core-example-audit-implementation` readiness scope and its stated exclusions. It does not approve the I-0008-013 plan or authorize implementation, change behavior/conformance, publish a contract, or establish full v1 conformance.
