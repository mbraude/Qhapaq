---
spec: SPEC-0008
scope: portable-binding-specification-audit-implementation
assessment: approved
sources:
  - path: .github/instructions/specifications.instructions.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: AGENTS.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e
  - path: conformance/README.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/schemas.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2
  - path: docs/development/conventions/specifications.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a
  - path: docs/development/spec-driven-workflow.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: da0d7ea110236bddcebc9607b435721ecf53d00dff7694a2f43a402f819b3ea2
  - path: schemas/README.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 9735bf13164fda904d9d926a1ef896038360c7334e8ad831cac195dfc59ab0a1
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b
  - path: work/0008/implementation/I-0008-015-portable-binding-specification-audit.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 607d7caef3b548d6f05273a79f810e2b33135245c9bb8580c81306c85a0faaac
  - path: work/0008/plan.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: b602977cd2f1d5ccc617f5d54ef049c0f5c615f0f6dab7d333481ab44a0d6f20
  - path: work/0008/readiness/requirement-example-audit.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 5186fbba33d1810efc047a7f14715a998980630b32112c23c116898239f8c9cf
  - path: work/templates/readiness.md
    revision: e989d2b4337550bc1577f79b9d39c09d159d2368
    content_sha256: 707d334f40feb8e3462f8ee814c55ce3a8f66c32a860a4b8557d5eaa2f672bf2
---

# SPEC-0008: Portable Binding Specification Audit Implementation Readiness

## Assessed scope

Assess implementation readiness for
[I-0008-015](../implementation/I-0008-015-portable-binding-specification-audit.md):
inventory normative and non-normative content, examples, rationale, and
potentially behavior-affecting defaults throughout SPEC-0007. The governing
requirements are R-0000-007 and R-0008-005. The exact conditional edit manifest
is limited to `specs/0007-portable-pipeline-definitions-and-binding.md`; edits
are permitted only for editorial classification that preserves existing
behavior and conformance expectations.

## Exclusions

This assessment does not authorize changes to product behavior, conformance
expectations, requirement meaning or identifiers, implementation, schemas,
conformance vectors, profiles, or their README artifacts. It does not assess
other numbered specifications or checker behavior. SPEC-0000 R-0000-007,
SPEC-0008 R-0008-005, D-0008-003, and the applicable traceability decisions
are read-only authorities, not targets of this slice.

## Completeness and consistency

R-0000-007 makes portable pipeline semantics, canonical JSON, CLI/MCP
contracts, and conformance data language-neutral; the .NET reference
implementation cannot override those specifications. R-0008-005 assigns
content categories and says that examples outside requirement blocks are
illustrative and non-normative, while examples inside a block are normative,
labeled as such, and part of its fingerprint and conformance expectations.
D-0008-003 is complete and accepted. ADR-0003 defines requirement-block
boundaries and fingerprint effects; ADR-0004 distinguishes editorial
clarification from behavior amendment and requires reverse-impact review when
requirement blocks change.

SPEC-0007 is a large, structured specification covering pipeline definitions,
dataflow, transforms, schema profiles, operation descriptors, .NET declarations,
binding, diagnostics, AI/MCP authoring, security, compatibility, testing, and
migration. The audit must inspect the complete file, including examples
embedded in prose, tables, and JSON/code blocks, and record dispositions rather
than infer classification from headings alone. The specification's
open-questions section states that no question remains for the initial Service,
CLI, or MCP contracts; later optional surfaces require a new exact versioned
contract. This does not authorize resolving or extending those surfaces during
the audit.

The classification method is determinate for the bounded editorial task.
Content outside requirement blocks remains non-normative; examples there must
be explicitly illustrative and cannot add, relax, or contradict required
behavior. Content inside requirement blocks is normative. If an item can be
reclassified only by changing a required behavior, conformance expectation,
ownership boundary, or unresolved contract, stop and request the appropriate
specification/ADR decision and a reassessment. Preserve requirement IDs; review
fingerprints and all repository references for every changed block.

The audit is disjoint from I-0008-013, I-0008-014, and I-0008-016. I-0008-002
remains an aggregate milestone, not an executable substitute. The existing
`requirement-example-audit` readiness authorizes planning I-0008-002 only and
does not authorize edits to SPEC-0007.

## Conformance and prerequisite artifacts

I-0008-015 requires checking schema and conformance links only to confirm that
ownership and normative status are represented consistently. The schema and
conformance READMEs and their authoring convention were reviewed for this
boundary. The audit does not alter schemas, vectors, profiles, or their owning
guidance. No new schema/vector is an entry prerequisite for this
documentation-only classification audit; existing requirement blocks and
R-0008-005 define the applicable expectations. Any discovered inconsistency
requiring a material schema, vector, behavior, or conformance change is outside
this manifest and must be routed to its owner for separate planning and
approval.

D-0008-003 is complete. The exact I-0008-015 plan still requires separate plan
approval before execution. This readiness assessment requires its own explicit
approval for the assessed implementation scope; neither approval is implied
here.

## Blockers

No unresolved prerequisite prevents planning and reviewing the bounded
SPEC-0007 audit. Any substantive behavior, conformance, architecture, or
ownership ambiguity discovered while auditing is a stop condition, not
authority to edit. Plan approval and implementation readiness approval remain
separate lifecycle gates.

## Validation and approval

Reviewed R-0000-007, R-0008-005, D-0008-003, ADR-0003, ADR-0004,
SPEC-0007's complete outline and open-questions boundary, the I-0008-015 exact
manifest and entry gates, parent I-0008-002, and the planning-readiness
exclusion. Reviewed the applicable specification, schema, and conformance
authoring guidance and their README ownership descriptions. Captured 19 exact
source-file hashes against repository HEAD
`e989d2b4337550bc1577f79b9d39c09d159d2368`; the source tree was unchanged at
those paths.

The runbook snapshot refresh passed `git diff --check`. Reviewed both changed
files under ADR-0003/ADR-0004; the runbook and readiness record are
maintenance-only documentation and require no `Spec:` trailer or inline
requirement markers. Specification trace review passed. All 19 readiness
source hashes and relative links were verified; `git diff --check` passed. No
product build or unit tests apply to this documentation-only readiness
assessment.

Explicitly approved in this session on 2026-10-12 for I-0008-015
implementation readiness only, against the exact pre-approval full-byte
SHA-256 `bf7f7d28282ec73d4b0a95989b039cf628234d94d05f379fd3cfe04fed1ff1cc`.
All 19 assessed source hashes were verified against current bytes at revision
`e989d2b4337550bc1577f79b9d39c09d159d2368`. This approval does not approve
the slice plan, authorize implementation, publish a contract, or claim
whole-v1 conformance.
