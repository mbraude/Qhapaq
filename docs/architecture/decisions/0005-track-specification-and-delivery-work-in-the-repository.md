# ADR-0005: Track Specification and Delivery Work in the Repository

> **Status:** Accepted
> **Date:** 2026-10-09
> **Related:** [ADR-0004](0004-classify-changes-and-trace-through-commits.md)

## Context

Specification-first development requires repeated decisions before an
implementation can be planned. Rollout checklists embedded in requirement
blocks mix product rules, unresolved questions, delivery tasks, and progress.
Large features also need smaller implementation slices that can be reviewed
before dependent work begins.

Work must survive chat sessions and remain reviewable with the specifications
and code it concerns. An external issue system must not be necessary to resume
the development process.

## Decision

Store development work under the repository's `work/` directory. Specifications
remain authoritative for product behavior; ADRs and engineering policies govern
architecture and practices. Work plans describe decisions and delivery, never
override those sources, and are not executable pipeline definitions.

The [development workflow](../../development/spec-driven-workflow.md) defines
the artifact contracts and lifecycle:

- Stable, individually stored decision and implementation items reference
  requirements and persistent artifacts.
- A companion plan owns phase membership and preferred order. Item dependencies
  form a directed acyclic graph; order alone never implies dependency.
- Readiness records assess a named scope and exact source snapshot separately
  from item completion, commit success, and contract publication.
- Implementation milestones can be extracted before specification closure.
  Concrete slices specify files, ownership, namespaces, tests, and exit gates
  before execution; do not scaffold speculative production types.
- Changes to specifications trigger reconciliation and reverse-impact review
  of affected work. Preserve identities, completed history, and explicit
  approval gates.
- Repository skills create, reconcile, display, and execute this work one
  bounded item at a time. Human review and approval remain explicit.

Platform and component changes use their existing specification formats.
Architectural decisions can be outputs of decision items. Bugs continue to use
the lightweight ADR-0004 workflow; complex bugs may use implementation slices
without inventing new requirements or a competing change classification.

## Consequences and Tradeoffs

- Plans, requirements, and implementation changes can be reviewed together.
- Markdown with YAML metadata is readable without a project-management tool.
- Generated roadmap views do not create a second source of task status.
- Planning adds overhead; small bugs do not require a plan.
- Skills are AI-led procedures, not deterministic enforcement. Mechanical
  validation and CI integration may be added later; semantic review and human
  approval cannot be inferred from them.
- Material source changes require reassessment rather than merely refreshing
  a revision field.

## Rollout

1. Add the workflow guide, templates, and repository skills.
2. Generate companion plans for existing specifications when requested.
   This decision does not migrate their checklists or change rollout gates.
3. Pilot decision closure before detailing implementation phases.
4. Add deterministic plan validation if concrete consumers require it.

## Alternatives

- **External tracker as authority:** makes development depend on access to a
  separate system and separates plans from the revisions they describe.
- **All tracking inside specifications:** obscures requirements and mixes
  implementation detail with portable behavior.
- **A workflow engine now:** unnecessary infrastructure before the procedures
  and artifact contracts have been exercised.
