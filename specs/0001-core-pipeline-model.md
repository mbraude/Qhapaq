# SPEC-0001: Core Pipeline Model

> **Status:** Draft  
> **Target:** Qhapaq v1  
> **Last updated:** 2026-10-04

## 1. Summary

Qhapaq is a language-neutral pipeline model with a .NET reference implementation
for building larger typed operations from small typed primitives. Pipelines can
be constructed through the enhanced C# API or represented as canonical,
versioned JSON. The same definition model supports validation, Mermaid
visualization, persistence, AI-assisted authoring, CLI use, and policy-gated MCP
execution.

The v1 reference implementation targets .NET 10. CLI and MCP contracts are
language-neutral. Pipeline definitions are persistable, but individual runs are
non-durable and cannot resume after process failure.

## 2. Goals

- Make small operation implementations easy to author, test, and reuse.
- Preserve native type safety throughout an implementation's in-process
  execution.
- Compose operations sequentially, concurrently, conditionally, and iteratively.
- Add cross-cutting behavior through type-preserving decorators.
- Give declarative pipelines deterministic validation and binding behavior.
- Make operations and pipeline shapes discoverable to AI systems.
- Let non-.NET systems use Qhapaq through stable CLI and MCP contracts.
- Separate safe authoring and validation from privileged execution.
- Keep the core independent of any particular dependency injection, logging, or
  MCP hosting implementation.

## 3. Non-goals

Qhapaq v1 is not:

- A durable or distributed workflow engine.
- A scheduler, message broker, or state store.
- An exactly-once execution system.
- A transaction or compensation framework.
- A general-purpose programming language.
- A mechanism for loading arbitrary code named by untrusted documents.
- A multi-language execution runtime.

YAML, XML, Markdown, and Mermaid are not executable definition formats in v1.
Generated Mermaid is a view of a canonical JSON definition.

Remote Qhapaq hosts and remote operation providers are deferred rather than
rejected. Their intended evolution and the abstractions v1 must preserve are
described in
[`0003-product-evolution-roadmap.md`](0003-product-evolution-roadmap.md).

## 4. Core Abstraction

Normatively, an operation is an asynchronous mapping from a value matching its
declared input schema to a value matching its declared output schema. It accepts
a cancellation signal, may have documented side effects, and either produces a
valid output or reports failure.

The .NET reference implementation binds that abstraction to:

```csharp
public interface IOperation<TInput, TOutput>
{
    Task<TOutput> ExecuteAsync(
        TInput input,
        CancellationToken cancellationToken = default);
}
```

An implementation must:

- Honor cancellation when it can do so safely.
- Return a task that completes only when its work has completed.
- Propagate failures rather than returning a success-shaped default value.
- Document externally visible side effects and idempotency expectations.
- Be safe for the lifetime with which its host registers it.

This .NET interface intentionally has no general-purpose execution-context
parameter.
Operations may receive collaborators such as loggers, clients, clocks, or caches
through normal construction and dependency injection. Runtime tracing should use
standard .NET diagnostics facilities rather than ambient Qhapaq service access.

## 5. Composition Algebra

### 5.1 Sequential Composition

Given:

```text
first:  IOperation<A, B>
second: IOperation<B, C>
```

sequential composition produces:

```text
IOperation<A, C>
```

The second operation starts only after the first completes successfully. A
failure or cancellation from the first prevents the second from starting. The
runtime does not implicitly convert incompatible intermediate schemas or native
types.

The initial binary implementation is named `CompoundOperation<TInput,
TIntermediate, TOutput>`. Fluent APIs and declarative syntax may flatten longer
sequences for readability, but their behavior is equivalent to binary
composition.

### 5.2 Parallel Composition

Given:

```text
left:  IOperation<A, B>
right: IOperation<A, C>
```

parallel composition produces:

```text
IOperation<A, ParallelResult<B, C>>
```

Both branches receive the same input and may execute concurrently. The result
has stable `Left` and `Right` members rather than relying on serialized CLR tuple
metadata.

If either branch fails, the composed operation must signal cancellation to the
other branch, observe both branch tasks, and report every branch failure in a
Qhapaq parallel-execution exception. Signaling cancellation does not guarantee
that a branch or its side effects stop immediately.

