---
spec: SPEC-0007
process_version: 1
sources:
  - path: SPEC.md
    revision: 7178f84c93d8393c30a5a5cf57f3c923d36274fc
    content_sha256: fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e
  - path: specs/0008-multi-language-conformance-and-repository-organization.md
    revision: 7178f84c93d8393c30a5a5cf57f3c923d36274fc
    content_sha256: 26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926
  - path: specs/0005-build-release-and-website-delivery.md
    revision: ffbae7cb66e4773e57a646822bb0b03b614ca200
    content_sha256: 8259be3d7e256d77ab18e96c35906ce64c01d25eb7a22f45a911c0727d1a1679
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: 8fbf725e0fda9697c3eff44435481d7755141272
    content_sha256: 30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c
  - path: specs/0002-operation-catalogs-and-host-configuration.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca
  - path: specs/0004-ai-assisted-connections.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: 39625b975496c96ae55c21785fd632f75d10096349acc82a4d277fc93c698e57
  - path: specs/0006-dotnet-layered-architecture.md
    revision: ff91861578d0d4368836d05d1039bbd93fca4efa
    content_sha256: 399e0083473b9adb30375c6572e53c1c04249606e46f7aab3fd4eb8ed289232e
  - path: specs/0001-core-pipeline-model.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e
  - path: docs/architecture/decisions/0001-use-microsoft-dependency-injection.md
    revision: c9c41e16fa3fd4df2aa6c26b8341c46c06b40018
    content_sha256: 663bc361c4799b69e700c6161311d60e010b89c0f65a6065be5acf9d20358173
  - path: docs/development/coding-conventions.md
    revision: 8f0082a220dcb36f848c5e9db05104787ee3b280
    content_sha256: 436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a
  - path: docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03
  - path: docs/architecture/decisions/0005-track-specification-and-delivery-work-in-the-repository.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 439ab896a425eca94d2addc99aff88db7897213cdcd3053cf50866e63b7c9825
  - path: AGENTS.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272
  - path: schemas/README.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 9735bf13164fda904d9d926a1ef896038360c7334e8ad831cac195dfc59ab0a1
  - path: conformance/README.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 0fee06404af6fc9c5321b7b30bf990f1f28c42c777b334f7928db5d1ef806307
  - path: implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/LayerDependencyTests.cs
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 62eafc81acf00d7bf15390aa110119e0be3d6e4a7cf0988193e9bb664e40eb4a
  - path: docs/development/conventions/dotnet.md
    revision: 7178f84c93d8393c30a5a5cf57f3c923d36274fc
    content_sha256: d590f92c5e151ae4eb02540d48a7e029863346715204c18ebe3afdc7394d7336
  - path: docs/development/conventions/documentation.md
    revision: 911ede5a759d7288dc569002ab2bbb136caeb52d
    content_sha256: ee1ab8d0f2237adb5a1fd986ce5c925eb1b0d6bafa51bd5c700bfd3436e7f657
  - path: .github/instructions/dotnet.instructions.md
    revision: 7178f84c93d8393c30a5a5cf57f3c923d36274fc
    content_sha256: 97fa3163316d35c1a7ccac75293f896652f7f7b150cc4fbff83ab4d67ee9d05e
  - path: docs/development/conventions/schemas.md
    revision: 1c0b6e5b5195381e4cb985f4270d746e0f039817
    content_sha256: efdccc4b508826ba8302db9f5ab5ea909ef549678c23e28c3f81e694cb27a0f2
---

# SPEC-0007: Work Plan

## Source and workflow reconciliation

- Date: 2026-10-12. Reconciled the SPEC-0006 and workflow-guide source drift
  exposed while resolving SPEC-0008's transitive prerequisites. Exact current
  bytes are committed at the revisions recorded above.
- The SPEC-0006 common-library workspace changes were already reconciled
  through D-0008-015. The later I-0006-001 changes resolve the first Service V1
  use case by linking the existing SPEC-0007 architecture-enforcement and first
  Service/CLI slice milestones to their governing contracts. The affected
  milestones already cover those outcomes; no SPEC-0007 item, requirement
  coverage, status, dependency, phase membership, or readiness gate changes.
- The workflow-guide changes make approved material snapshots immutable and
  add derived runbooks plus one-row `work-next` orchestration. They do not
  change authoritative lifecycle evidence or eligibility rules represented by
  this plan. Existing approvals remain limited to their recorded exact
  snapshots.
- This source reconciliation does not approve an implementation plan,
  authorize execution, infer completion, renew readiness, or publish a
  contract.

## D-0008-015 common-library ownership reconciliation

- Date: 2026-10-11. The user selected a common source workspace for portable
  validation libraries, with language-specific `src/` and `tests/` trees.
  SPEC-0006 R-0006-024 and R-0006-041 and SPEC-0008 R-0008-001 through
  R-0008-003, R-0008-019, and R-0008-027 are amended; SPEC.md R-0000-019 and
  R-0000-020 now identify the common .NET paths and category.
- D-0007-012's prior approval remains historical and unchanged. Its
  post-approval note records the location supersession; algorithm ownership,
  assembly identity, permitted consumers, and distribution remain unchanged.
- I-0007-001, I-0007-007, and I-0007-008 now identify common-project
  ownership, tests, architecture checks, and the prerequisite decision
  D-0008-015. Their implementation milestones remain open and unapproved.
- Source reconciliation updates the exact working-copy hashes and records
  committed baseline `7178f84c93d8393c30a5a5cf57f3c923d36274fc` for SPEC.md,
  SPEC-0006, SPEC-0008, .NET conventions, and the applicable .NET path
  instruction. The committed blobs were verified against their prior
  snapshot hashes before advancing the baselines. No SPEC-0007 requirement or
  behavior changed.
- No implementation, common workspace, readiness approval, or package is
  created. The build-and-test skill and remaining path consumers stay assigned
  to the approved migration work after the target workspaces exist.
- Validation and exact-snapshot evidence are recorded in D-0008-015. This
  reconciliation does not approve that decision or any implementation work.

## D-0007-014 DI lifetime and state ownership reconciliation

- Date: 2026-10-12. The user selected lifecycle/ownership policy and deferred
  concrete Microsoft DI registrations to reviewed implementation slices.
  [D-0007-014](decisions/D-0007-014-di-lifetimes.md) records the decision in
  the .NET conventions. It covers immutable registry generations, per-run
  scope ownership, derived-plan cache/disposal boundaries, and protected
  credential-cache ownership, aligned with the referenced SPEC-0002, SPEC-0004,
  SPEC-0006, and SPEC-0007 requirements.
