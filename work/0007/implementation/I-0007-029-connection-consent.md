---
id: I-0007-029
kind: implementation
granularity: milestone
change_kind: requirement
title: Trusted connection planning and independent local consent
status: open
spec: SPEC-0007
requirements: [R-0007-370]
depends_on: [I-0007-010]
artifacts: [specs/0004-ai-assisted-connections.md, schemas, conformance, implementations/dotnet]
---

# I-0007-029: Connection Planning and Consent

## Objective and coverage

Track planning, independent local consent, authentication, sanitized status/tests,
revocation and approved reload/restart under SPEC-0004.

## Entry gates

Real Phase 3A host boundaries and exact enabled connector/provider contracts.
Concrete slices must name those contracts and their prerequisite items.

## File and ownership manifest

Pending owner-spec decisions and trusted broker/provider/adapter/test manifests.

## Design and integration

MCP authoring and generic tool approval never substitute for trusted local consent.
Keep credential state and payload disclosure outside model-visible plans.

## Tests and validation

Consent binding, changed-plan rejection, authentication, sanitized failures,
revocation, cancellation and approved configuration lifecycle.

## Exit criteria

- [ ] Supported connection flow conforms to exact owner-spec contracts/vectors.
- [ ] Consent and privacy boundaries, checks and human review pass.

## Plan approval

Absent; companion milestone only.

## Delivery evidence and review

No connection or consent flow delivered during bootstrap.
