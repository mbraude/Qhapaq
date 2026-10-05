# SPEC-0007: Portable Pipeline Definitions and Plan Binding

> **Status:** Draft
>
> **Target:** Qhapaq v1
>
> **Last updated:** 2026-10-04

## 1. Summary

Qhapaq pipelines use one canonical, versioned JSON representation for
interchange, persistence, review, hashing, AI-assisted authoring, validation,
visualization, and execution-plan binding. A pipeline document is inert data. It
never names implementation types, embeds executable source, or directly
constructs runtime objects.

A conforming host parses a definition, validates it in deterministic stages,
resolves exact operation contracts through its effective registry, type-checks
all dataflow and transforms, evaluates policy, and binds an immutable execution
plan before any operation executes. Each run maintains an internal immutable
execution frame whose named output slots let later transforms and the final
pipeline projection combine values from earlier operations.

Operation contracts are portable, versioned, and immutable. Code-authored .NET
operations keep an authoritative portable descriptor JSON document adjacent to
the implementation. A Roslyn incremental generator validates that document and
emits the static declaration, explicit registration, and embedded canonical
manifest. Runtime assembly scanning and attribute-only descriptors are not the
registration model.

## 2. Goals

- Define the normative shape and semantics of portable pipeline JSON.
- Make complete structural, type, binding, and policy validation possible before
  execution.
- Let transforms combine explicitly selected earlier outputs, boundary input,
  and public literals without arbitrary generated code.
- Preserve native values between ordinary in-process operations while making
  transforms explicit serialization boundaries.
- Make data dependencies visible to humans, AI systems, validators, and Mermaid
  projections.
- Give AI systems sufficient operation metadata and structured diagnostics to
  discover, author, validate, and repair pipelines without executing them.
- Keep operation metadata co-located with code-authored implementations while
  preserving one language-neutral descriptor model.
- Prevent silent operation-contract drift through exact versions, canonical
  contract digests, and immutable published identities.
- Keep execution permission and payload-disclosure permission independent from
  definition validity and plan bindability.

## 3. Non-goals

This specification does not:

- Define observability, tracing, metrics, or run-history storage.
- Make Qhapaq a general-purpose programming language.
- Permit executable source, scripts, runtime compilation, or arbitrary
  reflection in pipeline documents.
- Define durable runs, checkpoints, replay, compensation, or transactional
  rollback.
- Permit dynamic operation selection or unspecified latest versions.
- Make validation prove that an external service will be available or that a
  side effect is desirable.
- Require JSON serialization between ordinary in-process operations.
- Make generated Mermaid, Markdown, YAML, prompts, or skills executable pipeline
  formats.
- Define the final public .NET API signatures for descriptor authoring or source
  generation.

## 4. Terminology

- **Pipeline definition:** canonical, versioned JSON that describes one portable
  executable pipeline.
- **Node:** one locally identified structural element in a pipeline definition.
- **Operation contract:** the immutable portable behavior identified by an
  operation ID and exact contract version.
- **Operation descriptor:** the portable contract and documentation metadata for
  an operation or decorator.
- **Operation implementation:** trusted executable code that declares support
  for an exact operation contract and digest.
- **Execution plan:** an immutable, host-specific binding of a validated
  definition to implementations, serializers, transforms, and policy decisions.
- **Execution frame:** per-run internal storage containing the boundary input and
  immutable named node-output slots.
- **Transform:** a side-effect-free structural node expressed in the versioned
  Qhapaq mapping language.
- **Dominates:** a node dominates another node when every valid control-flow path
  to the latter necessarily completes the former successfully.
- **Contract digest:** a digest of the canonical normative portion of an
  operation descriptor.
- **Implementation identity:** the package, extension, built-in provider, or
  connector version and integrity information selected by the host.

## 5. Representations and Lifecycle

A pipeline has three executable-lifecycle representations:

1. The portable pipeline definition.
2. A derived immutable execution plan.
3. One non-durable run of that plan.

The host must treat pipeline JSON as inert input. Deserialization produces only
a definition model and must not:

- activate a type named by the document;
- load an assembly or extension;
- resolve a credential;
- access an external resource;
- construct an operation implementation; or
- begin a side effect.

The lifecycle is:

```text
parse
  -> document-schema validation
  -> structural validation
  -> exact contract resolution
  -> schema and transform type checking
  -> native binding validation
  -> capability and side-effect aggregation
  -> host-policy evaluation
  -> immutable plan binding
  -> execution
```

Every stage before execution must complete successfully before any operation
starts. Plan binding may precompute serializers, native materializers,
expression accessors, last-consumer information, and implementation factories.
An execution plan is host-specific derived state and is not a portable artifact.

## 6. Pipeline Document

### 6.1 Required top-level members

Every definition contains:

