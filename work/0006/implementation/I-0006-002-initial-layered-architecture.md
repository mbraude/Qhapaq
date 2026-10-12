---
id: I-0006-002
kind: implementation
granularity: milestone
change_kind: maintenance
title: Verify the initial layered architecture and Service V1 vertical slice
status: open
spec: SPEC-0006
requirements:
  - R-0006-001
  - R-0006-002
  - R-0006-003
  - R-0006-004
  - R-0006-005
  - R-0006-006
  - R-0006-007
  - R-0006-008
  - R-0006-009
  - R-0006-010
  - R-0006-011
  - R-0006-012
  - R-0006-013
  - R-0006-014
  - R-0006-015
  - R-0006-016
  - R-0006-017
  - R-0006-018
  - R-0006-019
  - R-0006-020
  - R-0006-021
  - R-0006-022
  - R-0006-023
  - R-0006-024
  - R-0006-025
  - R-0006-026
  - R-0006-027
  - R-0006-028
  - R-0006-029
  - R-0006-030
  - R-0006-031
  - R-0006-032
  - R-0006-033
  - R-0006-034
  - R-0006-035
  - R-0006-036
  - R-0006-037
  - R-0006-038
depends_on:
  - I-0006-001
  - I-0007-001
  - I-0007-011
  - I-0008-008
  - I-0008-004
artifacts:
  - src/implementations/dotnet
---

# I-0006-002: Verify the Initial Layered Architecture and Service V1 Vertical Slice

## Objective and coverage

Aggregate acceptance of SPEC-0006's initial layer scaffold and first non-executing
Service V1 vertical slice after their implementation and required repository
migrations are delivered by their owning plans. This milestone does not own or
duplicate production code, architecture tests, or migration manifests.

The scope covers R-0006-001 through R-0006-038 for the initial scaffold and
descriptor-retrieval use case. Portable-helper semantics and later pipeline
model and execution behavior under R-0006-039 through R-0006-041 and subsequent
SPEC-0007 capabilities are excluded from this initial gate and remain governed
by their SPEC-0007 implementation items.

## Entry gates

The SPEC-0006 scope has current approved readiness; this milestone is decomposed
into concrete, approved slices; I-0006-001 is complete; and the actual output
artifacts from the cross-plan dependencies exist and have delivery approval.
SPEC-0008 identity and relocation work must pass its own readiness, validation,
recovery, and approval gates before its outputs satisfy this milestone.

## File and ownership manifest

Aggregate milestone only. SPEC-0007 owns the architecture-enforcement tests
and initial retrieval implementation; SPEC-0008 owns Entry Point identity
migration and source relocation. Concrete child slices must name exact files,
tests, and owners before this milestone is eligible for execution.

## Design and integration

Verify adjacent-layer calls, constructor-injected boundaries, public/internal
contract visibility, layer-owned composition, Service V1 compatibility,
Entry Point behavior preservation, and clean package-consumer boundaries
against the exact implementation outputs. Preserve SPEC-0008's migration
ordering and avoid treating an existing scaffold or placeholder as completed
behavior.

## Tests and validation

The eventual child slices must establish a passing before-state and validate
the affected project structure, assembly/root-namespace identities,
architecture rules, complete Microsoft DI graph and scopes, unit and
integration behavior, Service consumer boundary, and migrated path consumers.
Use the documented repository commands available at that time; do not infer
that a command exists from generated build output.

## Exit criteria

- [ ] The initial .NET project and test structure satisfies the approved SPEC-0006 and SPEC-0008 snapshots.
- [ ] Required architecture and package-consumer checks pass against real delivered collaborators.
- [ ] The first Service V1 vertical slice preserves the exact SPEC-0007 contracts and failure behavior.
- [ ] Entry Point identities and relocated paths satisfy their separate approved migration scopes.
- [ ] Exact input/output snapshots and all validation evidence are recorded.
- [ ] Explicit delivery review covers the aggregate outcome.

## Plan approval

Absent. This milestone cannot execute; concrete child slices and their exact
dependency edges must be approved first.

## Delivery evidence and review

No aggregate conformance assessment or implementation approval has been
recorded. Existing projects and `LayerDependencyTests` are only baseline
evidence.
