# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Bootstrapped on branch `master` at baseline commit
  `c1580148ae7d6230bfef6441d2e419fd71974470`; the worktree was clean.
- No SPEC-0006 plan previously existed. The specification's two open questions
  about the first Service V1 use case and its request/result/error shapes are
  answered by SPEC-0007 D-0007-004 and R-0007-404 through R-0007-410. They
  were textually open in SPEC-0006 at bootstrap. I-0006-001 has since aligned
  Sections 13 and 15 with those completed decisions and is complete after
  explicit delivery approval.
- SPEC-0006 R-0006-033 overlaps work assigned to SPEC-0007 I-0007-001 and
  I-0007-011 and SPEC-0008 I-0008-008 and I-0008-004. Those items remain
  externally owned; I-0006-002 is an aggregate acceptance milestone rather
  than a duplicate implementation manifest.
- The SPEC-0006 source was reviewed against its committed baseline
  `71bf914cd8edf48b6af94544c342c4ad2c906929`. Its working-copy changes are
  limited to I-0006-001's Section 13 rollout references and Section 15
  resolved-use-case wording; all 41 requirement blocks and identifiers remain
  unchanged. The source record retains that committed baseline revision and
  records the reviewed working-copy bytes.
- I-0006-001 keeps its approved planned `change_kind: editorial`. Trace
  review verified the diff as `maintenance` because no requirement block
  changed; the commit uses that trailer, and the difference is recorded in
  delivery evidence without editing the approved plan snapshot.
- The approved `service-v1-reconciliation` readiness remains scoped to
  R-0006-004, R-0006-005, and R-0006-033 and the unchanged documentation
  outcome. Its source records predate the delivered SPEC-0006 text; this
  reconciliation does not extend that readiness to runtime implementation,
  I-0006-002, or broader SPEC-0006 work. Reconcile sources and reassess
  readiness before later scopes.
- All other recorded source snapshots match their current exact bytes.
  I-0006-002 remains a non-executable milestone pending later decomposition,
  current scoped readiness, and exact plan approval. No dependencies or phase
  membership changed.
- Reconciliation is complete for the reviewed current SPEC-0006 snapshot.
- `docs/development/spec-driven-workflow.md` gained the immutable
  approved-snapshot rule. The source record keeps its committed baseline
  revision and records the working-copy bytes. The rule changes no item scope,
  dependency, or readiness conclusion in this plan.
