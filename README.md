# Qhapaq

Qhapaq is an AI-forward system for defining, composing, validating, and
executing typed pipelines. Pipelines use a language-neutral, versioned JSON
format and can be consumed through a portable CLI or Model Context Protocol
(MCP) server. The .NET 10 implementation is the v1 reference runtime.

## Project status

Qhapaq is specification-first and currently in repository bootstrap. The
product model, security boundaries, extension model, generated invocation
skills, and delivery strategy are documented. Source projects, schemas,
conformance vectors, automation, and user-facing documentation are the next
implementation stages.

The living project specification is [SPEC.md](SPEC.md). Focused specifications
are indexed in [specs/README.md](specs/README.md).

## Repository map

| Path | Purpose |
| --- | --- |
| [specs/](specs/) | Normative feature and behavior specifications. |
| [schemas/](schemas/) | Language-neutral schemas for portable documents and protocols. |
| [conformance/](conformance/) | Shared valid, invalid, and behavioral compatibility vectors. |
| [implementations/](implementations/) | Language-specific reference and future implementations. |
| [examples/](examples/) | Small executable examples of supported scenarios. |
| [docs/](docs/) | Architecture, development, guide, reference, and website source documentation. |
| [scripts/](scripts/) | Maintained local and CI automation entry points. |
| [build/](build/) | Build orchestration configuration. |
| [tools/](tools/) | Project-owned development utilities and tool configuration. |
| [.vscode/](.vscode/) | Shared Visual Studio Code extension recommendations and workspace configuration. |
| [.agents/skills/](.agents/skills/) | Portable, reviewed skills for repository work. |
| [.ai/](.ai/) | Reusable prompts and evaluations for AI-assisted development. |
| [AGENTS.md](AGENTS.md) | Repository-wide working agreements for AI agents. |
| [Coding conventions](docs/development/coding-conventions.md) | Detailed engineering requirements and defaults. |

Additional GitHub workflows, community files, and language-specific projects
will be added only when their behavior and consumers are defined.

## Editor setup

Visual Studio Code is the recommended editor for Qhapaq development. When the
repository is opened, install the workspace's recommended extensions for C#,
EditorConfig, Markdown, YAML, GitHub Actions, and container development.

The recommendations intentionally omit optional AI assistants, account-specific
tools, and extensions that are not required by the repository's selected
technologies. Shared settings, tasks, launch profiles, and MCP configuration
will be added only when their commands and trust boundaries are defined.

## Intended distribution

Qhapaq v1 is expected to provide:

- Four .NET packages: `Qhapaq.Abstractions`, `Qhapaq`, `Qhapaq.Hosting`, and
  `Qhapaq.Mcp`.
- Self-contained CLI executables for the supported platform matrix.
- A container image for the CLI and separately hosted MCP server.
- Versioned schemas and conformance data.
- A static public website with stable, prerelease, and edge downloads.

These artifacts do not exist yet. Do not treat the current repository as a
usable release.

## Contributing

Contribution, coding, testing, security, and contributor-rights policies are
still being established. Until they are published, use small reviewed changes,
do not commit secrets or private data, and follow the decisions in
[SPEC.md](SPEC.md).

## License

The repository is source-available under the
[PolyForm Internal Use License 1.0.0](LICENSE). Review the license before using
or modifying the software. Separate commercial terms and trademark guidance
will be documented after legal review.
