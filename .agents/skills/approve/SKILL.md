---
name: approve
description: "Review and explicitly approve an exact ready-for-review Qhapaq work item or scoped specification-readiness record, record approval evidence, and generate a complete Git commit message without staging, committing, or pushing. Use when the user wants to approve work and commit later through VS Code or other Git tooling."
argument-hint: "[work-item-id or readiness-record-path] [skip-build-and-test=true|false]"
---

# Approve a Reviewed Qhapaq Outcome

## Contract

This workflow coordinates human review and approval evidence for one reviewable
work outcome, then prepares its commit message without performing Git delivery.
Read [AGENTS.md](../../../AGENTS.md), the
[specification-driven workflow](../../../docs/development/spec-driven-workflow.md),
the target plan and item or readiness record, and the applicable specification
instructions.

Supported targets:

- A decision or implementation work item with `status: ready-for-review`.
- A scoped readiness record with `assessment: ready-for-review`.

A specification by itself has no approval status in this workflow. For
specification readiness, approve only the named scoped readiness record.
Component contract publication is a separate lifecycle and is never performed
by this skill.

Never infer human approval from invoking this skill, a passing check, a commit,
or an earlier approval of another snapshot. Obtain explicit confirmation of
the exact material outcome in this invocation before recording approval.
Never stage, commit, push, create or switch branches, rewrite history, bypass
hooks, or undo recorded approval because later delivery fails.

## Arguments

- `<work-item-id or readiness-record-path>` is optional when the target can be
  resolved unambiguously from the current request and available editor context.
- `skip-build-and-test` defaults from the target and complete change scope:
  `true` for design/specification-only work, `false` for implementation items
  and any change containing implementation or test code. Users may request
  additional validation by setting it to `false` for design work. It cannot be
  set to `true` for implementation/code work because build and tests are
  required.

## Procedure

### 1. Identify and check the target

Inspect the complete Git status and confirm the repository is not in an
unresolved merge, rebase, cherry-pick, or revert. Confirm that `HEAD` is attached
and the current branch is the user's intended delivery context. The default
branch is permitted. Recommend `work-branch-start` when isolation or
pull-request review would be useful, but do not require or create a branch.

Resolve the target using this precedence:

1. An explicit work-item ID or readiness-record path in the invocation.
2. A work-item ID or readiness-record path explicitly named in the user's
   current message.
3. A uniquely identified work-item/readiness file referenced by the current
   prompt, attachment, tagged file, or active/open editor context supplied to
   the conversation.
4. If only a specification path is referenced, inspect its owning plan and
   find ready-for-review items whose artifact, requirement, or source links
   directly correspond to that specification. A readiness record must name
   that specification and an explicit scope.

Use file names and editor state only when they are actually available in the
conversation context. Continue only when exactly one ready-for-review target is
directly identified. If no candidate or more than one candidate fits, use
`ask_user` to request the target; never infer it from plan order.

For a work item:

- Require `kind: decision` or `kind: implementation` and
  `status: ready-for-review`.
- Read its owning plan, transitive prerequisites, requirements, acceptance
  criteria, resolution or delivery evidence, and every required output.
- Verify prerequisites are complete, outputs exist, and every acceptance
  criterion and normative entry gate is satisfied.
- Recompute the item's material SHA-256 exactly as specified in the workflow
  guide. Verify the item and all material inputs and outputs still match the
  recorded review snapshot.

For a readiness record:

- Require `assessment: ready-for-review`, a named scope, exclusions, validation,
  and no unresolved blocker.
- Read the governing specification, linked decisions, plan, required artifacts,
  and readiness evidence.
- Verify each recorded source hash against the exact current file bytes and the
  recorded baseline revision.

Stale, incomplete, blocked, ambiguous, or materially changed targets require
renewed assessment or review, not approval.

### 2. Review the exact changes and validate

Inspect every staged, unstaged, deleted, renamed, and untracked change,
including full diffs and untracked text. Identify which changes are necessary
outputs or approval evidence for the selected target. Stop before approval if
any change is unrelated, sensitive, generated without an authoritative source,
unreviewable, or outside the selected target.

Classify validation from both the target kind and the actual complete worktree:

- **Design/specification-only:** default `skip-build-and-test=true`. Run
  `spec-trace-check` plus applicable documented documentation checks.
- **Implementation/code:** `skip-build-and-test=false` is mandatory. Run
  `build-and-test`, which includes traceability, locked build, and all
  documented unit-test projects.

If the user explicitly sets `skip-build-and-test=false` for design work, run
the full documented build-and-test workflow. Never skip traceability or bypass
required implementation validation. Record precisely which checks ran.

Keep the change classification and proposed trailers reported by
`spec-trace-check`; they are inputs to the commit message.

### 3. Request explicit approval

Present the target ID/path, outcome, exclusions, acceptance results, validation
results, every file expected in the later commit, and the exact snapshot:

- For a work item, show its material SHA-256 plus full-byte SHA-256 hashes for
  the material input and output files, excluding only evidence fields permitted
  by the workflow guide.
- For a readiness record, show the readiness record and exact assessed
  source/input hashes.

Use `ask_user` to request one explicit choice:

- Approve this exact snapshot, record approval, and generate a commit message.
- Do not approve; stop for changes or further review.

Before asking, verify every substantive acceptance criterion is satisfied and
recorded. Finalize all material content, compute the material hash from that
finalized snapshot, and compare the displayed hashes character-for-character
with the computed values.

Approval applies only to the displayed snapshot and named scope. If the user
declines, stop without changing approval status. If material files change after
approval, stop and request renewed approval.

### 4. Record approval

After explicit approval, record in the target's prescribed review section:

- that approval was explicitly given in this session without inventing a
  person's name;
- the date;
- exact scope and exclusions; and
- the reviewed snapshot hashes.

Only update lifecycle metadata and review-evidence sections excluded from the
material hash. For a work item, set `status: complete` only when its acceptance
criteria, persistent outputs, and required validation are satisfied. For a
readiness record, set `assessment: approved` only for its named scope and
unchanged assessed snapshot. Do not mark a specification or contract version
`Published`.

Recompute the approved material hash and verify every recorded full-byte hash.
If approved material changed, revert only this skill's approval metadata edits,
never discard user work, return the target to review as appropriate, and ask
for approval again.

### 5. Generate the commit message

Reinspect Git status and verify the complete worktree still contains only
changes within the approved target scope, including the approval evidence. If
concurrent or unrelated changes appeared, stop without staging or generating a
success-shaped delivery result.

Generate a complete commit message that represents the entire approved
worktree:

- Match the repository's established subject style.
- Use an imperative, specific, concise subject.
- Add a body when distinct outcomes or important rationale would otherwise be
  hidden.
- End with the exact `Change-Kind:` and `Spec:` trailers verified by
  `spec-trace-check`, followed by required attribution trailers.
- Keep all trailers in one final contiguous paragraph with no blank lines
  between trailer lines.

Present the message in one plain-text fenced block so it can be copied directly
into the VS Code Source Control commit-message field. Do not write it to a
repository file or the Git index. State that the user must ensure the UI commit
contains exactly the approved files and unchanged snapshot; any material edit
requires renewed approval and a regenerated message.

## Output

Report the target and approved scope, exact snapshot, recorded approval
evidence, validation performed, complete copy-ready commit message, current
branch, and any remaining blockers. State explicitly that no files were staged,
committed, pushed, or published. Distinguish approval, Git delivery, readiness,
and component-contract publication.
