---
name: approve-commit-push
description: "Approve and locally commit an exact ready-for-review Qhapaq work item or scoped specification-readiness record through the shared approval workflow, then push the resulting commit to origin. Use when the user asks to approve, commit, and push; never publishes component contracts."
argument-hint: "[work-item-id or readiness-record-path] [skip-build-and-test=true|false]"
---

# Approve, Commit, and Push a Reviewed Qhapaq Outcome

Use this skill only when the user intends to approve an exact reviewed outcome,
commit its related changes, and push the resulting commit to `origin`.

## Preconditions

Before invoking `approve-commit`, confirm that:

- the repository has an `origin` remote;
- `HEAD` is attached to the explicitly intended delivery branch;
- the configured upstream, when present, has been inspected; and
- the intended remote branch is unambiguous.

Stop before approval if any push precondition fails. Never create or switch
branches, rewrite history, force-push, bypass hooks, or infer a differently
named remote branch.

## Workflow

1. Invoke the repository's `approve-commit` skill with the target and every
   user-supplied argument. Do not duplicate or replace any part of its target
   resolution, exact-snapshot review, validation, explicit approval, evidence
   recording, or commit workflow.
2. After the local commit succeeds, verify that `HEAD` is still attached to the
   same branch and that the push destination remains unchanged.
3. Push the current branch to `origin`:
   - use the configured upstream when it points to `origin` and the current
     branch;
   - otherwise set `origin/<current-branch>` as the upstream on the first push;
   - never push to a differently named branch unless the user explicitly
     requests it; and
   - never use a force option.
4. If the push is rejected, preserve the recorded approval and local commit,
   and report the exact rejection. Do not pull, rebase, merge, reset, retry with
   force, undo approval evidence, or invoke `approve-commit` again.

## Output

Report the target and approved scope, exact snapshot, recorded approval
evidence, validation performed, commit hash and subject, and pushed remote
branch. If pushing fails, distinguish the successful approval and local commit
from the failed remote delivery. Distinguish readiness from component-contract
publication, which this skill never performs. Do not report full success unless
approval, commit, and push completed.