- The source snapshot now includes SPEC-0004, ADR-0001, and the documentation
  conventions used for this decision. The .NET convention source baseline
  remains `7178f84c93d8393c30a5a5cf57f3c923d36274fc`; its exact reviewed
  working-copy SHA-256 is updated above.
- I-0007-001 directly depends on D-0007-014, so its architecture-test
  expectations inherit these rules. Related implementation milestones already
  depend transitively on I-0007-001 or its descendants; no new dependency edge,
  phase membership, or scope is needed.
- No product requirement changes. No implementation, readiness approval,
  package, or publication is created. Existing approvals for earlier exact
  SPEC-0008 policy outputs remain historical; their snapshots are not revised
  or reapproved by this decision.

## Source-byte reconciliation after branch integration

- Date: 2026-10-11. Baseline: `637015dc481f2d1e5b764b0deaad38828f2cc35e`.
- Eight recorded input hashes differed solely by LF/CRLF conversion after
  integration into master. Reconstructing each alternate line-ending form
  reproduces its recorded SHA-256 exactly; no source text or requirement changed.
  Updated those hashes to current exact bytes and retained committed baseline
  revisions. The other eight source records were already current.
- No item identity, scope, status, dependency, acceptance criterion, or normative
  gate changes. Historical approvals remain evidence for their original exact
  snapshots, not newly issued approvals. No readiness or implementation authority
  is inferred. D-0007-009 still requires its ownership decision and exact review;
  Phase 1 still requires I-0008-012 before artifact production.
- This bounded reconciliation permits current-source decision selection, not
  implementation or publication.

## Workflow-source and D-0007-015 approval reconciliation

- Date: 2026-10-11. Baseline: `801b57722055b3d1dd85dc95eaad9d775fe37f74`.
  The workflow-guide source record now reflects its exact current bytes. The
  reviewed change makes work branches optional and documents the approval-only
  workflow; it does not alter SPEC-0007 semantics, item identities, dependencies,
  acceptance criteria, or implementation gates.
- D-0007-015 is complete. Its decision file records explicit approval of the
  exact decision snapshot. The earlier note that it awaited approval described
  the prior state and is superseded by that evidence. This does not approve
  readiness, artifact production, or implementation.
- D-0007-013 remains open. I-0007-002 and I-0007-005 remain open artifact
  milestones; no vector tooling, vectors, or publication evidence is inferred.
- Validation: all 16 source hashes match current bytes; all 75 work-item IDs
  and dependencies resolve without duplicates or cycles; `git diff --check`
  and the specification trace check pass (`maintenance`).

Approval recorded on 2026-10-11: the user approved this exact plan snapshot.
Full-byte SHA-256 before recording this approval evidence:
`cc68857353778a0c9bd6aa80856cf3aca684ef296f7a79a9c175bc84c7b05c11`.
This approval covers plan reconciliation only, not D-0007-013, readiness, or
implementation.

## D-0007-013 test-artifact convention reconciliation

- Date: 2026-10-11. Baseline: `801b57722055b3d1dd85dc95eaad9d775fe37f74`.
  D-0007-013 is ready-for-review with its exact snapshot recorded in the item.
  It records .NET vector loading, golden
  maintenance, and clean package-consumer conventions under R-0007-346,
  R-0007-347, R-0006-031, and R-0001-072. Its selected loader copies canonical
  `conformance/` files into test output; consumer tests use temporary packed
  public packages. Acceptance checks pass; explicit human approval is pending.
  No product requirement, portable envelope, item identity, dependency, or
  implementation gate changed.
- The D-0007-015 impact review confirms its accepted portable envelope remains
  authoritative and unchanged: D-0007-013 keeps `expected` values in canonical
  vectors and does not introduce .NET-specific portable semantics. D-0007-015
  remains complete; its recorded D-0007-013 hash identifies its historical
  reviewed input and does not require reopening the decision.
- D-0007-013 remains the required decision prerequisite for downstream
  conformance tooling and I-0008-003. I-0007-002 and I-0007-005 remain open;
  this decision produces no tooling, vectors, publication, or readiness
  evidence.

## Scope and authority

  ## Scope and authority

Migrated development work for
[SPEC-0007](../../specs/0007-portable-pipeline-definitions-and-binding.md),
its retained Section 21 requirements and two Section 23 questions, using the
[development workflow](../../docs/development/spec-driven-workflow.md).
The plan does not change product requirements, publication rules, or architecture.
This plan owns implementation sequencing; item files own operational status and
dependencies. The specification no longer contains the legacy rollout sequence
or checklists. Previously completed decisions remain in Git history, without
retrospective completion or approval tasks.

Current decision detail covers Phases 0 and 0A. Phase 1's explicit vector-envelope
decision is separated from tooling. Future delivery is recorded as milestones,
not approved executable file plans. Exact paths/namespaces/tests and remaining
capability-specific decisions must be detailed before each slice executes.

Item files own status and dependencies. Tables below own phase membership and
preferred order, not dependency edges. Broad milestones carry common dependencies
plus explicit per-capability entry gates; concrete planning must split them into
exact dependencies, not execute them as omnibus tasks.

Item lifecycle and approval evidence are recorded only in item files; this plan
does not infer completion, readiness, or approval.
Use `work-plan-show SPEC-0007` for a derived graph and `spec-next SPEC-0007`
for one eligible decision.

## D-0007-009 ownership reconciliation

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

## D-0007-011 portable helper ownership reconciliation

- Date: 2026-10-11. SPEC-0006 baseline is the committed source at
  `492206db449e564156775d1b2e30ef0f89afb808`; the source record hashes the
  reviewed working-copy change introducing R-0006-039.
- The accepted logical map assigns portable algorithm semantics and runtime
  validation findings to Business. Runtime use passes through Business and
  adjacent contracts; DAL supplies/stores metadata only; build tooling consumes
  the same semantics through an explicit reviewed boundary. Build diagnostics
  and runtime diagnostic envelopes remain distinct. No project, assembly,
  package, or production helper file is selected; D-0007-012 owns the physical
  tooling/runtime boundary.
- R-0006-039 is added to D-0007-011 and the affected architecture, validation,
  generator, registry, parsing, schema-engine, and normalization milestones.
  Their statuses and dependencies remain unchanged; existing D-0007-012
  prerequisites are preserved. No SPEC-0008 item, readiness approval,
  implementation output, schema, or vector changes.
- This bounded reconciliation reviews the new requirement against
  R-0007-348/R-0007-346 and R-0006-020, updates only work whose helper ownership
  or enforcement scope is directly affected, and does not reconcile the
  previously recorded unrelated SPEC-0008 source drift. No cross-plan edge
  changes; no cycle or cancelled prerequisite is introduced.
