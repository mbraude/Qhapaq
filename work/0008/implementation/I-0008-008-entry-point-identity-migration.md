---
id: I-0008-008
kind: implementation
granularity: milestone
change_kind: refactor
title: Apply matched .NET Entry Point identities
status: open
spec: SPEC-0008
requirements:
  - R-0006-001
  - R-0006-002
  - R-0006-021
  - R-0006-023
  - R-0006-024
  - R-0006-026
  - R-0006-028
  - R-0006-030
  - R-0006-031
  - R-0006-032
  - R-0006-033
depends_on: [D-0008-009, D-0008-012]
artifacts:
  - implementations/dotnet
---

# I-0008-008: Apply Matched .NET Entry Point Identities

## Objective and coverage

Rename the .NET top-layer directories, projects, assemblies, root namespaces,
derived source namespaces, tests, and direct consumers from
`Qhapaq.Implementations.*` to the approved `Qhapaq.EntryPoints.*` identities.
Preserve the `qhapaq` executable filename, existing distribution package IDs,
public behavior, and adjacent-layer dependency direction.

## Entry gates

D-0008-009 and D-0008-012 are complete; the affected SPEC-0006 amendment,
scope readiness, exact rename manifest, compatibility validation, and recovery
plan are approved.

## File and ownership manifest

Pending D-0008-012. Concrete slices must enumerate every production and test
directory, project reference, solution entry, namespace, architecture rule,
documentation consumer, automation input, and packaging input affected by the
identity change.

## Design and integration

Each production directory and project file must match its assembly and root
namespace. Handwritten source namespaces remain derived from the root namespace
and relative directories. Executable and package identities change only if a
separate approved decision requires it.

## Tests and validation

Run before-and-after restore, build, unit, integration, architecture, package,
executable-discovery, documentation-link, and traceability checks plus the
approved recovery exercise.

## Exit criteria

- [ ] Every approved identity and only those identities is renamed.
- [ ] Directory, project, assembly, root namespace, and source namespaces match.
- [ ] Executable, package, behavior, and dependency compatibility is preserved.
- [ ] Required validation passes.
- [ ] Explicit delivery review covers the exact implemented snapshot.

## Plan approval

Absent. This milestone requires decomposition or promotion to approved slices.

## Delivery evidence and review

No delivery evidence or approval recorded.
