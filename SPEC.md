# Qhapaq Project Specification

> **Status:** Draft  
> **Version:** 0.7
> **Last updated:** 2026-10-04

## 1. Purpose

Qhapaq is an AI-forward pipeline system for defining, composing, validating, and
executing typed pipelines. Its name literally means "a thing of importance,
prominence, or greatness." Symbolically, it represents the roads that connected
an entire civilization.

The project embodies that symbolism by connecting small, independently useful
operations into dependable orchestrations. Any language or system can consume
Qhapaq through its CLI or Model Context Protocol (MCP) surface. .NET applications
also receive an enhanced in-process, strongly typed library API. Pipelines use a
language-neutral JSON format so the implementation language is not part of their
portable contract.

This document is the living, top-level specification for the repository. It
records project goals, repository conventions, proposed structure, and decisions
that affect the project as a whole.

### 1.1 Product Model

The language-neutral model treats an operation as an asynchronous mapping from a
declared input schema to a declared output schema. The .NET reference
implementation expresses that abstraction as:

```csharp
public interface IOperation<TInput, TOutput>
{
    Task<TOutput> ExecuteAsync(
        TInput input,
        CancellationToken cancellationToken = default);
}
```

Operations compose without losing this abstraction. Sequential composition feeds
one operation's output into the next. Parallel composition gives two operations
the same input and combines their outputs. Decorators preserve an operation's
input and output types while adding behavior such as retries, caching, batching,
timeouts, logging, or metrics. Conditional and bounded-loop combinators provide
controlled flow without turning the initial release into a durable workflow
engine.

The .NET 10 reference implementation executes strongly typed CLR values
in-process. JSON is used at pipeline, persistence, CLI, and MCP boundaries, not
between every operation. A canonical JSON definition binds through a
host-controlled operation registry into a validated, immutable execution plan.
Generated Mermaid flowcharts visualize that definition but are not executable
source.

The initial architecture and execution semantics are specified in
[`specs/0001-core-pipeline-model.md`](specs/0001-core-pipeline-model.md).
Operation catalogs, extensions, host profiles, and authentication are specified
in
[`specs/0002-operation-catalogs-and-host-configuration.md`](specs/0002-operation-catalogs-and-host-configuration.md).
Deferred but intentional product directions, including remote credential stores
and gRPC hosting, are tracked in
[`specs/0003-product-evolution-roadmap.md`](specs/0003-product-evolution-roadmap.md).
AI-assisted connection onboarding and its local consent boundary are specified
in
[`specs/0004-ai-assisted-connections.md`](specs/0004-ai-assisted-connections.md).
Continuous integration, release publication, and website delivery are specified
in
[`specs/0005-build-release-and-website-delivery.md`](specs/0005-build-release-and-website-delivery.md).
The initial .NET layer boundaries, dependency direction, visibility, service
versioning, and component plan are specified in
[`specs/0006-dotnet-layered-architecture.md`](specs/0006-dotnet-layered-architecture.md).

### 1.2 Initial Scope Boundaries

Qhapaq v1 will:

- Provide a C# API and a .NET 10 in-process execution engine.
- Provide a language-neutral CLI contract and separately distributed executable
  for supported operating systems and architectures.
- Support code-defined and canonical JSON-defined pipelines.
- Support sequential, parallel, decorated, conditional, and bounded-loop
  composition.
- Persist pipeline definitions and cache bound execution plans.
- Generate Mermaid flowcharts from validated definitions.
- Expose authoring, discovery, validation, visualization, and policy-gated
  execution through a separately hosted MCP server.
- Generate portable pipeline invocation skills that let AI systems execute an
  exact validated pipeline with schema-validated boundary inputs through the
  normative CLI or MCP contract.
- Publish conformance schemas and test vectors independently of the .NET
  implementation.
- Let users build an operation catalog from built-ins, explicitly selected
  OpenAPI operations, and explicitly installed precompiled .NET extensions.
- Keep portable project catalogs separate from trusted user host profiles and
  externally resolved credentials.
- Let MCP clients propose resource connections while requiring an independent
  trusted local consent flow to approve and apply configuration changes.
