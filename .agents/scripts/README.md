# Shared Workflow Scripts

Read-only, standard-library Python helpers shared by the repository
[skills](../skills/README.md). They perform the deterministic parts of the
[specification-driven workflow](../../docs/development/spec-driven-workflow.md)
so that agents spend reasoning only on judgment.

Scripts used by a single skill stay in that skill's `scripts/` folder and may
import [`qhapaq_work.py`](qhapaq_work.py) from here. Current examples are
[`runbook_facts.py`](../skills/work-runbook-sync/scripts/runbook_facts.py) and
[`build_and_test.py`](../skills/build-and-test/scripts/build_and_test.py),
which runs the locked build and unit tests and so is not read-only.

## Rules

- **Use a script when one exists.** When a step needs a value one of these
  scripts computes, run the script. Do not hand-compute, estimate, or write an
  ad hoc PowerShell or Python script for that value.
- **Propose a script for repeated work.** If a deterministic computation is
  needed in more than one invocation and no script covers it, propose adding
  one here instead of regenerating it each time.
- **Scripts report facts; skills decide.** Script output never grants
  approval, readiness, or eligibility, and never replaces a judgment that a
  skill assigns to the agent.
- **Fail closed.** If a script exits with an error you cannot explain from its
  output, stop and report it; never substitute a guessed value.
- **No persistent state.** Scripts read exact current bytes on every run and
  keep no cache, so their output is invocation-local evidence only.
- **Use the documented CLI exactly.** Run from the repository root. If a
  flag or argument order is unclear, inspect that script's `--help` before
  invoking it; do not infer one helper's syntax from another. Mutually
  exclusive output modes replace one another, rather than accumulating.

## Scripts

All paths are repository-relative and printed with `/` separators. Use
Windows path separators in PowerShell invocations. Where supported, `--json`
selects machine-readable output; its position follows the individual script's
CLI. For `work_hashes.py`, place it before the subcommand.

### `work_hashes.py`

Hashes and verifies work-record snapshots. Exit code `1` means a requested
file is missing or a verification found a mismatch.

| Command | Output |
| --- | --- |
| `files PATH...` | Full-byte SHA-256 of each file. |
| `sources PATH...` | Ready-to-paste frontmatter `sources` entries: `path`, `revision` (last commit touching the path, or `null` if untracked), `content_sha256` of the working-copy bytes, and, for decision and implementation work items, plans, and readiness records, `material_sha256`. Reports on stderr which paths differ from their revision. |
| `material ITEM...` | The material SHA-256 defined in the workflow guide for the record's kind: a plan or readiness record uses its own definition, and work items and other files use the work-item definition. |
| `verify RECORD...` | For a plan or readiness record, its `process_version` state (`current`, `process-missing`, or `process-outdated`), then each frontmatter source with one of the source states below. Work-item, plan, and readiness sources that record `material_sha256` are checked by material and marked `(material)`; process artifacts are marked `(process source)`; a cited runbook or diagram is `derived-view`; a cited reconciliation record is `reconciliation-record`. |
| `evidence [--section NAME] ITEM...` | Current-content comparisons for recorded material digests and path/hash rows. Two-column rows default to byte verification; three-column rows may specify `bytes`, `material`, or `baseline`. Work-item checkbox progress and lifecycle/evidence changes are accepted consistently in plan and delivery sections, including legacy digests. Changed manifest paths in `Plan approval` are `planned-output` for delivery review. Use `--section` for the relevant approval; a mismatch in a historical table does not revoke a completed approval. |
| `approval TARGET [--files PATH...]` | Verifies that a work item, plan, or readiness record is approvable (for a plan or readiness record, every recorded source and its `process_version` are current) and prints the ready-to-paste approval evidence block: an `Approved material SHA-256` line plus a path/hash table of `--files`. Exits 1 listing anything non-current, without printing a block. |
| `diff [--max-lines N] RECORD...` | For each non-current source, a unified diff from the recorded bytes (recovered from Git history, or the recorded revision) to the working copy, with added and removed line counts. `--max-lines 0` prints everything; the default is 200 per source. |
| `refresh [--stale] RECORD [PATH...] [--add PATH...] [--remove PATH...]` | The only writing command: rewrites the named recorded sources (or, with `--stale`, every non-current one) in the record's frontmatter in place with the current `revision`, `content_sha256`, and, for work items, plans, and readiness records, `material_sha256`; `--add` appends complete entries for new sources (refreshing any already recorded) and `--remove` deletes entries. Refuses unknown or missing paths, derived views, and a record naming itself, and writes nothing when any path is refused. Run it only after judging the delta. |

Paths may use globs, for example
`python .agents/scripts/work_hashes.py material "work/0008/implementation/I-0008-01*.md"`.

Source states are facts, not verdicts:

| State | Meaning |
| --- | --- |
| `current` | Current bytes match the recorded hash; a work-item, plan, or readiness source with `material_sha256` matches its current material hash; or a legacy work-item source without `material_sha256` has recoverable recorded bytes (or a recorded revision) whose material hash matches current content. Checkbox-state-only changes to a work item's acceptance criteria are progress metadata. Legacy fallback is reported as `material (legacy fallback)`. |
| `missing` | The file does not exist. |
| `stale` | Current bytes differ, and material content differs or cannot be compared; or a recorded `material_sha256` no longer matches. In plan-approval evidence, stale hashes for manifest outputs are instead `planned-output`; final delivery review must verify their exact current bytes. |
| `reconciliation-record` | The path is non-authoritative reconciliation history and cannot be a source. |

New work-item material digests normalize task-list checkbox state. Existing
checkbox-sensitive digests remain supported without rewriting approval
evidence. The runbook uses the same evidence comparison as `work_hashes.py`,
but requires unchanged manifest baselines before execution and does not
revalidate historical plan inputs for completed items.

