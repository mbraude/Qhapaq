# Coding Conventions

> **Status:** Initial defaults
> **Applies to:** Qhapaq repository

These conventions define repository engineering defaults that are not fully
expressible through formatters, analyzers, compilers, schemas, or tests.
Objective rules should be automated as the toolchain is introduced.

Normative product behavior remains in [SPEC.md](../../SPEC.md) and numbered
[specifications](../../specs/). When these conventions conflict with a product
specification, the specification wins.

## 1. Requirement levels

- **Required:** the rule must be followed.
- **Default:** follow the rule unless a change documents a justified exception.
- **Recommendation:** preferred when practical.
- **Decision required:** record the choice in a specification or ADR before
  implementation.

Exceptions should be narrow, reviewable, and recorded close to the decision
without weakening unrelated rules.

## 2. General engineering

### Required

- Prefer clarity, correctness, and explicit behavior over cleverness.
- Keep changes focused and preserve existing behavior outside their stated
  scope.
- Validate invalid input at the boundary that has enough context to explain the
  error.
- Surface failures explicitly; do not silently substitute default output.
- Keep public contracts intentional, documented, and covered by compatibility
  tests.
- Use deterministic behavior for canonicalization, generated views, hashes,
  manifests, and conformance data.
- Keep implementation-specific details out of portable contracts.

### Default

- Prefer small types and functions with one clear responsibility.
- Prefer immutable values and read-only views across boundaries.
- Model meaningful states explicitly rather than with unrelated Boolean flags.
- Reuse a shared abstraction only when its callers have the same semantics, not
  merely similar syntax.
- Delete superseded code instead of retaining speculative compatibility layers
  before a public contract exists.

## 3. Repository and project organization

- Language-neutral specifications, schemas, conformance data, and examples stay
  at the repository root.
- .NET production projects belong under `implementations/dotnet/src/`.
- .NET unit and integration projects belong under the corresponding directories
  in `implementations/dotnet/tests/`.
- Primitive operation packages depend only on `Qhapaq.Abstractions` unless an
  accepted specification requires more.
- `Qhapaq.Service.V1`, `Qhapaq.Business`, and `Qhapaq.DAL` must not depend on
  hosting, CLI, or MCP assemblies.
- `Qhapaq.Implementations.Hosting` may integrate with .NET hosting and
  dependency injection.
- `Qhapaq.Implementations.MCP` remains a separately hosted adapter over shared
  application services.
- CLI code may compose implementation packages but is not another reusable
  NuGet package boundary.

Adding or reversing a project dependency is a design change that requires
review against [SPEC-0001](../../specs/0001-core-pipeline-model.md).

### Layering and dependency direction

The .NET implementation follows the architecture specified by
[SPEC-0006](../../specs/0006-dotnet-layered-architecture.md):

```text
Service Implementations -> Service -> Business -> DAL
```

- Production behavior calls only the next lower layer and only through a
  constructor-injected abstraction defined in `Qhapaq.Abstractions`.
- Every production project uses its project name as both `AssemblyName` and
  `RootNamespace`: `Qhapaq.Service.V1`, `Qhapaq.Business`, `Qhapaq.DAL`, or
  `Qhapaq.Implementations.<Implementation>`.
- Service Implementation code must not reference Business or DAL code.
- Service code must not reference DAL code.
- Business code must not reference Service or Service Implementation code.
- DAL code must not reference a higher layer.
- Composition uses Microsoft dependency injection and follows the same
  adjacent-layer direction: Hosting delegates to Service V1, Service V1 to
  Business, and Business to DAL. Each layer registers its own internal
  implementations.
- Service contracts use explicit versioned namespaces. Breaking changes add a
  side-by-side version instead of mutating an existing contract.
- Only supported Service-boundary and operation-authoring contracts are public.
  Other cross-layer contracts and concrete implementations remain internal.
- Architecture tests enforce namespace, visibility, project-reference, and DI
  resolution rules when the initial projects are scaffolded.

Folders and namespaces must make the owning layer unambiguous. Shared code does
not bypass a layer: place it in the lowest layer that owns its semantics or
define a boundary contract when two adjacent layers genuinely collaborate.

## 4. C# and .NET

These defaults apply when the .NET 10 projects are created.

### Language and compiler

- **Required:** enable nullable reference types.
- **Required:** compile production code with warnings treated as errors after
  the initial project scaffold provides a reviewed baseline.
- **Required:** do not suppress a warning without a local explanation or a
  repository-wide documented rationale.
- **Default:** use the latest C# language version supported by the pinned .NET 10
  SDK, rather than an unpinned preview compiler.
