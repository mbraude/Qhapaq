---
id: D-0007-010
kind: decision
title: Representative node and expression type relationships
status: complete
spec: SPEC-0007
requirements: [R-0007-346, R-0006-026, R-0006-040]
depends_on: [D-0007-009]
artifacts: [specs/0006-dotnet-layered-architecture.md]
---

# D-0007-010: Type Relationships

## Objective

Record representative composition and shared abstractions for nodes/expressions.

## Scope and exclusions

Relationships justified by governing behavior and the ownership map. No empty
type hierarchy or exhaustive prediction of future class names.

## Questions to resolve

Where do composition, discriminated representations, or a shared abstraction
actually preserve semantics? How are inert definitions distinct from bound plans?

## Acceptance criteria

- [x] Representative relationships and rationale are persistent.
- [x] Ownership and visibility match D-0007-009.
- [x] No speculative production scaffolding is required for decision closure.
- [x] Architecture-test implications and required checks are recorded; the
      exact-snapshot human review remains a separate lifecycle gate.

## Resolution

The user selected separate, closed internal variant families for pipeline nodes
and mapping expressions, with a shared root within a family only where variants
share a semantic invariant or operation required by consumers. Recursive
structure uses composition. Inert syntax remains separate from bound-plan and
compiled execution state. The conceptual relationship is recorded in
[SPEC-0006 R-0006-040](../../../specs/0006-dotnet-layered-architecture.md#54-representative-type-relationships),
consistent with [R-0007-346](../../../specs/0007-portable-pipeline-definitions-and-binding.md#net-organization-and-portable-validation)
and [R-0006-026](../../../specs/0006-dotnet-layered-architecture.md#9-initial-components).
Exact CLR names, file organization, public syntax trees, and speculative
production scaffolding remain excluded. Composition-only types without shared
roots were not selected because a root remains useful where variants genuinely
share semantics; a broad base spanning syntax and bound plans was rejected
because those are separate lifecycle representations.

## Validation and review

Validation performed 2026-10-11:

- Acceptance review: R-0007-346, R-0006-026, and R-0006-040 are covered.
  The accepted node/expression relationship and its alternatives are recorded
  in SPEC-0006; ownership remains in Business and private, consistent with
  D-0007-009. Exact implementation type names and production scaffolding are
  excluded.
- Plan reconciliation: all 16 SPEC-0007 source hashes match current bytes and
  their committed baseline revisions resolve. All 75 SPEC-0007/SPEC-0008
  item IDs are unique, dependencies resolve, and the combined graph is
  acyclic. D-0007-010 and I-0007-001 are the only affected work items; no
  readiness record, dependency edge, or implementation approval is changed.
- Requirement structure: R-0006-040 is the next unused ID and fingerprints
  to `fca8f1`. All 39 prior SPEC-0006 requirement fingerprints match HEAD;
  no existing reference became stale and no prior reference to R-0006-040
  existed.
- Specification trace check: PASS with a warning for implementation-specific
  .NET layer terminology in SPEC-0006. The changed files are one specification
  and three work-planning records. The change kind is `requirement`; no
  product code, tests, or waivers changed. Reverse-impact review confirms the
  new architecture rule agrees with R-0007-346, R-0006-026, and the existing
  R-0006-035 through R-0006-039 ownership and boundary requirements.
- Documentation and whitespace: all three local Markdown links in the
  changed work items resolve; `git diff --check` reports no whitespace
  errors. Git reports the existing CRLF-to-LF normalization warning for this
  decision file.
- No build or unit tests apply: the change adds a specification requirement
  and updates work-planning artifacts only.

Proposed commit trailers:

```text
Change-Kind: requirement
Spec: R-0006-040@fca8f1
```

Exact ready-for-review snapshot. Full-byte hashes cover the reviewed
working-copy inputs and outputs. The decision material hash normalizes
line endings and excludes only the status line and this validation/review
section, as defined by the workflow.

| Material input/output | SHA-256 |
| --- | --- |
| This decision's material content | `dc5e46e698f9ca92de27d9d6ef4dcb52bfb6bd89ac1646658fb1fadb0b8a32aa` |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `.github/instructions/specifications.instructions.md` | `7e90f2c5a32dfb947e25b86c7ab6b5be53d046d4704e3b4d71768077b9ea52e2` |
| `docs/development/conventions/specifications.md` | `9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a` |
| `docs/development/coding-conventions.md` | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/spec-driven-workflow.md` | `c1045d2891c7ccbe00c833e247d7254c7e4161857dfe6884b47a644cb3e1c11e` |
| `docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md` | `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| `docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md` | `439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825` |
| `specs/0001-core-pipeline-model.md` | `38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e` |
| `specs/0002-operation-catalogs-and-host-configuration.md` | `c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca` |
| `specs/0005-build-release-and-website-delivery.md` | `8259be3d7e256d77ab18e96c35906ce64c01d25eb7a22f45a911c0727d1a1679` |
| `specs/0006-dotnet-layered-architecture.md` | `e2ecf39f0c7dd282cdd5a04b9d292c803531e86c76497fc66b068472a9bd6456` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `e212841e5af69e06dba739222f0696f793436e391e7dbf66c0e047d8596a2e12` |
| `schemas/README.md` | `9735bf13164fda904d9d926a1ef896038360c7334e8ad831cac195dfc59ab0a1` |
| `conformance/README.md` | `0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307` |
| `docs/development/conventions/dotnet.md` | `72ac12a7ae56110729d011ecffe0c551961811dde30462ab2568647ccd6702f1` |
| `docs/development/conventions/schemas.md` | `efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2` |
| `implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/LayerDependencyTests.cs` | `62eafc81acf00d7bf15390aa110119e0be3d6e4a7cf0988193e9bb664e40eb4a` |
| `work/0007/decisions/D-0007-009-model-ownership.md` | `b18191e694df1d479ab827b192782ffc6271b780ccb06967e3a5b23bd4ac7565` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | `cb41307519ac4682ef6c1418b4fddcb8f9b242b640cae752aa0fbf4d5aa05690` |
| `work/0007/plan.md` | `53a601107ebd1e4027356241401983d590a185a1dde3b970f7a59b5ebfe60c9c` |

Approval recorded on 2026-10-11: the user explicitly approved this exact
snapshot in this session.

Approved scope: D-0007-010's representative node and expression type
relationships, SPEC-0006 R-0006-040, and the bounded SPEC-0007 plan
reconciliation recorded above. Exclusions remain exact CLR names and file
organization, production implementation, architecture tests, readiness or
implementation approval, and component-contract publication.

Approved material SHA-256:
`dc5e46e698f9ca92de27d9d6ef4dcb52bfb6bd89ac1646658fb1fadb0b8a32aa`.
The decision's full-byte SHA-256 immediately before recording this approval
was `573fb83dd63cb4bcfbb7eec7a41a5ad012a0601e15501fdffd14fe331b7a973a`.
The exact input/output file-byte hashes approved are the values in the
ready-for-review snapshot table above; only this status and approval evidence
changed.

No readiness, implementation authority, or component-contract publication is
inferred.
