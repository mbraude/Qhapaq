---
id: D-0007-013
kind: decision
title: Conformance loading, golden files and consumer test conventions
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0007-347, R-0006-031]
depends_on: []
artifacts: [docs/development/coding-conventions.md]
---

# D-0007-013: Test Artifact Conventions

## Objective

Define .NET test consumption conventions without duplicating portable cases.

## Scope and exclusions

Vector loading, golden-file regeneration/maintenance, and clean package-consumer
tests. Portable vector envelope semantics are D-0007-015, not host-specific policy.

## Questions to resolve

How are shared vectors located and selected deterministically? How are golden
changes reviewed/regenerated? What makes a consumer test independent of internals?

## Acceptance criteria

- [ ] Persistent loading and golden-file procedures identify authoritative inputs.
- [ ] Tests report exact artifact versions/capabilities without duplicated cases.
- [ ] Clean consumer boundaries and architecture-test implications are explicit.
- [ ] Coordinate portable conventions with D-0007-015; checks and review pass.

## Resolution

Unresolved. No new test tooling is installed or implemented by this item.

## Validation and review

Existing test projects do not establish the missing vector/consumer conventions.
