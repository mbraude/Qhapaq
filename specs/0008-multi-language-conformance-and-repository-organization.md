# SPEC-0008: Multi-language Conformance and Repository Organization

> **Status:** Draft; decision questions resolved in normative requirements; exact snapshot review and readiness remain required
> **Version:** 0.14
> **Scope:** Future multi-language implementations and repository artifact organization
> **Last updated:** 2026-10-10

## 1. Purpose and Decision Status

This document records the proposed direction for supporting Qhapaq
implementations in multiple languages while accommodating software artifacts
that are not runtime implementations, such as a website, editor integrations,
and development tools.

The decision questions are resolved in normative requirement blocks and await
review of the exact specification snapshot where not already approved. This
draft does not publish a conformance profile, add a language runtime, authorize
implementation, or approve a migration slice. Discussion and alternatives do
not receive requirement IDs.

Existing specifications and engineering policies remain in force. In
particular, this draft does not relocate source, rename assemblies, change
portable behavior, or promise additional language runtimes in v1.

The [SPEC-0008 work plan](../work/0008/plan.md) tracks decision and future
delivery work. It is not an executable delivery plan until the applicable
requirements, readiness, and implementation-slice gates are approved.

## 2. Existing Foundations

The governing sources already distinguish portable semantics from the .NET
reference implementation:

- [SPEC.md](../SPEC.md), particularly R-0000-007 and R-0000-009, establishes
  language-neutral contracts, shared vectors, and conformance declarations.
  R-0000-009 places new implementations under
  `src/implementations/<language>/`.
- [SPEC-0006](0006-dotnet-layered-architecture.md) defines the initial .NET
  architecture, including its Entry Points layer.
- [SPEC-0007](0007-portable-pipeline-definitions-and-binding.md) defines
  portable definitions, operation contracts, and binding semantics.
- [SPEC-0005](0005-build-release-and-website-delivery.md) defines build,
  release, provenance, and website delivery obligations.
- [ADR-0003](../docs/architecture/decisions/0003-enforce-specification-traceability.md)
  and [ADR-0004](../docs/architecture/decisions/0004-classify-changes-and-trace-through-commits.md)
  define specification traceability and change classification.

The specification library is intended to be sufficient to reproduce Qhapaq
without treating reference implementation behavior as the semantic authority.
This draft explores how to make that intent practical across languages and
artifact types.

## 3. Goals and Non-goals

### Goals

- Describe compatibility independently of implementation language.
- Distinguish runtime implementations from integrations, website source, and
  contributor tools.
- Separate common engineering policy from language- and artifact-specific
  conventions.
- Retain useful language-specific examples without accidentally making their
  syntax a portable requirement.
- Give future implementations a precise, testable conformance target.
- Preserve self-contained build workspaces and shared portable test assets.

### Non-goals

- Implement another runtime or select its language.
- Generate working implementations solely by introducing this document.
- Change the canonical JSON format, exact-version resolution, non-durable v1
  execution, or host-controlled policy and disclosure boundaries.
- Select a website framework, extension platform toolchain, or generator API.
- Finalize profile schemas, names, versions, test suites, or publication gates.
- Create empty directory scaffolds, migrate existing source, or rename packages.
- Replace detailed engineering conventions or architectural ADRs with this
  discussion document.

## 4. Artifact Taxonomy and Source Layout

### Terminology

An **implementation** is a runtime that consumes portable
Qhapaq contracts and implements a declared set of conformance obligations.

An **integration** connects Qhapaq to an external product or ecosystem through
supported contracts. A Visual Studio extension is an example; its presence
does not by itself make it a runtime implementation.

A **website** is the public product and documentation surface, not an
execution or credential control plane. A **development tool** supports
contributors, builds, or validation rather than pipeline execution.

Artifact purpose and source language are separate classifications. C# source
could belong to a runtime, an integration, or a contributor tool.

### Top-level source directory

**[R-0008-001]** Maintained software is classified by responsibility beneath the top-level
`src/` directory:

```text
src/
  implementations/
    dotnet/
      src/
      tests/
  integrations/
  website/
  tools/

SPEC.md
specs/
schemas/
conformance/
examples/
docs/
scripts/
build/
```

The categories classify artifact purpose independently of implementation
language. They are ownership groupings, not shared build workspaces. Directories
are added only for real content; this target does not require empty scaffolds.

**[R-0008-002]** A maintained artifact belongs under `src/` when it has an independently
buildable, testable, packageable, or distributable software lifecycle. Each
implementation or independently maintained integration, website, or development
tool keeps a self-contained workspace containing its source, tests, dependency
manifests, and pinned toolchain where applicable. The repeated
`src/implementations/dotnet/src/` preserves the distinction between production
projects and tests; it does not require another artifact to use the same inner
layout.

Specifications, portable schemas, shared conformance vectors, curated
documentation, user-facing examples, automation entry points under `scripts/`,
and cross-artifact orchestration under `build/` remain outside `src/`. Executable
syntax alone does not make an example or automation entry point a software
workspace.

### Ownership and dependencies

**[R-0008-003]** Software workspaces consume portable root assets and interact with other
workspaces only through documented public contracts, protocols, packages, or
release artifacts:

- Implementations consume portable specifications, schemas, and vectors.
- Integrations consume supported public contracts, protocols, or packages
  rather than implementation internals.
- Website generation consumes curated content and release metadata without
  making the deployed site authoritative for product semantics.
- Build tools may inspect source without becoming runtime dependencies.
- A workspace must not consume another workspace's private build output.

Generated outputs remain ignored or in an explicitly documented generated
location unless a version-controlled consumer requires them. Generated output
does not become authoritative over its source, and a deployed or generated
website does not become authoritative for product semantics.

The physical relocation of the existing .NET workspace and related path
updates require separately reviewed migration work. This decision does not move
files, rename namespaces, assemblies, or packages, or change runtime behavior.

### Concrete artifact ownership

**[R-0008-019]** Artifact ownership follows the responsibility and supported
contract of the artifact, not its implementation language:

- The Roslyn incremental generator required by SPEC-0007 is owned by the .NET
  implementation workspace because it supplies the .NET operation-authoring
  build contract. It is independently versioned and packaged build tooling,
  and consuming it must not add a generator assembly or its private
  dependencies to a runtime application's dependency closure. The exact
  reviewed package and shared-algorithm boundaries remain governed by the
  SPEC-0007 generator/runtime reuse decision.
- Each product integration is an independently maintained workspace beneath
  `src/integrations/`, including when it uses the same language as an
  implementation. It may consume only supported public contracts, protocols,
  packages, or release artifacts and must not reference a runtime workspace's
  private source or build output.
- A project-owned contributor, validation, or build utility with its own
  software lifecycle is an independently maintained workspace beneath
  `src/tools/`. Root `scripts/` and `build/` remain automation entry points and
  cross-artifact orchestration rather than owners of runtime libraries.
- An implementation workspace may consume portable root assets and approved
  public build-time tooling, but it must not take runtime dependencies on
  integrations or contributor tools. Packaging and release assembly preserve
  these ownership and dependency directions instead of merging private outputs
  across workspaces.

## 5. Engineering Policy Ownership and Applicability

### Common and specialized conventions

**[R-0008-004]** Engineering policy uses a common baseline with scoped
specializations:

- `docs/development/coding-conventions.md` owns repository-wide engineering
  requirements and defaults, including correctness, boundary validation,
  security, privacy, determinism, traceability, testing, documentation,
  generated artifacts, and dependency review.
- A language- or artifact-specific guide is added beneath
  `docs/development/conventions/` only when a maintained consumer needs it.
  Each guide declares its applicability, links the common policy and relevant
  specifications and ADRs, and owns only concerns specific to that scope, such
  as syntax, naming, API idioms, compiler or package tooling, accessibility, or
  integration lifecycle.
- All applicable policies are cumulative. A specialized guide may explicitly
  replace a common Default or Recommendation within its declared scope. It
  must not weaken a common Required rule or override a specification or ADR;
  such a conflict requires changing the higher-authority source first.
- Portable product behavior remains in specifications, architectural choices
  remain in ADRs, and specialized guides link those authorities rather than
  copying their normative rules.
- Path-specific agent instructions link the applicable common and specialized
  policies and contain only path routing or tool-execution guidance that does
  not create a competing policy source.

No empty specialized guide or directory is created speculatively. Moving the
existing .NET-specific material and removing duplicated instruction text is
separate delivery work and does not change product behavior.

### Normative content categories

**[R-0008-005]** Specification content is separated by authority, declared
scope, and requirement-block boundaries:

- Portable product requirements belong in `SPEC.md`, a numbered platform
  specification, or an implementation-neutral component specification. Their
  requirement blocks must remain independent of implementation language.
- A normative language-specific API or runtime contract belongs in a numbered
  implementation specification whose status or introductory scope explicitly
  names the language and runtime. Its normative rules use requirement blocks
  and must not be embedded in a portable requirement block. SPEC-0006 is the
  current .NET implementation specification; no implementation specification
  is created for a language or runtime that has not been approved.
- Rationale, alternatives, goals, non-goals, open questions, and future-only
  direction remain outside requirement blocks and are non-normative.
- An example outside a requirement block is non-normative, is introduced as an
  **Illustrative example**, and cannot add, relax, or contradict required
  behavior.
- An example inside a requirement block is normative, is introduced as a
  **Normative example**, and forms part of that block's fingerprint and
  conformance expectations. A merely explanatory example must be moved outside
  the block rather than labeled non-normative within it.

Mixed content is split at headings or requirement-block boundaries so readers
and tooling can determine its category without interpreting programming
language syntax. Labels do not replace stable requirement identifiers.

### Language-neutral traceability

**[R-0008-016]** Traceability markers use the language-neutral payload
`spec: <requirement-id>@<fingerprint>[, <requirement-id>@<fingerprint>...]`.
Each maintained implementation language defines, in its applicable engineering
policy, the native comment or documentation constructs that may carry the
payload and the exact attachment rules for invariants, whole-member
enforcement, and verifying tests. A language is not supported for traceability
until those placements and a matching checker extractor are registered.
Language-specific documentation syntax, including C# XML documentation, is
not required in another language.

Marker-like text outside a registered comment or documentation construct,
including text in string literals, generated output, examples, or unsupported
files, is not a traceability marker and must not satisfy a traceability
obligation.