- **Default:** use file-scoped namespaces and SDK-style projects.
- **Default:** enable implicit global usings only when the resulting imports are
  predictable and consistent across the solution.

### Naming and layout

- Use `PascalCase` for namespaces, types, methods, properties, events, constants,
  and public members.
- Use `camelCase` for parameters and local variables.
- Use `camelCase` for instance fields; do not prefix field names with an
  underscore.
- Qualify instance field, property, and method references with `this.`.
- Prefix interfaces with `I`.
- Suffix asynchronous methods returning `Task`, `Task<T>`, `ValueTask`, or
  `ValueTask<T>` with `Async`, except language- or framework-mandated members.
- Keep all parameters or arguments on the same line when there are five or
  fewer and the complete declaration or invocation is no longer than 100
  characters.
- When a declaration or invocation exceeds five parameters or 100 characters,
  put every parameter or argument on its own line. Do not partially wrap a
  parameter or argument list.
- Default to one public top-level type per file and match the file name to that
  type.
- Choose names that describe domain behavior; avoid abbreviations that are not
  established Qhapaq vocabulary.

### Types and APIs

- Prefer the narrowest visibility that satisfies the design.
- Prefer records or immutable classes for value-like models.
- Validate constructor invariants and prevent partially valid public objects.
- Use `required` members only when serializers, binders, and callers can enforce
  them consistently; otherwise prefer constructors or factories.
- Do not expose mutable collections. Accept or return interfaces that communicate
  the required semantics, and make ownership clear.
- Avoid `dynamic`, reflection-based activation, and runtime type-name loading in
  product paths.
- Avoid unnecessary `as`, null-forgiving operators, and broad type casts. Fix
  the type model or add a validated guard.
- Add XML documentation comments to every type, field, constructor, and method,
  regardless of visibility. Unit-test types and methods are exempt from this
  documentation requirement.
- Public APIs require XML documentation when their purpose, constraints, failure
  modes, or security behavior are not self-evident.

### Asynchrony and cancellation

- Propagate `CancellationToken` through every asynchronous composition layer.
- Put `CancellationToken` last in public parameter lists and provide a default
  only when cancellation is genuinely optional at that boundary.
- Check cancellation before beginning expensive work or irreversible side
  effects.
- Never use `.Result`, `.Wait()`, or `GetAwaiter().GetResult()` in asynchronous
  product paths.
- Never use `async void` except framework-required event handlers.
- Observe every started task. Concurrent branches must not lose secondary
  failures.
- Do not start background work whose lifetime and failure handling are
  unowned.

### Exceptions and results

- Throw exceptions for exceptional execution failures; use explicit result
  models for expected protocol or validation outcomes where the specification
  defines them.
- Preserve original exception context when translating at a boundary.
- Catch only exceptions that can be handled, enriched, translated, or cleaned
  up meaningfully.
- Do not catch `Exception` merely to log and continue.
- Structured errors must be stable, machine-readable, safe to disclose, and
  mapped consistently across CLI and MCP.

### Dependency injection and time

- Use `Microsoft.Extensions.DependencyInjection` for .NET composition, as
  decided by
  [ADR-0001](../architecture/decisions/0001-use-microsoft-dependency-injection.md).
- Use constructor injection for required collaborators.
- Avoid service-location patterns and hidden ambient mutable state.
- Keep `IServiceCollection`, `IServiceProvider`, and `IServiceScopeFactory` out
  of behavioral Service, Business, DAL, and `Qhapaq.Abstractions` contracts.
- Only executable or hosting boundaries may build or directly access the root
  service provider.
- Each layer explicitly registers its own internal concrete types and delegates
  composition only to the immediately lower layer.
- Do not call `BuildServiceProvider`, resolve services, or invoke product
  behavior during registration.
- Do not use reflection-based assembly scanning for initial Qhapaq service
  registration.
- Enable Microsoft DI build and scope validation in development and tests.
- Inject clocks, randomness, file systems, network clients, or other
  nondeterministic boundaries when behavior must be tested deterministically.
- Define collaborator lifetimes intentionally; do not let singleton services
  capture scoped credentials or request state.

## 5. Portable JSON and schemas

- Use UTF-8 JSON and `System.Text.Json` in the .NET reference implementation
  unless an accepted decision selects otherwise.
- Portable property names use a documented, consistent casing policy.
- Do not serialize CLR assembly names, type names, exception objects, delegates,
  credentials, or implementation-only state.
- Reject unknown document versions.
- Reject unknown fields when accepting them could create ambiguous execution or
  security behavior.
- Keep semantic ordering explicit. Canonicalization must not depend on hash-map
  enumeration, current culture, local time zone, or platform-specific paths.
