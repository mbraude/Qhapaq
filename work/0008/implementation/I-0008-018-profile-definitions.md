---
id: I-0008-018
kind: implementation
granularity: slice
change_kind: requirement
title: Deliver initial profile definitions and evidence matrices
status: open
spec: SPEC-0008
requirements:
  - R-0007-347
  - R-0008-006
  - R-0008-007
  - R-0008-008
  - R-0008-011
  - R-0008-012
  - R-0008-013
  - R-0008-014
  - R-0008-015
  - R-0008-023
  - R-0008-024
  - R-0008-025
  - R-0008-026
depends_on:
  - I-0008-017
artifacts:
  - conformance/profiles/README.md
  - conformance/profiles/qhapaq.runtime/candidates/1.0/profile.json
  - conformance/profiles/qhapaq.cli.local/candidates/1.0/profile.json
  - conformance/profiles/qhapaq.mcp.host/candidates/1.0/profile.json
  - conformance/profiles/qhapaq.dotnet.in-process/candidates/1.0/profile.json
---

# I-0008-018: Deliver Initial Profile Definitions and Evidence Matrices

## Objective and coverage

Create reviewable candidate `1.0` definitions for `qhapaq.runtime`,
`qhapaq.cli.local`, `qhapaq.mcp.host`, and `qhapaq.dotnet.in-process`. Each
candidate binds the exact authoritative revisions, ordered mandatory
requirement ID/fingerprint pairs, exact prerequisite profile candidates,
optional capabilities, and a complete profile-fixed evidence matrix.

Candidate paths do not make the files published profile versions and cannot
support conformance claims. I-0008-021 owns protected promotion and publication
records.

## Entry gates

- I-0008-017 is complete and its exact schema bytes are approved.
- I-0008-012 and this exact slice plan are explicitly approved.
- The authoritative requirement inventory and fingerprints are current.
- Each selected obligation is reviewed for applicability to the named surface;
  a disputed obligation or absent normative rule blocks the affected profile
  rather than being made optional or inferred.
- Evidence recipe leaves name only portable evidence kinds and exact executable
  bounds governed by R-0008-011.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| add | `conformance/profiles/README.md` | Explain candidate versus published state, review, and immutable promotion | Portable conformance profiles | Public |
| add | `conformance/profiles/qhapaq.runtime/candidates/1.0/profile.json` | Runtime baseline obligations and evidence matrix | Portable conformance profiles | Public candidate |
| add | `conformance/profiles/qhapaq.cli.local/candidates/1.0/profile.json` | Local CLI obligations plus exact runtime prerequisite | Portable conformance profiles | Public candidate |
| add | `conformance/profiles/qhapaq.mcp.host/candidates/1.0/profile.json` | MCP host, policy, disclosure, and runtime obligations | Portable conformance profiles | Public candidate |
| add | `conformance/profiles/qhapaq.dotnet.in-process/candidates/1.0/profile.json` | In-process .NET API, architecture, and runtime obligations | Portable conformance profiles | Public candidate |

## Design and integration

Profiles reference specifications and requirements; they do not copy normative
prose or create another executable pipeline format. CLI and MCP remain sibling
profiles. All three surface profiles bind the same exact runtime prerequisite,
and cumulative obligation evaluation is deterministic.

Each mandatory obligation maps to a complete `all-of`/`any-of` recipe over the
closed evidence kinds. Vector evidence identifies exact suite versions and
capabilities. Language-specific tests, architecture tests, security analysis,
review, build provenance, and release evidence remain distinct leaves where
vectors alone are insufficient. Missing or inapplicable mappings are not
success.

## Tests and validation

- Validate all four files against
  `schemas/conformance-profile-v1.schema.json`.
- Recompute every requirement fingerprint from the authoritative block and
  compare the ordered inventory.
- Verify transitive prerequisite closure, no profile cycle, no partial
  obligation, and no CLI/MCP sibling dependency.
- Verify every mandatory obligation has a satisfiable but non-weakened recipe,
  every executable leaf has a finite bound, and synthetic-data requirements
  cover payload-bearing evidence.
- Run `git diff --check` and `spec-trace-check`.

## Exit criteria

- [ ] The four candidate files validate and bind current exact requirement
  fingerprints and source revisions.
- [ ] Prerequisite closure and evidence matrices are complete and acyclic.
- [ ] Review confirms that no mandatory obligation was omitted, weakened,
  substituted, or treated as optional.
- [ ] Delivery evidence records exact candidate digests, fingerprint and
  matrix checks, and explicit review of the delivered snapshot.
- [ ] No profile or conformance claim is represented as published.

## Plan approval

Absent. Approval must cover the exact four-profile obligation inventory,
evidence matrices, manifest, dependencies, and gates.

## Delivery evidence and review

No profile candidate, profile version, declaration, or publication record has
been produced or approved.
