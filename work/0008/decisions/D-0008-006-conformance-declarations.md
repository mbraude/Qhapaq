---
id: D-0008-006
kind: decision
title: Define capability and conformance declarations
status: complete
spec: SPEC-0008
requirements: [R-0000-009, R-0008-006, R-0008-007, R-0008-008, R-0008-009, R-0008-010]
depends_on: [D-0008-004, D-0008-005]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-006: Define Capability and Conformance Declarations

## Objective

Define machine-readable and human-readable declarations for profile support,
capabilities, unsupported behavior, partial progress, and exact evidence.

## Scope and exclusions

A declaration reports support; it does not itself prove conformance or make a
mandatory profile obligation optional. No schema is published by this decision.

## Questions to resolve

Define identities, required fields, capability relationships, unsupported and
partial states, evidence links, failure representation, and validation rules.

## Acceptance criteria

- [x] Full claims, progress, unsupported behavior, and failures are distinguishable.
- [x] Declarations bind exact profile and implementation versions.
- [x] Mandatory obligations cannot be hidden by capability omission.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-009](../../../specs/0008-multi-language-conformance-and-repository-organization.md#capability-and-conformance-declarations)
  defines one closed, versioned declaration envelope with the distinct kinds
  `conformance-claim`, `progress`, and `unsupported-target`.
- Each declaration addresses one exact published profile version and binds one
  implementation ID, declared version, and immutable artifact-set digest.
  Human-readable renderings preserve rather than broaden that machine-readable
  meaning.
- Optional capabilities use exact identities and only `supported` or
  `unsupported`; omission makes no assertion, and partial capability claims
  require independently defined narrower capabilities.
- [SPEC-0008 R-0008-010](../../../specs/0008-multi-language-conformance-and-repository-organization.md#capability-and-conformance-declarations)
  keeps requirement IDs and fingerprints out of the ordinary declaration by
  binding an immutable assessment manifest. That manifest exhaustively marks
  every mandatory obligation `satisfied`, `failed`, or `not-evaluated` and
  maps positive results to exact evidence entries.
- Full claims require every mandatory obligation to be satisfied. Progress
  preserves failed and unevaluated obligations. Unsupported targets are limited
  to `surface-absent`, `not-implemented`, or `platform-unsupported`; attempted
  but incomplete support remains progress.
- A schema, evidence-sufficiency thresholds, publication and support
  procedures, concrete declarations, implementation, and contract publication
  remain excluded.

## Validation and review

Validated 2026-10-10:

- Confirmed the plan source snapshot matches the exact edited SPEC-0008 bytes,
  all ten sequential SPEC-0008 requirement identifiers are unique, all 19
  work-item identities are unique, and all 45 direct dependencies resolve.
- Confirmed all relative links in the six changed Markdown files resolve and
  `git diff --check` passes.
- Derived `R-0008-009@6dfa76` and `R-0008-010@8795f0`. The unchanged
  R-0008-006, R-0008-007, and R-0008-008 fingerprints remain `7a5169`,
  `8b507a`, and `fcca09`; no stale fingerprint references exist.
- Specification trace review ran without a semantic-review skip and returned
  `PASS` with no errors, warnings, or waivers. It classified the change as
  `requirement`; no product or test code changed.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `f275062e9abf2c1ce67a23055549a26e98e33f1c1a7852851345fbdd1227ce5d` |
| `work/0008/decisions/D-0008-006-conformance-declarations.md` | Material SHA-256 `e40bc9ae2d8635ed6dc57c87ddfd99d838f7c5d24b4b3191f29965905d7836a7` |
| `work/0008/decisions/D-0008-007-conformance-evidence.md` | SHA-256 `a41ce15630d970ed225f90bfc77c9cba67c6aa8c9a0b4abc33f3700d0d948353` |
| `work/0008/decisions/D-0008-013-claim-publication.md` | SHA-256 `54fc5899d2f2d8b53049f6d4131d688fd432042fc33413bcc8accd31d81e74fc` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `af6464822e1f2c69bad09f3832d17aa9d959bb68823f179abaa789bb90a2ad83` |
| `work/0008/plan.md` | SHA-256 `a0cad0f119ed562d0eeca780ac12d25dac7baf3651e77c1b67fa310eb4bf893a` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is the closed, versioned declaration envelope; exact
profile and implementation artifact-set binding; capability dispositions;
immutable assessment-manifest references; exhaustive mandatory-obligation
results; full-claim, progress, unsupported-target, and invalidity semantics
defined by R-0008-009 and R-0008-010. Declaration schemas, evidence-sufficiency
thresholds, publication and support procedures, concrete declarations,
implementation, contract publication, and pushing remain excluded.
