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

## 4. Plan contract and source snapshots

A [plan](../../work/templates/plan.md) has frontmatter:

| Field | Meaning |
| --- | --- |
| `spec` | Owning specification ID |
| `sources` | List of `{path, revision, content_sha256}` records |

For each authoritative input actually used, `path` is repository-relative,
`revision` is the full Git commit hash supplying the baseline, and
`content_sha256` is SHA-256 of the exact file bytes last reconciled. For a new
uncommitted input, use `revision: null` and record why in reconciliation evidence.
For an edited input, keep the committed baseline revision and hash the reviewed
working-copy bytes. Never claim uncommitted text is identical to a commit.
Source records exclude the plan itself and generated views.

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

Reconciliation evidence records the baseline, source changes, affected items,
readiness impact, and unresolved blockers. Do not update a source hash merely
to silence staleness. If reconciliation is incomplete, retain the old snapshot
and state what remains; a partially reconciled plan is not current.

## 5. Lifecycle, review, and completion

```text
open -> in-progress -> ready-for-review -> complete
             |
             +-> blocked -> in-progress
open / in-progress / blocked / ready-for-review -> cancelled
```

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
Material changes to acceptance criteria, scope, dependencies, or artifacts after
approval require renewed approval. Metadata-only recording of approval does not.
Do not invent approver identities or claim evidence that is not available.

When approval covers an uncommitted item's own material plan or resolution,
record a **material SHA-256** alongside the full-byte hashes of its other inputs
and outputs. Compute it from the item's UTF-8 text, normalizing line endings to
LF and omitting only the frontmatter `status` line and these level-two sections:
`Validation and review`, `Plan approval`, and `Delivery evidence and review`.
Omit each named heading and its body through the next level-two heading or EOF.
Everything else, including scope, dependencies, manifest, criteria, and
resolution, remains covered. Label this hash as material, not a file-byte hash.
Recompute it before relying on the approval. This permits evidence and lifecycle
updates without requiring a separate review file or a self-referential hash.

Commits and publication remain separate. Work-item completion is not component
contract publication; apply ADR-0004's per-version publication procedure.
Use existing commit skills only when requested and their whole-worktree scope
matches the user's intent. Do not stage unrelated work to finalize an item.

## 6. Readiness and execution eligibility

A [readiness record](../../work/templates/readiness.md) identifies the owning
specification, named scope, source snapshots, assessment, blockers, exclusions,
validation, and approval. `assessment` is `not-assessed`, `blocked`,
`ready-for-review`, or `approved`. Scope lists requirement IDs and included
capabilities; it is not an assertion about an entire release.

Readiness evaluates completeness, consistency, testability, security,
compatibility, and conformance expectations beyond the known decision backlog.
Where normative gates require actual schemas or vectors before implementation,
readiness and slice eligibility must require those artifacts, not promises.
Readiness neither publishes a contract nor relaxes a rollout gate.

An approved readiness record applies only to its assessed source snapshot.
Changed sources require impact review and a new assessment for affected scope.
Preserve earlier evidence in Git; do not silently carry approval onto new text.

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
/spec-create <idea or target> [kind=platform|component|amendment]
/work-plan-sync SPEC-0007
/work-plan-show SPEC-0007 [phase=0] [remaining]
/work-plan-edit SPEC-0007 <requested planning change>
/spec-next SPEC-0007 [phase=0] [item=D-0007-001]
/spec-readiness SPEC-0007 scope=mapping-v1
/implementation-plan SPEC-0007 phase=1A
/implement-next SPEC-0007 [item=I-0007-001]
```

`spec-next` and `implement-next` stop after one bounded item. On a subsequent
invocation, surface pending approval for the preceding item before choosing
dependent work. Record explicit approval if supplied; otherwise ask whether to
review it or proceed with an independent eligible item. Never pick a blocked
alternative silently. No decisions remaining means assess readiness, not assume
the specification is complete.

`work-plan-show` is read-only. Display counts by kind/status, phases, ready items,
review gates, blockers, implementation milestones, and next eligible actions.
Render prerequisite-to-dependent edges in Mermaid when useful; a tree-like
outline labels repeated prerequisites. Validate the graph before presenting it.
Report stale inputs, missing references, and cycles explicitly, and withhold
trusted eligibility for affected items. Do not save a generated view unless
requested; exports identify their source snapshot and are not status authorities.

## 9. Validation and evaluation

Before reporting a mutating workflow successful:

1. Check frontmatter, IDs, kind/owner agreement, and required body sections.
2. Resolve item, requirement, source, and artifact references. Planned outputs
   may be absent; completed outputs and execution prerequisites may not.
3. Check unique ownership, dependencies, cross-plan cycles, and phase membership.
4. Check requirement coverage, retained scope after splits, cancelled dependencies,
   exact manifests, and normative entry/exit gates.
5. Check source snapshots, readiness impact, and approval evidence.
6. Run `spec-trace-check`; implementation also runs the applicable documented
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
