# SPEC-0010: Repository Work-Run Orchestration

> **Status:** Draft
> **Version:** 0.1
> **Scope:** Resumable, policy-bounded orchestration of repository work runbooks
> **Last updated:** 2026-10-14

## 1. Purpose and Status

The repository workflow currently advances a dependency-ordered runbook one
bounded action at a time. Repeated invocations require user attention even
when the next action is already determined, and a long sequence is vulnerable
to interruption when a process or computer stops.

This specification defines a local orchestrator that can continue safe
runbook actions, preserve enough progress to recover after interruption, and
stop when human judgment or authorization is required. It composes existing
repository skills; it does not replace their validation, planning, approval,
or delivery rules.

The optimization of repeated parsing, hashing, validation, and runbook
selection remains in [SPEC-0009](0009-repository-validation-derived-state.md).
This specification concerns orchestration lifecycle, user authorization,
recovery, and optional concurrency or interaction surfaces.

This is repository development tooling, not Qhapaq pipeline execution. It does
not change the non-durable execution model of v1 pipeline runs, promise
exactly-once effects, or provide pipeline resume, compensation, or rollback.
The [SPEC-0010 work plan](../work/0010/plan.md) tracks decisions and future
delivery. This draft does not select an implementation technology, journal
format, UI, or concurrency architecture.

## 2. Goals and Non-goals

### Goals

- Continue through dependency-ready runbook actions without repeated manual
  invocations when the run's explicit authorization permits it.
- Reduce elapsed time and user interaction overhead while preserving every
  existing review, approval, validation, and delivery boundary.
- Recover safely after sleep, process termination, or machine restart.
- Make the active run, completed actions, current gate, and next user action
  understandable.
- Permit safe overlap of independent work only when repository changes are
  isolated and the user has authorized concurrency.

### Non-goals

- Change the behavior or contract of the existing single-action runbook
  workflow.
- Change authoritative work-item, plan, readiness, approval, or source records.
- Infer approval from a run request, successful checks, a commit, or earlier
  approval of a different snapshot.
- Automatically resolve specification or architecture decisions.
- Promise uninterrupted execution while the machine is asleep or offline.
- Guarantee exactly-once effects when recovering an interrupted action.
- Select a user interface, programming language, storage format, command
  syntax, branch naming convention, or concurrency implementation.
- Execute Qhapaq pipelines or alter their durability guarantees.

## 3. Authority and Composition

The runbook remains a generated view; authoritative specifications, plans,
work items, readiness records, approval evidence, and Git state determine
eligibility and status. SPEC-0009 governs any reuse of validated derived
state. The
[specification-driven workflow](../docs/development/spec-driven-workflow.md)
continues to govern review, approval, branch, and delivery semantics.

**[R-0010-001]** A work-run orchestrator must select eligible actions from a
current runbook and invoke each action through its existing owning workflow. It must not independently infer
eligibility, reproduce an owning workflow's validation or approval procedure,
change the contract of the existing single-action runbook workflow, or treat
generated runbook content as authoritative status.

## 4. Run Identity and Persistent Progress

**[R-0010-002]** Each run must be bound to an explicit primary specification,
included specification scope, and run authorization. The user must be able to
identify the run and request its status, pause, or cancellation without
changing authoritative work-item status.

**[R-0010-003]** The orchestrator must preserve sufficient local progress to
identify the selected action, its owning workflow, its input identity, its
execution state, and its observed outcome after process termination or
machine restart. This progress is non-authoritative derived state: it cannot
establish eligibility, approval, completion, or delivery, and must be
reconciled with current authoritative sources before further execution.

## 5. Recovery and Stop Conditions

**[R-0010-004]** Before resuming a persisted run, the orchestrator must verify
that the run scope and authorization remain valid and reconcile recorded
progress against current repository, work-item, runbook, and Git state. If an
interrupted action's effects or completion cannot be established safely, the
orchestrator must stop for reconciliation rather than blindly repeat it or
report success.

**[R-0010-005]** The orchestrator must stop and identify the exact target and
reason when execution encounters a consequential decision, a material
outcome requiring review, missing or ambiguous authorization, stale or
inconsistent inputs, a blocked selected action, a failed required check, or
an uncertain action outcome. It must not skip the selected blocked action
for unrelated work. Continuation may resume only after the required decision,
review, authorization, or repair is recorded and revalidated.

## 6. Authorization and Delivery

**[R-0010-006]** A run may perform approvals or Git delivery only within
explicitly authorized action classes and scope. A request to continue a run
does not by itself authorize approval of a material snapshot, commit, push, or
any other action outside that recorded authorization. Any approval evidence
must identify its actual authorization basis and exact reviewed or delegated
scope; the orchestrator must not claim human review that did not occur.

