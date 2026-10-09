---
id: I-0007-002
kind: implementation
granularity: milestone
change_kind: maintenance
title: Shared vector tooling and golden-file procedures
status: open
spec: SPEC-0007
requirements: [R-0007-347]
depends_on: [D-0007-013, D-0007-015]
artifacts: [conformance/README.md, implementations/dotnet/tests]
---

# I-0007-002: Conformance Tooling

## Objective and coverage

Implement version-aware shared vector consumption and golden maintenance.
Cover the first two Phase 1 checklist entries with D-0007-015's envelope decision.

## Entry gates

Accepted portable envelope and .NET test conventions; approved relevant readiness.

## File and ownership manifest

Pending slice planning. Tooling locations/files must follow reviewed ownership.

## Design and integration

Do not copy portable cases into host-specific fixtures. Report exact versions
and capabilities exercised; preserve existing alpha fixtures.

## Tests and validation

Test loading, malformed/unsupported envelopes, expected-result comparison, and
deterministic golden regeneration using documented commands selected in planning.

## Exit criteria

- [ ] Reusable tooling consumes shared families and reports exact identities.
- [ ] Regeneration is reviewable; checks pass and delivery is approved.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No tool or envelope publication performed during extraction.
