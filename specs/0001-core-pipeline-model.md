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
execution. A validated definition can also be exported as a portable invocation
skill for repeated use by AI systems.

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
- Generate portable skills that invoke an exact pipeline with
  schema-validated boundary inputs.
- Let non-.NET systems use Qhapaq through stable CLI and MCP contracts.
- Separate safe authoring and validation from privileged execution.
- Keep core behavioral contracts independent of dependency-injection,
  logging, and MCP hosting types; .NET composition uses the framework selected
  by the implementation architecture.

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
Registry-visible code-authored operations declare portable metadata through a
separate static declaration contract; internal operations need not do so. The
portable descriptor and .NET authoring pattern are defined in
[`0007-portable-pipeline-definitions-and-binding.md`](0007-portable-pipeline-definitions-and-binding.md).

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
`ParallelExecutionException`. Its read-only `BranchExceptions` collection
reports failures in stable left-to-right branch order. Cancellation caused only
by a sibling branch failure is not an additional branch failure. Signaling
cancellation does not guarantee that a branch or its side effects stop
immediately.

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
maximum number of body invocations, execution fails with a
`LoopLimitExceededException` whose `MaxIterations` value reports the configured
limit instead of returning a potentially incomplete result.

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

An invocation skill is a packaging and discovery artifact around a definition
or exact definition reference. It is not a fourth executable representation.
The definition remains the source of truth, and a conforming host remains
responsible for validation, binding, policy, and execution.

The definition is the source of truth. An execution plan is a derived cache and
must not be treated as a portable artifact. In v1, "compile" means binding a
definition into this validated execution plan. It does not mean generating C#,
IL, or an assembly.

Plan binding must fail before execution when a referenced operation or decorator
is unavailable, its exact requested version is unavailable, connected types are
incompatible, configuration is invalid, the structure is invalid, or host
policy rejects a capability.

Each run maintains a private execution frame containing the boundary input and
immutable named node outputs. Transforms explicitly bind only the dominating
outputs they consume. The frame is ephemeral engine state, not a general
operation context, persistent run history, or model-accessible payload store.

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
- Side-effect-free transform.
- Sequence.
- Named parallel branches.
- Decorator wrapping one inner expression.
- Conditional with a predicate and two branches.
- Bounded loop with a condition, body, and maximum iteration count.

Every node has a stable document-local ID. Transforms and the optional final
output projection may combine explicitly bound boundary input and earlier node
outputs when those outputs dominate the consumer. The normative document model,
execution-frame scope rules, transform language, schema profile,
canonicalization, and plan-binding lifecycle are defined in
[`0007-portable-pipeline-definitions-and-binding.md`](0007-portable-pipeline-definitions-and-binding.md).

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
- Exact immutable contract version and contract digest.
- Human-readable name and description.
- Portable input, output, and configuration JSON Schemas.
- Declared capabilities and side-effect characteristics.
- Documentation and examples intended for humans and AI systems.

An implementation binding additionally associates the portable descriptor with
native input and output types, implementation identity, integrity information,
and factory information held by the host. Those details are not supplied by the
pipeline document. Pipelines pin exact operation contracts; the trusted host
selects exact implementation artifacts.

Operation IDs are portable names, not implementation type names. A host decides
which descriptors and implementations to register. Portable binding requires
compatible declared schemas. The .NET binding additionally requires CLR type
assignability.

Values remain native runtime values between in-process operations; the .NET
reference implementation uses strongly typed CLR objects. Serialization occurs
at CLI, MCP, pipeline, and persistence boundaries and in explicit serialization
or transform nodes. Qhapaq does not automatically reshape or convert mismatched
intermediate values; a pipeline must use an explicit transform or registered
mapping operation.

Published operation ID and contract-version pairs are immutable. Compatible
newer versions support authoring and migration analysis but are never silently
substituted for an exact pipeline reference. Descriptor declaration, digest, and
compatibility rules are defined in
[`0007-portable-pipeline-definitions-and-binding.md`](0007-portable-pipeline-definitions-and-binding.md).

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
execution over canonical JSON. It also generates portable invocation-skill
bundles from validated definitions.

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
- Listing and inspecting persisted pipeline definitions when the host exposes a
  pipeline store.
- Validating a pipeline definition.
- Creating or transforming a pipeline definition.
- Generating a Mermaid flowchart.
- Generating a portable pipeline invocation-skill bundle.
- Executing a validated definition when host policy explicitly permits it.
- Executing an exact persisted pipeline reference when the host advertises that
  capability and policy explicitly permits it.

