---
id: D-0008-007
kind: decision
title: Define sufficient conformance evidence
status: complete
spec: SPEC-0008
requirements: [R-0000-007, R-0000-009, R-0008-006, R-0008-007, R-0008-008, R-0008-010, R-0008-011, R-0008-012, R-0008-013, R-0008-014, R-0008-015]
depends_on: [D-0008-004, D-0008-005]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-007: Define Sufficient Conformance Evidence

## Objective

Define which shared vectors, language-specific tests, reviews, security checks,
and release evidence are sufficient for each profile claim.

## Scope and exclusions

Passing vectors alone does not prove obligations that require code review,
architecture evidence, concurrency testing, or security analysis. This item
does not implement a harness.

## Questions to resolve

Map obligation types to evidence; define skipped-case handling, synthetic data,
bounded execution, exact build identity, retention, reproducibility, and review.

## Acceptance criteria

- [x] Every obligation category has sufficient, observable evidence.
- [x] Skips, missing evidence, failures, and unsupported obligations cannot look successful.
- [x] Reports exclude credentials and sensitive payloads.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-011](../../../specs/0008-multi-language-conformance-and-repository-organization.md#conformance-evidence)
  makes sufficient evidence an immutable part of each profile version. Its
  complete matrix uses closed portable evidence kinds and profile-fixed
  `all-of` and `any-of` recipes with exact executable bounds.
- [SPEC-0008 R-0008-012](../../../specs/0008-multi-language-conformance-and-repository-organization.md#conformance-evidence)
  defines immutable evidence entries, closed outcomes, exact build and
  artifact identity, independent rerun inputs, and digest-bound review
  approvals. Self-review is permitted for the current single-author project.
- [SPEC-0008 R-0008-013 through R-0008-015](../../../specs/0008-multi-language-conformance-and-repository-organization.md#conformance-evidence)
  prevents missing, skipped, failed, errored, mismatched, incomplete, or
  unverified evidence from satisfying a recipe; requires synthetic,
  non-sensitive evidence; and ties availability to the period during which a
  declaration is presented as verifiable.
- Harness and schema implementation, concrete profile matrices, publication
  and withdrawal procedures, independent-review policy, and contract
  publication remain excluded.

## Validation and review

Validated 2026-10-10:

- Confirmed all 11 plan source snapshots match the exact current bytes, all 15
  sequential SPEC-0008 requirement identifiers are unique, all 19 work-item
  identities are unique, and all 45 direct dependencies resolve.
- Confirmed all relative links in the five changed Markdown files resolve and
  `git diff --check` passes.
- Derived `R-0008-011@ddf0c6`, `R-0008-012@b93ca9`,
  `R-0008-013@980847`, `R-0008-014@c8b6fb`, and
  `R-0008-015@c3b775`. No stale fingerprint references exist.
- Specification trace review ran without a semantic-review skip and returned
  `PASS` with no errors, warnings, or waivers. It classified the change as
  `requirement`; no product or test code changed.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `7a1f61e8de54ba3dc9e789075c93445d4bd72703c0dd3b8bb41889120d32addb` |
| `work/0008/decisions/D-0008-007-conformance-evidence.md` | Material SHA-256 `0aef11b387bd8b8413443b86824a5d2d12ca1ed3bf683f73a3bb32ac6f38f7ab` |
| `work/0008/decisions/D-0008-013-claim-publication.md` | SHA-256 `29b5b578107516983a64d302fed6c41e94faa30cc211b0855181d78f0143a744` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `7b009be05ecdcc4ab9dbda5b2f848c3b9a50c3eec30f79e79549fe6cbb1da159` |
| `work/0008/plan.md` | SHA-256 `5dc9366349a52a4f7931133262d6d6cb1f9b1603042e7403d24cbdb836e68e85` |

Approved explicitly in this session on 2026-10-10 for the corrected exact
snapshot above. The approved scope is the immutable profile-version evidence
matrix; closed portable evidence kinds; profile-fixed `all-of` and `any-of`
recipes; exact executable bounds; immutable, independently rerunnable
evidence; digest-bound build provenance and review approval; explicit
unsuccessful outcomes; synthetic-data and sensitive-content rules; and
evidence availability defined by R-0008-011 through R-0008-015. Harness and
schema implementation, concrete profile matrices, publication and withdrawal
procedures, independent-review policy, contract publication, and pushing
remain excluded.
