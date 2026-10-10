---
id: I-0007-024
kind: implementation
granularity: milestone
change_kind: requirement
title: Incremental Service, CLI, MCP and Mermaid authoring projections
status: open
spec: SPEC-0007
requirements: [R-0007-368, R-0007-400, R-0007-401, R-0007-402, R-0007-403, R-0007-411, R-0007-412, R-0007-414, R-0007-415, R-0007-416, R-0007-418, R-0007-419, R-0007-420, R-0007-421, R-0007-422, R-0007-423]
depends_on: [D-0007-005, D-0007-006, I-0007-011]
artifacts: [implementations/dotnet/src, implementations/dotnet/tests]
---

# I-0007-024: Authoring Projections

## Objective and coverage

Phase 8: remaining public authoring contracts; descriptor listing; early structural
conclusions; full four-conclusion validation; resolved dataflow/effect/prerequisite
explanation; deterministic Mermaid; conservative contract comparison;
capability introspection; bounded raw-document and catalog selectors; CLI/MCP.

## Entry gates

Common prerequisites are first Service slice and exact surface decisions.
Per-use-case gates remain explicit: listing needs Phases 3/3A; structural
validation Phase 4; full validation/explanation Phase 6B; comparison Phase 5A
and exact descriptors; Mermaid validated definitions and promised schema analysis.

## File and ownership manifest

Pending splitting by use case so each concrete slice gains exact prerequisite IDs.
Do not require the complete runner for non-executing projections.

## Design and integration

Adapters consume Service V1 only; no duplicate validation/policy/binding/projection
rules or access to Business/DAL/generator/manifest internals.

## Tests and validation

Versioned consumer/adapter tests, unavailable-conclusion cases, comparison vectors,
Mermaid goldens, catalog pagination, capability omission, exit-status/MCP
projection, cancellation, safe diagnostics and architecture checks.

## Exit criteria

- [ ] Each advertised authoring use case passes its genuine prerequisite gates.
- [ ] CLI/MCP/third-party behavior agrees; checks and human review pass.

## Plan approval

Absent; aggregate milestone, not an executable slice.

## Delivery evidence and review

No authoring surface added or advertised during extraction.