- `format`, with the exact value `qhapaq.pipeline/v1`;
- a stable pipeline `id`;
- an exact pipeline `version`;
- an optional non-normative `metadata` object;
- `schemas.input` and `schemas.output`;
- one `root` composition expression; and
- an optional explicit `output` projection.

Unknown properties are rejected unless the normative pipeline JSON Schema
explicitly permits them.

Illustrative shape:

```json
{
  "format": "qhapaq.pipeline/v1",
  "id": "contoso.orders.create-from-customer",
  "version": "1.0.0",
  "metadata": {
    "displayName": "Create an order from a customer"
  },
  "schemas": {
    "input": {
      "type": "object",
      "required": ["customerId", "requestedBy"],
      "properties": {
        "customerId": { "type": "string" },
        "requestedBy": { "type": "string" }
      },
      "additionalProperties": false
    },
    "output": {
      "type": "object",
      "required": ["customerId", "orderId"],
      "properties": {
        "customerId": { "type": "string" },
        "orderId": { "type": "string" }
      },
      "additionalProperties": false
    }
  },
  "root": {
    "id": "order-flow",
    "kind": "sequence",
    "steps": [
      {
        "id": "get-customer",
        "kind": "operation",
        "operation": {
          "id": "contoso.customers.get",
          "version": "1.2.0"
        }
      },
      {
        "id": "calculate-price",
        "kind": "operation",
        "operation": {
          "id": "contoso.pricing.calculate",
          "version": "2.0.0"
        }
      },
      {
        "id": "create-order-input",
        "kind": "transform",
        "language": "qhapaq.mapping/v1",
        "inputs": {
          "customer": {
            "source": "node",
            "node": "get-customer"
          },
          "pricing": {
            "source": "node",
            "node": "calculate-price"
          },
          "request": {
            "source": "pipeline-input"
          }
        },
        "outputSchema": {
          "type": "object",
          "required": ["customerId", "total", "requestedBy"],
          "properties": {
            "customerId": { "type": "string" },
            "total": { "type": "number" },
            "requestedBy": { "type": "string" }
          },
          "additionalProperties": false
        },
        "expression": {
          "object": {
            "customerId": {
              "select": "$inputs.customer.id"
            },
            "total": {
              "select": "$inputs.pricing.total"
            },
            "requestedBy": {
              "select": "$inputs.request.requestedBy"
            }
          }
        }
      },
      {
        "id": "create-order",
        "kind": "operation",
        "operation": {
          "id": "contoso.orders.create",
          "version": "3.1.0"
        }
      }
    ]
  },
  "output": {
    "language": "qhapaq.mapping/v1",
    "inputs": {
      "customer": {
        "source": "node",
        "node": "get-customer"
      },
      "order": {
        "source": "node",
        "node": "create-order"
      }
    },
    "expression": {
      "object": {
        "customerId": {
          "select": "$inputs.customer.id"
        },
        "orderId": {
          "select": "$inputs.order.id"
        }
      }
    }
  }
}
```

The normative JSON Schema may refine property names and factoring before v1 is
published, but it must preserve the semantics in this specification.

### 6.2 Node identities

Every node has a non-empty document-local `id`. Node IDs:

- are unique across the complete definition;
- are stable diagnostic and visualization anchors;
- do not select implementations;
- do not contribute to operation identity; and
- must not contain credentials or sensitive payload data.

Changing a node ID changes the canonical definition because bindings and
diagnostics may reference it.

### 6.3 Structural node kinds

The v1 language supports:

- `operation`;
- `transform`;
- `sequence`;
- named `parallel` branches;
- `decorate`;
- `conditional`; and
- bounded `loop`.

Combinators and transforms are language constructs, not catalog operations.
Registry descriptors use `primitive` or `decorator` as their composition role.

An operation reference always contains an operation ID and exact contract
version. Version ranges, aliases, and unspecified latest versions are invalid.

Decorator order is explicit and semantically significant. Parallel branch names
are stable members of the parallel result. Conditionals and loops follow the
composition semantics in
[`0001-core-pipeline-model.md`](0001-core-pipeline-model.md).

## 7. Execution Frame and Dataflow

### 7.1 Immutable slots

Each run has a private execution frame containing:

- the validated boundary input; and
- one immutable output slot for every successfully completed node whose value is
  still required.

A node writes its output slot at most once. A consumer cannot mutate a stored
value through the execution-frame contract. The frame is engine state, not a
general operation context and not an externally inspectable result store.

The engine must not automatically log, serialize, persist, or disclose frame
values. Payload-disclosure policy applies independently from execution
permission.

### 7.2 Explicit transform inputs

A transform declares a map of local input names to sources. A source is either:

- `pipeline-input`; or
- the output of a named node that dominates the transform.

The mapping expression reads only its declared `$inputs` values and literals.
It cannot enumerate the execution frame or access an undeclared node.

The immediately preceding sequence output may be supported as authoring
shorthand, but canonical JSON must represent or deterministically normalize it
to an explicit source.

