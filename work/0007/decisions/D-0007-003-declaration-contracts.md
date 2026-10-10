---
id: D-0007-003
kind: decision
title: Declaration APIs, manifest envelope and generator compatibility
status: complete
spec: SPEC-0007
requirements: [R-0007-252, R-0007-253, R-0007-257, R-0007-258, R-0007-261, R-0007-263, R-0007-265, R-0007-268, R-0007-269, R-0007-290, R-0007-291, R-0007-293, R-0007-295, R-0007-296, R-0007-335, R-0007-344, R-0007-397, R-0007-398, R-0007-399]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-003: Declaration Contracts

## Objective

Resolve the declaration, manifest, diagnostic, and compatibility contracts in
R-0007-344 and the former Section 23 question 1.

## Scope and exclusions

Supported .NET authoring/registration APIs, portable manifest envelope,
diagnostic-code policy, and initial compatibility matrix. Organization decisions
are coordinated with Phase 0A; no implementation classes are scaffolded here.
Namespaces cannot be finalized inconsistently with those decisions.

## Questions to resolve

What are the exact marker constructor, static declaration and generated API
names, manifest shape, stable diagnostic codes, registration contract versions,
and accepted/emitted descriptor/manifest support matrix?

## Acceptance criteria

- [x] Public authoring shapes and required runtime registration APIs are explicit.
- [x] Manifest closure, canonical ordering, byte equality, and version axes agree.
- [x] Diagnostics cover required rejected inputs with stable safe mappings.
- [x] Supported, mixed, unknown, and incompatible versions have exact outcomes.
- [x] Related examples and conformance expectations agree; existing alpha format
  is preserved rather than silently rewritten.
- [x] Checks pass and the exact decision is reviewed and approved.

## Resolution

Resolved in
[SPEC-0007 Sections 12.1 through 13.4](../../../specs/0007-portable-pipeline-definitions-and-binding.md#121-authoritative-source):

- R-0007-252, R-0007-253, R-0007-257, and R-0007-258 define the stable
  `QhapaqOperationAttribute`, inferred and explicit same-directory descriptor
  association, and supported partial authoring shape.
- R-0007-263 and R-0007-265 define the V1Alpha1 generic static declaration
  interface, immutable descriptor return type, and public generated registration
  entry point.
- R-0007-268 and R-0007-269 define the minimal closed canonical manifest and
  embedded/package byte equality.
- R-0007-261 defines `QHPG0001` through `QHPG0012` and their safe,
  deterministic diagnostic policy.
- R-0007-290, R-0007-291, and R-0007-397 close the initial exact alpha support
  matrix and whole-package rejection behavior.
- R-0007-398 keeps the handwritten marker stable while versioning generated
  declaration and registration namespaces side by side.
- R-0007-399 keeps host/catalog-version membership out of operation declarations
  and requires a later Service/host contract over exact operation references.

Model ownership remains coordinated with
[D-0007-009](D-0007-009-model-ownership.md), and generator/runtime algorithm
reuse remains coordinated with
[D-0007-012](D-0007-012-generator-runtime-reuse.md). Neither is an artificial
dependency of this contract decision.

## Validation and review

Decision input: on 2026-10-09 the user selected:

- a stable marker with parameterless inference and an explicit same-directory
  basename override;
- a generic static declaration interface returning an immutable
  `OperationDescriptor`;
- an assembly-root public registration entry point with `Register` and
  `ManifestBytes`;
- the minimal portable manifest envelope;
- the twelve-code `QHPG` diagnostic taxonomy;
- the strict initial alpha-only compatibility matrix; and
- versioned generated namespaces while keeping catalog-version membership in
  trusted host and Service contracts.

Validation performed on 2026-10-09:

- Work-artifact structure: PASS. Checked 48 unique item identities, required
  sections by item kind, 95 dependency edges, acyclic ordering, no unknown
  prerequisite, and one phase or cancelled membership per item.
- Specification structure: PASS. All 399 R-0007 identifiers are unique;
  R-0007-397 through R-0007-399 use the next unused sequence and no prior
  identifier was removed or retired.
- Specification trace check: PASS with warnings. Classified as `requirement`
  because the change adds three platform requirement blocks while amending
  eleven existing blocks. Repository-wide reverse-impact search found no stale
  code or test fingerprint, no changed implementation, and no new waiver.
  Semantic review checked R-0007-251 through R-0007-276, R-0007-290 through
  R-0007-296, R-0007-335, R-0007-344, and R-0006-027. The warning is expected:
  this explicitly .NET-specific section names public CLR APIs and generator
  package contracts.
- Contract consistency: PASS. The marker overloads preserve one descriptor per
  operation; the generated generic declaration agrees with `IOperation`; the
  minimal manifest preserves complete exact-format descriptors; diagnostics
  cover every required rejected-input category; and generator and host
  compatibility fail closed on every unsupported axis.
- Documentation checks: PASS. `git diff --check` reported no whitespace error,
  changed local links resolve, and all 11 plan source hashes match the exact
  current bytes.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and creates no implementation.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `c9e1ca80ab12dfe5892f54fcf2d16bf1b958f45ccb15fc21c476ff4ed5e88d31` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | SHA-256 `a9b6fbc797c0134a5aacfc77792c1d48d22f25c92c33fe0ca760f6fa7b68b520` |
| `work/0007/plan.md` | SHA-256 `6c5d7e787c9d2b3533bacb2a973ce00a250198719d4c0f344d1aa8fc47a5c40f` |
| `work/0007/decisions/D-0007-005-subsequent-surface-contracts.md` | SHA-256 `4607edebbbdad8b7324551e5cf8d553fa1ae0d7ffcb08f27f074a417eb7fcad6` |

Approval does not authorize implementation, publication, or a readiness claim.

Approval recorded on 2026-10-09: the user explicitly approved this exact
corrected snapshot in this session.

Approved scope: D-0007-003's declaration, manifest, diagnostic, compatibility,
and catalog-version-separation outcome, plus the bounded SPEC-0007 plan
reconciliation. Commit scope: this decision, SPEC-0007,
`work/0007/plan.md`, and D-0007-005's downstream catalog-membership clarification.
Exclusions: implementation, generated artifacts, schema or conformance
publication, specification readiness, and contract publication.

Approval covers the unchanged material content with SHA-256
`c9e1ca80ab12dfe5892f54fcf2d16bf1b958f45ccb15fc21c476ff4ed5e88d31`, plus
these exact input/output snapshots:

| Material | SHA-256 |
| --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `a9b6fbc797c0134a5aacfc77792c1d48d22f25c92c33fe0ca760f6fa7b68b520` |
| `work/0007/plan.md` | `6c5d7e787c9d2b3533bacb2a973ce00a250198719d4c0f344d1aa8fc47a5c40f` |
| `work/0007/decisions/D-0007-005-subsequent-surface-contracts.md` | `4607edebbbdad8b7324551e5cf8d553fa1ae0d7ffcb08f27f074a417eb7fcad6` |

### Proposed commit trailers

```text
Change-Kind: requirement
Spec: R-0007-252@32845a, R-0007-253@bb5d63, R-0007-257@32509e, R-0007-258@4c952d
Spec: R-0007-261@6ed893, R-0007-263@1c008f, R-0007-264@33ec04, R-0007-265@a31066
Spec: R-0007-268@41a3d4, R-0007-291@5d715d, R-0007-335@8624e5
Spec: R-0007-397@53ea6b, R-0007-398@d22ab5, R-0007-399@2edf98
```
