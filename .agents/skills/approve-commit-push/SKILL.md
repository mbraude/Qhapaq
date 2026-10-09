---
name: approve-commit-push
description: "Review and explicitly approve an exact ready-for-review Qhapaq work item or scoped specification-readiness record, even when identified by the prompt's referenced/open file; record approval, then commit and push related changes. Uses documentation-only checks for design/spec work and requires build and tests for implementation/code work; never publishes component contracts."
argument-hint: "[work-item-id or readiness-record-path] [skip-build-and-test=true|false]"
---

# Approve, Commit, and Push a Reviewed Qhapaq Outcome

## Contract

This workflow coordinates human review, approval evidence, and delivery of one
reviewable work outcome. Read [AGENTS.md](../../../AGENTS.md), the
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
Never commit or push unrelated changes, rewrite history, force-push, bypass
hooks, or undo a recorded approval because delivery failed.

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
unresolved merge, rebase, cherry-pick, or revert.

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
conversation context; do not claim to inspect VS Code's active editor through
an unavailable interface. A specification file alone is not an approval
target. Continue only when exactly one ready-for-review target is directly
identified. If no candidate or more than one candidate fits, use `ask_user`
to request the target; never infer it from plan order, pick a neighboring
item, or treat a merely related open item as the user's intended target.

Resolve the chosen item by exact ID or repository-relative readiness path.

For a work item:

- Require `kind: decision` or `kind: implementation` and
  `status: ready-for-review`.
- Read its owning plan, transitive prerequisites, requirements, acceptance
  criteria, resolution or delivery evidence, and every required output.
- Verify prerequisites are complete, outputs exist, and every acceptance
  criterion and normative entry gate is satisfied. A milestone cannot be
  approved as an executable slice or treated as completed delivery.
- Recompute the item's material SHA-256 exactly as specified in the workflow
  guide. Verify the item and all material inputs and outputs still match the
  recorded review snapshot. A material mismatch requires renewed assessment
  and review, not approval.

For a readiness record:

- Require `assessment: ready-for-review`, a named scope, exclusions, validation,
  and no unresolved blocker.
- Read the governing specification, linked decisions, plan, required artifacts,
  and readiness evidence. Verify each recorded source hash against the exact
  current file bytes and the recorded baseline revision.
- If the record is stale, incomplete, blocked, or its scope is ambiguous, stop
  and identify the required `work-plan-sync` or `spec-readiness` follow-up.

Do not modify the target during eligibility checks.

### 2. Review the exact changes and select validation

Inspect every staged, unstaged, deleted, renamed, and untracked change,
including full diffs and untracked text. Identify which changes are necessary
outputs or approval evidence for the selected target.

Stop before approval if:

- any change is unrelated, sensitive, generated without an authoritative
  source, or cannot be reviewed;
- the intended branch or push destination is ambiguous;
- a required check fails; or
- the target fails any acceptance criterion, prerequisite, or normative gate.

Do not include unrelated work merely because the commit skill stages the whole
worktree. Resolve scope explicitly, or ask the user to separate unrelated
changes before proceeding.

Classify validation from both the target kind and the actual complete
worktree—not from a filename alone:

- **Design/specification-only:** a decision item, specification amendment,
  readiness assessment, or planning/documentation outcome with no
  implementation or test code in the reviewed change. Default
  `skip-build-and-test=true`. Run `spec-trace-check` separately, plus applicable
  documented documentation checks; do not build or run unit tests by default.
- **Implementation/code:** an implementation work item, or any reviewed change
  containing product or test code. `skip-build-and-test=false` is mandatory.
  Run `build-and-test`, which includes traceability, locked build, and all
  documented unit-test projects. Do not honor a request to skip this required
  validation; stop and explain the gate if it cannot be completed.

If the user explicitly sets `skip-build-and-test=false` for design work, run
the full documented build-and-test workflow as well. The user may not set
`skip-build-and-test=true` to bypass implementation/code validation.

When defaulting to skip build and tests, still run `spec-trace-check`: skipping
compilation and unit tests never skips the repository's required traceability
review. Record precisely which checks did and did not run.

### 3. Request explicit approval

Present the target ID/path, outcome, exclusions, acceptance results, validation
results, every file included in the proposed commit, and the exact snapshot:

- For a work item, show its material SHA-256 plus full-byte SHA-256 hashes for
  the material input and output files, excluding only evidence fields as
  permitted by the workflow guide.
- For a readiness record, show the readiness record and the exact assessed
  source/input hashes.

Use `ask_user` to request one explicit choice:

- Approve this exact snapshot and continue to commit and push.
- Do not approve; stop for changes or further review.

The approval applies only to the displayed snapshot and the named scope. If
the user declines, stop without changing approval status or committing. If
material files change after approval, stop and request renewed approval.

### 4. Record approval

After explicit approval, record in the target's prescribed review section:

- that approval was explicitly given in this session (do not invent a person's
  name);
- the date;
- exact scope and exclusions; and
- the reviewed snapshot hashes.

For a work item, set `status: complete` only if its acceptance criteria,
persistent outputs, and required validation are satisfied. For a readiness
record, set `assessment: approved` only for its named scope and unchanged
assessed snapshot. Do not mark the specification or contract version
`Published`.

Recompute the approved material hash and verify every recorded full-byte hash.
If the approved material changed, revert only this skill's approval metadata
edits (never discard user work), return the target to review as appropriate,
and ask for approval again.

### 5. Commit and push

Reinspect Git status and verify that the complete worktree still contains only
changes within the approved target scope. Include the approval evidence in the
same commit. If concurrent or unrelated changes appeared, stop without
staging or committing.

For implementation/code work or an explicit request to run build and tests,
invoke the repository's existing `commit-and-push` skill to perform its full
preflight, validation, staging, trailer verification, commit, and non-force
push to `origin`.

For design/specification-only work with the default
`skip-build-and-test=true`, first complete the separate `spec-trace-check` and
documentary checks in step 2, then invoke
`commit-and-push-without-build-and-test`. This wrapper performs the shared
commit workflow while explicitly skipping only build, unit tests, and its own
trace-check invocation; the trace check already performed in step 2 remains
required. Do not use the wrapper for implementation/code work.

Pass through any user-supplied `change-kind` or `skip-semantic-review` only as
the invoked skills permit.

Do not hand-stage a subset and claim the target was delivered while bypassing
the existing commit workflow. The commit skill must confirm that its
whole-worktree scope matches this approved target.

If validation or commit fails, report the failure and stop. If the commit
succeeds but the push is rejected, preserve the local commit and report the
remote rejection exactly; do not pull, rebase, merge, reset, or force-push.

## Output

Report the target and approved scope, exact snapshot, recorded approval
evidence, validation performed, commit hash and subject if committed, pushed
remote branch if pushed, and any remaining blockers. Distinguish clearly
between approval, local commit, remote push, readiness, and contract
publication. Never claim a later stage succeeded unless it did.
