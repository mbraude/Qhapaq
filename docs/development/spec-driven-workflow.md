# Specification-Driven Work

This guide defines repository development artifacts and procedures under
[ADR-0005](../architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md).
It does not define product behavior or replace
[change classification and traceability](coding-conventions.md#3-specification-traceability).

## 1. Authority and entry points

| Change | Authoritative source | Entry point |
| --- | --- | --- |
| Platform capability or behavioral amendment | `SPEC.md` or numbered specification | `spec-create`, then decision work |
| Component within platform contracts | Component specification | `spec-create` with component scope |
| Cross-cutting architectural decision | ADR; also amend specifications if behavior changes | Decision item producing an ADR |
| Clearly governed defect | Existing requirements | `fix-bug` |
| Complex clearly governed defect | Existing requirements | `fix-bug`, optionally organized into implementation slices |
| Planning only | Work artifacts, subordinate to the sources above | `work-plan-edit` |

Classification and planning depth are independent. A complex bug does not become
an amendment because it needs a plan. An ambiguous or unspecified defect does
not become a bug because its fix is small. Follow
[ADR-0004](../architecture/decisions/0004-classify-changes-and-trace-through-commits.md).

Specifications define what must be true. Plans define what to decide or deliver
next. Skills define how to perform that work. YAML metadata and Mermaid graphs
here are development aids, not executable Qhapaq pipeline formats.

## 2. Storage and identity

Use [work/](../../work/README.md), with these directories created only when a
consumer needs them:

```text
work/
  0007/
    plan.md
    runbook.md
    reconciliations/
      index.md
      2026-10-14-source-refresh.md
    decisions/
      D-0007-001-numeric-helpers.md
    implementation/
      I-0007-001-strict-json-reading.md
    readiness/
      mapping-v1.md
  components/
    0001/
      plan.md
      decisions/
      implementation/
      readiness/
```

The paths above are illustrative, not existing plans. `SPEC-0000` owns work for
`SPEC.md`. Component directories use `COMP-NNNN` ownership. Decision IDs use
`D-NNNN-NNN` for platform work and `D-CNNNN-NNN` for components; implementation
IDs use `I` instead of `D`. Allocate the next unused sequence within each owner
and kind, using at least three sequence digits. Never renumber or reuse IDs.

A plan may have one tracked `runbook.md`. It is a generated, snapshot-stamped
view of one primary plan, optionally coordinated with explicitly included plans
and transitive cross-plan prerequisites. Plans, items, readiness records,
approval evidence, and authoritative sources remain the status and eligibility
authority. Never edit runbook rows manually or infer completion from them;
regenerate after authoritative inputs change.

A plan has one `reconciliations/index.md` and zero or more bounded
reconciliation records when source-impact or workflow evidence exists. These
records preserve history and link back to the plan, but are not authoritative
inputs, generated views, or alternate status stores. They never own plan scope,
phase membership, order, status, dependencies, gates, readiness, or approval,
and must not appear in a record's `sources` list. The plan links only to the
index so routine navigation does not load historical evidence.

An item has one owning plan and phase. Other plans can link to it as an external
prerequisite, not copy it. Architectural decisions and complex bugs can belong
to the plan for their primary governing specification. Related specifications
remain explicit references. Templates are under
[work/templates/](../../work/templates/).

## 3. Work-item contract

Each item is a Markdown file with YAML frontmatter and the required body
sections in its [decision](../../work/templates/decision.md) or
[implementation](../../work/templates/implementation.md) template.

| Field | Shape and meaning |
| --- | --- |
| `id` | Stable ID matching kind and owning specification |
| `kind` | `decision` or `implementation` |
| `title` | Nonempty outcome description |
| `status` | `open`, `in-progress`, `ready-for-review`, `complete`, `blocked`, or `cancelled` |
| `spec` | Owning `SPEC-NNNN` or `COMP-NNNN` |
| `requirements` | List of existing, non-retired requirement IDs; no heading references |
| `depends_on` | List of globally unique item IDs, interpreted as AND prerequisites |
| `artifacts` | List of repository-root-relative output paths; existence required at completion |
| `planning_readiness_scope` | Optional exact readiness scope that must be current and approved before an implementation milestone can be decomposed into slices |

An empty requirement list is allowed for an unresolved new capability with no
requirement yet. Explain this in the decision item and add the resulting IDs
when resolved. An executable implementation slice must have governing
requirements. Repository paths in metadata use `/`, independently of shell
path syntax. Quote YAML strings when punctuation requires it.

Decision items state objective, scope/exclusions, unresolved questions,
acceptance criteria, resolution, and validation/review evidence. Accepted
semantics belong in requirements, not only in the resolution section. An
unresolved choice must not be presented as accepted behavior.

Implementation items additionally carry `granularity: milestone` or `slice`
and `change_kind` using ADR-0004's existing kinds. Milestones describe future
outcomes but cannot be executed by `implement-next`. Slices contain:

- Requirement coverage and explicitly incomplete behavior.
- An exact file manifest: action (`add`, `modify`, `delete`), path, purpose,
  project/namespace where applicable, and visibility.
- Contracts, integration points, ownership, and dependency direction.
- Tests, conformance groups, documented commands, and observable exit gates.
- Plan approval evidence, separate from delivery review evidence.

Promote a milestone to a slice in place if its scope remains the same. When
splitting it, keep the milestone as an aggregate gate depending on its child
slices and record their IDs. Retire obsolete manifests explicitly.
Aggregate completion requires evidence and approval, not just completed children.
When a milestone's entry gates require approved implementation readiness before
concrete slices may be planned, set `planning_readiness_scope` to the exact
scope name. The generated runbook must select the matching readiness assessment
or approval action before `/implementation-plan`; missing or non-current
readiness is not an eligible planning command.

## 4. Plan contract and source snapshots

A [plan](../../work/templates/plan.md) has frontmatter:

| Field | Meaning |
| --- | --- |
| `spec` | Owning specification ID |
| `process_version` | The workflow guide's process version this record followed |
| `sources` | List of `{path, revision, content_sha256}` records; work-item, plan, and readiness sources add `material_sha256` |

For each authoritative input actually used, `path` is repository-relative,
`revision` is the full Git commit hash supplying the baseline, and
`content_sha256` is SHA-256 of the exact file bytes last reconciled. For a new
uncommitted input, use `revision: null` and record why in the bounded
reconciliation record.
For an edited input, keep the committed baseline revision and hash the reviewed
working-copy bytes. Never claim uncommitted text is identical to a commit.
Source records exclude the plan itself, reconciliation records, and generated
views: reconciliation history, runbooks, and diagrams are never sources.

When a source is a decision or implementation work item, also record its
`material_sha256`, computed as defined in
[section 5](#5-lifecycle-review-and-completion). When a source is another
plan, record its `material_sha256`: SHA-256 of the plan's UTF-8 text with LF
line endings, omitting its frontmatter `sources` list and `process_version`
line and every level-2 section whose heading contains "reconciliation",
"impact review", or "evidence" (case-insensitive). The canonical plan contains
only the excluded `Reconciliation index`; the broader heading rule preserves
legacy hash compatibility. Keep excluded sections free of scope, phase,
ordering, and gate content. When a source is a readiness record,
record its `material_sha256` the same way, additionally omitting its
`assessment` line and its `## Validation and approval` section; reassessment
findings remain material. Such a source is current when its
material SHA-256 matches, even if its bytes changed: recording lifecycle status
or review evidence on a cited item, reconciling a cited plan's sources
without changing its scope, or recording approval on a cited readiness record
does not make the citing record stale, while any material change does. For
legacy work-item sources without `material_sha256`, the verifier compares the
recoverable recorded bytes (or the recorded revision when those bytes are
unavailable) using this same material definition. Matching material is
current; changed or unverifiable material is stale. It reports when this
legacy material fallback was used so records can be upgraded opportunistically
without forcing reassessment or renewed approval for evidence-only changes.
Other source types without `material_sha256` remain byte-verified.

Process artifacts—this guide, [work/templates/](../../work/templates/), and
the workflow skills and scripts under `.agents/`—govern how records are
produced, not what they assess. Do not cite them as sources merely because a
record followed them. Cite one only when the record's own scope governs or
changes it, for example a plan for a specification that amends this workflow.
Instead, plans and readiness records state `process_version`, the value below.

**Process version:** 1

Increment the process version only when a change to this guide or its
templates invalidates conclusions recorded under earlier versions, and state
why in the change. A record whose `process_version` is missing or lower than
the current value is not current: re-review it under the current process
before relying on it. Other guide, template, and skill edits leave existing
records current.

Include the governing specification, relevant cross-specification sources,
ADRs, and engineering policies used to plan the work. Include artifacts such
as schemas when their contents govern delivery. Compare current source bytes
with recorded hashes before trusting the plan. A different hash requires impact
review; it does not automatically invalidate all unrelated scopes.

Phase sections own ordered item links, entry gates, and exit gates. Do not
duplicate item status or dependencies in phase tables. Link normative gates by
requirement ID. Track artifact-producing prerequisites as items, and record
existing artifact prerequisites in slice entry criteria.

Order selects among eligible items but does not add dependency edges. Dependency
graphs must be acyclic across plans; a cancelled prerequisite does not satisfy
a dependent's gate. Rewire or cancel affected work explicitly.

Each reconciliation operation adds one bounded record beneath
`reconciliations/` and one link to its index. Use a `YYYY-MM-DD-<scope>.md`
name, adding a stable numeric suffix when needed. A record states the baseline,
source changes, affected items, readiness impact, unresolved blockers, whether
reconciliation is complete, and links to both the index and plan. Keep one
event per record; do not append an accumulating journal to the plan or one
unbounded evidence file.

The plan retains a level-two `Reconciliation index` section linking only to
`reconciliations/index.md`. That section remains excluded from the plan's
material hash. Reconciliation records and their index are non-material history:
changing them does not change plan eligibility, and they are read only when an
operation needs the corresponding source-impact or historical evidence. Do not
update a source hash merely to silence staleness. If reconciliation is
incomplete, retain the old snapshot and state what remains; a partially
reconciled plan is not current.

Hash mismatches are change detectors, not approval revocations. First compare
the delta with the selected scope, governing requirements, manifest, and
assessment findings. If those are unaffected, record the impact review and
refresh only the source metadata; preserve the assessment, authorization, and
original approval evidence. This maintenance requires validation, not another
human approval. A material change to the work being authorized requires a new
authorization for that changed scope, not retroactive invalidation of the
previous approval. If impact cannot be established, report the precise unknown
instead of claiming that the earlier approval failed.

Plan-approval evidence binds the material hash of an applicable readiness
record, not its full file bytes. The plan approval must separately verify that
the readiness record is currently approved, its own approval evidence matches
its material content, and its recorded sources are current. This keeps
assessment, lifecycle, and approval-evidence changes from invalidating an
unchanged plan authorization while a change to readiness findings, scope, or
other material content requires authorization of the changed scope.
Use material hashes for work-item and plan inputs as well; reserve full-byte
hashes for specifications and artifacts, with manifest inputs labeled as
baselines. Do not make an unrelated edit elsewhere in a whole specification
or plan a reason to reapprove an unchanged slice; perform scoped impact review.

## 5. Lifecycle, review, and completion

```text
open -> in-progress -> ready-for-review -> complete
             |
             +-> blocked -> in-progress
open / in-progress / blocked / ready-for-review -> cancelled
```

### Branches and Git delivery

Work-item status, approval, and Git delivery are separate lifecycles. A branch,
commit, push, pull request, or merge does not approve or complete an item, and
item completion does not imply merge to the default branch. Exact material
snapshots and source revisions remain the review authority.

Work may proceed on the current attached branch, including the default branch,
when that is the user's intended delivery context. A named work branch remains
recommended when an effort is expected to span multiple commits, move files,
disrupt shared repository surfaces, or benefit from pull-request review.
Prefer one branch for a coordinated specification or delivery scope when that
is useful, with independently reviewed commits for its bounded work items.
Use `work-branch-start` only when branch setup is requested or selected.
Mutating skills inspect and report branch context but do not require, create,
or switch branches silently.

Branch names and topology are operational and must not become work-item status
or plan-frontmatter authority. A work item may move between branches without
changing its ID, dependencies, or lifecycle. Record temporary coordination in
the pull request or a bounded reconciliation record only when it materially
helps review.

Do not carry unrelated working-tree changes onto a new branch. Coherent
uncommitted changes for the selected scope may move with an explicitly
confirmed branch creation; never stash, commit, reset, or discard them
implicitly. Integrating the default branch into a work branch requires source
and snapshot impact review. Materially changed files require renewed approval;
unaffected approvals remain valid.

Move `ready-for-review` back to `in-progress` when review requires edits.
Complete means acceptance criteria, persistent outputs, required validation,
and explicit human approval all exist. A skill may record completion only when
the user approves the exact reviewed snapshot; it must not infer approval from
"continue", a commit, successful tests, or earlier approval of a plan.

Record review evidence in the item's body: approver as explicitly supplied
(or a reference to their approval), date, exact scope, and snapshot. A snapshot
can be a full committed revision or a table of repository paths and SHA-256
hashes of the reviewed working-copy artifacts. Include material inputs and
outputs, excluding the evidence record itself to avoid self-referential hashes.
The `[ ]`/`[x]` state of acceptance-criterion checkboxes is progress metadata,
not criterion content; changing checkbox state alone does not change a plan's
approved material scope. Changes to criterion wording, scope, dependencies, or
the manifest still require renewed plan approval. Delivery approval records
the final output snapshot and verifies every criterion before completion.
Metadata-only recording of approval does not change the approved scope. Do not
invent approver identities or claim evidence that is not available.

### Historical approval versus current eligibility

An explicit approval is a permanent fact about the named scope and snapshot.
Later edits do not undo it. A completed prerequisite is satisfied by its
`status: complete`, explicit delivery approval, recorded acceptance/validation
evidence, and persistent outputs. Do not replay its old readiness, plan-input
currentness, or execution-entry gates when reviewing a dependent or aggregate.
Unchecked progress boxes in an otherwise evidenced completed record are a
bookkeeping defect, not missing human approval; report the discrepancy without
reopening the item or asking the user to approve it again.

Currentness checks answer whether an approval's scope can authorize **new**
work against today's inputs. Historical evidence tables describe what was
reviewed then; comparing every historical row with today's files cannot answer
whether that approval occurred. For aggregates, check coverage and the current
aggregate outputs against the child outcomes, not whether every child input
still has its old bytes. A substantive discrepancy creates explicit follow-up
work; it does not silently revoke completed delivery.

When approval covers an uncommitted item's own material plan or resolution,
record a **material SHA-256** alongside the full-byte hashes of its other inputs
and outputs. Compute it from the item's UTF-8 text, normalizing line endings to
LF and omitting only the frontmatter `status` line and these level-two sections:
`Validation and review`, `Plan approval`, and `Delivery evidence and review`.
Omit each named heading and its body through the next level-two heading or EOF.
Normalize Markdown task-list checkbox state to `[ ]` before hashing; criterion
wording remains covered. Everything else, including scope, dependencies,
manifest, criteria, and resolution, remains covered. Label this hash as
material, not a file-byte hash. Existing checkbox-sensitive hashes remain valid:
compare their recoverable material snapshot using the same progress
normalization, or accept a matching legacy material digest. Do not rewrite
historical evidence or require reapproval to adopt the normalized digest.
Recompute it before relying on the approval. This permits evidence and lifecycle
updates without requiring a separate review file or a self-referential hash.

**Approved plan snapshots are immutable.** Once a human approves an item's
material plan, no skill or agent edits its scope, criterion wording,
dependencies, manifest, exclusions, or `change_kind` unless the user explicitly
requests a change after being told it requires renewed plan approval. Checking
or unchecking acceptance criteria records progress and does not alter the
approved plan. Never revoke a recorded approval silently, or block an unchanged
plan because execution has reached its approved outputs.

Plan approval authorizes the reviewed scope and manifest; it does not approve
the output bytes. Before execution, readiness and plan-approval evidence must
be current, including the then-current bytes of files that are planned outputs.
After execution, changes to paths in that exact approved manifest are expected
outputs, not stale prerequisites for delivery review. Preserve their baseline
hashes in plan-approval evidence, then inspect and snapshot the final bytes in
delivery evidence. Changes to inputs outside the manifest remain stale and
block delivery until reconciled. A changed authoritative source that alters
required meaning or exceeds the approved scope requires a separate decision,
readiness assessment, and plan approval; final-output review must not silently
expand the approved change.

An item's `change_kind` is the planned classification. The commit's
`Change-Kind:` trailer comes from `spec-trace-check` on the actual diff. If
they differ, use the verified trailer, record the difference in delivery
evidence, and show it to the reviewer at delivery approval. Do not edit the
approved item to match. Changing material content of a `complete` item,
including its `change_kind`, is an amendment to completed work: create a
follow-up item, or reopen the item only with explicit user approval.

Commits and publication remain separate. Work-item completion is not component
contract publication; apply ADR-0004's per-version publication procedure.
Use existing commit skills only when requested and their whole-worktree scope
matches the user's intent. Do not stage unrelated work to finalize an item.

## 6. Readiness and execution eligibility

A [readiness record](../../work/templates/readiness.md) identifies the owning
specification, named scope, source snapshots, assessment, blockers, exclusions,
validation, and approval. `assessment` is `not-assessed`, `blocked`,
`ready-for-review`, or `approved`. `authorizes` states what an approved
assessment permits: `implementation` (execution of the assessed scope, after
plan approval) or `planning` (concrete implementation planning only). It is
material content, so changing it requires reassessment. New and reassessed
records state it; for an older record without it, read the record's own text.
Scope lists requirement IDs and included
capabilities; it is not an assertion about an entire release.

Readiness evaluates completeness, consistency, testability, security,
compatibility, and conformance expectations beyond the known decision backlog.
Where normative gates require actual schemas or vectors before implementation,
readiness and slice eligibility must require those artifacts, not promises.
Readiness neither publishes a contract nor relaxes a rollout gate.

An approved readiness record applies to the assessed source snapshot for
implementation eligibility. Before execution, changed sources require scoped
impact review. An unchanged assessment can remain approved with a recorded
no-impact review and refreshed source metadata; only affected findings or scope
require a new assessment and authorization. After a slice has executed,
changes to its explicitly approved manifest outputs do not retroactively
invalidate the readiness or plan authorization for that slice's delivery
review: the reviewer checks those final outputs against the approved scope,
requirements, and acceptance criteria. Such changed sources are not current
inputs for another implementation slice; reassess downstream work against the
new source snapshot only when scoped impact review identifies affected
findings. Any out-of-manifest source change requires impact review; an output
change that alters required behavior or the approved scope requires changed
authorization before delivery.
A work-item, plan, or readiness source whose recorded `material_sha256` still matches has
not changed for this purpose, and process artifacts are not readiness sources
unless the assessed scope governs them (see
[section 4](#4-plan-contract-and-source-snapshots)). A readiness record states
`process_version` like a plan.
Preserve earlier evidence in Git; do not silently carry approval onto new
material scope or findings.

Derived conclusions, not manually stored statuses:

- **Dependency-ready:** every prerequisite item is complete.
- **Decision-eligible:** dependency-ready, current relevant plan inputs, and no
  unresolved entry blocker; not already complete or cancelled.
- **Implementation-eligible:** a slice is dependency-ready, its material plan
  is approved, relevant specification readiness is approved/current, and all
  required source artifacts and entry gates are satisfied.

A readiness requirement for a narrowly governed bug can be satisfied by the
documented governing-requirement review rather than whole-specification closure.
Use `fix-bug`; do not invent additional bug ceremonies or waive normative gates.

## 7. Creation, editing, and synchronization

### New specification

`spec-create` classifies the request, uses existing platform/component conventions,
drafts agreed requirements, and creates initial decision work using the templates.
It asks for unresolved consequential choices rather than silently accepting them.
It does not create production placeholders or publish incomplete contracts.

### Existing specification

`work-plan-sync` bootstraps a missing plan or reconciles an existing one. Extract
open questions and rollout milestones without losing their scope or gates.
Deduplicate overlapping questions. Keep completed specification decisions
distinct from outstanding implementation artifacts. Do not infer historical
human approval from a checked box; record source evidence and flag unverified
completion for review. Do not execute items as part of synchronization.

Moving existing normative checklist text needs explicit migration scope.
Preserve requirement IDs, tombstones where applicable, and reverse-impact
review. Bootstrapping alone leaves existing specifications unchanged; migrated
work artifacts become the operational status authority, while original
normative obligations remain in force. Report any temporary duplicate checklist
status rather than maintaining two competing trackers.

### Planning-only edits

`work-plan-edit` changes scope, phase membership, order, or dependencies without
changing product requirements. Split or cancel work with explicit reasons and
replacement links. Review downstream coverage and approval impact. If a proposed
edit requires new behavior or architecture, stop and identify its authoritative
decision rather than hiding it in the plan.

### Requirement or implementation changes

Edit the authoritative source first, then synchronize affected plans in the same
coherent change where practical. Review referencing code and tests under existing
traceability rules. An in-progress slice pauses for material replanning; preserve
user work and account for already implemented code.

Reopen a completed item only when its original completion claim was wrong.
Legitimate completion followed by new requirements creates follow-up work.
Cancel obsolete open work rather than deleting its identity.

## 8. Skills and stopping points

These are AI-led repository procedures, not an automated scheduler or a
deterministic validator. Arguments in the examples are requests interpreted by
the skill, not a standalone command-line parser.

```text
/work-branch-start SPEC-0007
/spec-create <idea or target> [kind=platform|component|amendment]
/work-plan-sync SPEC-0007
/work-plan-show SPEC-0007 [phase=0] [remaining]
/work-runbook-sync SPEC-0007 [include=SPEC-0008,...]
/work-next SPEC-0007
/work-plan-edit SPEC-0007 <requested planning change>
/spec-next SPEC-0007 [phase=0] [item=D-0007-001]
/spec-readiness SPEC-0007 scope=mapping-v1
/implementation-plan SPEC-0007 phase=1A
/implement-next SPEC-0007 [item=I-0007-001]
/approve D-0007-001
```

`spec-next` and `implement-next` stop after one bounded item. On a subsequent
invocation, surface pending approval for the preceding item before choosing
dependent work. Record explicit approval if supplied; otherwise ask whether to
review it or proceed with an independent eligible item. Never pick a blocked
alternative silently. No decisions remaining means assess readiness, not assume
the specification is complete.

`approve` reviews and records approval of one exact ready-for-review snapshot,
then outputs a complete commit message for use with Git tooling or the VS Code
Source Control UI. It does not stage, commit, push, or open a pull request.
`approve-commit` and `approve-commit-push` compose that same approval workflow
with optional Git delivery.

`work-plan-show` is read-only. Display counts by kind/status, phases, ready items,
review gates, blockers, implementation milestones, and next eligible actions.
Render prerequisite-to-dependent edges in Mermaid when useful; a tree-like
outline labels repeated prerequisites. Validate the graph before presenting it.
Report stale inputs, missing references, and cycles explicitly, and withhold
trusted eligibility for affected items. Do not save a generated view unless
requested; exports identify their source snapshot and are not status authorities.

`work-runbook-sync` materializes the same dependency and eligibility reasoning
as a tracked table under the primary plan directory. Its rows contain linked
work items or synthetic workflow gates, descriptions, copyable skill commands,
derived status, evidence-backed completion dates, and blockers. It includes
transitive cross-plan prerequisites and records an exact source-set digest.
Regeneration replaces derived rows and is a no-op when the meaningful rendered
content is unchanged. The runbook is reviewable navigation, not another editable
status source.

`work-next` refreshes that runbook before selection, invokes the first safe row
through its existing owning skill, refreshes the runbook afterward, and stops.
It may then offer applicable validation, approval, commit, and push workflows,
but it delegates to their existing skills and preserves every explicit review
and delivery gate. One invocation advances at most one row; it never skips a
blocked selected row for an unrelated action.

When approval is followed by a commit, refresh the selected runbook after
recording approval and before staging, so that one delivery includes its
derived bookkeeping. Review the regenerated runbook with its helper; do not
request a second material approval solely for this derived view.

## 9. Validation and evaluation

Before reporting a mutating workflow successful:

1. Check frontmatter, IDs, kind/owner agreement, and required body sections.
2. Resolve item, requirement, source, and artifact references. Planned outputs
   may be absent; completed outputs and execution prerequisites may not.
3. Check unique ownership, dependencies, cross-plan cycles, and phase membership.
4. Check requirement coverage, retained scope after splits, cancelled dependencies,
   exact manifests, and normative entry/exit gates.
5. Check source snapshots, readiness impact, and approval evidence.
6. Check that the plan has exactly one reconciliation-index link, every indexed
   record exists and links back, no record is unindexed, and no reconciliation
   record appears as an authoritative source.
7. Run `spec-trace-check`; implementation also runs the applicable documented
   checks and `build-and-test`. Never invent unavailable commands or claim
   unperformed validation.

Until a deterministic work-artifact validator exists, these structural and
semantic checks are AI-led and must be reported as such.

Evaluate the procedures with these cases:

| Scenario | Expected result |
| --- | --- |
| No plan exists | Sync creates decision work and implementation milestones, not production code |
| Same sources and plan synced again | No duplicate items or ID churn |
| New requirement after completion | Follow-up work and scoped readiness reassessment |
| Item split | Original identity retained, coverage and dependencies preserved |
| Cancelled prerequisite or dependency cycle | Explicit blocker; no execution |
| Working-copy source differs from baseline | Exact hash and impact review, not false committed provenance |
| Draft or unapproved milestone | Implementation refuses execution |
| Review requested changes | Item returns to in-progress; approval is not carried forward |
| Clearly governed bug | Existing regression-test workflow remains available |
| Viewer invoked | No repository edits, commits, or reconciliation |
