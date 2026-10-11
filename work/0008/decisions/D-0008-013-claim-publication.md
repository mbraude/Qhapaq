---
id: D-0008-013
kind: decision
title: Define profile and conformance claim publication
status: complete
spec: SPEC-0008
requirements: [R-0005-027, R-0005-029, R-0005-032, R-0005-034, R-0005-035, R-0008-007, R-0008-008, R-0008-009, R-0008-010, R-0008-011, R-0008-012, R-0008-013, R-0008-014, R-0008-015, R-0008-022, R-0008-023, R-0008-024, R-0008-025, R-0008-026]
depends_on: [D-0008-005, D-0008-006, D-0008-007, D-0008-011]
artifacts:
  - specs/0005-build-release-and-website-delivery.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-013: Define Profile and Conformance Claim Publication

## Objective

Define the review, approval, publication, support, retention, and withdrawal
process for profile definitions and implementation conformance claims.

## Scope and exclusions

Work-item completion, a passing test run, a commit, and component publication
are distinct. This item does not publish a profile or claim.

## Questions to resolve

Define approvers, exact snapshots, promotion gates, provenance, evidence
retention, support status, correction and withdrawal, and release integration.

## Acceptance criteria

- [x] Publication requires explicit approval of exact definitions, builds, and evidence.
- [x] Published claim meaning cannot change silently.
- [x] Correction, withdrawal, retention, and audit behavior is defined.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-023](../../../specs/0008-multi-language-conformance-and-repository-organization.md#profile-and-conformance-claim-publication)
  requires one identified authorized maintainer to approve the exact immutable
  profile or claim inputs after validation. Work-item, Git, test, evidence
  review, and component-publication events do not imply that authority.
- [SPEC-0008 R-0008-024](../../../specs/0008-multi-language-conformance-and-repository-organization.md#profile-and-conformance-claim-publication)
  defines content-addressed publication records and closed append-only profile
  and claim lifecycle states. Deprecated profiles permit new prominently
  warned claims; retired profiles do not.
- [SPEC-0008 R-0008-025](../../../specs/0008-multi-language-conformance-and-repository-organization.md#profile-and-conformance-claim-publication)
  makes corrections new immutable objects and defines explicit supersession
  and withdrawal without deletion or implicit replacement conformance.
- [SPEC-0008 R-0008-026](../../../specs/0008-multi-language-conformance-and-repository-organization.md#profile-and-conformance-claim-publication)
  retains publication records and tombstones indefinitely while requiring
  evidence for every active or otherwise verifiable claim.
- [SPEC-0005 R-0005-035](../../../specs/0005-build-release-and-website-delivery.md#6-build-and-version-model)
  permits profile and full-claim promotion only through protected stable or
  prerelease root manifests. Edge may publish immutable progress evidence but
  cannot publish or imply conformance.

This decision defines publication semantics but does not publish a profile,
claim, component contract, release, or implementation.

## Validation and review

Validated 2026-10-10:

- Confirmed 743 unique normative requirement IDs, 69 unique work-item IDs,
  resolvable changed-item requirement and dependency references, and an
  acyclic cross-plan dependency graph.
- Confirmed all 12 recorded SPEC-0008 source hashes match the exact current
  bytes, all relative links in the six changed Markdown files resolve, and
  `git diff --check` passes. Git reported only the repository's existing
  line-ending normalization warnings.
- Specification trace review ran without a semantic-review skip and returned
  `PASS` with no errors, warnings, or waivers. It classified the change as
  `requirement`, derived `R-0005-035@1d989e`,
  `R-0008-023@bfa7a1`, `R-0008-024@940fa2`,
  `R-0008-025@0b210a`, and `R-0008-026@b73a1a`, and confirmed that the new
  blocks preserve R-0005-027, R-0005-029, R-0005-032, R-0005-034,
  R-0008-007 through R-0008-015, and R-0008-022 without making an existing
  fingerprint or code/test reference stale.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and explicitly defers
  implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0005-build-release-and-website-delivery.md` | SHA-256 `42bc95d2ef871b191b09242561fed3fa812670f4eb410482d557c0413c193a3f` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `5097e7f8921b5e865feccbb304f890840a9b929e33fc159d468c8b089212bdc1` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | SHA-256 `5f8f4e7b4acc95922b67ff4818fefc6f6753bfc539cdcc82d86eb35d684142a5` |
| `work/0008/decisions/D-0008-013-claim-publication.md` | Material SHA-256 `15b3e64478da3704b7cc3dfc4bfd831ea88d63747be4a8855cc592c5fa57c83f` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `90b231d20c600c94acc0fe1b4422fb944a67b6e09cd2d0bd79eba422002b9401` |
| `work/0008/plan.md` | SHA-256 `2cc8fabcd9a9fd7c6cb8c57c4ef749d00e7543023bfc21693e947f77e2fbbfaf` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is exact-snapshot maintainer approval, protected
stable or prerelease promotion, immutable publication records, closed profile
and claim lifecycle states, new-object correction, explicit withdrawal,
evidence availability, and indefinite audit tombstones. Profile, conformance
claim, component-contract, release, and implementation publication or
execution remain excluded.
