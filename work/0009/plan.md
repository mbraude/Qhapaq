---
spec: SPEC-0009
process_version: 1
sources:
  - path: specs/0009-repository-validation-derived-state.md
    revision: f6ba2d2eb8a306f0f0794b0804cbe2a302443d54
    content_sha256: 59a20f67e18d9ed1653a301919d7ad2eeb047e80e35630789377dba2ec2f6d1b
  - path: .agents/skills/spec-trace-check/SKILL.md
    revision: 07d7b41d910f9dc7a65fea1cb05fb4c62bf6e7cb
    content_sha256: 4aa125b6bd3bd6738668a3aa99ef4fd18b3ceb385d634d2e6dc0ea5bf2adc7bd
  - path: .agents/skills/work-runbook-sync/SKILL.md
    revision: null
    content_sha256: e4e1e45d12d677411a36df48d8f14a5be9e33bcc533e111407a12789f6492033
  - path: .agents/skills/work-next/SKILL.md
    revision: null
    content_sha256: ac9074ed72923e20ad4754aa752847f3e55caec4bb20c73a90aee946d10e1400
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 71bf914cd8edf48b6af94544c342c4ad2c906929
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 77cbd9e62a3a5c512f6d4a86fb6a024220a58f3a
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825
  - path: docs/development/spec-driven-workflow.md
    revision: b627023baef4d16d8c1c3598b24ba9d66f9e96bb
    content_sha256: da0d7ea110236bddcebc9607b435721ecf53d00dff7694a2f43a402f819b3ea2
  - path: docs/development/coding-conventions.md
    revision: a3242861598a02c89ffabfb047130d4dd4290127
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: tools/README.md
    revision: e20a65c7b1652c62408f7505119e644d7a4383aa
    content_sha256: fe502e9664f68d7f6e3eb362a952c217c77b4801e80cab7752f8b09daa91222f
  - path: AGENTS.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: work/0008/implementation/I-0008-007-trace-checker.md
    revision: 657026c88467af20fb02b803a3db6f495ef6ddf7
    content_sha256: 74379cffa236025bf9057c684896fde61f135100a6cbc921d9c334ac89dcd4d7
  - path: work/0008/implementation/I-0008-009-migration-validation-orchestration.md
    revision: e8416b6ea141479efa7245db5b8c9bebf3270221
    content_sha256: 5ddf346996d284a536a2c7b3506045d2e6c4dcc4b26d299f9e2e411086424f6f
---

# SPEC-0009: Work Plan

## Scope and authority

This plan delivers
[SPEC-0009](../../specs/0009-repository-validation-derived-state.md)
without changing the requirements or completion gates of SPEC-0007 or
SPEC-0008. SPEC-0009 owns non-authoritative derived validation state, exact
content and rule-version identity, cached and uncached equivalence, explicit
invalidation, shared exact-byte digest reuse, independent required validation,
safe lifecycle behavior, complete runbook freshness, cached command selection,
incremental dependency invalidation, refresh collapsing, and exact-identity
validation receipts.

SPEC-0008 continues to own deterministic trace-checker semantics and
registration. This plan consumes its checker outcome through an external
prerequisite and introduces no reverse dependency. Exact tool ownership,
implementation technology, persistent representation, concurrency strategy,
and command integration require an ADR before executable implementation
planning.

## Phase 0: Architecture

### Entry gates

SPEC-0009 is reviewed as the governing draft. R-0009-001 through R-0009-014
bound the decision without selecting an implementation implicitly.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0009-001](decisions/D-0009-001-derived-state-tool-architecture.md) | Select repository-tool ownership, implementation boundary, storage, concurrency, and command integration in an ADR. |

### Exit gates

D-0009-001 is complete and explicitly approved for an exact snapshot. The
resulting ADR resolves every consequential implementation choice needed for
scoped readiness and implementation planning without changing SPEC-0008.

## Phase 1: Incremental validation foundation

### Entry gates

D-0009-001 is complete. I-0008-007 has delivered the deterministic validation
behavior that incremental state accelerates. Scoped readiness and concrete
implementation slices are separately approved.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0009-001](implementation/I-0009-001-derived-state-foundation.md) | Deliver exact-identity indexing, cache lifecycle, equivalence, diagnostics, and recovery. |

### Exit gates

The derived-state foundation satisfies R-0009-001 through R-0009-005 and
R-0009-008 through R-0009-011, passes cached-versus-uncached equivalence,
manifest-freshness, and corruption tests, and has explicit delivery review.

## Phase 2: Workflow adoption and required validation

### Entry gates

I-0009-001 is complete. Each consuming workflow has current readiness and an
approved concrete slice. Required CI integration additionally waits for the
root validation orchestration owned by I-0008-009.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0009-002](implementation/I-0009-002-workflow-digest-adoption.md) | Migrate fingerprint, reverse-index, and exact-byte digest consumers to the central interface without changing workflow semantics. |
| 2 | [I-0009-003](implementation/I-0009-003-independent-validation-integration.md) | Add clean-state or fully verified required-validation use and recovery evidence. |

### Exit gates

Repository workflows preserve exact snapshot, approval, and traceability
semantics while reusing eligible results. Stored next commands require complete
freshness, incremental invalidation covers all dependents, composed mutations
end with one current runbook, and validation receipts bind complete identities.
Required validation remains independently reproducible and does not accept
unverified local state.

## External prerequisites

- [I-0008-007](../0008/implementation/I-0008-007-trace-checker.md) delivers the
  deterministic trace checker before I-0009-001.
- [I-0008-009](../0008/implementation/I-0008-009-migration-validation-orchestration.md)
  delivers root validation orchestration before I-0009-003 integrates required
  CI verification.

These dependencies point only from SPEC-0009 to SPEC-0008. Neither prerequisite
depends on this plan, and no SPEC-0007 or SPEC-0008 completion gate is changed.

## Reconciliation evidence

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
- Date: 2026-10-12. Bootstrapped from the new uncommitted SPEC-0009 draft and
  the exact current supporting sources recorded above.
- The SPEC-0009 source record uses `revision: null` because the new draft has no
  committed baseline. Its `content_sha256` records the exact reviewed
  working-copy bytes used for this plan.
- Created one open architectural decision and three future implementation
  milestones. No implementation slice is executable, no readiness or plan is
  approved, and no production or validation tool is changed.
- Existing SPEC-0007 and SPEC-0008 specifications, plans, items, readiness
  records, and approvals are unchanged. The pre-existing modification to
  `work/0008/runbook.md` is unrelated and was preserved.
- Reconciliation is complete for the initial draft. Human review of the exact
  specification and plan snapshots is the next gate.
