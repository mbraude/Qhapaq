# Source and workflow reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-13. Reviewed the workflow-guide changes since the recorded
  source snapshot. The added `material_sha256` rule distinguishes work-item
  material changes from lifecycle/review-evidence changes when judging source
  currentness and readiness impact. It changes workflow interpretation, not
  SPEC-0008 requirements, item outcomes, phase membership, or dependency
  edges. The prior plan discussion already preserves approvals at their exact
  reviewed snapshots; this update records the current guide bytes without
  renewing any plan or readiness approval. Existing readiness records that
  cite older guide, plan, or item snapshots remain subject to separate
  reassessment before they can support eligibility. The updated source
  baseline is `da70a0e303f4ff75ee095168d670d709ba3c1afe`.
