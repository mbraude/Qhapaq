---
id: D-0007-004
kind: decision
title: First non-executing descriptor retrieval Service and CLI contracts
status: complete
spec: SPEC-0007
requirements: [R-0007-344, R-0007-352, R-0007-400, R-0007-401, R-0007-402, R-0007-403, R-0007-404, R-0007-405, R-0007-406, R-0007-407, R-0007-408, R-0007-409, R-0007-410, R-0006-004, R-0006-005, R-0006-033]
depends_on: [D-0007-006]
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md, specs/0006-dotnet-layered-architecture.md]
---

# D-0007-004: Exact Descriptor Retrieval

## Objective

Specify the first policy-filtered exact descriptor retrieval vertical slice.
This also covers the first-Service open questions in SPEC-0006.

## Scope and exclusions

Versioned public request/result/structured-error shapes, exact CLI mappings,
cancellation, unavailability/conflicts, and descriptor disclosure. No operation
execution, credentials, extension installation, or trusted-profile mutation.

## Questions to resolve

What exact version/digest selectors and responses are exposed? How are
disclosure denial, unavailable/conflicting descriptors, cancellation and safe
diagnostics mapped through Service V1 and CLI?

## Acceptance criteria

- [x] Exact public contracts and CLI input/output/status mappings are specified.
- [x] Disclosure and lookup behavior are explicit and fail closed.
- [x] Adjacent-layer and clean third-party consumer expectations are preserved.
- [x] Non-executing guarantees and conformance cases are explicit.
- [x] Coordinate unavailable conclusions with D-0007-006 without implying authority.
- [x] Relevant source indexes/references and traceability checks are complete;
  exact-snapshot human review remains the lifecycle gate.

## Resolution

Resolved in
[SPEC-0007 Section 14.2](../../../specs/0007-portable-pipeline-definitions-and-binding.md#142-exact-descriptor-retrieval):

- R-0007-404 through R-0007-406 define the exact Service V1 selector, closed
  result envelope, disclosure behavior, and structured errors.
- R-0007-407 and R-0007-408 define the exact CLI grammar, projections, and
  stable exit statuses.
- R-0007-409 preserves adjacent-layer collaboration, cancellation, and the
  non-executing boundary.
- R-0007-410 defines language-neutral Service and CLI conformance coverage.

The remaining subsequent CLI and MCP contracts stay with
[D-0007-005](D-0007-005-subsequent-surface-contracts.md); no third decision item
is created.

## Validation and review

Decision input: on 2026-10-10 the user explicitly selected:

- required operation ID and exact contract version with an optional expected
  digest precondition;
- one indistinguishable unavailable outcome for absent or non-disclosable
  descriptors;
- `qhapaq operation get` with text and versioned JSON projections;
- stable exit statuses `0`, `1`, `2`, `3`, `4`, `5`, and `130`;
- a normal fail-closed digest-mismatch result after disclosure authorization;
- the immutable `OperationDescriptor` inside versioned result envelopes; and
- one asynchronous Service response envelope containing exactly one normal
  result or structured error.

Validation performed on 2026-10-10:

- Work-artifact structure: PASS. Checked 48 unique item identities, dependency
  targets, no cancelled prerequisites, acyclic ordering, one phase membership
  per item, and all 12 exact plan source snapshots.
- Specification structure: PASS. All 410 R-0007 identifiers are unique;
  R-0007-404 through R-0007-410 are the next unused sequence, and no prior
  identifier was removed or retired.
- Specification trace check: PASS with warnings. Classified as `requirement`
  because the change adds seven platform requirement blocks. Repository-wide
  reverse-impact review found no changed code or tests, stale fingerprint,
  removed requirement, or waiver. The warning is expected: this explicitly
  .NET-specific Service subsection names public CLR contracts.
- Semantic review: PASS. Checked the new requirements against R-0007-297,
  R-0007-300, R-0007-301, R-0007-344, R-0007-352, R-0007-400 through
  R-0007-403, R-0006-001, R-0006-003 through R-0006-005, R-0006-032,
  R-0006-033, R-0001-044, and R-0002-028 through R-0002-032. Exact selection,
  fail-closed disclosure, stage-aware conclusions, adapter authority, public
  Service versioning, structured failures, cancellation, and non-execution
  remain consistent.
- Documentation checks: PASS. `git diff --check` reported no whitespace error,
  local links in all changed Markdown resolve, and all plan source hashes match
  exact current bytes.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `64a84a47f788c7efcd0ecfe85278358f3bde1d1f0bc5ee245afa19327a7185d6` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `1abf378410e3d9563f39ec37baf46757998ee029e55e86fdd5c78539f020a1f3` |
| `work/0007/plan.md` | SHA-256 `0b1b7da7833d2014a138ad9ba2ddad7f63899efb9099beae7cef8b7af66875e2` |
| `work/0007/implementation/I-0007-011-first-service-cli-slice.md` | SHA-256 `fd37295fc2761a5f5dcefdee970dcf27f03b5813f49966083eee023cf85ad251` |

Approval recorded on 2026-10-10: the user explicitly approved this exact
snapshot in this session.

Approved scope: D-0007-004 and its exact descriptor-retrieval Service V1 and
CLI contract outcome, including the bounded SPEC-0007 plan reconciliation and
I-0007-011 requirement coverage. Commit scope is exactly this decision,
SPEC-0007, `work/0007/plan.md`, and I-0007-011.

Exclusions: implementation, schemas, conformance vectors, contract publication,
execution, credentials, extension installation, trusted-profile mutation,
payload-disclosure authority, and specification-readiness approval.

Approval covers unchanged material content with SHA-256
`64a84a47f788c7efcd0ecfe85278358f3bde1d1f0bc5ee245afa19327a7185d6` and
these exact full-byte snapshots:

| Material | SHA-256 |
| --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `1abf378410e3d9563f39ec37baf46757998ee029e55e86fdd5c78539f020a1f3` |
| `work/0007/plan.md` | `0b1b7da7833d2014a138ad9ba2ddad7f63899efb9099beae7cef8b7af66875e2` |
| `work/0007/implementation/I-0007-011-first-service-cli-slice.md` | `fd37295fc2761a5f5dcefdee970dcf27f03b5813f49966083eee023cf85ad251` |

Approval and completion do not authorize implementation, publication,
execution, payload disclosure, or specification readiness.

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0007-404@a3072c, R-0007-405@80b08b, R-0007-406@469690
Spec: R-0007-407@ee4706, R-0007-408@b1bb45, R-0007-409@151a07
Spec: R-0007-410@2f7f60
```
