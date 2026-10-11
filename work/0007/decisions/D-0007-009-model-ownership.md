---
id: D-0007-009
kind: decision
title: Model ownership and visibility map
status: complete
spec: SPEC-0007
requirements: [R-0007-346, R-0006-010, R-0006-011, R-0006-012, R-0006-014, R-0006-035, R-0006-036, R-0006-037, R-0006-038]
depends_on: []
artifacts: [specs/0006-dotnet-layered-architecture.md]
---

# D-0007-009: Model Ownership

## Objective

Assign ownership and visibility for the first definition-to-execution models.

## Scope and exclusions

Definition, schema, expression, descriptor, bound-plan, failure, and
Service-boundary models. Distinguish private representations, internal
cross-layer contracts, and supported public APIs. No speculative class catalogue.

## Questions to resolve

Which layer owns each responsibility? Which values actually cross adjacent
boundaries, and which public authoring/Service contracts are necessary?

## Acceptance criteria

- [x] Persistent ownership/dependency map covers each listed model family.
- [x] Public/internal/private boundaries preserve SPEC-0006's call graph.
- [x] Representatives support the first retrieval, generator, and parsing slices.
- [x] No architectural exception is introduced; any future exception requires
  its own accepted authoritative decision.
- [x] Checks pass and the exact input/output ownership snapshot is recorded
  for explicit human review.

## Resolution