**[R-0008-017]** The deterministic trace checker separates language syntax
from portable validation. A registered language-aware extractor parses only
the native constructs permitted by that language's policy and emits the
payload, source span, attachment target, and whether the target is production
code or a test. One shared rules engine validates payload grammar, requirement
resolution, current fingerprints, invariant and test placement, changed-
requirement reverse impact, and waiver scope across all registered languages.
Language extractors must not independently redefine those portable rules.

For each diagnostic, the checker reports the file, source span, stable rule,
and offending marker or requirement identity. Malformed markers, unsupported
placements, stale fingerprints, unresolved or retired requirements, missing
required references, and extractor failures are errors rather than ignored
text or successful results.

**[R-0008-018]** The portable waiver payload remains
`spec-waive: <rule>[, <rule>...] — <justification>` and is recognized only in
the same registered native constructs and attachment scopes in which a
reference could appear. A waiver remains explicit, reviewable, and limited to
the named judgment finding; it cannot waive marker grammar, requirement
resolution, fingerprints, identifier integrity, reverse-impact inspection, or
required commit trailers. Adding, broadening, or moving a waiver continues to
require explicit human direction.

### Illustrative language-specific example

**Illustrative example (non-normative).** A language-specific example can
explain portable behavior without defining a portable or language-specific
contract. Because this example is outside a requirement block, changing its
syntax does not change a requirement fingerprint.

For example, the following illustrates an asynchronous input-to-output mapping;
it is not a proposed mandatory API for every language and does not fully
specify cancellation or failure semantics:

```csharp
public interface IOperation<TInput, TOutput>
{
    Task<TOutput> ExecuteAsync(
        TInput input,
        CancellationToken cancellationToken = default);
}
```

An exact .NET interface could separately be normative in an explicitly
.NET-specific requirement. Another language could use a different API while
preserving the applicable portable behavior.

## 6. Conformance Model

### Meaning of a profile

A **conformance profile** is a named, versioned set of specification obligations
that supports a defined compatibility claim. It answers what an implementation
promises when it says it conforms to a particular Qhapaq surface.

A profile selects a coherent set of authoritative requirements; it does not
create another executable format or permit a different interpretation of
portable semantics. Profiles are defined by Qhapaq, not invented by each
implementation to excuse omissions.

**[R-0008-006]** The initial conformance profiles have these identities,
applicability boundaries, and prerequisites:

| Profile ID | Applies to | Required scope | Prerequisite profiles |
| --- | --- | --- | --- |
| `qhapaq.runtime` | A runtime implementation that validates, binds, and executes portable pipeline definitions | Applicable language-neutral canonical-model, validation, binding, execution, exact-version, policy-before-side-effect, cancellation, and failure-preservation obligations | None |
| `qhapaq.cli.local` | A locally installed CLI distribution that hosts Qhapaq execution | The complete portable CLI contract and local adapter behavior, including every applicable `qhapaq.runtime` obligation | `qhapaq.runtime` |
| `qhapaq.mcp.host` | An MCP server that hosts Qhapaq tools | The complete portable MCP contract, host policy and payload-disclosure boundaries, and every applicable `qhapaq.runtime` obligation | `qhapaq.runtime` |
| `qhapaq.dotnet.in-process` | The supported public in-process .NET API for constructing, validating, and executing pipelines | Applicable .NET API and architecture contracts plus every applicable `qhapaq.runtime` obligation | `qhapaq.runtime` |

Profile obligations are cumulative with all transitive prerequisites. A
dependent profile cannot replace, reinterpret, or make optional an obligation
from `qhapaq.runtime`. The CLI and MCP profiles are independent siblings; an
artifact can implement either without implementing the other. Remote CLI,
MCP, or other protocol clients do not satisfy these host profiles and receive
no initial profile until their protocol and client obligations are specified.

### Profile contents and version identity

A profile definition identifies:

- Exact identity, version, applicability, and referenced specification snapshot.
- Required requirement IDs and prerequisite profiles.
- Mandatory obligations and explicitly optional capabilities.
- Shared test-vector groups and implementation-specific evidence.
- The compatibility claim permitted by satisfying those obligations.
- Review, publication, support, and compatibility-change rules.

Implementation release versions, profile versions, document versions, protocol
versions, and requirement fingerprints represent different things.

**[R-0008-008]** A published profile version has the immutable identity
`<profile-id>@<major>.<minor>`. `major` is a positive decimal integer without
leading zeroes, `minor` is a non-negative decimal integer without leading
zeroes, and the first publishable version of a profile is `1.0`. Draft
revisions are not profile versions and cannot support conformance claims.

Each profile version binds its exact profile identity and applicability, each
prerequisite profile at an exact version, the exact authoritative
specification revisions, and the complete ordered set of mandatory requirement
ID and fingerprint pairs. It also identifies optional capabilities and other
non-mandatory profile metadata without treating them as mandatory obligations.
An implementation release, document revision, protocol version, or requirement
fingerprint must not be substituted for or inferred to be a profile version.