Execution is privileged and must be policy-gated. The host must be able to
disable it, constrain available operations and capabilities, enforce resource
budgets, and resolve secrets without exposing them to the model or pipeline
document. The server must not load code or expand its registry based solely on
untrusted MCP input. MCP tools must not install extensions, modify trusted host
profiles, return credential material, or broaden execution policy.

## 13. Portable Pipeline Invocation Skills

### 13.1 Purpose and Authority

A pipeline invocation skill gives an AI system reviewed instructions and
machine-readable artifacts for invoking a particular Qhapaq pipeline. It is a
thin adapter over the normative CLI or MCP execution contract. It must not
reimplement pipeline semantics, contain executable operation code, or act as a
capability token.

Possession or invocation of a skill grants no execution, connection, secret,
network, extension, budget, or payload-disclosure authority. Every invocation
must pass the same complete validation, binding, policy, budget, credential
resolution, and disclosure checks as a direct CLI or MCP request.

### 13.2 Parameter Model

The pipeline boundary input schema is the skill's parameter contract. A
generated skill must not introduce a second expression or parameter language.
Runtime input is a JSON value validated against that schema before any operation
starts.

Static operation configuration is not implicitly overridable. A pipeline author
who wants a value to vary between invocations must expose it through the
pipeline boundary input or use an explicit operation whose declared semantics
perform that binding. Skills and invocation requests must not patch arbitrary
locations in a canonical definition.

Examples and default values, when exported, are non-authoritative documentation
unless the pipeline input schema gives them normative semantics. A generator
must not invent omitted required values or silently substitute invalid input.

### 13.3 Portable Bundle Profile

The v1 portable profile is a self-contained directory with:

- `SKILL.md`, containing human- and agent-readable invocation guidance.
- `qhapaq-skill.json`, a versioned machine-readable manifest.
- `references/input.schema.json` and `references/output.schema.json`.
- `references/pipeline.json` in snapshot mode.

The manifest declares:

- Its Qhapaq skill-bundle format identifier and version.
- The pipeline ID, exact pipeline version, and canonical definition digest.
- Whether the bundle uses snapshot or reference mode.
- The pipeline document format version.
- Relative paths and media types for included artifacts.
- Required host capabilities and declared pipeline side-effect
  characteristics.
- Generator identity and version as informational provenance.

Paths in a bundle are normalized relative paths and must not escape the bundle
root. A bundle must not contain credentials, resolved secret values, token-cache
material, trusted host-profile contents, implementation type names, executable
operation code, or policy overrides.

`SKILL.md` describes when the pipeline is appropriate, identifies its side
effects and prerequisites, explains the boundary input, and directs the consumer
to the normative Qhapaq CLI or MCP operation. Generated prose, pipeline
metadata, operation descriptions, examples, and other untrusted display text
must be clearly delimited so they cannot silently become authoritative
instructions or override the manifest, pipeline definition, host policy, or
higher-authority guidance.

Client-specific skill, prompt, or agent formats are adapters over this portable
bundle. They must preserve its exact pipeline identity, version, digest,
parameter schema, authority limits, and disclosure behavior.

### 13.4 Snapshot and Reference Modes

Snapshot mode is the required portable mode and includes the canonical pipeline
definition in the bundle. Before execution, the host recomputes its canonical
digest and rejects a mismatch. Snapshot mode does not require access to the host
that generated the skill, but the executing host must provide the exact
registered operations and permitted capabilities required by the definition.

Reference mode identifies a persisted definition by stable pipeline ID, exact
pipeline version, and expected canonical digest. It is an optional host
capability for centrally managed pipelines. The host resolves the reference and
must fail before execution if it is absent or if its identity, version, or
digest differs. Reference mode must not select an unspecified `latest` version
or silently follow a mutable alias.

A skill must be regenerated or explicitly reviewed when the intended canonical
definition changes. Updating examples or non-semantic guidance must not alter
the pinned definition digest.

### 13.5 CLI and MCP Generation

The normative CLI supports generating a bundle from a validated canonical
definition and may write the resulting bounded directory tree to a
user-selected destination. It must refuse path traversal, unexpected overwrite,
invalid definitions, unresolved exact operation versions, or content that would
place prohibited sensitive material in the bundle.

The MCP surface accepts a validated definition or exact persisted reference and
returns a structured bundle or an MCP resource containing that bundle. An MCP
tool must not write to an arbitrary client-selected filesystem path. Skill
generation does not install the skill, persist or approve a connection, modify
a trusted profile, install an extension, or broaden execution or disclosure
policy.

Executing a generated skill uses the ordinary definition-execution request in
snapshot mode or an exact-reference execution request in reference mode. The
structured result includes the pipeline ID, version, digest, run ID, status, and
either a schema-valid output or a structured indication that output was
withheld, redacted, summarized, or limited by policy. CLI and MCP mappings use
the same language-neutral result and error models.

