---
id: I-0008-017
kind: implementation
granularity: slice
change_kind: requirement
title: Deliver portable conformance contract schemas
status: open
spec: SPEC-0008
requirements:
  - R-0005-034
  - R-0005-035
  - R-0007-347
  - R-0008-008
  - R-0008-009
  - R-0008-010
  - R-0008-011
  - R-0008-012
  - R-0008-013
  - R-0008-014
  - R-0008-015
  - R-0008-022
  - R-0008-023
  - R-0008-024
  - R-0008-025
  - R-0008-026
depends_on:
  - I-0008-012
artifacts:
  - schemas/conformance-profile-v1.schema.json
  - schemas/conformance-declaration-v1.schema.json
  - schemas/conformance-assessment-v1.schema.json
  - schemas/conformance-evidence-bundle-v1.schema.json
  - schemas/conformance-publication-record-v1.schema.json
  - schemas/conformance-status-entry-v1.schema.json
  - schemas/qhapaq-release-manifest-v1.schema.json
  - schemas/README.md
---

# I-0008-017: Deliver Portable Conformance Contract Schemas

## Objective and coverage

Deliver the closed, versioned, language-neutral JSON Schema contracts needed to
represent profile definitions, declarations, assessment manifests, evidence
bundles, immutable publication records, append-only status entries, and the
root release manifest that binds those exact inputs. The schemas express only
the semantics already fixed by the listed requirements.

This slice does not choose profile obligations, publish a profile or claim,
implement a harness, define a workspace command, or promote a release.

## Entry gates

- I-0008-012 is complete and this exact slice plan is explicitly approved.
- The approved `conformance-artifact-delivery` readiness snapshot remains
  applicable to the current authoritative sources.
- The seven format identities and schema identifiers are reviewed as concrete
  representations of R-0005-034, R-0005-035, and R-0008-008 through
  R-0008-026; any missing product semantic stops this slice for a specification
  decision rather than being invented in JSON Schema.
- Existing `operation-descriptor-v1alpha1` assets remain unchanged.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| add | `schemas/conformance-profile-v1.schema.json` | Closed profile definition and evidence-recipe matrix envelope | Portable root schemas | Public portable contract |
| add | `schemas/conformance-declaration-v1.schema.json` | Closed claim, progress, and unsupported-target declaration envelope | Portable root schemas | Public portable contract |
| add | `schemas/conformance-assessment-v1.schema.json` | Exhaustive obligation dispositions and evidence mappings | Portable root schemas | Public portable contract |
| add | `schemas/conformance-evidence-bundle-v1.schema.json` | Immutable bounded outcomes, exact inputs, digests, provenance, and approvals | Portable root schemas | Public portable contract |
| add | `schemas/conformance-publication-record-v1.schema.json` | Content-addressed profile or claim publication record | Portable root schemas | Public portable contract |
| add | `schemas/conformance-status-entry-v1.schema.json` | Closed append-only profile and claim lifecycle entry | Portable root schemas | Public portable contract |
| add | `schemas/qhapaq-release-manifest-v1.schema.json` | Exact root release membership and digest binding | Portable root schemas | Public portable contract |
| modify | `schemas/README.md` | Index the contracts, identities, offline resolution, and compatibility rules | Portable root documentation | Public |

No generated validators or copied language-specific models are checked in.

## Design and integration

All `$id` and `$ref` values are stable and offline-resolvable. Each schema is
closed, rejects unknown format versions and ambiguous fields, and keeps source
revisions distinct from immutable artifact-set digests. The declaration schema
does not duplicate requirement fingerprints; the assessment schema owns the
exhaustive requirement-level result. Evidence recipes and outcomes use only
the closed kinds and dispositions in R-0008-011 through R-0008-013.

Publication records and status entries remain immutable objects. Corrections,
supersession, deprecation, retirement, and withdrawal create new records rather
than overwrite earlier bytes. The release-manifest schema binds rather than
embeds or rewrites workspace evidence and cannot turn edge progress into a
full claim.

## Tests and validation

- Validate every schema against the repository's documented JSON Schema
  dialect and resolve every reference offline.
- Validate hand-authored minimum valid and targeted invalid instances during
  this slice; I-0008-019 turns the approved instances into the versioned
  portable vector families.
- Check closed-property behavior, exact format identities, digest shapes,
  declaration-kind exclusivity, exhaustive assessment dispositions, recipe
  kinds, outcome kinds, approval bindings, and lifecycle transitions.
- Run `git diff --check`.
- Run `spec-trace-check`.
- No .NET build or unit test is required until I-0008-019 and I-0008-020
  connect these schemas to shared tooling and adapters.

## Exit criteria

- [ ] Every manifest file exists at the exact path and contains no unresolved
  external reference.
- [ ] Valid instances pass and targeted unknown-version, partial-claim,
  skipped-evidence, digest-mismatch, lifecycle, and edge-promotion cases fail.
- [ ] README identities and compatibility guidance match the schema bytes.
- [ ] Validation and traceability checks pass.
- [ ] Delivery evidence records exact schema digests, commands, results, and
  explicit review of the delivered snapshot.

## Plan approval

Absent. Approval must cover this exact scope, manifest, dependencies, and entry
and exit gates after I-0008-012 is approved.

## Delivery evidence and review

No schema has been produced, approved, or published. Delivery must record the
exact schema bytes and validation output; work-item approval is not profile,
claim, component-contract, or release publication.