- Validation: all 16 SPEC-0007 plan source hashes match exact working-copy
  bytes. SPEC-0006 contains 39 unique requirement IDs; R-0006-039 is the next
  unused ID and the 38 baseline requirement fingerprints are unchanged. The
  new block fingerprint is `27b828`, with no prior inline references to update.
  All 74 existing work-item identities and 199 prerequisite edges remain
  unchanged; no cycle, cancelled prerequisite, or cross-plan edge is introduced.
  The new D-0007-012 cross-reference resolves and `git diff --check` passes,
  with only the repository's existing line-ending normalization warnings.
- Specification trace check: PASS with a warning for implementation-specific
  .NET and layer terminology in SPEC-0006. The change is classified as
  `requirement`; proposed trailers are `Change-Kind: requirement` and
  `Spec: R-0006-039@27b828`. All prior SPEC-0006 requirement fingerprints are
  unchanged, no prior reference to the new requirement exists, and no code,
  test, or waiver changed. No build or unit tests apply to this specification
  and work-planning change. The exact
  material and input/output hashes are recorded in D-0007-011 for review.
- The related SPEC-0008 plan remains outside this bounded reconciliation: it
  has no affected SPEC-0008 item, its recorded source drift predates this
  decision, and D-0008-010's completed workspace-ownership scope remains
  unchanged. Its historical reference to the prior D-0007-012 snapshot is not
  rewritten. This reconciliation is not human approval or implementation
  authority.

## Phase 0: Close required normative decisions

### Entry gates

R-0007-340 through R-0007-345 govern contract completeness and publication.
Decisions can proceed independently where their actual prerequisites permit.
This plan retains Phase 0A before expansion of remaining public APIs.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0007-001](decisions/D-0007-001-numeric-helpers.md) | Numeric helpers and reductions |
| 2 | [D-0007-002](decisions/D-0007-002-mapping-completeness.md) | Complete operator-set and all-capabilities audit |
| 3 | [D-0007-003](decisions/D-0007-003-declaration-contracts.md) | Declaration APIs, manifest and compatibility matrix |
| 4 | [D-0007-006](decisions/D-0007-006-non-executing-conclusions.md) | Stage-aware non-executing conclusions |
| 5 | [D-0007-004](decisions/D-0007-004-exact-descriptor-service.md) | First descriptor-retrieval Service/CLI contracts |
| 6 | [D-0007-005](decisions/D-0007-005-subsequent-surface-contracts.md) | Minimal subsequent Service/CLI/MCP contracts |

### Cancelled extraction

[D-0007-007](decisions/D-0007-007-inherited-decision-review.md) retains its
identity only as the cancellation record for an unnecessary retrospective
review gate. No active item depends on it and no replacement is required.

### Exit gates

R-0007-345: applicable Section 23 contracts are resolved for supported artifacts,
generation, and Service use cases. R-0007-340/343: no v1 operator-set completion
or schema/vector publication before all selected capabilities have normative
semantics and conformance requirements. Actual vectors are required before
dependent implementation; current readiness and publication evidence remain
distinct from earlier decisions in Git history.

## Phase 0A: Establish .NET organization and reuse boundaries

### Entry gates

Established SPEC-0006 architecture and representative use cases under R-0007-346;
unrelated Phase 0 decisions need not close first.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0007-008](decisions/D-0007-008-folder-namespace-conventions.md) | Feature folder and namespace conventions |
| 2 | [D-0007-009](decisions/D-0007-009-model-ownership.md) | Model ownership and visibility |
| 3 | [D-0007-010](decisions/D-0007-010-type-relationships.md) | Representative type relationships |
| 4 | [D-0007-011](decisions/D-0007-011-portable-helper-ownership.md) | Shared portable helper ownership |
| 5 | [D-0007-012](decisions/D-0007-012-generator-runtime-reuse.md) | Build-tooling/runtime reuse boundaries |
| 6 | [D-0007-013](decisions/D-0007-013-test-artifact-conventions.md) | Vector/golden/consumer test conventions |
| 7 | [D-0007-014](decisions/D-0007-014-di-lifetimes.md) | DI lifetimes and state ownership |
| 8 | [I-0007-001](implementation/I-0007-001-architecture-enforcement.md) | Applicable architecture enforcement tests |

### Exit gates

R-0007-346 requires persistent ownership/dependency maps, representative
relationships, and enforcing architecture tests. Completing only decision prose
does not complete this phase. Do not create empty production placeholders.

## Phase 1: Publish language-neutral schemas and vectors

### Entry gates

Applicable Phase 0 decisions are prerequisites for each artifact family under
R-0007-347. Before any Phase 1 artifact family starts, the SPEC-0008
conformance-artifact planning gate [I-0008-012](../0008/implementation/I-0008-012-conformance-artifact-planning.md)
must be complete. This gates artifact production on accepted conformance
decisions and a reviewed implementation plan, not on completion of SPEC-0008
delivery.
Unrelated execution/mapping artifacts do not block descriptor tooling.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [D-0007-015](decisions/D-0007-015-conformance-envelope.md) | Portable envelope and result conventions |
| 2 | [I-0007-002](implementation/I-0007-002-conformance-tooling.md) | Shared tooling and golden maintenance |
| 3 | [I-0007-005](implementation/I-0007-005-validation-foundation-artifacts.md) | Profile, JSON, pattern/format and diagnostic artifacts |
| 4 | [I-0007-003](implementation/I-0007-003-descriptor-artifacts.md) | Descriptor/manifest/digest/vocabulary/compatibility artifacts |
| 5 | [I-0007-004](implementation/I-0007-004-pipeline-mapping-artifacts.md) | Pipeline/mapping/scope/default-normalization artifacts |
| 6 | [I-0007-006](implementation/I-0007-006-execution-failure-artifacts.md) | Failure and structural execution artifacts |

### Exit gates

Every portable rule needed by each dependent milestone has versioned schema/vector
coverage and exact expected results independent of .NET. Tooling reports exercised
versions/capabilities. Preserve earlier alpha descriptor artifacts.

## Phase 1A: Implement shared portable validation foundations

### Entry gates

Phase 0A and applicable Phase 1 families support R-0007-348; unrelated artifact
families are not prerequisites.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-007](implementation/I-0007-007-portable-validation-foundations.md) | Shared offline portable algorithms and safe diagnostics |

### Exit gates

Tested generator/runtime reuse without network, operation construction, project-code
execution, layer bypass, or a parallel runtime.

