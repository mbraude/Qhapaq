---
id: D-0007-014
kind: decision
title: DI lifetimes and immutable state ownership
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0006-013, R-0006-016, R-0006-019]
depends_on: [D-0007-009]
artifacts: [docs/development/coding-conventions.md]
---

# D-0007-014: DI Lifetimes

## Objective

Document lifetime and ownership rules needed by the first implementation slices.

## Scope and exclusions

Registry snapshots, cached plans, per-run state, and credential-related
collaborators. Preserve constructor injection, private run state, and established
composition boundaries; do not add ambient execution context.

## Questions to resolve

Which lifetimes, disposal ownership, snapshot capture, and invalidation boundaries
apply to each collaborator? What tests detect unsafe cross-run state sharing?

## Acceptance criteria

- [ ] Persistent lifetime/ownership rules cover every listed state family.
- [ ] Run isolation and immutable snapshot rules remain compatible with requirements.
- [ ] DI resolution/scope and architecture-test expectations are explicit.
- [ ] Checks pass; material policy/architecture decisions receive human approval.

## Resolution

Unresolved. Architectural changes belong in SPEC-0006 or an ADR as applicable.

## Validation and review

No DI lifetime or credential implementation approved by extraction.
