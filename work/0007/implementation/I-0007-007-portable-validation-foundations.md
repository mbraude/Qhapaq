---
id: I-0007-007
kind: implementation
granularity: milestone
change_kind: requirement
title: Shared portable validation foundations
status: open
spec: SPEC-0007
requirements: [R-0007-348, R-0006-021, R-0006-024, R-0006-039, R-0006-041, R-0008-001, R-0008-002, R-0008-003, R-0008-019, R-0000-019, R-0000-020]
depends_on: [I-0007-001, I-0007-002, I-0007-005, D-0008-015]
artifacts: [src/common/dotnet/src, src/common/dotnet/tests]
---

# I-0007-007: Portable Validation Foundations

## Objective and coverage

Phase 1A: strict JSON; RFC 8785 and digests; exact offline document schema
selection; embedded profile/reference/cycle/complexity validation; bounded
patterns/formats; descriptor/vocabulary validation; safe location-aware diagnostics.
The shared production project and its tests belong to the self-contained
`src/common/dotnet/` workspace, not the .NET implementation workspace.

## Entry gates

Phase 0A and applicable Phase 1 foundations. Descriptor-specific sub-slices also
require I-0007-003's artifacts; this is not a whole-Phase-1 barrier.

## File and ownership manifest

Pending splitting into concrete algorithm slices under decided reuse boundaries.

## Design and integration

Business owns runtime validation semantics under R-0006-039. The single
implementation resides in
`src/common/dotnet/src/Qhapaq.Portable.Validation/`, selected by D-0007-012 and
required by R-0006-041; its tests reside under `src/common/dotnet/tests/`.
Business references it at runtime and the generator uses it only as build-time
tooling. Reviewed low-level dependencies must
preserve deterministic offline behavior. Generator-only dependencies must not
add runtime assets to consuming applications. No host dependencies, network,
operation construction, project-code execution, or duplicate implementations.

## Tests and validation

All applicable portable parsing, canonicalization, schema, pattern, format,
descriptor, vocabulary, digest and diagnostic vectors; culture/path/Unicode
boundaries and documented build-and-test.

## Exit criteria

- [ ] Every R-0007-348 checklist obligation has a delivered tested implementation.
- [ ] Reuse boundaries, artifact prerequisites, checks and human review pass.

## Plan approval

Absent. Narrow slices must precede execution and replace conditional prerequisites
with exact dependency IDs as their scopes become concrete.

## Delivery evidence and review

No foundations implemented by extraction.
