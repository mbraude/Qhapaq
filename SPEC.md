# Qhapaq Project Specification

> **Status:** Draft  
> **Version:** 0.1  
> **Last updated:** 2026-10-04

## 1. Purpose

Qhapaq is a software library whose name literally means "a thing of importance,
prominence, or greatness." Symbolically, it represents the roads that connected
an entire civilization.

The project should embody that symbolism by providing dependable connections
between systems, people, and ideas. Its exact technical scope will be refined
through future specifications and architectural decisions.

This document is the living, top-level specification for the repository. It
records project goals, repository conventions, proposed structure, and decisions
that affect the project as a whole.

## 2. Repository Goals

The repository should be:

- **Open-source forward:** easy to understand, adopt, contribute to, and govern.
- **AI forward:** structured so AI coding agents can work safely and consistently.
- **Specification driven:** important behavior and decisions are documented before
  or alongside implementation.
- **Automation friendly:** formatting, validation, testing, packaging, and release
  processes should be reproducible.
- **Secure by default:** dependencies, contributions, releases, and credentials
  should follow least-privilege and supply-chain security practices.
- **Technology conscious, not technology bound:** repository conventions should
  remain useful while the implementation language and platform are undecided.

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
|-- docs/
|   |-- architecture/
|   |   |-- decisions/
|   |   `-- diagrams/
|   |-- development/
|   |-- guides/
|   |-- reference/
|   `-- wiki/
|-- examples/
|-- scripts/
|-- specs/
|-- src/
|-- tests/
|   |-- integration/
|   |-- unit/
|   `-- fixtures/
|-- tools/
|   `-- mcp/
|-- .editorconfig
|-- .gitattributes
|-- .gitignore
|-- AGENTS.md
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- NOTICE
|-- README.md
|-- RELEASE.md
|-- SECURITY.md
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
| `LICENSE` | The project's approved open-source license. |
| `NOTICE` | Attributions and notices when required by dependencies or the license. |
| `CODE_OF_CONDUCT.md` | Community participation expectations and enforcement process. |
| `CHANGELOG.md` | User-visible changes, preferably following Keep a Changelog. |
| `RELEASE.md` | Versioning, packaging, signing, and release procedures. |

### 4.2 Source and Quality

| Path | Purpose |
| --- | --- |
| `src/` | Library implementation, organized around its public API and domain. |
| `tests/unit/` | Fast, isolated tests for implementation behavior. |
| `tests/integration/` | Tests across components or external boundaries. |
| `tests/fixtures/` | Stable, non-sensitive test inputs and expected outputs. |
| `examples/` | Small, executable examples that demonstrate supported use cases. |
| `scripts/` | Maintained developer and CI automation entry points. |
| `tools/` | Tool configuration or project-owned development utilities. |
| `build/` | Build orchestration files only; generated output remains ignored. |

The final layout may adopt language-specific conventions instead of these generic
directories. That decision should be documented before implementation begins.

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
  package or workspace convention instead of being hidden under `tools/`.

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

Automation will be introduced in stages.

### Stage 1: Repository Health

- Validate formatting and linting.
- Run unit tests and static/type analysis.
- Check links and documentation conventions.
- Scan committed content for secrets.
- Perform dependency and license review.

### Stage 2: Packaging

- Build reproducible packages.
- Generate a software bill of materials where appropriate.
- Sign release artifacts and publish checksums.
- Verify packages in a clean environment.

### Stage 3: Release and Deployment

- Use protected GitHub environments for deployments.
- Prefer workload identity federation over stored cloud credentials.
- Require explicit approvals for production changes.
- Preserve provenance and an audit trail for released artifacts.
- Provide a documented rollback or recovery path.

CI should run on pull requests and protected branches. Releases should be
triggered from immutable version tags or an auditable release workflow, not from
unreviewed branch pushes.

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

These conventions should be revisited before the first public release.

## 8. Initial Artifact Plan

### Now

- [x] Create the root project specification.
- [ ] Select the implementation language, supported runtimes, and package format.
- [ ] Define the library's initial problem statement and public API goals.
- [ ] Select an open-source license.

### After the Technology Decision

- [ ] Add focused `.gitignore`, `.editorconfig`, and `.gitattributes` files.
- [ ] Create the source, test, example, and documentation directories in the
      conventions of the selected ecosystem.
- [ ] Add local build, formatting, linting, and test commands.
- [ ] Add `README.md`, contribution guidelines, community health files, and AI
      instructions.
- [ ] Add coding conventions and toolchain guidance under `docs/development/`.
- [ ] Add only those MCP configurations and skills with defined consumers and
      documented trust boundaries.
- [ ] Add pull request CI and dependency automation.

### Before the First Public Release

- [ ] Document the support and compatibility policy.
- [ ] Add packaging, provenance, signing, and release automation.
- [ ] Add security reporting and vulnerability response procedures.
- [ ] Confirm license compatibility and required attributions.
- [ ] Publish generated API reference and user guides.

## 9. Open Decisions

| ID | Decision | Status |
| --- | --- | --- |
| D-001 | What problem and use cases will Qhapaq address? | Open |
| D-002 | Which implementation language and runtimes will be supported? | Open |
| D-003 | What package and distribution formats will be provided? | Open |
| D-004 | Which open-source license will the project use? | Open |
| D-005 | Which operating systems and architectures will be supported? | Open |
| D-006 | Which build and documentation systems will be used? | Open |
| D-007 | Will Qhapaq deploy a service, publish only a library, or do both? | Open |
| D-008 | Which AI tools, skill conventions, and instruction formats, including `.dm`, must be supported? | Open |
| D-009 | What governance and maintainer model will apply? | Open |
| D-010 | Which MCP servers, trust boundaries, and configuration formats will be supported? | Open |

## 10. Definition of Repository Readiness

The repository is ready for implementation when:

- The initial use cases, scope, and non-goals are documented.
- The language, runtime support policy, package format, and license are selected.
- A contributor can run formatting, linting, build, and tests with documented
  commands.
- Pull requests execute the same required checks in CI.
- Contribution, conduct, support, security, and AI-use expectations are clear.
- No required workflow depends on undocumented local state or committed secrets.

## 11. Revision History

| Version | Date | Summary |
| --- | --- | --- |
| 0.1 | 2026-10-04 | Established the initial repository vision, layout, and decision backlog. |
