---
name: spec-readiness
description: "Assess completeness and implementation readiness of a named Qhapaq specification scope and exact revision. Use after decision closure or before implementation planning; checks unknown gaps, consistency, conformance expectations, prerequisites, and explicit approval."
argument-hint: "<spec-id> scope=<name>"
---

# Assess Specification Readiness

## Contract

Read [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), and the
[readiness template](../../../work/templates/readiness.md).
Resolve a named scope with explicit requirements/capabilities and exclusions.
Ask if the scope is ambiguous. Do not publish, commit, implement, or silently
resolve new product decisions.

## Procedure

1. Read the governing specification, related requirements/ADRs, plan/items,
   existing readiness evidence, and required artifacts. If relevant plan sources
   are stale, report the need for `work-plan-sync` before approval.
2. Check known decisions and normative entry/exit gates. Open blocking decisions,
   unverified approval, or missing required artifacts remain explicit blockers.
3. Independently inspect completeness: closed shapes and contracts, typing,
   failures, null/missing behavior, deterministic order, limits/accounting,
   policy/security/privacy, compatibility, and cross-specification consistency
   as applicable. An empty decision backlog is not proof of completeness.
4. Map scope requirements to required conformance expectations and actual
   prerequisite artifacts. Distinguish specified cases from published vectors.
   Do not require unrelated release artifacts or relax specified gates.
5. Populate or revise the scope's readiness record with exact source snapshots,
   findings, exclusions, validation, and blockers. Preserve prior approval
   history in Git; material changes need reassessment. Report newly discovered
   decision work for reconciliation rather than closing it implicitly.
6. Apply the workflow validation checklist and invoke
   [spec-trace-check](../spec-trace-check/SKILL.md). Record only performed checks.
7. Set blocked when findings prevent readiness; otherwise ready-for-review.
   Set approved only when the user explicitly approves the exact assessed
   snapshot after the required checks. Earlier approval of another scope or
   a successful commit is insufficient.

## Output and stop

Report scope, requirement coverage, source snapshots, blockers, missing
conformance/prerequisites, validation, and review gate. State explicitly that
readiness is scoped and is neither publication nor a full v1 conformance claim.
Stop without executing an implementation item.

Evaluation: no open items can still yield blocked readiness; a changed source
does not inherit approval; independent scope exclusions remain explicit; a
required schema/vector cannot be replaced by a promise to generate it later.
