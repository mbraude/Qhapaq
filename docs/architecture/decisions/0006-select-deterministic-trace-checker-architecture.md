# ADR-0006: Select Deterministic Trace-checker Architecture

> **Status:** Proposed
> **Date:** 2026-10-15
> **Related:** [ADR-0003](0003-enforce-specification-traceability.md),
> [ADR-0004](0004-classify-changes-and-trace-through-commits.md)

## Context

[SPEC-0008 R-0008-016 through R-0008-018](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
require native syntax extraction for each registered language and one shared
engine for portable marker, fingerprint, placement, reverse-impact, and waiver
rules. The checker must also be a required validation group under
[R-0008-021](../../../specs/0008-multi-language-conformance-and-repository-organization.md#9-validation-ci-and-release-orchestration).

The repository's shared workflow helpers use Python, while the maintained
implementation is .NET and already pins its SDK and NuGet dependencies. The
repository's established .NET workspace name is `dotnet`; `C#` identifies the
language parsed by Roslyn, not the workspace directory convention. One parser
or runtime should not own both language-specific syntax and portable semantic
rules.

## Decision

### Ownership and boundaries

- The trace checker is an independently maintained development tool under
  `src/tools/trace-checker/`, independent of product runtime packages. Its
  shared rules engine is a Python workspace with production code under
  `src/tools/trace-checker/python/src/` and tests under
  `src/tools/trace-checker/python/tests/`.
- Each language extractor is a language-native tool component. The initial C#
  extractor is a .NET command-line tool in
  `src/tools/trace-checker/dotnet/`, using Roslyn
  (`Microsoft.CodeAnalysis.CSharp`) to parse C# syntax and the registered
  constructs from the applicable language policy. Its production code is under
  `src/tools/trace-checker/dotnet/src/` and tests are under
  `src/tools/trace-checker/dotnet/tests/`.
- I-0008-007 may plan the Python rules engine and tests, plus the .NET extractor
  and tests, in those workspaces. Each workspace owns its applicable pinned
  toolchain, dependency manifests, lock files, and `bin/` build output.
  Repository-wide ignore rules already exclude workspace `bin/` and `obj/`
  directories. Tool documentation records setup, commands, inputs, outputs,
  and dependencies.
- The common trace-check workflow helper lives with the repository's shared
  Python workflow scripts under `.agents/scripts/`. The
  `spec-trace-check` skill invokes that generic helper without embedding
  language-specific build or invocation logic. The helper builds and invokes
  the registered native checker for the language being checked, then passes
  its normalized facts to the shared Python rules engine.
- Language-native checkers follow one versioned, machine-readable JSON
  command-line contract. Each extractor returns only normalized extraction
  facts: marker payload, source span, attachment target, and production-or-test
  classification. The helper routes those facts to the Python shared rules
  engine, which exclusively owns portable validation. Extractors may report
  extraction failures, but they do not implement portable semantic rules.
- The Python engine exclusively owns marker grammar, requirement resolution,
  current fingerprints, placement validation, reverse-impact checks, waiver
  scope, and stable checker diagnostics. Extractors must not duplicate or
  override those rules.
- Extractor registration and evidence that each extractor matches its approved
  language policy belong to I-0008-007. A language remains unsupported until
  both its placement policy and matching extractor are registered, as required
  by R-0008-016.

### Dependencies and toolchains

- The Python engine uses the standard library for portable validation. Its
  supported Python runtime and any development/test dependencies are pinned
  and locked in the tool workspace. Its package or runnable build output, when
  built, goes in that workspace's ignored `bin/` directory.
- The C# extractor uses a pinned .NET SDK and a pinned
  `Microsoft.CodeAnalysis.CSharp` package in its own tool workspace. NuGet
  restore uses that workspace's lock file. Neither the extractor nor its
  private parser dependencies enter a Qhapaq runtime dependency closure.
- The Python engine does not use Tree-sitter or another language grammar
  package to parse C#; future languages add their own native extractor and
  parser dependencies without moving language syntax into the shared engine.

### Invocation and validation

- I-0008-007 owns the documented trace-check command and the Python-engine and
  .NET-extractor build/test commands. The shared helper exposes one stable
  deterministic command for running the complete checker:
  `python .agents/scripts/trace_check.py`. The `spec-trace-check` skill uses
  this command for its deterministic gate. For each checked language, the
  helper builds and runs the matching native extractor into its workspace's
  ignored `bin/` output, validates the extractor's JSON contract, then invokes
  the shared Python engine. Root CI invokes the same command. Tool
  documentation records the command and the separate Python-engine and
  .NET-extractor test commands.
- The `spec-trace-check` workflow invokes that deterministic command once and
  may add the existing AI-led semantic review, which is not a substitute for
  the checker. `build-and-test` invokes `spec-trace-check` before its build and
  unit-test steps, so the checker is not run twice in that workflow.
- Root CI invokes the same checker through its validation adapter. Skills are
  convenient local entry points, not enforcement boundaries.
- The checker is a separate validation group in the build-and-test sequence,
  not itself a unit or integration test. Unit and integration tests separately
  validate the shared engine, extractor behavior, and their normalized
  interface using fixtures.
- I-0008-009 owns root adapters, CI impact selection, and required CI status
  integration. The trace-check group must not be suppressible by path
  filtering; missing or ambiguous mappings fail closed as specified by
  R-0008-021. The checker is a validation input to release workflows, not a
  publisher or release action.

## Consequences and Tradeoffs

- Python keeps the shared portable rules engine aligned with repository
  workflow tooling, while Roslyn gives the C# extractor native syntax
  information and attachment boundaries. The `dotnet` workspace name follows
  repository convention; `C#` remains the language parsed by its extractor.
- Separating the `.agents/scripts/` workflow helper from the independently
  maintained `src/tools/trace-checker/` workspaces keeps skill/CI orchestration
  generic without moving tool source out of its governed workspace. The helper
  owns build and language dispatch; the Python engine owns cross-language
  portable semantics.
- The split introduces a cross-process interface and two pinned toolchains.
  Their protocol, errors, versions, and fixture coverage must be explicit and
  tested; an unavailable or failed extractor must fail the check.
- Additional language support requires a separately reviewed native
  extractor, parser dependency, registration, and policy-match evidence.
- The tool's exact files, package versions, entry-point syntax, fixtures, and
  root integration manifests are detailed in the approved I-0008-007 and
  I-0008-009 implementation plans, not implemented by this decision.

## Alternatives

- **One .NET checker for both extraction and semantic validation:** rejected
  because it makes the shared engine .NET-specific and does not align the
  contributor-facing validation tool with the repository's Python workflow.
- **Python parser for C# syntax:** rejected in favor of the runtime-native
  Roslyn extractor; syntax extraction and placement attachment remain the
  responsibility of the language-specific layer.
- **`csharp/` as the .NET workspace directory:** rejected in favor of
  `dotnet/`, matching the repository's established workspace naming
  convention. `C#` remains appropriate when naming the parser or language.
- **One grammar package for all languages:** rejected because language syntax
  support should be registered and versioned with each language-native
  extractor rather than bundled into the shared semantic engine.
- **Skills as the enforcement mechanism:** rejected because skills are
  workflow guidance. The standalone command and required CI status remain the
  deterministic enforcement points.
