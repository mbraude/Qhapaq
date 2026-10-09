---
name: implement-next
description: "Implement one approved, dependency-ready Qhapaq delivery slice from a work plan. Use to resume incremental implementation after scoped readiness and concrete file/test planning; validates the outcome and stops for human delivery review."
argument-hint: "<spec-id> [phase=<identity>] [item=<implementation-id>]"
---

# Implement the Next Slice

## Contract

Read [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), target plan,
slice, approved readiness, and applicable path-specific instructions.
Execute one slice only. Do not publish, commit, push, grant approval, or scaffold
future slices.

## Procedure

1. Inspect worktree changes and source snapshots. Resolve prerequisite items
   across plans. Report absent/stale plans, missing artifacts, cycles, or
   cancelled dependencies before execution.
2. Surface any preceding delivery review gate. Record completion only if the
   user explicitly approves its exact unchanged material snapshot and its exit
   criteria pass. Otherwise ask whether to review it or work independently.
3. Select the named slice or the first implementation-eligible slice in
   requested phase/plan order. Require granularity=slice, approved material plan,
   current approved relevant readiness, completed dependencies, and all normative
   entry gates. Report a named blocked item without substituting another.
   If no slice is eligible, show blockers and suggest planning/review as needed.
4. Read governing requirement blocks, architecture boundaries, nearby code and
   existing helpers. Set in-progress. Implement the approved manifest, preserving
   unrelated user changes and intended behavior outside scope.
5. For `change_kind: bug`, use [fix-bug](../fix-bug/SKILL.md): reproduce, add a
   failing referencing regression test, apply the fix, and validate. Do not
   reinterpret ambiguous behavior as a bug or skip required regression evidence.
6. Add/update the tests and artifacts proving the exact exit criteria.
   Record incidental file discoveries in the manifest. Material scope, ownership,
   public-contract, or dependency changes pause execution for
   [implementation-plan](../implementation-plan/SKILL.md) and reapproval; new
   behavior requires an authoritative specification decision.
7. Run the smallest documented checks proving the slice, plus
   [build-and-test](../build-and-test/SKILL.md), which includes traceability,
   with the actual change kind. Include schema/conformance/consumer checks
   specified by the slice. For artifact-only slices without .NET changes, use
   `spec-trace-check` and the applicable documented artifact checks instead.
   Do not skip mandatory gates or invent unavailable tooling.
8. On failure, fix within approved scope or record a blocker; do not claim
   delivery. On success, record actual files, checks/results, deviations, and
   exact reviewed input/output snapshots; set ready-for-review.
9. Complete only after explicit human delivery approval of that material
   snapshot. Plan approval, readiness approval, or successful tests alone are
   insufficient. Reconcile authoritative-source changes if any before ending.

## Output and stop

Report slice ID, implemented requirement coverage, exclusions, artifact links,
validation results, blockers, proposed trailers, and delivery review gate.
Stop after this one slice; do not advance dependent work or auto-complete its
aggregate milestone.

Evaluation: an unapproved slice or milestone is refused; exact exit criteria
drive testing; material deviations trigger replanning; validation failure
prevents ready-for-review; approval never implies contract publication.
