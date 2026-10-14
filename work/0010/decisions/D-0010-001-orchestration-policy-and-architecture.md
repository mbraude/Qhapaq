---
id: D-0010-001
kind: decision
title: Resolve work-run authorization and architecture
status: open
spec: SPEC-0010
requirements:
  - R-0010-001
  - R-0010-002
  - R-0010-003
  - R-0010-004
  - R-0010-005
  - R-0010-006
  - R-0010-007
  - R-0010-008
  - R-0010-009
depends_on: []
artifacts:
  - docs/architecture/decisions/0007-orchestrated-repository-work-runs.md
---

# D-0010-001: Resolve Work-Run Authorization and Architecture

## Objective

Resolve the architecture and policy needed to run repository work through
multiple steps safely, preserve progress across interruption, and stop at
explicit review or decision gates.

## Scope and exclusions

This decision covers R-0010-001 through R-0010-009. It selects delegated
approval classes and defaults, authorization scope and revocation, run-state
representation and recovery, cancellation semantics, concurrency and
worktree isolation, and whether a graphical interface belongs in the initial
delivery.

It does not change SPEC-0009 cache or validation semantics, the single-step
contract of `work-next`, pipeline execution durability, or any work-item
approval gate without an explicit amendment to its governing requirement.

## Questions to resolve

- Which assessment and approval gates may be delegated for one explicitly
  authorized run, and which always require exact-snapshot human review?
- What run authorization profile is the default, how is scope bounded, and how
  can it be revoked?
- Which interrupted actions can be reconciled automatically, and which require
  the run to stop for manual recovery?
- What local state storage, atomicity, locking, retention, and cleanup rules
  are needed for restart and concurrent-run safety?
- Is the initial implementation serial, or does it include independent
  actions in isolated Git worktrees?
- Can one item's commit proceed while another isolated item is being
  implemented, and what validation ordering applies?
- Is a command-based interface sufficient initially, or is a graphical
  VS Code experience required?

## Acceptance criteria

- [ ] An ADR records the selected architecture, policy, and rejected
  alternatives.
- [ ] Every selected behavior conforms to SPEC-0010 and preserves its
  stop, recovery, and exact-snapshot boundaries.
- [ ] Deferred concurrency or UI work is explicitly scoped and does not block
  safe serial execution.
- [ ] Required validation passes and the exact input/output snapshot is
  recorded for review.

## Resolution

Open. The ADR and any resulting specification amendments are pending.

## Validation and review

No resolution, validation evidence, or approval is recorded.
