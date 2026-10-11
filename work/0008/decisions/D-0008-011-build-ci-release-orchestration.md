---
id: D-0008-011
kind: decision
title: Define build, CI, and release orchestration
status: complete
spec: SPEC-0008
requirements: [R-0005-030, R-0005-032, R-0005-033, R-0005-034, R-0008-017, R-0008-019, R-0008-020, R-0008-021, R-0008-022]
depends_on: [D-0008-001, D-0008-002, D-0008-004, D-0008-007, D-0008-008, D-0008-010]
artifacts:
  - specs/0005-build-release-and-website-delivery.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
---

# D-0008-011: Define Build, CI, and Release Orchestration

## Objective

Define artifact-local commands, root orchestration, CI impact selection,
conformance-report handling, and consistent multi-artifact releases.

## Scope and exclusions

SPEC-0005 release, security, provenance, and recovery obligations remain in
force. This item does not select unapproved language, website, or extension
toolchains.

## Questions to resolve

Define required workspace entry points, root dispatch, shared-contract impact
fan-out, trace-checker invocation, path filtering, evidence retention, report
transport, and release assembly across independent toolchains.

## Acceptance criteria

- [x] Each workspace contract and root orchestration boundary is explicit.
- [x] Shared contract changes trigger every affected implementation.
- [x] Filtering cannot bypass required conformance or SPEC-0005 gates.
- [x] Required validation passes and the exact input/output snapshot is recorded for review.

## Resolution

Accepted for specification review:

- [SPEC-0008 R-0008-020](../../../specs/0008-multi-language-conformance-and-repository-organization.md#9-validation-ci-and-release-orchestration)
  defines a closed workspace-capability vocabulary implemented by native
  commands behind stable root adapters. Inapplicable capabilities are declared
  explicitly, and root automation does not reimplement workspace toolchains.
- [SPEC-0008 R-0008-021](../../../specs/0008-multi-language-conformance-and-repository-organization.md#9-validation-ci-and-release-orchestration)
  makes a root-owned declarative impact graph authoritative for transitive
  selection. Shared changes fan out to every affected consumer; uncertainty
  selects the full required set, and filtering cannot suppress traceability,
  conformance, or SPEC-0005 gates.
- [SPEC-0008 R-0008-022](../../../specs/0008-multi-language-conformance-and-repository-organization.md#9-validation-ci-and-release-orchestration)
  requires immutable content-addressed workspace reports and evidence,
  digest-only root aggregation, and an exact root release manifest for the
  independently versioned public artifacts promoted together.
- [SPEC-0005 R-0005-034](../../../specs/0005-build-release-and-website-delivery.md#6-build-and-version-model)
  applies the same manifest and build-once boundary to delivery, publication,
  and authorized retries without private-output merging or accidental runtime
  dependencies.

Concrete command syntax, impact-map format, workflow layout, report schemas,
retention and claim-publication procedures, and toolchain selection remain
excluded for later specification or implementation work.

## Validation and review

Validated 2026-10-10:

- Confirmed 738 unique normative requirement IDs, 71 unique work-item IDs,
  resolvable authoritative requirement and dependency references, and an
  acyclic cross-plan dependency graph.
- Confirmed every recorded SPEC-0008 source hash matches the exact current
  bytes, every relative link in changed Markdown resolves, and `git diff
  --check` passes. Git reported only the repository's existing line-ending
  normalization warnings.
- Specification trace review ran without a semantic-review skip and returned
  `PASS` with no errors, warnings, or waivers. It classified the change as
  `requirement`, derived `R-0005-034@8b655a`, `R-0008-020@7ebd4b`,
  `R-0008-021@d6279f`, and `R-0008-022@e2d28a`, and confirmed that no existing
  requirement fingerprint or code/test reference became stale.
- No build or unit tests were run because this decision changes only
  specification and planning documentation and explicitly defers
  implementation.

Exact ready-for-review snapshot:

| Path | Snapshot |
| --- | --- |
| `specs/0005-build-release-and-website-delivery.md` | SHA-256 `da4d393724f268b03a21fe2e36beb1d4cd01c9c73ae0c9d370e6f8a6d33aefa2` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | SHA-256 `56ae226939c2378aa1949437f9864fbd3978b35ae33f5a9480e2b3f5ccbb7bb6` |
| `work/0008/decisions/D-0008-011-build-ci-release-orchestration.md` | Material SHA-256 `605a7c2e4c4809e6616b176ad05034f53346cc23dd554270262c635ba438c6b9` |
| `work/0008/decisions/D-0008-012-migration-sequencing.md` | SHA-256 `a5114d3b4dd5c6a7c91181ce2c25a1b05659baf9e4f8105d26b048bdc5512ef8` |
| `work/0008/decisions/D-0008-013-claim-publication.md` | SHA-256 `a05885eccbd9c03c94aab5f137d29b68561558ed4070d4e760de91b305d9c3f6` |
| `work/0008/implementation/I-0008-003-conformance-artifacts.md` | SHA-256 `54225833bbc43220d1363e4818d400a92cf846138e4b7b4da3a111c50de78e87` |
| `work/0008/implementation/I-0008-005-dependent-surface-updates.md` | SHA-256 `e03b870a6200a70563c2ebd50dd673f009ad0daa0b91b9360ba8a88ab242adf0` |
| `work/0008/implementation/I-0008-006-future-workspaces.md` | SHA-256 `9a5c58e58ea71c3a0a46fbafbf79367315e6a2d96fc362a9ed209808e9055f1d` |
| `work/0008/implementation/I-0008-007-trace-checker.md` | SHA-256 `dd0b4bb92f39a6c2b957747c68a92f47a21364bdd8fd12b7f0894c9a99fd66e4` |
| `work/0008/plan.md` | SHA-256 `f3a025b40b16e39385cad8c5c71863886239e42b69d2587e2d6f243fb66d1736` |

Approved explicitly in this session on 2026-10-10 for the exact snapshot
above. The approved scope is workspace capability and root-adapter boundaries,
root-owned transitive fail-closed impact selection, immutable digest-bound
conformance-report transport, and coordinated release assembly through one
exact root manifest. Concrete commands, impact-map and report formats,
workflow layout, retention and claim-publication procedures, toolchain
selection, implementation, release assembly, pushing, and component contract
publication remain excluded.