### 13.6 Compatibility and Conformance

The skill-bundle format version is independent of the pipeline document,
pipeline, operation, package, CLI, and MCP protocol versions. A breaking bundle
change requires a new bundle format version.

Snapshot skill generation is part of host conformance for implementations that
claim invocation-skill support. Reference-mode generation and execution are
reported as a separate host capability. Shared conformance vectors cover bundle
structure, path safety, canonical digest verification, input validation,
version and digest mismatch rejection, authority preservation, secret
exclusion, disclosure enforcement, and resistance to instruction injection
through untrusted metadata.

## 14. Security and Reliability Requirements

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

## 15. Observability

Every implementation should integrate with its ecosystem's logging, metrics, and
distributed tracing standards. The .NET reference implementation uses standard
.NET abstractions. Diagnostics should identify the pipeline, plan, run,
expression, operation ID, implementation version, attempt, branch, and duration
without recording input or output payloads by default.

The detailed event and metric contract will be specified separately. The core
operation interface remains independent of a Qhapaq-specific execution context.

## 16. Compatibility, Conformance, and Versioning

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

## 17. .NET Package Boundaries

The initial public package decomposition is:

- `Qhapaq.Abstractions`: public Service and operation-authoring contracts,
  minimal shared types, and internal cross-layer contracts.
- `Qhapaq`: distribution package containing the `Qhapaq.Service.V1`,
  `Qhapaq.Business`, and `Qhapaq.DAL` implementation assemblies.
- `Qhapaq.Hosting`: integration package containing the
  `Qhapaq.Implementations.Hosting` assembly.
- `Qhapaq.Mcp`: separately hosted MCP adapter package containing the
  `Qhapaq.Implementations.MCP` assembly.

Primitive-operation libraries should need only `Qhapaq.Abstractions`. The main
`Qhapaq` package provides the complete default authoring and execution
experience. Hosting and MCP dependencies remain optional.

The `qhapaq` CLI is a separately distributed executable built from the same
reference implementation and the `Qhapaq.Implementations.CLI` assembly. It is
not an additional reusable NuGet library boundary.

Package boundaries and assembly boundaries are intentionally independent. The
layer-aligned assemblies implement the Service Implementations, versioned
Service, Business, and DAL boundaries defined in
[`0006-dotnet-layered-architecture.md`](0006-dotnet-layered-architecture.md).
The physical layer assemblies do not create additional public NuGet package
boundaries.

## 18. Testing Strategy

The implementation requires:

- Algebra and type-compatibility unit tests for every combinator.
- Cancellation and multi-failure tests for parallel execution.
- Attempt, timeout, and decorator-ordering tests.
- Conditional branch and loop-boundary tests.
- Execution-frame dominance, transform, final-projection, JSON Schema
  conformance, and canonicalization golden tests.
- Definition-to-plan binding tests for every rejection condition.
- Exact operation-contract version, digest, and compatibility-diff tests.
- Registry allowlist and policy tests.
- Mermaid golden tests.
- MCP tests proving execution is unavailable or rejected when policy disallows
  it.
- Skill-bundle golden tests for snapshot generation, manifest and path
  validation, exact identity/version/digest pinning, and round-tripping through
  CLI and MCP.
- Skill-execution tests proving invalid boundary input and changed referenced
  definitions fail before operations start.
- Skill-security tests proving generated artifacts contain no secrets, cannot
  broaden authority, preserve disclosure controls, and safely delimit untrusted
  metadata.
- CLI contract tests for JSON output, diagnostics, exit statuses, and execution
  policy.
- Shared conformance tests that do not depend on .NET implementation details.
- Trimming and clean-package consumer tests for published libraries.

## 19. Alternatives Considered

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

### Skills as another executable pipeline format

Making `SKILL.md`, scripts, prompts, or client-specific agent files executable
pipeline sources would create competing semantics and weaken deterministic
validation. Qhapaq instead treats a skill as a portable adapter that embeds or
exactly references canonical JSON and delegates execution to a conforming host.

### Mutable or latest pipeline references

Allowing a generated skill to follow an unspecified latest version would make
reviewed automations change behavior without review and could broaden side
effects or data access. Reference-mode skills therefore pin pipeline identity,
version, and canonical digest and fail closed on mismatch.

## 20. Open Questions

1. Which operation capability vocabulary and side-effect classifications are
   required in v1?
2. What policy model governs MCP and local-host execution?
3. Which retry, timeout, cache, and concurrency decorators ship in the initial
   package?
4. What exception hierarchy and structured MCP error envelope are public API?
5. What operating systems and architectures are supported and tested?
6. What exact CLI commands, exit statuses, and structured error schema are
   normative?