### 7.3 Dominance and scope

Sequential nodes may reference earlier nodes in the same enclosing sequence
when those nodes dominate the consumer.

A node after a parallel join may reference the completed result of every named
branch. A node inside one parallel branch cannot reference a sibling branch.

Branch-local conditional outputs do not escape directly. The conditional
produces one common output contract, and downstream consumers reference that
conditional output. Both branches must produce values compatible with that
contract.

Each loop iteration has an iteration-local frame. The loop body may read the
current loop state, the pipeline input, and values defined in dominating outer
scopes. Only the final loop result escapes. Retaining per-iteration outputs
requires an explicit bounded collection construct or operation; the engine does
not retain iteration history implicitly.

References to nodes that may not execute, have not completed, are in an
inaccessible branch, or occur later in the dataflow are invalid before
execution.

### 7.4 Lifetime and budgets

The execution plan computes the consumers of each slot. An implementation may
release a slot after its final consumer completes, subject to native object
lifetime requirements.

Frame values count toward host memory and output-size budgets. A budget failure
is an execution failure and must not produce a success-shaped partial result.

## 8. Transform Language

### 8.1 Purpose

`qhapaq.mapping/v1` is a portable, deterministic, side-effect-free expression
language for constructing one schema-valid value from declared inputs and
public literals. It is represented as JSON syntax rather than executable source.

The initial language includes:

- property and array-item selection;
- object and array construction;
- JSON literals;
- Boolean and numeric expressions;
- string concatenation and supported formatting;
- conditional expressions;
- explicit null handling and coalescing;
- bounded array projection and filtering; and
- explicit supported parsing and conversion functions.

The normative schema will enumerate every operator, operand shape, and result
typing rule. Unknown operators are invalid.

### 8.2 Prohibited capabilities

A transform cannot:

- perform network, filesystem, process, or credential access;
- access environment variables or host services;
- inspect implementation-native types or invoke reflection;
- invoke an operation dynamically;
- use a clock, random source, or mutable global state;
- define recursion or unbounded iteration;
- execute source text; or
- read an undeclared execution-frame slot.

### 8.3 Type checking

Every transform declares an output schema. The validator derives an expression
result schema from its declared input schemas and proves that every successful
result conforms to the declared output schema.

Potentially absent or nullable selections do not satisfy required non-null
outputs without an explicit operation such as coalescing, conditional handling,
or a checked assertion. There are no implicit string, number, Boolean, enum,
date, or identifier conversions.

An expression may contain a checked partial operation, such as parsing a date.
Such an operation must have specified failure behavior. A runtime value failure
terminates the transform before any downstream operation begins.

### 8.4 Serialization boundary

Ordinary in-process operation connections continue to use native values.
A transform is an explicit portable-value boundary:

1. Each bound native input is projected using the resolved operation contract's
   portable representation.
2. The mapping expression evaluates those portable values.
3. The result is validated against the transform output schema.
4. The result is materialized into the downstream implementation's registered
   native input type when applicable.
5. The downstream operation may start only after successful materialization.

The plan binder pre-binds these projections and materializers. A transform must
not discover serializers or native types during a run.

## 9. Schema Profile and Compatibility

Pipeline and operation schemas use JSON Schema Draft 2020-12 under a Qhapaq v1
profile. The profile must define:

- the supported keywords and formats;
- object and array closure rules;
- numeric and string constraints;
- nullability and union restrictions;
- local reference packaging;
- default-value semantics; and
- the conservative compatibility algorithm.

Remote schema resolution during validation or execution is prohibited.
References resolve only within the definition or through exact, digest-pinned
artifacts available to the host.

Compatibility validation is conservative. A connection is accepted only when
the validator can prove that every successful upstream value conforms to the
downstream input schema. An unsupported or indeterminate comparison is rejected
rather than treated as compatible.

At minimum:

- every downstream required property is guaranteed upstream;
- optional or nullable values cannot satisfy required non-null inputs;
- numeric ranges and string constraints are not weakened accidentally;
- union selection is unambiguous;
- array-item schemas are compatible; and
- additional-property behavior is respected.

The normative schemas and conformance vectors will define the exact profile and
algorithm before implementation of portable pipeline binding is complete.

## 10. Pipeline Output

Without an explicit `output` projection, the root expression's output must be
compatible with `schemas.output` and becomes the pipeline result.

An explicit output projection:

- runs only after the root completes successfully;
- may bind the boundary input and any node output that dominates completion of
  the root;
- uses `qhapaq.mapping/v1`;
- must produce a value conforming to `schemas.output`; and
- cannot cause external side effects.

This permits a result to combine selected values from multiple operations
without turning the execution frame into a persistent or externally queryable
store.

## 11. Operation Descriptors

### 11.1 Portable descriptor

Every registry-visible primitive or decorator has one portable descriptor
containing:

