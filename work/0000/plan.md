---
spec: SPEC-0000
process_version: 1
sources:
  - path: SPEC.md
    revision: 733f879fb7872fd692c0661af8e6eb62708a7e38
    content_sha256: c68a0e3c08b3d6c1baa7b5753cf4d3630f94fe5f7936bfede002e2e9f662c908
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 07d7b41d910f9dc7a65fea1cb05fb4c62bf6e7cb
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: 5c166ff223ad2d5c57824de534d409bcac22b090
    content_sha256: 49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834
---

# SPEC-0000: Work Plan

## Scope and authority

This plan tracks the current amendment to the repository integration policy in
[SPEC.md](../../SPEC.md), under the change classification and traceability rules
of [ADR-0004](../../docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md)
and the related
[coding conventions](../../docs/development/coding-conventions.md).

The plan does not redefine product behavior, approve a reviewed snapshot,
configure GitHub, rewrite a branch, open or merge a pull request, or migrate the
unrelated historical backlog already recorded in `SPEC.md`.

## Phase 1: Pull-request integration policy

### Entry gates

- [R-0000-045](../../SPEC.md#7-branching-changes-and-releases) governs the
  branching and integration recommendation.
- ADR-0004 requires every commit to carry an exact change classification and
  applicable specification provenance.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0000-001](decisions/D-0000-001-preserve-traceability-through-rebase-merges.md) | Review the amendment that makes rebase merge the preferred integration method while prohibiting automatic source-branch rewriting during pull-request creation. |

### Exit gates

- R-0000-045 and the traceability conventions describe one consistent
  integration policy.
- The exact amendment snapshot has passed required validation and explicit
  human review.

## External prerequisites

None.

## Reconciliation index

Historical source-impact and workflow evidence is stored in the [reconciliation index](reconciliations/index.md).
The linked records are non-material and do not own current plan state.
