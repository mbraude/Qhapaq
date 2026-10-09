---
id: I-0007-030
kind: implementation
granularity: milestone
change_kind: maintenance
title: Shared local and blocking CI validation
status: open
spec: SPEC-0007
requirements: [R-0007-370]
depends_on: []
artifacts: [scripts, .github, docs/development]
---

# I-0007-030: Shared CI Checks

## Objective and coverage

Track local/CI build, architecture, schema, conformance and clean-consumer scripts
under SPEC-0005 as the corresponding artifacts appear, not after Phase 9.

## Entry gates

Exact owner-spec CI/event/permission contracts and artifact-specific consumers.
Existing build/test commands are baseline inputs, not evidence of every missing
CI, schema or consumer gate.

## File and ownership manifest

Pending per-artifact automation manifests; add tooling only with a defined consumer.

## Design and integration

Local and CI commands share entry points; preserve traceability and blocking checks.

## Tests and validation

Documented script behavior, failing-check propagation and clean CI consumer paths.

## Exit criteria

- [ ] Required gates exist for each delivered family when that family needs them.
- [ ] Script/CI checks and exact human review pass.

## Plan approval

Absent; companion milestone only.

## Delivery evidence and review

No workflow added or CI result claimed during extraction.
