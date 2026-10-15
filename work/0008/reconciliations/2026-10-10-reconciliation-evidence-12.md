# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. D-0008-010 drafted responsibility-based artifact ownership
  and dependency directions in R-0008-019. The .NET implementation workspace
  owns the independently versioned Roslyn generator package as build tooling;
  product integrations and maintained contributor tools remain separate
  workspaces even when written in .NET; and private outputs or accidental
  runtime dependencies do not cross those boundaries.
- Downstream impact: D-0008-011 now depends on D-0008-010 and covers
  R-0008-019 when defining workspace orchestration. D-0008-012 and I-0008-004
  through I-0008-006 cover the ownership requirement for migration, dependent
  consumer updates, and future real workspaces. The SPEC-0007 D-0007-012 and
  I-0007-008 items now treat R-0008-019 and D-0008-010 as inputs while
  retaining their separate shared-algorithm, package-boundary, implementation,
  and test decisions.
- Source baseline: SPEC-0008 uses committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` and exact reviewed working-copy
  byte hash
  `433b67c0cb12370756258192e57f5e42298eb7f8879160966cc3d52734f4cbbc`.
  Other authoritative source bytes and records remain unchanged.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-010 snapshot, resolve D-0007-012, create or relocate a workspace,
  select an integration platform, implement or package the generator, or
  authorize implementation. Reconciliation is complete for D-0008-010 and its
  affected downstream work.
