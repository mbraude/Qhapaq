# D-0007-012 generator/runtime reuse reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. SPEC-0006 baseline revision remains
  `8c63f2df1b8950fc0e283810e21e1d59db81f867`; its reviewed working-copy source
  has SHA-256
  `052fad91fa6781e84fe6d3c93491c067f7e35dd0c4e807d2ca472e1fffc08e6e`.
  The .NET conventions baseline remains
  `8f0082a220dcb36f848c5e9db05104787ee3b280`, and its reviewed working-copy
  source has SHA-256
  `e3f7da320fba86a5ec2217607bbb35175fb905bfc91ee5e005a87a0d5d009d9f`.
- The user selected one narrowly scoped shared algorithm library assembly,
  referenced by Business at runtime and consumed by the Roslyn generator only
  as build-time tooling. Reviewed low-level dependencies are permitted when
  deterministic and offline. The shared assembly may enter runtime dependency
  closure through Business; generator-only dependencies must not add runtime
  assets. SPEC-0006 R-0006-041 records the boundary. R-0006-021 and
  R-0006-024 also record the assembly distribution and project placement.
- D-0007-012, I-0007-001, I-0007-007, and I-0007-008 now reference all three
  affected requirements. The implementation milestones remain open. Other
  R-0006-039 consumers retain Business as logical semantic owner; no unrelated
  milestone is reopened.
- Adding the shared assembly amended R-0006-021 and R-0006-024 and added
  R-0006-041. At that snapshot, the cited fingerprints were `d969c8` for
  R-0006-021, `c4e735` for R-0006-024, and `2c2d4a` for R-0006-041.
  Historical references in D-0007-008 and D-0008-009 were refreshed without
  changing their approved material outcomes or carrying approval onto the new
  source snapshot.
- The D-0007-011 and D-0008-010 approvals remain scoped to their prior
  snapshots: their logical ownership and workspace-ownership decisions are
  unchanged, and both explicitly left the physical shared-library boundary to
  D-0007-012. No prior approval is carried over to this decision.
- SPEC-0008 source snapshots for SPEC-0006 and the .NET conventions were also
  refreshed after impact review. D-0008-009's Entry Points terminology remains
  unaffected; no SPEC-0008 item, dependency, status, or readiness gate changed.
- No item identities, dependencies, phase membership, or normative gates
  change. D-0007-011 and D-0008-010 remain complete. No readiness, production
  implementation, package, schema, vector, or contract publication is inferred.
- Source and workflow structure checks: all 16 recorded SPEC-0007 source hashes
  match exact current bytes and their baseline revisions resolve; the combined
  work-item graph has 75 unique IDs and 208 resolved dependency edges with no
  cycle or cancelled prerequisite. No dependency edge, phase membership, or
  readiness record changed.
- Requirement structure and fingerprints: SPEC-0006 has 41 unique requirement
  IDs. R-0006-021 and R-0006-024 were amended, and R-0006-041 is the next
  unused identifier. Their current fingerprints are recorded above.
- Source/workflow checks pass: all 16 SPEC-0007 source hashes match exact
  current bytes and their recorded baseline revisions resolve. The combined
  plan graph has 75 concrete items and 208 dependency edges, with no duplicate
  IDs, missing or cancelled prerequisites, or cycles. Local links in all
  changed Markdown files resolve; `git diff --check` reports no whitespace
  errors.
- Specification trace check: PASS with warnings. It classifies the mixed
  requirement addition and requirement amendments as `requirement`, verifies
  current fingerprints for R-0006-021, R-0006-024, and R-0006-041, and finds
  no stale references, errors, code/test changes, or waivers. Warnings cover
  the mixed change kinds, the intentionally .NET-specific project/assembly/
  package details, and future architecture/package-consumer tests planned but
  not yet delivered.
- No build or unit tests apply to this specification, architecture, diagram,
  conventions, and work-plan change.
- D-0007-012 has its exact ready-for-review snapshot recorded in its validation
  section. No approval, readiness assessment, implementation authority, or
  publication is inferred.
