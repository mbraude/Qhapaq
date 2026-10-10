---
id: D-0008-001
kind: decision
title: Adopt artifact taxonomy and source layout
status: open
spec: SPEC-0008
requirements: [R-0000-009]
depends_on: []
artifacts:
  - SPEC.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-001: Adopt Artifact Taxonomy and Source Layout

## Objective

Decide the responsibility-based artifact taxonomy, top-level source layout,
workspace boundaries, and explicit exceptions for examples, scripts, tools,
portable assets, and generated output.

## Scope and exclusions

R-0000-009 currently owns the location of additional implementations. This item
does not move files, create directories, select another runtime, or rename
assemblies.

## Questions to resolve

Compare the proposed `src/` taxonomy with retained alternatives; define what
counts as maintained software; decide nesting and workspace rules; and identify
every required amendment to existing path obligations.

## Acceptance criteria

- [ ] The adopted taxonomy and exceptions are normative and unambiguous.
- [ ] R-0000-009 is preserved or amended explicitly.
- [ ] Workspace, portable-asset, generated-output, and cross-artifact boundaries agree.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Record accepted behavior in SPEC-0008 and any amendment to SPEC.md.

## Validation and review

No validation or approval recorded.
