---
name: approve-implementation-plan
description: "Review and explicitly approve exact Qhapaq implementation slice plans before execution. Use when authorizing one slice, a phase, or all concrete slices in a specification work plan; does not approve delivery or bypass readiness and dependency gates."
argument-hint: "<spec-id> [phase=<identity>] [item=<implementation-id>]"
---

# Approve an Implementation Plan

## Contract

Approve the execution plan for one or more concrete Qhapaq implementation
slices after reviewing their exact material snapshots. This is a distinct
approval from specification readiness and delivery review:

- Plan approval authorizes execution of the reviewed slice scope and manifest.
- Readiness approval confirms the named specification scope is sufficiently
  complete and current to implement.
- Delivery approval accepts a completed slice after validation.

All applicable gates remain mandatory. Plan approval alone does not make a
slice implementation-eligible. Do not implement, publish, commit, push, change
branches, or mark a slice complete.

## Arguments

- `<spec-id>`: review concrete slices in that specification's work plan.
- `phase=<identity>`: limit review to concrete slices in one named phase.
- `item=<implementation-id>`: review exactly one implementation item.

With no phase or item, inspect the whole named plan and propose approval only
for its fully specified, unstarted slices. Explicitly list milestones and other
items excluded from approval. A milestone is never approved for execution.

## Procedure

### 1. Resolve scope and gates

1. Read `AGENTS.md`, the specification-driven workflow, the owning plan,
   selected implementation items, their requirements, all transitive
   dependencies, applicable readiness records, and governing sources. Skip
   documents already in the current context, and read only the requirement
   blocks and sections the selected slices cite rather than whole large
   specifications.
2. Run `python .agents/scripts/git_preflight.py` once for the branch, full
   change list, and unresolved Git operations; a `no changes since HEAD`
   finding does not block plan approval. Continue on
   the current attached branch when it is the user's intended context. Do not
   switch branches. Stop if unrelated, sensitive, or unreviewable changes make
   the approval scope ambiguous.
3. Verify plan source hashes against exact current bytes with
   `python .agents/scripts/work_hashes.py verify <plan>`. If relevant plan
   inputs are stale or reconciliation is incomplete, stop and request
   `work-plan-sync` before approval.
4. Require a current, approved readiness record that covers every selected
   slice's relevant requirements and capabilities. If it is absent, stale,
   blocked, or does not cover the selected scope, stop and request
   `spec-readiness`, followed by approval of that exact readiness record.
5. Require selected items to be implementation items with
   `granularity: slice`, an unstarted status (`open` or `blocked`), an exact
   file manifest, governing requirements, test and validation expectations,
   and explicit entry and exit criteria. Do not approve milestones, decisions,
   incomplete manifests, cancelled work, or material scope that is already
   being executed. Recommend `implementation-plan` for missing decomposition.
6. Validate item references, dependency targets, requirement identifiers,
   cross-plan graph acyclicity, and normative gates. Missing or cancelled
   dependencies block approval. Incomplete but valid dependencies may remain
   pending; approval does not satisfy them, and the report must identify which
   slices cannot yet execute.

### 2. Review and snapshot the proposed approval

For every selected slice, verify that its scope, exclusions, file actions,
ownership, dependencies, tests, commands, and exit criteria are concrete and
consistent with its authoritative requirements. Do not silently edit the plan
or resolve product decisions. If a material correction is required, stop and
request planning or source reconciliation; the revised snapshot must be
reviewed afresh.

Compute for each item the material SHA-256 defined in the workflow guide, and
full-byte SHA-256 hashes for every material input used to authorize it,
including the owning plan, governing specification and requirements,
applicable approved readiness record, and direct prerequisite items or existing
artifacts relied upon. Use one run of the
[shared workflow scripts](../../scripts/README.md) for both:

```text
python .agents/scripts/work_hashes.py material <item>...
python .agents/scripts/work_hashes.py files <input>...
```

Never hand-write a hashing or material-normalization script.

Present before asking for approval:

- the selected item IDs and titles and the milestones or items excluded;
- the approved readiness scope and any pending dependencies;
- each item's material hash and the paths plus full-byte hashes of its
  material inputs;
- each selected item's intended changes, tests, and exclusions; and
- the files that approval evidence will modify.

Run the workflow's applicable structural checks and `spec-trace-check`. Do not
ask for approval while any required check fails or any substantive plan gate
is unsatisfied.

### 3. Obtain explicit approval

Use `ask_user` to request one explicit choice for the complete displayed set:

- Approve these exact implementation plan snapshot(s).
- Do not approve; stop for changes or further review.

Do not infer approval from invoking this skill, prior approval, readiness,
successful checks, a commit, or a general request to proceed. If the user
declines, make no edits.

### 4. Record plan approval

After explicit approval, rerun the same `material` and `files` commands and
check that the selected items and all material inputs still match the
displayed hashes. If any material input changed, stop without recording
approval and request renewed review.

In each approved slice's existing `Plan approval` section, record that explicit
approval was given in this session without inventing an approver name, the
date, exact scope and exclusions, the item's material SHA-256, and the
full-byte hashes of its material inputs. Preserve the item status; plan approval
does not change an item to `in-progress`, `ready-for-review`, or `complete`.
Do not change material plan content or approval evidence for unselected items.

Recompute the item material hashes and verify every recorded input hash with
`python .agents/scripts/work_hashes.py evidence --section "Plan approval" <item>...`.
Check
the full worktree and report any concurrent change; do not stage, commit, push,
or create a commit message.

## Output and stop

Report approved item IDs and exact snapshots, readiness scope, pending
dependencies and other execution blockers, checks performed, and the next
eligible `implement-next` invocation. Explain that the skill authorizes only
the reviewed plan snapshots.

`implement-next` still executes one slice per invocation and stops at delivery
review. Each outcome needs explicit human delivery approval before the next
dependent slice can proceed. Reapproval is required if material plan content or
governing inputs change.

There is no automatic “spec complete” transition. A specification scope is
finished only after its planned work and aggregate acceptance gates are
verified, every required slice has delivery approval, and remaining normative
requirements are satisfied. Use `work-plan-show` to identify remaining work.
This workflow does not mark a specification complete or publish a component
contract.