The initial primitive is binary. Larger fan-outs are equivalent to recursive
binary composition, while authoring APIs may present a flattened named-branch
view.

### 5.3 Decorators

A decorator transforms:

```text
IOperation<A, B> -> IOperation<A, B>
```

Decorators can add retries, timeouts, caching, batching, concurrency limits,
logging, tracing, metrics, or other policies without changing the wrapped
operation's public types.

Decorator order is semantically significant. For example, retrying a timeout is
different from applying one timeout across all attempts. Code and JSON must
preserve explicit nesting order.

Retry configuration uses `maxAttempts`, including the initial attempt, rather
than the ambiguous term `maxRetries`. Cancellation is not retryable by default.

### 5.4 Conditional Composition

A conditional combines:

```text
predicate: IOperation<A, bool>
whenTrue:  IOperation<A, B>
whenFalse: IOperation<A, B>
```

and produces `IOperation<A, B>`.

The predicate runs once for each invocation. Only the selected branch executes,
and it receives the original input. Both branches must have compatible document
output schemas and implementation-native output types.

### 5.5 Bounded Loops

A bounded while-loop combines:

```text
condition: IOperation<TState, bool>
body:      IOperation<TState, TState>
```

and produces `IOperation<TState, TState>`.

The condition is evaluated before each iteration. The output of one body
invocation becomes the state for the next condition evaluation. Every loop must
declare a positive `maxIterations`. If the condition remains true after the
maximum number of body invocations, execution fails with a loop-limit exception
instead of returning a potentially incomplete result.

Arbitrary graph cycles and unbounded loops are invalid in v1.

## 6. Pipeline Representations and Lifecycle

A pipeline has three representations:

1. **Definition:** canonical, versioned JSON suitable for interchange,
   persistence, signing, hashing, review, and AI authoring.
2. **Execution plan:** an immutable in-memory object produced by resolving
   registry entries, validating types and policy, and precomputing execution
   structure.
3. **Run:** one non-durable invocation of a bound plan with a typed or
   deserialized boundary input.

The definition is the source of truth. An execution plan is a derived cache and
must not be treated as a portable artifact. In v1, "compile" means binding a
definition into this validated execution plan. It does not mean generating C#,
IL, or an assembly.

Plan binding must fail before execution when a referenced operation or decorator
is unavailable, its exact requested version is unavailable, connected types are
incompatible, configuration is invalid, the structure is invalid, or host
policy rejects a capability.

## 7. Canonical JSON Model

Every document must declare:

- A Qhapaq document format identifier and version.
- A stable pipeline identifier and pipeline version.
- Boundary input and output schema references or inline schemas.
- One root composition expression.
- Exact operation and decorator identifiers and versions.
- Configuration values or host-resolved references.
- Optional human-readable metadata that does not affect execution semantics.

The model is an expression tree whose structural forms include:

- Primitive operation reference.
- Sequence.
- Named parallel branches.
- Decorator wrapping one inner expression.
- Conditional with a predicate and two branches.
- Bounded loop with a condition, body, and maximum iteration count.

The normative JSON Schema and canonicalization rules remain to be defined.
Canonicalization must make semantically relevant ordering explicit so hashes,
signatures, caches, and reviews are deterministic.

Pipeline documents must not contain:

- Implementation type names used for activation, including assembly-qualified
  CLR type names.
- Executable source code or scripts.
- Inline credentials or secret values.
- Implicit type conversions.
- Unbounded loops.
- References that select an unspecified "latest" implementation version.

## 8. Operation Registry

A host-controlled registry is the only mechanism by which a declarative
operation reference becomes executable code. A registry descriptor includes:

- Stable operation or decorator identifier.
- Exact implementation version.
- Human-readable name and description.
- Portable input, output, and configuration JSON Schemas.
- Declared capabilities and side-effect characteristics.
- Documentation and examples intended for humans and AI systems.

An implementation binding additionally associates the portable descriptor with
native input and output types and factory information held by the host. Those
details are not supplied by the pipeline document.

Operation IDs are portable names, not implementation type names. A host decides
which descriptors and implementations to register. Portable binding requires
compatible declared schemas. The .NET binding additionally requires CLR type
assignability.

