---
name: push
description: "Push existing commits from the current attached Git branch to the same-named branch on origin without committing, rebasing, merging, or changing work-item state. Use when the user asks to push or publish the current branch."
---

# Push the Current Branch

Use this skill only when the user intends to publish existing commits from the
current branch to `origin`. It requires no arguments. Infer the source from the
attached current branch and use only the same-named branch on `origin`.

## Contract

This skill manages Git delivery only. It does not inspect or commit
working-tree changes, approve or complete work items, open or merge pull
requests, create tags or releases, publish component contracts, or run build
and test validation.

Uncommitted changes do not prevent a push because they are not published, but
the final report must identify that they remain local.

## Preconditions

1. Inspect the current branch, complete working-tree status, `origin`, the
   configured upstream, the remote default branch, and unresolved Git
   operations.
2. Stop when:
   - `HEAD` is detached;
   - `origin` is absent;
   - a merge, rebase, cherry-pick, or revert is in progress;
   - the configured upstream names another remote or a differently named
     branch; or
   - the destination cannot be resolved exactly as
     `origin/<current-branch>`.
3. Fetch the destination ref when it exists and determine the exact ahead and
   behind counts without changing the worktree.
4. Stop when the local branch is behind or diverged. Report the remote tip and
   preserve every local commit and file. Never pull, merge, rebase, reset,
   force-push, change branches, or bypass hooks.
5. If the current branch is the remote default branch, state that explicitly.
   The user's invocation is permission to perform an ordinary push, not to
   bypass branch protection.

## Push

1. Record the local tip and the commits not yet present at the destination.
2. Push the current branch without any force option:
   - when the configured upstream is `origin/<current-branch>`, use it;
   - when no upstream exists, push to the same-named branch on `origin` and
     set that branch as upstream.
3. If the push is rejected, preserve the repository state and report the exact
   rejection. Do not retry through another integration operation.
4. Verify that the remote destination tip equals the local tip and that the
   upstream is `origin/<current-branch>`.

## Output

Report the local and remote branch names, previous and resulting upstream,
pushed commit range and final tip, whether the branch is the remote default,
and any remaining staged, unstaged, or untracked files. Do not claim full
success until the remote tip is verified.

Opening, pushing, or updating a branch does not approve or complete a work item
and does not publish a component contract.
