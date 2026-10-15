---
spec: SPEC-0008
process_version: 1
sources:
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: bf53966bc7a98a62c2c1e0692434de6ee16c1d7d
    content_sha256: 51566da6fc6521022146426661004112ee133e3600656a68a59c71e4f040c779
  - path: docs/architecture/decisions/0003-enforce-specification-traceability.md
    revision: 77cbd9e62a3a5c512f6d4a86fb6a024220a58f3a
    content_sha256: da233fb4acea9077ff49822111698c3d2484b67b69bca0f9b018eafe383d6411
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 07d7b41d910f9dc7a65fea1cb05fb4c62bf6e7cb
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/development/coding-conventions.md
    revision: a3242861598a02c89ffabfb047130d4dd4290127
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/development/conventions/dotnet.md
    revision: c1580148ae7d6230bfef6441d2e419fd71974470
    content_sha256: d590f92c5e151ae4eb02540d48a7e029863346715204c18ebe3afdc7394d7336
  - path: .agents/scripts/README.md
    revision: 33bbc94fe7afb6075e4779360c00eff2a7afc493
    content_sha256: f86cefd71054d4ff008490082726d9dead644dc5eb01c860ccd31c099dbf4a8f
  - path: .gitignore
    revision: 3235ba5b6bfc1ccdd05c97407a84bd7d7dfd9d97
    content_sha256: 0ea2ede54128044f313ef1394b9a8fa9f9d07f88ba7afffb433a8240829b88b8
  - path: tools/README.md
    revision: e20a65c7b1652c62408f7505119e644d7a4383aa
    content_sha256: fe502e9664f68d7f6e3eb362a952c217c77b4801e80cab7752f8b09daa91222f
  - path: work/0008/decisions/D-0008-008-language-native-traceability.md
    revision: 77cbd9e62a3a5c512f6d4a86fb6a024220a58f3a
    content_sha256: a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5
    material_sha256: c8ae60bf1bdbb10277b47160a7a645cf1bbae969352a032942ec05dc6b910b26
  - path: work/0008/decisions/D-0008-011-build-ci-release-orchestration.md
    revision: 3141a4b42153f45dbab9b3cdcbb664c8ba568f50
    content_sha256: 85eb2f440d89f38a77abe64ad4c76cdc926f34d6586e0b445920c57ea3643dc4
    material_sha256: 605a7c2e4c4809e6616b176ad05034f53346cc23dd554270262c635ba438c6b9
  - path: work/0008/decisions/D-0008-014-policy-checker-delivery-boundary.md
    revision: ad9c5b4800f4360df50cbcd6ae59131e1cf36392
    content_sha256: 434ba2c039eada0798d92776b1e7bc51e50c6995d0fed7292974e9e651e23b44
    material_sha256: b5acf1091308475010e929864fe7e063c30f95526a4b52868d4f2bba988e1f82
  - path: work/0008/implementation/I-0008-001-engineering-policy-separation.md
    revision: e797e847315de55b8d51f938c8ebdcbd4526505a
    content_sha256: e6e45f8fd659e0f10dfd137df74015269631c899d4d59733b8934e42d513ac48
    material_sha256: cd5630e41a99115709bb1a90d6048d4d2fbb8a285259199d92e272c175537a62
  - path: work/0008/implementation/I-0008-007-trace-checker.md
    revision: bc64ea0128052fce377772dce87ca0d961a56c2b
    content_sha256: 156d94e8f03fef2dfd87f2b52a90d8d2de1919aa36a86d7bf7e25095d74c40b3
    material_sha256: a15c221e6e02d1cad2d50b76251384d8f21242fd46b45d4d470a2a8a4fa4967d
  - path: work/0008/implementation/I-0008-009-migration-validation-orchestration.md
    revision: 9396b5567d753f80057164527185d6faa37f0c8e
    content_sha256: a1675cc1b398765f1d2809a76eee2dcec6232c84a925db213af5b933008402fe
    material_sha256: d5ce8f8a6bee4b09f13f8ff336009488acb4d9a4c00cd407fd73ebb8e7b365b1
---

# D-0008-016 Trace-checker Architecture Revision Reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md) | [Decision](../decisions/D-0008-016-trace-checker-architecture.md)

- Date: 2026-10-14. The reviewer requested that the proposed .NET extractor
  workspace use the established `dotnet` name, that tool workspaces use
  `src/` and `tests/`, and that the shared Python workflow helper remain under
  `.agents/scripts/`. The user selected keeping the helper there while placing
  the independently maintained Python engine in a sibling tool workspace.
- Revised proposal: the Python rules engine and native .NET/Roslyn extractor
  are separate workspaces beneath `src/tools/trace-checker/`, each with
  `src/` and `tests/`. The generic helper under `.agents/scripts/` builds and
  invokes the native extractor matching the language being checked, validates
  its versioned JSON command-line contract, and sends normalized facts to the
  shared Python engine. Workspace build output uses ignored `bin/` (and .NET
  intermediate output uses ignored `obj/`). The shared Python rules engine
  remains the sole owner of portable semantics, as required by R-0008-017.
- Impact review: the requirements and upstream decisions remain unchanged.
  I-0008-007 still depends on approval of D-0008-016 and current approved
  implementation readiness. I-0008-009 retains root-adapter, impact-selection,
  and required-CI ownership. No language support is registered and no
  implementation work is authorized.
- Readiness and approval impact: each material proposal revision supersedes
  the previous review snapshot. D-0008-016 remains `in-progress` while the
  latest clarification is validated. No previous readiness or approval is
  carried forward.
- Plan impact: no plan scope, phase, dependency, or readiness scope changed.
  The plan remains current; this reconciliation records only the revised
  architecture proposal and its review gate.
- Validation for the preceding revision: `python
  .agents/scripts/trace_facts.py` returned `PASS - Change-Kind: maintenance; no
  Spec trailer`; all changed files were documentation and work evidence, so
  semantic code review and build/tests were not applicable. The plan
  reconciliation check passed, source verification reported all recorded
  inputs current, and `git diff --check` passed with only the recorded CRLF
  normalization warning for the work item. Latest-revision validation is
  recorded in D-0008-016.
- Initial proposal snapshot is retained in
  [the prior reconciliation record](2026-10-15-d-0008-016-trace-checker-architecture.md).
- Preceding-revision ADR output:
  `docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md`,
  SHA-256 `bbb9ff39c52f64719dbf6a4a3150055e6388f1c1a72203c2da84887983c59712`.
  The complete input snapshots are recorded in this file's `sources` list.
- Review base: `bc64ea0128052fce377772dce87ca0d961a56c2b` on branch `master`.
- Latest clarification validation: `python .agents/scripts/trace_facts.py`
  passed with `Change-Kind: maintenance` and no `Spec:` trailer;
  `python .agents/scripts/plan_reconciliations.py check work/0008/plan.md`
  passed; `work_hashes.py verify` reported the plan and reconciliation sources
  current; and `git diff --check` passed with only the work-item line-ending
  normalization warning. The latest change remains documentation and workflow
  evidence only; no build or unit tests apply.
- Latest ADR output:
  `docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md`,
  SHA-256 `759dc91c963cfdba47901afdcd0113d5f42e259c0533c63d9d24eb649da184a0`.
- Latest review target is the clarified proposal described above. D-0008-016
  remains in progress until this final review snapshot is recorded.
