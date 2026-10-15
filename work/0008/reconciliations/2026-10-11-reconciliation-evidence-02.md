# Reconciliation evidence

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-11. Reconciled the impact of D-0007-012's SPEC-0006 amendment.
  Updated the source snapshots for SPEC-0006 and the .NET conventions to the
  current working-copy bytes; their committed baseline revisions are retained.
- D-0008-009's approved Entry Points terminology is unaffected by the separate
  `Qhapaq.Portable.Validation` shared support assembly. Its original exact
  approval snapshot remains historical; only its post-snapshot requirement
  fingerprint references were refreshed. D-0008-010 had left this physical
  reuse boundary to D-0007-012, so its workspace ownership decision remains
  unchanged. No SPEC-0008 item, dependency, status, or readiness gate changed.
- SPEC-0006 current SHA-256 is
  `052fad91fa6781e84fe6d3c93491c067f7e35dd0c4e807d2ca472e1fffc08e6e`;
  .NET conventions current SHA-256 is
  `e3f7da320fba86a5ec2217607bbb35175fb905bfc91ee5e005a87a0d5d009d9f`.
- Validation: all 17 recorded source hashes match exact current bytes and
  their recorded baseline revisions resolve. The cross-plan graph contains 75
  concrete decision/implementation items and 208 edges, with no duplicates,
  missing or cancelled prerequisites, or cycles; the two template placeholders
  are excluded. Changed Markdown links resolve and `git diff --check` reports
  no whitespace errors. The whole working-tree specification trace check
  passes with warnings; its `requirement` classification and references are
  recorded in the D-0007-012 review evidence.
- No approval is carried onto D-0007-012's new requirement snapshot, and no
  implementation, release, or conformance artifact is authorized by this
  source reconciliation.
