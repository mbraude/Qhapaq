---
name: work-branch-start
description: "Optionally create or select a safe Git work branch for a Qhapaq specification, implementation, or bug scope. Use when the user wants branch isolation, pull-request review, or to move current scoped changes off the default branch."
argument-hint: "<spec-id, work-item-id, bug, or branch-name>"
---

# Start a Work Branch

## Contract

Read [AGENTS.md](../../../AGENTS.md) and the branch guidance in the
[workflow guide](../../../docs/development/spec-driven-workflow.md). Resolve the
requested work scope and its owning specification or bug description. This
skill manages branch context only. It does not edit work artifacts, change
item status, approve, commit, stash, push, merge, rebase, reset, or discard
files.

## Procedure

1. Inspect the current branch, configured upstream, `origin`, default branch,
   complete working-tree status, and unresolved Git operations. Stop for a
   merge, rebase, cherry-pick, or revert in progress.
2. Resolve the target scope and confirm that the user wants a work branch.
   Recommend one for multi-commit work, file moves, disruption across shared
   surfaces, or pull-request review. Any change may remain on the explicitly
   intended current branch, including the default branch.
3. Derive a concise candidate such as `spec/0008-repository-organization` or
   `bug/<description>`. Never infer a different target when the user supplied
   an exact branch name. If the target or base branch is ambiguous, ask.
4. Inspect every staged, unstaged, and untracked change. Permit carrying
   uncommitted files only when all changes coherently belong to the requested
   scope and the user explicitly confirms branch creation. Unrelated,
   sensitive, generated, or unreviewable changes block switching.
5. If already on a suitable named branch, report a no-op. Otherwise create the
   new branch from the current committed `HEAD`. Do not switch to another
   existing branch with dirty files. Never overwrite an existing branch or
   recreate it at a different revision.
6. Verify that the branch is attached, every preexisting working-tree change
   remains present, and no new file change appeared. Do not configure an
   upstream until a later commit-and-push workflow pushes the branch.

## Output and stop

Report the base and resulting branches, target scope, carried working-tree
files, upstream state, and next workflow action. State that branch creation
does not approve, complete, commit, or push any work.

Evaluation: unrelated dirty changes block switching; coherent target changes
remain byte-identical; an existing suitable branch is not recreated; no
lifecycle metadata changes merely because a branch exists.