After publication, a profile-version definition and the meaning of a claim
against it are immutable. A later version within the same major version is
compatible with an earlier version only when it preserves every mandatory
obligation and prerequisite of the earlier version. A minor version may make a
reviewed semantics-preserving correction, including the resulting exact
fingerprint update, or add optional capabilities or other non-mandatory
metadata. Adding or removing a mandatory obligation; changing mandatory
behavior, applicability, or a prerequisite identity or version; weakening an
obligation; or making a previously optional capability mandatory requires a
new major version.

Retirement, supersession, support status, and withdrawal do not alter a
profile version or an existing claim. Version numbers imply no support period.
Conformance to one version never creates or migrates a claim for another
version automatically, including a compatible minor version; a new exact
claim requires evidence against the newly claimed version. Publication,
support-window, retention, and withdrawal procedures are defined separately
from these compatibility rules.

### Profiles versus capabilities

A profile is a compatibility baseline. A capability identifies a supported
feature or installed facility, such as a particular operation family.

Two runtimes can satisfy the same profile while exposing different operation
catalogs.

**[R-0008-007]** A conformance claim must name an exact Qhapaq profile identity
and, once profile versioning is defined, its exact profile version. A claim for
a dependent profile is valid only when the same artifact set satisfies that
profile and every transitive prerequisite; prerequisite identities need not be
repeated in human-readable claim text.

An implementation must not claim a profile with exclusions, exceptions,
partial support, substituted behavior, or missing mandatory obligations.
Unqualified claims such as "Qhapaq conformant" or "Qhapaq compatible" are not
conformance claims. Progress toward a profile and capabilities outside its
required scope may be reported separately, but must not use conformance
language or downgrade any profile obligation. An implementation missing
required cancellation semantics, for example, does not satisfy a profile that
includes them.

### Intended uses

The proposed lifecycle is:

1. Planning selects the profiles an implementation intends to support.
2. A language-specific harness evaluates shared vectors against that runtime.
3. Additional tests and review address obligations not proven by vectors alone.
4. A release declares support backed by evidence for its exact built version
   and the exact profile revision.
5. Compatibility changes are reviewed without silently changing the meaning of
   an existing claim.

Shared cases could cover canonicalization, validation, exact-version binding,
composition, cancellation, failure preservation, and policy-before-side-effect
ordering. Harness details may vary by language; portable expected behavior
would not.

Progress reporting would be distinct from a full conformance claim. The
candidate model does not treat a self-declared manifest or a passing vector
suite alone as proof of every security and concurrency obligation.

A machine-readable declaration and release conformance report are proposed
artifacts. Evidence sufficiency and claim publication remain unresolved.

### Capability and conformance declarations

The exact profile version is the public identity of its immutable requirement
set. A declaration therefore does not repeat Qhapaq requirement identifiers or
fingerprints for ordinary consumers. Detailed obligation results remain
available in a separately identified assessment manifest for validators and
auditors.

**[R-0008-009]** A capability and conformance declaration is a closed,
machine-readable envelope with an exact declaration-format identity and
version. Each envelope has exactly one of these kinds:
`conformance-claim`, `progress`, or `unsupported-target`. It addresses exactly
one published profile version and identifies exactly one evaluated
implementation by implementation ID, declared implementation version, and an
immutable digest of the evaluated artifact set. A source revision may be
included as metadata but must not replace the artifact-set digest. The same
artifact set may have separate declarations for multiple profiles.

A declaration may report optional capabilities by their exact identities with
the disposition `supported` or `unsupported`. Omission makes no assertion.
Partial capability support must not be declared unless the applicable profile
defines independently declarable, narrower capability identities. A
human-readable rendering must preserve the declaration kind, exact profile and
implementation identities, and capability dispositions; it must not broaden a
machine-readable declaration or turn progress into conformance.

**[R-0008-010]** A `conformance-claim` or `progress` declaration must bind an
immutable assessment-manifest identity and digest. The assessment manifest
identifies the target profile's complete ordered set of mandatory requirement
ID and fingerprint pairs, including transitive prerequisites, and gives each
pair exactly one disposition: `satisfied`, `failed`, or `not-evaluated`. It
also maps every `satisfied` obligation and every declared `supported`
capability to one or more exact evidence entries. The declaration exposes the
profile identity and assessment reference rather than duplicating that
requirement-level mapping. Evidence-sufficiency rules are defined separately.

A `conformance-claim` is valid only when the assessment classifies every
mandatory obligation as `satisfied`. A `progress` declaration may summarize
the three dispositions, but any summary must equal the exhaustive assessment;
it must not use conformance language. An `unsupported-target` declaration is
valid only when the implementation does not target the profile and gives
exactly one reason: `surface-absent`, `not-implemented`, or
`platform-unsupported`. An attempted implementation with a failed or
unevaluated obligation is progress, not an unsupported target.

Unknown declaration formats, versions, kinds, profiles, capability identities,
dispositions, or unsupported-target reasons are invalid. Missing required
fields, duplicate obligation results, mismatched summaries, unresolvable or
digest-mismatched assessment manifests, incomplete mandatory-obligation sets,
or evidence-free positive results are also invalid. Validation failure must be
reported explicitly and must not produce a conformance claim, progress report,
or unsupported-target result.

### Conformance evidence

Evidence sufficiency is part of an immutable profile version rather than a
claimant-selected or assessor-selected threshold. This permits different
obligations to require different proof while giving every implementation
claiming the same profile version the same acceptance rules.

