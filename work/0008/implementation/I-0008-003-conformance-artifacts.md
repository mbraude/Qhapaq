---
id: I-0008-003
kind: implementation
granularity: milestone
change_kind: requirement
title: Deliver conformance profiles, declarations, and evidence artifacts
status: open
spec: SPEC-0008
requirements:
  - R-0005-034
  - R-0005-035
  - R-0006-035
  - R-0006-036
  - R-0006-037
  - R-0006-038
  - R-0006-039
  - R-0007-347
  - R-0007-348
  - R-0008-006
  - R-0008-007
  - R-0008-008
  - R-0008-009
  - R-0008-010
  - R-0008-011
  - R-0008-012
  - R-0008-013
  - R-0008-014
  - R-0008-015
  - R-0008-019
  - R-0008-020
  - R-0008-021
  - R-0008-022
  - R-0008-023
  - R-0008-024
  - R-0008-025
  - R-0008-026
  - R-0008-027
  - R-0008-028
  - R-0008-029
depends_on:
  - D-0008-004
  - D-0008-005
  - D-0008-006
  - D-0008-007
  - D-0008-010
  - D-0008-011
  - D-0008-012
  - D-0008-013
  - D-0007-009
  - D-0007-011
  - D-0007-015
  - I-0008-012
  - I-0007-002
  - I-0007-005
artifacts: []
---

# I-0008-003: Deliver Conformance Profiles, Declarations, and Evidence Artifacts

## Objective and coverage

Deliver approved profile definitions, declaration schemas, shared evidence
contracts, reports, vectors, publication records and status history, and
protected-release integration for the four initial profiles and their
cumulative prerequisites. The profile boundaries and claim restrictions are
governed, but this milestone remains non-executable until its remaining
planning gates are complete.

## Entry gates

All listed decisions and the I-0008-012 concrete delivery plan are complete;
accepted requirements, schemas, vector groups, exact publication gates, and
scope readiness are approved. The SPEC-0007 prerequisites are actual completed
tooling and validation-foundation outputs, not merely planned work.

The .NET profile must respect SPEC-0006 layer ownership and validation
boundaries. Shared portable validation, profile artifacts, and host-specific
orchestration must remain assigned to their governing owners; release
integration must include the required manifest and recovery evidence.

## File and ownership manifest

Pending accepted formats and ownership. Concrete slices must name authoritative
schemas, vectors, harness adapters, reports, documentation, and release wiring.

## Design and integration

Keep portable assets language-neutral, harnesses language-specific, claims
exact-versioned, and missing evidence explicitly unsuccessful.
Apply the workspace ownership and root orchestration boundaries in R-0008-019
through R-0008-022. Deliver this work in the sequence required by R-0008-027,
with exact before-and-after input snapshots, validation, and recovery evidence
for each migration stage under R-0008-028 and R-0008-029. Honor the
dedicated-branch gate for migration work; it is a scope-specific requirement
and is not relaxed by the repository's optional general branch workflow.

## Tests and validation

Cover valid and invalid declarations, profile dependencies, compatibility,
skips and failures, secret-free reports, reproducibility, exact approval and
release bindings, lifecycle transitions, correction, withdrawal, evidence
availability, retention, audit history, and publication gates.

## Exit criteria

- [ ] Approved profile and declaration artifacts exist.
- [ ] Sufficient evidence is produced for exact builds and profile revisions.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