- Deny disclosure of operation payloads to MCP clients by default, independently
  from permission to execute an operation.

Qhapaq v1 will not:

- Resume a pipeline run after process failure.
- Provide distributed scheduling, durable timers, exactly-once effects,
  compensation, or transactional rollback.
- Load arbitrary CLR types or assemblies named by a pipeline document.
- Treat YAML, XML, Markdown, or Mermaid as executable pipeline formats.
- Emit C#, IL, or assemblies as its pipeline compilation mechanism.
- Promise additional in-process language runtimes in v1.

### 1.3 Portability and Implementations

The CLI and MCP contracts, canonical JSON model, execution semantics, and
conformance data are language-neutral and normative. The .NET implementation is
the v1 reference implementation, but it is not the semantic authority when it
conflicts with those specifications.

Users must not need a system-wide .NET installation to use the CLI. Releases
should include self-contained executables for the supported platform matrix and
a container image. Native AOT may be used where compatible, but portability
depends on explicitly published operating-system and architecture targets rather
than a claim that one binary runs everywhere.

If another implementation is added, it must declare its conformance level and
pass the shared language-neutral test vectors. A new implementation belongs
under `implementations/<language>/`; it must not fork the document format or
redefine common execution semantics.

### 1.4 Product Evolution

V1 intentionally establishes abstractions for capabilities that are important
but not part of its local single-user delivery:

- Remote secret and credential providers such as Azure Key Vault.
- A Qhapaq host callable locally or remotely over gRPC.
- Remote operation providers that expose primitives to the engine over gRPC.
- Hosted and eventually tenant-scoped configuration, identity, and policy.

These are deferred deliverables, not rejected use cases. V1 contracts must avoid
embedding local filesystem paths, process identity, or .NET-specific transport
assumptions into portable pipeline and catalog documents.

### 1.5 Public Project Website

Qhapaq will have a public static website hosted on Azure Static Web Apps. The
site will advertise the project, explain its purpose and capabilities, show
representative use cases, and direct users to installation, documentation,
source, packages, and community resources.

The website is a product and documentation surface, not a Qhapaq execution,
configuration, credential, or control-plane component. Pull requests receive
isolated preview deployments, and reviewed changes merged to `main` deploy
automatically to production. Its information architecture, visual design,
accessibility requirements, framework, domain, and analytics remain separate
design decisions. Build and deployment behavior is defined in
[`specs/0005-build-release-and-website-delivery.md`](specs/0005-build-release-and-website-delivery.md).

### 1.6 Licensing, Commercial Rights, and Brand

Qhapaq is source-available rather than OSI open source. Publicly released source
is licensed under the PolyForm Internal Use License 1.0.0, which permits internal
business use and modification but does not permit distribution or sublicensing.

The project owner reserves the right to offer separate commercial licenses for
distribution, embedding, OEM use, hosted or managed services, support, and other
uses not granted by the public license. Commercial terms will be documented
separately and reviewed by qualified legal counsel before they are offered.

The software license does not grant rights to the Qhapaq name, logos, service
identity, or compatibility marks. A separate trademark and brand-use policy will
define permitted nominative references and protect official products and hosted
services.

External contributions require contributor terms that preserve the project
owner's ability to distribute contributions under the public license and
separate commercial licenses. The contributor agreement or assignment model
must be selected with legal review before accepting substantive outside
contributions.

## 2. Repository Goals

The repository should be:

- **Source-available forward:** easy to understand, evaluate, use internally,
  contribute to, and govern while preserving commercial and hosting rights.
- **AI forward:** structured so AI coding agents can work safely and consistently.
- **Specification driven:** important behavior and decisions are documented before
  or alongside implementation.
- **Automation friendly:** formatting, validation, testing, packaging, and release
  processes should be reproducible.
- **Secure by default:** dependencies, contributions, releases, and credentials
  should follow least-privilege and supply-chain security practices.
- **Technology conscious, not technology bound:** the reference implementation
  may use platform-specific strengths without making portable contracts depend
  on .NET.

## 3. Guiding Principles

