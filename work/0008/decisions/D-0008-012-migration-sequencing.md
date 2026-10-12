---
id: D-0008-012
kind: decision
title: Define migration sequencing, validation, and recovery
status: complete
spec: SPEC-0008
requirements:
  - R-0000-009
  - R-0005-030
  - R-0005-034
  - R-0005-035
  - R-0006-021
  - R-0006-023
  - R-0006-024
  - R-0006-030
  - R-0006-032
  - R-0008-001
  - R-0008-002
  - R-0008-003
  - R-0008-019
  - R-0008-020
  - R-0008-021
  - R-0008-022
  - R-0008-023
  - R-0008-024
  - R-0008-025
  - R-0008-026
  - R-0008-027
  - R-0008-028
  - R-0008-029
depends_on:
  - D-0008-001
  - D-0008-002
  - D-0008-003
  - D-0008-004
  - D-0008-005
  - D-0008-006
  - D-0008-007
  - D-0008-008
  - D-0008-009
  - D-0008-010
  - D-0008-011
  - D-0008-013
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-012: Define Migration Sequencing, Validation, and Recovery

## Objective

Define the coordinated migration order, prerequisite amendments and ADRs,
before-and-after validation, compatibility protection, and recovery steps.

## Scope and exclusions

This is a planning decision, not authorization to relocate files, rewrite
history, destructively reset worktrees, or combine independent renames.

## Questions to resolve

Sequence policy extraction, normative amendments, profile artifacts, the
Entry Point identity migration, source moves, consumer updates, release
changes, and future workspaces; define compatibility checks, recovery
checkpoints, and preservation of user changes.

## Acceptance criteria

- [x] Every migration step has prerequisites, observable validation, and recovery.
- [x] Public identity and behavior changes require separate approved amendments.
- [x] Instructions, tests, automation, documentation, and plans are included in impact review.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-027](../../../specs/0008-multi-language-conformance-and-repository-organization.md#10-migration-sequencing-validation-and-recovery)
  sequences prerequisite policy, audit, traceability, conformance, and
  orchestration work before migration; requires the Entry Point identity
  migration at existing paths before separate source relocation; and keeps
  public identity, compatibility, behavior, release, and publication changes
  behind their own governing requirements and approvals.
- [SPEC-0008 R-0008-028](../../../specs/0008-multi-language-conformance-and-repository-organization.md#10-migration-sequencing-validation-and-recovery)
  requires equivalent before-and-after checks, exact snapshots and evidence,
  full consumer impact review, observable compatibility comparison, and
  fail-closed treatment of missing or ambiguous validation.
- [SPEC-0008 R-0008-029](../../../specs/0008-multi-language-conformance-and-repository-organization.md#10-migration-sequencing-validation-and-recovery)
  requires a dedicated branch and exact recovery checkpoint, preserves
  user-owned tracked and untracked changes, and limits recovery to inverse
  slice-owned changes or dedicated commit reverts without history rewriting,
  destructive resets, or replacement of immutable published artifacts.

This decision records migration semantics only. It does not approve a concrete
slice, move or rename a file, change a public identity or behavior, assemble a
release, publish a profile or claim, or authorize implementation.

## Validation and review

Validated 2026-10-10:

- Confirmed 746 unique normative requirement IDs, 70 unique work-item IDs,
  resolvable changed-item requirement and dependency references, and an
  acyclic cross-plan dependency graph.
- Confirmed all 12 recorded SPEC-0008 source hashes match the exact current
  bytes, all relative links in the eight changed Markdown files resolve, and
  `git diff --check` passes. Git reported only the repository's existing
  line-ending normalization warnings.
- The specification trace review at that snapshot ran without a
  semantic-review skip and returned `PASS` with no errors, warnings, or
  waivers. It classified the change as `requirement` and recorded
  then-current fingerprint `4468fb` for R-0008-027, alongside R-0008-028 and
  R-0008-029. It confirmed that no requirement fingerprint or code/test
  reference was stale at that time.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and explicitly defers
  implementation.
- The authoritative input was committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` with SPEC-0008 SHA-256
  `5097e7f8921b5e865feccbb304f890840a9b929e33fc159d468c8b089212bdc1`;
  the output snapshot is recorded below.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | Material SHA-256 `fade58baef6fb5507699317d2fc662cb2f385702f438e2f0aad7c5e6cfd9f8e7` |
| `work/0008/implementation/I-0008-004-source-relocation.md` | SHA-256 `47bb09dc9ebd92a3f2d896aa9583a30c268d82543e5e12bab3986899d87963c2` |
| `work/0008/implementation/I-0008-005-dependent-surface-updates.md` | SHA-256 `295d0f8d26a57989ebd1861e41ef4978de88622311c580664290a2db5d04966f` |
| `work/0008/implementation/I-0008-006-future-workspaces.md` | SHA-256 `5f7ee5c654f328ed170e271e03f4a924e1e46775791263f1ff0afb1ea796cd0f` |
| `work/0008/implementation/I-0008-008-entry-point-identity-migration.md` | SHA-256 `7a89a29dbbaeee0b6128f5dd4b01935fcf988e182f13861de82d1ebdb58102a1` |
| `work/0008/implementation/I-0008-009-migration-validation-orchestration.md` | SHA-256 `33d7d097c91994cae8e3bad82e7f4dd7dd9e9225e07572d5838c1c3f242ac261` |
| `work/0008/plan.md` | SHA-256 `7dca7e589def8b7787dfc1e49bfb1ca809557f651dc4b43ad73d65ae64d5439c` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is prerequisite-first migration sequencing, Entry
Point identity rename before separate source relocation, equivalent
before-and-after validation, complete consumer impact review, preservation of
user-owned changes, non-destructive recovery, and the bounded downstream plan
reconciliation. Implementation, rename, relocation, public identity or
behavior change, release assembly, profile or claim publication, pushing, and
component-contract publication remain excluded.
