# D-0007-013 test-artifact convention reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Baseline: `801b57722055b3d1dd85dc95eaad9d775fe37f74`.
  D-0007-013 is ready-for-review with its exact snapshot recorded in the item.
  It records .NET vector loading, golden
  maintenance, and clean package-consumer conventions under R-0007-346,
  R-0007-347, R-0006-031, and R-0001-072. Its selected loader copies canonical
  `conformance/` files into test output; consumer tests use temporary packed
  public packages. Acceptance checks pass; explicit human approval is pending.
  No product requirement, portable envelope, item identity, dependency, or
  implementation gate changed.
- The D-0007-015 impact review confirms its accepted portable envelope remains
  authoritative and unchanged: D-0007-013 keeps `expected` values in canonical
  vectors and does not introduce .NET-specific portable semantics. D-0007-015
  remains complete; its recorded D-0007-013 hash identifies its historical
  reviewed input and does not require reopening the decision.
- D-0007-013 remains the required decision prerequisite for downstream
  conformance tooling and I-0008-003. I-0007-002 and I-0007-005 remain open;
  this decision produces no tooling, vectors, publication, or readiness
  evidence.
