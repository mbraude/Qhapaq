# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-13. Detailed only I-0008-012 and decomposed the existing
  I-0008-003 conformance-artifact milestone into five executable slices while
  retaining I-0008-003 as the non-executable delivery aggregate. I-0008-017
  owns closed portable schemas; I-0008-018 owns the four candidate profile
  definitions and evidence matrices; I-0008-019 owns portable contract and
  lifecycle vectors; I-0008-020 owns adapters and immutable evidence in the
  existing .NET test workspaces; and I-0008-021 owns fail-closed protected
  publication integration.
- Every child has an exact repository file manifest, responsibility and
  visibility, governing requirements, entry and exit gates, tests or vectors,
  documented commands or an explicit command-resolution blocker, and required
  delivery/publication evidence. Portable schemas, profiles, and vectors stay
  under root `schemas/` and `conformance/`; .NET adapters stay in existing
  implementation test projects; root aggregation/publication stays in
  `build/`, `scripts/`, and `.github/workflows/`.
- I-0007-002 and I-0007-005 are true execution prerequisites only for
  I-0008-019, where their actual shared tooling and validation-foundation
  outputs are first consumed. Their milestone artifacts are not represented
  as delivered, and I-0008-019 plan approval is blocked until their child
  manifests and exact commands exist. I-0008-017 and I-0008-018 can deliver
  their independently governed contracts first.
- Refined I-0008-009 to depend on I-0008-020 rather than the I-0008-003
  aggregate. I-0008-021 then depends on I-0008-009 and I-0008-020, allowing
  protected publication to consume root manifest orchestration without a
  cycle. I-0008-003 depends on all five children. The combined SPEC-0007 and
  SPEC-0008 graph remains acyclic.
- The approved conformance-artifact readiness record included an older exact
  `work/0008/plan.md` byte snapshot. The intervening plan-only delta split the
  disjoint requirement/example audit scope and added its source inventory. A
  bounded impact review found no change to conformance requirements,
  decisions, milestones, dependencies, authoritative specification bytes, or
  readiness conclusions. The approved readiness remains applicable to
  planning I-0008-003 through I-0008-012; it does not approve any child plan
  or make a delivery slice executable.
- I-0008-003 still covers every former acceptance outcome. R-0008-027 is
  satisfied only when this aggregate completes as migration stage 2's
  conformance prerequisite. R-0008-028 and R-0008-029 do not apply to the
  current add/modify-only child manifests; adding a move or rename requires
  separate migration readiness, before/after validation, a dedicated branch,
  checkpoint, user-change preservation, and non-destructive recovery.
- No production artifact was created. I-0008-012 is ready for exact review;
  all executable child plan approvals remain absent. Validation covers current
  source hashes, requirement and dependency references, unique IDs, phase
  membership, exact manifests, parent acceptance coverage, cross-plan
  acyclicity, local links, whitespace, and specification traceability. No
  build or unit tests apply to this planning-only change.
