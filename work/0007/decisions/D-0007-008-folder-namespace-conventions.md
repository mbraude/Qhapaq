---
id: D-0007-008
kind: decision
title: Feature folders and canonical namespace conventions
status: open
spec: SPEC-0007
requirements: [R-0007-346, R-0006-021, R-0006-025]
depends_on: []
artifacts: [docs/development/coding-conventions.md]
---

# D-0007-008: Folder and Namespace Conventions

## Objective

Close the first Phase 0A organization checkpoint before public APIs expand.

## Scope and exclusions

Feature folders, folder-to-namespace mapping, and canonical naming inside
established assemblies. Do not rename layers or create placeholder production types.

## Questions to resolve

How are features nested within each owning assembly? Which folder/namespace
exceptions, if any, are justified and enforceable?

## Acceptance criteria

- [ ] Persistent conventions cover representative features and namespace mapping.
- [ ] Existing assembly, visibility, and dependency rules remain intact.
- [ ] Architecture-test expectations are identified for I-0007-001.
- [ ] Checks and explicit review cover the exact policy.

## Resolution

Unresolved. Architectural boundary changes require SPEC-0006 or an ADR, not
only an ordinary naming convention.

## Validation and review

No namespace policy or completion approval added during bootstrap.
