---
id: D-0007-012
kind: decision
title: Generator and runtime reuse boundaries
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0007-259, R-0007-260, R-0007-348, R-0008-019, R-0006-039]
depends_on: [D-0007-011, D-0008-010]
artifacts: [specs/0006-dotnet-layered-architecture.md]
---

# D-0007-012: Generator and Runtime Reuse

## Objective

Decide how build-time tooling shares portable algorithms with runtime consumers.

## Scope and exclusions

Required project/package/dependency boundaries; no runtime hosting dependency
inside generator validation, operation construction, network use, or layer bypass.
R-0006-039 and D-0007-011 assign logical semantic ownership but do not decide
the shared-library boundary owned by this item. R-0008-019 fixes workspace
ownership but does not decide that shared-library boundary.

## Questions to resolve

How do tooling and runtime reuse the owned algorithms? Does this require a
new reviewed assembly/package boundary, and how is it enforced?

## Acceptance criteria

- [ ] Tooling/runtime dependency map is persistent and compatible with SPEC-0006.
- [ ] Any necessary boundary change is decided before code implementation.
- [ ] Offline, non-executing generation and runtime validation share semantics.
- [ ] Architecture-test requirements, validation, and human approval are recorded.

## Resolution

Unresolved. A new ADR may replace the listed SPEC-0006 output when chosen.

## Validation and review

No generator dependency or package layout is selected during bootstrap.
