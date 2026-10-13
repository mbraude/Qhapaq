---
name: work-runbook-sync
description: "Generate or refresh a tracked, dependency-ordered Qhapaq workflow runbook. Use when creating a tabular checklist for one or more specifications, updating runbook status, or recalculating exact next skill commands after work items, readiness, approvals, or source snapshots change."
argument-hint: "<primary-spec-id> [include=<spec-id,...>]"
---

# Synchronize a Work Runbook

## Contract

Read [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), the
[runbook template](../../../work/templates/runbook.md), every selected plan,
and all transitive prerequisites. Generate or refresh
`work/<primary-id>/runbook.md`.

The runbook is a tracked, derived view. Plans, work items, readiness records,
approval evidence, and authoritative sources remain the status and eligibility
authority. Never infer completion from a runbook row, edit authoritative status
to match a runbook, execute work, approve an outcome, commit, or push.

## Scope

- The first argument is the primary specification and owns the runbook path.
- Include every item in the primary plan.
- `include=` adds every item from the named plans when one runbook coordinates
  multiple specification outcomes.
- Always include transitive cross-plan prerequisites, even when their plans
  were not explicitly included. Do not include unrelated items from those
  prerequisite plans.
- If a requested plan is missing, include a synthetic synchronization gate
  with the exact `work-plan-sync` command rather than creating the plan.

## Procedure

1. Inspect the branch and complete worktree. Read an existing runbook only to
   obtain its declared scope and freshness metadata; never trust its rows over
   current source records.
2. Resolve selected plans, their phase order, item records, readiness records,
   material plan approvals, review evidence, artifacts, and all transitive
   prerequisites. Check source currentness, IDs, ownership, references,
   cancelled dependencies, and cross-plan cycles. For every implementation
   slice, resolve its exact file manifest and determine which specification
   documents it may edit. Check readiness against both the slice's governing
   requirements/capabilities and those planned edits; a readiness record that
   authorizes planning only, excludes edits, omits a target specification, is
   stale, or is otherwise not explicitly approved for implementation does not
   satisfy this gate.
3. Build a stable dependency order. Prerequisites precede dependents. Among
   otherwise independent work, order by:
   1. freshness or structural repair gates;
   2. pending review of an already produced outcome;
   3. in-progress work;
   4. decisions;
   5. readiness assessment and approval;
   6. implementation decomposition and plan approval;
   7. executable implementation slices;
   8. aggregate milestones;
   9. requested-spec order, plan phase order, item order, and stable ID.
4. Create synthetic rows only for workflow gates that do not have their own
   work-item identity, such as plan synchronization, scoped readiness,
   implementation-plan approval, or completion review. Give each a stable,
   descriptive identity such as `SYNC SPEC-0008` or
   `READINESS SPEC-0008 conformance-artifacts-implementation`. Do not persist
   synthetic status anywhere else. Readiness gates for a slice must identify
   the slice and the specification documents and capabilities they cover. Keep
   separate gates for readiness assessment and approval when the assessment
   is ready-for-review.
5. For each row, derive exactly one current command:

   | Current condition | Skill command |
   | --- | --- |
   | Missing or stale plan/source input | `/work-plan-sync <spec-id>` |
   | Eligible decision | `/spec-next <spec-id> item=<id>` |
   | Decision or delivered slice ready for review | `/approve <id>` |
   | Decisions complete and named readiness absent or stale | `/spec-readiness <spec-id> scope=<scope>` |
   | Readiness ready for review | `/approve <readiness-record-path>` |
   | Milestone requiring concrete slices | `/implementation-plan <spec-id> item=<id>` |
   | Slice lacks current, approved implementation readiness covering its requirements and every specification document its manifest may edit | `/spec-readiness <spec-id> scope=<slice-scope>-implementation` |
   | Slice implementation readiness is ready for review | `/approve <readiness-record-path>` |
   | Concrete slice has current, approved implementation readiness but lacks plan approval | `/approve-implementation-plan <spec-id> item=<id>` |
   | Plan-approved, dependency-ready slice has current, approved implementation readiness | `/implement-next <spec-id> item=<id>` |
   | Aggregate milestone awaiting verification | The exact applicable planning or approval command; never `implement-next` |
   | Complete or cancelled item | Empty command |

   Before emitting an implementation-plan approval command, require a current,
   explicitly approved readiness assessment for the slice's implementation
   scope. It must cover the slice's governing requirements/capabilities and
   every specification document the manifest may edit. A readiness approval
   that only authorizes planning or explicitly excludes those edits is
   insufficient, even when it is current and shares requirement IDs. If no
   suitable record exists, is stale, or its coverage is ambiguous, create a
   readiness gate ahead of plan approval; do not mark the slice ready for plan
   approval. Apply the same readiness precondition to implementation execution,
   in addition to plan approval, dependency readiness, and entry-artifact
   checks. If no command is currently safe, leave it empty and explain the
   blockers. Never emit `implement-next` for `granularity: milestone`.
6. Populate the runbook table with exactly these columns:

   | Work item | Description | Skill command | Status | Date Completed | Pre-requisites / blocked by |
   | --- | --- | --- | --- | --- | --- |

   Use repository-relative links for real work items. Put commands in inline
   code so they are directly copyable. Use `<br>` between multiple blockers.
   Status must distinguish persisted lifecycle state from derived eligibility,
   for example `Open - ready`, `Open - blocked`, `Ready for review`,
   `Complete`, `Cancelled`, or `Gate - refresh required`.
7. Populate `Date Completed` only from explicit completion/review evidence for
   an item whose persisted status is `complete`. Use ISO `YYYY-MM-DD`. Use an
   em dash for other rows. If a complete item lacks a defensible completion
   date, write `Unknown - evidence missing` and report the structural finding;
   do not infer a date from Git history or file timestamps.
8. Record the primary specification, explicit included specifications,
   transitive prerequisite owners, generation time, branch, `HEAD`, source-file
   count, and a SHA-256 digest over the sorted repository-relative paths and
   exact bytes of every plan, item, readiness record, and authoritative source
   used. Exclude the runbook itself. Label working-copy snapshots accurately.
9. Set `Next command` above the table to the first safe actionable row. A
   command is safe only if every prerequisite for that command—not merely for
   the eventual implementation—is satisfied. In particular, never recommend
   plan approval before current implementation readiness covers the slice's
   planned edits. When stale or invalid inputs affect eligibility, the next
   command must repair or reconcile them; do not show downstream approval or
   execution as trustworthy. If there are multiple independent eligible rows,
   choose by the stable order and list the others under `Also eligible`.
10. Write the complete runbook from the template. Regeneration replaces the
    derived metadata and table, preserving no manual row edits. If inputs and
    rendered content other than generation metadata are unchanged, report a
    no-op rather than rewriting the file solely to change its timestamp.
11. Validate table links, commands, item coverage, dependency order, source
    metadata, and the absence of dependency cycles. Invoke
    [spec-trace-check](../spec-trace-check/SKILL.md) for a changed runbook.

## Output and stop

Report the runbook path, primary and included scopes, item and gate counts,
source digest, structural findings, first actionable row, and exact next
command. Do not execute that command.

Evaluation: regeneration is idempotent for unchanged inputs; every prerequisite
precedes its dependent; readiness must explicitly authorize the slice's planned
edits before plan approval or implementation; stale or insufficient readiness
suppresses unsafe eligibility; milestones never receive `implement-next`;
completion dates come only from explicit evidence; the runbook never becomes an
independent status authority.
