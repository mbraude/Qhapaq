# SPEC-0008: Multi-language Conformance and Repository Organization

> **Status:** Draft; artifact taxonomy resolved, remaining decisions unresolved
> **Version:** 0.2
> **Scope:** Future multi-language implementations and repository artifact organization
> **Last updated:** 2026-10-10

## 1. Purpose and Decision Status

This document records the proposed direction for supporting Qhapaq
implementations in multiple languages while accommodating software artifacts
that are not runtime implementations, such as a website, editor integrations,
and development tools.

The artifact taxonomy and source-layout decision in section 4 is resolved in
normative requirement blocks and is awaiting review of the exact specification
snapshot. Other proposals remain subject to decision work and review. This
draft introduces no conformance profiles, additional language runtimes, or
implementation authorization. Discussion and open questions do not receive
requirement IDs.

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
  architecture, including its current Service Implementations layer.
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

## 5. Proposed Engineering Policy Structure

### Common and specialized conventions

The proposed common conventions cover correctness, boundary validation,
portable contracts, security, privacy, determinism, traceability, observable
testing, documentation, generated artifacts, and dependency review.

Language conventions would own naming, syntax, API idioms, compiler settings,
package management, and language-specific tooling. Artifact conventions would
own additional concerns such as website accessibility or editor-extension
lifecycle behavior.

For .NET, potential extraction includes namespace and assembly layout, C#
member organization, nullable types, task and cancellation idioms, Microsoft
dependency injection, serialization-library selection, and NuGet tooling.
Portable behavior would remain in specifications rather than be copied into
each language guide. Path-specific agent instructions would link to the
applicable common and specialized sources.

Exact document locations and policy applicability remain open. Architecture
choices would be recorded in ADRs; detailed engineering rules would remain in
engineering documentation.

### Language-neutral traceability

The proposed portable marker is the payload
`spec: <requirement-id>@<fingerprint>`. Language conventions would define its
placement in native comments or documentation constructs, including verifying
tests. C# XML documentation would not be a universal requirement.

Future tooling could separate marker parsing from comment syntax. Existing
identifier, fingerprint, invariant-placement, reverse-impact, and explicit
waiver rules would remain the baseline pending any reviewed amendment.

### Illustrative language-specific examples

Language-specific examples are useful for explaining portable behavior. Under
the proposed distinction, an example is clearly labeled non-normative and
separated from the requirement block so changing illustrative syntax does not
change the requirement's fingerprint.

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

## 6. Proposed Conformance Model

### Meaning of a profile

A **conformance profile** is a named, versioned set of specification obligations
that supports a defined compatibility claim. It answers what an implementation
promises when it says it conforms to a particular Qhapaq surface.

A profile selects a coherent set of authoritative requirements; it does not
create another executable format or permit a different interpretation of
portable semantics. Profiles would be defined by Qhapaq, not invented by each
implementation to excuse omissions.

Potential profiles include a portable runtime baseline, CLI, MCP, and a .NET
authoring API. These names and boundaries are illustrative only. Dependencies
would be explicit: for example, a local execution CLI profile might require
the runtime baseline, while a remote client could have different obligations.

### Candidate profile contents

A future profile definition could identify:

- Exact identity, version, applicability, and referenced specification snapshot.
- Required requirement IDs and prerequisite profiles.
- Mandatory obligations and explicitly optional capabilities.
- Shared test-vector groups and implementation-specific evidence.
- The compatibility claim permitted by satisfying those obligations.
- Review, publication, support, and compatibility-change rules.

Implementation release versions, profile versions, document versions, protocol
versions, and requirement fingerprints represent different things. Their
relationships remain to be specified rather than assumed to move together.

### Profiles versus capabilities

A profile is a compatibility baseline. A capability identifies a supported
feature or installed facility, such as a particular operation family.

Two runtimes could satisfy the same profile while exposing different operation
catalogs. Capability declarations would not turn mandatory profile obligations
into optional behavior. An implementation missing required cancellation
semantics, for example, would not satisfy a profile that includes them.

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
artifacts, not defined formats. Profile composition, partial-support claims,
evidence sufficiency, and claim publication remain unresolved.