The user selected the boundary-first map in SPEC-0006 on 2026-10-11.
Recorded in [SPEC-0006 Sections 5.1 and 5.2](../../../specs/0006-dotnet-layered-architecture.md#51-definition-to-execution-model-ownership):

- R-0006-035 covers all seven model families and their ownership/exposure.
- R-0006-036 defines internal adjacent-port placement, supported public nested
  values, projection boundaries, and separation of failure/frame representations.
- R-0006-037 records retrieval, inert-parsing, and generator model flows without
  selecting a shared algorithm/library boundary.
- R-0006-038 records architecture, package-consumer, and slice-test obligations.

No public definition/expression/bound-plan object model, new assembly/package,
layer exception, production type, schema, vector, or generated output is added.
[D-0007-010](D-0007-010-type-relationships.md) still owns representative type
relationships, [D-0007-011](D-0007-011-portable-helper-ownership.md) owns shared
algorithm placement, and [D-0007-012](D-0007-012-generator-runtime-reuse.md)
owns tooling/runtime dependency choices. No future slice is authorized.

## Validation and review

Decision input: on 2026-10-11 the user explicitly selected the boundary-first
ownership map in SPEC-0006, with no new assembly or public
definition/expression/bound-plan object model. This selection is not final
approval of the resulting material snapshot.

Validation performed on 2026-10-11:

- Ownership/semantic review: PASS. All seven families have persistent owners,
  supported exposure, and adjacent-port rules. Retrieval, parsing, and generator
  flows agree with SPEC-0007's exact-version, non-executing, stage-aware,
  disclosure, failure, and static declaration requirements. Existing
  SPEC-0006 visibility, call graph, and composition rules are preserved.
- Source and workflow checks: PASS. All 16 SPEC-0007 source hashes match
  exact current bytes. All 74 SPEC-0007/SPEC-0008 identities, ownership,
  required item sections, and plan memberships pass; 199 dependency edges
  resolve, with no cycle or cancelled prerequisite. No dependency changed.
- Specification structure/fingerprints: PASS. R-0006-035 through R-0006-038
  are the next four unused identifiers; all 34 original block fingerprints
  remain unchanged. No existing requirement or published contract was modified.
- Specification trace check: PASS with warnings. Change kind is `requirement`.
  Semantic/reverse-impact review covers R-0006-003 through R-0006-016,
  R-0006-020, R-0006-025 through R-0006-027, R-0006-030 through R-0006-032,
  the four new ownership requirements, and SPEC-0007's inert lifecycle,
  private frames, missing/null distinction, declarations/manifest verification,
  stage-aware conclusions, retrieval, and failure projections. No product
  code, test code, stale reference, or waiver is added. The expected warning
  is .NET-specific implementation/namespace naming in this architecture spec.
- Documentation/diagnostics: PASS. Checked 101 local Markdown file targets;
  `git diff --check` reports no whitespace errors. VS Code reports no
  diagnostics for the changed specification and related plan checked.
- No build or unit tests were run: only specifications and work documentation
  change. R-0006-038's real architecture, consumer, and behavioral tests remain
  implementation obligations, not claimed results of this decision.

Remaining gates: exact human review of D-0007-009; D-0007-010/011/012 and the
other Phase 0A decisions; real enforcing tests in I-0007-001; scoped readiness
and concrete slice-plan approval. SPEC-0008's unrelated source-byte drift
remains explicitly outside this bounded reconciliation.

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0006-035@76072a, R-0006-036@8476ab, R-0006-037@d8f638, R-0006-038@6c8271
```

### Exact ready-for-review snapshot

Baseline: `637015dc481f2d1e5b764b0deaad38828f2cc35e`. Full-byte hashes below
cover the reviewed working copies, not a claim that they are already committed.
The item material hash normalizes line endings to LF and excludes only its
status line and validation/review evidence as defined by the workflow.

| Material input/output | SHA-256 |
| --- | --- |
| This decision's material content | `b99e604783d8797828f2ce69a9fcf4fb1e19530149b8d35973231d7bbff54803` |
| `specs/0006-dotnet-layered-architecture.md` | `8bdfab494c48cbdddfcb458bea9e71bc63dc6fc0709bbaf63325e58fb600ae10` |
| `work/0007/plan.md` | `fcfb9ade86f4d385a0bd9826ed92030ba44a57d6baf5c1cdcbca9e7d71990d94` |
| `work/0008/plan.md` | `b5cfeb547e04ddc50c3ed6a181ab39d26a61a8f1067fee7e51d3eb5b1c0a2b4a` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | `d7e8c5057e28e2788bb32fc7be087db640444aece6920b7f7d6f912df0656316` |
| `work/0007/implementation/I-0007-008-descriptor-generation.md` | `e2160492bac9f649d6d333d8a5f8cb251087f973311d5d434f6b7501b1bed271` |
| `work/0007/implementation/I-0007-011-first-service-cli-slice.md` | `f04981abd2211e5b962c042fa0f55f1268cb0bdb29879eb4ccd0697529a0bab9` |
| `work/0007/implementation/I-0007-012-inert-parsing.md` | `47d5604cb71c4f7fec7ad9ded29ea834627666ed2f6b8ab2dec8893d69ee0863` |
| `SPEC.md` | `cbb6cec07dff90ff9c8eef54b5cd3ae2c97da5d17ecd452f7e677664be99aa3d` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `docs/development/coding-conventions.md` | `0d4a23e0cf96ef3d3ab9e575ad7b65899403989d95317d5339434a7717270fa6` |
| `docs/development/spec-driven-workflow.md` | `55c10d072e97d305ced1591c365ef65e61e5564df3f3d29e6e9d84a99ef7b127` |

Approval recorded on 2026-10-11: the user explicitly approved the exact snapshot
above in this session after revalidation, and selected local commit followed by
push through the outer approve-commit-push workflow.

Approved scope: D-0007-009's seven-family ownership/visibility outcome and
representative retrieval, parsing, and generator flows, plus the bounded
SPEC-0007/SPEC-0008 plan and four implementation-milestone reconciliations.
The unchanged material SHA-256 is
`b99e604783d8797828f2ce69a9fcf4fb1e19530149b8d35973231d7bbff54803`;
the eleven full-byte input/output hashes in the snapshot table are the exact
approved values. Only this item's lifecycle and review evidence are updated
after approval; every other reviewed file remains byte-identical.

Approval-time validation: exact material/input/output hashes, current SPEC-0007
source records, acceptance criteria, prerequisites, acyclic cross-plan graph,
local Markdown targets, and whitespace checks pass. Specification trace check
passes with the expected .NET-specific naming warning; all 34 original
fingerprints remain unchanged, and no code/test reference or new waiver exists.
No build or unit tests were run for this specification/documentation-only scope.

Exclusions: production/test code, new assemblies/packages, public syntax/plan
models, other organization decisions, readiness or executable slice approval,
generated artifacts, and contract publication. Completion of this decision
does not complete Phase 0A or authorize future implementation.
