# D-0007-014 DI lifetime and state ownership reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-12. The user selected lifecycle/ownership policy and deferred
  concrete Microsoft DI registrations to reviewed implementation slices.
  [D-0007-014](decisions/D-0007-014-di-lifetimes.md) records the decision in
  the .NET conventions. It covers immutable registry generations, per-run
  scope ownership, derived-plan cache/disposal boundaries, and protected
  credential-cache ownership, aligned with the referenced SPEC-0002, SPEC-0004,
  SPEC-0006, and SPEC-0007 requirements.
- The source snapshot now includes SPEC-0004, ADR-0001, and the documentation
  conventions used for this decision. The .NET convention source baseline
  remains `7178f84c93d8393c30a5a5cf57f3c923d36274fc`; its exact reviewed
  working-copy SHA-256 is updated above.
- I-0007-001 directly depends on D-0007-014, so its architecture-test
  expectations inherit these rules. Related implementation milestones already
  depend transitively on I-0007-001 or its descendants; no new dependency edge,
  phase membership, or scope is needed.
- No product requirement changes. No implementation, readiness approval,
  package, or publication is created. Existing approvals for earlier exact
  SPEC-0008 policy outputs remain historical; their snapshots are not revised
  or reapproved by this decision.
