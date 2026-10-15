# D-0008-015 common-library ownership reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. The user selected a common source workspace for portable
  validation libraries, with language-specific `src/` and `tests/` trees.
  SPEC-0006 R-0006-024 and R-0006-041 and SPEC-0008 R-0008-001 through
  R-0008-003, R-0008-019, and R-0008-027 are amended; SPEC.md R-0000-019 and
  R-0000-020 now identify the common .NET paths and category.
- D-0007-012's prior approval remains historical and unchanged. Its
  post-approval note records the location supersession; algorithm ownership,
  assembly identity, permitted consumers, and distribution remain unchanged.
- I-0007-001, I-0007-007, and I-0007-008 now identify common-project
  ownership, tests, architecture checks, and the prerequisite decision
  D-0008-015. Their implementation milestones remain open and unapproved.
- Source reconciliation updates the exact working-copy hashes and records
  committed baseline `7178f84c93d8393c30a5a5cf57f3c923d36274fc` for SPEC.md,
  SPEC-0006, SPEC-0008, .NET conventions, and the applicable .NET path
  instruction. The committed blobs were verified against their prior
  snapshot hashes before advancing the baselines. No SPEC-0007 requirement or
  behavior changed.
- No implementation, common workspace, readiness approval, or package is
  created. The build-and-test skill and remaining path consumers stay assigned
  to the approved migration work after the target workspaces exist.
- Validation and exact-snapshot evidence are recorded in D-0008-015. This
  reconciliation does not approve that decision or any implementation work.