## Phase 2: Implement .NET descriptor authoring and generation

### Entry gates

Relevant authoring decisions, Phase 0A, descriptor/manifest/digest/diagnostic
artifacts and their Phase 1A foundations support R-0007-349 acceptance.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-008](implementation/I-0007-008-descriptor-generation.md) | Deterministic generator and clean authoring consumer |

### Exit gates

Clean consumers author/validate/generate/register/package with supported APIs and
explicit inputs; required determinism, byte equality and minimal trimming/AOT checks.

## Phase 3: Implement registry core and native bindings

### Entry gates

Phase 2 registration/manifest contracts and Phase 1A runtime verification
support R-0007-350 acceptance.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-009](implementation/I-0007-009-registry-native-bindings.md) | Exact immutable registry and explicit native bindings |

### Exit gates

Deterministic exact resolution; invalid/ambiguous registrations unavailable before
binding. Registry core alone is not a conforming host.

## Phase 3A: Establish trusted host configuration and policy

### Entry gates

Registry and applicable foundations plus exact host contracts/vectors for each
enabled capability support R-0007-351. Host decisions may precede registry
implementation.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-010](implementation/I-0007-010-trusted-host-policy.md) | Real fail-closed trusted sources, policy and credential boundaries |

### Exit gates

Supported host constructs an immutable effective registry and tested bind-time,
invocation-time, connection, credential and independent disclosure boundaries.
SPEC-0002/0004 contract decisions must be extracted before capability implementation.

## Phase 3B: Deliver the first non-executing Service and CLI slice

### Entry gates

Reviewed R-0007-404 through R-0007-410 retrieval contracts, Phase 0A, registry,
trusted selection and descriptor-disclosure policy support R-0007-352.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-011](implementation/I-0007-011-first-service-cli-slice.md) | Exact retrieval through CLI and public Service |

### Exit gates

Real non-executing adjacent-layer use case and clean third-party consumer; no
execution, credentials, installation, profile mutation or authority grant.

## Phase 4: Implement parsing and portable validation

### Entry gates

Applicable pipeline/profile/scope/diagnostic artifacts, ownership and shared
parsing foundations support R-0007-353. Can proceed independently of Phases 2
through 3B.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-012](implementation/I-0007-012-inert-parsing.md) | Registry-independent inert structural validation |

### Exit gates

Parsing/structural/scope/diagnostic vectors pass without activation or effects.
No complete semantic validity or canonical pre-normalization digest is claimed.

## Phase 5: Implement the schema and mapping engines

### Entry gates

R-0007-354 and each subphase's actual artifact/foundation prerequisites.

### Ordered items

| Order | Subphase | Item | Outcome |
| --- | --- | --- | --- |
| 1 | 5A | [I-0007-013](implementation/I-0007-013-schema-engine.md) | Instance validation and conservative compatibility |
| 2 | 5B | [I-0007-014](implementation/I-0007-014-mapping-inference.md) | Exact language parsing and static inference |
| 3 | 5C | [I-0007-015](implementation/I-0007-015-mapping-evaluation.md) | Every operator and portable evaluation budgets |

### Exit gates

R-0007-355 through R-0007-357: exact portable acceptance/rejection, distinct
missing/null and complete instance/compatibility/mapping/failure suites.

## Phase 6: Normalize exact contracts and bind immutable plans

### Entry gates

R-0007-358: no execution during normalization or binding. Reference-host exact
metadata comes from Phase 3; alternative offline sources require explicit review.

### Ordered items

| Order | Subphase | Item | Outcome |
| --- | --- | --- | --- |
| 1 | 6A | [I-0007-016](implementation/I-0007-016-normalization-identity.md) | Contract-informed defaults and canonical identity |
| 2 | 6B | [I-0007-017](implementation/I-0007-017-binding-cache.md) | Complete immutable binding and stale-cache rejection |

### Exit gates

R-0007-359/360: canonical defaults precede identity and persistence; all validation
stages complete before returning plans and every invalidation input is honored.

## Phase 7: Implement the execution frame and runner

### Entry gates

R-0007-361: fully bound plans and real invocation policy; one non-durable run.

### Ordered items

| Order | Subphase | Item | Outcome |
| --- | --- | --- | --- |
| 1 | 7A | [I-0007-018](implementation/I-0007-018-frame-primitive-sequence.md) | Private frame and primitive/sequence execution |
| 2 | 7B | [I-0007-019](implementation/I-0007-019-transforms-final-output.md) | Transform boundaries, lifetimes and final output |
| 3 | 7C | [I-0007-020](implementation/I-0007-020-parallel-conditional.md) | Concurrent/conditional failure-safe execution |
| 4 | 7D | [I-0007-021](implementation/I-0007-021-decorators-recovery.md) | Decorator attempts and lexical recovery |
| 5 | 7E | [I-0007-022](implementation/I-0007-022-loops-collections.md) | Bounded loops and item/chunk collections |
| 6 | 7F | [I-0007-023](implementation/I-0007-023-integrated-runner.md) | Integrated limits, cancellation, failures and privacy |

### Exit gates

R-0007-362 through R-0007-367 retain execution acceptance conditions. Observe all started tasks,
preserve catchability/effects, keep frames private, and pass the complete safety/
execution suite. No rollback, partial-success or early public enablement.

## Phase 8: Add Service and authoring projections

### Entry gates

Exact contracts, the first Service slice, and use-case-specific prerequisites
support R-0007-368 and R-0007-411 through R-0007-423. Non-executing work does
not depend on the whole runner.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-024](implementation/I-0007-024-authoring-projections.md) | Incremental listing, validation, explanation, Mermaid and comparison |

### Exit gates

Each supported adapter consumes common versioned Service behavior without
duplicating domain/policy rules. Plan narrower slices with explicit dependencies:
listing after 3/3A; structural conclusions after 4; full validation/explanation
after 6B; comparison after 5A/exact sources; Mermaid after required analysis.
Capability advertisement, bounded inputs, catalog pagination, CLI/MCP mappings,
and unavailable-surface omission must remain consistent across those slices.

## Phase 9: Enable policy-gated execution

### Entry gates

Phases 0 through 8 supply the applicable prerequisites for every enabled surface.
R-0007-369 requires the complete parse-to-permission safety path, all claimed
conformance, and required verification.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-025](implementation/I-0007-025-enable-execution.md) | Separate public execution with independent policy/disclosure |

### Exit gates

No execution enablement until all applicable gates and suites pass. Document
enabled capabilities and unavailable optional surfaces; optional conformance
claims do not remove required v1 deliverables. Inline-definition and
exact-reference modes remain separate, and execution permission never implies
result-payload disclosure.