Values remain native runtime values between in-process operations; the .NET
reference implementation uses strongly typed CLR objects. Serialization occurs
at CLI, MCP, pipeline, and persistence boundaries and in explicit serialization
operations. Qhapaq does not automatically reshape or convert mismatched
intermediate values; a pipeline must reference an explicit mapping operation.

The v1 reference host can populate its registry from built-in operations,
declarative OpenAPI connectors, and explicitly installed precompiled .NET
extensions. Catalog and host configuration semantics are defined in
[`0002-operation-catalogs-and-host-configuration.md`](0002-operation-catalogs-and-host-configuration.md).

## 9. Execution Semantics

- Each pipeline invocation is independent unless registered operations explicitly
  share state.
- Cancellation flows through every combinator and decorator.
- Operation exceptions propagate unless an explicit decorator handles them.
- Qhapaq emits diagnostics but does not silently convert failures to default
  outputs.
- Concurrent branches do not imply transactional isolation or rollback.
- Hosts may impose budgets for duration, attempts, iterations, concurrency,
  memory, output size, or operation capabilities.
- Definition validation does not prove that side-effecting execution is safe.

Execution is at-least-once at the operation level when retry decorators are
used. Authors must account for idempotency or supply deduplication behavior when
retrying side effects.

## 10. Mermaid Visualization

Qhapaq generates Mermaid flowcharts from validated pipeline definitions.
Visualization is deterministic for a given canonical definition and shows:

- Operation identifiers and versions.
- Sequential and parallel relationships.
- Decorator nesting.
- Conditional branches.
- Loop boundaries and maximum iteration counts.

Mermaid is an explanatory projection. Editing generated Mermaid does not modify
or define a pipeline.

## 11. CLI Surface

The CLI is a normative cross-language process boundary. It supports operation
discovery, validation, Mermaid rendering, plan inspection, and policy-gated
execution over canonical JSON.

Machine-readable input and output use versioned JSON through files or standard
input and standard output. Human diagnostics go to standard error and must not
corrupt machine-readable standard output. Exit statuses and structured error
documents are part of the compatibility contract.

The exact command grammar, exit-status mapping, streaming behavior, and error
schema will be specified separately. Releases should include self-contained
executables for supported operating systems and architectures plus a container
image. Users of these artifacts do not need a system-wide .NET installation.

## 12. MCP Surface and Trust Boundary

The Qhapaq MCP server is a separately hosted adapter over the same catalog,
validation, binding, visualization, and execution services used by other hosts.
Its v1 tools support:

- Listing and inspecting registered operation descriptors.
- Validating a pipeline definition.
- Creating or transforming a pipeline definition.
- Generating a Mermaid flowchart.
- Executing a validated definition when host policy explicitly permits it.

Execution is privileged and must be policy-gated. The host must be able to
disable it, constrain available operations and capabilities, enforce resource
budgets, and resolve secrets without exposing them to the model or pipeline
document. The server must not load code or expand its registry based solely on
untrusted MCP input. MCP tools must not install extensions, modify trusted host
profiles, return credential material, or broaden execution policy.

## 13. Security and Reliability Requirements

- Reject unknown document versions and unknown fields where ambiguity would
  affect execution.
- Never activate an implementation type from a document-provided type name.
- Resolve secrets through host-provided references and redact them from logs,
  diagnostics, definitions, and MCP responses.
- Validate complete structure, configuration, types, schemas, and policy before
  starting any operation.
- Bound loops, retries, concurrency, execution duration, and output size through
  definition constraints or host policy.
- Observe all started tasks so branch failures are not lost.
- Make decorator ordering and side-effect behavior visible to reviewers.
- Treat operation descriptions and other registry metadata as untrusted display
  text at protocol and UI boundaries.

## 14. Observability

Every implementation should integrate with its ecosystem's logging, metrics, and
distributed tracing standards. The .NET reference implementation uses standard
.NET abstractions. Diagnostics should identify the pipeline, plan, run,
expression, operation ID, implementation version, attempt, branch, and duration
without recording input or output payloads by default.

The detailed event and metric contract will be specified separately. The core
operation interface remains independent of a Qhapaq-specific execution context.

## 15. Compatibility, Conformance, and Versioning

The following versions are independent:

- NuGet package version.
- Pipeline document format version.
- User-authored pipeline version.
- Registered operation implementation version.