1. **Clarity over cleverness.**
2. **Small, reviewable, reversible changes.**
3. **Documentation and tests are part of the product.**
4. **Humans remain accountable for AI-assisted contributions.**
5. **Automate repeatable checks and make failures actionable.**
6. **Keep public interfaces intentional and backward compatibility explicit.**
7. **Prefer open standards and portable tooling where practical.**
8. **Never commit secrets, generated credentials, or private user data.**

## 4. Proposed Repository Structure

The following is the target structure. Directories and files should be added when
they have real content rather than being committed as empty placeholders.

```text
Qhapaq/
|-- .agents/
|   `-- skills/
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |-- agents/
|   |-- instructions/
|   |-- prompts/
|   |-- workflows/
|   |-- CODEOWNERS
|   |-- SUPPORT.md
|   |-- dependabot.yml
|   |-- copilot-instructions.md
|   `-- pull_request_template.md
|-- .ai/
|   |-- README.md
|   |-- prompts/
|   `-- evaluations/
|-- .vscode/
|   |-- extensions.json
|   |-- mcp.json
|   `-- settings.json
|-- build/
|-- conformance/
|-- docs/
|   |-- architecture/
|   |   |-- decisions/
|   |   `-- diagrams/
|   |-- development/
|   |-- guides/
|   |-- reference/
|   `-- wiki/
|-- examples/
|-- implementations/
|   `-- dotnet/
|       |-- src/
|       `-- tests/
|           |-- integration/
|           `-- unit/
|-- schemas/
|-- scripts/
|-- specs/
|-- tools/
|-- .editorconfig
|-- .gitattributes
|-- .gitignore
|-- AGENTS.md
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- LICENSING.md
|-- NOTICE
|-- README.md
|-- RELEASE.md
|-- SECURITY.md
|-- TRADEMARKS.md
`-- SPEC.md
```

### 4.1 Root Files

| Path | Purpose |
| --- | --- |
| `README.md` | Project overview, quick start, status, and links to deeper documentation. |
| `SPEC.md` | This living repository and project specification. |
| `AGENTS.md` | Tool-neutral instructions and constraints for AI coding agents. |
| `CONTRIBUTING.md` | Contributor setup, workflow, quality, documentation, and AI-use requirements. |
| `SECURITY.md` | Supported versions, secure development expectations, and private vulnerability reporting. |
| `.gitignore` | Ignores selected for the eventual language, tools, editors, and OS artifacts. |
| `.editorconfig` | Cross-editor whitespace, encoding, and newline conventions. |
| `.gitattributes` | Line-ending, diff, linguist, and generated-file behavior. |
| `LICENSE` | Canonical PolyForm Internal Use License 1.0.0 terms. |
| `LICENSING.md` | Plain-language licensing model and commercial-license contact path. |
| `NOTICE` | Attributions and notices when required by dependencies or the license. |
| `CODE_OF_CONDUCT.md` | Community participation expectations and enforcement process. |
| `CHANGELOG.md` | User-visible changes, preferably following Keep a Changelog. |
| `RELEASE.md` | Versioning, packaging, signing, and release procedures. |
| `TRADEMARKS.md` | Qhapaq name, logo, compatibility-mark, and brand-use policy. |

### 4.2 Source and Quality

| Path | Purpose |
| --- | --- |
| `implementations/dotnet/src/` | .NET reference implementation, CLI, and MCP source. |
| `implementations/dotnet/tests/unit/` | Fast, isolated tests for .NET behavior. |
| `implementations/dotnet/tests/integration/` | Tests across .NET components and external boundaries. |
| `schemas/` | Normative language-neutral document and protocol schemas. |
| `conformance/` | Shared valid, invalid, and execution test vectors for every implementation. |
| `examples/` | Small, executable examples that demonstrate supported use cases. |
| `scripts/` | Maintained developer and CI automation entry points. |
| `tools/` | Tool configuration or project-owned development utilities. |
| `build/` | Build orchestration files only; generated output remains ignored. |

Language-specific conventions remain within each implementation directory.
Normative schemas, conformance vectors, and specifications remain at the
repository root so no implementation owns the portable contract.

### 4.3 Specifications and Documentation

