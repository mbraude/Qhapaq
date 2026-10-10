---
id: I-0007-025
kind: implementation
granularity: milestone
change_kind: requirement
title: Public policy-gated execution and claimed conformance
status: open
spec: SPEC-0007
requirements: [R-0007-337, R-0007-369, R-0007-411, R-0007-412, R-0007-413, R-0007-415, R-0007-417, R-0007-418, R-0007-419, R-0007-420, R-0007-421, R-0007-422, R-0007-423]
depends_on: [D-0007-005, I-0007-017, I-0007-023, I-0007-024]
artifacts: [implementations/dotnet, docs]
---

# I-0007-025: Enable Execution

## Objective and coverage

Phase 9: separate execution Service; normative CLI requests/results/diagnostics/
exit status; MCP independent execution/disclosure; complete claimed conformance,
inline-definition and exact-reference modes; withheld-output results; generator/
registry/native/cache/architecture/security/AOT tests and capability docs.

## Entry gates

Phases 0 through 8 for every enabled surface, all parse-to-permission checks and
required suites. Optional advertisements do not remove required v1 scope.
No intermediate milestone allows a partial v1 execution-conformance claim.

## File and ownership manifest

Pending exact Service/adapter/publication/verification slice manifests.

## Design and integration

Authoring cannot install extensions, change trusted profiles, resolve credentials,
execute operations or grant authority. Definitions cannot load code or inspect frames.

## Tests and validation

All claimed language-neutral/host suites, generator determinism/byte equality,
native/cache/architecture/security, supported trimming/AOT and enabled capabilities.

## Exit criteria

- [ ] Full safety path and all claimed suites pass before public enablement.
- [ ] Capability documentation, supported-target checks and human review pass.

## Plan approval

Absent; milestone only.

## Delivery evidence and review

No execution or release readiness declared by bootstrap.
