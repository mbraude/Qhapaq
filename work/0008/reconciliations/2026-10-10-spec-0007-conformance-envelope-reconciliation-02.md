# SPEC-0007 conformance-envelope reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. D-0008-014 resolved the policy/checker delivery boundary
  under existing R-0008-016 and R-0008-017. Policy authoring and placement
  definitions belong to I-0008-001 and may be delivered without claiming
  traceability support. I-0008-007 owns extractor registration and evidence
  that registrations match the approved policies; it now depends on I-0008-001.
  The support condition remains unchanged: both policy placements and a
  matching registered extractor are required. The milestones remain separate;
  executable child slices are deferred to implementation planning after scoped
  readiness. No specification or ADR change was needed, and no tool ownership
  or implementation technology was selected.
- Readiness impact: the engineering-policy readiness record remains historical
  and stale; reassess it against the resolved boundary and current milestone
  snapshots before implementation planning. No readiness or implementation
  approval is inferred.
- Reconciliation is bounded to D-0008-014 and I-0008-001/I-0008-007. Phase
  membership and all other work items remain unchanged. D-0008-014 and its
  affected milestones are prepared for exact-snapshot review; no implementation
  or language-support claim is authorized.
- Validation: all 12 plan source hashes match current bytes; all 74 repository
  work-item IDs are unique, dependencies resolve, and the graph is acyclic.
  Relative Markdown links in the four changed files resolve and `git diff
  --check` passes. The specification trace check passes as maintenance; only
  planning/work-item documentation changed, with no requirement block, code,
  or test edits. Exact review inputs and outputs are recorded in D-0008-014.
