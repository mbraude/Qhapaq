---
name: spec-create
description: "Draft or amend a Qhapaq platform or component specification and create its initial decision work plan. Use when creating a spec, specifying a new feature or component, or proposing a behavioral amendment; not for clearly governed bug fixes."
argument-hint: "<idea or spec-id> [kind=platform|component|amendment]"
---

# Create a Specification

## Contract

Read [AGENTS.md](../../../AGENTS.md), the
[workflow guide](../../../docs/development/spec-driven-workflow.md), and applicable
[specification instructions](../../../.github/instructions/specifications.instructions.md).
Use the existing [platform](../../../specs/README.md) and
[component](../../../specs/components/README.md) conventions.

Arguments describe an idea or existing target, with an optional suggested kind.
Classify the actual requested behavior under ADR-0004; do not blindly accept a
kind that contradicts it. Ask for missing scope or consequential decisions.
Do not commit, publish, implement production code, or mark work approved.

## Procedure

1. Inspect the worktree and read related specifications and architectural
   decisions. Preserve unrelated changes. A clearly governed defect belongs to
   [fix-bug](../fix-bug/SKILL.md), not a new specification.
2. Identify platform capability, component extension, or behavioral amendment.
   A component requiring a new platform contract records that prerequisite
   first. Architectural decisions belong in ADRs, not only in a work plan.
3. For a new document, allocate the next unused specification number and
   requirement IDs. For an amendment, preserve IDs and published-version
   immutability. Never renumber existing requirements.
4. Draft purpose, goals/non-goals, agreed contracts and semantics, security,
   privacy, compatibility, failures, limits, tests/conformance, rollout,
   alternatives, and open questions as applicable. Separate unresolved choices
   from accepted requirements. Keep implementation file manifests out of portable
   specifications. Ask for decisions rather than inventing approval.
5. Update the relevant specification index and directly affected references.
   Review changed requirement references and fingerprints under existing policy.
6. Invoke [work-plan-sync](../work-plan-sync/SKILL.md) for the new or amended
   scope. It creates or reconciles decision items and future milestones without
   executing them. Do not extract unrelated existing backlogs.
7. Apply the workflow guide's validation checklist and invoke
   [spec-trace-check](../spec-trace-check/SKILL.md). Fix failures before reporting
   a successful draft; record checks actually performed.

## Output and stop

Report classification, changed specification/plan links, accepted requirements,
unresolved decisions, proposed trailers, validation, and the next review gate.
Stop for review. A draft, successful commit, or new work plan is not readiness
or publication.

Evaluation: new platform and component drafts get distinct identities; a
published component amendment requires a new version; unresolved choices remain
open; a clearly governed bug is routed without generating a replacement spec.
