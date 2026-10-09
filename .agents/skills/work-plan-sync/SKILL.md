---
name: work-plan-sync
description: "Create or reconcile repository-owned Qhapaq work plans from a specification. Use to extract rollout phases and open questions, bootstrap missing work items, or update a roadmap after spec changes while preserving IDs, dependencies, approval gates, and history."
argument-hint: "<spec-id or path> [phase=<identity>]"
---

# Synchronize a Work Plan

## Contract

Read [AGENTS.md](../../../AGENTS.md) and the
[workflow guide](../../../docs/development/spec-driven-workflow.md), especially
source snapshots, synchronization, and validation. Resolve the target
specification and its owning plan. Ask if ambiguous.

Use the shared [plan](../../../work/templates/plan.md),
[decision](../../../work/templates/decision.md), and
[implementation](../../../work/templates/implementation.md) templates.
No separate bootstrap skill is needed: a missing plan uses this procedure.
Do not execute items, approve work, commit, publish, or migrate normative
specification text unless the user explicitly includes that migration.

## Procedure

1. Inspect worktree changes and the target's current authoritative inputs.
   Read any existing plan, items, readiness records, and cross-plan prerequisites.
   Inventory all phases but bound item detail to the requested/current scope.
2. If a plan exists, compare source records against exact current bytes and
   their committed baseline revisions. Read the changed source text, not just
   revision numbers. Recover old text from the recorded revision where possible.
   If an old uncommitted snapshot cannot be recovered, report that limitation
   and review the full affected scope; do not invent an exact diff.
3. Bootstrap: extract unresolved decisions and future delivery milestones,
   preserving phase identities, normative gates, and actual dependencies.
   Deduplicate questions appearing in rollout and open-question sections.
   Do not confuse completed semantics with published schemas/vectors or code.
   Checked boxes are source evidence, not proof of historical human approval.
   Record unverified completion as ready-for-review or blocked with an explanation.
4. Reconcile: add new work, revise open scope, split broad work, cancel obsolete
   items with replacement links, and update genuine dependencies. Preserve IDs.
   If previously correct completed work is superseded, create follow-up items.
   Reopen only a wrong original completion claim, explaining the evidence.
5. Assess effects on code/test references, downstream slices, plan approvals,
   and readiness. Reassess affected scopes; do not carry old approval onto new
   semantics or invalidate unrelated work without evidence. Missing decisions
   become blockers rather than implicit defaults.
6. Populate repository-relative artifact paths and existing requirement IDs.
   Detail current decisions; leave speculative implementation work as milestones.
   Keep architectural choices in the appropriate source or as unresolved items.
7. Update phase membership and reconciliation evidence. Compute real SHA-256
   source snapshots and use full Git revisions. Advance snapshots only for
   completely reviewed inputs; retain stale records and explain remaining
   reconciliation if blocked. Do not hash plans as their own sources.
8. Check unique IDs/ownership, retained coverage, references, required sections,
   cross-plan cycles, cancelled dependencies, source accuracy, and normative
   gates using the workflow guide. Invoke
   [spec-trace-check](../spec-trace-check/SKILL.md).

## Output and stop

Report created/changed/cancelled items, dependencies, source baseline, readiness
impact, unresolved blockers, checks, and next review action. Explain any
remaining duplicate tracking inside an unmigrated specification.
Stop for review; source reconciliation is not human approval.

Evaluation: repeated sync of unchanged sources is idempotent; new requirements
create scoped follow-up work; missing plans create no production files; missing
historical snapshots or normative migration scope are reported explicitly.
