---
name: approve-commit
description: "Approve an exact ready-for-review Qhapaq work item or scoped specification-readiness record through the shared approval workflow, then commit the approved changes locally without pushing. Use when approval and a local commit are both requested; never publishes component contracts."
argument-hint: "[work-item-id or readiness-record-path] [skip-build-and-test=true|false]"
---

# Approve and Commit a Reviewed Qhapaq Outcome

Use this skill only when the user intends to approve an exact reviewed outcome
and immediately create its local commit without pushing.

## Workflow

1. Invoke [approve](../approve/SKILL.md) with the target and every user-supplied
   argument. Do not duplicate or replace its target resolution, exact-snapshot
   review, validation, explicit approval, evidence recording, or commit-message
   generation.
2. Verify that the complete worktree still contains exactly the approved scope
   and unchanged snapshot. The `git_preflight.py` run that `approve` performs
   after recording evidence is that verification; rerun it only if anything
   touched the worktree since, and then require the same `snapshot_id`.
   Include the approval evidence in the same commit. If
   concurrent, unrelated, or material changes appeared, stop without staging
   or committing. Supply those preflight facts, the `spec-trace-check`
   verdict, and its trailers to `commit` so it collects none of them again
   and does not re-read content `approve` already reviewed.
3. Invoke [commit](../commit/SKILL.md), supplying the complete message generated
   by `approve` and the matching validation mode. For implementation/code work,
   use `skip-build-and-test=false`. For design/specification-only work already
   validated by `approve`, use `skip-build-and-test=true`; approval's trace and
   documentary checks remain required.
4. Require `commit` to verify the supplied message against the final staged
   snapshot and approved trailers. If validation or commit fails, preserve the
   recorded approval and report the exact failure. Do not push or invoke
   `approve` again unless the material snapshot changes.

## Output

Report the target and approved scope, exact snapshot, recorded approval
evidence, validation performed, commit hash and subject, and any remaining
blockers. State explicitly that the commit is local and was not pushed.
Distinguish approval, local commit, readiness, and contract publication.
