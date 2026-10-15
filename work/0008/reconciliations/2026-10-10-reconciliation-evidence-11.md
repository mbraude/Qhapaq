# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. D-0008-009 drafted the .NET **Entry Points** terminology
  and matched `Qhapaq.EntryPoints.<EntryPoint>` directory, project, assembly,
  root-namespace, and derived source-namespace identities across the affected
  SPEC-0006 architecture requirements. Executable filenames and distribution
  package IDs remain separate identities. SPEC-0008 records the resolved
  question, ADR-0001 uses the new hosting identity, and the architecture
  diagram and coding conventions remain consistent with the amended source.
- Downstream impact: new I-0008-008 owns the coordinated identity migration
  without conflating it with repository relocation. D-0008-012 now covers the
  rename's sequencing, compatibility validation, and recovery. I-0008-005
  depends on both the identity migration and source relocation before it closes
  remaining consumer updates. No existing item was cancelled, approved, or
  executed, and no implementation was changed.
- Source baseline: SPEC-0008 and the coding conventions use committed baseline
  `130919358da2c7c9918e0eff6caa82fd7bc9b44b`; SPEC-0006 uses
  `66c43b3d030e84a4ac055b6853946c401d7a9b8c`; and ADR-0001 uses
  `d3ff6bf9df744c63fc776775956ce41a907a5bcf`. Their exact reviewed
  working-copy SHA-256 values are respectively
  `3efd22dbdfea9783141fda61e8625340ea67224663b07ca63c32fb86155dba02`,
  `8cd098f3f9bd877ef9f1c77a77c4b1a895b28ae92ace65299ff05daa4a859b05`,
  `62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653`,
  and `f7855b81e87db15f89326d7a297cc983eb8ba1a4f250aed380a999e5f87de217`.
  Other source records remain unchanged because their bytes and impact are
  unchanged. Reconciliation is complete for D-0008-009 and its affected
  downstream work.
- Readiness remains not assessed. This reconciliation does not approve the
  D-0008-009 snapshot, rename projects or namespaces, move source, change
  package or executable identities, or authorize implementation.
