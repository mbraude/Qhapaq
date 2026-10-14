---
name: spec-readiness
description: "Assess completeness and implementation readiness of a named Qhapaq specification scope and exact revision. Use after decision closure or before implementation planning; checks unknown gaps, consistency, conformance expectations, prerequisites, and explicit approval."
argument-hint: "<spec-id> scope=<name>"
---

# Assess Specification Readiness

## Contract

Read [AGENTS.md](../../../AGENTS.md) unless it is already in context. The
rules below are the parts of the
[workflow guide](../../../docs/development/spec-driven-workflow.md) this skill
needs; do not read the guide unless a case here is unclear. Read the
[readiness template](../../../work/templates/readiness.md) only when creating
a new record; when reassessing, edit the existing record.
Resolve a named scope with explicit requirements/capabilities and exclusions.
Ask if the scope is ambiguous. Do not publish, commit, implement, or silently
resolve new product decisions.

Readiness record rules:

- Frontmatter: `spec`, `scope`, `assessment` (`not-assessed`, `blocked`,
  `ready-for-review`, or `approved`), `authorizes` (`implementation` to permit
  execution after plan approval, or `planning` for concrete implementation
  planning only), `process_version` (the guide's current value, which
  `work_hashes.py verify` reports as `actual` for the `process_version` row),
  and `sources`.
- Sources are the authoritative inputs actually assessed: specifications,
  ADRs, engineering policies, governing schemas, and the plan, work items, and
  readiness records consulted. Never cite the record itself, runbooks or
  diagrams, or process artifacts (the guide, templates, and `.agents/` skills
  and scripts) unless the assessed scope governs them.
- Body sections follow the template: Assessed scope, Exclusions,
  Completeness and consistency, Conformance and prerequisite artifacts,
  Blockers, and Validation and approval. The material hash omits `sources`,
  `process_version`, `assessment`, `Validation and approval`, and any section
  whose heading contains "reconciliation", "impact review", or "evidence", so
  put findings in the other sections.
- An approval applies only to its assessed snapshot; never carry it onto
  changed material text. Describe an earlier or another record's limits as
  such ("the earlier `<scope>` readiness authorized planning only") so they
  are not read as this record's own.

## Procedure

1. Inspect branch context and worktree, then read the governing specification,
   related requirements/ADRs, plan/items, existing readiness evidence, and
   required artifacts. Continue on the current attached branch when it is the
   user's intended delivery context, including the default branch. Recommend
   [work-branch-start](../work-branch-start/SKILL.md) for multi-commit or
   disruptive work, but do not require or silently create a branch. Check plan
   source currentness with `python .agents/scripts/work_hashes.py verify`. If
   relevant plan sources are stale, report the need for `work-plan-sync`
   before approval.
2. Check known decisions and normative entry/exit gates. Open blocking decisions,
   unverified approval, or missing required artifacts remain explicit blockers.
3. Independently inspect completeness: closed shapes and contracts, typing,
   failures, null/missing behavior, deterministic order, limits/accounting,
   policy/security/privacy, compatibility, and cross-specification consistency
   as applicable. An empty decision backlog is not proof of completeness.
4. Map scope requirements to required conformance expectations and actual
   prerequisite artifacts. Distinguish specified cases from published vectors.
   Do not require unrelated release artifacts or relax specified gates.
5. Populate or revise the scope's readiness record: findings, exclusions,
   validation, blockers, and `authorizes`. Write its `sources` with the
   script, never by hand: `python .agents/scripts/work_hashes.py refresh
   <record> --stale --add <new source>... [--remove <dropped source>...]`
   refreshes non-current entries, appends new ones with revision, content
   hash, and `material_sha256` for work-item, plan, and readiness sources, and
   deletes dropped ones in one call (for a new record, replace the template's
   placeholder entries with `sources: []` first). Run it after the last material edit,
   then one `work_hashes.py verify <record>` must report every source current.
   Verify requirement fingerprints with one
   `python .agents/scripts/spec_fingerprints.py --id <ID>...` call listing
   every requirement. Preserve prior approval
   history in Git; material changes need reassessment. Report newly discovered
   decision work for reconciliation rather than closing it implicitly.
6. Apply the workflow validation checklist and invoke
   [spec-trace-check](../spec-trace-check/SKILL.md). Record only performed checks.
7. Set blocked when findings prevent readiness; otherwise ready-for-review.
   Set approved only when the user explicitly approves the exact assessed
   snapshot after the required checks. Earlier approval of another scope or
   a successful commit is insufficient.

## Output and stop

Report scope, requirement coverage, source snapshots, blockers, missing
conformance/prerequisites, validation, and review gate. State explicitly that
readiness is scoped and is neither publication nor a full v1 conformance claim.
Stop without executing an implementation item.

Evaluation: no open items can still yield blocked readiness; a changed source
does not inherit approval; independent scope exclusions remain explicit; a
required schema/vector cannot be replaced by a promise to generate it later.
