# SPEC-0008 source and cross-plan reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Reconciled the SPEC-0008, SPEC-0005, SPEC-0006,
  common-conventions, and workflow source records against their exact current
  committed bytes. Added the specialized .NET and schema convention guides as
  authoritative inputs for the affected SPEC-0007 work.
- SPEC-0008's finalized R-0008-019 retains the previously recorded Roslyn
  generator workspace ownership; D-0007-012 and I-0007-008 already cover that
  boundary. R-0008-020 through R-0008-022 define workspace capabilities,
  fail-closed root impact selection, and content-addressed evidence/release
  manifests, which apply to I-0007-030 and I-0007-031. R-0008-023 through
  R-0008-026 define publication and public claim lifecycle gates relevant to
  I-0007-032. These milestones now record the applicable requirements and
  depend on D-0008-011, D-0008-013, and I-0008-003 where their outputs or
  publication rules are required.
- SPEC-0006's accepted top-layer terminology is now Entry Points. Existing
  SPEC-0007 items use the current identities; no further item change was
  needed. The common coding policy transferred .NET-specific conventions to
  `docs/development/conventions/dotnet.md`; D-0007-008's enforcement
  expectation remains valid, and I-0007-001 still requires its implementation.
  D-0007-008 retains a historical link to the former policy location; repairing
  that link is deferred because it would alter an already approved completed
  item's material snapshot. D-0007-013's output ownership remains unresolved
  and must be decided before its policy artifact is authored.
- I-0008-003 now records its SPEC-0007 prerequisites: D-0007-015 for the
  portable vector envelope, I-0007-002 for shared vector tooling, and
  I-0007-005 for validation foundation artifacts. These are open milestones or
  an open decision, so their required outputs are not yet available. No
  SPEC-0007 decision is resolved and no schema, vector, report, profile, or
  claim is published by this reconciliation.
- No SPEC-0007 implementation output or readiness approval is inferred.
  Readiness and concrete slice planning remain required for affected
  milestones. No cycle was introduced: the SPEC-0008 artifact milestone
  consumes SPEC-0007 prerequisites, while the affected SPEC-0007 CI, release,
  and website milestones consume SPEC-0008 publication/orchestration outputs.
- Source and structural validation: all 16 recorded authoritative source hashes
  match current bytes; all 73 SPEC-0007/SPEC-0008 work-item IDs are unique; all
  dependency references resolve and the cross-plan graph has no cycle. The
  newly linked requirement IDs R-0005-035 and R-0008-020 through R-0008-026
  exist. `git diff --check` passes; Git reports only its existing CRLF-to-LF
  normalization warnings. Specification trace check: PASS. All changed files
  are planning/documentation artifacts classified as `maintenance`; no product
  requirements, code, tests, or published artifacts changed, and no `Spec:`
  trailer applies. No build or test command applies to these planning-only
  updates.
- Exact changed output snapshots:

  | Path | SHA-256 |
  | --- | --- |
  | `work/0007/implementation/I-0007-030-shared-ci-checks.md` | `3752e63239e6086b22ff31477a6c9f2c4600fa7b872c8d19dfe20d5e1ba2f4e5` |
  | `work/0007/implementation/I-0007-031-distribution-verification.md` | `c9dd33b093fe0936724f3febfbbf1c6db5d00c3c286f309d7ca1cfacac388c4f` |
  | `work/0007/implementation/I-0007-032-website-release-gates.md` | `7d1e462ebab558e4e2be501fe15efeee4d77b87b92a7a83d9d04461cf42c295f` |
  | `work/0008/implementation/I-0008-003-conformance-artifacts.md` | `739272db2384f773ffc28b98385743c8eea603a499634ce12ca4ff44614daf19` |
