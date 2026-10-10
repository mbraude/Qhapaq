---
name: spec-next
description: "Resolve one dependency-ready specification decision in a Qhapaq work plan. Use to continue iterating a spec, close the next open question in a phase, or work on a named decision item; stops at consequential choices and human review."
argument-hint: "<spec-id> [phase=<identity>] [item=<decision-id>]"
---

# Resolve the Next Specification Decision

## Contract

Read [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), applicable
specification instructions, and the target plan. Handle one decision item.
Do not implement future slices, commit, publish, or infer approval.

## Procedure

1. Inspect worktree and source currentness. If no plan exists or affected
   sources are stale, report the need for
   [work-plan-sync](../work-plan-sync/SKILL.md) before selection. Do not silently
   bootstrap or expand the requested scope.
2. Surface pending review of the preceding item. If explicit approval of its
   exact unchanged snapshot is supplied, validate its criteria and record it.
   Otherwise ask whether to review it or proceed with an independent eligible
   item; do not automatically bypass the review gate.
3. Select the named item, or the first decision-eligible item in the requested
   phase/plan order. Read transitive prerequisites. If the named item is blocked,
   report why without choosing another. If none are eligible, show blockers;
   if no decisions remain, recommend `spec-readiness` for a named scope.
4. State selected ID, objective, exclusions, and acceptance criteria. Set
   in-progress before work. Read requirements and adjacent semantics, relevant
   ADRs, examples, and existing conformance artifacts.
5. Identify alternatives and recommend a resolution. Ask the user for
   consequential missing decisions. If input is unavailable, record the
   blocker and stop; never treat a recommendation as accepted.
6. Apply accepted decisions to their authoritative specification or ADR.
   Update all affected semantics, examples, conformance expectations, references,
   and fingerprints. Preserve identities and published-version immutability.
   Record the result in the item's resolution through links and requirement IDs,
   not duplicated normative text.
7. Reconcile effects using `work-plan-sync`, bounded to this decision and its
   affected downstream work. Do not resolve other decisions during reconciliation.
   Record real source snapshots, readiness impact, and remaining blockers.
8. Check item acceptance criteria and workflow structure, then invoke
   [spec-trace-check](../spec-trace-check/SKILL.md) and applicable documented
   artifact checks. Failures or missing required outputs prevent a successful
   ready-for-review claim.
9. Before requesting review, complete every substantive acceptance criterion,
   run required checks, and record the exact output/input snapshot. Acceptance
   criteria cover the outcome and validation, not the reviewer’s approval.
   Set ready-for-review only after those gates pass; do not edit material
   content or mark the item complete while waiting for review. Complete only
   after explicit human approval of that exact material outcome, using the
   [approve-commit-push](../approve-commit-push/SKILL.md) workflow when delivery
   is requested.

## Output and stop

Report selected item, accepted decisions, changed artifact links, requirement
coverage, validation, blockers, proposed trailers, and next review gate.
Stop after this one decision.

Evaluation: a named blocked item is not skipped; unanswered numeric semantics
remain unresolved; passing trace checks do not imply approval; a resolved
decision does not enable implementation without its separate prerequisites.
