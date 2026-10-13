---
id: I-0008-019
kind: implementation
granularity: slice
change_kind: requirement
title: Deliver conformance contract and lifecycle vectors
status: open
spec: SPEC-0008
requirements:
  - R-0007-347
  - R-0007-348
  - R-0008-007
  - R-0008-008
  - R-0008-009
  - R-0008-010
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
  - I-0007-002
  - I-0007-005
  - I-0008-018
artifacts:
  - conformance/conformance-contracts-v1/README.md
  - conformance/conformance-contracts-v1/profile-valid-runtime.json
  - conformance/conformance-contracts-v1/profile-invalid-prerequisite.json
  - conformance/conformance-contracts-v1/declaration-valid-progress.json
  - conformance/conformance-contracts-v1/declaration-valid-unsupported.json
  - conformance/conformance-contracts-v1/declaration-invalid-partial-claim.json
  - conformance/conformance-contracts-v1/assessment-valid-exhaustive.json
  - conformance/conformance-contracts-v1/assessment-invalid-omitted-obligation.json
  - conformance/conformance-contracts-v1/evidence-valid-all-of.json
  - conformance/conformance-contracts-v1/evidence-invalid-skipped.json
  - conformance/conformance-contracts-v1/evidence-invalid-sensitive.json
  - conformance/conformance-contracts-v1/evidence-invalid-digest.json
  - conformance/conformance-contracts-v1/publication-valid-profile.json
  - conformance/conformance-contracts-v1/publication-invalid-edge-claim.json
  - conformance/conformance-contracts-v1/lifecycle-valid-correction.json
  - conformance/conformance-contracts-v1/lifecycle-valid-withdrawal.json
---

# I-0008-019: Deliver Conformance Contract and Lifecycle Vectors

## Objective and coverage

Publish a bounded portable vector family proving the closed conformance
schemas, candidate profiles, evidence sufficiency, declaration validity, and
publication lifecycle rules. Every case uses the
`qhapaq.conformance-vector/v1` envelope and exact expected-result conventions
owned by SPEC-0007.

This slice does not duplicate cases in .NET fixtures, execute a profile against
an implementation, or publish a profile or claim.

## Entry gates

- I-0007-002 has delivered approved version-aware shared vector tooling and
  golden procedures at the exact paths in its approved child manifests.
- I-0007-005 has delivered approved strict-JSON, canonicalization, schema
  selection, embedded-profile, diagnostic, pattern, and format foundations at
  the exact paths in its approved child manifests.
- I-0008-018 and its schema prerequisite are complete and approved.
- I-0008-012 and this exact slice plan are approved.
- The implementation plan is reconciled if either SPEC-0007 milestone's final
  output paths differ from its currently pending milestone-level artifacts;
  no output is assumed to exist merely because it is named as a prerequisite.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| add | `conformance/conformance-contracts-v1/README.md` | Suite identity, version, capabilities, coverage, and regeneration rules | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/profile-valid-runtime.json` | Minimum valid exact runtime profile candidate | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/profile-invalid-prerequisite.json` | Reject invalid or cyclic prerequisite identity | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/declaration-valid-progress.json` | Accept exhaustive progress without claim language | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/declaration-valid-unsupported.json` | Accept explicit unsupported target and reason | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/declaration-invalid-partial-claim.json` | Reject exclusions or incomplete full claim | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/assessment-valid-exhaustive.json` | Accept complete obligation dispositions and mappings | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/assessment-invalid-omitted-obligation.json` | Reject omitted mandatory obligation | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/evidence-valid-all-of.json` | Accept a complete bounded recipe | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/evidence-invalid-skipped.json` | Keep skipped mandatory evidence unsuccessful | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/evidence-invalid-sensitive.json` | Reject evidence that violates payload-safety rules | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/evidence-invalid-digest.json` | Reject mismatched artifact or evidence digest | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/publication-valid-profile.json` | Accept exact approved protected profile input | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/publication-invalid-edge-claim.json` | Reject full claim promotion from edge | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/lifecycle-valid-correction.json` | Preserve original object and explicit supersession | Portable conformance | Public |
| add | `conformance/conformance-contracts-v1/lifecycle-valid-withdrawal.json` | Preserve tombstone and audit history | Portable conformance | Public |

## Design and integration

Each file is one self-contained envelope with stable suite/case identity, raw
JSON input, capability groups, typed expected outcome, and deterministic
ordered diagnostics. Inputs use synthetic non-sensitive values. Existing
alpha descriptor fixtures remain unchanged and are not treated as v1 envelope
or digest goldens.

Ordinary runs are read-only. Golden regeneration emits proposed changes and
requires normative review. The shared tooling reports exact suite versions and
capabilities and must not make .NET the semantic authority.

## Tests and validation

- Run the approved I-0007-002 read-only shared conformance command over this
  exact directory; record the command after that item's final plan establishes
  its syntax.
- Run its approved offline golden proposal command and verify a no-diff result.
- Validate all raw inputs against the appropriate I-0008-017 schema and verify
  exact diagnostics for rejected cases.
- Repeat under the cultures, path roots, and input order variations required by
  I-0007-005; bytes and ordered outcomes must remain identical.
- Run `git diff --check` and `spec-trace-check`.

The final plan approval must replace the two command references above with the
documented exact commands from completed I-0007-002; absence of those commands
is an execution blocker, not permission to invent parallel tooling.

## Exit criteria

- [ ] Every listed case passes with its exact expected result through the
  approved shared tooling.
- [ ] Read-only execution changes no tracked file and golden proposal produces
  no unexplained change.
- [ ] Culture, path, input-order, and offline runs are deterministic.
- [ ] Delivery evidence records suite and case identities, exact file digests,
  tooling identity, commands, results, and explicit review.

## Plan approval

Absent. Approval is blocked until I-0007-002 and I-0007-005 have approved child
manifests and the exact shared commands and artifact paths are reconciled here.

## Delivery evidence and review

No portable vector or golden has been produced or approved.
