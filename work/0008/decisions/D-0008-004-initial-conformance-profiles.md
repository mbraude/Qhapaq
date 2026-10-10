---
id: D-0008-004
kind: decision
title: Define initial conformance profiles and dependencies
status: complete
spec: SPEC-0008
requirements: [R-0000-007, R-0000-009]
depends_on: [D-0008-003]
artifacts:
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-004: Define Initial Conformance Profiles and Dependencies

## Objective

Define the smallest coherent initial profiles, mandatory runtime baseline,
applicability, prerequisite relationships, and permitted compatibility claims.

## Scope and exclusions

Profiles select existing obligations and cannot fork portable semantics, waive
mandatory rules, or imply support for an unimplemented runtime.

## Questions to resolve

Choose initial profile identities and boundaries; define prerequisite profiles,
optional capabilities, remote-client distinctions, and prohibited partial claims.

## Acceptance criteria

- [x] Each profile has coherent scope, applicability, and explicit prerequisites.
- [x] Mandatory requirements cannot be downgraded through capability declarations.
- [x] Claim language is precise and testable.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-006](../../../specs/0008-multi-language-conformance-and-repository-organization.md#meaning-of-a-profile)
  defines `qhapaq.runtime` as the portable execution baseline and defines
  `qhapaq.cli.local`, `qhapaq.mcp.host`, and
  `qhapaq.dotnet.in-process` as independent surface profiles that each require
  that baseline.
- The .NET profile covers the full supported in-process construction,
  validation, and execution API rather than a definition-only library.
- Profile obligations and transitive prerequisites are cumulative. CLI and MCP
  remain independent siblings, and no initial remote-client profile is defined.
- [SPEC-0008 R-0008-007](../../../specs/0008-multi-language-conformance-and-repository-organization.md#profiles-versus-capabilities)
  requires exact profile claims, prohibits partial or unqualified conformance
  claims, and keeps optional capabilities from weakening mandatory obligations.
- Profile version compatibility, machine-readable declarations, evidence
  sufficiency, publication, and remote-client contracts remain excluded for
  D-0008-005, D-0008-006, D-0008-007, and D-0008-013 or future protocol work.

## Validation and review

Validated 2026-10-10:

- Confirmed all 11 plan source hashes and committed baselines, seven sequential
  SPEC-0008 requirement identifiers, 19 unique work-item identities, and
  resolvable direct dependencies.
- Confirmed all relative links in the eight changed Markdown files resolve and
  `git diff --check` passes.
- Derived `R-0008-006@7a5169` and `R-0008-007@8b507a`; no existing fingerprint
  references require updates.
- Specification trace review ran without a semantic-review skip and returned
  `PASS with warnings`, with no errors or waivers. It classified the change as
  `requirement`. The warning identifies the .NET language and implementation
  scope necessarily named by the explicitly language-specific profile. No
  product or test code changed.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `d1649a3335e0034049538af508b6c7712cfa4ae3d1271a3a5fa73edcf55f0915` |
| `work/0008/decisions/D-0008-004-initial-conformance-profiles.md` | Material SHA-256 `b036b5b064ee2369475c37ce6ff27f257d6d8d63116f7bec1386ca6748293e41` |
| `work/0008/decisions/D-0008-005-profile-version-compatibility.md` | SHA-256 `cf61252a85f51b333ec5904f4aecb43d3629e34037dc2b5abe2af59f2db44d7e` |
| `work/0008/decisions/D-0008-006-conformance-declarations.md` | SHA-256 `0349dd5ca21433c3bdd47ad6bb358c72563a018d0de6cf9a60076c0a29c7b782` |
| `work/0008/decisions/D-0008-007-conformance-evidence.md` | SHA-256 `03b438c1e5e89107df2b9aa9f5d07332af65c3d5c8674912b604d4011cf0c790` |
| `work/0008/decisions/D-0008-013-claim-publication.md` | SHA-256 `7d79262ecf7faccef2752d5c8fa68b3e7b36184f6666a8a666e2450661c4cc72` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `b2321045b0820bdaa0be0e89bd9c800ce8932b9c0ba76a0cf430a1e525fd0b67` |
| `work/0008/plan.md` | SHA-256 `73cd3caaa1c27bfcf7397d7e0a64e2ca9b4a33711336e90a22767f02d1153ee7` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is the four initial profile identities and
applicability boundaries, cumulative portable-runtime prerequisites,
independent CLI and MCP profiles, the full supported in-process .NET profile,
and the conformance-claim restrictions defined by R-0008-006 and R-0008-007.
Profile versioning, declaration formats, evidence sufficiency, publication,
remote-client profiles and contracts, implementation, and contract publication
remain excluded.
