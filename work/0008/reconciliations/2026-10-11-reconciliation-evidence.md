# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Synchronized the SPEC-0008 planning inputs after the
  conformance-artifact readiness assessment found stale source hashes and
  incomplete requirement/dependency coverage. Refreshed the plan's source
  records for the fully reviewed current inputs; the inventory now includes
  SPEC-0005, SPEC-0006, SPEC-0007, SPEC-0008, repository policy, templates,
  and the owned SPEC-0007 plans/items consumed by this scope.
- Baseline: `8a534afd2e4a4cbd28e30de6e115967977862727`. Reviewed changed source
  text against the recorded committed baselines and current working-copy bytes.
  The plan now records 17 authoritative input snapshots; this excludes the
  plan itself and generated views.
- Extended I-0008-012 and I-0008-003 coverage to applicable SPEC-0005
  release/recovery, SPEC-0006 .NET layer and validation, SPEC-0007 portable
  validation, and SPEC-0008 ownership, orchestration, publication, and
  migration requirements. Added the completed SPEC-0007 and SPEC-0008
  decisions governing ownership, orchestration, sequencing, and architecture
  as explicit prerequisites; the actual I-0007-002 and I-0007-005 outputs
  remain execution prerequisites, not completed artifacts.
- I-0008-003 now records its .NET ownership boundaries, protected release
  responsibilities, exact-snapshot validation, recovery evidence, and the
  requirement-specific dedicated-branch gate for migration work. These
  constraints do not make branches mandatory for unrelated work.
- The existing conformance-artifact readiness assessment is a pre-sync,
  blocked snapshot and is not renewed by these planning edits. A fresh
  assessment against the reconciled requirements and inputs is required
  before plan approval or implementation. No requirement was amended, no
  item was approved or executed, and no conformance artifact was produced.
- I-0008-012 and I-0008-003 remain open, unapproved milestones. I-0007-002 and
  I-0007-005 remain open and their required outputs are not present, so
  conformance artifact delivery remains blocked pending those outputs and
  approved, executable child planning.
- Validation: all 17 recorded source hashes match exact current bytes and each
  recorded full revision contains its source path; all 77 work-item IDs are
  unique, dependency references resolve, and the combined graph is acyclic.
  All 30 requirement references in each affected item resolve and prior
  requirement coverage is retained. Local Markdown links, whitespace, and
  `git diff --check` pass. The combined dependency diagram was regenerated and
  its freshness check passes: 76 source files, 74 items, 208 dependencies, and
  22 cross-specification edges. Specification trace check was not run for this
  synchronization; the anticipated `maintenance` classification and absence
  of applicable `Spec:` trailers remain unverified.
