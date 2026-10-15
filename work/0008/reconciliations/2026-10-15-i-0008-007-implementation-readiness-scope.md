---
spec: SPEC-0008
process_version: 1
sources:
  - path: work/0008/readiness/trace-checker.md
    revision: 9baae4207ab6930ed144ef4c970eb1cb6658439e
    content_sha256: 45be6669c48ebb6bb21dfd755ce50528a304aadc4d86f17b90f4a048ac644441
    material_sha256: 87965089fa7ce0ff77f4c7090f7be45e73afd93c2ce77f38a7d33fa8d21f9249
  - path: work/0008/plan.md
    revision: bc64ea0128052fce377772dce87ca0d961a56c2b
    content_sha256: 049e35381b904042f6fc4934bd72fb723d1ef5c2ae768d4f80781a7bbdce426d
    material_sha256: df9435cef8e584ec0ab2d05d7befde76dca0f6531d3c1feececd841e829d7852
  - path: work/0008/implementation/I-0008-007-trace-checker.md
    revision: c4cb62ffda867c83a53e7c621892a3db23f36f61
    content_sha256: bf890e6109e4da5a2c2f6efe1febb22dff83abf312ba21d95609bcf85293db58
    material_sha256: cd7b3bfe9db31dfbe2dfb8ce63e0e15d2dc4cd66ddd680842378496782202a9e
---

# I-0008-007 Implementation-Readiness Scope Reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md) | [Trace-checker milestone](../implementation/I-0008-007-trace-checker.md) | [Planning-only readiness](../readiness/trace-checker.md)

- Baseline: I-0008-007 was an open milestone with no plan approval. Its
  `planning_readiness_scope` selected `trace-checker`, but the matching
  approved readiness record declared `authorizes: planning`; the milestone's
  entry gate required implementation readiness before concrete slices could
  be planned.
- Reconciliation: preserve the existing gate and identify its required
  authorization level explicitly. I-0008-007 now selects the distinct
  `trace-checker-implementation` scope. Current, approved implementation
  readiness for that scope is required before slice planning. The earlier
  `trace-checker` planning-only approval is not carried forward as
  implementation readiness. Each concrete slice still requires separate
  current implementation readiness covering its exact manifest and
  specification edits before plan approval or execution.
- Readiness impact: changing the milestone's material source makes
  `work/0008/readiness/trace-checker.md` stale for its recorded source snapshot.
  Its previous approval remains historical evidence for the former
  planning-only material and does not satisfy the new implementation-readiness
  scope. Reassess `trace-checker-implementation` against current sources and
  require explicit approval before creating slices.
- Dependency impact: no item IDs, dependencies, phase membership, requirement
  coverage, or child-slice relationships changed. No plan-approval evidence
  existed for I-0008-007, so no plan approval was carried forward or revoked.
- Blocker: the new implementation-readiness assessment and its explicit
  approval remain outstanding. No concrete slice planning or implementation
  is authorized by this reconciliation.
- Reconciliation is complete for the milestone's readiness-scope mapping.
  The implementation-readiness assessment remains an open gate.