**[R-0008-011]** Each published profile version must contain a complete evidence
matrix covering every mandatory requirement ID and fingerprint pair and every
optional capability that the profile permits a declaration to report as
`supported`. Each matrix entry is a closed evidence recipe composed of
non-empty `all-of` and `any-of` expressions whose leaves have stable identities
and use exactly one of these portable evidence kinds:

- `shared-vector`;
- `implementation-test`;
- `integration-test`;
- `architecture-review`;
- `security-review`; or
- `build-provenance`.

An evidence-recipe leaf defines the observable result required for that
obligation or capability and identifies any exact vector group, test contract,
or review scope that governs it. Each executable leaf also defines finite
execution-time and resource bounds. An `all-of` expression requires every
child; an `any-of` expression requires at least one child. Alternatives in an
`any-of` expression must prove the same observable rule through
profile-authorized evidence boundaries. A claimant must not omit a child,
weaken a bound, add an alternative, or substitute an evidence kind that the
exact profile version does not authorize.

**[R-0008-012]** Evidence for one assessment is an immutable,
content-addressed bundle. Every entry identifies its evidence kind, the exact
recipe leaf it addresses, the evaluated implementation artifact-set digest,
its immutable inputs, and its bounded result. Executable entries have the
closed outcomes `passed`, `failed`, `skipped`, or `error`; only `passed`
satisfies an executable leaf. Architecture-review and security-review entries
have the outcomes `approved`, `rejected`, or `not-completed`; only `approved`
satisfies a review leaf. A review approval identifies the reviewer, review
time, exact scope, and reviewed artifact-set digest. The reviewer may be a
contributor to the reviewed implementation; independent review and a
predefined checklist are not required unless a future profile version
expressly adds a different obligation.

A `build-provenance` entry has the outcomes `verified` or `unverified`; only
`verified` satisfies its leaf. It binds the source revision, dependency-lock
inputs, toolchain and environment identity, build invocation, and produced
artifact-set digest. Executable evidence also records the harness or command
identity, toolchain and environment identity, expected result, and result
digest needed for an independent rerun from the immutable inputs. Reproduction
requires the same normative result, not byte-identical incidental logs.

**[R-0008-013]** An assessment may mark a mandatory obligation `satisfied` or
an optional capability `supported` only when its exact evidence recipe
evaluates true and every selected evidence entry resolves with the recorded
digest. Missing evidence, an unsatisfied recipe branch, a digest or
artifact-set mismatch, a failed check, a skipped check, an execution error, a
rejected or incomplete review, unverified provenance, or an exceeded bound
must not satisfy a recipe. A mandatory obligation has no
`not-applicable` evidence outcome; applicability is fixed by the profile.

**[R-0008-014]** Conformance evidence uses synthetic, non-sensitive fixtures. Evidence bundles,
reports, logs, and human-readable renderings must not contain credentials,
resolved secrets, authentication material, sensitive environment values, or
sensitive operation payload content. Discovery of prohibited material
invalidates the affected evidence entry; correction requires a new immutable
evidence bundle and assessment rather than mutation of the published bytes.

**[R-0008-015]** Evidence must remain resolvable for as long as a declaration is published or
otherwise presented as verifiable. If its evidence is no longer resolvable,
the declaration must no longer be presented as a verifiable claim or progress
report, and the loss of verifiability must be explicit. Publication,
withdrawal, and discoverability procedures are defined separately.

### Profile and conformance-claim publication

**[R-0008-023]** Publishing a profile version or implementation conformance
claim requires the explicit approval of one identified authorized maintainer
after all applicable validation succeeds. The approval records the approver,
time, exact scope, and immutable identities and digests of the bytes approved.
A profile approval covers its exact definition, prerequisite versions,
authoritative specification revisions, requirement fingerprints, evidence
matrix, and publication metadata. A claim approval covers its exact
declaration, assessment manifest, evidence bundle, evaluated artifact set,
profile version, and root release manifest.

Work-item completion, a passing check, a commit or push, evidence-review
authorship, component-contract publication, and approval of another snapshot
do not grant publication authority. A publication gate must fail explicitly
when approval, validation, an exact input, or a required digest binding is
missing, unsuccessful, stale, or inconsistent.

**[R-0008-024]** Each published profile version and conformance claim has an
immutable, content-addressed publication record. The record binds the exact
published object and its approval to the protected stable or prerelease root
release manifest that promotes it, and it remains publicly discoverable by its
stable identity. Profile publication records expose exactly one current
support status: `supported`, `deprecated`, or `retired`. Claim publication
records expose exactly one current status: `active`, `superseded`, or
`withdrawn`.

Status history is append-only metadata and must not mutate the published
profile, declaration, assessment, evidence, artifact set, approval, or release
manifest. A deprecated profile remains eligible for new claims only when the
claim prominently reports the deprecation. A retired profile rejects new
claims. Supersession does not withdraw or migrate an earlier claim.

**[R-0008-025]** Published bytes and publication-record history are never
rewritten to correct a profile or claim. A profile correction uses the new
minor or major version required by R-0008-008. A claim correction publishes a
new declaration, assessment, evidence bundle, approval, and publication record
and marks the earlier claim `superseded` only by appending a status event that
identifies the replacement.

