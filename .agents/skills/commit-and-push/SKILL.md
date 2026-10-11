---
name: commit-and-push
description: Review and commit the selected Git snapshot through the repository's shared commit workflow, then push the current branch to origin. Use when the user asks to commit and push repository changes.
---

# Commit and Push

Use this skill only in a Git repository when the user intends to commit changes
and push the resulting commit to `origin`.

## Arguments

Pass `skip-build-and-test`, `skip-semantic-review`, and `change-kind` through to
the repository's `commit` skill exactly as supplied by the user.

## Preconditions

Before invoking `commit`, confirm that:

- the repository has an `origin` remote;
- `HEAD` is attached to the explicitly intended delivery branch;
- the configured upstream, when present, has been inspected; and
- the intended remote branch is unambiguous.

Stop before committing if any push precondition fails. Never create or switch
branches, rewrite history, force-push, bypass hooks, or infer a differently
named remote branch.

## Workflow

1. Invoke the repository's `commit` skill with every user-supplied argument.
   Do not duplicate or replace any part of its review, validation, staging,
   trailer verification, or commit workflow.
2. After the local commit succeeds, verify that `HEAD` is still attached to the
   same branch and that the intended push destination remains unchanged.
3. Invoke the repository's `push` skill. Do not duplicate or replace its
   remote-state inspection, same-named destination, rejection handling,
   verification, or reporting.
4. If `push` fails, preserve the local commit and report the exact failure. Do
   not invoke `commit` again.

## Output

Report the commit hash, final subject, specification trailers, validation
results, and pushed remote branch. If pushing fails, distinguish the successful
local commit from the failed remote delivery. Do not report full success unless
both the commit and push completed.
