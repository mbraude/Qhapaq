---
id: D-0008-009
kind: decision
title: Resolve .NET entry-point terminology and identity naming
status: complete
spec: SPEC-0008
requirements:
  - R-0006-001
  - R-0006-002
  - R-0006-009
  - R-0006-010
  - R-0006-014
  - R-0006-015
  - R-0006-017
  - R-0006-018
  - R-0006-020
  - R-0006-021
  - R-0006-023
  - R-0006-024
  - R-0006-026
  - R-0006-028
  - R-0006-030
  - R-0006-031
  - R-0006-032
  - R-0006-033
depends_on: []
artifacts:
  - specs/0006-dotnet-layered-architecture.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - docs/architecture/decisions/0001-use-microsoft-dependency-injection.md
  - docs/architecture/diagrams/dotnet-layered-components.mmd
  - docs/development/coding-conventions.md
---

# D-0008-009: Resolve .NET Entry-Point Terminology and Identity Naming

## Objective

Choose an unambiguous name for the .NET top layer and define the matched source
and compiled identities without conflating executable or package identities.

## Scope and exclusions

SPEC-0006 remains authoritative. Source relocation, layer terminology,
assembly identity, namespace identity, package identity, and public behavior
are separate concerns and must not be bundled implicitly.

## Questions to resolve

Choose layer terminology and a role-qualified identity; define compatibility
and migration effects; and identify required SPEC-0006 amendments and ADRs.

## Acceptance criteria

- [x] Layer terminology is unambiguous across language runtime and .NET architecture usage.
- [x] Assembly, namespace, package, and path decisions are separated explicitly.
- [x] Every affected SPEC-0006 requirement and architecture test is identified.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0006](../../../specs/0006-dotnet-layered-architecture.md) names the
  top .NET layer **Entry Points** and retains its transport and hosting adapter
  responsibilities plus adjacent-layer dependency direction.
- Production directories, project names, assembly names, root namespaces, and
  derived source namespaces use the matched
  `Qhapaq.EntryPoints.<EntryPoint>` identity. The initial identities are
  `Qhapaq.EntryPoints.Hosting`, `Qhapaq.EntryPoints.MCP`, and
  `Qhapaq.EntryPoints.CLI`.
- The `qhapaq` executable filename and the `Qhapaq.Hosting` and `Qhapaq.Mcp`
  package IDs remain separate distribution identities and are not renamed by
  this decision.
- The affected architecture enforcement surface is
  `implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/LayerDependencyTests.cs`
  plus its project references. I-0008-008 must update that test, each renamed
  production and test project, solution membership, project references,
  namespaces, documentation consumers, automation, and packaging inputs as one
  validated migration.
- No new ADR is required because SPEC-0006 is the .NET architecture authority
  and records the naming rationale and rejected alternatives. ADR-0001 is
  updated only to keep its accepted composition chain consistent.
- Source relocation, project and namespace migration, consumer updates, and
  compatibility recovery remain excluded implementation work owned by
  D-0008-012, I-0008-004, I-0008-005, and I-0008-008.

## Validation and review

Validated 2026-10-10:

- Confirmed all 12 plan source snapshots match exact current bytes, all 21
  SPEC-0008 work-item identities are unique, every one of the 51 direct
  dependency references resolves, and the dependency graph remains acyclic.
- Confirmed all relative links in the ten changed Markdown files resolve and
  `git diff --check` passes. Git reported only the repository's existing
  line-ending normalization warnings.
- Derived fingerprints for all 16 SPEC-0006 blocks at the original review
  snapshot:
  `R-0006-002@986093`, `R-0006-009@d7d6c5`, `R-0006-010@0bbcbc`,
  `R-0006-014@e5b3fd`, `R-0006-015@583f2e`, `R-0006-017@32c03d`,
  `R-0006-020@19dcc3`, `R-0006-021`, `R-0006-023@5c84f0`,
  `R-0006-024`, `R-0006-026@5c802d`, `R-0006-028@6edbcf`,
  `R-0006-030@e300b6`, `R-0006-031@3f2f97`, `R-0006-032@d0fa7c`, and
  `R-0006-033@80ef20`.
- Post-snapshot reference reconciliation (2026-10-11): D-0007-012 extended
  SPEC-0006 R-0006-021 and R-0006-024 to include `Qhapaq.Portable.Validation`.
  The exact 2026-10-10 approved snapshot remains historical and unchanged; the
  approved Entry Points terminology outcome is unaffected. Current
  fingerprints are `R-0006-021@d969c8` and `R-0006-024@c4e735`.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `amendment` and reviewed all 16 changed SPEC-0006 blocks. The warning records
  intentional .NET, project, assembly, namespace, executable, and package
  identities in the explicitly .NET-specific implementation specification.
  No product or test code changed.
- No build or unit tests were run because this decision changes only
  specification, architecture, policy, diagrams, and planning documentation
  and explicitly defers the implementation migration.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0006-dotnet-layered-architecture.md` | SHA-256 `62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `3efd22dbdfea9783141fda61e8625340ea67224663b07ca63c32fb86155dba02` |
| `docs/architecture/decisions/0001-use-microsoft-dependency-injection.md` | SHA-256 `f7855b81e87db15f89326d7a297cc983eb8ba1a4f250aed380a999e5f87de217` |
| `docs/architecture/diagrams/dotnet-layered-components.mmd` | SHA-256 `00dd9d7847b037a697c07a093b496ca43af1945a216b1151e9e79bccf033525d` |
| `docs/development/coding-conventions.md` | SHA-256 `8cd098f3f9bd877ef9f1c77a77c4b1a895b28ae92ace65299ff05daa4a859b05` |
| `work/0008/decisions/D-0008-009-dotnet-adapter-terminology.md` | Material SHA-256 `9a48f1e86b7d9ce876d1680b04185e8bdee446b88f5a2bf7e1263a60100567bc` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | SHA-256 `5e922a69c20330f397bd2ab2dd9d7543a8dd8dd709280d87b1b0b8c0df6067e0` |
| `work/0008/implementation/I-0008-005-dependent-surface-updates.md` | SHA-256 `ff674dd90303654b2437792a4811d3410aee058fa3d9e0a49e672578697c53b8` |
| `work/0008/implementation/I-0008-008-entry-point-identity-migration.md` | SHA-256 `d92a6945cf83a4b04a66abd63ef3b3aa2eea1200658925de8bd5dea69f10403e` |
| `work/0008/plan.md` | SHA-256 `47409d2aa2dffb12c27a95201cd4b458544cc6fe48ac941c5314631e38b2b3ef` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is the **Entry Points** layer name; matched
`Qhapaq.EntryPoints.*` directory, project, assembly, root-namespace, and
derived source-namespace identities; preserved executable and package
identities; the affected architecture and policy updates; and bounded
downstream migration planning. Project and source renames, source relocation,
implementation, build and test execution, pushing, and component contract
publication remain excluded.