Run the helper regression tests from the repository root:

```powershell
python -m unittest discover -s .agents\scripts\tests
```

### `plan_reconciliations.py`

Extracts legacy plan-embedded reconciliation sections and validates the
indexed record layout.

| Command | Output |
| --- | --- |
| `extract [PLAN...]` | Prepares every requested plan migration before writing, splits dated events into bounded records, creates the index, replaces embedded history with one index link, and refuses any material-hash change or target collision. Defaults to every instantiated plan. |
| `normalize [PLAN...]` | Moves an existing reconciliation index to the plan's final section without changing its material hash. Defaults to every instantiated plan. |
| `check [PLAN...]` | Verifies one reconciliation index per plan, no remaining embedded reconciliation/evidence sections, resolvable index links, complete record indexing, and record back-links. Defaults to every instantiated plan. |
### `spec_fingerprints.py`

Prints `R-…@xxxxxx` fingerprints for requirement blocks using the
[`spec-trace-check`](../skills/spec-trace-check/SKILL.md) grammar, with each
block's line and retired state. Defaults to every specification.

| Argument | Effect |
| --- | --- |
| `PATH...` | Limit to these specification files. |
| `--rev REV` | Read text at a Git revision instead of the working copy. |
| `--id ID...` | Print only these requirements. |
| `--refs ID...` | List repository references to these requirements and whether each is current. |

### `trace_facts.py`

Computes the deterministic parts of
[`spec-trace-check`](../skills/spec-trace-check/SKILL.md) steps 1–4 for every
change since `HEAD`: scope and file classes, identifier and placement errors,
changed, retired, and removed blocks, stale repository references, and code
reference and waiver grammar on changed lines. Its `result` line is either a
final `PASS` (no changes, or the maintenance fast path when only non-product
files changed), `FAIL - mechanical errors`, or `INCOMPLETE`, which means the
skill's judgment steps remain. Exit code `1` means mechanical errors.

### `git_preflight.py`

Git facts for the commit, push, approval, and branch skills: branch, default
branch, `origin`, upstream and ahead/behind counts as of the last fetch,
unresolved operations, and recent subjects.

| Mode | Output |
| --- | --- |
| *(default)* | The selected commit snapshot (staged index, or all changes when nothing is staged) with status and large, binary, or generated hints; excluded paths; likely secrets on added lines (pattern name and line, never the value); and a `snapshot_id`. Blocks on a detached `HEAD`, unresolved operation, unmerged paths, no changes, or a likely secret. |
| `--push` | The commits a push would publish with their `Change-Kind:` trailers. Blocks on a detached `HEAD`, missing `origin`, unresolved operation, upstream other than `origin/<branch>`, a branch behind its upstream, or nothing to push. Add `--fetch` to run `git fetch origin <branch>` first. |
| `--verify-pushed` | After a push: whether `HEAD` equals `origin/<branch>`. Exits `1` when it does not. |

`snapshot_id` is SHA-256 over the sorted selected paths and their content
blobs. It is unchanged by `git add` of the same content, so equal values prove
the staged index is the snapshot reviewed earlier in the same invocation.
Secret patterns are hints only; they neither prove nor rule out a secret.

### `qhapaq_work.py`

The importable library behind the scripts: frontmatter and level-2 section
parsing, exact-byte hashing, material hashing, and requirement fingerprints
that match the [`spec-trace-check`](../skills/spec-trace-check/SKILL.md) block
grammar.

## Runbook facts helper

[`runbook_facts.py`](../skills/work-runbook-sync/scripts/runbook_facts.py)
belongs to the [runbook synchronization skill](../skills/work-runbook-sync/SKILL.md).
Its output modes are mutually exclusive. Use separate invocations with the
same primary and included specifications:

```powershell
python .agents\skills\work-runbook-sync\scripts\runbook_facts.py 0007 --judgments-template --out $env:TEMP\qhapaq-0007-runbook.json
'{"items": {"I-0008-017": {"command": "", "status": "Open - blocked"}}}' |
  python .agents\skills\work-runbook-sync\scripts\runbook_facts.py 0007 --write --judgments -
python .agents\skills\work-runbook-sync\scripts\runbook_facts.py 0007 --check
```

Do not combine `--open`, `--rows`, `--json`, `--check`, `--judgments-template`,
or `--write`. To set a coordinated
scope, pass `--include 0008`; later invocations without `--include` keep the
runbook's declared `included_specs` (an empty `--include ""` clears it).
Transitive prerequisites are included automatically without that option.

`--judgments-template --out FILE` writes the template and prints a compact
summary: suggested commands and gates for every row the facts determine, and
hints for each remaining `<judge>` row. `--write` renders from those
suggestions plus any overrides (`--judgments FILE`, or `-` for standard input;
a UTF-8 byte-order mark is accepted), writes or reports a no-op, checks the
result, and prints `Next command` and `Also eligible`. It rejects unresolved
`<judge>` rows, overrides whose `items` is not an object keyed by item ID (or
a list of entries with `id`) or whose `gates` is not a list, and commands whose
`item=` or spec argument is wrong. With stale
in-scope plans, `--write` alone renders gate mode. `--open`, `--rows`, and
`--json` are for investigation only. Never hand-render a runbook, edit the
template with an ad hoc script, or generate a rendering script. `--check`
returning findings is a validation result, not evidence of a script crash.

## Validation

Run the shared workflow helper regression tests with
`python -m unittest discover -s .agents/scripts/tests`.

After changing a script, rerun it against the current repository and compare
its output with the values already recorded in work records. Material hashes
must reproduce recorded `Material SHA-256` values, and fingerprints must
reproduce current `R-…@xxxxxx` references.
