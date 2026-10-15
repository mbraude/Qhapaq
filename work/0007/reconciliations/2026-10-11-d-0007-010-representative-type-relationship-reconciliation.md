# D-0007-010 representative type relationship reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Baseline: `8c63f2df1b8950fc0e283810e21e1d59db81f867`.
  The user selected separate, closed, layer-private node and expression
  variant families, with shared roots only for genuine common semantics.
- Added SPEC-0006 R-0006-040 to define composition-based recursion, separation
  of inert syntax from bound/compiled plan state, and the layer-private
  boundary. Exact CLR types and file organization remain for implementation
  planning; no code, schema, vector, or public contract changed.
- D-0007-010 now records the selected outcome and adds R-0006-040 to its
  governing requirements. I-0007-001 now includes R-0006-040 and specifies
  corresponding architecture-enforcement coverage. No other downstream
  item is revised: D-0007-012 concerns the independent generator/runtime
  dependency boundary, and I-0007-008 remains downstream of I-0007-001.
- No item identity, dependency edge, phase membership, or readiness approval
  changed. D-0007-010 still requires its checks and exact-snapshot review;
  this reconciliation does not mark it complete. I-0007-001 remains an
  unapproved milestone, and no implementation or publication eligibility is
  inferred.
- Source reconciliation is limited to the new SPEC-0006 requirement. Its
  working-copy SHA-256 is recorded in the source list above; the committed
  baseline revision is retained. The other SPEC-0007 source records remain
  unchanged. Existing references to R-0006-026 and fingerprints of existing
  requirement blocks are unaffected.
- Initial structure checks: all 16 SPEC-0007 source hashes match and their
  baseline revisions resolve; all 75 SPEC-0007/SPEC-0008 item IDs are unique,
  dependencies resolve, and the combined graph is acyclic. All three local
  Markdown links in the changed work items resolve. The exact comparison
  against HEAD preserves all 39 existing SPEC-0006 requirement fingerprints;
  R-0006-040 is the next identifier and fingerprints to `fca8f1`.
- Specification trace check: PASS with a warning for the implementation-
  specific .NET layer terminology in new R-0006-040. No prior references to
  the new requirement exist and no product code, tests, or waivers changed.
  The derived change kind is `requirement`, with `Spec: R-0006-040@fca8f1`.
  No build or unit tests apply to this specification and work-planning change.
