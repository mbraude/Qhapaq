---
id: D-0007-012
kind: decision
title: Generator and runtime reuse boundaries
status: complete
spec: SPEC-0007
requirements: [R-0007-346, R-0007-259, R-0007-260, R-0007-348, R-0008-019, R-0006-020, R-0006-021, R-0006-024, R-0006-039, R-0006-041]
depends_on: [D-0007-011, D-0008-010]
artifacts:
  - specs/0006-dotnet-layered-architecture.md
  - docs/architecture/diagrams/dotnet-layered-components.mmd
  - docs/development/conventions/dotnet.md
---

# D-0007-012: Generator and Runtime Reuse

## Objective

Decide how build-time tooling shares portable algorithms with runtime consumers.

## Scope and exclusions

Required project/package/dependency boundaries; no runtime hosting dependency
inside generator validation, operation construction, network use, or layer bypass.
R-0006-039 and D-0007-011 assign logical semantic ownership but do not decide
the shared-library boundary owned by this item. R-0008-019 fixes workspace
ownership but does not decide that shared-library boundary.

## Questions to resolve

How do tooling and runtime reuse the owned algorithms? Does this require a
new reviewed assembly/package boundary, and how is it enforced?

## Acceptance criteria

- [x] Tooling/runtime dependency map is persistent and compatible with SPEC-0006.
- [x] Any necessary boundary change is decided before code implementation.
- [x] Offline, non-executing generation and runtime validation share semantics.
- [x] Architecture-test requirements and validation evidence are recorded;
      exact-snapshot human review remains a separate lifecycle gate.

## Resolution

