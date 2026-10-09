---
name: work-plan-edit
description: "Make planning-only edits to a Qhapaq work plan or items. Use to split tasks, reorder phases, revise implementation manifests, cancel obsolete work, or change dependencies without silently changing requirements or architecture."
argument-hint: "<spec-id> <requested planning change>"
---

# Edit a Work Plan

## Contract

Read [AGENTS.md](../../../AGENTS.md) and the
[workflow guide](../../../docs/development/spec-driven-workflow.md).
Resolve the requested plan/items and inspect their sources and dependents.
Do not alter product behavior, infer approval, execute slices, commit, or push.

## Procedure

1. Inspect the worktree, source currentness, current scope, dependencies,
   readiness, and approval evidence. Ask for an unclear requested change.
   If sources changed, reconcile using
   [work-plan-sync](../work-plan-sync/SKILL.md) before trusting the affected plan.
2. Classify the proposed edit. Planning-only work is normally maintenance.
   If it needs new behavior or architecture, stop and identify the required
   specification amendment or ADR; do not encode that decision only in a plan.
3. Edit the smallest coherent scope. Preserve IDs and completed history.
   For a split, retain the original as an aggregate gate or cancel it with
   explicit replacement links, preserving all acceptance criteria. Update
   dependents according to the prerequisites they actually need.
4. For a material in-progress implementation edit, account for existing code,
   pause execution, and update its manifest, tests, entry/exit gates, and
   downstream slices. Preserve unrelated user changes. Reapproval is required
   for changed material plan content.
5. Keep membership/order in the plan, status/dependencies in items. Do not
   treat preferred order as dependency. Cancel obsolete open work with reasons.
   New requirements after valid completion create follow-up work; only an
   incorrect completion claim reopens the original.
6. Reassess affected approvals/readiness and record the rationale. Do not
   manufacture new source snapshots or approval just to remove a blocker.
7. Apply the workflow validation checklist, including cross-plan cycles and
   requirement coverage after splits. Invoke
   [spec-trace-check](../spec-trace-check/SKILL.md). No code build is needed for
   plan-only edits unless documented checks require it.

## Output and stop

Report edited items, scope retained/moved/removed, dependency and approval
impact, blockers, checks, proposed classification, and review gate.
Stop for review.

Evaluation: splitting retains coverage and stable history; cancelling a required
prerequisite blocks dependents until explicitly rewired; a requested behavior or
layering change is not accepted as a planning-only edit.
