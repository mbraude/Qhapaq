---
id: D-0007-001
kind: decision
title: Numeric helpers and array reductions
status: open
spec: SPEC-0007
requirements: [R-0007-340, R-0007-341, R-0007-343, R-0007-108, R-0007-167]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-001: Numeric Helpers and Array Reductions

## Objective

Resolve the numeric capabilities identified by R-0007-340 and Section 8.12.

## Scope and exclusions

Decide purpose-built v1 scalar helpers and array reductions within the existing
portable numeric domain. No general reducer, interpreter, executable code, or
implicit future-version deferral. Read the existing arithmetic, inference,
evaluation, and accounting requirements before choosing semantics.

## Questions to resolve

- Which absolute, minimum, maximum, clamp, and rounding operations belong in v1?
- What are their closed operands, domain restrictions, and exact rounding modes?
- Are sum, minimum, maximum, and average reductions supported? What happens for
  empty arrays, accumulation order, intermediate rounding, and overflow?
- How do missing/null, static inference, evaluation order, failure, and resource
  accounting interact with every selected operator?

## Acceptance criteria

- [ ] Record included and rejected candidates explicitly in normative requirements.
- [ ] Define closed shapes, typing, missing/null, order, failures, and budgets.
- [ ] Define exact numeric and rounding behavior, including reduction boundaries.
- [ ] Define required language-neutral conformance cases and consistent examples.
- [ ] Preserve R-0007-343 publication gates; do not publish schemas prematurely.
- [ ] Traceability and relevant checks pass; human review covers the exact outcome.

## Resolution

Unresolved. Resulting requirement IDs will be added here, not duplicate semantics.
The cross-operator audit is [D-0007-002](D-0007-002-mapping-completeness.md).

## Validation and review

Bootstrap evidence: this checkpoint is unchecked in the specification at the
plan's baseline. The legacy checklist has since been removed; this item owns
remaining work. No resolution, execution, or human approval is claimed.
