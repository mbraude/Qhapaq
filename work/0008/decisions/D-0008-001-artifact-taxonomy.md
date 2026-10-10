---
id: D-0008-001
kind: decision
title: Adopt artifact taxonomy and source layout
status: complete
spec: SPEC-0008
requirements:
  - R-0000-009
  - R-0000-017
  - R-0000-019
  - R-0000-020
  - R-0000-031
  - R-0008-001
  - R-0008-002
  - R-0008-003
depends_on: []
artifacts:
  - SPEC.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-001: Adopt Artifact Taxonomy and Source Layout

## Objective

Decide the responsibility-based artifact taxonomy, top-level source layout,
workspace boundaries, and explicit exceptions for examples, scripts, tools,
portable assets, and generated output.

## Scope and exclusions

R-0000-009 currently owns the location of additional implementations. This item
does not move files, create directories, select another runtime, or rename
assemblies.

## Questions to resolve

Compare the proposed `src/` taxonomy with retained alternatives; define what
counts as maintained software; decide nesting and workspace rules; and identify
every required amendment to existing path obligations.

## Acceptance criteria

- [x] The adopted taxonomy and exceptions are normative and unambiguous.
- [x] R-0000-009 is preserved or amended explicitly.
- [x] Workspace, portable-asset, generated-output, and cross-artifact boundaries agree.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-001 through R-0008-003](../../../specs/0008-multi-language-conformance-and-repository-organization.md#4-artifact-taxonomy-and-source-layout)
  define the responsibility-based `src/` taxonomy, lifecycle-based root
  exceptions, self-contained workspaces, public cross-artifact boundaries, and
  generated-output rules.
- [SPEC.md R-0000-009, R-0000-017, R-0000-019, R-0000-020, and R-0000-031](../../../SPEC.md)
  align the repository target and path obligations with that taxonomy.
- Physical relocation, scaffolding, runtime selection, and identity changes
  remain excluded and require their separately reviewed downstream work.

## Validation and review

Validated 2026-10-10:

- Confirmed all 11 plan source hashes and committed baseline paths. The edited
  `SPEC.md` and SPEC-0008 records retain their committed baseline revisions and
  hash the reviewed working-copy bytes.
- Confirmed 718 unique normative requirement IDs, resolvable requirement
  references in every changed work item, 67 unique work-item IDs, resolvable
  dependencies, and an acyclic dependency graph.
- Confirmed every relative link in changed Markdown resolves, `git diff
  --check` passes, and no stale code or test fingerprint references exist for
  the amended requirement blocks.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `requirement`; the warnings identify the intentional combination of new
  SPEC-0008 requirements with necessary SPEC.md amendments and the
  language/path examples inherent in a repository-organization requirement.
  No product or test code changed.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `SPEC.md` | SHA-256 `9f49ea636b86865933bdd4b175ca90287e470625d4be5e8db79751475817ca78` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `21c6c203c228218a67a076545513b31cc3d5a737e6d3078a935a620a5c50d8fa` |
| `work/0008/decisions/D-0008-001-artifact-taxonomy.md` | Material SHA-256 `e87d87b9f31578cbaa002d29a5451689ab6213d8b370a2c40082e5cf8ecb19b2` |
| `work/0008/decisions/D-0008-010-artifact-ownership-boundaries.md` | SHA-256 `d86ee9dd9c6359a8782ff15f170a74adab958b91500522efd8575ea5163c43d5` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | SHA-256 `55723c4f40c6358da1af47675ed9fa95044fda0d29de6889212799bb805d07f9` |
| `work/0008/implementation/I-0008-004-source-relocation.md` | SHA-256 `317c62e3b94ac68a3f2302b3ddbddb9181f9dc568eb142b951a3c2abc8f5dc99` |
| `work/0008/implementation/I-0008-005-dependent-surface-updates.md` | SHA-256 `66b2e3acb771207b543150ddaa01f864e827b47fb1291cc6cc583916b4e1ce22` |
| `work/0008/implementation/I-0008-006-future-workspaces.md` | SHA-256 `e99b55ede3c4e682ebf0751e4a2114afead9160bccbb68c552547abc83957a5b` |
| `work/0008/plan.md` | SHA-256 `f6e15d509be7a92bed8def160a5d44d3a1c35467aa3ed4963983bb49dd050718` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot above.
The approved scope is the responsibility-based artifact taxonomy and related
SPEC.md path obligations. Physical relocation, scaffolding, runtime selection,
assembly or package renames, and implementation remain excluded.
