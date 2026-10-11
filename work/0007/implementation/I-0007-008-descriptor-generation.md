---
id: I-0007-008
kind: implementation
granularity: milestone
change_kind: requirement
title: .NET descriptor authoring and deterministic generation
status: open
spec: SPEC-0007
requirements: [R-0007-349, R-0007-335, R-0008-019, R-0006-035, R-0006-036, R-0006-037, R-0006-038, R-0006-039]
depends_on: [D-0007-003, D-0007-012, D-0008-010, I-0007-001, I-0007-002, I-0007-003, I-0007-007]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-008: Descriptor Generation

## Objective and coverage

Phase 2: authoring value/marker/static contracts; incremental generator; explicit
inputs; exact case/basename association; offline validation/digests/generic
agreement; deterministic declaration/registration/manifest bytes and diagnostics.

## Entry gates

Exact authoring contracts, relevant Phase 0A/1/1A artifacts and approved readiness.

## File and ownership manifest

The generator is owned by the .NET implementation workspace as independently
versioned build tooling. Exact project, package, public API, shared-library,
and test manifests remain pending D-0007-012 and concrete slice planning.

## Design and integration

No source execution or runtime scanning. Preserve format support matrix and
equal embedded/package manifest bytes.
Keep compiler-symbol, source-location, and build-diagnostic models tooling-local;
public descriptor projections expose only supported immutable nested values.
SPEC-0006 R-0006-039 and D-0007-011 assign logical ownership of portable
validation semantics to Business and require the generator to consume those
semantics without a parallel implementation. The physical tooling/library
boundary remains gated by D-0007-012.

## Tests and validation

All R-0007-349 cases, reproducibility across paths/cultures/input order, clean
consumer packages, and minimal trimming/Native AOT smoke path before API expansion.

## Exit criteria

- [ ] Clean consumer authors, validates, generates, registers and packages operations.
- [ ] Required publication constraints, checks and human delivery review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No authoring APIs, generator or AOT checks delivered here.