A claim must be withdrawn when it is materially false, its required evidence
is invalid or unavailable, its evaluated artifact set or provenance is
compromised, or continued presentation would violate security, privacy, or
legal obligations. Withdrawal appends the actor, time, reason, and any
replacement identity; it does not delete the claim or imply conformance for a
replacement. A withdrawn claim must not be presented as active or verifiable.

**[R-0008-026]** Publication records, approval records, complete status
histories, and withdrawal tombstones are retained indefinitely, subject to
legal requirements. Supporting evidence remains resolvable while a claim is
`active` or otherwise presented as verifiable. Evidence may be removed after
the claim becomes `superseded` or `withdrawn`, but the retained record must
state that the claim is no longer verifiable and preserve the evidence
identities and digests needed for audit.

The publication audit history identifies every actor, event, time, object,
prior and resulting status, release manifest, and destination. Discovery and
human-readable renderings must expose current status, retained history, exact
profile and implementation identities, and any deprecation, supersession,
withdrawal, or loss-of-verifiability notice without broadening the underlying
claim.

## 7. .NET Entry-Point Terminology

The word "implementation" currently describes both a language runtime and the
.NET layer formerly called Service Implementations. SPEC-0006 names the upper
.NET layer **Entry Points** while retaining its adapter responsibilities and
adjacent-layer dependency direction. Its directories, projects, assemblies,
root namespaces, and derived source namespaces use the matched
`Qhapaq.EntryPoints.<EntryPoint>` identity. Executable filenames and
distribution package IDs remain separate identities.

Source relocation and the coordinated project, assembly, and namespace rename are
separate changes: moving directories does not inherently change namespaces,
package identities, dependencies, or portable behavior.

## 8. Security, Privacy, Failures, and Compatibility

This draft proposes no weakening of execution, network, consent, credential, or
payload-disclosure policy. A language's inability to reproduce a required trust
boundary would be a conformance limitation, not permission to skip it.

Future conformance tooling would need synthetic credentials and payloads,
bounded test execution, explicit failure reporting, and reports free of
resolved secrets. Missing evidence, skipped mandatory cases, unsupported
obligations, or failed checks would be distinguishable from successful
conformance.

Repository restructuring would preserve behavior and public identity unless a
separate reviewed amendment intentionally changes them. Existing source paths,
instruction patterns, architecture tests, build inputs, and work-plan snapshots
would need coordinated impact review before a move.

## 9. Validation, CI, and Release Orchestration

**[R-0008-020]** Each maintained software workspace must document the
workspace-native commands that provide every applicable orchestration
capability from this closed set: `restore`, `format-check`, `build`, `test`,
`conformance`, `pack`, and `verify`. A workspace explicitly declares an
inapplicable capability; omission must not be interpreted as success or
inapplicability.

Maintained root automation adapts those capabilities into stable repository
entry points and dispatches to workspaces without reimplementing their
toolchain-specific behavior. Local and CI execution use the same workspace
commands, pinned toolchains, dependency locks, and validation policy. A
workspace command may produce public artifacts only from that workspace and
must not consume another workspace's private source or build output.

**[R-0008-021]** Root orchestration owns a declarative impact graph that maps
repository paths and portable root assets to affected workspace capabilities
and repository validation groups. Selection expands transitively through
public dependencies. A change to a specification, schema, shared conformance
vector, profile, declaration or evidence contract, traceability rule, root
automation contract, or other shared input must select every implementation,
integration, tool, website surface, and portable check affected by that input.

Path filtering is an optimization only. A missing, stale, conflicting, or
ambiguous mapping selects the full required validation set and reports the
mapping problem. Workspace-owned metadata may add affected work but must not
suppress root-selected work. Event-required checks, the deterministic trace
checker, applicable conformance recipes, and SPEC-0005 security, provenance,
package, website, and release gates must not be bypassed by impact selection.
Any selected required capability or validation group that fails, is skipped,
cannot run, or lacks a declared mapping fails the gate.

**[R-0008-022]** A workspace emits each conformance report and evidence bundle
as an immutable, content-addressed artifact that identifies the workspace,
command and toolchain identities, source revision, evaluated artifact-set
digest, exact inputs, bounded outcome, and artifact digest. Root orchestration
validates those artifacts and produces an aggregate manifest that references
their exact identities and digests; it must not rewrite their evidentiary
content. Missing, invalid, unsuccessful, unresolvable, or digest-mismatched
required evidence fails the applicable gate.

A coordinated build or release is defined by a root release manifest that
binds one source revision to the exact identities, versions, and digests of
every included public workspace artifact, portable asset, required report,
evidence bundle, checksum, software bill of materials, and provenance record.
Artifact versions may remain independently assigned; membership in the
manifest, not a shared version number or private-output merge, defines the
consistent release set. Verification, promotion, publication, and authorized
retry use the same manifest and exact bytes. Retention, discoverability,
approval, and withdrawal of published conformance claims remain governed by
the separate publication decision.

## 10. Migration Sequencing, Validation, and Recovery

**[R-0008-027]** Repository migration must proceed through separately approved
and reviewable stages in this order:

1. Approve every prerequisite specification amendment and ADR, then record the
   exact source baseline, affected public identities, path consumers, and
   preserved user-owned changes.
