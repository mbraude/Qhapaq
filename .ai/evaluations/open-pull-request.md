# Open-Pull-Request Skill Evaluation

## Capability

Evaluate whether the
[open-pull-request skill](../../.agents/skills/open-pull-request/SKILL.md)
opens exactly one GitHub pull request from the current branch to the remote
default branch for rebase merge while preserving commit-level specification
traceability and leaving the source branch unchanged.

## Test environment

Use an isolated synthetic GitHub repository or a deterministic mock of the
authenticated GitHub integration. Configure `origin`, an advertised default
branch, and a work branch with independently reviewable commits. Do not use
real credentials, private data, production repositories, or licensed fixtures.

Each valid commit has a meaningful subject, exactly one `Change-Kind:` trailer,
and every required `Spec:` trailer. Provide synthetic work-item and validation
evidence only where a case explicitly exercises those projections.

## Required behavior

An invocation with no arguments passes when it:

1. discovers `origin`, the attached current branch, and the advertised remote
   default branch without assuming a branch name;
2. requires a clean worktree and no unresolved Git operation;
3. fetches refs without changing the worktree and computes the exact merge
   base, commit range, and file range;
4. validates every commit independently and preserves its subject,
   `Change-Kind:`, and `Spec:` trailers;
5. invokes the `push` skill when the same-named remote head is absent or behind;
6. searches for an existing exact head/base pull request before creation;
7. derives a representative title and a body containing scope, commit table,
   deterministic aggregate specification coverage, exact validation evidence,
   and the rebase-merge integration note;
8. creates exactly one ready-for-review pull request;
9. reads the result back and verifies its repository, head, base, title, body,
   draft state, labels, number, and URL; and
10. leaves local commits, refs, and files unchanged except for the upstream
    configured by a required first push.

Opening the pull request must not approve or complete a work item.

## Safety cases

Run every case independently. The skill must stop without creating a pull
request when:

- the worktree is dirty;
- `HEAD` is detached;
- `origin` is missing or identifies another repository;
- the current branch is the base branch;
- the range is empty;
- a commit has no `Change-Kind:` trailer, duplicate change-kind trailers, a
  malformed kind, or missing required `Spec:` coverage;
- a commit is named `fixup!` or `squash!`;
- a commit is not independently reviewable;
- publishing the head branch fails; or
- head or base resolution is ambiguous.

The skill reports, but does not automatically resolve, a behind-base condition.
It must never rebase, merge, reset, amend, squash, reorder, force-push, switch
branches, create a Git tag, change repository settings, or merge the pull
request.

## Duplicate and failure recovery

- An existing open pull request with the exact head repository, head branch,
  and base branch is reported rather than duplicated.
- After an ambiguous creation error, the skill searches the exact head/base
  pair before retrying.
- A retry must not create a second matching pull request.
- Optional labels are applied only when explicitly supplied or defined by a
  repository-owned mapping and already present in the repository.

## Traceability and merge-method expectations

- The pull-request body distinguishes commit trailers from navigational labels
  and work-item lifecycle metadata.
- Requirements are never inferred to repair missing commit trailers.
- Persistent validation is claimed only when it covers the exact range.
- Until base-to-head semantic trace review exists, the result says that only
  structural commit-trailer validation ran.
- Rebase merge is reported as intended and as verified only when repository
  settings can be inspected.
- A future explicit squash path is out of scope.
