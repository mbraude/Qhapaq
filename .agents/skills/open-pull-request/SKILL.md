---
name: open-pull-request
description: "Validate, publish, and open a GitHub pull request from the current work branch to the remote default branch for rebase merge. Use when the user asks to open, create, or submit a PR; preserves commit-level Change-Kind and Spec trailers without rewriting the source branch."
---

# Open a Pull Request

Open one GitHub pull request from the current attached work branch to the
remote default branch. The skill requires no arguments. Discover `origin`, the
current head branch, and `origin`'s advertised default branch. Honor an
explicitly supplied base, title, or draft preference only after validating it;
otherwise derive them.

## Contract

This skill prepares a branch for review and opens a pull request intended for
rebase merge under
[R-0000-045](../../../SPEC.md#7-branching-changes-and-releases). It does not
commit changes, rebase or otherwise rewrite the source branch, merge the pull
request, approve or complete work items, create tags or releases, change
repository settings, or publish component contracts.

Pull-request descriptions and labels are review projections. Commit trailers
remain the specification-traceability authority, and work artifacts remain the
approval and lifecycle authority.

## Resolve the range

1. Inspect the complete working-tree status, current branch, `origin`,
   configured upstream, remote repository identity, remote default branch, and
   unresolved Git operations.
2. Stop when:
   - the working tree is not clean;
   - `HEAD` is detached;
   - `origin` is absent or is not the intended GitHub repository;
   - a merge, rebase, cherry-pick, or revert is in progress;
   - the head branch is the selected base branch;
   - the base branch does not exist on `origin`; or
   - head or base resolution is ambiguous.
3. Fetch the base and existing remote head refs without modifying the
   worktree. Compute their merge base and the exact
   `<merge-base>..HEAD` commit and file range. Stop when the range is empty.
4. Report when the head is behind the base. Do not merge, rebase, reset,
   force-push, or otherwise synchronize it automatically.

## Validate permanent commits

For every commit in oldest-to-newest range order:

1. Require a meaningful subject that is not a `fixup!` or `squash!` commit.
2. Require exactly one canonical `Change-Kind:` trailer using a kind defined
   by ADR-0004.
3. Require applicable `Spec:` trailers for `requirement`, `amendment`,
   `extension`, `bug`, and `editorial` commits. Validate their grammar and
   retain every reference in the review summary.
4. Treat each commit as permanent default-branch history. Stop if a commit is
   not independently reviewable; never repair, amend, squash, or reorder it.
5. Use persistent validation and approval evidence only when it covers the
   exact included snapshot. Do not turn an expected CI run into a passing
   result.

Run the repository specification trace check in an explicit base-to-head mode
when that mode exists. Until then, report commit-trailer validation separately
from semantic range validation and never claim that the latter ran.

## Publish the head branch

If the local head is not present at the same-named `origin` branch or is ahead
of it, invoke the repository's `push` skill. Stop if `push` fails. Verify that
the remote head tip equals local `HEAD` before creating the pull request.

## Build review metadata

1. Derive a concise title and summary from the complete commit and file range,
   not only the tip commit.
2. Build the body with:
   - summary and explicit scope;
   - base, head, merge base, and included commits;
   - a commit table containing commit, subject, change kind, unambiguous work
     item when present, and `Spec:` coverage;
   - the deterministically ordered union of specification references;
   - exact validation and approval evidence;
   - compatibility, migration, or review notes supported by the range; and
   - an integration note that rebase merge must preserve each commit and its
     trailers.
3. State that opening or merging the pull request does not itself approve or
   complete a work item.
4. Never infer requirements from branch names, paths, labels, or prose when a
   commit trailer is missing.
5. Treat GitHub labels as optional navigation metadata. Apply only labels the
   user explicitly supplied or a future repository-owned mapping defines, and
   only when those labels already exist. Never create labels or Git tags.

## Create exactly one pull request

1. Search the target repository for an existing open pull request with the
   exact head repository, head branch, and base branch. If found, report it and
   do not create another.
2. Create the pull request through an authenticated GitHub integration. Use a
   ready-for-review PR when all required local gates pass; use draft only when
   the user explicitly requests it or persistent evidence identifies an
   incomplete review gate.
3. A creation error may have occurred after the server accepted the request.
   Search again by exact head and base before any retry. Never create a second
   matching pull request.
4. Read the resulting pull request back and verify repository, number, URL,
   title, body, base, head, draft state, and labels actually applied.
5. Verify that repository settings permit rebase merge when that information
   is available. Otherwise report the intended method as unverified; opening a
   pull request does not control its eventual merge method.

## Output

Report the pull request number and URL, repository, base and head, exact commit
range, aggregate specification coverage, validation evidence, draft state,
labels, intended rebase-merge method and whether it was verified, and any
behind-base condition. Distinguish branch publication from pull-request
creation and from eventual review or merge.
