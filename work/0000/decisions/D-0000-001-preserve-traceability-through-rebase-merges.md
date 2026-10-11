---
id: D-0000-001
kind: decision
title: Preserve commit traceability through rebase merges
status: complete
spec: SPEC-0000
requirements:
  - R-0000-045
depends_on: []
artifacts:
  - SPEC.md
  - docs/development/coding-conventions.md
---

# D-0000-001: Preserve Commit Traceability Through Rebase Merges

## Objective

Review the default pull-request integration method and preserve the
requirement provenance of each independently validated commit on the protected
default branch.

## Scope and exclusions

This decision is governed by R-0000-045 and ADR-0004. It covers the recommended
merge method, commit-trailer preservation, and whether opening a pull request
may rewrite its source branch.

It does not configure repository hosting settings, rename the default branch,
rewrite existing history, merge a pull request, define release-tag behavior,
approve work items, or publish component contracts.

## Questions to resolve

- Should independently validated commits remain distinct on the default branch?
- Should pull-request creation automatically rebase or otherwise rewrite its
  source branch?
- How should an explicitly selected future squash merge preserve specification
  coverage?

## Acceptance criteria

- [x] The preferred merge method preserves independently validated commits and
  their specification-traceability trailers.
- [x] Pull-request creation does not automatically rewrite the source branch.
- [x] The traceability convention remains safe if squash behavior is selected
  explicitly in the future.
- [x] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

Drafted for review:

- [R-0000-045](../../../SPEC.md#7-branching-changes-and-releases) prefers
  rebase merges so independently validated commits and their traceability
  trailers remain distinct, and prohibits automatic source-branch rewriting
  during pull-request creation.
- The
  [coding conventions](../../../docs/development/coding-conventions.md#3-specification-traceability)
  require default-branch integration to preserve every included commit's
  traceability. Rebase merge retains each commit and its trailers; an
  explicitly selected future squash merge must retain complete required
  `Spec:` coverage.

This resolution does not configure or perform a merge and does not implement
the proposed push or pull-request skills.

## Validation and review

Validated 2026-10-10:

- Confirmed R-0000-045 retains its identifier and changes fingerprint from
  `0c75d0` to `88335b`; no repository code or test reference uses the old
  fingerprint.
- Confirmed all relative links in the four changed Markdown files resolve,
  work-item IDs remain unique, required decision sections are present, the
  plan's SPEC source hash matches the exact current bytes, and
  `git diff --check` passes. Git reported only the repository's existing
  line-ending normalization warnings.
- Specification trace review ran without a semantic-review skip and returned
  `PASS` with no errors, warnings, or waivers. It classified the change as
  `amendment` and derived `R-0000-045@88335b`. No product code or tests changed.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `SPEC.md` | SHA-256 `c68a0e3c08b3d6c1baa7b5753cf4d3630f94fe5f7936bfede002e2e9f662c908` |
| `docs/development/coding-conventions.md` | SHA-256 `49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834` |
| `work/0000/plan.md` | SHA-256 `1414fbe4e56082a264a78f2208ee816ac72a32fa4cb2dd24fe5b0deff2d7464d` |
| `work/0000/decisions/D-0000-001-preserve-traceability-through-rebase-merges.md` | Material SHA-256 `9e066e56863d6b72e2ff4d5a0ef397f1c46a04a266e98f206f576699590cfdae` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is rebase-merge preference, preservation of
independently validated commits and their traceability trailers, prohibition
on automatic source-branch rewriting during pull-request creation, and the
bounded future-squash traceability rule. Repository-hosting configuration,
default-branch renaming, history rewriting, merging, release tagging,
work-item approval by Git operations, and component-contract publication
remain excluded.
