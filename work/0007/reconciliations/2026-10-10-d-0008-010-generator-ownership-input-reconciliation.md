# D-0008-010 generator-ownership input reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. SPEC-0008 at committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` is now an explicit cross-plan
  source. Its source record hashes the reviewed working-copy bytes containing
  R-0008-019; it does not claim those bytes are committed or approved.
- R-0008-019 assigns the independently versioned Roslyn generator package to
  the .NET implementation workspace as build tooling and prohibits generator
  or private tooling dependencies from entering runtime dependency closures.
- D-0007-012 now depends on D-0008-010 and covers R-0008-019 while retaining
  ownership of the exact generator/runtime algorithm-reuse, assembly, package,
  and architecture-enforcement decisions. I-0007-008 now depends on both
  decisions and records the accepted workspace ownership while leaving its
  exact project, package, API, shared-library, and test manifests pending.
- No SPEC-0007 requirement, phase, implementation artifact, runtime dependency,
  package, workspace, or readiness state changes. This reconciliation resolves
  no SPEC-0007 decision and does not approve D-0008-010 or authorize generator
  implementation.
