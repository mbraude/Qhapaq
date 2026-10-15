# D-0007-009 ownership reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. SPEC-0006 baseline:
  `637015dc481f2d1e5b764b0deaad38828f2cc35e`. Its source record hashes the
  reviewed working-copy refinement, not the committed baseline text.
- R-0006-035 through R-0006-038 add the selected seven-family ownership map,
  adjacent-port/public projection rules, representative retrieval/parsing/
  generator flows, and their enforcing-test obligations. R-0006-001 through
  R-0006-034 and all portable SPEC-0007 semantics are unchanged.
- D-0007-009 is the only decision being resolved. I-0007-001 records architecture
  enforcement coverage; I-0007-008, I-0007-011, and I-0007-012 record the
  corresponding model and consumer/slice-test constraints. Their milestone
  status, dependencies, and unapproved executable manifests remain unchanged.
- D-0007-010/011/012 remain unresolved for type relationships, shared portable
  helpers, and tooling/runtime dependencies. D-0007-009 must receive exact
  human approval before its dependents become dependency-ready. No assembly,
  package, class catalogue, schema, vector, or implementation is created.
- The related SPEC-0008 plan records the SPEC-0006 source impact without
  changing its identity-migration or engineering-policy scope. Existing
  engineering-policy approval is not an approval of these new ownership
  requirements. No new readiness approval is inferred; concrete delivery
  still requires current scoped readiness and approved slice planning.
- This decision's source-impact reconciliation is complete for SPEC-0007.
  Its Phase 1 dependency on I-0008-012 is unchanged; no new cross-plan edge
  or deadlock is introduced. The saved Mermaid export remains a historical
  snapshot and is not regenerated as part of this decision.
- Validation: 74 unique owned items and 199 prerequisite edges resolve with
  no cycle or cancelled prerequisite; all 16 SPEC-0007 source hashes match
  exact bytes. SPEC-0006 has 38 unique identifiers with all 34 original
  fingerprints unchanged. Changed Markdown file targets resolve and
  `git diff --check` passes. Specification trace check passes with the expected
  implementation-specific naming warning; no code/test reference changed.
  No build or unit tests apply to this specification/planning-only decision.
