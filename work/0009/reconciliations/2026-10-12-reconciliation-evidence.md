# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-12. Reconciled SPEC-0009 version 0.2, which adds complete
  runbook input manifests, conditional reuse of stored next commands,
  incremental dependency invalidation, final-refresh collapsing, and
  exact-identity validation receipts in R-0009-011 through R-0009-014.
- D-0009-001 now resolves the additional architecture questions. I-0009-001
  owns the runbook freshness manifest foundation; I-0009-002 owns workflow
  adoption, targeted preflight, incremental invalidation, refresh collapsing,
  and local receipt reuse; I-0009-003 includes required-validation receipt
  verification. No new dependency points from SPEC-0007 or SPEC-0008 to this
  plan.
- Recorded the current working-copy bytes of the three directly related skills.
  Their immediate changes retain fingerprint maps, input bytes, parsed fields,
  and digests only within one invocation; use the freshly synchronized next
  command without re-deriving global order; and strengthen the existing
  meaningful-content no-op. They create no persistent cache, skip no freshness
  check, and trust no prior runbook.
- Existing SPEC-0007 and SPEC-0008 specifications, plans, items, readiness
  records, and approvals remain unchanged. The pre-existing modifications to
  `work/0008/runbook.md` and its new language-contract readiness record are
  unrelated and were preserved.
- Reconciliation is complete for this amendment. Human review of the exact
  specification, plan, work-item, and skill snapshots is the next gate.
