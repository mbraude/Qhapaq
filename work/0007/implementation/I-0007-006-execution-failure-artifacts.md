---
id: I-0007-006
kind: implementation
granularity: milestone
change_kind: requirement
title: Runtime failure and structural execution artifact family
status: open
spec: SPEC-0007
requirements: [R-0007-347, R-0007-304, R-0007-307]
depends_on: [D-0007-015]
artifacts: [schemas, conformance]
---

# I-0007-006: Execution and Failure Artifacts

## Objective and coverage

Publish runtime failure and caught-failure projection schemas, catchability,
aggregate dispositions, effect outcomes, bounded recovery causality, and execution
semantics for every structural node.

## Entry gates

Relevant normative decisions and readiness; actual mapping artifacts I-0007-004
are required for cases that exercise mapping. Independent failures can publish earlier.

## File and ownership manifest

Pending exact versioned artifacts and capability groups during slice planning.

## Design and integration

Runtime failures are not validation diagnostics. Preserve non-durable execution,
no rollback, no partial-success results, lexical scope and private frame rules.

## Tests and validation

Versioned portable failure, cancellation, concurrency, nested control-flow,
isolation, resource-limit, and adverse-path results; consume with I-0007-002.

## Exit criteria

- [ ] Required schemas and complete per-node vector groups exist with results.
- [ ] Relevant checks and exact-snapshot human review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No failure/runner conformance suite delivered during extraction.