## 7. Proposed Terminology and Architecture Clarification

The word "implementation" currently describes both a language runtime and the
.NET Service Implementations layer. The proposed clarification is to call the
upper .NET layer **Adapters** while retaining its responsibilities and
adjacent-layer dependency direction.

Possible assembly naming approaches include short artifact names such as
`Qhapaq.Hosting`, `Qhapaq.Mcp`, and `Qhapaq.Cli`, or explicitly role-qualified
names such as `Qhapaq.Adapters.Hosting`. No naming option is selected here.

A future decision would amend SPEC-0006 and record the architectural rationale
in an ADR where appropriate. Source relocation and assembly/API renaming are
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

## 9. Proposed Validation, CI, and Release Direction

Each software workspace could expose documented restore, format, lint, build,
test, and packaging entry points appropriate to its ecosystem. Root automation
would orchestrate these rather than assume every source artifact is .NET.

Candidate CI validation groups are portable-contract checks, per-language
builds and tests, shared conformance execution, integration validation, and
website build and preview checks.

Path filtering could avoid unrelated builds while changes to shared contracts
and vectors trigger every affected implementation. Release assembly would
preserve SPEC-0005's consistent source and provenance obligations. Exact
filtering, evidence retention, and release gates remain open.

## 10. Candidate Rollout and Alternatives

This is a discussion sequence, not an approved delivery plan:

1. Resolve terminology, profile boundaries, and source taxonomy.
2. Record accepted requirements and any necessary ADRs.
3. Separate common, language, and artifact conventions.
4. Review mixed portable and .NET requirement blocks and illustrative examples.
5. Define profile declarations and sufficient validation evidence.
6. Plan coordinated source relocation and any independently approved renames.
7. Update affected automation, instructions, documentation, and work plans.
8. Add future artifact workspaces only when their consumers and scope exist.

Migration planning would include validation before and after relocation,
preservation of user changes, and a scoped recovery path if build or discovery
breaks. It would not rely on rewriting history or destructive worktree resets.

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
| Q-0008-002 | Which conventions are common, language-specific, or artifact-specific, and where will they live? |
| Q-0008-003 | How will normative portable requirements, language-specific contracts, and non-normative examples be labeled and separated? |
| Q-0008-004 | Which initial profiles are needed, what is the mandatory runtime baseline, and how do profile dependencies work? |
| Q-0008-005 | How are profile versions tied to exact specification revisions and requirement fingerprints, and what constitutes a compatible change? |
| Q-0008-006 | What capability and conformance declaration formats are needed, and how are partial support and unsupported behavior reported? |
| Q-0008-007 | Which shared vectors, language-specific tests, reviews, and release evidence are sufficient for each conformance claim? |
| Q-0008-008 | What language-native traceability placements and checker support are needed without weakening existing traceability and waiver rules? |
| Q-0008-009 | Should the .NET Service Implementations layer be renamed to Adapters, and should assembly names change independently? |
| Q-0008-010 | Who owns the Roslyn generator and future integrations, and what public dependency boundaries apply? |
| Q-0008-011 | How will artifact-local commands, CI impact selection, conformance reports, and consistent releases be orchestrated? |
| Q-0008-012 | What migration order, prerequisite amendments, ADRs, validation gates, and recovery steps are required? |
| Q-0008-013 | What review and approval process permits publication of profiles and implementation conformance claims? |

The next gate is decision work and human review of scoped requirement drafts.
This document alone is neither specification readiness nor delivery approval.

## 12. Revision History

| Version | Date | Changes |
| --- | --- | --- |
| 0.2 | 2026-10-10 | Adopted the artifact taxonomy, maintained-software boundary, self-contained workspace rule, root exceptions, cross-artifact dependency rule, and explicit migration exclusion. |
| 0.1 | 2026-10-10 | Recorded multi-language conformance, illustrative examples, source organization, engineering policy separation, and open questions; requirements and work-item creation remain deferred. |