| Path | Purpose |
| --- | --- |
| `specs/` | Version-controlled feature, protocol, and behavior specifications. |
| `docs/architecture/` | Current architecture and system context. |
| `docs/architecture/decisions/` | Numbered Architecture Decision Records (ADRs). |
| `docs/development/` | Coding conventions, testing practices, and development toolchain guidance. |
| `docs/guides/` | Contributor and user task-oriented guidance. |
| `docs/reference/` | Generated or curated technical reference material. |
| `docs/wiki/` | Canonical wiki source that can be published or synchronized. |

Documentation stored in this repository is canonical. If a GitHub Wiki is used,
it should be generated or synchronized from `docs/wiki/` so knowledge does not
live only in a separate wiki repository.

### 4.4 GitHub and Community

The `.github/` directory will contain:

- GitHub-specific support and repository metadata.
- Issue forms and pull request templates.
- Ownership and review rules.
- Dependency update configuration.
- Continuous integration, release, documentation, and deployment workflows.
- GitHub Copilot repository instructions, path-specific instructions, custom
  agents, and prompts.

Project-wide contribution and security policies remain at the repository root so
they are prominent and usable independently of GitHub. GitHub-specific files
should adapt or link to canonical project guidance rather than duplicate it.

Workflows should initially be limited to checks the project can execute
reliably. Deployment workflows should be introduced only after deployment
targets and environments are specified.

### 4.5 AI Collaboration

AI guidance should be layered rather than tied to one vendor:

- `AGENTS.md` defines repository-wide, tool-neutral working agreements.
- `.agents/skills/<skill-name>/SKILL.md` defines portable, self-contained skills;
  a skill may also contain bounded `scripts/`, `references/`, or `assets/`.
- `.github/copilot-instructions.md` adapts those agreements for GitHub Copilot.
- `.github/instructions/` contains focused GitHub Copilot instructions for
  languages, domains, or repository areas.
- `.github/agents/` contains GitHub Copilot custom agent definitions.
- `.github/prompts/` contains GitHub Copilot prompt files.
- `.ai/prompts/` contains reusable, reviewed prompt templates for recurring work.
- `.ai/evaluations/` contains test cases or rubrics that measure AI-generated
  changes against project expectations.

Skills should implement repeatable capabilities rather than hold general
repository policy. General policy belongs in `AGENTS.md`, `CONTRIBUTING.md`, or
the relevant document under `docs/development/`.

Qhapaq-generated pipeline invocation skills are product artifacts, not
repository-collaboration policy. They contain or reference a canonical pipeline
definition and delegate validation, binding, policy enforcement, and execution
to a conforming Qhapaq host. They must not become an additional executable
pipeline format or grant authority beyond the active host policy. The portable
invocation-skill profile is defined in
[`specs/0001-core-pipeline-model.md`](specs/0001-core-pipeline-model.md).

Any tool-specific instruction file, including proposed `.dm` files, must have a
documented consumer and format before it is added. Tool-neutral guidance should
remain authoritative to avoid conflicting instructions.

AI-assisted changes are held to the same review, test, security, licensing, and
attribution standards as human-authored changes. Contributors must not provide
AI tools with secrets, private data, or third-party code they are not permitted
to share.

### 4.6 MCP Integration

Model Context Protocol integration has separate locations for configuration and
implementation:

- `.vscode/mcp.json` contains safe, portable MCP server definitions used by
  VS Code. It must not contain credentials or machine-specific private values.
- User-specific or private MCP configuration remains outside the repository.
- `tools/mcp/<server-name>/` contains MCP servers owned as development tooling by
  this project.
- A first-class, published Qhapaq MCP product should use the repository's future
  implementation convention instead of being hidden under `tools/`.

Committed MCP configuration should reference environment variables, interactive
inputs, or an approved external secret store for sensitive values. Every
configured server must document its purpose, trust boundary, required access,
and setup process.

### 4.7 Coding Conventions

Coding standards should have three complementary layers:

1. Formatters, linters, compiler settings, and tests enforce objective rules.
2. `docs/development/coding-conventions.md` documents rules and rationale that
   cannot be expressed by tooling.
3. `AGENTS.md` and applicable tool-specific instructions summarize the
   operational requirements for AI-assisted changes.

