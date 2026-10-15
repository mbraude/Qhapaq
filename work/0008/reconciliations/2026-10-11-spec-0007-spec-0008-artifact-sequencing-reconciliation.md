# SPEC-0007/SPEC-0008 artifact sequencing reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Baseline: clean worktree at
  `3ef71768659562d7e82951493b0b6b3671405d49`.
- The user selected a sequencing boundary in which relevant SPEC-0008
  conformance decisions and concrete implementation planning precede SPEC-0007
  Phase 1 artifact production, while SPEC-0008 artifact delivery follows its
  SPEC-0007 foundation outputs. This does not require full SPEC-0008 delivery
  before SPEC-0007 can resume.
- Added [I-0008-012](implementation/I-0008-012-conformance-artifact-planning.md)
  to plan exact, reviewable delivery slices for I-0008-003 before production
  starts. It is ordered before SPEC-0008 delivery work and depends on the
  relevant conformance/publication decisions plus SPEC-0007's portable
  envelope and test-artifact decisions.
- I-0008-003 now depends on I-0008-012 as well as D-0007-015, I-0007-002, and
  I-0007-005. Therefore conformance artifact delivery follows both completed
  planning and the actual SPEC-0007 shared-tooling and validation-foundation
  outputs. The later SPEC-0007 CI, distribution, and website/release
  dependencies on I-0008-003 remain unchanged.
- No requirement, source specification, or existing item scope was changed.
  The new planning gate and affected delivery items remain open; no schemas,
  vectors, tooling, reports, profiles, or claims were produced or approved.
  Relevant decisions and planning can be completed before Phase 1 artifacts
  begin, with no dependency cycle.
- No source snapshot was advanced: this reconciliation changes only work-plan
  and work-item records, not their authoritative specification or policy
  inputs. Validation of source hashes, item ownership and references,
  dependency acyclicity, changed-file links, and whitespace passes: all 12
  recorded SPEC-0008 source hashes match current bytes; 77 work-item IDs are
  unique and all dependencies resolve; the combined graph has no cycles; and
  all checked local links resolve. `git diff --check` passes with only the
  repository's existing CRLF-to-LF warnings. I-0008-012 appears once in this
  plan.
- Specification trace review: PASS. All nine changed files are planning
  records classified as `Other`; the inferred change kind is `maintenance`.
  No specification blocks, product code, tests, inline references, or waivers
  changed, so no `Spec:` trailer applies and behavioral reverse-impact review
  is not applicable.