- stable operation ID;
- exact contract version;
- canonical contract digest;
- composition role;
- input, output, and configuration schemas;
- structured failure contract;
- capabilities and side-effect classification;
- idempotency guarantees;
- human-readable name and description;
- usage guidance for when to use and not use the operation; and
- reviewed examples intended for humans and AI systems.

The descriptor separates normative `contract` fields from non-normative
`documentation` fields. The contract digest covers normative fields and excludes
documentation-only corrections, host availability, implementation provenance,
and policy state.

Operation descriptions, imported specifications, and examples are untrusted
metadata. MCP and documentation projections must delimit them from authoritative
instructions and must not let them broaden host or model authority.

### 11.2 Composition roles

Portable descriptors use:

- `primitive` for leaf operations; and
- `decorator` for operations that wrap an inner operation.

A decorator descriptor declares that its input and output contracts are
preserved from its inner operation and provides a configuration schema.
Structural sequence, parallel, conditional, loop, and transform forms are not
registry descriptors.

### 11.3 Availability

The effective registry reports whether an exact descriptor is:

- available;
- unavailable because a trusted implementation is absent;
- unavailable because required host configuration is absent; or
- unavailable because active policy excludes it.

Explanations must not reveal credentials, secret references, sensitive
filesystem locations, or other protected host configuration.

## 12. .NET Operation Declarations

This section is specific to the .NET reference implementation and does not
change the portable descriptor model.

`IOperation<TInput, TOutput>` remains an execution-only contract. It does not
gain descriptor instance methods or a general-purpose execution-context
parameter.

### 12.1 Authoritative descriptor source

Every registry-visible code-authored .NET operation has one checked-in portable
descriptor JSON document adjacent to its implementation. That document is the
authoritative source for the complete portable descriptor, including its
normative contract and non-normative documentation.

The initial descriptor format is
`qhapaq.operation-descriptor/v1alpha1`, defined by
[`../schemas/operation-descriptor-v1alpha1.schema.json`](../schemas/operation-descriptor-v1alpha1.schema.json).
It is a pre-release format that may be replaced by another pre-release version
before immutable `v1` is published. Validators resolve the checked-in schema
offline by its stable `$id`; validation never requires network access.

The descriptor document:

- conforms to the exact versioned operation-descriptor schema;
- contains no CLR type names, implementation factories, credentials, resolved
  secrets, or host-specific availability state;
- declares its stable operation ID, exact contract version, contract digest,
  schemas, failures, capabilities, effects, idempotency, role, and
  documentation;
- is included as an explicit build input rather than found through filesystem
  enumeration; and
- is packaged with source when source packages are produced.

The implementation and descriptor use exact, case-sensitive basename matching
and reside in the same physical source directory:

```text
HttpOperation.cs
HttpOperation.descriptor.json
```

An operation cannot obtain its descriptor from an orthogonal descriptor tree,
a parent directory, a linked file outside its source directory, or recursive
filesystem discovery. The generator rejects a missing descriptor, more than one
matching descriptor, basename or case mismatch, reuse by another operation, or
an association outside the operation's physical directory.

The contract digest excludes its own field and is computed from the canonical
normative descriptor portion defined in Section 13. A supplied digest must
match the computed value. The generator never silently replaces a missing or
incorrect digest.

C# declaration code is a generated projection of this JSON source. Authors do
not maintain a second hand-written descriptor property or duplicate descriptor
fields in attributes.

### 12.2 Operation marker and authoring shape

A registry-visible operation uses a marker attribute or an equivalent explicit
compiler input to associate the implementation class with exactly one descriptor
document. The marker may carry the descriptor build-input identity or path, but
it does not carry portable contract fields.

The intended authoring shape is conceptually:

```csharp
[QhapaqOperation("GetCustomerOperation.descriptor.json")]
public sealed partial class GetCustomerOperation :
    IOperation<GetCustomerInput, GetCustomerOutput>
{
    public Task<GetCustomerOutput> ExecuteAsync(
        GetCustomerInput input,
        CancellationToken cancellationToken = default)
    {
        // Operation behavior.
    }
}
```

The exact attribute name, constructor shape, generated type names, and namespace
layout remain implementation API details. Registry-visible implementation
classes must be compatible with partial source generation. Internal
combinators, test delegates, and non-catalog operations need not declare
portable descriptors and are not included in the generated manifest.

### 12.3 Build-time discovery and validation

The .NET operation-authoring package supplies a Roslyn incremental generator.
Each compilation explicitly references the generator as build tooling rather
than as a runtime dependency.

During compilation, the generator:

1. Uses semantic symbol analysis to find operation classes carrying the marker.
2. Resolves the associated descriptor only from declared compiler build inputs.
3. Selects the validator by the descriptor's exact `format` value and rejects an
   unknown or unsupported version.
4. Parses and validates the descriptor against the exact offline schema without
   loading the operation assembly, constructing the operation, executing project
   code, accessing the network, or resolving credentials.
