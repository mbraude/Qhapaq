---
id: I-0007-028
kind: implementation
granularity: milestone
change_kind: requirement
title: OpenAPI import, generic HTTP and installed-extension integration
status: open
spec: SPEC-0007
requirements: [R-0007-370]
depends_on: [I-0007-009, I-0007-010]
artifacts: [specs/0002-operation-catalogs-and-host-configuration.md, schemas, conformance, implementations/dotnet]
---

# I-0007-028: OpenAPI and Extensions

## Objective and coverage

Track supported import, generic HTTP execution, packaging and extension
administration under SPEC-0002, integrated with registry and trusted host sources.

## Entry gates

Exact owner-spec contracts/decisions and enabled source/provider integrity rules.
Decision work can proceed earlier; this dependency applies to integration delivery.

## File and ownership manifest

Pending owner-spec extraction and per-capability implementation manifests.

## Design and integration

Equivalent portable descriptors, exact identity, destination/authentication
restrictions and explicit trusted installation; authoring never installs code.

## Tests and validation

Import selection, integrity, conflicting contracts, HTTP policy/auth boundaries,
extension administration and equivalent descriptor results.

## Exit criteria

- [ ] Each supported source passes contracts and registry/host integration checks.
- [ ] Required vectors and review exist before enabling or advertising it.

## Plan approval

Absent; companion milestone only.

## Delivery evidence and review

No extension or remote connector capability approved by extraction.
