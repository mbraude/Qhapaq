---
spec: SPEC-0008
process_version: 1
sources:
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 71bf914cd8edf48b6af94544c342c4ad2c906929
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
  - path: tools/README.md
    revision: e20a65c7b1652c62408f7505119e644d7a4383aa
    content_sha256: fe502e9664f68d7f6e3eb362a952c217c77b4801e80cab7752f8b09daa91222f
---

# D-0008-016 Trace-checker Architecture Reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md) | [Decision](../decisions/D-0008-016-trace-checker-architecture.md)

- Date: 2026-10-15. The decision adds proposed ADR-0006 selecting a Python
  shared rules engine, a native Roslyn C# extractor, a standalone local
  `python tools/trace-checker/check.py` validation command, and required CI
  integration owned by I-0008-009. The current SPEC-0008 requirements already
  define the portable checker behavior; no normative requirement changed.
- Impact review: D-0008-008, D-0008-011, D-0008-014, and I-0008-001 remain
  current and complete. I-0008-007 retains its dependency on D-0008-016 and
  remains blocked until this proposal is explicitly approved and its exact
  implementation scope has current approved readiness. I-0008-009 remains the
  owner of root adapters, impact selection, and CI integration; its existing
  scope and prerequisites are unchanged. No source fingerprints, plan
  dependencies, phase membership, or existing plan approvals changed.
- Readiness and approval impact: this decision is ready for human review, not
  approved. No implementation readiness or plan approval is created or
  renewed. After approval, reassess implementation readiness before creating
  or approving executable slices. Language support remains unregistered until
  a matching extractor and policy are delivered and reviewed.
- Reconciliation is complete for this decision's source and downstream impact.
  The plan remains current; no plan scope, item, phase, or dependency edit is
  required. The next gate is explicit review and approval of D-0008-016.
- Proposed ADR output: `docs/architecture/decisions/0006-select-deterministic-trace-checker-architecture.md`
  (working-copy SHA-256
  `f06b63559f43bf1e3a378a1ccae2bbf645f97355634f3d084962a9107f842d6a`, also
  recorded in the decision's review snapshot).