5. Verifies that the class is a supported concrete partial declaration and
   implements exactly one compatible `IOperation<TInput, TOutput>` contract.
6. Validates canonicalization, contract digest, composition role, and every
   other compiler-verifiable declaration rule.
7. Rejects duplicate operation ID and contract-version pairs within the
   compilation.
8. Emits deterministic source only when the required inputs are valid.

Generator diagnostics are build diagnostics. Missing or ambiguous descriptor
inputs, invalid JSON or schemas, digest mismatches, unsupported class shapes,
operation/declaration generic mismatches, and duplicate identities are errors.
Diagnostics identify source locations and stable diagnostic codes without
including operation payloads, credentials, or protected host configuration.

Incremental caching is an optimization only. Changing an operation declaration,
descriptor document, descriptor schema, or generator version must invalidate all
affected generated outputs.

### 12.4 Generated declaration and registration

For each valid operation, the generator emits a partial declaration that
implements the static descriptor-declaration contract and exposes the descriptor
represented by the authoritative JSON. The generated implementation must not
instantiate the operation.

Conceptually, generated source includes:

```csharp
partial class GetCustomerOperation :
    IDeclaredOperation<GetCustomerInput, GetCustomerOutput>
{
    public static OperationDescriptor Descriptor =>
        GeneratedOperationDescriptors.GetCustomer;
}
```

The generator also emits an explicit registration table containing closed
generic references:

```csharp
internal static class GeneratedOperationRegistration
{
    internal static void Register(OperationRegistryBuilder builder)
    {
        builder.Add<
            GetCustomerOperation,
            GetCustomerInput,
            GetCustomerOutput>();
    }
}
```

Generated registration is ordinary compiled code. Runtime registration invokes
this table directly; it does not enumerate assemblies, types, attributes, or
resources to discover operations.

Generated sources are compiler outputs and are not checked into the repository.
Their ordering, identifiers, canonical descriptor bytes, and package manifest
bytes must be deterministic and independent of absolute paths, machine state,
culture, and filesystem enumeration order.

### 12.5 Generated portable manifest

The generator produces one canonical portable operation manifest for its
compilation. The manifest contains the complete generated descriptors in stable
operation-ID and contract-version order. It does not contain CLR type names or
implementation factories.

The canonical manifest bytes are embedded into the compiled operation assembly
as deterministic data reachable through its explicit generated registration
entry point. Packaging may also expose the identical bytes as a package
artifact. An embedded and packaged copy must be byte-for-byte equal.

The manifest is a projection of the checked-in descriptor documents. It never
becomes an independent authoring source, and editing generated output is not a
supported workflow.

### 12.6 Referenced packages and extensions

A generator processes the source compilation and explicit descriptor build
inputs to which it is attached. It does not discover operations by scanning
referenced assemblies.

Each trusted operation or extension package therefore ships its own generated
manifest and explicit registration entry point. A host includes a package only
through trusted host configuration and calls that entry point explicitly.
Combining built-in, extension, and OpenAPI-backed descriptors occurs during
effective-registry construction, where cross-package identity and digest
conflicts are rejected.

### 12.7 Runtime verification

Generated output improves correctness and reachability but is not an authority
grant. Effective-registry construction must still:

- validate the embedded canonical manifest and recompute every contract digest;
- verify agreement among the manifest, generated static declaration, registered
  native generic types, and implementation identity;
- reject duplicate ID and contract-version pairs or conflicting digests across
  all enabled sources;
- apply trusted host configuration, implementation-integrity checks, connection
  availability, and active policy; and
- produce immutable registry entries before any operation can execute.

Source generation does not grant execution permission or descriptor-disclosure
permission. CLI and MCP projections consume the same policy-filtered application
services backed by the effective registry; they do not read generated assembly
metadata directly.

### 12.8 Trimming, AOT, and security

Closed generic references in generated registration preserve required operation
types for trimming and Native AOT without unbounded reflection. Generated code
must not use descriptor values as source text, type names, member names, or
instructions. Descriptor text and examples remain untrusted metadata even
though their containing package is trusted.

OpenAPI-backed operations and future non-.NET providers produce the same
portable descriptors without using this .NET authoring pattern.

## 13. Contract and Implementation Versioning

### 13.1 Separate identities

An operation contract identity consists of:

```text
operation ID + exact contract version + contract digest
```

An implementation identity consists of its provider, package or extension
version, and integrity information. A pipeline selects only the operation
contract. The trusted host selects and enables an implementation.

A bound plan records both identities. An implementation may bind only when it
declares support for the exact requested contract version and digest.

### 13.2 Immutability

Once published, an operation ID and contract-version pair is immutable. A host
must reject duplicate descriptors with the same ID and version but different
contract digests.

The contract digest covers the canonical normative descriptor, including:

