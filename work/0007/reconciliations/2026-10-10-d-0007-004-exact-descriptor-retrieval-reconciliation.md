# D-0007-004 exact descriptor-retrieval reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. Baseline
  `07073fe16ae1b6f64feaeedb01557d6f5b9731fd` supplies the committed
  SPEC-0007 input. The source record hashes the current working-copy bytes
  containing D-0007-004's accepted contract decisions; it does not claim those
  bytes are committed. SPEC-0002 is now an explicit source because effective
  registry construction and disclosure policy govern this use case.
- New R-0007-404 through R-0007-410 define the exact Service selector and
  response, indistinguishable absent/non-disclosable result, digest
  precondition, structured errors, `qhapaq operation get` grammar and output,
  stable exit statuses, adjacent-layer/non-executing boundaries, and
  language-neutral conformance coverage.
- D-0007-004 is the only decision resolved by this reconciliation. I-0007-011
  now references the exact requirements it must implement. D-0007-005 remains
  open for subsequent CLI and MCP contracts and retains its existing
  dependencies. No item or dependency is added, removed, split, or cancelled.
- The change creates no implementation, schema, vector, registry, policy,
  descriptor publication, execution or payload-disclosure authority, or
  readiness approval. I-0007-011 remains a milestone that requires concrete
  implementation planning and all existing prerequisites.
- Validation and exact ready-for-review snapshots remain to be recorded in
  D-0007-004. This reconciliation is not human approval, completion,
  implementation, publication, or permission to execute.
