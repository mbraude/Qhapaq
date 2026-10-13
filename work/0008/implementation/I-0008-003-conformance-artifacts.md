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
  - I-0008-017
  - I-0008-018
  - I-0008-019
  - I-0008-020
  - I-0008-021
artifacts:
  - schemas
  - conformance
  - implementations/dotnet/tests
  - build
  - scripts
  - .github/workflows
---

# I-0008-003: Deliver Conformance Profiles, Declarations, and Evidence Artifacts

## Objective and coverage

Deliver approved profile definitions, declaration schemas, shared evidence
contracts, reports, vectors, publication records and status history, and
protected-release integration for the four initial profiles and their
cumulative prerequisites. This is the non-executable aggregate gate for:

1. [I-0008-017](I-0008-017-conformance-contract-schemas.md), which delivers
   the closed portable schemas.
2. [I-0008-018](I-0008-018-profile-definitions.md), which delivers the four
   candidate profile definitions and evidence matrices.
3. [I-0008-019](I-0008-019-conformance-contract-vectors.md), which delivers
   portable contract, evidence, and lifecycle vectors.
4. [I-0008-020](I-0008-020-dotnet-conformance-evidence.md), which connects the
   shared artifacts to the existing .NET test surfaces and produces immutable
   evidence.
5. [I-0008-021](I-0008-021-conformance-publication-integration.md), which
   enforces protected profile and claim promotion through the exact root
   release manifest.

The child sequence preserves every outcome formerly assigned to this
milestone. The aggregate cannot be completed merely because its children are
complete; it still requires exact delivery evidence and explicit review.

## Entry gates

All child slices are complete and explicitly delivery-approved. Their
individual entry gates preserve the exact decision, readiness, SPEC-0007
artifact, root-orchestration, and publication prerequisites at the first point
where each is actually consumed.

The .NET profile must respect SPEC-0006 layer ownership and validation
boundaries. Shared portable validation, profile artifacts, and host-specific
orchestration must remain assigned to their governing owners; release
integration must include the required manifest and recovery evidence.

## File and ownership manifest

This aggregate owns no files independently. The exact union of the five child
manifests is the aggregate manifest; overlapping ownership is prohibited.

## Design and integration

Keep portable assets language-neutral, harnesses language-specific, claims
exact-versioned, and missing evidence explicitly unsuccessful. Child ownership
follows R-0008-019 through R-0008-022. Completing this aggregate satisfies the
conformance-artifact prerequisite in migration stage 2 of R-0008-027.

These children do not rename or relocate repository files and therefore are
not executable migration slices. If execution planning adds a move, rename, or
other migration action, that affected slice must stop for separate scope
readiness and add the exact before/after validation, dedicated-branch,
checkpoint, user-change preservation, and recovery gates in R-0008-028 and
R-0008-029.

## Tests and validation

The child validation union covers valid and invalid declarations, profile
dependencies, compatibility, skips and failures, secret-free reports,
reproducibility, exact approval and release bindings, lifecycle transitions,
correction, withdrawal, evidence availability, retention, audit history, and
publication gates. Aggregate review verifies that no former acceptance
criterion is uncovered and that the evidence from each child names the exact
artifact bytes it validated.

## Exit criteria

- [ ] I-0008-017 through I-0008-021 are complete with approved delivery
  evidence for their exact snapshots.
- [ ] Approved profile and declaration artifacts exist.
- [ ] Sufficient evidence is produced for exact builds and profile revisions.
- [ ] Protected publication consumes the same verified bytes and fails closed
  for missing, invalid, unsuccessful, skipped, unavailable, or mismatched
  required inputs.
- [ ] Required validation passes across the complete child evidence set.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Not applicable to execution; this is an aggregate milestone. Each child slice
requires its own exact plan approval after I-0008-012 is approved.

## Delivery evidence and review

I-0008-003 was decomposed without changing its identity, requirements, or
acceptance outcome. No child plan or delivery is approved, and no schema,
vector, profile, report, claim, publication record, workflow, or release was
created by this planning change.
