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

1. Fetch the destination ref when it exists, without changing the worktree,
   then collect the push facts once:

   ```text
   python .agents/scripts/git_preflight.py --push --fetch
   ```

   `--fetch` runs `git fetch origin <current-branch>` first and reports a
   fetch failure as a fact; do not run separate fetch or `rev-parse` commands.

   It reports the current branch, `origin`, the configured upstream, the remote
   default branch, unresolved Git operations, exact ahead and behind counts,
   and the commits a push would publish with their `Change-Kind:` trailers. It
   exits `1` with a `blocking:` list when `HEAD` is detached, `origin` is
   absent, an operation is unresolved, the upstream is not
   `origin/<current-branch>`, the branch is behind, or nothing would be
   pushed. Use these facts instead of separate Git inspection commands. Check
   the working-tree status only for the final report.
2. Stop when:
   - `HEAD` is detached;
   - `origin` is absent;
   - a merge, rebase, cherry-pick, or revert is in progress;
   - the configured upstream names another remote or a differently named
     branch; or
   - the destination cannot be resolved exactly as
     `origin/<current-branch>`.
3. Stop when the local branch is behind or diverged. Report the remote tip and
   preserve every local commit and file. Never pull, merge, rebase, reset,
   force-push, change branches, or bypass hooks.
4. If the current branch is the remote default branch, state that explicitly.
   The user's invocation is permission to perform an ordinary push, not to
   bypass branch protection.

## Push

1. Record the local tip and the commits not yet present at the destination
   from the push facts.
2. Push the current branch without any force option:
   - when the configured upstream is `origin/<current-branch>`, use it;
   - when no upstream exists, push to the same-named branch on `origin` and
     set that branch as upstream.
3. If the push is rejected, preserve the repository state and report the exact
   rejection. Do not retry through another integration operation.
4. Verify that the remote destination tip equals the local tip and that the
   upstream is `origin/<current-branch>` with one
   `python .agents/scripts/git_preflight.py --verify-pushed` run; it exits `1`
   when they differ.

## Output

Report the local and remote branch names, previous and resulting upstream,
pushed commit range and final tip, whether the branch is the remote default,
and any remaining staged, unstaged, or untracked files. Do not claim full
success until the remote tip is verified.

Opening, pushing, or updating a branch does not approve or complete a work item
and does not publish a component contract.
