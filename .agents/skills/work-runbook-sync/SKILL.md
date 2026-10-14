---
name: work-runbook-sync
description: "Generate or refresh a tracked, dependency-ordered Qhapaq workflow runbook. Use when creating a tabular checklist for one or more specifications, updating runbook status, or recalculating exact next skill commands after work items, readiness, approvals, or source snapshots change."
argument-hint: "<primary-spec-id> [include=<spec-id,...>]"
---

# Synchronize a Work Runbook

## Contract

Apply [AGENTS.md](../../../AGENTS.md). This skill states every workflow rule it
needs; do not read the
[workflow guide](../../../docs/development/spec-driven-workflow.md) or the
[runbook template](../../../work/templates/runbook.md), because `--write`
renders the template's structure itself. Resolve every selected plan and all
transitive prerequisites through the facts helper below, reading source
excerpts only where a `<judge>` row requires them. Generate or refresh
`work/<primary-id>/runbook.md`.

## Facts helper

Start every invocation with exactly one command, before any other resolution:

```text
python .agents/skills/work-runbook-sync/scripts/runbook_facts.py <primary-spec-id> [--include <spec-id>,<spec-id>] --judgments-template --out <temp-file>
```

Use a file outside the repository, for example
`$env:TEMP\qhapaq-<id>-runbook.json`. It writes the judgments template and
prints a compact summary (typically 1–3 KB): stale plans, structural findings,
cycles, working-copy inputs, whether runbook inputs changed, suggested gates,
every row with a determined command or blocker and the basis for it, each
`<judge>` row with its hints, and a count of rows blocked only by incomplete
prerequisites. Treat that summary as the facts for this invocation: do not
view the template file, do not run `git status` (the summary reports
working-copy inputs and the branch is recorded on write), and do not run
`--open`, `--rows`, or `--json` unless a `<judge>` row needs a fact the summary
omits.

The output modes `--open`, `--rows`, `--json`, `--check`,
`--judgments-template`, and `--write` are mutually exclusive; keep the same
primary ID and `--include` arguments across invocations. Without `--include`,
the helper keeps the existing runbook's `included_specs`; pass `--include`
only to change the scope (an empty value clears it), so do not read the
runbook to find it. Use `--help` for flag
details instead of reading the script source.

- Suggestions implement the command table in step 5 wherever the facts fully
  determine it: dependency-blocked rows, outcomes ready for review, eligible
  decisions, milestones without planned child slices
  (`/implementation-plan`), and slices whose single scope-matched readiness
  record is stale, not assessed, ready for review, or current but blocked (a
  `READINESS` gate before the slice, with a generated description; a blocked
  record gets status `Gate - blocked`) or is current, approved,
  covers every manifest specification edit, mentions every slice requirement,
  and is not limited to planning (`/approve-implementation-plan`, or
  `/implement-next` when plan approval is recorded with unchanged reviewed
  hashes). A slice with no candidate readiness record gets an assessment gate.
  A record's planning limit comes from its `authorizes` frontmatter field
  when present (`implementation` or `planning`); otherwise from planning-only
  language in a sentence that does not describe another or an older record.
- Every other open row is `<judge>`: aggregate milestones whose child slices
  exist, slices with ambiguous or partially covering readiness, and
  hints such as `planning-only-language` (shown with its sentence excerpt) or
  `unmentioned_requirements` (requirement IDs the record does not name
  literally, which ranges such as `R-0008-008–015` can cause). Hints list only
  scope-matched readiness records when one exists. Hints prompt
  judgment; they are not verdicts. Read only the cited excerpt you need.
- `--write [--judgments FILE|-]` renders the complete runbook from the
  suggestions overlaid with your overrides, writes it only when content other
  than generation metadata changed (otherwise it reports a no-op), runs
  `--check`, and prints the resulting `Next command` and `Also eligible`.
  Overrides list only what you decide: an `items` entry merges over that
  row's suggestion, a `gates` entry replaces the same-ID suggested gate or adds
  one (with `before: <item id>`), and `{"id": ..., "drop": true}` removes a
  suggested gate. Pass them on standard input with `--judgments -`, for
  example by piping a PowerShell here-string or `ConvertTo-Json` output; never
  write ad hoc scripts to edit the template. `items` is an object keyed by
  item ID (a list of entries with `id` is also accepted) and `gates` is a
  list; any other shape exits 2. It exits 2 without writing when a
  `<judge>` remains unresolved, a judgment names an unknown or settled item, a
  gate precedes an unknown row, or a command names an unknown skill, an
  unknown `item=`, or a spec argument other than that item's specification.
- When any in-scope plan is stale or missing, `--write` without `--judgments`
  renders a gate-mode runbook: a `SYNC SPEC-NNNN` gate with
  `/work-plan-sync NNNN` per stale plan, and every open row blocked until
  those plans are synchronized. This needs no item judgments.
- `--check` validates an existing runbook against current inputs: digest and
  file count, primary scope, column count, link targets, item coverage,
  settled-row semantics, open-row prerequisites, dependency order, skill names
  and spec arguments, and that `Next command` and `Also eligible` appear in
  rows. It exits 1 with findings. A digest-only finding means inputs changed.
