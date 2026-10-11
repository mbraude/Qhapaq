---
id: D-0007-011
kind: decision
title: Shared portable algorithm ownership
status: complete
spec: SPEC-0007
requirements: [R-0007-346, R-0007-348, R-0006-020, R-0006-039]
depends_on: [D-0007-009]
artifacts: [specs/0006-dotnet-layered-architecture.md]
---

# D-0007-011: Portable Helper Ownership

## Objective

Assign shared responsibilities before generator and runtime implementations diverge.

## Scope and exclusions

Canonicalization, digest computation, schema/descriptor/vocabulary validation,
and diagnostic construction. Reuse must not bypass layer boundaries.

## Questions to resolve

Which layer or reviewed tooling boundary owns each algorithm? Which consumers
reuse it, and how are build diagnostics distinct from runtime diagnostics?

## Acceptance criteria

- [x] Persistent map assigns each helper family and its permitted consumers.
- [x] Adjacent-layer contracts and tooling boundaries remain explicit.
- [x] Determinism, offline behavior, and safe diagnostic envelopes are preserved.
- [x] Required architecture-check obligations and validation evidence are
      recorded; exact-snapshot approval remains a separate lifecycle gate.

## Resolution

The user selected Business as the logical owner of the shared portable
validation semantics. Runtime callers consume them through Business behavior
and adjacent-layer contracts; DAL remains the metadata/storage provider.
Build-time tooling reuses the same semantics through an explicit, reviewed
dependency boundary without a parallel implementation. Portable findings
remain payload-safe and distinct build and runtime diagnostic envelopes are
preserved. The physical dependency boundary remains for
[D-0007-012](D-0007-012-generator-runtime-reuse.md); no project, assembly,
package, or production helper file is selected here.

## Validation and review

Alternative independent shared-core ownership was not selected because the
logical semantic owner can remain Business while physical reuse is decided
separately. DAL ownership was not selected because registry/storage duties do
not supply the context for domain validation; duplicate generator/runtime
implementations were rejected because they could diverge from the portable
semantics.

Validation performed 2026-10-11:

- Ownership and semantics: PASS. SPEC-0006 R-0006-039 assigns logical
  ownership of portable helper semantics and permitted runtime/build consumers
  to Business while preserving SPEC-0007 R-0007-348, R-0007-346, and
  R-0006-020. Portable findings remain payload-safe and build/runtime
  diagnostic envelopes remain distinct. No physical project/package boundary,
  production helper, schema, or vector was selected.
- Plan reconciliation: PASS. All 16 SPEC-0007 source hashes match exact current
  working-copy bytes. The 74 work-item identities and 199 dependency edges are
  unchanged; no dependency field, cycle, cancelled prerequisite, or cross-plan
  edge changed. Only D-0007-011, D-0007-012, and directly affected
  architecture/validation/generator/registry/parsing/schema/normalization
  milestones were reconciled. Unrelated SPEC-0008 source drift remains out of
  scope.
- Requirement structure and fingerprints: PASS. R-0006-039 is the next unused
  identifier; all 38 prior SPEC-0006 requirement fingerprints are unchanged.
  Its fingerprint is `27b828`, and no prior inline reference exists.
- Specification trace check: PASS with a warning for implementation-specific
  .NET and layer terminology in SPEC-0006. Change kind is `requirement`;
  proposed trailers are `Change-Kind: requirement` and
  `Spec: R-0006-039@27b828`. No prior SPEC-0006 reference is stale, and no
  code, test, or waiver changed.
- Documentation: PASS. The D-0007-012 link resolves and `git diff --check`
  passes; Git reports only line-ending normalization warnings. No build or
  unit tests apply to this specification and work-planning change.

Exact ready-for-review snapshot. Hashes cover the reviewed working copies; the
decision's material hash normalizes line endings and excludes its status and
validation/review sections:

| Material input/output | SHA-256 |
| --- | --- |
| This decision's material content | `992a5ade5ee57510fc7da146022bb4ee10d6d553582dafd2736e78730c99a5b3` |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `.github/instructions/specifications.instructions.md` | `7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2` |
| `docs/architecture/decisions/0003-enforce-specification-traceability.md` | `da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411` |
| `docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md` | `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| `docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md` | `439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825` |
| `specs/0006-dotnet-layered-architecture.md` | `c044679c4ca4255c75c835cadee8a194685a1206d11ff1aace8167d01db0a65d` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `e212841e5af69e06dba739222f0696f793436e391e7dbf66c0e047d8596a2e12` |
| `work/0007/plan.md` | `8ff5abb11584a23ffcf8a3d1ddb9ba95af9ce1dfd3bd275b736ec7214c896b16` |
| `work/0007/decisions/D-0007-009-model-ownership.md` | `b18191e694df1d479ab827b192782ffc6271b780ccb06967e3a5b23bd4ac7565` |
| `work/0007/decisions/D-0007-012-generator-runtime-reuse.md` | `9e2253afaff6ef03e5e1bf6867868dfb1aa18edb77bde28b4fbaf8df45836673` |
| `work/0008/plan.md` | `b5cfeb547e04ddc50c3ed6a181ab39d26a61a8f1067fee7e51d3eb5b1c0a2b4a` |
| `work/0008/decisions/D-0008-010-artifact-ownership-boundaries.md` | `7fc79f6b2fbd01841ad152c9e3bf9dc9d4cb08d150ca748ae36d10ff8c7c110c` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | `0efb1cb3fc6b7d67d57cd505f37016305701283fe71289a185076e0293185421` |
| `work/0007/implementation/I-0007-007-portable-validation-foundations.md` | `b962585b194c5011b9a7732500fb337290b43582ba560564e1d28a6933cef2a4` |
| `work/0007/implementation/I-0007-008-descriptor-generation.md` | `e8bc945be18de7f18aa858f4602e7f3902a436ffcdfcde1314707cbe83e62c9f` |
| `work/0007/implementation/I-0007-009-registry-native-bindings.md` | `f089eef28d345da98c75d88a704990149729b92ba594b10d50baa39bd798858a` |
| `work/0007/implementation/I-0007-012-inert-parsing.md` | `eaac3e0b1d59f7e3e148db03d0718072e0e2f15ca9f23663c529580b9cd3e17f` |
| `work/0007/implementation/I-0007-013-schema-engine.md` | `a7f99d1ab2b674ffb0b8233c54ecb6652d5992296b3d409dcd5d02728cabeefe` |
| `work/0007/implementation/I-0007-016-normalization-identity.md` | `7570875423f1aa2515feeb5e8c30ea8231ab1fd484fb2c9d0e4488f0dfbf2bdd` |
| `docs/development/coding-conventions.md` | `0d4a23e0cf96ef3d3ab9e575ad7b65899403989d95317d5339434a7717270fa6` |
| `docs/development/spec-driven-workflow.md` | `55c10d072e97d305ced1591c365ef65e61e5564df3f3d29e6e9d84a99ef7b127` |

This review gate concerns only D-0007-011's logical ownership map; D-0007-012,
implementation, physical dependency selection, readiness, and delivery remain
separate gates.

Approval recorded on 2026-10-11: the user explicitly approved this exact
snapshot in this session and requested local commit followed by push.

Approved scope: D-0007-011's logical portable-helper ownership map, its
SPEC-0006 requirement, and the bounded SPEC-0007 plan reconciliation listed
above. Exclusions remain D-0007-012's physical boundary decision,
implementation/readiness approval, production code, schemas/vectors, and
contract publication.

The approved material SHA-256 remains
`992a5ade5ee57510fc7da146022bb4ee10d6d553582dafd2736e78730c99a5b3`.
All 22 full-byte input/output hashes in the exact-snapshot table above are the
approved values. Only this decision's lifecycle and review-evidence section
changed after approval.
