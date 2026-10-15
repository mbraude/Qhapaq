# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-10. Reconciled the SPEC.md and common coding-conventions
  snapshots after commit `4e24e1b0e293691eb731bbc8429671aaf20cbb43`. SPEC.md
  now prefers rebase integration to preserve independently validated commits
  and prohibits automatic source-branch rewriting when opening pull requests.
  The common conventions require preserving every included commit's
  traceability, describe rebase preservation, and retain complete `Spec:`
  coverage if squash is explicitly selected. Entry Points terminology in the
  conventions remains consistent with D-0008-009.
- Impact review: these edits change repository integration and commit
  traceability guidance, not SPEC-0008 requirements, profile semantics,
  conformance claims, or migration requirements. I-0008-001 and I-0008-005
  remain valid with unchanged scope, requirements, dependencies, and manifests;
  no new item or dependency is needed. D-0008-009's approved Entry Points
  wording is unchanged; its recorded conventions snapshot is retained as
  historical approval evidence and is not extended to approve the separate
  integration-policy change. No code/test references or SPEC-0008 requirement
  fingerprints are affected. The R-0000-045 amendment is separately tracked
  by the SPEC-0000 plan.
- Source baseline: both changed inputs are committed at
  `4e24e1b0e293691eb731bbc8429671aaf20cbb43`. Their exact current SHA-256
  values are `c68a0e3c08b3d6c1baa7b5753cf4d3630f94fe5f7936bfede002e2e9f662c908`
  for `SPEC.md` and
  `49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834` for
  `docs/development/coding-conventions.md`. The former uncommitted snapshots
  are recoverable: the recorded SPEC.md hash matches the CRLF form of its
  recorded baseline, and the recorded conventions hash matches the CRLF form
  of the previously committed conventions file. The remaining delta is
  reviewed against those exact texts.
- Readiness remains not assessed; no implementation milestone gains execution
  eligibility or plan approval. The separate SPEC-0007 plan also has stale
  snapshots for SPEC-0008 and the coding conventions and needs its own bounded
  synchronization. SPEC-0000's two shared-source hashes match the current
  bytes. Reconciliation is complete for this SPEC-0008 source drift; no
  duplicate R-0000-045 decision work is created here.
- Validation: all 12 recorded source hashes match current bytes; all 22 work
  items have unique identities and exactly one plan membership, with resolved
  requirements and dependencies and no dependency cycle. All 28 relative
  Markdown links resolve, and `git diff --check` passes (with Git's existing
  CRLF-to-LF normalization warning). The specification trace check classified
  this work-plan-only change as `maintenance` and passed; no normative
  requirement block or code/test reference changed. Proposed trailer:
  `Change-Kind: maintenance`; no `Spec:` trailer applies.
- No readiness was reassessed and no approval was inferred. Human review of
  this reconciled plan snapshot remains required.