- `--open` and `--rows` print the full facts and the table skeleton; `--json`
  prints everything. They are for investigation only.

Never hand-render the runbook or write ad hoc rendering scripts; use `--write`.

Source currentness is reported per recorded hash as `current`, `missing`, or
`stale`. A work-item, plan, or readiness source that records
`material_sha256` is judged by that hash. For a legacy work-item source without
`material_sha256`, the shared verifier compares recoverable recorded bytes (or
the recorded revision when those bytes are unavailable) by material hash;
unchanged material is `current` and the output identifies the legacy fallback.
This avoids reopening readiness or plan approval for status/evidence-only
changes while still requiring reassessment when the source's material changes.
A plan or readiness record whose
`process_version` is missing or older than the guide's reports a
`process_version` source in state `process-missing` or `process-outdated`; a
cited runbook or diagram reports `derived-view`. Neither is current.

It reads exact working-copy bytes and reports, with line references: transitive
item selection and owners; plan and readiness source currentness; dependency
state; a stable topological order with cycle detection; plan-approval state and
changed reviewed hashes; manifest specification edits; candidate readiness
records and their coverage of those edits; completion-date evidence; the
source-set digest; working-copy inputs; and structural findings. It keeps no
persistent state and grants no trust across invocations.

Treat its output as the retained input snapshot for this invocation. Do not
re-derive what it reports by reading whole plans, items, or readiness records,
or by writing ad hoc hash or parsing scripts. Read only the line-referenced
excerpts that a judgment requires, such as readiness coverage or
planning-only scope, synthetic gates, weak date evidence, or plan-approval
currency. Its hints, including `planning-only-language`, are prompts for that
judgment, not verdicts. If the helper fails or reports something you cannot
reconcile with the source excerpt, stop and report it; never fall back to
guessed values.

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

1. Take branch and worktree facts from the helper summary rather than separate
   Git commands. If it reports `runbook inputs unchanged: True` (the digest
   covers every selected input, so a different scope cannot match), run
   `--check`;
   when that passes, report the runbook as current and stop without judging or
   rewriting rows. Otherwise never trust existing runbook rows over current
   source records, and do not read the existing runbook.
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
   Within this invocation, read each exact input snapshot once and retain its
   bytes, parsed fields, and computed digest for every later currentness,
   dependency, rendering, and source-set operation. Do not reopen or rehash an
   unchanged input merely because another row consumes it. Before writing,
   confirm that retained working-copy inputs still identify the current bytes;
   if a relevant input changed during synchronization, discard the affected
   retained results and resolve them again, rerunning the facts helper when
   needed. This reuse is invocation-local and creates no persistent cache or
   cross-invocation trust.
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
   `Complete`, `Cancelled`, `Gate - refresh required`, or `Gate - blocked`.
7. Populate `Date Completed` only from explicit completion/review evidence for
   an item whose persisted status is `complete`. Use ISO `YYYY-MM-DD`. Use an
   em dash for other rows. If a complete item lacks a defensible completion
   date, write `Unknown - evidence missing` and report the structural finding;
   do not infer a date from Git history or file timestamps.
8. Record the primary specification, explicit included specifications,
   transitive prerequisite owners, generation time, branch, `HEAD`, source-file
   count, and a SHA-256 digest over the sorted repository-relative paths and
   exact bytes of every plan, item, readiness record, and authoritative source
   used. Exclude the runbook itself. Use the facts helper's
   `source_file_count` and `source_set_sha256`, whose rule is SHA-256 over the
   sorted lines `<path>\n<SHA-256 of exact bytes or MISSING>\n`. Label
   working-copy snapshots accurately.
9. Set `Next command` above the table to the first safe actionable row. A
   command is safe only if every prerequisite for that command—not merely for
   the eventual implementation—is satisfied. In particular, never recommend
   plan approval before current implementation readiness covers the slice's
   planned edits. When stale or invalid inputs affect eligibility, the next
   command must repair or reconcile them; do not show downstream approval or
   execution as trustworthy. If there are multiple independent eligible rows,
   choose by the stable order and list the others under `Also eligible`.
10. Render with the helper. If the facts report a stale or missing in-scope
    plan, run `--write` alone (gate mode) and skip item judgments: no
    downstream row is trustworthy until those plans are synchronized.
    Otherwise review the summary's suggestions and decide each `<judge>` row,
    adding readiness, approval, or reconciliation gates with a `before` item
    ID where needed. When every suggestion stands and nothing is `<judge>`, run
    `--write` alone; otherwise pass only your overrides through
    `--write --judgments -`. Fix any exit-2 errors and rerun. The helper
    replaces derived metadata and the table, preserves no manual row edits,
    derives `Next command`, `Also eligible`, and summary counts from the
    rendered rows, and reports a no-op when only generation metadata would
    change. Delete the temporary template file.
11. `--write` runs `--check` and prints the resulting `Next command` and
    `Also eligible`; resolve every finding and report those values without
    reopening the runbook. Confirm the absence of dependency cycles from the
    summary. Invoke [spec-trace-check](../spec-trace-check/SKILL.md) for a
    changed runbook.

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
