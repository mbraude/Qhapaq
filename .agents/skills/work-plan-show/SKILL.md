---
name: work-plan-show
description: "Read-only view of a Qhapaq specification roadmap and remaining work. Use to show open items, phase progress, review gates, blockers, ready actions, or a dependency tree/Mermaid graph without editing or synchronizing the plan."
argument-hint: "<spec-id> [phase=<identity>] [remaining] [item=<id>]"
---

# Show a Work Plan

## Contract

Read the [workflow guide](../../../docs/development/spec-driven-workflow.md).
Resolve the requested plan and filters. This skill is read-only: no status
changes, reconciliation, approvals, file writes, commits, or item execution.
If no plan exists, report that and suggest `work-plan-sync`; do not create it.

## Procedure

1. Read the owning plan, selected items, readiness records, source snapshots,
   and transitive prerequisites, including cross-plan dependencies. A phase
   filter does not hide prerequisites needed to understand blockers.
2. Check source currentness, ID/owner agreement, references, membership, and
   dependency cycles. Report missing prerequisites or cancelled dependencies.
   Do not display affected eligibility as trustworthy when inputs are stale
   or invalid. Recommend sync without invoking it.
3. Summarize counts by kind and persisted status. Distinguish decision items,
   implementation milestones, concrete slices, and aggregate gates. Aggregate
   counts are item counts, not a percentage of feature implementation.
4. Derive dependency readiness and execution eligibility using the guide.
   A milestone is never an executable slice. Highlight pending human review,
   unavailable artifacts, invalidated readiness, and material plan approval.
5. Display a phase outline and linked item table with ID, title, status,
   derived eligibility, and blockers. `remaining` omits complete/cancelled items
   from the primary list but retains them as labelled prerequisite context.
6. Render a dependency graph when useful or requested. Edges mean prerequisite
   to dependent. Tree-like output labels shared/repeated references rather
   than duplicating identities. Mermaid uses safe synthetic node labels and
   does not interpret item text as diagram syntax.
7. Identify eligible next actions in preferred order, separately for decisions
   and implementation. No decision items remaining recommends readiness review,
   not automatic completion or publication.

## Output and stop

Return the outline/table, graph if requested, source currentness, structural
findings, review gates, and next actions. Label it an AI-led view of the current
repository snapshot, not a deterministic validator result. A requested export
is a separate explicit write operation and must identify source snapshots;
never silently persist a second status authority.

Evaluation: viewing makes no edits; shared prerequisites appear once in a graph;
cycles and stale inputs suppress affected eligibility; filtered views retain
necessary cross-phase context.
