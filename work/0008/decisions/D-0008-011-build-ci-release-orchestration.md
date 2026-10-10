---
id: D-0008-011
kind: decision
title: Define build, CI, and release orchestration
status: open
spec: SPEC-0008
requirements: [R-0005-030, R-0005-032, R-0005-033]
depends_on: [D-0008-001, D-0008-002, D-0008-004, D-0008-007]
artifacts:
  - specs/0005-build-release-and-website-delivery.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-011: Define Build, CI, and Release Orchestration

## Objective

Define artifact-local commands, root orchestration, CI impact selection,
conformance-report handling, and consistent multi-artifact releases.

## Scope and exclusions

SPEC-0005 release, security, provenance, and recovery obligations remain in
force. This item does not select unapproved language, website, or extension
toolchains.

## Questions to resolve

Define required workspace entry points, root dispatch, shared-contract impact
fan-out, path filtering, evidence retention, report transport, and release
assembly across independent toolchains.

## Acceptance criteria

- [ ] Each workspace contract and root orchestration boundary is explicit.
- [ ] Shared contract changes trigger every affected implementation.
- [ ] Filtering cannot bypass required conformance or SPEC-0005 gates.
- [ ] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Unresolved. Record accepted behavior in SPEC-0008 and amend SPEC-0005 where needed.

## Validation and review

No validation or approval recorded.