The detailed coding conventions are authoritative. AI instruction files should
link to them rather than copy the complete text.

### 4.8 Instruction Authority

When guidance overlaps, the following precedence applies:

1. Applicable law, the project license, and the security policy.
2. This project specification.
3. `CONTRIBUTING.md` and documented engineering policies.
4. `AGENTS.md`.
5. Applicable path-specific or tool-specific AI instructions.
6. Individual prompts and skills.

A prompt, skill, MCP server, or tool-specific configuration must not silently
override higher-authority project guidance.

## 5. Automation Strategy

Automation is event-driven and implemented with GitHub Actions. Repository
scripts remain the authoritative entry points for build, test, package, and
site-generation behavior so contributors can reproduce CI locally.

### 5.1 Pull Requests

Every pull request targeting `main` runs required formatting, build, test,
conformance, package smoke, documentation, secret, dependency, and license
checks. Website changes receive an isolated Azure Static Web Apps preview that
is removed when the pull request closes. Pull-request workflows do not receive
package-publishing or production-deployment credentials.

### 5.2 Main and Edge

Every reviewed merge or other protected push to `main` runs a release-shaped
build, publishes a public `edge` build identified by its exact commit, updates
the moving edge download pointer and container tag, and deploys the production
website. Edge artifacts are explicitly unstable and are not pushed to the stable
nuget.org feed.

### 5.3 Stable Releases

Stable and prerelease publication is triggered only by protected Semantic
Version tags. The tag is the explicit release decision; the subsequent verified
publication is automatic. A release builds one artifact set and publishes those
exact bytes as NuGet packages, self-contained CLI archives, a container image,
schemas, conformance data, checksums, SBOMs, provenance, and release notes.
Published stable artifacts are immutable.

Stable releases are readiness-driven during v1 rather than forced onto a fixed
calendar. Maintainers review readiness at least monthly. Nightly and weekly
scheduled workflows provide deeper platform, integration, dependency, license,
and security assurance but do not publish stable releases.

Protected GitHub environments, least-privilege workflow permissions, trusted
publishing, and workload identity federation are used where supported. A
narrowly scoped, rotated deployment token may be used where Azure Static Web
Apps requires it. All channels preserve provenance and an audit trail and have
documented recovery behavior. The normative model is defined in
[`specs/0005-build-release-and-website-delivery.md`](specs/0005-build-release-and-website-delivery.md).

## 6. Specification Process

Substantial features should begin with a document in `specs/` containing:

1. Status and owners.
2. Problem statement.
3. Goals and non-goals.
4. User-facing behavior and examples.
5. Proposed design and public API.
6. Security, privacy, accessibility, and compatibility considerations.
7. Testing and observability strategy.
8. Alternatives considered.
9. Rollout, migration, and rollback plans when applicable.
10. Unresolved questions.

Specifications should use a stable identifier such as
`specs/0001-short-title.md`. Cross-cutting technical decisions should use ADRs
under `docs/architecture/decisions/`.

## 7. Branching, Changes, and Releases

The initial recommendation is:

- Use a protected default branch named `main`.
- Develop through short-lived branches and pull requests.
- Require automated checks and at least one approving review.
- Prefer squash merges to keep the early history focused.
- Use Conventional Commits only if release automation will consume them.
- Adopt Semantic Versioning once a public API exists.
- Treat breaking changes as explicit design decisions.
- Let automation maintain a release proposal and changelog when the project has
  enough user-visible changes; publishing still begins only from a protected
  version tag.

These conventions should be revisited before the first public release.

## 8. Initial Artifact Plan

### Now

- [x] Create the root project specification.
- [x] Select C# and .NET 10 as the initial implementation language and runtime.
- [x] Define the library's initial problem statement and public API goals.
- [x] Select canonical JSON definitions and generated Mermaid visualization.
- [x] Define non-durable, in-process execution as the v1 execution model.
- [x] Define CLI and MCP as the language-neutral v1 consumption surfaces.
- [x] Define built-ins, OpenAPI connectors, and trusted precompiled extensions
      as the v1 operation sources.
- [x] Separate portable project catalogs from trusted user profiles and secret
      providers.