## Companion milestones and delivery boundaries

### Entry gates

R-0007-370: exact contracts and tests belong to their linked specifications.
This plan tracks integration obligations, not approvals of those specifications.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-026](implementation/I-0007-026-definition-persistence.md) | Canonical persistence and exact references |
| 2 | [I-0007-027](implementation/I-0007-027-invocation-skills.md) | Invocation-skill contracts, snapshots and mappings |
| 3 | [I-0007-028](implementation/I-0007-028-openapi-extensions.md) | OpenAPI/HTTP/extension integration |
| 4 | [I-0007-029](implementation/I-0007-029-connection-consent.md) | Trusted connection planning and local consent |
| 5 | [I-0007-030](implementation/I-0007-030-shared-ci-checks.md) | Early shared local/CI blocking gates |
| 6 | [I-0007-031](implementation/I-0007-031-distribution-verification.md) | Package/target/installation verification |
| 7 | [I-0007-032](implementation/I-0007-032-website-release-gates.md) | Website and public-release obligations |
| 8 | [I-0007-033](implementation/I-0007-033-deferred-capability-seams.md) | Preserve deferred v1 seams without expanding scope |

### Exit gates

Complete each governing prerequisite before advertising its capability. Website
work is independent of binding; build automation supports early stages; execution
uses Phase 9 even when invoked through a skill. No implicit legacy format,
durability, exactly-once or transactional rollback is introduced.

## External prerequisites

- [SPEC-0006](../../specs/0006-dotnet-layered-architecture.md) and engineering
  conventions govern organization. Its first-Service questions are deduplicated
  into D-0007-004, not a competing backlog.
- [SPEC-0001](../../specs/0001-core-pipeline-model.md) owns persistence and product
  invocation skills. Further detailed companion assessment is deferred.
- [SPEC-0002](../../specs/0002-operation-catalogs-and-host-configuration.md) and
  [SPEC-0004](../../specs/0004-ai-assisted-connections.md) own host/source/provider/
  consent contracts; these are explicit unassessed entry gates, not approved plans.
- [SPEC-0005](../../specs/0005-build-release-and-website-delivery.md),
  [SPEC-0003](../../specs/0003-product-evolution-roadmap.md), and
  [SPEC.md](../../SPEC.md) own companion delivery/release/deferred obligations.
  No owner plan exists yet. When created, link its actual prerequisite item IDs;
  do not copy or invent external identities.

## Initial extraction evidence

- Date: 2026-10-09.
- Baseline: `34fbe88fb9d4857adc6db5390cc623c210c71540`, clean worktree before
  extraction. SPEC-0007 was last changed by
  `2dba9fb01b6b2dd78c1f904a90049cdc37052f7a`.
- Source hashes record exact working-copy bytes, not normalized Git blob hashes.
  Recorded commits supply their baseline text; no authoritative input was edited.
- Scope extraction is complete for the current decisions and all Section 21
  milestone families. Full future implementation design and companion-spec
  readiness are deliberately not assessed. Source snapshots do not assert that
  those unresolved decisions have been resolved.
- Created D-0007-001 through D-0007-015 and I-0007-001 through I-0007-033.
  No cancelled, completed, approved or executed items were created.
- Section 23 question 1 maps to D-0007-003; question 2 maps to D-0007-004/005.
  R-0007-344's conclusion checkpoint is D-0007-006.
- R-0007-340's checked entries are consolidated as inherited D-0007-007 review
  evidence. Numeric closure and both remaining audit checkboxes map to
  D-0007-001/002. Closure-vector versus Phase 1 publication evidence is flagged
  there without weakening either obligation.
- Phase 0A's seven policy/architecture decisions and its eighth enforcing-test
  obligation are all retained. Conformance envelope decisions are not disguised
  as implementation tooling work.
- Existing descriptor alpha fixtures are structural only; initial digest values
  are not canonical goldens. Existing architecture tests establish layer baseline,
  not the unimplemented Phase 0A refinements. No code/test fingerprint changes.
- Specification checklist text remains unchanged because normative migration was
  not requested. R-0007-336 still governs its persistent checklist. This companion
  plan is a proposed operational extraction, not a replacement authority: do not
  independently advance conflicting checkbox states. Report differences and obtain
  explicit migration scope to replace operational tracking while preserving gates.
- No readiness record exists yet; no specification, implementation plan, contract
  version or historical completion is approved by synchronization.
- Validation: inspected all 49 new Markdown artifacts. Checked 48 unique item
  identities and ownership, required metadata/body sections, one phase membership
  per item, existing/non-retired requirement references, and acyclic dependencies
  with no missing or cancelled prerequisites. Checked 61 repository-relative
  links, 11 source byte hashes and full baseline revisions, ASCII text and
  whitespace. No readiness records or executable slices were introduced.
- Coverage review preserves all Section 21 phases and companion checklist
  families, independent descriptor tooling and inert parsing, the two Section 23
  questions, and the unresolved historical/vector evidence described above.
- Specification trace check: PASS. All additions are classified Other/planning
  documentation; current change kind is maintenance, with proposed trailer
  `Change-Kind: maintenance`. No required `Spec:` trailer, changed requirement
  fingerprints, new waivers, or product-code reverse-impact scope. Semantic review
  was not user-skipped; no changed product behavior exists to review. No findings.
- Documentation-only validation; no build or unit tests run. Synchronization
  stops for human plan review, without commit, approval, or publication.

## Checklist migration reconciliation

- Date: 2026-10-09. User explicitly requested removal of the legacy specification
  sequence and use of Git history for previously completed decisions. This
  reconciliation supersedes the initial extraction's duplicate-tracking and
  inherited-review gates; it does not approve any remaining decision or delivery.
- Baseline remains `34fbe88fb9d4857adc6db5390cc623c210c71540`. SPEC-0007's source
  hash records reviewed working-copy bytes, not committed text. Other source
  records remain unchanged.
- Section 21 now contains declarative publication, acceptance, and migration
  requirements, not phases, task checkboxes, or implementation dependency lists.
  R-0007-336/338/339 are retired operational/summary blocks; all IDs remain
  present. R-0007-337 and R-0007-340 through R-0007-370 retain the applicable
  normative obligations. Section 8 references no longer rely on legacy phases
  or completed-checkpoint status.
- Existing phase membership, preferred order, organization prerequisites,
  independent descriptor/parsing work, future milestones, and companion delivery
  coverage remain here. No new items, completed-history placeholders, production
  code, or executable slices are introduced.
