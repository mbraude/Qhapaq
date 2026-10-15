# Source and workflow reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-14. Reconciled the reviewed I-0008-016 editorial audit outputs.
  SPEC-0006 and SPEC-0008 now label retained examples according to
  R-0008-005; the specification-authoring guidance links to that rule and
  uses its exact labels. The edits preserve .NET contract boundaries and
  conformance meaning. Changed requirement fingerprints and reverse-impact
  evidence are recorded in I-0008-016; no active product-code or test
  references were found stale. Historical fingerprints in completed decision
  validation evidence remain tied to those decisions' reviewed snapshots.
- Refreshed only the three reviewed source records:
  `specs/0006-dotnet-layered-architecture.md` at baseline revision
  `ff91861578d0d4368836d05d1039bbd93fca4efa`, working-copy SHA-256
  `7e8b252a96cbfef18eaa92d7d742234a626dfbf2758dbbdd63feac055925f58a`;
  `specs/0008-multi-language-conformance-and-repository-organization.md` at
  baseline revision `71bf914cd8edf48b6af94544c342c4ad2c906929`, working-copy
  SHA-256 `51566da6fc6521022146426661004112ee133e3600656a68a59c71e4f040c779`;
  and `docs/development/conventions/specifications.md` at baseline revision
  `911ede5a759d7288dc569002ab2bbb136caeb52d`, working-copy SHA-256
  `cedd8481133460d1a2f8ad1ed5d7c02d1981d83c837cda88b13c18d1b7fd19f8`.
  No item scope, requirement coverage, dependency, phase membership, or
  aggregate gate changed. The plan material hash remains
  `6a79348b7686002e8a03592ef3a76b50e737a5cdb03e5e6f24dee8a0485a9890`.
- I-0008-016's readiness record is stale against the changed specification and
  guidance sources and its changed item material; reassess and approve that
  exact implementation scope before relying on it. Its recorded plan approval
  also predates the checked acceptance criteria: current item material is
  `798f810a11b98d61cea36ed0ceb2b07885e1d2f42c8f3891596bdd2df5fb4fd8`,
  rather than the approved `2060cb93df653a8ba3d042366b97e7c3d436c8a04266af97e6de709acbafd3da`.
  Do not treat that plan approval as current; renew approval for the exact
  implementation plan after readiness is current and approved. The source
  reconciliation does not renew either approval or approve delivery.
- The final `/spec-trace-check` result is `PASS with warnings`: the
  implementation namespace in SPEC-0006 R-0006-004 and the illustrative
  language-specific C# example in SPEC-0008 are implementation-specific
  content explicitly permitted by R-0008-005. No mechanical errors, semantic
  errors, or new waivers were reported. The complete judgment and proposed
  trailers are recorded in I-0008-016's delivery evidence.
