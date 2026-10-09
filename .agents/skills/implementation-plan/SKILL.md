---
name: implementation-plan
description: "Create or revise concrete, dependency-ordered Qhapaq implementation slices for an approved specification scope. Use to detail a phase, split a delivery milestone, or revise files, projects, namespaces, tests, and exit gates before incremental implementation."
argument-hint: "<spec-id> phase=<identity> [item=<implementation-id>]"
---

# Plan Incremental Implementation

## Contract

Read [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), relevant
architecture and coding conventions, and the
[implementation template](../../../work/templates/implementation.md).
Do not generate production placeholders, implement slices, approve plans,
commit, or invent unresolved contracts.

## Procedure

1. Resolve the requested phase/milestone, source currentness, scoped readiness,
   existing implementation items, and cross-plan dependencies. Inspect current
   code and documented toolchain so the plan reflects reality.
2. Require approved/current relevant specification readiness before declaring
   concrete slices implementation-ready. If unresolved decisions remain,
   document blocked milestones and needed decisions; do not imply execution
   eligibility. Clearly governed bugs use the existing requirement review and
   [fix-bug](../fix-bug/SKILL.md), not whole-specification closure.
3. Establish or update the phase dependency graph and measurable outcomes.
   Prefer independently testable foundations or vertical slices. Distinguish
   true dependencies from preferred sequence.
4. Detail only the requested/next phase. For each slice specify exact file
   actions and purposes, projects/directories/namespaces, visibility,
   contracts/integration, reusable helpers, requirement coverage/exclusions,
   tests/vectors, documented commands, and entry/exit criteria.
5. Preserve stable IDs. Promote same-scope milestones in place, or retain an
   aggregate milestone depending on child slices when splitting. Check all
   former acceptance criteria remain covered and downstream work depends on
   the outcomes it actually needs.
6. For replanning in-progress work, account for implemented code, pause affected
   execution, and record material deviations. Identify specification/ADR changes
   needed for new behavior or ownership; do not accept them inside the plan.
7. Record snapshots of material authoritative inputs through bounded
   `work-plan-sync` reconciliation where needed. Keep plan approval absent or
   invalidated until the exact revised material plan is explicitly approved.
8. Apply workflow validation, including manifests, architecture boundaries,
   prerequisites, cross-plan cycles, coverage, and readiness.
   Invoke [spec-trace-check](../spec-trace-check/SKILL.md).

## Output and stop

Report slices and dependencies, exact manifests, requirement coverage, missing
prerequisites, validation, and requested plan review. Plan approval is distinct
from item delivery status: an approved but unstarted slice stays open.
Stop without creating production files.

Evaluation: milestones cannot execute; broad future work is not filled with
speculative class hierarchies; a split retains its aggregate gate; material
replanning invalidates plan approval without erasing implemented user work.
