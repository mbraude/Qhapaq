---
id: D-0007-002
kind: decision
title: Audit and close the complete v1 mapping operator set
status: open
spec: SPEC-0007
requirements: [R-0007-340, R-0007-341, R-0007-342, R-0007-343]
depends_on: [D-0007-001]
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-002: Mapping Completeness

## Objective

Close the reopened operator set and audit all capability-completeness
dimensions in R-0007-340 without creating duplicate work for the same gate.

## Scope and exclusions

All selected v1 mapping capabilities, including existing collection, string,
regex, object, and newly decided numeric operators. Conformance expectations
must be complete; publishing their actual artifact families remains Phase 1.

## Questions to resolve

Which operators lack any closed shape, typing, missing/null, failure, deterministic
evaluation, portable accounting, or conformance requirement? Are all cross-cutting
tables and examples mutually consistent? Does any unresolved candidate remain?

## Acceptance criteria

- [ ] Audit each operator against every closure dimension in R-0007-340.
- [ ] Resolve gaps in authoritative requirements, not only in this item.
- [ ] Reconcile operand tables, inference, budgets, examples, and conformance groups.
- [ ] Account for all selected/rejected capabilities and R-0007-343's version gate.
- [ ] Traceability and relevant checks pass; explicit human review is recorded.

## Resolution

Unresolved. Depends on numeric closure; full completeness requires the current
operator audit, not predecessor status alone. Earlier decisions can be reviewed
through Git history without a retrospective work-item gate.

## Validation and review

No completeness assessment or approval performed during extraction.
