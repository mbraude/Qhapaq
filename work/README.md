# Development Work

This directory stores repository-owned specification decisions, delivery plans,
and readiness evidence under
[ADR-0005](../docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md).
It is not part of the portable product specification or a runtime input.

The [workflow guide](../docs/development/spec-driven-workflow.md) defines the
contracts, authority, lifecycle, approval gates, and validation procedures.
Specifications and ADRs remain authoritative; these artifacts never grant
permission to override them.

## Starting and resuming

- Use `spec-create` for a new specification and initial decision work.
- Use `work-plan-sync <spec-id>` to create a missing companion plan or reconcile
  it after source changes.
- Use `work-plan-show <spec-id>` to inspect remaining work and dependencies.
- Use `spec-next <spec-id>` for one decision, then review and explicitly approve.
- Assess a named scope with `spec-readiness` before detailed delivery.
- Use `implementation-plan` to approve concrete slices and `implement-next` to
  deliver one at a time.
- Use `work-plan-edit` for planning-only changes.

No existing specification backlog has been extracted as part of scaffolding.
Owner directories are created on demand. Git records their change history.

## Templates

Copy and populate these templates; placeholders are not accepted evidence:

- [Plan](templates/plan.md)
- [Decision item](templates/decision.md)
- [Implementation milestone or slice](templates/implementation.md)
- [Readiness record](templates/readiness.md)

Do not treat templates as live work items. Do not maintain generated roadmap
views as another editable status source.
