---
id: D-0007-009
kind: decision
title: Model ownership and visibility map
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0006-010, R-0006-011, R-0006-012, R-0006-014]
depends_on: []
artifacts: [specs/0006-dotnet-layered-architecture.md]
---

# D-0007-009: Model Ownership

## Objective

Assign ownership and visibility for the first definition-to-execution models.

## Scope and exclusions

Definition, schema, expression, descriptor, bound-plan, failure, and
Service-boundary models. Distinguish private representations, internal
cross-layer contracts, and supported public APIs. No speculative class catalogue.

## Questions to resolve

Which layer owns each responsibility? Which values actually cross adjacent
boundaries, and which public authoring/Service contracts are necessary?

## Acceptance criteria

- [ ] Persistent ownership/dependency map covers each listed model family.
- [ ] Public/internal/private boundaries preserve SPEC-0006's call graph.
- [ ] Representatives support the first retrieval, generator, and parsing slices.
- [ ] Any architectural exception has an accepted authoritative decision.
- [ ] Checks pass and human review covers exact ownership decisions.

## Resolution

Unresolved. Record decisions in SPEC-0006 or an ADR; update artifact paths if an
ADR is selected. Do not decide CLR types in the portable mapping requirements.

## Validation and review

Existing layered architecture is a source prerequisite, not inferred completion
of this refinement.
