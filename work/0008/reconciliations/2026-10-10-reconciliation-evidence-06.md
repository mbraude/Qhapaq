# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. D-0008-004 drafted the initial profile boundaries in
  R-0008-006 and the corresponding claim restrictions in R-0008-007. The
  initial set is `qhapaq.runtime`, `qhapaq.cli.local`, `qhapaq.mcp.host`, and
  `qhapaq.dotnet.in-process`; each surface profile requires the portable runtime
  baseline. CLI and MCP are independent siblings, and remote-client profiles
  remain deferred.
- Downstream impact: D-0008-005 through D-0008-007 and D-0008-013 now reference
  the applicable profile or claim requirements while retaining their existing
  scopes and dependencies. I-0008-003 now covers R-0008-006 and R-0008-007 but
  remains a non-executable milestone blocked by the four downstream decisions,
  publication policy, readiness, and concrete slice planning. No item was
  created, cancelled, approved, or executed, and no dependency changed.
- Source baseline: SPEC-0008 uses committed baseline
  `d6cf2c053ee259d51f641da3c27cdbcea4a2c243` and exact reviewed working-copy
  byte hash
  `d1649a3335e0034049538af508b6c7712cfa4ae3d1271a3a5fa73edcf55f0915`.
  The unchanged SPEC.md, coding-conventions, and ADR-0003 byte snapshots now
  record their newer exact committed baselines; other source records remain
  unchanged because their bytes and provenance are unchanged.
- Readiness remains not assessed. This reconciliation does not approve
  D-0008-004, define profile versions or declaration and evidence formats,
  publish a profile or conformance claim, authorize remote clients, or alter
  implementation code. Earlier completed decisions remain unaffected.
