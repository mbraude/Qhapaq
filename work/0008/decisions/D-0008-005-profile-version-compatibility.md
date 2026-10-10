---
id: D-0008-005
kind: decision
title: Define profile versioning and compatibility
status: complete
spec: SPEC-0008
requirements: [R-0000-007, R-0000-009, R-0008-006, R-0008-007, R-0008-008]
depends_on: [D-0008-004]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-005: Define Profile Versioning and Compatibility

## Objective

Define how profile versions bind exact specification revisions and requirement
fingerprints and what changes preserve or break a compatibility claim.

## Scope and exclusions

Profile, implementation-release, document, protocol, and requirement
fingerprint versions remain distinct. This item does not select a schema format.

## Questions to resolve

Define immutable identity, snapshot binding, compatible additions and
corrections, retirement, supersession, support windows, and claim migration.

## Acceptance criteria

- [x] Version identities bind exact authoritative obligations.
- [x] Compatibility and breaking-change rules are explicit.
- [x] Existing claims cannot change meaning silently.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-008](../../../specs/0008-multi-language-conformance-and-repository-organization.md#profile-contents-and-version-identity)
  defines immutable `<profile-id>@<major>.<minor>` identities, beginning at
  `1.0`, that bind exact prerequisite versions, authoritative specification
  revisions, and mandatory requirement ID and fingerprint pairs.
- Minor versions permit only reviewed semantics-preserving corrections and
  non-mandatory additions. Mandatory-obligation, applicability, or prerequisite
  changes require a new major version.
- Retirement, supersession, support state, and withdrawal cannot change an
  existing profile version or claim. Claims never migrate automatically and
  version numbers imply no support period.
- Declaration schemas, evidence sufficiency, publication and support
  procedures, concrete profile publication, and implementation remain
  excluded.

## Validation and review

Validated 2026-10-10:

- Confirmed the plan source snapshot matches the exact edited SPEC-0008 bytes,
  all eight sequential SPEC-0008 requirement identifiers are unique, all 19
  work-item identities are unique, and direct dependencies resolve.
- Confirmed all relative links in the seven changed Markdown files resolve and
  `git diff --check` passes.
- Derived `R-0008-008@fcca09`; the unchanged R-0008-006 and R-0008-007
  fingerprints remain `7a5169` and `8b507a`. No existing R-0008-008
  fingerprint references require updates.
- Specification trace review ran without a semantic-review skip and returned
  `PASS` with no errors, warnings, or waivers. It classified the change as
  `requirement`; no product or test code changed.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `41646c6cc180d77734607990bf9aa9c836bfe7ec6e6916e19573529f326dc88d` |
| `work/0008/decisions/D-0008-005-profile-version-compatibility.md` | Material SHA-256 `66e8e6778db8ffc906ee4227edeb1bb512e2b29cda12d99a2fa8371489093812` |
| `work/0008/decisions/D-0008-006-conformance-declarations.md` | SHA-256 `f5f46abbbb11e5fc5d51463d22453413b1ac063e84af3912313e6f0a38cecc55` |
| `work/0008/decisions/D-0008-007-conformance-evidence.md` | SHA-256 `1616470070decd7dad3d58dafda0c9d84368f1c3586bcc39f62a3374a0ac6917` |
| `work/0008/decisions/D-0008-013-claim-publication.md` | SHA-256 `2d3ee59ef095010267c5bcce18c80635d7ca4b00dcd4c0428d60e621f1ed72a9` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `9af387884ad1845b81811a3d9a1fbc6e5a5dce437d55322748ff28e2a827682f` |
| `work/0008/plan.md` | SHA-256 `1569d5dc6ec4df5f7761153246f1fe54bbe0fc2553e4fb1e74315f33607ca6c9` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is immutable profile-version identity beginning at
`1.0`, exact prerequisite/specification/requirement-fingerprint binding,
minor-compatible and major-breaking change rules, immutable retirement and
supersession behavior, and explicit claim migration defined by R-0008-008.
Declaration schemas, evidence sufficiency, publication and support procedures,
concrete profile publication, implementation, and contract publication remain
excluded.
