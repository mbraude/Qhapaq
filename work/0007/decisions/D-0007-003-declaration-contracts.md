---
id: D-0007-003
kind: decision
title: Declaration APIs, manifest envelope and generator compatibility
status: open
spec: SPEC-0007
requirements: [R-0007-344, R-0007-258, R-0007-261, R-0007-268, R-0007-290, R-0007-291, R-0007-295]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-003: Declaration Contracts

## Objective

Resolve the declaration, manifest, diagnostic, and compatibility contracts in
R-0007-344 and Section 23 question 1.

## Scope and exclusions

Supported .NET authoring/registration APIs, portable manifest envelope,
diagnostic-code policy, and initial compatibility matrix. Organization decisions
are coordinated with Phase 0A; no implementation classes are scaffolded here.
Namespaces cannot be finalized inconsistently with those decisions.

## Questions to resolve

What are the exact marker constructor, static declaration and generated API
names, manifest shape, stable diagnostic codes, registration contract versions,
and accepted/emitted descriptor/manifest support matrix?

## Acceptance criteria

- [ ] Public authoring shapes and required runtime registration APIs are explicit.
- [ ] Manifest closure, canonical ordering, byte equality, and version axes agree.
- [ ] Diagnostics cover required rejected inputs with stable safe mappings.
- [ ] Supported, mixed, unknown, and incompatible versions have exact outcomes.
- [ ] Related examples and conformance expectations agree; existing alpha format
  is preserved rather than silently rewritten.
- [ ] Checks pass and the exact decision is reviewed and approved.

## Resolution

Unresolved. Coordinate ownership with [D-0007-009](D-0007-009-model-ownership.md)
and tooling reuse with [D-0007-012](D-0007-012-generator-runtime-reuse.md).
Coordination is not an artificial dependency on unrelated Phase 0 work.

## Validation and review

Exact contracts and Section 23 question remain unresolved; no API approval claimed.