- input, output, and configuration schemas;
- structured failures;
- capabilities;
- side effects;
- idempotency;
- composition role; and
- other machine-enforced behavioral guarantees.

Documentation-only changes do not change the contract digest. Changing the
meaning of an operation requires a new contract version even when its schemas
remain unchanged.

### 13.3 Compatibility rules

Operation contract versions use Semantic Versioning with Qhapaq-specific,
conservative compatibility rules.

A major version is required for a potentially breaking change, including:

- removing or renaming an accepted input;
- adding a required input;
- narrowing accepted input values;
- removing an output or making a guaranteed output optional;
- incompatibly changing an output type or structured failure;
- adding externally visible side effects;
- weakening idempotency;
- requiring a new privileged capability;
- changing composition role; or
- changing the meaning of an existing value.

A minor version may describe a demonstrably backward-compatible addition, such
as accepting an optional input or adding an output where the prior contract
explicitly permits additive properties.

A patch version does not change the normative portable contract. Compatible
implementation fixes and performance changes normally advance the implementation
version while continuing to implement the same exact operation contract.

Contract-diff tooling classifies a comparison as `compatible`, `breaking`, or
`indeterminate`. Indeterminate changes are not treated as compatible.

Compatibility does not permit substitution. A pipeline requesting version
`2.1.0` binds only to the exact `2.1.0` contract, even when `2.2.0` is classified
as backward compatible. Compatibility information supports authoring,
migration, and review.

### 13.4 Descriptor, generator, manifest, and surface versions

Descriptor schema versions, generator package versions, generated registration
contract versions, manifest-envelope versions, and Service, CLI, or MCP contract
versions are independent:

| Axis | Example identity | Compatibility rule |
| --- | --- | --- |
| Descriptor document | `qhapaq.operation-descriptor/v1alpha1` | A breaking descriptor-shape or semantic change uses a new format value and schema. |
| Generator package | `Qhapaq.Operation.Generators` package version | One release may support multiple descriptor formats through version-specific validators. |
| Generated registration contract | Versioned .NET authoring-runtime API | Generated code declares the exact runtime contract it requires; incompatible API changes are side-by-side or major-version changes. |
| Portable manifest envelope | `qhapaq.operation-manifest/v1alpha1` | Envelope changes are versioned independently from contained descriptor formats. |
| Service, CLI, and MCP surfaces | Their own versioned contracts | Transport evolution does not rewrite or implicitly upgrade descriptor documents. |

A generator release publishes a compatibility matrix listing every descriptor
format, manifest envelope, and registration-contract version it accepts or
emits. Generator and schema versions are not one-to-one.

For each supported descriptor format, the generator uses a format-specific
parser and validator and then maps valid content into a common internal
generation model. Normalization must preserve every normative field and the
exact original format identity. The generator must not reinterpret an unknown
field, silently downgrade a newer format, or treat a newer format as an older
one.

A compilation may contain descriptors from multiple formats only when the
selected generator explicitly supports all of them and the selected manifest
envelope can preserve each exact descriptor. The generated manifest records the
format of every contained descriptor.

Adding support for a new descriptor format is a backward-compatible generator
feature when existing generated output remains compatible. Removing support for
a previously supported published format is a breaking generator change.
Projects pin a generator package version and fail the build when a descriptor
format falls outside its published support matrix.

Generated registration code targets a versioned authoring-runtime contract.
Package dependency constraints must prevent compiling generated code against an
incompatible runtime contract. A breaking registration API does not require a
new descriptor schema when descriptor semantics are unchanged.

Effective-registry construction independently declares the descriptor formats,
manifest envelopes, and registration-contract versions supported by that host.
It rejects an unsupported combination before making any operation available.
A package that compiled successfully with a newer generator is therefore not
assumed to be loadable by an older host.

Business and Service layers expose a stable versioned summary model for common
catalog fields and may also return the exact versioned portable descriptor when
policy permits. CLI and MCP adapters project those Service contracts; they do
not bind directly to generator or manifest internals. Metadata that cannot be
represented compatibly requires an additive versioned projection or a new
Service, CLI, or MCP contract rather than silent omission or reinterpretation.

The pre-release sequence may introduce `v1alpha2`, `v1beta1`, and similar
formats without mutating an earlier checked-in schema. Once
`qhapaq.operation-descriptor/v1` is published, its schema and semantics are
immutable. A breaking post-v1 change publishes `v2`; supported generators and
hosts may continue to accept `v1` and `v2` side by side.

## 14. Validation and Plan Binding

Validation occurs in these ordered stages:

1. Parse JSON and reject duplicate object member names.
2. Validate the pipeline document against its exact format schema.
3. Validate node identities, structural rules, scopes, and bounded control flow.
4. Resolve every exact operation and decorator contract.
5. Validate operation and decorator configuration.
6. Propagate schemas through structural nodes.
7. Validate transform sources, dominance, expressions, and output schemas.
8. Prove every operation connection schema-compatible.
9. Verify implementation-native input and output bindings.
10. Aggregate capabilities, side effects, idempotency, and resource budgets.
11. Evaluate active host policy and required connection availability.
12. Construct the immutable execution plan.