- Schema references must resolve from versioned repository or package content
  without ambient network access.
- Breaking portable-contract changes require a new document, schema, or
  protocol version and updated conformance vectors.

## 6. Security and privacy

- Treat pipeline documents, imported OpenAPI documents, operation metadata,
  external responses, paths, URLs, and generated prose as untrusted input.
- Never write secrets, tokens, authorization codes, credential references that
  reveal sensitive state, or operation payloads to logs by default.
- Keep execution permission, network permission, and payload disclosure as
  separate policy decisions.
- Validate structure, schemas, configuration, types, capabilities, budgets, and
  policy before starting any operation.
- Bound loops, retries, concurrency, duration, memory-sensitive buffering, and
  output size.
- Normalize and validate archive and bundle paths before file creation; reject
  traversal outside the intended root.
- Use allowlists for implementation activation, connector operations, network
  destinations, and disclosed fields where applicable.
- Do not add cryptography, secret storage, or authentication mechanisms without
  specialist review and an explicit design decision.

## 7. Logging, diagnostics, and observability

- Use structured logging fields rather than interpolating machine-readable
  values into message text.
- Identify pipeline, plan, run, expression, operation, implementation version,
  attempt, branch, and duration where applicable.
- Avoid payload contents in logs, traces, metrics, exception messages, and test
  snapshots unless a test uses synthetic non-sensitive values and the behavior
  is intentional.
- Use stable event names and dimensions with bounded cardinality.
- Diagnostics must be actionable and distinguish validation, binding, policy,
  configuration, cancellation, timeout, and operation failures.
- Human CLI diagnostics go to standard error; machine-readable output remains
  valid on standard output.

## 8. Testing

### Required

- Add tests for changed behavior and for every corrected defect.
- Test observable contracts rather than private implementation details.
- Keep tests deterministic and independent of execution order.
- Use synthetic credentials, endpoints, and payloads.
- Prove rejection paths as well as successful paths.
- Verify cancellation, timeout, concurrency, and multiple-failure behavior when
  the changed code can exercise them.
- Consume shared conformance vectors instead of copying language-neutral cases
  into implementation-specific fixtures.

### Organization

- Unit tests cover isolated algorithms, type compatibility, composition,
  canonicalization, binding, and policy decisions.
- Integration tests cover process, package, hosting, transport, connector, and
  external-boundary behavior.
- Golden files are appropriate for canonical JSON, Mermaid, schemas, manifests,
  and protocol envelopes when diffs are reviewable and regeneration is
  documented.
- Test names describe the condition and expected outcome without encoding
  incidental implementation steps.

## 9. Dependencies and tools

- Prefer the platform and existing dependencies before adding a package.
- Pin SDKs and tools; use lock files where the ecosystem supports them.
- Centralize .NET package versions when the solution is scaffolded.
- Review license, maintenance, provenance, transitive dependency, trimming, and
  security implications before adoption.
- Keep runtime dependencies out of abstraction packages unless they are part of
  that package's public purpose.
- Do not add a dependency solely to avoid a small, well-understood use of the
  standard library.
- Dependency updates must pass the same tests and package-consumer checks as
  source changes.

## 10. Documentation

- Update documentation and examples in the same change as the behavior they
  describe.
- Use repository-relative links in Markdown source.
- Link to the authoritative specification instead of duplicating normative
  rules across guides.
- Label planned behavior clearly; do not present unimplemented functionality as
  available.
- Include language identifiers on fenced code blocks.
- Keep generated reference output separate from curated source and document its
  generation command.
- Use accessible headings, descriptive link text, alt text, and table structure.

## 11. Generated code and artifacts

- Generated files identify their source and generation process when the format
  permits it.
- Never hand-edit generated output when the source can be changed and
  regenerated.
- Generation must be deterministic or clearly identify unavoidable variance.
- Do not commit build output, caches, local profiles, test result directories,
  deployment credentials, or machine-specific IDE state.
- Published packages, manifests, checksums, SBOMs, and provenance must refer to
  the exact same built bytes.

## 12. Decision triggers

Record a specification or ADR before implementing a choice that affects:

- Public API or portable document compatibility.
- Trust boundaries, authentication, authorization, or disclosure.
- Project dependency direction or package boundaries.
- Persistence, remote protocols, deployment topology, or durability.
- Canonicalization, schema draft, error envelope, version derivation, or
  supported platform matrix.
- Build system, test framework, documentation generator, signing, or provenance
  standards when more than a local implementation detail is involved.

Minor refactoring and application of an existing convention do not require a
new decision record.
