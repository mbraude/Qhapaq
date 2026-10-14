---
spec: SPEC-0010
process_version: 1
sources:
  - path: specs/0010-repository-work-run-orchestration.md
    revision: null
    content_sha256: abb20e024e4f1313a3f5ccc14d2ee93d7bf8d050e0f53c26bdd13b72090fb664
  - path: specs/0009-repository-validation-derived-state.md
    revision: 62cf5878eba2fb5e9674ea41c2aaacd0135949ce
    content_sha256: 59a20f67e18d9ed1653a301919d7ad2eeb047e80e35630789377dba2ec2f6d1b
  - path: specs/0003-product-evolution-roadmap.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 2b5fced51668b8bd2d586e377adbf667deabc3cb48c8569890ec7e709992ce32
  - path: docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825
---

# SPEC-0010: Work Plan

## Scope and authority

This plan tracks
[SPEC-0010](../../specs/0010-repository-work-run-orchestration.md), which
specifies resumable, policy-bounded orchestration of repository work runbooks.
It does not change `work-next`, workflow approval policy, or pipeline execution
durability. SPEC-0009 remains responsible for reusable derived validation
state and runbook freshness.

The first decision resolves run authorization, approval boundaries, recovery,
interface, and concurrency architecture. Implementation milestones remain
non-executable until the specification scope is reviewed, readiness is
assessed, and concrete slices are planned and approved.

## Phase 0: Resolve orchestration policy and architecture

### Entry gates

SPEC-0010 requirements R-0010-001 through R-0010-009 define the proposed
behavior. No implementation is authorized by this phase.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0010-001](decisions/D-0010-001-orchestration-policy-and-architecture.md) | Resolve delegated authorization, recovery, run state, interface, and concurrency decisions in an ADR. |

### Exit gates

D-0010-001 is complete and approved for an exact snapshot. Its ADR resolves
every consequential architecture choice needed for scoped readiness and
implementation planning without weakening the specification's stop,
authorization, and recovery boundaries.

## Phase 1: Deliver resumable serial orchestration

### Entry gates

D-0010-001 is complete. SPEC-0010 and the exact implementation scope are
approved, current scoped readiness and concrete plan approval exist, and the
existing work skills expose the required machine-readable outcomes.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0010-001](implementation/I-0010-001-resumable-serial-orchestration.md) | Run multiple authorized actions serially with durable progress, safe recovery, and explicit stop conditions. |

### Exit gates

Serial runs survive process interruption without trusting stale or uncertain
state, preserve all existing work-item and review semantics, and demonstrate
measurable reductions in repeated user interactions while retaining
`work-next` as the single-action fallback.

## Phase 2: Optional isolated concurrency and interaction surface

### Entry gates

I-0010-001 is complete. D-0010-001 explicitly selected the relevant optional
capability for delivery.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0010-002](implementation/I-0010-002-isolated-parallel-work.md) | Execute eligible independent actions concurrently in isolated worktrees without cross-item staging or commit contamination. |
| 2 | [I-0010-003](implementation/I-0010-003-run-management-interface.md) | Provide the selected command-based or graphical controls for run status, pause, resume, cancellation, and exact-snapshot review. |

### Exit gates

Only capabilities selected by D-0010-001 proceed to concrete planning.
Deferred capabilities are explicitly cancelled or retained as blocked future
work; no parallel mutation or graphical interface is implied by serial
orchestration approval.

## Related non-blocking work

[I-0009-001](../0009/implementation/I-0009-001-derived-state-foundation.md)
and [I-0009-002](../0009/implementation/I-0009-002-workflow-digest-adoption.md)
may provide reusable performance improvements. They are not prerequisites for
safe serial orchestration; SPEC-0010 must preserve SPEC-0009's authority and
verification rules whenever derived state is reused.

## Reconciliation evidence

- Date: 2026-10-14. Bootstrapped from the new uncommitted SPEC-0010 draft.
  The source uses `revision: null` because it has no committed baseline; its
  content hash records the exact working-copy bytes used.
- SPEC-0009 already governs safe reuse and measured reduction of repeated
  parsing, hashing, validation, and runbook-selection work. This plan therefore
  assigns durable run lifecycle, authorization, recovery, concurrency, and UI
  decisions to SPEC-0010 rather than broadening SPEC-0009.
- No implementation, readiness record, concrete slice, approval, or delivery
  authority is created. Existing unrelated working-tree changes are preserved.
- Reconciliation is complete for the initial draft; exact specification and
  plan snapshots remain subject to human review.