Validation reports four distinct conclusions:

- **document validity:** the definition conforms to the portable language;
- **host bindability:** the active host has matching trusted implementations and
  native bindings;
- **policy eligibility:** current policy would permit the planned capabilities
  and side effects; and
- **execution permission:** evaluated again for a specific invocation.

Document validity does not grant execution or payload-disclosure permission.
Changes to the effective registry, host profile, policy, connections, or
implementation integrity invalidate affected cached plans.

## 15. Structured Diagnostics

Validation diagnostics are versioned machine-readable values containing:

- stable diagnostic code;
- severity;
- node ID when applicable;
- JSON Pointer into the submitted definition;
- human-readable message;
- expected and actual schema summaries when applicable; and
- zero or more bounded remediation suggestions.

Example:

```json
{
  "code": "QHP-TYPE-004",
  "severity": "error",
  "nodeId": "create-order-input",
  "path": "/root/steps/2/expression/object/customerId",
  "message": "The expression may produce null, but the target property is required.",
  "expectedSchema": {
    "type": "string"
  },
  "actualSchema": {
    "type": ["string", "null"]
  },
  "suggestions": [
    "Use coalesce to provide a non-null value.",
    "Select a source property that is required."
  ]
}
```

Diagnostics must not contain operation payloads, credentials, resolved secrets,
or protected host configuration by default.

## 16. AI and MCP Authoring Surface

The MCP adapter exposes the same shared application services used by other
entry points. Its authoring surface supports:

- listing operation descriptors with filters for text, composition role,
  capabilities, side effects, schema characteristics, and availability;
- retrieving one complete exact-version descriptor;
- validating a pipeline without executing it;
- explaining resolved dataflow, transforms, effects, and prerequisites;
- rendering deterministic Mermaid from a validated definition; and
- comparing operation contracts for migration assistance.

Validation returns structured diagnostics, inferred node schemas, exact resolved
contracts and digests, aggregated effects and capabilities, and the four
validation conclusions from Section 14.

Pipeline creation and transformation tools return inert definitions. They do not
install extensions, mutate trusted profiles, resolve credentials, execute
operations, or grant authority.

Execution remains a separate policy-gated tool. A successful validation response
must not be represented as execution approval.

## 17. Canonicalization and Mermaid

Canonical definitions use the JSON Canonicalization Scheme defined by RFC 8785
after successful document validation and normalization. Duplicate member names,
non-conforming numeric values, and values that cannot be represented by the
canonicalization profile are invalid.

Canonicalization preserves all semantically significant array ordering,
including sequence steps, decorator nesting, and ordered mapping operands.
Object member ordering is canonicalized and is not semantic unless a future
format version explicitly says otherwise.

Mermaid is generated from the validated definition and shows:

- node IDs;
- exact operation IDs and contract versions;
- sequential and explicit data-dependency edges;
- parallel branches and joins;
- decorator nesting;
- conditional branches;
- loop boundaries and maximum iterations; and
- transform nodes with concise input and output summaries.

Mermaid is explanatory output and cannot be edited as an executable source.

## 18. Security and Privacy

- Treat pipeline documents, descriptors, examples, imported API metadata, and
  generated prose as untrusted input.
- Never execute source text or load an implementation named by a pipeline.
- Resolve operations only through the immutable effective registry.
- Require exact versions and reject conflicting contract digests.
- Keep credentials, secret references, and resolved secrets outside definitions,
  transforms, frames exposed to transforms, diagnostics, and generated views.
- Do not expose an execution frame through MCP or persist it as run history.
- Apply resource budgets to transforms, collections, loops, parallelism, frame
  storage, and output size.
- Bound expression depth, collection sizes, diagnostic counts, and schema
  complexity to resist denial of service.
- Validate complete structure, types, bindings, and policy before starting side
  effects.
- Revalidate execution permission and payload disclosure for every invocation.
- Do not treat extension isolation, attributes, source generators, or descriptor
  validation as a sandbox for untrusted executable code.

## 19. Compatibility and Evolution

Pipeline format versions are independent from pipeline versions, operation
contract versions, implementation versions, Service API versions, and package
versions.

Unknown format versions, node kinds, transform-language versions, mapping
operators, or normative schema keywords are rejected. A host must not silently
reinterpret a newer definition as v1.

Additive documentation metadata may evolve without changing execution semantics.
Any change that alters canonical execution meaning requires a new pipeline
format or transform-language version with explicit migration tooling.

Persisted definitions remain the source of truth. Cached plans are disposable
and must be rebuilt when their definition digest, registry generation, policy,
host profile, connection bindings, implementation identity, or contract digest
changes.