- [x] Document remote credential stores and both gRPC hosting models as
      intentional post-v1 evolution paths.
- [x] Define AI-assisted connection planning with trusted local approval.
- [x] Separate resource execution permission from MCP payload-disclosure
      permission.
- [x] Define the initial `Qhapaq.Abstractions`, `Qhapaq`, `Qhapaq.Hosting`,
      and `Qhapaq.Mcp` package boundaries.
- [x] Define the initial .NET layered architecture, dependency direction,
      visibility rules, and component plan.
- [x] Record the future Azure-hosted static project website as a product surface.
- [x] Define the event-driven CI, edge, stable-release, and website delivery
      model.
- [x] Select PolyForm Internal Use License 1.0.0 as the public source-available
      license.

### After the Technology Decision

- [x] Add focused `.gitignore`, `.editorconfig`, and `.gitattributes` files.
- [x] Create the source, test, example, and documentation directories in the
      conventions of the selected ecosystem.
- [ ] Define the normative CLI contract and conformance levels.
- [ ] Add language-neutral schemas and initial conformance vectors.
- [ ] Define the portable pipeline invocation-skill bundle schema and generate
      it through the normative CLI and MCP surfaces.
- [ ] Define the initial authentication-provider set and protected token-cache
      behavior.
- [ ] Add local build, formatting, linting, and test commands.
- [x] Add `README.md` and initial repository-wide and path-specific AI
      instructions.
- [ ] Add contribution guidelines and community health files.
- [ ] Add commercial-licensing, trademark, and contributor-rights policies
      after legal review.
- [x] Add coding conventions under `docs/development/`.
- [ ] Add toolchain guidance under `docs/development/`.
- [x] Add only those MCP configurations and skills with defined consumers and
      documented trust boundaries.
- [ ] Add required pull request CI, branch protection, and dependency
      automation.
- [ ] Add Azure Static Web Apps pull-request previews and automatic production
      deployment from `main`.
- [ ] Add release-shaped `main` builds and a public edge download channel.

### Before the First Public Release

- [ ] Document the support and compatibility policy.
- [ ] Add protected-tag packaging, trusted publishing, provenance, signing or
      attestation, and release automation.
- [ ] Add security reporting and vulnerability response procedures.
- [ ] Confirm license compatibility and required attributions.
- [ ] Complete legal review of the public license, commercial terms, trademark
      policy, and contributor agreement.
- [ ] Publish generated API reference and user guides.
- [ ] Specify, create, and publish the static project website on Azure.

## 9. Open Decisions

