---
spec: SPEC-0008
scope: portable-binding-specification-audit-implementation
assessment: approved
authorizes: implementation
process_version: 1
sources:
  - path: .github/instructions/specifications.instructions.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2
  - path: AGENTS.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: SPEC.md
    revision: c5e1c6b1e3c8c4fb1ae61ecd2f1547986f90d65d
    content_sha256: 998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6
  - path: conformance/README.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/schemas.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2
  - path: docs/development/conventions/specifications.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a
  - path: schemas/README.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 9735bf13164fda904d9d926a1ef896038360c7334e8ad831cac195dfc59ab0a1
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: work/0008/decisions/D-0008-003-normative-content-labeling.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801
  - path: work/0008/implementation/I-0008-002-requirement-example-audit.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b
  - path: work/0008/implementation/I-0008-015-portable-binding-specification-audit.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 56dfc47b4d9325e89d00cdc66a4bb390a731f128f189dc7bfd51cef917824c68
  - path: work/0008/plan.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 3cffe3e26f15fd00ffccc1907382b79920205773216625c71a2f7585b57ad121
    material_sha256: 6a79348b7686002e8a03592ef3a76b50e737a5cdb03e5e6f24dee8a0485a9890
  - path: work/0008/readiness/requirement-example-audit.md
    revision: b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd
    content_sha256: 5186fbba33d1810efc047a7f14715a998980630b32112c23c116898239f8c9cf
    material_sha256: 02f56e89e8b1197fde3e9b558d5027b63520cf12080f526d2b46733d57a5a730
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

Since the prior assessed snapshot, SPEC.md moved its illustrative C# interface
example outside R-0000-002 and labeled it illustrative, leaving the portable
requirement text language-neutral. This is consistent with R-0008-005 and does
not change R-0000-007, the SPEC-0007 audit scope, or the conditional
SPEC-0007-only edit manifest.

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

D-0008-003 is complete, and the exact I-0008-015 plan was separately approved
on 2026-10-12. This readiness assessment still requires explicit approval for
the assessed implementation scope before the slice can execute; neither plan
approval nor this reassessment implies that approval.

## Blockers

No unresolved prerequisite prevents the bounded SPEC-0007 audit. Any
substantive behavior, conformance, architecture, or ownership ambiguity
discovered while auditing is a stop condition, not authority to edit. This
current assessment is ready for explicit review and approval; implementation
remains gated on that approval and the separately approved slice plan.

## Validation and approval

Reviewed R-0000-007, R-0008-005, D-0008-003, ADR-0003, ADR-0004,
SPEC-0007's complete outline and open-questions boundary, the I-0008-015 exact
manifest and entry gates, parent I-0008-002, and the planning-readiness
exclusion. Reviewed the applicable specification, schema, and conformance
authoring guidance and their README ownership descriptions. Verified all 19
source paths against the current working copy. The only changed source bytes
since the prior assessment are the SPEC-0008 plan and I-0008-015: the plan
adds conformance-delivery slices in later phases, and the item records the
separate approval of its unchanged material plan. Neither delta changes this
scope's requirements, manifest, dependencies, entry criteria, exclusions, or
readiness conclusion. The 17 other recorded source hashes remain current.
All inputs are committed at `b46ff279fb74bdcb1d8fe744ff1bcb9977e0b7fd`;
the generated runbook is excluded from this readiness source set. Seven Git
blobs differ from their working-copy bytes only by CRLF/LF line endings; their
LF-normalized content matches the recorded baseline. Source hashes record the
exact current working-copy bytes.

The current 19 source hashes and relative links were verified. This
reassessment additionally compared the SPEC.md delta with the prior recorded
source snapshot and confirmed that it changes only the placement and label of
the illustrative C# interface; R-0000-007 remains unchanged. The runbook
snapshot refresh and this readiness update passed `git diff --check`.
Specification trace review passed under ADR-0003/ADR-0004; this readiness
record and the generated runbook are maintenance-only documentation and
require no `Spec:` trailer or inline requirement markers. No product build or
unit tests apply to this documentation-only readiness assessment.

Historical approval: explicitly approved in this session on 2026-10-12 for
I-0008-015 implementation readiness only, against the prior exact pre-approval
full-byte SHA-256
`bf7f7d28282ec73d4b0a95989b039cf628234d94d05f379fd3cfe04fed1ff1cc`. A
subsequent approval on 2026-10-14 covered the then-current readiness snapshot
with pre-approval full-byte SHA-256
`e7a39c2b0471078a979f75c514fa3ad0b172eff4c7d9739a67b68562a13e04e0` and
runbook SHA-256
`cf42965796b7d3372325a182eaa61f6032efe231857c870c8cb64700cb47d4bf`. Both
approvals remain evidence only for their respective snapshots. Neither
approves this reassessment or the slice plan, publishes a contract, or claims
whole-v1 conformance.

Current approval: explicitly approved in this session on 2026-10-14 for the
I-0008-015 implementation-readiness scope and exclusions above. Approval
applies only to this readiness snapshot; it does not approve the separate
slice plan or execute the slice.

Approved material SHA-256: `fbc321553f64dfb0746fd9d77ba56fa1fc4a5a090446ac80c0fc4c9db5aeb0a2` (`work/0008/readiness/portable-binding-specification-audit-implementation.md`).