The categories of approval that may be delegated, the default authorization
profile, and the relationship between automated assessment and exact-snapshot
human approval remain open decisions.

## 7. Concurrency and Isolation

**[R-0010-007]** If an implementation executes repository-mutating actions
concurrently, it must establish that those actions are dependency-independent
and isolate their working changes so one action cannot stage, commit, or
overwrite another action's changes. Each resulting commit and review target
must remain attributable to its exact work item and snapshot. A shared working
tree must not be used for concurrent mutations.

The initial release may remain serial. Whether concurrent work, isolated Git
worktrees, or overlapping commit operations are in scope for that release
requires an architecture decision.

## 8. Status, Security, and Privacy

**[R-0010-008]** While a run is active or paused, its status must identify
completed and current actions, the current stop or review gate, and the exact
user action needed to continue. It must distinguish orchestrator progress
from authoritative work-item completion, approval, and Git delivery.

**[R-0010-009]** Persisted run state must be local, bounded to orchestration
metadata and references needed for recovery, excluded from version control by
default, and safe to delete without modifying authoritative work or Git
history. It must not persist credentials, resolved secrets, operation
payloads, private user data, or complete copies of untrusted source content.

Whether a graphical VS Code experience is required or a command-based
interface is sufficient remains an open decision. Any interaction surface
must present exact review and authorization targets before accepting a
user decision.

## 9. Verification Expectations

Delivery must include deterministic cases for:

- continuing across multiple dependency-ready actions and stopping at every
  required gate;
- pause, cancellation, sleep, process termination, and machine restart;
- interruption before, during, and after a repository-mutating action;
- recovery when action outcome is uncertain, with no blind replay or
  success-shaped fallback;
- changed source, runbook, authorization, branch, or work-item state between
  pause and resume;
- exact-snapshot review and approval evidence, including rejected or revised
  changes;
- staging and commit isolation for distinct work items;
- concurrent independent and dependent actions, if concurrency is supported;
- deletion, corruption, and incompatible versions of local run state;
- authorization boundaries for approval, commit, push, pause, resume, and
  cancellation; and
- performance measurements separating user interaction time, process
  startup, synchronization, validation, implementation, and required review.

## 10. Rollout

1. Resolve delegated approval, run authorization, recovery, and cancellation
   semantics in an architectural decision.
2. Establish baseline end-to-end time and user interaction counts for repeated
   `work-next` invocations; distinguish orchestration overhead from work and
   validation cost addressed by SPEC-0009.
3. Deliver a serial, resumable orchestrator with explicit stop and recovery
   behavior, retaining the existing single-action entry point unchanged.
4. Evaluate isolated worktree execution for dependency-independent work only
   after serial recovery and delivery semantics are validated.
5. Decide whether a graphical VS Code surface materially improves run
   creation, status, pause, resume, cancellation, and exact-snapshot review.

Each stage remains separately reviewable. Concurrency and a graphical UI are
not prerequisites for safe serial orchestration.

## 11. Alternatives

### Repeated manual `work-next`

Retained as the single-step primitive and recovery fallback, but insufficient
as the only interface for a long run whose safe next actions are already
determined.

### Unbounded autonomous execution

Rejected because it could cross review, decision, source-currentness, or
delivery boundaries without fresh authorization.

### Shared-checkout parallel mutations

Rejected because concurrent staging or file changes could cause one item's
commit or review snapshot to include another item's work.

### External tracker as the run-state authority

Not selected. The run must remain resumable without requiring an external
system, and authoritative workflow records remain repository-owned.

## 12. Open Questions

- Which approval and validation gates are procedural and may be explicitly
  delegated for a run, and which always require human review?
- What authorization profile is safe by default, and how is its exact scope
  recorded and revoked?
- Which interrupted actions can be reconciled automatically, and which must
  always stop for manual recovery?
- What local state representation, atomicity, locking, retention, and
  cleanup behavior are required for concurrent processes?
- Should the initial orchestrator be serial only, or include isolated
  worktree execution for independent actions?
- Can commits for one completed item proceed while another isolated item is
  being implemented, and what validation and integration ordering is required?
- Is a graphical VS Code experience required initially, or should a
  command-based interface establish the lifecycle first?
- Which metrics and thresholds demonstrate a meaningful reduction in
  end-to-end delay and repeated user interaction without weakening review?

## 13. Revision History

| Version | Date | Changes |
| --- | --- | --- |
| 0.1 | 2026-10-14 | Initial draft for resumable, policy-bounded repository work-run orchestration. |
