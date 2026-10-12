---
id: D-0007-014
kind: decision
title: DI lifetimes and immutable state ownership
status: complete
spec: SPEC-0007
requirements:
  - R-0007-346
  - R-0006-013
  - R-0006-016
  - R-0006-019
  - R-0002-029
  - R-0002-030
  - R-0004-041
  - R-0007-351
  - R-0007-360
  - R-0007-362
depends_on: [D-0007-009]
artifacts: [docs/development/conventions/dotnet.md]
---

# D-0007-014: DI Lifetimes

## Objective

Document lifetime and ownership rules needed by the first implementation slices.

## Scope and exclusions

Registry snapshots, cached plans, per-run state, and credential-related
collaborators. Preserve constructor injection, private run state, and established
composition boundaries; do not add ambient execution context.

## Questions to resolve

Which lifetimes, disposal ownership, snapshot capture, and invalidation boundaries
apply to each collaborator? What tests detect unsafe cross-run state sharing?

## Acceptance criteria

- [x] Persistent lifetime/ownership rules cover registry generations, cached
      plans, invocation state, and credential-related collaborators.
- [x] Run isolation, snapshot capture, invalidation, and disposal rules remain
      compatible with governing requirements.
- [x] DI resolution/scope and architecture-test expectations are explicit;
      concrete service registrations remain for implementation planning.
- [x] Applicable checks pass and the exact input/output snapshot is recorded.

## Resolution

The user selected persistent lifecycle and ownership rules, with concrete
Microsoft DI registrations deferred to their reviewed implementation slices.
The rules are recorded in the
[.NET conventions](../../../docs/development/conventions/dotnet.md#host-generations-invocation-scopes-and-derived-plans)
under R-0007-346 and preserve the existing boundaries in
[SPEC-0006](../../../specs/0006-dotnet-layered-architecture.md#6-dependency-and-composition-rules),
[SPEC-0002](../../../specs/0002-operation-catalogs-and-host-configuration.md#10-effective-catalog-construction),
[SPEC-0004](../../../specs/0004-ai-assisted-connections.md#15-audit-and-revocation),
and [SPEC-0007](../../../specs/0007-portable-pipeline-definitions-and-binding.md#execution-and-public-surface-acceptance):

- A run captures one complete immutable registry, connection, and policy
  generation. A replacement is published only after explicit reload has
  rebuilt and revalidated it; resources owned by a retired generation remain
  alive until its active runs finish.
- The executable/hosting boundary owns one DI scope per pipeline invocation.
  Run-specific collaborators are scoped to that invocation and released after
  success, failure, or cancellation. Behavioral components do not access
  Microsoft DI scopes or providers.
- The host owns the cache of complete immutable, derived plans. It cannot
  return plans invalidated by any required cache input, and it owns eviction
  and release without disrupting active invocations.
- Resolved credential material remains within its protected provider boundary.
  A credential cache, if present, is provider-owned and clearable through the
  applicable administrative contract; secrets are not copied into registry
  generations, cached plans, definitions, or execution frames.
- DI lifetimes follow state ownership, but this decision does not assign exact
  singleton, scoped, or transient registrations to unimplemented service
  types. Their registrations and concrete disposal mechanics are decided in
  reviewed implementation slices.

The alternative of fixing every concrete service registration now was not
selected because those service types and compositions have not yet been
implemented or planned. No product requirement or runtime behavior is amended,
and this decision does not authorize implementation.

## Validation and review

Validation performed on 2026-10-12:

- Decision scope and requirement coverage: PASS. This records lifecycle and
  ownership guidance under existing requirements; it does not amend product
  requirements or authorize implementation.
- Source reconciliation: all 21 SPEC-0007 plan source records match current
  bytes and resolve to their recorded baselines. SPEC-0008 retains a malformed
  source record for `docs/development/conventions/schemas.md`; the
  `engineering-policy` readiness snapshot is stale. Neither is renewed or
  treated as evidence for this decision.
- Work-plan graph: PASS. The combined SPEC-0007/SPEC-0008 graph validates with
  75 items and 216 dependencies. Its generated diagram is refreshed and its
  freshness check passes; the diagram is a derived view and is not separately
  hashed to avoid a self-referential snapshot.
- Specification trace check: PASS. The five in-scope changes are documentation,
  work-planning records, and generated work-plan output; no specification,
  product code, or test code changed. Change kind is `maintenance`; proposed
  trailer: `Change-Kind: maintenance`.
- `git diff --check` and changed-document target checks pass. No build or unit
  tests were run because this decision changes only documentation and work
  artifacts, and no documented command applies.

No DI lifetime, registry reload, execution-plan cache, or credential
implementation is authorized by this decision.

Exact ready-for-review snapshot:

| Material input or output | SHA-256 |
| --- | --- |
| This decision's material content | `0bc60d687eb6982c75b9938bc41f90b7f488ca264e1c3d7aca34c62724f557e6` |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| `.github/instructions/dotnet.instructions.md` | `97fa3163316d35c1a7ccac75293f896652f7f7b150cc4fbff83ab4d67ee9d05e` |
| `specs/0002-operation-catalogs-and-host-configuration.md` | `c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca` |
| `specs/0004-ai-assisted-connections.md` | `39625b975496c96ae55c21785fd632f75d10096349acc82a4d277fc93c698e57` |
| `specs/0006-dotnet-layered-architecture.md` | `785bc5aba6b82f1aa3e73a84d86d91fcf4c7d0a3bb0425f2a389d1d874940732` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `docs/architecture/decisions/0001-use-microsoft-dependency-injection.md` | `663bc361c4799b69e700c6161311d60e010b89c0f65a6065be5acf9d20358173` |
| `docs/development/coding-conventions.md` | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/spec-driven-workflow.md` | `c1045d2891c7ccbe00c833e247d7254c7e4161857dfe6884b47a644cb3e1c11e` |
| `docs/development/conventions/dotnet.md` | `d590f92c5e151ae4eb02540d48a7e029863346715204c18ebe3afdc7394d7336` |
| `work/0007/plan.md` | `4c1cb8bd2aefb2e2cbfa1d17d77942ff926c94c4bbba147d71dfe1cfe05775f2` |
| `work/0008/plan.md` | `99db86435bedc756e827afe05854ac20146ec09bd03105fdf0e8787d488dc9e4` |

Approval recorded on 2026-10-12: the user explicitly approved this exact
outcome in this session. Approved scope: the lifecycle and ownership guidance
and bounded SPEC-0007/SPEC-0008 plan reconciliation in the material snapshot
above. Exclusions: concrete DI registrations and runtime implementation,
readiness approval, renewal of the unrelated SPEC-0008 readiness/source
records, and component-contract publication. The user also reviewed the
generated graph at SHA-256
`1ecd1b6a2eb8915cd4360185de8225dbcbc0279d4c127c530fb515f2fc4012cd`.
