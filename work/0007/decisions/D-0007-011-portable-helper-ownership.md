---
id: D-0007-011
kind: decision
title: Shared portable algorithm ownership
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0007-348, R-0006-020]
depends_on: [D-0007-009]
artifacts: [specs/0006-dotnet-layered-architecture.md]
---

# D-0007-011: Portable Helper Ownership

## Objective

Assign shared responsibilities before generator and runtime implementations diverge.

## Scope and exclusions

Canonicalization, digest computation, schema/descriptor/vocabulary validation,
and diagnostic construction. Reuse must not bypass layer boundaries.

## Questions to resolve

Which layer or reviewed tooling boundary owns each algorithm? Which consumers
reuse it, and how are build diagnostics distinct from runtime diagnostics?

## Acceptance criteria

- [ ] Persistent map assigns each helper family and its permitted consumers.
- [ ] Adjacent-layer contracts and tooling boundaries remain explicit.
- [ ] Determinism, offline behavior, and safe diagnostic envelopes are preserved.
- [ ] Required architecture checks and exact-snapshot approval are recorded.

## Resolution

Unresolved. Actual helper files are planned with implementation slices later.

## Validation and review

No shared-project or package boundary selected by extraction.