2. Deliver approved common-policy separation, requirement and example audit,
   deterministic trace checking, conformance artifacts, and root orchestration
   prerequisites through their own concrete slices.
3. Rename the .NET Entry Point directories, projects, assemblies, root
   namespaces, derived source namespaces, tests, and direct consumers at their
   existing workspace paths. This stage uses an exact rename manifest and must
   preserve executable filenames, distribution package IDs, portable behavior,
   and dependency direction unless a separate approved amendment explicitly
   changes one of those contracts.
4. After the identity stage passes validation and is approved, relocate the
   consistently named .NET workspace to `src/implementations/dotnet/` through
   an exact move manifest. Consumer changes required for build, test,
   discovery, instruction applicability, traceability, or CI correctness land
   atomically with the move. Relocation must not implicitly rename an identity
   or change behavior.
5. Update remaining non-atomic automation, documentation, release, and
   work-plan consumers, then add another workspace only for an approved real
   consumer and scope.

Each stage requires scope readiness, concrete file and consumer manifests,
recovery instructions, and explicit approval before execution. A public
identity, compatibility, behavior, release, profile-publication, or
conformance-claim change requires its own governing requirement and approval;
it must not be hidden in a relocation or consumer-update stage. Completion of
this decision does not approve or execute any migration stage.

**[R-0008-028]** Every executable migration slice must record an exact input
snapshot and establish a passing before-state with the same applicable
workspace capabilities and repository validation groups that will be used for
the after-state. Any accepted baseline exception must be identified before the
slice begins and must not conceal a new regression.

After the slice, validation must cover every affected restore, format check,
build, test, conformance, package, verification, architecture, executable and
package identity, discovery, instruction, link, automation, CI impact,
documentation, release, and work-plan surface. The result must compare
observable identities and behavior with the before-state, record the exact
output snapshot and evidence, and fail closed when a required check is failed,
skipped, unavailable, ambiguously mapped, or inconsistent. Required
validation and impact selection remain governed by R-0008-020 through
R-0008-022 and applicable SPEC-0005 and SPEC-0006 requirements.

**[R-0008-029]** Before a migration slice mutates the repository, it must use a
dedicated work branch and record a recovery checkpoint containing the exact
starting commit, worktree state, move or rename manifest, and validation
baseline. User-owned tracked and untracked changes must be preserved and
excluded from slice-owned recovery; if they cannot be isolated safely, the
slice stops before mutation.

If validation fails, the slice stops dependent work, preserves diagnostics,
and reverses only its own changes by applying the documented inverse moves or
by reverting dedicated migration commits. Recovery must restore the recorded
baseline and rerun its applicable checks. It must not rewrite history, use a
destructive worktree reset, overwrite user changes, rebuild or replace an
immutable published artifact, or silently continue from a partial migration.
Release and publication recovery remains governed by SPEC-0005, including
immutable-destination reporting and authorized retry with the same verified
artifact set.

### Alternatives

Alternatives retained for review include keeping responsibility-based roots
without `src/`, grouping all software under a generic products directory,
flattening language workspaces, and using one monolithic conformance target.
The discussed preference is responsibility categories beneath `src/`,
self-contained workspaces, and a small set of coherent profiles rather than
unnecessary abstractions or speculative scaffolding.

## 11. Decision Questions

These labels identify discussion questions, not requirement IDs or work items.

