---
id: D-0007-004
kind: decision
title: First non-executing descriptor retrieval Service and CLI contracts
status: open
spec: SPEC-0007
requirements: [R-0007-344, R-0007-352, R-0006-004, R-0006-005, R-0006-033]
depends_on: []
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

- [ ] Exact public contracts and CLI input/output/status mappings are specified.
- [ ] Disclosure and lookup behavior are explicit and fail closed.
- [ ] Adjacent-layer and clean third-party consumer expectations are preserved.
- [ ] Non-executing guarantees and conformance cases are explicit.
- [ ] Coordinate unavailable conclusions with D-0007-006 without implying authority.
- [ ] Relevant source indexes/references, traceability, and review are complete.

## Resolution

Unresolved. Section 23 question 2 is split between this first slice and
[D-0007-005](D-0007-005-subsequent-surface-contracts.md); it is not a third item.

## Validation and review

No request, result, CLI grammar, or error-shape decision made during extraction.
