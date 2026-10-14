---
name: work-runbook-sync
description: "Generate or refresh a tracked, dependency-ordered Qhapaq workflow runbook. Use when creating a tabular checklist for one or more specifications, updating runbook status, or recalculating exact next skill commands after work items, readiness, approvals, or source snapshots change."
argument-hint: "<primary-spec-id> [include=<spec-id,...>]"
---

# Synchronize a Work Runbook

## Contract

Apply [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), and the
[runbook template](../../../work/templates/runbook.md); read each only if it is
not already in the current context. Resolve every selected plan and all
transitive prerequisites through the facts helper below, reading source
excerpts only where a judgment requires them. Generate or refresh
`work/<primary-id>/runbook.md`.

## Facts helper

Run the helper once per invocation before any other resolution; every mode
except `--write` is read-only:

```text
python .agents/skills/work-runbook-sync/scripts/runbook_facts.py <primary-spec-id> [--include <spec-id>,<spec-id>] --open
```

`--open` omits settled items (cancelled, or complete with explicit date
evidence) whose rows it can render exactly; drop it only when you need their
facts. Two further modes, each a separate invocation over the same inputs:

The output modes `--open`, `--rows`, `--json`, `--check`,
`--judgments-template`, and `--write` are mutually
exclusive. Replace the mode flag for each invocation; do not append a second
mode to the initial command. For example, from the repository root:

```powershell
python .agents\skills\work-runbook-sync\scripts\runbook_facts.py 0007 --open
python .agents\skills\work-runbook-sync\scripts\runbook_facts.py 0007 --rows
python .agents\skills\work-runbook-sync\scripts\runbook_facts.py 0007 --check
```

Keep the same primary ID and `--include` arguments in all three invocations.

- `--rows` prints the table skeleton: exact rows for settled items and rows
  with `<command>` and `<status>` placeholders, in dependency order, for open
  items. Fill only the placeholders and any description you must judge.
- `--check` validates an existing runbook against current inputs: digest and
  file count, primary scope, column count, link targets, item coverage,
  settled-row semantics, open-row prerequisites, dependency order, known skill
  names, and that `Next command` and `Also eligible` appear in rows. It exits 1
  with findings. A digest-only finding means inputs changed; any other finding
  means the runbook is malformed or out of date.
- `--judgments-template` prints a JSON file listing each open item with
  `<judge>` placeholders for `command` and `status`, a suggested value where
  the facts determine one, and per-item hints (readiness coverage, plan
  approval, changed reviewed hashes). `--write [--judgments FILE]` renders the
  complete runbook, writes it only when content other than generation metadata
  changed (otherwise it reports a no-op), and runs `--check`. It exits 2
  without writing when a judgment is missing, names an unknown item or skill,
  or places a gate before an unknown row.
- When any in-scope plan is stale or missing, `--write` without `--judgments`
  renders a gate-mode runbook: a `SYNC SPEC-NNNN` gate with
  `/work-plan-sync NNNN` per stale plan, and every open row blocked until
  those plans are synchronized. This needs no item judgments.

Never hand-render the runbook or write ad hoc rendering scripts; use `--write`.
Use `--help` for flag details instead of reading the script source.

Source currentness is reported per recorded hash as `current`, `missing`,
`stale`, `evidence-only` (the recorded bytes differ only in status or review
evidence sections, so material content is unchanged), or
`stale-material-unchanged` (recorded bytes cannot be recovered, but the
material at the recorded revision matches). A work-item, plan, or readiness source that
records `material_sha256` is judged only by that hash and is never
`evidence-only` or `stale-material-unchanged`. Those two states arise only for
older work-item records without it; they are facts for you to judge against
the consuming record's rules, not automatic passes, and the record's next
reassessment should add `material_sha256`. A plan or readiness record whose
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
    Otherwise save `--judgments-template` output to a temporary file outside
    the repository, replace every `<judge>` (verify or override suggestions),
    add readiness, approval, or reconciliation gates as `gates` entries with a
    `before` item ID, and run `--write --judgments <file>`. Fix any exit-2
    errors and rerun. The helper replaces derived metadata and the table,
    preserves no manual row edits, derives `Next command`, `Also eligible`, and
    summary counts from the rendered rows, and reports a no-op when only
    generation metadata would change. Delete the temporary file.
11. `--write` runs `--check`; resolve every finding. Confirm the absence of
    dependency cycles from the facts output. Invoke
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