| Question | Unresolved decision |
| --- | --- |
| Q-0008-001 | Decided by R-0008-001 through R-0008-003: responsibility-based software categories under `src/`, lifecycle-based root exceptions, self-contained workspaces, and public cross-artifact boundaries. |
| Q-0008-002 | Decided by R-0008-004: common policy remains in `docs/development/coding-conventions.md`; real language and artifact specializations live beneath `docs/development/conventions/`; applicability is cumulative and path instructions link rather than duplicate policy. |
| Q-0008-003 | Decided by R-0008-005: portable requirements remain implementation-neutral; normative language contracts belong in explicitly scoped numbered implementation specifications; block boundaries and required labels distinguish normative from illustrative examples. |
| Q-0008-004 | Decided by R-0008-006 and R-0008-007: the initial profiles are the portable runtime, local CLI, MCP host, and in-process .NET API; every execution-bearing surface profile requires the runtime baseline; dependencies are cumulative; partial and unqualified conformance claims are prohibited; remote-client profiles are deferred. |
| Q-0008-005 | Decided by R-0008-008: immutable `MAJOR.MINOR` profile versions begin at `1.0`, bind exact authoritative obligations and prerequisite versions, permit only semantics-preserving or non-mandatory minor changes, require major versions for mandatory or prerequisite changes, and never migrate claims automatically. |
| Q-0008-006 | Decided by R-0008-009 and R-0008-010: one versioned closed envelope distinguishes full claims, exhaustive progress, and unsupported targets; declarations bind one exact profile and artifact set; assessment manifests retain requirement-level results and evidence mappings; capabilities are exact and non-partial; failures and unsupported reasons remain explicit. |
| Q-0008-007 | Decided by R-0008-011 through R-0008-015: each immutable profile version carries closed evidence recipes over portable evidence kinds; recipes may use profile-fixed conjunctions and alternatives; exact executable bounds, reproducible build and test identity, explicit unsuccessful outcomes, synthetic data, payload-safe reports, auditable review approvals, and declaration-lifetime evidence availability determine sufficiency. |
| Q-0008-008 | Decided by R-0008-016 through R-0008-018: exact portable marker and waiver payloads use policy-defined native placements; registered language-aware extractors feed one shared rules engine; diagnostics and unsupported placements fail explicitly; fingerprint, reverse-impact, and waiver limits remain intact. |
| Q-0008-009 | Decided by SPEC-0006 R-0006-001, R-0006-002, R-0006-021, R-0006-023, and related architecture requirements: the layer is Entry Points; directories, projects, assemblies, root namespaces, and derived source namespaces use `Qhapaq.EntryPoints.*`; executable and package identities remain separate. |
| Q-0008-010 | Decided by R-0008-019: the .NET workspace owns the independently versioned Roslyn build-tooling package; product integrations and maintained contributor tools own separate responsibility-based workspaces; only supported public boundaries may cross workspaces; and build tooling does not enter runtime dependency closures. |
| Q-0008-011 | Decided by R-0008-020 through R-0008-022 and SPEC-0005 R-0005-034: workspace-native capability commands sit behind maintained root adapters; a root-owned impact graph expands transitively and fails closed; immutable content-addressed evidence is aggregated by digest without rewriting; and one root manifest binds the exact independently versioned public artifacts and evidence promoted as a release. |
| Q-0008-012 | Decided by R-0008-027 through R-0008-029: prerequisite policy, audit, traceability, conformance, and orchestration work precedes migration; Entry Point identities change at existing paths before a separately approved source relocation; each slice uses exact manifests, equivalent before-and-after validation, full consumer impact review, preserved user changes, and non-destructive scoped recovery. |
| Q-0008-013 | Decided by R-0008-023 through R-0008-026 and SPEC-0005 R-0005-035: one authorized maintainer approves exact immutable publication inputs; protected stable or prerelease manifests promote profiles and claims; closed append-only lifecycle states preserve meaning; corrections create new objects; and records and tombstones remain auditable indefinitely. |

The next gate is decision work and human review of scoped requirement drafts.
This document alone is neither specification readiness nor delivery approval.

## 12. Revision History

| Version | Date | Changes |
| --- | --- | --- |
| 0.14 | 2026-10-10 | Defined staged migration prerequisites, Entry Point rename-before-relocation ordering, separate public-change approval, exact before-and-after validation and impact review, preserved user changes, and non-destructive scoped recovery. |
| 0.13 | 2026-10-10 | Defined exact-snapshot publication approval, protected-release promotion, immutable publication records, closed support and claim states, correction and withdrawal behavior, evidence availability, and indefinite audit tombstones. |
| 0.12 | 2026-10-10 | Defined workspace capability contracts and root adapters, fail-closed transitive CI impact selection, immutable digest-bound evidence transport, and coordinated release assembly through one exact root manifest. |
| 0.11 | 2026-10-10 | Assigned the Roslyn generator to the .NET implementation workspace as independently versioned build tooling, kept integrations and maintained contributor tools in separate responsibility-based workspaces, and prohibited private-output and accidental runtime dependencies. |
| 0.10 | 2026-10-10 | Renamed the .NET top layer to Entry Points, adopted matched `Qhapaq.EntryPoints.*` source and compiled identities, and kept executable and package identities separate. |
| 0.9 | 2026-10-10 | Defined portable traceability and waiver payloads, language-native placement registration, language-aware extraction into one shared rules engine, explicit diagnostics, and preserved reverse-impact and waiver limits. |
| 0.8 | 2026-10-10 | Defined profile-version evidence matrices, closed evidence kinds and recipes, bounded and independently reproducible evidence, review and provenance attestations, unsuccessful outcomes, sensitive-data exclusions, and declaration-lifetime evidence availability. |
| 0.7 | 2026-10-10 | Defined the versioned declaration envelope, exact implementation and profile binding, exhaustive assessment manifests, capability dispositions, full-claim and progress rules, unsupported-target reasons, and explicit invalidity behavior. |
| 0.6 | 2026-10-10 | Defined immutable profile-version identities and exact obligation bindings, compatible minor changes, breaking major changes, retirement and supersession behavior, and explicit claim migration. |
| 0.5 | 2026-10-10 | Defined the four initial conformance profiles, cumulative runtime prerequisites, applicability boundaries, and precise claim restrictions while deferring remote-client profiles. |
| 0.4 | 2026-10-10 | Separated portable requirements, explicitly scoped language-specific contracts, non-normative prose, illustrative examples, and normative examples while preserving requirement identifiers and fingerprint boundaries. |
| 0.3 | 2026-10-10 | Assigned common, language-specific, artifact-specific, architectural, and product-policy ownership; defined cumulative applicability, specialization precedence, and path-instruction linkage. |
| 0.2 | 2026-10-10 | Adopted the artifact taxonomy, maintained-software boundary, self-contained workspace rule, root exceptions, cross-artifact dependency rule, and explicit migration exclusion. |
| 0.1 | 2026-10-10 | Recorded multi-language conformance, illustrative examples, source organization, engineering policy separation, and open questions; requirements and work-item creation remain deferred. |