An implementation must not infer compatibility merely because two of these
versions are equal. Breaking document changes require a new document format
version. Operation resolution is exact and deterministic in v1; version ranges
and "latest" aliases are deferred.

The language-neutral specification, JSON Schemas, CLI and MCP contracts, and
conformance vectors are normative. The .NET implementation is the v1 reference
implementation, not a substitute for those artifacts.

Conformance is reported by capability:

- **Definition conformance:** parsing, validation, and canonicalization.
- **Visualization conformance:** deterministic Mermaid projection.
- **Execution conformance:** composition and failure semantics.
- **Host conformance:** normative CLI or MCP behavior.

An implementation may claim only the capabilities whose shared valid, invalid,
and behavioral test vectors it passes. Future implementations live under
`implementations/<language>/` and reuse the same root specifications, schemas,
and conformance data.

## 16. .NET Package Boundaries

The initial package decomposition is:

- `Qhapaq.Abstractions`: operation contracts and minimal shared types.
- `Qhapaq`: combinators, registry, document model, JSON parsing and
  canonicalization, binding, execution plans, execution, and deterministic
  Mermaid generation.
- `Qhapaq.Hosting`: integration with .NET hosting and dependency injection.
- `Qhapaq.Mcp`: separately hosted MCP adapter.

Primitive-operation libraries should need only `Qhapaq.Abstractions`. The main
`Qhapaq` package provides the complete default authoring and execution
experience. Hosting and MCP dependencies remain optional.

The `qhapaq` CLI is a separately distributed executable built from the same
reference implementation. It is not an additional reusable NuGet library
boundary.

## 17. Testing Strategy

The implementation requires:

- Algebra and type-compatibility unit tests for every combinator.
- Cancellation and multi-failure tests for parallel execution.
- Attempt, timeout, and decorator-ordering tests.
- Conditional branch and loop-boundary tests.
- JSON Schema conformance and canonicalization golden tests.
- Definition-to-plan binding tests for every rejection condition.
- Registry allowlist and policy tests.
- Mermaid golden tests.
- MCP tests proving execution is unavailable or rejected when policy disallows
  it.
- CLI contract tests for JSON output, diagnostics, exit statuses, and execution
  policy.
- Shared conformance tests that do not depend on .NET implementation details.
- Trimming and clean-package consumer tests for published libraries.

## 18. Alternatives Considered

### TypeScript or Python as the reference runtime

Both have strong AI ecosystems, but C# best matches the typed decorator model,
async execution contract, dependency injection, and compilation goals. The
language-neutral JSON format leaves room for future runtimes after semantics
stabilize.

### Multiple executable authoring formats

Supporting JSON, YAML, XML, Markdown, and Mermaid equally would create several
parsers and ambiguous feature parity. Canonical JSON plus generated Mermaid
gives one semantic source of truth.

### JSON values between every operation

This would simplify dynamic binding but discard native type safety and add
repeated serialization overhead. Qhapaq keeps typed values in-process and
serializes at explicit boundaries.

### Runtime code generation

Generating C#, IL, or assemblies adds compilation, sandboxing, caching,
compatibility, and debugging complexity without being necessary to execute a
bound operation graph. It is deferred.

### Durable execution

Checkpointing and recovery require persistence protocols, replay-safe effects,
version migration, distributed coordination, and compensation semantics.
Persistable definitions do not require durable runs, so durability is deferred.

### Multiple implementations in v1

Multiple runtimes would duplicate binding, execution, packaging, and
compatibility work before semantics stabilize. Qhapaq instead makes its CLI, MCP,
schemas, and conformance suite portable while shipping one reference engine.
Additional implementations can be added when an in-process use case justifies
their maintenance cost.

## 19. Open Questions

1. What JSON canonicalization scheme and JSON Schema draft will be normative?
2. How are schema references packaged and resolved without network-dependent
   validation?
3. Which operation capability vocabulary and side-effect classifications are
   required in v1?
4. What policy model governs MCP and local-host execution?
5. Which retry, timeout, cache, and concurrency decorators ship in the initial
   package?
6. What exception hierarchy and structured MCP error envelope are public API?
7. What operating systems and architectures are supported and tested?
8. Which open-source license will be used?
9. What exact CLI commands, exit statuses, and structured error schema are
   normative?