## 20. Testing and Conformance

The language-neutral conformance suite includes:

- valid and invalid pipeline-document vectors;
- canonicalization and duplicate-member tests;
- node-ID, scope, dominance, and inaccessible-branch tests;
- sequence, parallel, decorator, conditional, and bounded-loop vectors;
- transform parsing, type inference, nullability, conversion, and failure tests;
- explicit multi-output and final-output projection tests;
- conservative schema-compatibility vectors;
- exact-version and contract-digest conflict tests;
- operation-contract compatibility-diff vectors;
- structured diagnostic golden files;
- Mermaid golden files;
- registry and native-binding rejection tests;
- plan-cache invalidation tests; and
- security tests proving definitions cannot load code, access credentials,
  escape transform scope, or begin side effects before complete validation.

The .NET reference implementation additionally tests:

- descriptor JSON as the sole authoritative descriptor source;
- exact same-directory and basename association between an operation and its
  descriptor;
- structural validation against every supported offline descriptor schema;
- static descriptor declarations without operation construction or project-code
  execution during generation;
- required generator diagnostics and invalid-build-input rejection;
- generated source and canonical manifest reproducibility across machines,
  cultures, paths, and input enumeration orders;
- byte equality between embedded and packaged manifests;
- explicit reflection-free registration of built-in and extension operations;
- rejection of referenced assemblies that lack an explicitly enabled generated
  registration entry point;
- generator support-matrix behavior for supported, mixed, and unknown descriptor
  formats;
- registration-contract and manifest-envelope compatibility rejection;
- runtime revalidation of generated manifests and contract digests;
- generic native type and schema agreement;
- trimming and Native AOT compatibility; and
- OpenAPI and code-authored operations producing equivalent portable
  descriptors.

## 21. Rollout and Migration

Implementation proceeds in this order:

1. Publish the normative pipeline, mapping, descriptor, and diagnostic schemas.
2. Publish conformance vectors and canonical examples.
3. Publish the .NET descriptor-authoring schema, incremental generator,
   compatibility matrix, diagnostics, generated-manifest format, and
   effective-registry validation.
4. Implement document parsing and non-executing validation.
5. Implement transforms and execution-frame dataflow.
6. Implement immutable plan binding and cache invalidation.
7. Add Mermaid, CLI, and MCP authoring projections.
8. Enable policy-gated execution only after the complete validation path exists.

No compatibility migration is required because no portable pipeline format has
yet been released. Illustrative pre-v1 documents are not accepted as an implicit
legacy format.

Rollback disables plan execution or reverts the implementation while preserving
portable definitions. Derived plans may always be discarded and rebuilt.

## 22. Alternatives Considered

### General ambient operation context

Passing a mutable context or service locator to every operation would hide data
dependencies and weaken portability, testing, and AI reasoning. Qhapaq instead
keeps invocation data in explicit operation inputs and transform bindings while
the engine retains private run state.

### Only the immediately preceding value

Restricting transforms to the preceding output cannot construct results from
multiple earlier operations. Explicit named bindings provide that capability
while keeping dependencies statically visible.

### Persist every intermediate value

Treating the execution frame as a durable result store would add retention,
privacy, recovery, and versioning semantics outside v1. The frame is ephemeral,
private, and lifetime-managed.

### Embedded C#, JavaScript, or another scripting language

Embedded code prevents portable static validation and introduces compilation,
sandboxing, injection, and reproducibility problems. The constrained mapping
language covers data shaping without becoming a general runtime.

### JSON values between every operation

This simplifies dynamic composition but discards native type safety and adds
serialization overhead. Qhapaq serializes only at declared boundaries such as
transforms, CLI, MCP, and persistence.

### Complete descriptors encoded as .NET attributes

Attributes are suitable markers but cannot cleanly represent nested schemas,
examples, structured failures, and evolving metadata. Static declarations give
code authors strong co-location without requiring instance construction or
runtime scanning.

### Descriptor instance methods on `IOperation`

Instance methods require or encourage operation construction for discovery,
mix execution with registry concerns, and apply descriptor requirements to
internal combinators and test operations. A separate static declaration contract
keeps `IOperation` focused.

### Automatic compatible-version substitution

Substituting a newer compatible contract makes reviewed pipelines change without
an explicit edit. Compatibility metadata supports migration but never overrides
an exact pipeline reference.

## 23. Open Questions

1. Which precise JSON Schema Draft 2020-12 keywords and formats belong to the v1
   Qhapaq profile?
2. What is the complete `qhapaq.mapping/v1` operator set and complexity budget?
3. Which capability, side-effect, idempotency, and structured-failure
   vocabularies are normative?
4. What are the exact public .NET declaration-contract and marker-attribute type
   names, generated API names, stable generator diagnostic codes, and initial
   generator compatibility matrix?
5. What are the exact CLI commands and MCP tool request and response schemas?