- D-0007-007 is cancelled, not completed or deleted. D-0007-002 and
  I-0007-003/005/006 no longer depend on it; I-0007-004 no longer names it as an
  entry gate. D-0007-002 still requires the current completeness audit after
  D-0007-001. Publication and scoped readiness still require actual evidence.
- I-0007-025 no longer references retired R-0007-336. Existing references to the
  remaining acceptance requirements still govern the same milestone coverage.
  No code/test inline references to changed blocks require fingerprint updates.
- No readiness records or approved slices exist in this plan. Remaining numeric,
  contract, organization, and companion-spec decisions stay unresolved. Migration
  does not publish a contract or establish execution readiness.
- Validation: checked all 48 unique item identities, metadata and required
  sections, one phase membership each, 95 dependency edges, acyclic graph,
  non-retired requirement references, and absence of cancelled prerequisites.
  Resolved 77 repository-relative links and anchors across the plan, items, and
  specification. Checked 11 source records and unchanged non-specification
  hashes, ASCII work artifacts, and whitespace. The specification contains no
  task checkboxes or phase references; no stale phase anchors remain.
- Specification trace check: PASS with warnings. Scope since HEAD is one
  Specification and 49 Other/planning files, including the existing untracked
  extraction. All 384 requirement IDs are preserved; 43 blocks changed,
  including three retained retirement tombstones. Exact fingerprints were
  computed using the trace skill helper. Repository-wide reverse-impact search
  found no fingerprinted code/test references to the changed blocks, and no
  work item references a retired block. No product/test code changed.
- Semantic review ran, not skipped. Reviewed the legacy checklist against
  retained requirements and work coverage: R-0007-064/093/129 through 132/140,
  R-0007-336 through R-0007-370, and R-0007-378/383. Completed semantics remain
  in their substantive specification sections; publication, compatibility,
  exact identity, normalization, complete binding, non-durability, independent
  permission/disclosure, and execution safety obligations remain intact.
- Warning: R-0007-349/352/368 retain implementation type and assembly names
  (`Qhapaq.Abstractions`, `IOperation<TInput, TOutput>`, `Qhapaq.Service.V1`)
  from the former checklist. These remain explicitly .NET-specific acceptance
  requirements, not dependencies of the portable contract. No new implementation
  names or source-file references were added.
- Classification: amendment, because the specification's legacy operational
  tracking authority is explicitly retired. Product behavior is retained;
  associated planning maintenance is inseparable from this migration. No new
  waivers or waived findings. No build or unit tests run for this documentation-only
  change. No commit, contract publication, readiness, or delivery approval.

### Proposed commit trailers

```text
Change-Kind: amendment
Spec: R-0007-064@11dacd, R-0007-093@02bc90, R-0007-129@8f3c40, R-0007-130@33feb8, R-0007-131@2e230b, R-0007-132@b393aa, R-0007-140@dece32
Spec: R-0007-337@59e5d2, R-0007-340@461e39, R-0007-341@99d07c, R-0007-343@028495, R-0007-344@25665b, R-0007-345@040649, R-0007-346@c13709, R-0007-347@4a4d6f, R-0007-348@751226
Spec: R-0007-349@9ad651, R-0007-350@6c7d7d, R-0007-351@61802f, R-0007-352@9878cd, R-0007-353@0385b0, R-0007-354@e02caa, R-0007-355@1001ba, R-0007-356@d72b96, R-0007-357@92d8c6, R-0007-358@ed3c88, R-0007-359@d7f0b0, R-0007-360@96f212
Spec: R-0007-361@92d9bb, R-0007-362@78ddc6, R-0007-363@dca37b, R-0007-364@70d920, R-0007-365@916de2, R-0007-366@5563c5, R-0007-367@7d10ba, R-0007-368@c5f632, R-0007-369@511eb8, R-0007-370@7bc93c, R-0007-378@df03a9, R-0007-383@28fa2d
```

## D-0007-001 numeric decision reconciliation

- Date: 2026-10-09. Baseline
  `6fa79545b7bfa9d4253439dc315cda55d12b0f43` supplied the committed
  SPEC-0007 input. The source record now hashes the reviewed working-copy bytes
  containing D-0007-001's accepted numeric decisions; it does not claim those
  bytes are committed.
- R-0007-129 and new R-0007-385 through R-0007-391 select the purpose-built
  scalar helpers and reductions, reject general/configurable alternatives, and
  close their shapes, numeric behavior, typing, state, order, failure,
  accounting, and conformance expectations. Cross-cutting requirements and the
  reserved failure-code table are reconciled to that outcome.
- D-0007-001 is the only decision resolved by this reconciliation. D-0007-002
  remains the dependent all-operator completeness audit and is not eligible
  until D-0007-001 receives exact-snapshot approval and becomes complete.
  I-0007-004 remains downstream of D-0007-002 and D-0007-015; no implementation
  slice, schema, vector, readiness approval, or publication is created.
- Repository-wide reverse-impact search found no implementation, schema, or
  conformance references to the changed requirement IDs. The affected future
  artifact milestone remains governed through D-0007-002 and R-0007-343/347.
- Refreshed the historical proposed-trailer requirement fingerprints above for
  R-0007-064, R-0007-093, R-0007-129, R-0007-132, R-0007-340, and R-0007-343
  after the numeric decision changed their requirement text. They now identify
  the exact current SPEC-0007 blocks; this does not change the recorded source
  baseline or claim that the proposed trailers were committed.
- No readiness record exists. Numeric normative closure removes one known
  specification blocker but does not establish mapping-v1 readiness; D-0007-002,
  required schemas and vectors, and scoped readiness review remain outstanding.
- Validation and exact reviewed snapshots are recorded in D-0007-001. This
  reconciliation is not human approval, completion, implementation,
  publication, or permission to execute.

## D-0007-002 mapping-completeness reconciliation

- Date: 2026-10-09. Baseline
  `dd56a136e2b381b6c44cc05a2a803bf00e4d7dfb` supplied the committed
  SPEC-0007 input. The source record hashes the reviewed working-copy bytes
  containing D-0007-002's accepted resolution; it does not claim those bytes
  are committed.
- The all-operator audit found no selected or rejected capability mismatch and
  no shape, typing, state, failure, evaluation, or accounting gap in the
  specialized collection, string, regex, object-shaping, or numeric groups.
  It found that the foundational operators relied on distributed generic
  clauses without a complete result-and-conformance matrix, and that R-0007-334
  omitted the numeric, regex, and object-shaping groups from its aggregate
  inventory.
- R-0007-392 through R-0007-396 close only those core semantic and conformance
  gaps. R-0007-334 now inventories every specialized group. No operator,
  operand shape, capability selection, dependency, phase membership, schema,
  vector, implementation slice, or publication state changes.