| ID | Decision | Status |
| --- | --- | --- |
| D-001 | What problem and use cases will Qhapaq address? | Decided: typed, composable in-process pipelines for code and AI-authored orchestration |
| D-002 | Which implementation language and runtimes will be supported? | Decided: .NET 10 reference implementation; CLI and MCP remain language-neutral |
| D-003 | What package and distribution formats will be provided? | Decided: four NuGet packages, self-contained CLI executables, a container image, and canonical JSON |
| D-004 | Which public source license will the project use? | Decided: PolyForm Internal Use License 1.0.0, with separate commercial licensing and trademark policy |
| D-005 | Which operating systems and architectures will be supported? | Open |
| D-006 | Which build and documentation systems will be used? | Partial: GitHub Actions orchestrates CI/CD and calls repository scripts; the .NET build orchestration and static-site generator remain open |
| D-007 | Will Qhapaq deploy a service, publish only a library, or do both? | Decided: publish .NET libraries, a portable CLI, and an optional separately hosted MCP server |
| D-008 | Which AI tools, skill conventions, and instruction formats, including `.dm`, must be supported? | Partial: MCP and a portable `SKILL.md`-based pipeline invocation profile are product surfaces; other repository-agent conventions remain open |
| D-009 | What governance and maintainer model will apply? | Open |
| D-010 | Which MCP servers, trust boundaries, and configuration formats will be supported? | Partial: project-owned server with host-controlled discovery and policy-gated execution |
| D-011 | What is the canonical declarative format? | Decided: versioned JSON with generated Mermaid visualization |
| D-012 | What does pipeline compilation mean? | Decided: bind to a validated immutable in-memory execution plan |
| D-013 | Are pipeline runs durable? | Decided: definitions are persistable; v1 runs are non-durable |
| D-014 | How will non-.NET systems consume Qhapaq? | Decided: normative CLI and MCP contracts |
| D-015 | How will future implementations remain compatible? | Decided: shared specifications, schemas, conformance levels, and test vectors |
| D-016 | How can users extend the operation catalog without runtime compilation? | Decided: built-ins, declarative OpenAPI connectors, and explicitly installed precompiled .NET extensions |
| D-017 | Where is configuration stored? | Decided: portable project catalogs plus explicit trusted user profiles and external secret providers |
| D-018 | What deployment and identity model does v1 target? | Decided: local single-user CLI and MCP, preserving hosted abstractions |
| D-019 | Which deferred product evolutions must v1 preserve? | Decided: remote credential stores, gRPC Qhapaq hosts, remote gRPC operation providers, and hosted identity/configuration |
| D-020 | How can AI systems help configure connections safely? | Decided: MCP proposes immutable setup plans; a trusted local broker obtains explicit user approval and applies them |
| D-021 | May configured internal-resource outputs be returned to AI clients? | Decided: payload disclosure through MCP is denied by default and must be explicitly allowed per connection or operation |
| D-022 | Will Qhapaq have a public project website? | Partial: Azure Static Web Apps hosts automatic pull-request previews and production deployment from `main`; design, framework, domain, and analytics remain open |
| D-023 | How can AI systems package and repeat a pipeline invocation? | Decided: generate a portable invocation-skill bundle that embeds or exactly references canonical JSON, uses boundary input as its parameter surface, pins identity/version/digest, and delegates all authority to the host |
| D-024 | What events publish builds and the website? | Decided: pull requests validate and preview; protected `main` pushes publish edge and production website updates; protected Semantic Version tags publish immutable releases |
| D-025 | What release cadence applies? | Decided: event-driven edge delivery on every successful `main` change, readiness-driven stable releases with at least monthly review, and scheduled assurance without scheduled stable publication |
| D-026 | How are .NET implementation layers separated and versioned? | Decided: layer-aligned `Qhapaq.Service.V1`, `Qhapaq.Business`, `Qhapaq.DAL`, and `Qhapaq.Implementations.*` assemblies call only the next lower layer through DI contracts from `Qhapaq.Abstractions`; only supported Service and operation-authoring contracts are public, and physical assemblies remain bundled into a smaller NuGet package surface |
| D-027 | Which dependency-injection framework and composition model does the .NET implementation use? | Decided: Microsoft dependency injection with explicit, layer-owned registration delegated only to the immediately lower layer; behavioral contracts and components remain container-independent |

## 10. Definition of Repository Readiness

The repository is ready for implementation when:

- The initial use cases, scope, and non-goals are documented.
- The NuGet package boundaries, operating-system support, and license are
  selected.
- The CLI contract, portable schemas, and initial conformance vectors are
  specified.
- The core pipeline specification's remaining public API and document-schema
  questions are resolved.
- A contributor can run formatting, linting, build, and tests with documented
  commands.
- Pull requests execute the same required checks in CI.
- Contribution, conduct, support, security, and AI-use expectations are clear.
- No required workflow depends on undocumented local state or committed secrets.

## 11. Revision History

| Version | Date | Summary |
| --- | --- | --- |
| 0.7 | 2026-10-04 | Selected Microsoft dependency injection and adjacent-layer, layer-owned composition. |
| 0.6 | 2026-10-04 | Assigned layer-aligned assembly and root namespace names while preserving the smaller public NuGet package surface. |
| 0.5 | 2026-10-04 | Defined the .NET layered architecture, versioned Service boundary, DI direction, visibility rules, and initial component plan. |
| 0.4 | 2026-10-04 | Recorded the documented, evaluated repository skill surface as complete. |
| 0.3 | 2026-10-04 | Defined automated CI, edge builds, immutable releases, and website delivery. |
| 0.2 | 2026-10-04 | Added portable pipeline invocation skills as a v1 product capability. |
| 0.1 | 2026-10-04 | Established the initial repository vision, layout, and decision backlog. |
