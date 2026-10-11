---
id: D-0008-010
kind: decision
title: Assign generator and integration ownership boundaries
status: complete
spec: SPEC-0008
requirements: [R-0008-003, R-0008-019]
depends_on: [D-0008-001]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-010: Assign Generator and Integration Ownership Boundaries

## Objective

Apply the adopted public dependency boundary to decide concrete ownership for
the Roslyn generator, future product integrations, contributor tools, and
runtime workspaces.

## Scope and exclusions

R-0008-003 already prohibits private cross-workspace dependencies. Language
alone does not determine artifact ownership, and this item does not create a
new integration or generator API.

## Questions to resolve

Classify coupled and independently distributed tooling; define supported
contracts, private-output prohibitions, workspace ownership, packaging, and
cross-artifact dependency direction.

## Acceptance criteria

- [x] Ownership follows responsibility and supported contracts rather than source language.
- [x] Integrations cannot depend on private workspace outputs.
- [x] Build tools do not become runtime dependencies accidentally.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-019](../../../specs/0008-multi-language-conformance-and-repository-organization.md#concrete-artifact-ownership)
  assigns the Roslyn generator to the .NET implementation workspace as an
  independently versioned and packaged build-time artifact. Generator
  consumption must not add generator or private tooling dependencies to a
  runtime application's dependency closure.
- Product integrations remain independent workspaces beneath
  `src/integrations/` regardless of implementation language. Maintained
  contributor, validation, and build utilities with independent lifecycles
  remain workspaces beneath `src/tools/`; root `scripts/` and `build/` retain
  their automation and orchestration roles.
- Workspace interaction remains limited to portable root assets and documented
  public contracts, protocols, packages, or release artifacts. Private source
  and build outputs do not cross workspace boundaries.
- The exact generator package, shared validation assembly, and algorithm-reuse
  boundaries remain excluded and unresolved by
  [SPEC-0007 D-0007-012](../../../work/0007/decisions/D-0007-012-generator-runtime-reuse.md).

## Validation and review

Validated 2026-10-10:

- Confirmed 734 unique normative requirement IDs, 71 unique work-item IDs,
  resolvable requirement and dependency references, and an acyclic cross-plan
  dependency graph.
- Confirmed every relative link in changed Markdown resolves, both affected
  plans record the exact SPEC-0008 source bytes, and `git diff --check` passes.
  Git reported only the repository's existing line-ending normalization
  warnings.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `requirement`, derived `R-0008-019@571f96`, and confirmed that no existing
  requirement fingerprint or code/test reference became stale. The warning
  identifies the .NET, Roslyn, package, and workspace identities necessarily
  named by this repository-organization requirement.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and explicitly defers
  implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `433b67c0cb12370756258192e57f5e42298eb7f8879160966cc3d52734f4cbbc` |
| `work/0008/decisions/D-0008-010-artifact-ownership-boundaries.md` | Material SHA-256 `2ae33c77ef60e1ac98d71699fe058777f2de0a449837c1727b5afcce0e8f0332` |
| `work/0008/decisions/D-0008-011-build-ci-release-orchestration.md` | SHA-256 `30daf4f242e8847a33bf095faad2f6cbee025daf31e634c6f8ab5a10a9293a0d` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | SHA-256 `9d8d2a67a7e6424eaa22ae8d5399e524bd1ba5ee91e7b552ffae2be870c5f826` |
| `work/0008/implementation/I-0008-004-source-relocation.md` | SHA-256 `4eb0aa14addda1ed2f98b3f94adde65ba86de5ea2f6a9dd7465e3f96baf81329` |
| `work/0008/implementation/I-0008-005-dependent-surface-updates.md` | SHA-256 `7275514b405a75694faf6f53ddab06fdbd421065b1e9432d73c66a05c0e05fa8` |
| `work/0008/implementation/I-0008-006-future-workspaces.md` | SHA-256 `4088675c805e8d4f4f10ab410fd45826d9a89052639778c428a27c5681ec799d` |
| `work/0008/plan.md` | SHA-256 `b9b9d152be0fa81df8c31810e44e50e64c61ebeb8d47621d79324abbb20a4545` |
| `work/0007/decisions/D-0007-012-generator-runtime-reuse.md` | SHA-256 `067a691df6274ce47f92221275fcefff0d5f64124ff952f102c335aaadf75f71` |
| `work/0007/implementation/I-0007-008-descriptor-generation.md` | SHA-256 `0b6c3d202e11433d7b267d222ff525cf2a37db1020c7ad32cc70b49e9f8d6537` |
| `work/0007/plan.md` | SHA-256 `40185bf85debaf0515e0c6b05cbfa0186573cd4290ea8c19533445a83eb3e27f` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is responsibility-based ownership for the Roslyn
generator, product integrations, maintained contributor tools, and runtime
workspace dependency direction as defined by R-0008-019. Generator API and
shared-library design, integration-platform selection, workspace creation or
relocation, implementation, packaging execution, pushing, and component
contract publication remain excluded.
