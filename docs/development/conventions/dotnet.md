# .NET Conventions

> **Applies to:** maintained .NET implementation and common-library projects and their tests

This guide supplements the
[common coding conventions](../coding-conventions.md). The common policy
remains applicable; this guide owns only .NET-specific conventions. Portable
product behavior remains in the specifications, and architecture decisions
remain in ADRs.

The traceability placements here define permitted C# constructs, not checker
support. See [R-0008-016](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
for the language-support condition.

## Repository and project organization

- Until the approved R-0008-027 relocation, existing .NET implementation
  projects remain under `implementations/dotnet/src/` with tests under
  `implementations/dotnet/tests/`. Their target workspace paths are
  `src/implementations/dotnet/src/` and `src/implementations/dotnet/tests/`.
- Shared .NET library production projects belong under
  `src/common/dotnet/src/`; their tests belong under
  `src/common/dotnet/tests/`.
- Primitive operation packages depend only on `Qhapaq.Abstractions` unless an
  accepted specification requires more.
- `Qhapaq.Service.V1`, `Qhapaq.Business`, and `Qhapaq.DAL` must not depend on
  hosting, CLI, or MCP assemblies.
- `Qhapaq.Portable.Validation` is referenced by Business at runtime and by the
  generator only as a build-time dependency; no other runtime layer references
  it.
- `Qhapaq.EntryPoints.Hosting` may integrate with .NET hosting and
  dependency injection.
- `Qhapaq.EntryPoints.MCP` remains a separately hosted adapter over shared
  application services.
- CLI code may compose implementation packages but is not another reusable
  NuGet package boundary.

Adding or reversing a project dependency is a design change that requires
review against [SPEC-0001](../../../specs/0001-core-pipeline-model.md).

### Layering and dependency direction

The .NET implementation follows the architecture specified by
[SPEC-0006](../../../specs/0006-dotnet-layered-architecture.md):

```text
Entry Points -> Service -> Business -> DAL
```

- Production behavior calls only the next lower runtime layer through a
  constructor-injected abstraction defined in `Qhapaq.Abstractions`. Business
  may also call `Qhapaq.Portable.Validation` directly for the shared algorithms
  required by SPEC-0006 R-0006-041.
- Every production project uses its project name as both `AssemblyName` and
  `RootNamespace`: `Qhapaq.Portable.Validation`, `Qhapaq.Service.V1`,
  `Qhapaq.Business`, `Qhapaq.DAL`, or `Qhapaq.EntryPoints.<EntryPoint>`.
- Entry Point code must not reference Business or DAL code.
- Service code must not reference DAL code.
- Business code must not reference Service or Entry Point code.
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
- A registry-visible operation and its authoritative descriptor use
  `<OperationTypeName>.cs` and `<OperationTypeName>.descriptor.json` with exact
  case-sensitive basename matching in the same physical source directory.

Folders and namespaces must make the owning layer unambiguous. Shared code does
not bypass a layer: place it in the lowest layer that owns its semantics or
define a boundary contract when two adjacent layers genuinely collaborate.
`Qhapaq.Portable.Validation` is a shared support assembly in the
`src/common/dotnet/` workspace, not another runtime layer; its source is under
`src/common/dotnet/src/` and its tests under `src/common/dotnet/tests/`. It
contains only the deterministic algorithms shared by Business and the
build-time generator as specified by R-0006-041. It must not depend on runtime
layers or generator tooling.

### Production feature folders and namespaces

- **Required:** every handwritten C# source file in a production project uses
  the namespace obtained by appending each source-directory segment below the
  project directory to the project's `RootNamespace`, preserving exact casing.
  A handwritten source file in the project directory uses the
  `RootNamespace` itself.
- **Required:** no handwritten-source exception may omit, add, or rename a
  folder-derived namespace segment. Organizational grouping therefore uses a
  real namespace boundary rather than a namespace-neutral folder.
- Representative mappings include:

  | Project-relative source path | Namespace |
  | --- | --- |
  | `Qhapaq.Abstractions/Operations/` | `Qhapaq.Abstractions.Operations` |
  | `Qhapaq.Service.V1/DependencyInjection/` | `Qhapaq.Service.V1.DependencyInjection` |
  | `Qhapaq.Business/Validation/` | `Qhapaq.Business.Validation` |
  | `Qhapaq.DAL/Operations/` | `Qhapaq.DAL.Operations` |
  | `Qhapaq.EntryPoints.Hosting/DependencyInjection/` | `Qhapaq.EntryPoints.Hosting.DependencyInjection` |

The rule applies to handwritten production source physically located beneath
the current `implementations/dotnet/src/` path until relocation, its target
`src/implementations/dotnet/src/` path, and `src/common/dotnet/src/`. SDK- and
compiler-generated files outside those project source directories are not
handwritten source and are excluded.
Qhapaq-generated source follows the generated namespace contract in its
governing specification; generator tests must verify that contract separately.

Architecture tests must enumerate handwritten production C# files, derive the
expected namespace from the owning project's `RootNamespace` and relative
directory, and fail for a missing or non-exact declaration. Generated-source
contract tests remain separate so this file-layout rule does not silently
replace a specified generated namespace.

## Traceability placements

The portable reference and waiver payloads and shared checker rules are in the
[common specification traceability policy](../coding-conventions.md#3-specification-traceability).
The native C# placements below are governed by
[R-0008-016 through R-0008-018](../../../specs/0008-multi-language-conformance-and-repository-organization.md#language-neutral-traceability)
and [ADR-0003](../../architecture/decisions/0003-enforce-specification-traceability.md).
The commit classification and trailer rules remain in the common policy and
[ADR-0004](../../architecture/decisions/0004-classify-changes-and-trace-through-commits.md).

For C#, place a reference in a `//` comment immediately before the enforcing
statement or block. Add a short explanation after an em dash when the
connection is not obvious. When a whole member is the enforcement, such as a
dedicated validator, place it in the member's `<remarks>` instead. Place a test
reference in a `//` comment immediately before the test method.

```csharp
public async Task<Document> InvokeAsync(Document input, CancellationToken cancellationToken)
{
    // spec: R-0001-012@44aa01 — cancel the sibling before awaiting it so no failure is lost.
    ...
}
```

Waivers use the same registered native constructs and attachment scopes as
references. In C#, a member's `<remarks>` covers that member, and a `//`
comment covers the statement, block, or test method immediately following it.

```csharp
// spec-waive: untraced-behavior — the retry only absorbs transient HTTP 503 from the local
// test double and does not change observable behavior; see issue #42.
```

## C# and .NET

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

- Use `PascalCase` for namespaces, types, methods, properties, events, and
  public members other than constants.
- Use `camelCase` for parameters and local variables.
- Use `camelCase` for instance fields; do not prefix field names with an
  underscore.
- Qualify instance field, property, and method references with `this.`.
- **Required:** prefix interface names with `I`, followed by a `PascalCase`
  descriptive name; for example, `IMyInterface`.
- **Required:** prefix enumeration names with `E`, followed by a `PascalCase`
  descriptive name; for example, `EMyEnumeration`.
- **Required:** suffix methods that return `Task`, `Task<T>`, `ValueTask`, or
  `ValueTask<T>` with `Async`, except members whose names are mandated by the
  language, an implemented interface, an overridden member, or a framework.
- **Required:** do not declare `async void` methods, including event handlers.
  Asynchronous methods must return `Task`, `Task<T>`, `ValueTask`, or
  `ValueTask<T>`. When a synchronous framework callback must initiate
  asynchronous work, use a framework-supported task-returning callback or
  explicitly coordinate the returned task through an owning component; do not
  discard it.
- Keep all parameters or arguments on the same line when there are five or
  fewer and the complete declaration or invocation is no longer than 100
  characters.
- When a declaration or invocation exceeds five parameters or 100 characters,
  put every parameter or argument on its own line. Do not partially wrap a
  parameter or argument list.
- **Required:** define each class in its own file and match the file name to the
  class name, regardless of the class's accessibility or whether it is
  top-level or nested. Partial classes are the only exception to the
  one-class-to-one-file mapping.
- Name the primary partial-class file `<ClassName>.cs`. Name each additional
  partial-class file `<ClassName>.<Section>.cs`, where `<Section>` is a concise,
  unique `PascalCase` description of the declarations defined by that part.
  For example, define `Class1` in `Class1.cs` and a nested class named `Inner`
  in `Class1.Inner.cs`; both files declare `Class1` as `partial`.
- Do not use partial classes merely to avoid organizing a large class. Each
  additional part must have a cohesive purpose that its `<Section>` suffix
  communicates.
- Choose names that describe domain behavior; avoid abbreviations that are not
  established Qhapaq vocabulary.

### Class member layout

The following rules apply independently within every class declaration,
including each part of a partial class.

- **Required:** wrap each nonempty member category in a `#region` whose name
  matches the category below. Omit empty regions.
- Place member categories in this order:
  1. `Fields`
  2. `Constructors`
  3. `Disposal`
  4. `Properties`
  5. `Events`
  6. `Methods`
  7. `Explicit Interface Implementations`
  8. `Nested Types`
  9. `Static Methods`
- The `Disposal` region contains the finalizer, `IDisposable.Dispose`,
  `IAsyncDisposable.DisposeAsync`, and local disposal helpers such as
  `Dispose(bool isDisposing)`. Within this region, place the finalizer first,
  followed by the public disposal methods, explicit disposal interface
  implementations, and then local disposal helpers. This lifecycle-specific
  placement takes precedence over the general method-placement rules. Omit
  the region when the class has no finalization or disposal members.
- Sort fields first by accessibility in this order: `public`, `internal`,
  `protected internal`, `protected`, `private protected`, and `private`.
  Within each accessibility group, sort fields by category in this order:
  constants, static read-only fields, other static fields, instance read-only
  fields, and other instance fields. Sort fields alphabetically within the
  same category.
- Name constants with `UPPER_SNAKE_CASE`, for example
  `THIS_IS_A_CONSTANT`.
- Place a static constructor first in the `Constructors` region. Sort instance
  constructors by accessibility using the field accessibility order. Within
  the same accessibility, place the parameterless constructor first, then sort
  by parameter count and parameter-type signature.
- Sort properties first by accessibility using the field accessibility order,
  then alphabetically by property name. Apply the property's declared
  accessibility; a more restrictive accessor does not create a separate
  ordering group. Treat indexers as properties and place them after named
  properties of the same accessibility.
- Put events in the `Events` region. Sort them first by accessibility using the
  field accessibility order, then alphabetically by event name.
- Put instance methods in the `Methods` region. Sort them first by
  accessibility using the field accessibility order, then alphabetically by
  method name. Keep overloads together and sort overloads by parameter count
  and parameter-type signature.
- Put explicit interface implementations in the `Explicit Interface
  Implementations` region and sort them alphabetically by fully qualified
  interface member name. Explicit interface implementations do not declare an
  accessibility modifier; for example,
  `void IOperation.MyMethod(...)`, not
  `public void IOperation.MyMethod(...)`.
- Put static methods in the final `Static Methods` region. Sort them first by
  accessibility using the field accessibility order, then alphabetically by
  method name, with overloads ordered as for instance methods. Place operators
  after named static methods and sort them by operator token.
- Put nested type declarations in the `Nested Types` region. Keep a nested
  class in its own partial-class file as described above. Within the nested
  class itself, apply this class member layout recursively.

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
- Follow the
  [.NET `ConfigureAwait` guidance](https://devblogs.microsoft.com/dotnet/configureawait-faq/)
  according to the owning project:
  - App-model-agnostic library code in `Qhapaq.Abstractions`,
    `Qhapaq.Service.V*`, `Qhapaq.Business`, and `Qhapaq.DAL` must use
    `ConfigureAwait(false)` on every applicable `await`.
  - Entry Point code in `Qhapaq.EntryPoints.*` must use plain
    `await` and must not use `ConfigureAwait(false)`. These adapters own
    application and transport context.
  - Unit and integration tests must use plain `await`. Test frameworks such as
    xUnit may provide a synchronization context.
  - A library API that intentionally invokes caller-provided code on the
    captured context may use `ConfigureAwait(true)` only with a local comment
    explaining the exception and focused tests for that behavior.
- Apply the selected `ConfigureAwait` behavior to every applicable `await` in a
  method, not only its first await. An already-completed awaitable may continue
  synchronously without changing context.
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
  [ADR-0001](../../architecture/decisions/0001-use-microsoft-dependency-injection.md).
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

### Dependencies and tooling

- Centralize .NET package versions when the solution is scaffolded.

## .NET JSON implementation

- Use UTF-8 JSON and `System.Text.Json` in the .NET reference implementation
  unless an accepted decision selects otherwise.
- Portable property names, schema, and canonicalization requirements remain in
  the [common JSON policy](../coding-conventions.md#6-portable-json-and-schemas).

## Test artifact consumption

Apply the .NET organization requirements in
[R-0007-346](../../../specs/0007-portable-pipeline-definitions-and-binding.md#net-organization-and-portable-validation),
the portable vector semantics in
[R-0007-347](../../../specs/0007-portable-pipeline-definitions-and-binding.md#20-testing-and-conformance),
and the consumer boundaries in
[R-0006-031](../../../specs/0006-dotnet-layered-architecture.md#11-enforcement-and-testing).
Reported capability groups follow
[R-0001-072](../../../specs/0001-core-pipeline-model.md#16-compatibility-conformance-and-versioning).

The versioned vector envelopes and their `expected` values in the repository's
`conformance/` tree are authoritative. .NET tests consume those files rather
than maintaining duplicate language-neutral cases. Test projects copy the
required canonical files into test output while preserving their relative
paths; harnesses locate them relative to the test output directory, not the
process working directory. Selection uses exact suite IDs and versions and
declared capability groups, with deterministic ordering. Test output reports
the exact suite versions and capabilities exercised; it does not resolve an
implicit `latest`.

Ordinary conformance runs are read-only. Offline golden regeneration uses the
canonical vector inputs and emits proposed expected-result changes as a
reviewable diff outside the authoritative `conformance/` tree. Accepting a
proposal requires review against the governing requirements; the reviewed
expected values are then updated in the canonical vector envelopes. A .NET
fixture or generated copy is never an alternate golden source.

Package-consumer tests are integration tests. They pack the public Qhapaq
packages into a temporary local feed and build a fresh external-style consumer
project against those packages, without project references or access to
implementation internals. The scenarios prove that a third-party operation
library needs only `Qhapaq.Abstractions` and that a third-party entry point can
consume Service V1 without Business or DAL contracts. Keep these tests
separate from architecture tests, which enforce repository-internal project
references, visibility, namespaces, and composition rules.
