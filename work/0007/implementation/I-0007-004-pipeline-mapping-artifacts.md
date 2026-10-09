---
id: I-0007-004
kind: implementation
granularity: milestone
change_kind: requirement
title: Pipeline, mapping, scope and normalization artifact family
status: open
spec: SPEC-0007
requirements: [R-0007-343, R-0007-347]
depends_on: [D-0007-002, D-0007-015]
artifacts: [schemas, conformance]
---

# I-0007-004: Pipeline and Mapping Artifacts

## Objective and coverage

Publish pipeline schema and embedded self-contained mapping definitions; valid/
invalid documents; mapping parsing/inference/evaluation/failure and all selected
operator groups; mixed-version/patch preservation; scope/dominance; exact-default
normalization and definition identity vectors.

## Entry gates

The selected mapping set satisfies R-0007-340/343 through D-0007-001/002.
Previously completed decisions remain in Git history; actual vectors and scoped
readiness still require evidence. Applicable profile/diagnostic artifacts are
I-0007-005.

## File and ownership manifest

Pending exact version/path selection during slice planning.

## Design and integration

No .NET-dependent semantics, implicit mapping migration, or pre-normalization
canonical identity. Include regex and object groups as well as older helpers.

## Tests and validation

Cover every selected capability's shapes, inference, failures, order, missing/null,
budgets, and boundaries; shared tooling is I-0007-002.

## Exit criteria

- [ ] All listed artifacts and portable expected results are published.
- [ ] R-0007-343 closure/publication gates, checks, and human review are satisfied.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No pipeline/mapping schema or vector publication claimed by extraction.
