---
id: D-0008-008
kind: decision
title: Define language-native traceability placement and checking
status: complete
spec: SPEC-0008
requirements:
  - R-0008-005
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on: [D-0008-002, D-0008-003]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - docs/architecture/decisions/0003-enforce-specification-traceability.md
  - docs/development/coding-conventions.md
---

# D-0008-008: Define Language-Native Traceability Placement and Checking

## Objective

Define language-native placements and checker architecture for the portable
`spec: <requirement-id>@<fingerprint>` payload without weakening ADR-0003 or
existing waiver and reverse-impact rules.

## Scope and exclusions

R-0008-005 separates portable requirements from explicitly scoped language
contracts. This item does not revisit that ownership model, require C# XML
documentation in every language, or waive current traceability obligations.

## Questions to resolve

Define supported comment/documentation constructs, parser boundaries,
invariant and test placement, multi-language scanning, diagnostics, and
extension of current waiver handling.

## Acceptance criteria

- [x] The marker payload remains portable and exact.
- [x] Each supported language has unambiguous invariant and test placement.
- [x] Fingerprint, reverse-impact, and waiver behavior is not weakened.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-016](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
  preserves the exact portable marker payload while requiring each maintained
  implementation language to register unambiguous native invariant,
  whole-member, and test placements plus a matching checker extractor.
- [SPEC-0008 R-0008-017](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
  adopts language-aware extractors feeding one shared payload and rules engine,
  with explicit source diagnostics and failure for malformed, unsupported,
  stale, unresolved, missing, or unextractable traceability evidence.
- [SPEC-0008 R-0008-018](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
  keeps waiver syntax portable, scoped, reviewable, and unable to bypass
  mechanical checks or reverse-impact review.
- [ADR-0003](../../../docs/architecture/decisions/0003-enforce-specification-traceability.md#source-references)
  records the extractor boundary and shared-engine ownership.
  [Coding conventions](../../../docs/development/coding-conventions.md#3-specification-traceability)
  define the common registration rule and current C# placements.
- Checker implementation, CI integration, another runtime, and moving existing
  .NET-specific policy into a specialized guide remain excluded.

## Validation and review

Validated 2026-10-10:

- Confirmed all 11 plan source snapshots match the exact current bytes, all 18
  SPEC-0008 requirement identifiers are unique and comprise the complete
  sequence R-0008-001 through R-0008-018, all 20 work-item identities are
  unique, every direct dependency resolves, and the dependency graph is
  acyclic.
- Confirmed all relative links in the eight changed Markdown files resolve and
  `git diff --check` passes. Git reported only the repository's existing
  line-ending normalization warnings.
- Derived `R-0008-016@cfe5f4`, `R-0008-017@4e753a`, and
  `R-0008-018@2cb676`. No stale fingerprint references exist.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `requirement` and reviewed R-0008-016 through R-0008-018. The warning records
  the necessary mention of C# XML documentation while the requirement
  explicitly prevents that syntax from becoming portable. No product or test
  code changed.
- No build or unit tests were run because this decision changes only
  specification, architecture, policy, and planning documentation and creates
  no implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `4dab808ab9bd25ae591120a583e1b4d607fb8f28b66fdf2aa39ad711f7602d46` |
| `docs/architecture/decisions/0003-enforce-specification-traceability.md` | SHA-256 `1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83` |
| `docs/development/coding-conventions.md` | SHA-256 `604a6173250960aabdf3fd7c16c60c111f9e36ceb946baff1c28033c2654e454` |
| `work/0008/decisions/D-0008-008-language-native-traceability.md` | Material SHA-256 `c8ae60bf1bdbb10277b47160a7a645cf1bbae969352a032942ec05dc6b910b26` |
| `work/0008/decisions/D-0008-011-build-ci-release-orchestration.md` | SHA-256 `3b7081802ff8cf91575a0b43f119790df9febfa687790f7c654b50ea1e1002f3` |
| `work/0008/implementation/I-0008-001-engineering-policy-separation.md` | SHA-256 `fc3128316dc5e0982d1931bcd74d4d139c3ee0d5333796934c211e2431d125a3` |
| `work/0008/implementation/I-0008-007-trace-checker.md` | SHA-256 `42eab27c6be3d1a026e8a9faa5ef7ac88d36020d2ae49bfdf7a24e6140ed861d` |
| `work/0008/plan.md` | SHA-256 `3d0b717790f7451ea3545a0e44ae5c66f4af628fdb9452c28c4c2b5d0bdaa7f7` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is the portable marker and waiver payloads;
policy-defined native invariant, whole-member, and test placements; registered
language-aware extractors feeding one shared rules engine; explicit
diagnostics; and preserved fingerprint, reverse-impact, mechanical-check, and
waiver limits defined by R-0008-016 through R-0008-018. Checker
implementation, CI integration, another runtime, moving existing .NET-specific
policy into a specialized guide, component contract publication, and pushing
remain excluded.
