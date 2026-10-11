---
id: I-0007-001
kind: implementation
granularity: milestone
change_kind: maintenance
title: Enforce Phase 0A organization decisions
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0006-030, R-0006-031, R-0006-035, R-0006-036, R-0006-037, R-0006-038]
depends_on: [D-0007-008, D-0007-009, D-0007-010, D-0007-011, D-0007-012, D-0007-013, D-0007-014]
artifacts: [implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests]
---

# I-0007-001: Architecture Enforcement

## Objective and coverage

Complete Phase 0A by extending existing architecture tests for decided namespace,
visibility, dependencies, composition, and representative ownership relationships.

## Entry gates

Approved organization decisions and reviewed source readiness. Existing
LayerDependencyTests are baseline evidence, not completion of new checks.

## File and ownership manifest

Pending concrete slice planning; extend the architecture test project, not empty
production types. Exact test files and scope must be approved before execution.

## Design and integration

Preserve SPEC-0006's adjacent-layer boundaries and test existing real collaborators.
For D-0007-008, enumerate handwritten production C# files and compare each
declared namespace with the owning project's `RootNamespace` plus every
project-relative directory segment. Keep generated-namespace contract checks
separate.

For D-0007-009, enforce SPEC-0006 R-0006-035 through R-0006-038 against real
models: cross-layer contract placement, recursive public-signature reachability
(including nested descriptor/schema values and generic arguments), and exclusion
of concrete plans, private frame state, transport models, and compiler models
from public/runtime boundaries. Package-consumer and behavioral cases belong to
the corresponding retrieval, generator, and parsing slices, not placeholder
model creation in this milestone. Type relationships and shared-helper/tooling
boundaries remain pending D-0007-010 through D-0007-012.

## Tests and validation

Prove the decided rules reject violations; run documented architecture tests,
traceability and build-and-test when delivered.

## Exit criteria

- [ ] R-0007-346 ownership map and relationships have applicable enforcing tests.
- [ ] Handwritten production source uses exact project-relative namespaces and
  generated namespace contracts are tested separately.
- [ ] Checks pass and exact delivered scope receives human approval.

## Plan approval

Absent. This milestone cannot execute.

## Delivery evidence and review

No new tests run or delivered during bootstrap.
