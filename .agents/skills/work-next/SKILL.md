---
name: work-next
description: "Run the next safe action from a Qhapaq work runbook. Use for a fast repeated workflow that refreshes stale runbooks, selects the next dependency-ready item across specifications, delegates to existing planning, decision, readiness, implementation, approval, validation, commit, and push skills, then refreshes runbook status."
argument-hint: "<primary-spec-id>"
---

# Run the Next Work-Runbook Action

## Contract

Apply [AGENTS.md](../../../AGENTS.md) and the
[workflow guide](../../../docs/development/spec-driven-workflow.md), reading
each only if it is not already in the current context, and read
`work/<primary-id>/runbook.md` when it exists. Execute at most one runbook row
and its optional delivery action. Do not bypass source currentness, readiness,
plan approval, human review, validation, dependency, branch, commit, or push
gates.

This skill orchestrates existing skills; it does not reproduce their
procedures. Run every delegated skill inline in the current agent, never as a
subagent or background task, so the context already loaded here and the
retained synchronization facts are reused rather than rebuilt. A row may stop
for a consequential decision or explicit approval. That stop is the correct
outcome, not permission to continue to another row.

Synchronize the runbook at most twice per invocation: once before selection
and once after the selected row and any delivery action change repository
state. Do not add a refresh solely to record an intermediate state.

## Procedure

1. Invoke [work-runbook-sync](../work-runbook-sync/SKILL.md) with the supplied
   primary specification and the existing runbook's declared included scope.
   This creates a missing runbook, refreshes a stale one, or reports a no-op.
   Never select from stale rows.
2. Read the refreshed `Next command`, table, blockers, source digest, branch,
   and `HEAD`. Use that freshly synchronized `Next command` as the global row
   selection; do not independently reread every row or rebuild the global
   eligibility order in this invocation. Retain the synchronization result for
   reporting and reuse it until a delegated action changes repository state.
   This is invocation-local reuse, not permission to trust a runbook that was
   not synchronized in step 1. If structural errors, dependency cycles,
   cancelled prerequisites, or ambiguous eligibility remain, stop with the
   repair command. Before
   dispatching `/approve-implementation-plan` or `/implement-next`, independently
   recheck the selected slice's exact manifest and readiness record. The
   readiness must be current, explicitly approved for implementation, cover the
   slice's governing requirements/capabilities, and include every specification
   document the manifest may edit. Planning-only readiness, an explicit
   exclusion of those edits, stale evidence, or ambiguous coverage blocks both
   commands. If this preflight fails, do not invoke the selected command or
   switch to another row; stop and direct the user to the exact scoped
   `/spec-readiness` assessment and subsequent readiness approval, then a
   refreshed runbook. If every row is complete or cancelled and all aggregate
   gates are satisfied, report the runbook complete; do not invent a
   specification-complete status.
3. State the selected row, description, owning specification, exact command,
   prerequisites, expected stopping point, and what it will unlock. Execute
   only that command by invoking the named repository skill with the exact
   arguments. Never substitute an independent row when the selected row is
   blocked during execution.
4. Respect the delegated skill's stop:
   - `work-plan-sync`, `implementation-plan`, and `spec-readiness` stop for
     review and do not imply approval. A `spec-readiness` result must be
     explicitly approved for the selected implementation scope before the
     runbook may advance to plan approval; approval of a planning-only readiness
     scope is not interchangeable.
   - `spec-next` and `implement-next` handle one bounded item and stop at their
     review gate.
   - `approve-implementation-plan` and `approve` obtain their own explicit
     human approval and must not infer it from this orchestration request.
5. If the delegated action makes no changes, keep the current runbook and
   report the blocker or requested input; skip steps 6 to 8.
6. Offer a delivery choice only when the selected action produced a coherent,
   reviewable worktree outcome and the delegated workflow permits delivery.
   Ask before refreshing the runbook, so the single refresh in step 8 can be
   placed correctly. Use `ask_user` once with the applicable choices:
   - `Leave changes for review`
   - `Build and test only`
   - `Approve only`
   - `Approve and commit`
   - `Approve, commit, and push`
   - `Commit`
   - `Commit and push`

   Omit choices that do not apply. Offer approval variants only for an exact
   ready-for-review work-item or readiness target. Offer ordinary commit
   variants for coherent synchronization, planning, or runbook-only changes
   that have no approval target. Do not offer push when branch or remote
   preconditions are ambiguous. Recommend leaving changes for review when the
   exact material outcome has not yet been presented.
7. Delegate the selected delivery action:
   - `Build and test only` invokes [build-and-test](../build-and-test/SKILL.md).
   - `Approve only` invokes [approve](../approve/SKILL.md).
   - `Approve and commit` invokes
     [approve-commit](../approve-commit/SKILL.md).
   - `Approve, commit, and push` invokes
     [approve-commit-push](../approve-commit-push/SKILL.md).
   - `Commit` invokes [commit](../commit/SKILL.md).
   - `Commit and push` invokes
     [commit-and-push](../commit-and-push/SKILL.md).

   Pass the exact work-item or readiness target and applicable validation mode.
   For `Commit` and `Commit and push`, perform the step 8 refresh first.
   Existing approval skills decide whether full build and unit tests are
   mandatory for the actual change. Ordinary commit skills validate the whole
   selected snapshot. Never offer or pass a validation skip that repository
   policy forbids.
8. Invoke `work-runbook-sync` exactly once more so the table records the
   resulting persisted and derived status. This refresh is part of the
   selected row, not a second work item. Place it as follows:
   - `Commit` or `Commit and push`: refresh before invoking the commit skill,
     so the commit includes the refreshed runbook.
   - Approval variants: refresh after the approval skill records lifecycle
     evidence. When that skill also commits, leave the refreshed runbook
     uncommitted for the next delivery; do not start another commit round
     solely for it.
   - `Leave changes for review`, `Build and test only`, or no delivery choice:
     refresh after the selected action and any validation.

   Report the updated row, completion date when available, newly unlocked
   row, and its copyable command. Do not execute the newly unlocked row in the
   same invocation.

## Output and stop

Report the runbook snapshot, selected row and delegated skill, result,
validation/delivery result when selected, refreshed status, and exact next
command. One invocation advances at most one runbook row.

Evaluation: repeated invocation safely advances the dependency graph; stale
runbooks refresh before selection; cross-specification prerequisites are
eligible; review remains explicit; optional delivery composes existing skills;
failure or user input stops the loop without skipping to unrelated work.