The user selected a narrowly scoped shared library assembly containing the
single implementation of the portable algorithms in
[SPEC-0006 R-0006-041](../../../specs/0006-dotnet-layered-architecture.md#53-portable-helper-semantic-ownership).
The project, assembly, and root namespace are named
`Qhapaq.Portable.Validation` at
`implementations/dotnet/src/Qhapaq.Portable.Validation/`.
Its assembly and project maps are recorded under
[R-0006-021](../../../specs/0006-dotnet-layered-architecture.md#7-assemblies-and-distribution-packages)
and
[R-0006-024](../../../specs/0006-dotnet-layered-architecture.md#8-initial-net-project-and-file-plan).
Business references it for runtime behavior and remains the logical semantic
owner under
[R-0006-039](../../../specs/0006-dotnet-layered-architecture.md#53-portable-helper-semantic-ownership).
The Roslyn generator consumes the same implementation as build-time tooling.
The shared assembly is bundled in the `Qhapaq` runtime distribution and as a
private build-time asset of the generator package, without a separate public
package.
The shared assembly has no dependency on Business, DAL, Service, Entry Points,
the generator, runtime hosting, or project code. Reviewed low-level
dependencies are permitted when required and must preserve deterministic,
offline behavior and the non-executing boundary.

The shared assembly may be in an application's runtime dependency closure
through Business. The generator and dependencies used only by it remain
build-time-only and must not add runtime assets to consuming applications.
Architecture and clean package-consumer tests enforce dependency direction
and that separation. Exact package/API identities and low-level dependency
selections remain for concrete implementation planning; no production
assembly, package, or test is created by this decision.

The user selected this over a direct generator-to-Business dependency, which
would couple compiler tooling to runtime implementation dependencies, and
over linked-source compilation, which would produce separately compiled
copies that could diverge. The dedicated library keeps a single implementation
while leaving exact package identities for later slice planning.

## Validation and review

The decision is ready for exact-snapshot human review. Approval remains absent;
no implementation, publication, or readiness approval is inferred.

- Source reconciliation: SPEC-0007's 16 recorded input snapshots and
  SPEC-0008's 17 recorded input snapshots match exact current bytes; all
  recorded baseline revisions resolve. Both plans now record current
  SPEC-0006 and .NET-convention hashes.
- Workflow structure: 75 concrete work items and 208 dependency edges have no
  duplicate IDs, missing or cancelled prerequisites, or cycles. Local links in
  changed Markdown files resolve.
- Requirement integrity: SPEC-0006 retains 41 unique identifiers; R-0006-041
  is the next unused identifier. R-0006-021 and R-0006-024 were intentionally
  amended; all other existing requirement fingerprints match HEAD. Old
  fingerprints have no remaining references.
- Specification trace check ran without a semantic-review skip and returned
  `PASS with warnings`. It classifies this mixed requirement addition and
  requirement amendments as `requirement`, reviews R-0006-020, R-0006-021,
  R-0006-024, R-0006-039, R-0006-041, R-0007-348, and R-0008-019, and finds
  no errors, stale references, code/test changes, or waivers. Warnings cover
  mixed change kinds, intentionally .NET-specific project/assembly/package
  details, and architecture/package-consumer tests deferred to implementation.
- Markdown links resolve and `git diff --check` reports no whitespace errors.
  Git reports a line-ending normalization warning for the refreshed
  D-0007-008 evidence only. No build or unit tests were run because this
  decision changes specifications, architecture and planning documentation,
  and explicitly defers implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `07c75fefc458d942c87601636cd0d2b24d43806325b497ea6558050bfd617acb` |
| `specs/0006-dotnet-layered-architecture.md` | SHA-256 `052fad91fa6781e84fe6d3c93491c067f7e35dd0c4e807d2ca472e1fffc08e6e` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `e212841e5af69e06dba739222f0696f793436e391e7dbf66c0e047d8596a2e12` |
| `docs/development/conventions/dotnet.md` | SHA-256 `e3f7da320fba86a5ec2217607bbb35175fb905bfc91ee5e005a87a0d5d009d9f` |
| `docs/architecture/diagrams/dotnet-layered-components.mmd` | SHA-256 `cb9c16d8d1799c8e226242c6de6316f6abee32f62ff2f815510dc631e89ea731` |
| `work/0007/decisions/D-0007-008-folder-namespace-conventions.md` | SHA-256 `84ca69484e5da7d4a6dfe214b92c6425bb835673b47bacc91b3fed6785eaa047` |
| `work/0007/decisions/D-0007-011-portable-helper-ownership.md` | SHA-256 `92835fb032bbf2a8dc71ddf958eb3534901c15476051abe96081646debc57732` |
| `work/0008/decisions/D-0008-010-artifact-ownership-boundaries.md` | SHA-256 `7fc79f6b2fbd01841ad152c9e3bf9dc9d4cb08d150ca748ae36d10ff8c7c110c` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | SHA-256 `621c3a1edda62e952b8c812bc02a128cf752c55eb3d5ab6752de7e3c57861423` |
| `work/0007/implementation/I-0007-007-portable-validation-foundations.md` | SHA-256 `e6e281b7ffd5c551829423a51692b0389264ea592d8fbf55df39d4ba76f90ea4` |
| `work/0007/implementation/I-0007-008-descriptor-generation.md` | SHA-256 `ec4ca2d96350c23c5303309383e70f730c03ed9a48106042b7e2ea533dc8d5ee` |
| `work/0007/plan.md` | SHA-256 `49e32be20a9c9a2f482094d1e8da829ee5d02b2be591c72fc73c383d44b2fd75` |
| `work/0008/decisions/D-0008-009-dotnet-adapter-terminology.md` | SHA-256 `770a1134b3e632dfbdd1b92ec9d10e502afbaed188793eaf361d3eb769730c42` |
| `work/0008/plan.md` | SHA-256 `0e83a378bb760445bbd6442deac77024aa8e12d53ead1926669b0b03ef67767f` |

Historical approved trailer evidence (recorded 2026-10-11):

```text
Change-Kind: requirement
References at approval: R-0006-021 (fingerprint d969c8), R-0006-024
(fingerprint c4e735), R-0006-041 (fingerprint 2c2d4a)
```

Approval recorded on 2026-10-11: the user explicitly approved this exact
snapshot in this session.

Approved scope: the shared `Qhapaq.Portable.Validation` assembly and its
runtime/build-time dependency boundaries, distribution placement, permitted
low-level dependencies, and architecture/package-consumer enforcement
expectations, as recorded above and in R-0006-021, R-0006-024, and R-0006-041.
Exclusions: exact package/API identities and low-level dependency selections,
production implementation and tests, readiness approval, Git delivery, and
component contract publication.

The approved material SHA-256 is
`07c75fefc458d942c87601636cd0d2b24d43806325b497ea6558050bfd617acb`. The
approved full-byte input/output hashes are the exact values in the snapshot
table above. Only status and this validation/review evidence changed after
approval.

Post-approval ownership correction (2026-10-11): SPEC-0006 R-0006-041's
original approved project path under `implementations/dotnet/` is superseded
by the separately reviewed common-library ownership amendment in
[D-0008-015](../../0008/decisions/D-0008-015-common-library-workspaces.md).
The current project location is
`src/common/dotnet/src/Qhapaq.Portable.Validation/`, with tests under
`src/common/dotnet/tests/`. This correction changes repository ownership and
paths only; D-0007-012's approved algorithm-sharing, dependency, and
distribution decisions remain in force. The historical approval and its
exact-snapshot evidence above remain unchanged and do not approve the amended
location.
