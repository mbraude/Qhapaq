---
id: I-0007-031
kind: implementation
granularity: milestone
change_kind: requirement
title: Package composition and release-shaped distribution verification
status: open
spec: SPEC-0007
requirements: [R-0007-370]
depends_on: [I-0007-030]
artifacts: [specs/0005-build-release-and-website-delivery.md, build, implementations/dotnet, docs]
---

# I-0007-031: Distribution Verification

## Objective and coverage

Track package composition, supported-target decisions, self-contained CLI/container,
release-shaped builds and clean installation under SPEC-0005.

## Entry gates

Exact supported targets and package contracts; reviewed delivered capabilities
for each distribution. Concrete execution distributions require I-0007-025;
do not delay independent target/package decisions until the runner completes.

## File and ownership manifest

Pending target-specific build/package/install test manifests.

## Design and integration

Do not advertise unverified distributions or confuse artifact production with release.

## Tests and validation

Clean installation, package composition, target matrix, self-contained and
container behavior, supported trimming/AOT and release-shaped artifact consistency.

## Exit criteria

- [ ] All advertised distributions pass required owner-spec checks.
- [ ] Targets, evidence and exact human review are recorded before advertisement.

## Plan approval

Absent; companion milestone only.

## Delivery evidence and review

No target, package publication or installation claim made.
