---
id: D-0007-008
kind: decision
title: Feature folders and canonical namespace conventions
status: complete
spec: SPEC-0007
requirements: [R-0007-346, R-0006-021, R-0006-025]
depends_on: []
artifacts: [docs/development/coding-conventions.md]
---

# D-0007-008: Folder and Namespace Conventions

## Objective

Close the first Phase 0A organization checkpoint before public APIs expand.

## Scope and exclusions

Feature folders, folder-to-namespace mapping, and canonical naming inside
established assemblies. Do not rename layers or create placeholder production types.

## Questions to resolve

How are features nested within each owning assembly? Which folder/namespace
exceptions, if any, are justified and enforceable?

## Acceptance criteria

- [x] Persistent conventions cover representative features and namespace mapping.
- [x] Existing assembly, visibility, and dependency rules remain intact.
- [x] Architecture-test expectations are identified for I-0007-001.
- [x] Checks pass and the exact policy snapshot is prepared for explicit review.

## Resolution

Resolved as ordinary engineering policy in
[Production feature folders and namespaces](../../../docs/development/coding-conventions.md#production-feature-folders-and-namespaces):

- Every handwritten production source file maps its complete project-relative
  directory path, with exact casing, beneath the owning `RootNamespace`.
- Project-root source files use the `RootNamespace`.
- No handwritten-source exception may omit, add, or rename a path-derived
  namespace segment.
- SDK- and compiler-generated files outside production source directories are
  excluded. Qhapaq-generated source remains subject to its separately specified
  generated namespace contract and corresponding generator tests.
- I-0007-001 must enforce the handwritten file-to-namespace mapping by deriving
  expected namespaces from project roots and relative directories. It must not
  treat this rule as enforcement of generated namespace contracts.

The policy preserves R-0006-021 assembly and root-namespace identities and
R-0006-025 ownership signaling. It adds no layer, dependency, visibility
exception, model-ownership decision, or placeholder production type.

## Validation and review

Decision input: on 2026-10-10 the user selected exact project-relative path
mapping and no handwritten-source exceptions. Generated sources remain
separately governed.

Validation performed on 2026-10-10:

- Existing-source conformance: PASS. Every handwritten production C# file
  currently maps its project-relative directory exactly beneath its owning
  project root namespace.
- Work-artifact structure: PASS. Checked 48 unique item identities, all
  dependency references, and changed Markdown links. D-0007-008 remains the
  only resolved decision; I-0007-001 retains all existing dependencies.
- Source snapshots: PASS. All 12 plan source records match exact current bytes.
  The coding-conventions record uses the accepted working-copy policy and
  retains its committed baseline revision.
- Specification trace check: PASS. Classified as `maintenance`; the
  reverse-impact review covered R-0007-346, R-0006-021, and R-0006-025. No
  specification block, product code, or test code changed; no stale
  fingerprint, semantic conflict, or waiver was found.
- Documentation checks: PASS. `git diff --check` reported no whitespace error,
  and changed local links resolve.
- No build or unit tests were run because this decision changes engineering
  policy and planning documentation only and creates no implementation.

Exact ready-for-review snapshot:

| Material | Snapshot |
| --- | --- |
| This decision's material content | SHA-256 `d7d56781ba6ad1390e4aa5af9f6fece95c62430a79aee17b5842e7ce494a9a58` |
| `docs/development/coding-conventions.md` | SHA-256 `a83462c164858646583ac9137e20f7ab4f047648be9663790a23a50ae1f66867` |
| `work/0007/plan.md` | SHA-256 `028b2461e80f0a799be2cf45771847077220f4018369951d58b6d151fbad058e` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | SHA-256 `5ff5c3d2f2d84e10e1d1ebb41f8f3edb5a723b6254a02d42e26c7c7166cf6cdf` |

Approval recorded on 2026-10-10: the user explicitly approved this exact
snapshot in this session.

Approved scope: completion of D-0007-008 and its production feature-folder and
namespace policy, including reconciliation of the 0007 plan source snapshot and
the downstream I-0007-001 enforcement expectation. Exclusions: production or
test code, layer or dependency changes, model-ownership decisions, placeholder
types, implementation approval, schemas, conformance vectors, and contract
publication.

The approval covers this unchanged material content with SHA-256
`d7d56781ba6ad1390e4aa5af9f6fece95c62430a79aee17b5842e7ce494a9a58`,
plus these exact input/output snapshots:

| Material | SHA-256 |
| --- | --- |
| `docs/development/coding-conventions.md` | `a83462c164858646583ac9137e20f7ab4f047648be9663790a23a50ae1f66867` |
| `work/0007/plan.md` | `028b2461e80f0a799be2cf45771847077220f4018369951d58b6d151fbad058e` |
| `work/0007/implementation/I-0007-001-architecture-enforcement.md` | `5ff5c3d2f2d84e10e1d1ebb41f8f3edb5a723b6254a02d42e26c7c7166cf6cdf` |

Completion does not approve or execute I-0007-001 and does not publish a
component contract.

### Proposed commit trailers

```text
Change-Kind: maintenance
Spec: R-0007-346@c13709, R-0006-021@03d83e, R-0006-025@f80822
```
