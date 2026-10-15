# SPEC-0007/SPEC-0008 artifact sequencing reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Baseline: clean worktree at
  `3ef71768659562d7e82951493b0b6b3671405d49`.
- The user selected a sequencing boundary in which relevant SPEC-0008
  conformance decisions and concrete implementation planning precede SPEC-0007
  Phase 1 artifact production, while SPEC-0008 artifact delivery follows its
  SPEC-0007 foundation outputs. This does not require full SPEC-0008 delivery
  before SPEC-0007 can resume.
- Added [I-0008-012](../0008/implementation/I-0008-012-conformance-artifact-planning.md)
  as the tracked SPEC-0008 planning gate. All five Phase 1 artifact families
  (I-0007-002 through I-0007-006) now depend on it. The gate depends on the
  relevant SPEC-0008 conformance/publication decisions and the SPEC-0007
  envelope and test-artifact decisions; it creates no schemas, vectors,
  tooling, or reports.
- I-0008-003 also depends on I-0008-012, and retains its dependencies on
  D-0007-015, I-0007-002, and I-0007-005. It therefore cannot deliver
  SPEC-0008 artifacts until planning is complete and the actual SPEC-0007
  shared-tooling and validation-foundation outputs exist. Existing later
  SPEC-0007 CI, distribution, and website/release dependencies on I-0008-003
  remain unchanged.
- No requirement, source specification, or existing item scope was changed.
  The affected items remain open; the new gate and prerequisite work still
  require their own readiness, planning, and exact-snapshot review. SPEC-0007
  decisions and non-artifact foundations can continue, but Phase 1 artifact
  production is not yet eligible. SPEC-0008 delivery remains downstream of
  SPEC-0007 foundation output.
- No source snapshot was advanced: this reconciliation changes only work-plan
  and work-item records, not their authoritative specification or policy
  inputs. Validation of source hashes, item ownership and references,
  dependency acyclicity, changed-file links, and whitespace passes: all 16
  recorded SPEC-0007 source hashes match current bytes; 77 work-item IDs are
  unique and all dependencies resolve; the combined graph has no cycles; and
  all checked local links resolve. `git diff --check` passes with only the
  repository's existing CRLF-to-LF warnings. The new SPEC-0008 item appears
  once in its owning plan.
- Specification trace review: PASS. All nine changed files are planning
  records classified as `Other`; the inferred change kind is `maintenance`.
  No specification blocks, product code, tests, inline references, or waivers
  changed, so no `Spec:` trailer applies and behavioral reverse-impact review
  is not applicable.