- D-0007-002 is the only decision resolved by this reconciliation. Its
  downstream mapping-artifact milestone remains blocked on exact-snapshot
  approval of this decision and D-0007-015, then on concrete implementation
  planning. No readiness record or approval is created.
- Validation and exact reviewed snapshots are recorded in D-0007-002. This
  reconciliation is not human approval, completion, implementation,
  publication, or permission to execute.

## D-0007-003 declaration-contract reconciliation

- Date: 2026-10-09. Baseline
  `28ebb07edd36ebbc601fb21a381badb1233e42e2` supplied the committed
  SPEC-0007 input. The source record hashes the reviewed working-copy bytes
  containing D-0007-003's accepted contract decisions; it does not claim those
  bytes are committed.
- R-0007-252, R-0007-253, R-0007-257, R-0007-258, R-0007-261, R-0007-263,
  R-0007-265, R-0007-268, R-0007-291, and new R-0007-397 through R-0007-399
  close the marker, static declaration, generated registration, manifest,
  diagnostic, compatibility, generated-contract versioning, and catalog
  separation questions. The remaining Section 23 question concerns CLI and MCP
  contracts only.
- D-0007-003 is the only decision resolved by this reconciliation. D-0007-005
  now explicitly owns the downstream Service/host catalog-membership contract
  required by R-0007-399; it remains open and retains its existing dependencies.
  D-0007-009 and D-0007-012 retain model-ownership and algorithm-reuse decisions
  without becoming artificial prerequisites of D-0007-003.
- Descriptor `v1alpha1` is preserved. No schema, manifest artifact, generator,
  implementation type, conformance vector, Service surface, catalog
  configuration, publication, or implementation readiness is created.
- Validation and exact reviewed snapshots are recorded in D-0007-003. This
  reconciliation is not human approval, completion, implementation,
  publication, or permission to execute.

## D-0007-006 stage-aware conclusion reconciliation

- Date: 2026-10-09. Baseline
  `5f0a1cfcce38d35417f3627ea7e1c91f3ca7dc77` supplies the committed
  SPEC-0007 input. The source record hashes the current working-copy bytes
  containing D-0007-006's accepted decisions; it does not claim those bytes are
  committed.
- New R-0007-400 through R-0007-403 define the closed three-state conclusion
  model, stable unavailability reasons, exact early-slice matrix, normal-result
  versus structured-error boundary, adapter preservation, and negative
  conformance coverage.
- D-0007-006 is the only decision resolved by this reconciliation. D-0007-004
  now depends on it for retrieval conclusion semantics; D-0007-005 retains its
  existing dependency. I-0007-011, I-0007-012, and I-0007-024 now reference
  the exact requirements, and inert parsing now depends on D-0007-006.
- The changes do not name public APIs or commands, implement a surface, create
  schemas or vectors, publish a contract, grant execution or disclosure
  authority, or establish readiness. D-0007-004, D-0007-005, and every affected
  implementation milestone remain open.
- Validation and exact ready-for-review snapshots remain to be recorded in
  D-0007-006. This reconciliation is not human approval, completion,
  implementation, publication, or permission to execute.

## D-0007-004 exact descriptor-retrieval reconciliation

- Date: 2026-10-10. Baseline
  `07073fe16ae1b6f64feaeedb01557d6f5b9731fd` supplies the committed
  SPEC-0007 input. The source record hashes the current working-copy bytes
  containing D-0007-004's accepted contract decisions; it does not claim those
  bytes are committed. SPEC-0002 is now an explicit source because effective
  registry construction and disclosure policy govern this use case.
- New R-0007-404 through R-0007-410 define the exact Service selector and
  response, indistinguishable absent/non-disclosable result, digest
  precondition, structured errors, `qhapaq operation get` grammar and output,
  stable exit statuses, adjacent-layer/non-executing boundaries, and
  language-neutral conformance coverage.
- D-0007-004 is the only decision resolved by this reconciliation. I-0007-011
  now references the exact requirements it must implement. D-0007-005 remains
  open for subsequent CLI and MCP contracts and retains its existing
  dependencies. No item or dependency is added, removed, split, or cancelled.
- The change creates no implementation, schema, vector, registry, policy,
  descriptor publication, execution or payload-disclosure authority, or
  readiness approval. I-0007-011 remains a milestone that requires concrete
  implementation planning and all existing prerequisites.
- Validation and exact ready-for-review snapshots remain to be recorded in
  D-0007-004. This reconciliation is not human approval, completion,
  implementation, publication, or permission to execute.

## D-0007-005 subsequent-surface reconciliation

- Date: 2026-10-10. Baseline
  `07073fe16ae1b6f64feaeedb01557d6f5b9731fd` supplies the committed
  SPEC-0007 input. The source record hashes the reviewed working-copy bytes
  containing D-0007-005's accepted contract decisions; it does not claim those
  bytes are committed.
- New R-0007-411 through R-0007-423 define distinct typed Service operations,
  bounded raw-document inputs, immutable catalog identity and policy-filtered
  pagination, capability introspection, non-executing and execution outcomes,
  exact CLI and MCP mappings, shared exit statuses, structured errors,
  deferrals, cancellation, and conformance.
- D-0007-005 is the only decision resolved by this reconciliation. I-0007-009
  and I-0007-010 now depend on it for the contract/implementation identity
  separation and trusted catalog/capability contracts. I-0007-024 and
  I-0007-025 retain their existing phase ownership and now reference the exact
  authoring and execution requirements. No item is added, split, cancelled, or
  moved between phases.
- The change creates no implementation, schema, conformance vector, catalog,
  registry, policy, execution capability, payload-disclosure authority,
  publication, or readiness approval. All four affected implementation items
  remain open milestones requiring narrower implementation planning and their
  existing prerequisites.
- Validation and exact ready-for-review snapshots remain to be recorded in
  D-0007-005. This reconciliation is not human approval, completion,
  implementation, publication, or permission to execute.

## D-0007-008 folder and namespace reconciliation

- Date: 2026-10-10. Baseline
  `34fbe88fb9d4857adc6db5390cc623c210c71540` supplies the committed coding
  conventions. The updated source record hashes the working-copy bytes that
  add the accepted production feature-folder and namespace policy; it does not
  claim those bytes are committed.
- D-0007-008 is the only decision resolved by this reconciliation. The policy
  requires exact project-relative folder-to-namespace mapping for handwritten
  production C# source and permits no handwritten-source exception. Generated
  namespace contracts remain separately governed.
