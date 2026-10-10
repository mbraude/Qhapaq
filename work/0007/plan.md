---
spec: SPEC-0007
sources:
  - path: specs/0007-portable-pipeline-definitions-and-binding.md
    revision: 07073fe16ae1b6f64feaeedb01557d6f5b9731fd
    content_sha256: 1abf378410e3d9563f39ec37baf46757998ee029e55e86fdd5c78539f020a1f3
  - path: specs/0002-operation-catalogs-and-host-configuration.md
    revision: 66c43b3d030e84a4ac055b6853946c401d7a9b8c
    content_sha256: c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca
  - path: specs/0006-dotnet-layered-architecture.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: e5a35871ce14aa37d7169ac35d824c910bb0494a01e419dc7895a69dd0092eb9
  - path: specs/0001-core-pipeline-model.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e
  - path: docs/development/coding-conventions.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: a56e921915f25eab627cf3d4fbbe8d32028f99f965a3dd67fac6c166d10691bc
  - path: docs/development/spec-driven-workflow.md
    revision: 34fbe88fb9d4857adc6db5390cc623c210c71540
    content_sha256: 2f04cd9e4cc28dbae1cc55593ef7fe29b293911f34175c85faab19c061c8743b
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
---

# SPEC-0007: Work Plan

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
R-0007-347.
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
support R-0007-368. Non-executing work does not depend on the whole runner.

### Ordered items

| Order | Item | Outcome |
| --- | --- | --- |
| 1 | [I-0007-024](implementation/I-0007-024-authoring-projections.md) | Incremental listing, validation, explanation, Mermaid and comparison |

### Exit gates

Each supported adapter consumes common versioned Service behavior without
duplicating domain/policy rules. Plan narrower slices with explicit dependencies:
listing after 3/3A; structural conclusions after 4; full validation/explanation
after 6B; comparison after 5A/exact sources; Mermaid after required analysis.

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
claims do not remove required v1 deliverables.

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
