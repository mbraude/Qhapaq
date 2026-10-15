# SPEC-0007 conformance-envelope reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. D-0008-015 amends the repository taxonomy and dependency
  boundary to support language-specific common-library workspaces with
  separate source and test trees. The shared portable-validation project is
  assigned to `src/common/dotnet/`; the .NET implementation and generator
  remain in the implementation workspace. SPEC.md, SPEC-0006, and SPEC-0008
  are reconciled together because the root path map, .NET project plan, and
  repository taxonomy all govern this ownership.
- D-0008-015 is added to Phase 0 with prerequisites D-0008-001, D-0008-010,
  D-0008-012, and D-0007-012. I-0008-004 now depends on D-0008-015 and includes
  the shared library move; I-0008-005 explicitly includes both workspaces and
  build-skill consumer updates. No existing milestone is approved or completed.
- No existing migration-readiness approval covers this new workspace or move.
  The engineering-policy readiness evidence remains limited to its former
  scope; reassess migration readiness against concrete move and consumer
  manifests before implementation. The build-and-test skill is deliberately
  unchanged until the target workspaces exist.
- Exact source hashes for SPEC.md, SPEC-0006, SPEC-0008, the .NET conventions,
  and the .NET path instruction are refreshed to the reviewed working copies
  in this plan's source list. Their committed baselines are advanced to
  pre-change HEAD
  `7178f84c93d8393c30a5a5cf57f3c923d36274fc` after verifying the blobs match
  the prior source hashes. The impact review uses SPEC-0008 and the previously
  approved shared-library decision D-0007-012; D-0008-015 does not carry
  forward that approval.
- Validation and exact-snapshot evidence are recorded in D-0008-015. This plan
  reconciliation is not approval of the decision, migration, implementation,
  or any readiness record.