- No item is added, split, cancelled, or moved between phases. I-0007-001
  retains its existing dependencies and now identifies the exact handwritten
  source mapping check required after all Phase 0A decisions receive approval
  and a concrete implementation plan.
- The change creates no production type, folder, namespace, project dependency,
  schema, conformance vector, or implementation approval. D-0007-009 through
  D-0007-014 remain independent or blocked only by their recorded prerequisites;
  I-0007-001 remains an open milestone blocked by all seven Phase 0A decisions.
- Validation and the exact ready-for-review snapshot are recorded in
  D-0007-008. This reconciliation is not human approval, completion,
  implementation, publication, or permission to execute.

## D-0008-010 generator-ownership input reconciliation

- Date: 2026-10-10. SPEC-0008 at committed baseline
  `5c166ff223ad2d5c57824de534d409bcac22b090` is now an explicit cross-plan
  source. Its source record hashes the reviewed working-copy bytes containing
  R-0008-019; it does not claim those bytes are committed or approved.
- R-0008-019 assigns the independently versioned Roslyn generator package to
  the .NET implementation workspace as build tooling and prohibits generator
  or private tooling dependencies from entering runtime dependency closures.
- D-0007-012 now depends on D-0008-010 and covers R-0008-019 while retaining
  ownership of the exact generator/runtime algorithm-reuse, assembly, package,
  and architecture-enforcement decisions. I-0007-008 now depends on both
  decisions and records the accepted workspace ownership while leaving its
  exact project, package, API, shared-library, and test manifests pending.
- No SPEC-0007 requirement, phase, implementation artifact, runtime dependency,
  package, workspace, or readiness state changes. This reconciliation resolves
  no SPEC-0007 decision and does not approve D-0008-010 or authorize generator
  implementation.

## SPEC-0008 source and cross-plan reconciliation

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

## D-0007-015 portable conformance-envelope reconciliation

- Date: 2026-10-11. The committed SPEC-0007 baseline is
  `8fbf725e0fda9697c3eff44435481d7755141272`; the exact reviewed working-copy
  hash, including the D-0007-015 decision, is recorded in the source header.
- D-0007-015 specifies the selected self-contained per-case envelope, exact
  suite/case identity, typed outcomes, multi-group capability metadata, and
  reviewed offline golden regeneration under R-0007-347. The requirement
  remains the only normative source; this record does not replace it.
- D-0007-015 is the only decision outcome specified here and awaits approval
  of its exact ready-for-review snapshot. D-0007-013 remains open for
  .NET-specific loading and consumer-test conventions. I-0007-002 and
  I-0007-005 remain open milestones with their existing D-0007-015 gates.
- I-0008-003 now references R-0007-347 and retains its explicit dependencies
  on D-0007-015, I-0007-002, and I-0007-005. These prerequisites remain
  unresolved as implementation outputs; no vectors, schemas, tooling, or
  publication are produced by this decision.
- No readiness, executable slice, implementation, or delivery approval is
  inferred. Exact review of the resulting decision and plan snapshots remains
  required.

  The user explicitly approved this exact reconciliation snapshot on
  2026-10-11. The plan hash is its full-byte hash before this approval evidence
  was recorded; that evidence-only update does not alter the reviewed material.
  The approval covers this cross-plan reconciliation only, not readiness or any
  implementation item.

  | Reviewed artifact | SHA-256 |
  | --- | --- |
  | `work/0007/plan.md` before recording approval evidence | `533c0fb58356a6dd9a7ee45718bbcf5260a468bcc30fc2b3fd91ad3b95a100bb` |
  | `work/0007/implementation/I-0007-030-shared-ci-checks.md` | `3752e63239e6086b22ff31477a6c9f2c4600fa7b872c8d19dfe20d5e1ba2f4e5` |
  | `work/0007/implementation/I-0007-031-distribution-verification.md` | `c9dd33b093fe0936724f3febfbbf1c6db5d00c3c286f309d7ca1cfacac388c4f` |
  | `work/0007/implementation/I-0007-032-website-release-gates.md` | `7d1e462ebab558e4e2be501fe15efeee4d77b87b92a7a83d9d04461cf42c295f` |
  | `work/0008/implementation/I-0008-003-conformance-artifacts.md` | `739272db2384f773ffc28b98385743c8eea603a499634ce12ca4ff44614daf19` |

## SPEC-0007/SPEC-0008 artifact sequencing reconciliation

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

## D-0007-010 representative type relationship reconciliation

- Date: 2026-10-11. Baseline: `8c63f2df1b8950fc0e283810e21e1d59db81f867`.
  The user selected separate, closed, layer-private node and expression
  variant families, with shared roots only for genuine common semantics.
- Added SPEC-0006 R-0006-040 to define composition-based recursion, separation
  of inert syntax from bound/compiled plan state, and the layer-private
  boundary. Exact CLR types and file organization remain for implementation
  planning; no code, schema, vector, or public contract changed.
- D-0007-010 now records the selected outcome and adds R-0006-040 to its
  governing requirements. I-0007-001 now includes R-0006-040 and specifies
  corresponding architecture-enforcement coverage. No other downstream
  item is revised: D-0007-012 concerns the independent generator/runtime
  dependency boundary, and I-0007-008 remains downstream of I-0007-001.
- No item identity, dependency edge, phase membership, or readiness approval
  changed. D-0007-010 still requires its checks and exact-snapshot review;
  this reconciliation does not mark it complete. I-0007-001 remains an
  unapproved milestone, and no implementation or publication eligibility is
  inferred.
- Source reconciliation is limited to the new SPEC-0006 requirement. Its
  working-copy SHA-256 is recorded in the source list above; the committed
  baseline revision is retained. The other SPEC-0007 source records remain
  unchanged. Existing references to R-0006-026 and fingerprints of existing
  requirement blocks are unaffected.
- Initial structure checks: all 16 SPEC-0007 source hashes match and their
  baseline revisions resolve; all 75 SPEC-0007/SPEC-0008 item IDs are unique,
  dependencies resolve, and the combined graph is acyclic. All three local
  Markdown links in the changed work items resolve. The exact comparison
  against HEAD preserves all 39 existing SPEC-0006 requirement fingerprints;
  R-0006-040 is the next identifier and fingerprints to `fca8f1`.
- Specification trace check: PASS with a warning for the implementation-
  specific .NET layer terminology in new R-0006-040. No prior references to
  the new requirement exist and no product code, tests, or waivers changed.
  The derived change kind is `requirement`, with `Spec: R-0006-040@fca8f1`.
  No build or unit tests apply to this specification and work-planning change.

## D-0007-012 generator/runtime reuse reconciliation

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
