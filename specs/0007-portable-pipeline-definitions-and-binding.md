# SPEC-0007: Portable Pipeline Definitions and Plan Binding

> **Status:** Draft
>
> **Target:** Qhapaq v1
>
> **Last updated:** 2026-10-06

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
- Permit a pipeline format to compose mapping sites that use different exact
  mapping-language versions without implicitly migrating untouched sites.
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
- **Mapping site:** a transform node, final output projection, or future
  explicitly specified record that contains one mapping expression and selects
  its exact mapping-language version locally.
- **Caught-failure projection:** a fixed, non-sensitive portable value made
  available as an explicit transform source only within the recovery subtree of
  a `tryCatch` node.
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
- an optional normative `mappingLimits` object;
- `schemas.input` and `schemas.output`;
- one `root` composition expression; and
- an optional explicit `output` projection.

Unknown properties are rejected unless the normative pipeline JSON Schema
explicitly permits them.

The example assumes that the exact resolved contract for
`contoso.customers.get` version `1.2.0` guarantees a required string output
property named `id`, and that the contract for `contoso.pricing.calculate`
version `2.0.0` guarantees a required numeric output property named `total`.
The pipeline input schema above guarantees the required string property
`requestedBy`.

Illustrative pipeline shape using the canonical mapping-expression syntax:

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
          "op": "object",
          "fields": {
            "customerId": {
              "op": "property",
              "value": {
                "op": "input",
                "name": "customer"
              },
              "name": "id"
            },
            "total": {
              "op": "property",
              "value": {
                "op": "input",
                "name": "pricing"
              },
              "name": "total"
            },
            "requestedBy": {
              "op": "property",
              "value": {
                "op": "input",
                "name": "request"
              },
              "name": "requestedBy"
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
      "op": "object",
      "fields": {
        "customerId": {
          "op": "property",
          "value": {
            "op": "input",
            "name": "customer"
          },
          "name": "id"
        },
        "orderId": {
          "op": "property",
          "value": {
            "op": "input",
            "name": "order"
          },
          "name": "id"
        }
      }
    }
  }
}
```

The normative pipeline JSON Schema must encode these exact property names and
the closed structural shapes in Section 6.3.

### 6.2 Node identities

Every node has a non-empty document-local `id`. Node IDs:

- are unique across the complete definition;
- are stable diagnostic and visualization anchors;
- do not select implementations;
- do not contribute to operation identity; and
- must not contain credentials or sensitive payload data.

Changing a node ID changes the canonical definition because bindings and
diagnostics may reference it.

Every node is a JSON object with required `id` and `kind` members plus only the
members defined for that exact node kind. Node and supporting-record member
names are case-sensitive. Unknown members are invalid.

The normative pipeline schema defines the node type as a closed recursive
discriminated union over the exact v1 `kind` values. Each union member fixes
`kind` to one value, requires that kind's operands, recursively validates its
inline structural children as nodes, and rejects members belonging to another
kind. Structural composition is an inline expression tree; structural children
cannot be replaced by node-ID references. Node-ID references are permitted only
where this specification explicitly defines a dataflow source.

Node IDs are unique across the complete definition, including every inline
child of the root, rather than only within one sequence, branch, conditional,
decorator, or loop. Duplicate JSON member names are rejected before the node
union is evaluated.

### 6.3 Structural node kinds

The v1 language supports:

- `operation`;
- `transform`;
- `sequence`;
- named `parallel` branches;
- `decorate`;
- `conditional`;
- `tryCatch`;
- bounded `loop`; and
- bounded `forEach`.

Combinators and transforms are language constructs, not catalog operations.
Registry descriptors use `primitive` or `decorator` as their composition role.

An operation reference always contains an operation ID and exact contract
version. Version ranges, aliases, and unspecified latest versions are invalid.

Decorator order is explicit and semantically significant. Parallel branch names
are stable members of the parallel result. Conditionals, loops, and bounded
collection execution follow the composition semantics in
[`0001-core-pipeline-model.md`](0001-core-pipeline-model.md).

#### 6.3.1 Operation

An `operation` node is a leaf with this exact shape:

```json
{
  "id": "get-customer",
  "kind": "operation",
  "operation": {
    "id": "contoso.customers.get",
    "version": "1.2.0"
  },
  "configuration": {
    "includeHistory": false
  }
}
```

`operation` is a closed exact contract reference containing only required `id`
and `version` members. The referenced descriptor must have the `primitive`
composition role. The same exact-reference shape is used by `decorate` nodes
for decorator contracts. The containing member identifies the required
composition role.

Every v1 operation and decorator configuration schema is an object schema.
`configuration` is optional in an operation node. Omission is normalized to an
empty object before configuration defaults are materialized, and the normalized
configuration is validated and included in canonicalization. An explicitly
supplied configuration must be an object. Unknown operation-node,
exact-reference, and configuration members are rejected according to their
respective closed schemas.

#### 6.3.2 Transform

A `transform` node has this exact shape:

```json
{
  "id": "create-order-input",
  "kind": "transform",
  "language": "qhapaq.mapping/v1",
  "inputs": {
    "customer": {
      "source": "node",
      "node": "get-customer"
    },
    "request": {
      "source": "pipeline-input"
    }
  },
  "outputSchema": {
    "type": "object",
    "required": ["customerId"],
    "properties": {
      "customerId": { "type": "string" }
    },
    "additionalProperties": false
  },
  "expression": {
    "op": "object",
    "fields": {
      "customerId": {
        "op": "property",
        "value": {
          "op": "input",
          "name": "customer"
        },
        "name": "id"
      }
    }
  }
}
```

`language`, `inputs`, `outputSchema`, and `expression` are required.
`language` is exactly `qhapaq.mapping/v1`. `inputs` is a closed map whose keys
match `^[a-z][A-Za-z0-9]*$`; an input-free transform explicitly uses an empty
map. Each value in `inputs` is exactly one member of this closed source union:

```json
{ "source": "pipeline-input" }
```

```json
{ "source": "current-input" }
```

```json
{ "source": "node", "node": "get-customer" }
```

Within the `catch` subtree of a `tryCatch`, the union additionally permits:

```json
{ "source": "caught-failure" }
```

A node source contains only `source` and `node`; pipeline-input,
current-input, and caught-failure sources contain only `source`.
`current-input` is the value received by the transform through its enclosing
composition edge. At the root it is the boundary input. Within a `forEach`
body it is the current item or chunk. At the root of a `tryCatch` catch subtree
it is the original `tryCatch` input. A node source must identify an accessible
node that dominates the transform. A caught-failure source is valid only in
the lexical scope defined in Section 6.3.7. `outputSchema` is an inline schema
conforming to the Qhapaq v1 schema profile. `expression` is one canonical
`qhapaq.mapping/v1` operator object. Its `input` operators may name only keys
from the containing `inputs` map.

Because transforms have no implicit data sources, a transform with an empty
`inputs` map can produce only a deterministic value derived from public
literals. The inferred successful expression result must conform to
`outputSchema`, and the internal `missing` state cannot escape as output.
Unknown transform-node and source members are invalid.

#### 6.3.3 Sequence

A `sequence` node has this exact shape:

```json
{
  "id": "order-flow",
  "kind": "sequence",
  "steps": [
    {
      "id": "create-order-input",
      "kind": "transform",
      "language": "qhapaq.mapping/v1",
      "inputs": {},
      "outputSchema": {
        "type": "object",
        "required": [],
        "properties": {},
        "additionalProperties": false
      },
      "expression": {
        "op": "object",
        "fields": {}
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
}
```

`steps` is required and contains at least one inline node. Array order is
semantic execution order. The first step receives the sequence input. Each
later step begins only after its preceding step succeeds and receives that
step's output under the composition semantics of its node kind. Every adjacent
connection must be schema-compatible; the binder does not insert conversions.
A transform step continues to read only its explicitly declared sources.

A one-step sequence is valid and has the same input, output, failure, and
cancellation behavior as its single step. The sequence output is its final
step's output. An empty sequence is invalid and has no implicit identity or
pass-through behavior. Unknown sequence-node members are invalid.

#### 6.3.4 Parallel

A `parallel` node has this exact shape:

```json
{
  "id": "load-order-data",
  "kind": "parallel",
  "branches": {
    "customer": {
      "id": "load-customer",
      "kind": "operation",
      "operation": {
        "id": "contoso.customers.get",
        "version": "1.2.0"
      }
    },
    "pricing": {
      "id": "load-pricing",
      "kind": "operation",
      "operation": {
        "id": "contoso.pricing.calculate",
        "version": "2.0.0"
      }
    }
  }
}
```

`branches` is required and is a closed map containing at least two entries.
Each key matches `^[a-z][A-Za-z0-9]*$` and is the stable branch name and
parallel-result member name. Each value is one inline node. Every branch
receives the same parallel-node input and may execute concurrently. A branch
cannot access a sibling branch's outputs.

Branch-map member order is not semantic and does not determine start,
completion, or result order. Deterministic projections, diagnostics, branch
summaries, and aggregate-failure reporting order branches by ordinal branch
name. Reordering members without changing their names or values does not change
the canonical definition. Unknown parallel-node members are invalid.

The parallel node succeeds only when every branch succeeds and produces an
object whose members are the named branch outputs. If any branch fails, the
runtime signals cancellation to the remaining branches, observes every branch,
and reports every non-sibling-cancellation failure in deterministic branch-name
order rather than producing a partial result.

#### 6.3.5 Decorate

A `decorate` node has this exact shape:

```json
{
  "id": "retry-create-order",
  "kind": "decorate",
  "decorator": {
    "id": "qhapaq.retry",
    "version": "1.0.0"
  },
  "configuration": {
    "maxAttempts": 3
  },
  "inner": {
    "id": "create-order",
    "kind": "operation",
    "operation": {
      "id": "contoso.orders.create",
      "version": "3.1.0"
    }
  }
}
```

`decorator` and `inner` are required. `decorator` uses the closed exact
contract-reference shape defined for operation nodes, and the referenced
descriptor must have the `decorator` composition role. `inner` is exactly one
inline node. The decorator must preserve the inner node's input and output
contracts.

`configuration` is optional and follows the same object-only omission,
normalization, default-materialization, validation, and canonicalization rules
as operation configuration. Multiple decorators are represented only by
nesting `decorate` nodes. Each nested decorator is a node with its own globally
unique node ID. Nesting order is semantic: the outer `decorate` node wraps its
`inner` node after the complete inner node, including any nested decorator, is
bound. Unknown decorate-node members are invalid.

#### 6.3.6 Conditional

A `conditional` node has this exact shape:

```json
{
  "id": "choose-fulfillment",
  "kind": "conditional",
  "outputSchema": {
    "type": "object",
    "required": ["fulfillmentId", "fulfillmentType"],
    "properties": {
      "fulfillmentId": {
        "type": "string"
      },
      "fulfillmentType": {
        "type": "string",
        "enum": ["physical", "digital"]
      }
    },
    "additionalProperties": false
  },
  "condition": {
    "id": "requires-shipping",
    "kind": "operation",
    "operation": {
      "id": "contoso.orders.requires-shipping",
      "version": "1.0.0"
    }
  },
  "whenTrue": {
    "id": "ship-order",
    "kind": "operation",
    "operation": {
      "id": "contoso.orders.ship",
      "version": "1.0.0"
    }
  },
  "whenFalse": {
    "id": "complete-digital-order",
    "kind": "operation",
    "operation": {
      "id": "contoso.orders.complete-digital",
      "version": "1.0.0"
    }
  }
}
```

`outputSchema`, `condition`, `whenTrue`, and `whenFalse` are required.
`outputSchema` is an inline schema conforming to the Qhapaq v1 schema profile
and is the conditional node's declared output contract. `condition`,
`whenTrue`, and `whenFalse` are inline nodes.
`condition` may be any structural node whose output schema is exactly a
required, non-null Boolean or a schema statically proven to admit only Boolean
values. A transform condition may explicitly bind accessible dominating node
outputs under the ordinary transform source and scope rules.

The condition receives the conditional-node input and executes exactly once.
Only the selected branch executes, and it receives the original
conditional-node input rather than the condition output. Both branches must
accept that input.

During schema propagation, the binder derives the complete output schema of
each branch according to its outer node kind. A sequence contributes its final
step's output schema, and a parallel contributes its closed object schema of
named branch outputs. The binder must independently prove, using the
deterministic structural-subtype compatibility algorithm, that every successful
value admitted by each derived branch output schema conforms to
`outputSchema`:

```text
whenTrue.output  subset-of  conditional.outputSchema
whenFalse.output subset-of  conditional.outputSchema
```

Schema equality is sufficient but not required. An unsupported or
indeterminate comparison is incompatible. The binder must not infer, synthesize,
widen, or choose a common output schema from the two branches. Authors must
declare the intended contract and, when a branch's natural result has a
different shape, use an explicit transform within that branch to normalize its
outer result before the conditional boundary. For example, a branch that
performs parallel work can use a sequence whose parallel step is followed by a
normalizing transform.

Failure of either branch proof is a document-validation error associated with
the conditional and the incompatible branch. Validation must report the
declared `outputSchema` as the expected schema and the derived branch output
schema as the actual schema. No operation may begin for a definition that fails
this proof.

The conditional node's propagated output schema is exactly its declared
`outputSchema`. Only the selected branch executes at runtime, and its successful
result becomes the conditional result under that contract. Branch-local outputs
do not escape directly; downstream consumers reference the conditional node's
output. Unknown conditional-node members are invalid.

#### 6.3.7 Try/catch recovery

A `tryCatch` node has this exact shape:

```json
{
  "id": "reserve-or-backorder",
  "kind": "tryCatch",
  "outputSchema": {
    "type": "object",
    "required": ["orderId", "status"],
    "properties": {
      "orderId": { "type": "string" },
      "status": {
        "type": "string",
        "enum": ["reserved", "backordered"]
      },
      "failureCode": { "type": "string" }
    },
    "additionalProperties": false
  },
  "try": {
    "id": "reserve-inventory",
    "kind": "operation",
    "operation": {
      "id": "contoso.inventory.reserve",
      "version": "1.0.0"
    }
  },
  "catch": {
    "id": "create-backorder-input",
    "kind": "transform",
    "language": "qhapaq.mapping/v1",
    "inputs": {
      "request": { "source": "current-input" },
      "failure": { "source": "caught-failure" }
    },
    "outputSchema": {
      "type": "object",
      "required": ["orderId", "status", "failureCode"],
      "properties": {
        "orderId": { "type": "string" },
        "status": {
          "type": "string",
          "const": "backordered"
        },
        "failureCode": { "type": "string" }
      },
      "additionalProperties": false
    },
    "expression": {
      "op": "object",
      "fields": {
        "orderId": {
          "op": "property",
          "value": { "op": "input", "name": "request" },
          "name": "orderId"
        },
        "status": {
          "op": "literal",
          "value": "backordered"
        },
        "failureCode": {
          "op": "property",
          "value": { "op": "input", "name": "failure" },
          "name": "code"
        }
      }
    }
  }
}
```

`outputSchema`, `try`, and `catch` are required. `outputSchema` is an inline
schema conforming to the Qhapaq v1 schema profile and is the `tryCatch` node's
declared output contract. `try` and `catch` are inline nodes. Both must accept
the original `tryCatch` input. The root of the selected subtree receives that
input through its ordinary composition edge; `tryCatch` does not wrap or
replace it with a failure-context object.

The binder derives the complete output schema of each child according to its
outer node kind and independently proves:

```text
try.output   subset-of tryCatch.outputSchema
catch.output subset-of tryCatch.outputSchema
```

The proof, diagnostics, normalization requirements, and prohibition on
inferring or widening a common schema are the same as for conditional branches.
The `tryCatch` node's propagated output schema is exactly its declared
`outputSchema`.

The `try` child executes exactly once. If it succeeds, its result becomes the
`tryCatch` result and `catch` does not execute. If it terminates with a catchable
failure, the `catch` child executes exactly once with the original `tryCatch`
input. If `catch` succeeds, its result becomes the successful `tryCatch` result.
If `catch` fails or is cancelled, that terminal outcome becomes the
`tryCatch` outcome. The runtime must observe and retain the causal relationship
to the original try failure for bounded, payload-safe diagnostics; it must not
silently discard, relabel, or expose raw exception data from that failure.

Catchable failures are declared operation failures, mapping runtime failures,
decorator failures after the decorator has completed its own handling, bounded
structural-control failures, and aggregate failures produced by nodes in the
`try` subtree. Invocation cancellation, policy or authorization denial,
exhaustion of a run-wide host budget, implementation contract violations, and
unexpected host or implementation faults are not catchable. A non-catchable
outcome never starts `catch` and propagates unchanged. If invocation
cancellation is requested after a catchable try failure but before `catch`
starts, `catch` does not start and the invocation reports cancellation.

Within the complete lexical `catch` subtree, a transform may explicitly bind:

```json
{ "source": "caught-failure" }
```

This source is invalid everywhere else. It resolves to the nearest lexically
enclosing active `tryCatch`; nested catch scopes shadow outer caught failures.
It is not an addressable node output, cannot be selected by node ID, and does
not make partially completed try-child outputs accessible. Try-local and
catch-local outputs do not escape directly; only the `tryCatch` result does.

The caught-failure projection has this fixed successful-value schema:

```json
{
  "type": "object",
  "required": [
    "format",
    "category",
    "code",
    "sourceNodeId",
    "retryDisposition",
    "effectOutcome"
  ],
  "properties": {
    "format": {
      "type": "string",
      "const": "qhapaq.failure/v1"
    },
    "category": {
      "type": "string",
      "enum": ["operation", "mapping", "control", "aggregate"]
    },
    "code": {
      "type": "string",
      "minLength": 1,
      "maxLength": 256
    },
    "sourceNodeId": {
      "type": "string",
      "minLength": 1
    },
    "retryDisposition": {
      "type": "string",
      "enum": [
        "qhapaq.retry.transient",
        "qhapaq.retry.permanent",
        "qhapaq.retry.unknown"
      ]
    },
    "effectOutcome": {
      "type": "string",
      "enum": [
        "qhapaq.effect-outcome.none",
        "qhapaq.effect-outcome.occurred",
        "qhapaq.effect-outcome.unknown"
      ]
    }
  },
  "additionalProperties": false
}
```

`category` classifies the originating portable failure: `operation` for a
failure declared by an operation contract, `mapping` for a mapping runtime
failure, `control` for a decorator or bounded structural-control failure, and
`aggregate` when a structural node reports multiple failures. `code` is the
stable machine-readable code of the caught failure; an aggregate uses the
reserved aggregate-failure code defined by the structured-failure vocabulary
rather than selecting one child failure. `sourceNodeId` identifies the node
that reported the caught failure or aggregate. `retryDisposition` and
`effectOutcome` have the exact meanings defined in Section 15.2. The projection
does not contain an operation input or output, exception type, stack trace,
arbitrary exception message, connector response body, credential, resolved
configuration, nested aggregate causes, recovery causality, or
operation-specific failure payload.

A failure remains a control signal rather than a mapping value while it is
being raised. An enclosing `tryCatch` creates the caught-failure projection
only after catching that signal. Consequently, a mapping expression still
cannot catch its own failure; a transform in the catch subtree may only read
the already-created projection through an explicitly declared input source.

Validation and policy evaluation include both children before execution.
Capabilities, connections, and possible side effects are the union of both
children; idempotency uses the risk-summary precedence in Section 11.7.
Worst-case resource and operation-count planning must permit the `try` child
followed by the `catch` child rather than treating them as mutually exclusive
successful alternatives. A caught failure does not roll back, compensate, or
imply transactional isolation for side effects that the `try` subtree already
produced. Unknown `tryCatch` members are invalid.

#### 6.3.8 Bounded loop

A `loop` node has this exact shape:

```json
{
  "id": "process-pages",
  "kind": "loop",
  "maxIterations": 100,
  "condition": {
    "id": "has-more-pages",
    "kind": "operation",
    "operation": {
      "id": "contoso.pages.has-more",
      "version": "1.0.0"
    }
  },
  "body": {
    "id": "process-next-page",
    "kind": "operation",
    "operation": {
      "id": "contoso.pages.process-next",
      "version": "1.0.0"
    }
  }
}
```

`maxIterations`, `condition`, and `body` are required. `maxIterations` is a
positive JSON integer no greater than `9007199254740991`, the maximum portable
integer in the Qhapaq JSON data model. Each host profile advertises the maximum
iteration request that it can bind or permit. A pipeline requesting a larger
value remains document-valid but is host-unbindable or policy-ineligible; a
host limit does not change portable document validity.

`condition` and `body` may each be any inline structural node. Both receive the
current loop state. The condition output must be exactly a required, non-null
Boolean or a schema statically proven to admit only Boolean values. The body
must accept the loop-state schema and produce a value compatible with that same
schema.

The condition evaluates before each iteration. If it is false initially, the
body does not execute and the input state is the successful loop output. After
each successful body execution, its output becomes the state for the next
condition evaluation. If the condition remains true after exactly
`maxIterations` successful body executions, the loop fails with its declared
limit rather than returning a partial result.

Each iteration has an iteration-local frame. Child outputs do not escape an
iteration, and only the final loop state becomes the loop-node output. Unknown
loop-node members are invalid. Arbitrary graph cycles and unbounded loops are
invalid.

#### 6.3.9 Bounded collection execution

A `forEach` node in chunk mode has this exact shape:

```json
{
  "id": "price-order-lines",
  "kind": "forEach",
  "inputMode": "chunk",
  "maxItems": 10000,
  "chunkSize": 100,
  "maxConcurrency": 4,
  "body": {
    "id": "price-order-line-chunk",
    "kind": "operation",
    "operation": {
      "id": "contoso.pricing.price-line-chunk",
      "version": "1.0.0"
    }
  }
}
```

`inputMode`, `maxItems`, `maxConcurrency`, and `body` are required.
`inputMode` is exactly `item` or `chunk`. `maxItems` and `maxConcurrency` are
positive JSON integers no greater than `9007199254740991`. `body` is exactly
one inline node.

When `inputMode` is `item`, `chunkSize` is prohibited. The body executes once
for each input-array item and receives that item. When `inputMode` is `chunk`,
`chunkSize` is required and is a positive JSON integer no greater than
`9007199254740991`. The runtime partitions the input array into consecutive,
non-overlapping chunks of at most `chunkSize` items without reordering them.
The body executes once for each non-empty chunk and receives that chunk as an
array. An empty input executes no body invocation in either mode.

The `forEach` input contract is the propagated upstream homogeneous-array
schema with its `maxItems` additionally constrained to this node's `maxItems`.
The upstream schema must have effective type `array`, must declare `items`, and
must have a finite maximum cardinality no greater than the node's `maxItems`;
otherwise the connection is incompatible. In item mode, the body must accept
the upstream `items` schema. In chunk mode, the body must accept an array with
the same `items` schema, `minItems` equal to one, and `maxItems` equal to the
declared `chunkSize`. The binder does not insert conversions.

The binder derives the body output schema according to its outer node kind.
The `forEach` output schema is a homogeneous array whose `items` is that
derived body output schema. In item mode its minimum and maximum cardinalities
equal the input schema's minimum and maximum cardinalities. In chunk mode they
are `ceiling(input.minItems / chunkSize)` and
`ceiling(input.maxItems / chunkSize)`, respectively. An omitted input
`minItems` is zero for this calculation. These bounds describe successful
outputs; runtime cardinality validation remains required.

`maxItems` is an invocation-time upper bound on input cardinality. The runtime
must determine and validate the complete input-array cardinality against
`maxItems` before any body invocation begins. Exceeding `maxItems` is an
execution-budget failure and starts no body invocation. In item mode, a valid
input of length `n` causes exactly `n` body invocations and produces exactly
`n` output items. In chunk mode, it causes exactly
`ceiling(n / chunkSize)` body invocations and produces that many output items.
Each output item is the complete output of one body invocation. V1 never
flattens, merges, filters, or omits body outputs implicitly.

Body invocations may execute concurrently, but no more than
`maxConcurrency` invocations of this node may be active at once. A host may
execute fewer, including one at a time, without changing portable semantics.
Completion order is not semantic. The successful output array is ordered by
source item index in item mode and by ascending source chunk start index in
chunk mode, regardless of start or completion order.

This ordered array is a logical result contract, not a required insertion
algorithm or intermediate storage layout. Because the work count is known
before body execution, an implementation may preallocate indexed result slots,
retain indexed completion records, assemble ordered segments, or use another
bounded representation that produces the same observable array. Aggregation
need not copy a body output solely to place it in the result. Intermediate
storage is not observable, may remain segmented through compatible native
bindings or serialization, and must still obey memory and output budgets. The
complete aggregate becomes available to downstream nodes only after every body
invocation succeeds.

Each body invocation has an invocation-local frame. Its inline node IDs remain
globally unique definition identities, while runtime occurrences are
distinguished by their zero-based work index. A body may read its
`current-input`, the boundary pipeline input, and values from dominating outer
scopes. It cannot read another body invocation's outputs. Body-local outputs do
not escape individually; only the ordered `forEach` result becomes the node
output.

On the first observed non-cancellation body failure, the runtime stops starting
new body invocations, signals cancellation to every active sibling invocation,
and observes every invocation that started. It reports every non-cancellation
failure from started invocations in ascending work-index order and produces no
partial result. Cancellation caused only by a sibling failure is not an
additional failure. If invocation cancellation is requested, the runtime stops
starting work, signals every active invocation, observes them, and reports
cancellation when no started invocation reports a non-cancellation failure.
Cancellation does not guarantee that an active invocation or its side effects
stop immediately. V1 provides no retry, rollback, compensation, or
partial-success semantics for this node; those require explicit operations or
decorators.

The binder computes the node's maximum body-invocation count as `maxItems` in
item mode and `ceiling(maxItems / chunkSize)` in chunk mode. It includes that
bound, `maxConcurrency`, nested structural bounds, repeated capabilities, and
possible repeated side effects in plan budgets and policy evaluation. Each
body invocation uses the ordinary limits of its nested nodes and mapping sites,
while all invocations share the run's aggregate duration, parallelism, memory,
frame, operation-count, and output budgets. Nested `forEach` nodes do not
receive fresh aggregate host budgets. Input chunks, in-flight results, and the
ordered aggregate count toward host memory and output-size budgets. Exhausting
any aggregate host budget fails the node and produces no partial result.

Host profiles advertise the largest `maxItems` and `chunkSize` requests they
can bind. A larger request remains document-valid but is host-unbindable or
policy-ineligible. `maxConcurrency` is a local ceiling rather than a guaranteed
degree of parallelism; the host's lower run-wide parallelism limit remains in
force. Unknown `forEach` members and invalid member combinations are invalid.

## 7. Execution Frame and Dataflow

### 7.1 Immutable slots

Each run has a private execution frame containing:

- the validated boundary input; and
- one immutable output slot for every successfully completed node whose value is
  still required.

A runtime node occurrence writes its output slot at most once. Loop iterations
and `forEach` body invocations create distinct local occurrences of their
inline nodes and therefore distinct local slots. A consumer cannot mutate a
stored value through the execution-frame contract. The frame is engine state,
not a general operation context and not an externally inspectable result store.

The engine must not automatically log, serialize, persist, or disclose frame
values. Payload-disclosure policy applies independently from execution
permission.

### 7.2 Explicit transform inputs

A transform declares a map of local input names to sources. A source is either:

- `pipeline-input`; or
- `current-input`; or
- the output of a named node that dominates the transform; or
- `caught-failure` when the transform is lexically within a `tryCatch` catch
  subtree.

The mapping expression reads only its declared `$inputs` values and literals.
It cannot enumerate the execution frame or access an undeclared node.

`current-input` is the value the transform receives from its enclosing
composition edge. The immediately preceding sequence output may be supported as
authoring shorthand for this source, but canonical JSON must represent or
deterministically normalize it to an explicit `current-input` source.

### 7.3 Dominance and scope

Sequential nodes may reference earlier nodes in the same enclosing sequence
when those nodes dominate the consumer.

A node after a parallel join may reference the completed result of every named
branch. A node inside one parallel branch cannot reference a sibling branch.

Branch-local conditional outputs do not escape directly. The conditional
produces the contract declared by its `outputSchema`, and downstream consumers
reference that conditional output. Both branches must be statically proven
compatible with that contract before execution. The binder does not derive a
common contract from the branch schemas.

Try-local and catch-local outputs do not escape directly. A catch subtree
cannot reference a partially completed node in its sibling try subtree. The
`tryCatch` produces the contract declared by its `outputSchema`, and downstream
consumers reference only that output. A caught failure is available only
through an explicit `caught-failure` transform source in the lexical catch
scope; it is not a frame slot or a generally addressable node output.

Each loop iteration has an iteration-local frame. The loop body may read the
current loop state, the pipeline input, and values defined in dominating outer
scopes. Only the final loop result escapes. Retaining per-iteration outputs
requires an explicit `forEach` node or operation; the engine does not retain
iteration history implicitly.

Each `forEach` body invocation has an invocation-local frame. The body may read
its current item or chunk, the pipeline input, and values defined in dominating
outer scopes. Work items cannot read one another's outputs. Only the ordered
aggregate result escapes.

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

Every expression is a JSON object with an `op` member whose value is one exact
operator name. Each operator schema defines its remaining named operands and
rejects unknown members. Literal values use an explicit `literal` operator
rather than being confused with expression objects. Operator objects are the
only executable syntax; strings never contain JSONPath, source code, or another
expression language.

The canonical foundational operator shapes are:

```json
{ "op": "input", "name": "customer" }
```

```json
{
  "op": "property",
  "value": { "op": "input", "name": "customer" },
  "name": "id"
}
```

```json
{ "op": "literal", "value": { "source": "web", "priority": 1 } }
```

```json
{
  "op": "object",
  "fields": {
    "customerId": {
      "op": "property",
      "value": { "op": "input", "name": "customer" },
      "name": "id"
    }
  }
}
```

`input.name` is one exact key from the containing transform's `inputs` map.
`property.value` is any mapping expression, and `property.name` is one literal
JSON object member name rather than a path. `object.fields` maps each result
member name to one mapping expression. `literal.value` is the only operand in
which an arbitrary JSON value is interpreted as data rather than as an
expression. Operator and operand names are case-sensitive.

The versioned mapping-expression schema is a closed discriminated union over
the allowed `op` values. It validates each operator's required named operands,
recursively validates expression-valued operands, and rejects unknown members.
It does not enumerate child operators according to the result type required by
a parent. The mapping type checker separately infers child result schemas and
validates context-dependent requirements, such as whether `property.value`
produces an object and whether that object's schema permits `property.name`.

Declared transform inputs are read with an `input` operator naming exactly one
key from the transform's `inputs` map. Nested object values are read by
composing one `property` operator per property name. Canonical expressions do
not encode access paths as JSONPath strings or another embedded path grammar.

Selecting an optional property produces a type that includes the internal
`missing` state. `missing` is not JSON `null`, is not a portable value, and
cannot appear in a transform output. The expression must handle it explicitly
with an operator such as `coalesce-missing`, a conditional, or
`require-present`. Selecting a property that is absent at runtime never
silently produces `null` and does not fail unless the expression explicitly
requires the property.

`coalesce-missing` evaluates its fallback only when its primary expression is
missing and does not replace JSON `null`. `coalesce-null` evaluates its fallback
only when its primary expression is JSON `null` and does not handle missing.
Their inferred result types remove only the state each operator handles.

`require-present` fails the transform when its input is missing and otherwise
passes the value through, including JSON `null`. `require-non-null` fails when
its input is JSON `null`, does not handle missing, and otherwise passes the
value through. Their inferred result types remove only the state each operator
checks.

Sections 8.5 through 8.10 define the complete v1 operator set, operand shapes,
evaluation order, result typing, value-state behavior, runtime failure behavior,
and explicitly deferred capabilities. The normative schema must enumerate
exactly those operators and shapes. Unknown operators are invalid.

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

An expression may contain a checked partial operation, such as parsing a number.
Such an operation must have specified failure behavior. A runtime value failure
terminates the transform before any downstream operation begins.

`assert-number-range` is the v1 checked narrowing operation for numeric values.
`assert-length` is the corresponding operation for string and array lengths.
Their declared bounds must be no wider than the statically inferred input
bounds. A value within the asserted bounds passes through unchanged and
receives the narrower result schema. A value outside the bounds fails the
transform; the binder never inserts either assertion implicitly.

`assert-integer` is the v1 checked narrowing operation from `number` to
`integer`. An integral input passes through as the same mathematical JSON number
with an integer result schema. A non-integral input fails the transform. The
binder never inserts this assertion implicitly.

`parse-number` accepts only the culture-invariant JSON number grammar used by
the Qhapaq canonical data model. It rejects leading or trailing whitespace,
digit-group separators, leading plus signs, `NaN`, and infinities. Authors who
intend to tolerate surrounding whitespace must compose an explicit `trim`
operator before parsing. A parse failure fails the transform before any
downstream operation starts.

V1 has no separate canonical `parse-integer` operator. Integer parsing composes
`parse-number` followed by `assert-integer`, preserving one responsibility and
one failure rule per operator.

`parse-boolean` accepts exactly the lowercase strings `"true"` and `"false"`.
It rejects surrounding whitespace, alternate casing, numeric spellings, and
localized values. Authors who intend to tolerate surrounding whitespace must
compose `trim` explicitly. A parse failure fails the transform before any
downstream operation starts.

`stringify` accepts any portable JSON value except the internal `missing` state.
Strings, including strings constrained by date, time, UUID, URI, or other
formats, remain unchanged. Numbers and Booleans use their RFC 8785 canonical
lexical forms, and JSON `null` produces `"null"`. Arrays and objects produce
their RFC 8785 canonical JSON text. V1 has no separate type-specific
stringification operators.

`trim` removes only the four JSON whitespace characters U+0009, U+000A,
U+000D, and U+0020 from the beginning and end of a string. It is not
locale-sensitive and does not remove any other Unicode whitespace.

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

### 8.5 Closed operator set and operand shapes

In this section, `expression` means one recursively valid
`qhapaq.mapping/v1` operator object. `identifier` uses the transform-input alias
grammar `^[a-z][A-Za-z0-9]*$`. Every operator object requires its listed members
and rejects members not listed as required or optional.

| Operators | Required operands | Optional operands |
| --- | --- | --- |
| `literal` | `value`: any JSON value | none |
| `input`, `variable` | `name`: identifier | none |
| `property` | `value`: expression; `name`: string | none |
| `item` | `value`: expression; `index`: expression | none |
| `object` | `fields`: map from member names to expressions | none |
| `array` | `items`: ordered expression array | none |
| `length` | `value`: expression | none |
| `is-missing`, `is-null`, `require-present`, `require-non-null`, `not`, `negate`, `trim`, `stringify`, `parse-number`, `parse-boolean`, `assert-integer` | `value`: expression | none |
| `coalesce-missing`, `coalesce-null` | `value`: expression; `fallback`: expression | none |
| `if` | `condition`: expression; `then`: expression; `else`: expression | none |
| `and`, `or`, `add`, `multiply`, `concat` | `values`: ordered array of at least two expressions | none |
| `equal`, `not-equal`, `deep-equal`, `less-than`, `less-than-or-equal`, `greater-than`, `greater-than-or-equal`, `subtract`, `divide`, `remainder` | `left`: expression; `right`: expression | none |
| `map` | `value`: expression; `itemName`: identifier; `expression`: expression | `indexName`: identifier |
| `filter` | `value`: expression; `itemName`: identifier; `predicate`: expression | `indexName`: identifier |
| `assert-number-range` | `value`: expression and at least one bound | `minimum` or `exclusiveMinimum`; `maximum` or `exclusiveMaximum` |
| `assert-length` | `value`: expression and at least one bound | `minimum`; `maximum` |
| `assert-format` | `value`: expression; `format`: allowed format name | none |

`property.name`, assertion bounds, and `assert-format.format` are literal
operands rather than expressions. Numeric-range bounds are finite JSON numbers.
At most one inclusive or exclusive bound may be supplied for each side.
Length bounds are non-negative integer literals. The lower bound must not
exceed the upper bound, accounting for exclusive numeric endpoints.

An empty `object.fields` map and an empty `array.items` array are valid.
`property.name` names one member and never contains a path. `item.index` must
infer as a required, non-null integer expression.

`map` and `filter` evaluate only arrays. `itemName` is required and names the
current element. `indexName`, when present, names its zero-based index.
`variable` may name only a collection variable in active lexical scope.
`itemName` and `indexName` must differ from each other, from every transform
input alias, and from every active outer collection-variable name. Shadowing is
invalid. A collection variable is in scope only within the containing
`expression` or `predicate`, including nested expressions.

`length` and `assert-length` accept only strings and arrays. String length is
the number of Unicode scalar values; array length is the number of elements.
Object member counts are unsupported.

`equal` and `not-equal` accept scalar JSON values only. Numeric operands use
mathematical numeric equality without conversion to another JSON type; all
other operands must have the same scalar type, and no string, Boolean, or null
coercion occurs. `deep-equal` requires two arrays or two objects of the same
composite kind and recursively compares their complete contents. Array order is
significant; object member order is not. Deep inequality composes `not` with
`deep-equal`.

The four ordered comparison operators accept numeric operands only. They do not
define string collation, temporal ordering, or composite ordering.

`property.value` must infer as an object. `item.value` must infer as an array.
`if.condition`, every `and` and `or` value, and `not.value` must infer as
Boolean. Numeric arithmetic operands must infer as `integer` or `number`.
`concat` values and `trim.value` must infer as strings. `parse-number` and
`parse-boolean` accept strings. `assert-integer` accepts a number;
`assert-number-range` accepts an integer or number; `assert-length` accepts a
string or array; and `assert-format` accepts a string. These requirements are
in addition to the presence and nullability requirements in Section 8.7.

### 8.6 Evaluation order

The abstract evaluation order is deterministic and sequential:

1. `left` is evaluated before `right`.
2. Expression arrays are evaluated from index zero upward.
3. `property` evaluates `value` first. `item` evaluates `value` before `index`.
4. `object.fields` are evaluated in RFC 8785 member-name order.
5. `add` and `multiply` are left folds in listed order. Implementations must not
   regroup operands.
6. `if` evaluates `condition` and only the selected branch.
7. `and` stops at the first false operand. `or` stops at the first true operand.
8. A coalescing operator evaluates `fallback` only when its specifically
   handled state occurs.
9. `map` and `filter` evaluate their source once, then process elements from
   index zero upward. `map` evaluates one expression per element. `filter`
   evaluates one predicate per element and preserves the relative order of
   retained elements.

The first runtime failure in this order terminates the transform. Unevaluated
operands and elements cannot fail and consume no evaluation budget. An
implementation may evaluate internally in another order or in parallel only
when the observable result, selected first failure, and budget consumption are
identical to the abstract order.

### 8.7 Static result inference

An inferred expression type consists of one normalized Qhapaq v1 schema and a
separate `mayBeMissing` Boolean. JSON `null` remains part of the schema type.
`missing` is never encoded as a schema type or keyword.

When an operator combines alternatives, the type checker derives the least
representable common super-schema under the closed v1 profile. It combines
nullability; promotes `integer` and `number` to `number`; widens numeric and
length intervals only enough to cover both alternatives; retains `format`,
`pattern`, and uniqueness constraints only when both alternatives guarantee
the same constraint; intersects required object members and recursively joins
the effective schemas of properties that either alternative may emit; and
recursively joins array item schemas. Equal `const` values remain `const`.
Different finite `const` or `enum` sets combine as their set union when the
result remains within the enum limit. Other constraints are retained only when
the schema-profile compatibility rules prove that they admit both
alternatives.

If alternatives have different concrete types other than `integer` and
`number`, or any recursive join has no representation in the v1 profile, the
expression is invalid. In particular, a constructed array cannot mix unrelated
element types. Inferred schemas omit documentation annotations.

The operator-specific inference rules are:

- `literal` infers the exact value as a `const`. `input` infers its declared
  source schema. An item `variable` infers the source array's item schema; an
  index variable infers a non-negative integer schema bounded by the source
  array's maximum when one is known.
- `property` infers the effective named-property or additional-property schema
  and sets `mayBeMissing` when the member is not required. Selecting a member
  forbidden by the input schema is invalid.
- `item` infers the array item schema. It sets `mayBeMissing` unless the inferred
  index bounds and source `minItems` prove that every possible index exists.
- `object` produces a closed object schema with every field required. `array`
  joins its item schemas and has its exact constructed length. A field or item
  expression that may be missing is invalid.
- `length` returns a non-negative integer with bounds derived from the source
  string or array.
- Presence and null tests return required, non-null Boolean values.
  Coalescing removes only its handled state from the primary and joins the
  remaining primary type with the fallback. Requirement operators remove only
  their checked state from successful results.
- `if` joins its branch types after guard refinement. Boolean operators return
  required, non-null Boolean values.
- Equality, ordered comparison, and `deep-equal` return required, non-null
  Boolean values.
- Numeric operators use interval arithmetic. `add`, `multiply`, `subtract`, and
  `negate` preserve `integer` when all applicable operands are integers;
  otherwise they infer `number`. `divide` and `remainder` infer `number`.
- `concat` returns a string with summed length bounds. `trim` returns a string
  with minimum length zero and a maximum no greater than the source maximum.
- `map` returns an array whose item schema is the mapped-expression schema and
  whose length bounds equal the source bounds. Its mapped expression may not
  produce missing. `filter` preserves the source item schema and maximum
  length, sets minimum length to zero, and requires a required, non-null Boolean
  predicate.
- Parsers return required, non-null `number` or Boolean results on success.
  `stringify` returns a required, non-null string. Checked assertions intersect
  the input schema with the asserted constraint and remove no unrelated state.
  `assert-format` may name only a format in the closed v1 allowlist.

Except for operators expressly defined to inspect, propagate, or handle
`missing` or JSON `null`, every operand must be statically proven present and
non-null. Successful-result inference is independent from whether a checked
partial operator may fail for a runtime value.

Guard-based narrowing applies to exact canonically identical expressions.
`is-missing` narrows presence, and `is-null` narrows nullability. `not` reverses
the true and false facts. `and` carries true facts left to right; `or` carries
false facts left to right. `if` checks its selected branch under the facts
established by the corresponding condition outcome. Facts from alternatives
are retained only when every path establishes the same fact.

### 8.8 `missing` and JSON `null`

`missing` is an internal evaluation state introduced only by selection or
propagation from a selection. It has no literal syntax, cannot enter through a
declared portable input, cannot be serialized, and never satisfies a schema.

An absent optional property produces `missing`. A negative or out-of-range
array index also produces `missing`; neither selection fails solely because the
selected value is absent. A selected JSON `null` remains null.

The state predicates are total and return:

| Operand state | `is-missing` | `is-null` |
| --- | --- | --- |
| `missing` | `true` | `false` |
| JSON `null` | `false` | `true` |
| any other JSON value | `false` | `false` |

`coalesce-missing` evaluates and returns its fallback only for `missing`; it
passes JSON `null` through. `coalesce-null` evaluates and returns its fallback
only for JSON `null`; it propagates `missing`. `require-present` fails for
`missing` and passes JSON `null`. `require-non-null` fails for JSON `null` and
propagates `missing`.

Scalar equality may compare JSON `null`, but an equality operand may not be
missing. `stringify` converts JSON `null` to `"null"` and does not accept
missing. Constructors and mapped array items may contain null only when their
inferred schemas permit it, and may never contain missing.

The final transform expression must be statically proven present. It may return
JSON `null` only when `outputSchema` permits null. No operator silently converts
missing to null or null to missing.

### 8.9 Runtime failures

A mapping runtime failure is distinct from a static validation error,
cancellation, and an unexpected host fault. V1 mapping failures are:

- a failed `require-present` or `require-non-null`;
- text rejected by `parse-number` or `parse-boolean`;
- a failed integer, numeric-range, length, or format assertion;
- division or remainder by zero, a non-finite numeric result, or an integer
  result outside the portable safe-integer domain; and
- exhaustion of a portable mapping evaluation or size limit.

Numeric arithmetic uses IEEE 754 binary64 round-to-nearest, ties-to-even, with
one rounding after each operation in the abstract evaluation order. Fused
operations or reassociation must not change a result. `remainder` uses a
quotient truncated toward zero. A computed negative zero is normalized to
zero. A result outside the portable numeric domain fails rather than producing
`NaN`, infinity, or a clamped value.

The first mapping failure terminates the transform immediately. No remaining
operand, collection element, downstream node, or native materializer starts.
Failures are not values and cannot be caught by a mapping expression.

A mapping failure's protected host diagnostic identifies the transform node,
operator, and expression JSON Pointer without reproducing operand values. That
diagnostic may include bounded, non-sensitive context such as a violated
assertion bound. The portable runtime failure contains only the exact stable
code and closed envelope defined in Section 15.2.

Runtime values are validated at portable boundaries. A value that violates a
schema the binder had already proven is reported as a host or implementation
contract failure, not as ordinary mapping input failure. Cancellation remains
cancellation, and an unexpected implementation exception remains a host fault;
neither is relabeled as a mapping failure.

### 8.10 Portable complexity and evaluation limits

`qhapaq.mapping/v1` defines fixed structural ceilings, portable runtime
defaults, and deterministic accounting rules. Structural ceilings bound
validation of an untrusted definition. Runtime limits bound each independent
mapping-site evaluation. Trusted host policy separately bounds aggregate work,
memory, duration, concurrency, and output across a complete run.

Expression depth is the number of operator objects on one path from the root
operator through expression-valued operands. The root operator has depth one,
and each child operator reached through an expression-valued operand increases
the depth by one. All branches, including unselected `if` branches,
short-circuitable operands, coalescing fallbacks, and `map` and `filter` bodies,
participate in static depth validation. JSON containers nested within
`literal.value` are data and do not increase expression depth. No v1 expression
may exceed 256 operator levels. This ceiling is fixed and cannot be raised by a
pipeline or host.

Operator count is the number of operator objects syntactically present in one
mapping site. Every branch and operand is counted, while a `map` or `filter`
body is counted once regardless of how many times it may run. JSON values
nested within `literal.value` are not operators. The default maximum is 4,096
operators per mapping site. A pipeline may request another effective maximum,
but no v1 mapping site may contain more than 65,536 operators. The fixed
65,536-operator ceiling cannot be raised by a pipeline or host.

`mappingLimits`, when present, is a closed top-level object whose members are
positive integers in the portable safe-integer domain. Its optional members
are:

| Member | V1 default | Meaning |
| --- | ---: | --- |
| `maxOperators` | 4,096 | Syntactic operators permitted in each mapping site; never greater than 65,536 |
| `maxCollectionElements` | 100,000 | Elements permitted in each array processed or produced by a mapping |
| `maxCollectionVisits` | 1,000,000 | Cumulative `map` and `filter` element visits in one evaluation |
| `maxStringScalars` | 1,000,000 | Unicode scalar values permitted in each string |
| `maxStringUtf8Bytes` | 4,194,304 | UTF-8 bytes permitted in each decoded string value |
| `maxValueUtf8Bytes` | 67,108,864 | RFC 8785 canonical UTF-8 bytes permitted in each produced composite value and final result |
| `maxEvaluationWork` | 10,000,000 | Abstract work units permitted in one evaluation |

An omitted `mappingLimits` object or omitted member uses the corresponding v1
default. An explicitly supplied value may be lower or higher than the default,
subject to the fixed operator ceiling and trusted host policy. The effective
values apply independently to every mapping site in the definition. They are
normative pipeline content and participate in canonicalization and the
definition digest.

Every conforming evaluator supports the v1 defaults. A pipeline value above a
default is an explicit host-capacity requirement, not permission it grants
itself. Before any operation starts, the binder must verify that the active
trusted host policy can provide every explicit limit exactly as written. If it
cannot, host bindability fails. A host must not silently clamp a requested
limit. Host policy may permit greater capacity, but doing so does not raise the
effective limits of a pipeline that omitted them or requested lower values.

The runtime collection rules are:

- An array that becomes the source of `map` or `filter` must not contain more
  than `maxCollectionElements` elements.
- Every array produced by `literal`, `array`, `map`, or `filter`, and every
  array returned as the final mapping result, must not contain more than
  `maxCollectionElements` elements. The rule applies recursively to arrays in
  produced literal and composite values.
- Immediately before a `map` body or `filter` predicate begins for an element,
  one collection visit is debited from the evaluation's shared
  `maxCollectionVisits` budget. Filtered-out elements count. Unevaluated
  elements do not.
- Nested collection operators share the same visit budget. No nested operator,
  branch, or collection element receives a fresh budget.

String length is the number of Unicode scalar values. String byte size is the
number of bytes in the UTF-8 encoding of the decoded scalar sequence, without
Unicode normalization. A string that becomes an operator result, occurs
recursively in a produced literal or composite value, or occurs in the final
mapping result must satisfy both `maxStringScalars` and
`maxStringUtf8Bytes`.

Value size is the number of bytes in the RFC 8785 canonical UTF-8
representation. Every composite value created by `literal`, `object`, `array`,
`map`, or `filter`, and the final mapping result, must satisfy
`maxValueUtf8Bytes`. Implementations may calculate size incrementally without
materializing canonical JSON, but must produce the same byte count and must
stop construction before exceeding the effective limit. A mapping may select a
bounded portion of a larger input; input frame values that are not produced as
mapping results remain subject to separate host frame-memory and aggregate
output budgets.

Portable evaluation work uses one abstract work unit for each:

- operator invocation, charged before that operator begins;
- array element or object member examined or emitted by an operator, charged
  before that element or member is processed; and
- Unicode scalar value examined or emitted by a string-processing operator,
  charged before that scalar is processed.

Repeated evaluation of a `map` body or `filter` predicate charges every
operator invocation again. Composite construction, `deep-equal`, `stringify`,
and other traversals charge each member, element, or string scalar they
actually examine or emit under these rules. An item that is both examined and
emitted incurs both charges. Operators, operands, branches, elements, members,
and scalars skipped by the abstract evaluation order consume no work. Counters
use exact non-negative integer arithmetic; an implementation must treat
counter overflow as exhaustion rather than wrap the counter.

All portable runtime limits are debited immediately before the corresponding
work. The first debit or produced value that would exceed an effective limit
terminates the mapping before that work occurs. This failure follows the
abstract evaluation order in Section 8.6 and is a mapping runtime failure under
Section 8.9.

Expression depth above 256, operator count above 65,536, or operator count
above the effective `maxOperators` is a portable document-validity failure.
Runtime values are not required to be statically provable within the remaining
limits. When actual evaluation exceeds an accepted collection, string, value,
or work limit, the result is a mapping runtime failure. A diagnostic identifies
the mapping site and exceeded resource without reproducing protected payload
data.

Collection, string, value-size, and work overrides have no additional v1 hard
ceiling beyond the portable safe-integer domain. They remain finite and are
subject to explicit host approval. Hosts may also enforce independent
aggregate run limits. Exhausting an aggregate host limit is an execution-budget
failure and must not be relabeled as exhaustion of a portable mapping limit.

### 8.11 Future-version candidates

The following capabilities are intentionally outside v1 and are recorded as
non-normative candidates rather than commitments:

- bounded regular-expression matching, extraction, and replacement, dependent
  on the shared portable `pattern` grammar and evaluator;
- temporal parsing, canonical normalization, formatting, timezone conversion,
  comparison, and arithmetic, dependent on a dedicated portable temporal model;
- locale-independent Unicode case conversion, dependent on a pinned Unicode
  version and mapping algorithm;
- sorting, reduction, membership and containment helpers, substring and
  non-regex replacement helpers, Base64 conversion, object merge, and general
  format templates.

A future mapping-language version may select, rename, split, or omit these
candidates. This list grants no forward-compatibility interpretation to v1
hosts.

### 8.12 Language-version selection

Every mapping site contains a required `language` member that selects one exact
mapping-language version for that site. Language selection is local: there is no
pipeline-wide default, inheritance, version range, alias, or unspecified latest
version. Changing a pipeline format, another mapping site, or a host default
must not reinterpret an untouched mapping expression.

A pipeline format may permit more than one mapping-language version. Such a
pipeline may contain mapping sites that select different permitted versions,
including an older final output projection after a newer transform. Each site
is parsed, validated, type-checked, budgeted, compiled, and evaluated according
to its selected version. Mapping-language versions do not invoke or embed one
another; they compose only through portable values checked against the declared
Qhapaq schemas at node boundaries.

The exact pipeline-format schema defines the closed set of mapping-language
versions permitted at each kind of mapping site. `qhapaq.pipeline/v1` permits
only `qhapaq.mapping/v1`, as required by Sections 6.3.2 and 10. A later pipeline
format may permit `qhapaq.mapping/v1`, `qhapaq.mapping/v2`, or both without
altering the meaning or validity rules of `qhapaq.pipeline/v1`.

Patching or migrating one mapping site must preserve the `language` and
expression of every untouched site. Changing a site's `language` requires
validating its complete expression under the newly selected version and
produces a new canonical definition and definition digest. Canonicalization
preserves every exact `language` value and never performs language migration.

## 9. Schema Profile and Compatibility

### 9.1 Normative document-schema composition

The JSON Schema that validates a pipeline document is distinct from the Qhapaq
schema values embedded in that document for operation data, configuration, and
pipeline inputs and outputs. The normative pipeline-document schema may use
JSON Schema Draft 2020-12 composition keywords needed to define the closed
document grammar even when those keywords are not permitted in embedded Qhapaq
schema values.

Each published pipeline-format schema is an immutable, self-contained schema
bundle. It contains a version-specific definition for every mapping-language
version that the pipeline format permits. At each mapping site, the schema uses
a closed `oneOf` whose branches are distinguished by a `language` property with
one exact `const` value. Each branch validates the complete closed mapping-site
shape and references only the matching version's expression definition. For
example, a future pipeline format that permits two versions has the logical
shape:

```json
{
  "$defs": {
    "mappingSite": {
      "oneOf": [
        { "$ref": "#/$defs/mappingSiteV1" },
        { "$ref": "#/$defs/mappingSiteV2" }
      ]
    },
    "mappingSiteV1": {
      "type": "object",
      "required": ["language", "inputs", "expression"],
      "properties": {
        "language": { "const": "qhapaq.mapping/v1" },
        "inputs": { "$ref": "#/$defs/mappingInputs" },
        "expression": { "$ref": "#/$defs/mappingExpressionV1" }
      },
      "additionalProperties": false
    },
    "mappingSiteV2": {
      "type": "object",
      "required": ["language", "inputs", "expression"],
      "properties": {
        "language": { "const": "qhapaq.mapping/v2" },
        "inputs": { "$ref": "#/$defs/mappingInputs" },
        "expression": { "$ref": "#/$defs/mappingExpressionV2" }
      },
      "additionalProperties": false
    }
  }
}
```

The illustrative `mappingSite` above shows the version-dispatch pattern rather
than the complete transform-node or output-projection schema. The normative
schema defines separate complete closed branches for those records because
their required members differ.

The set of branches is fixed when a pipeline-format schema is published. A host
must not add a newly installed or newly implemented mapping language to an
older format's schema. Consequently, adding `qhapaq.mapping/v2` does not change
the accepted instances of `qhapaq.pipeline/v1`; a later pipeline format must
explicitly include the v2 branch. Schema artifacts may be maintained as
separate source modules, but the published validation bundle uses only bundled
resources and requires no file-system or network resolution.

### 9.2 Embedded schema profile

Schema values embedded in pipeline definitions and operation descriptors use
JSON Schema Draft 2020-12 under a Qhapaq v1 profile. The profile must define:

- the supported keywords and exact format allowlist;
- object and array closure rules;
- numeric and string constraints;
- nullability and union restrictions;
- local reference packaging;
- the conservative compatibility algorithm.

Remote schema resolution during validation or execution is prohibited.
The v1 profile permits only fragment-only `$ref` values that resolve within the
containing document, such as `#/$defs/customer`. External, relative-document,
and network references are invalid. A future format may introduce separately
packaged, digest-pinned schema artifacts without changing v1 behavior.

Every Qhapaq-supported `format` is an assertion, not an annotation. A value that
does not satisfy its declared format is invalid. An unknown or unsupported
format is also invalid rather than being ignored. The normative schema profile
and conformance vectors define the closed v1 format allowlist and the validation
rules for each member so that hosts cannot interpret formats differently.

The v1 format allowlist is:

- `date`;
- `time`;
- `date-time`;
- `duration`;
- `email`;
- `hostname`;
- `ipv4`;
- `ipv6`;
- `uri`; and
- `uuid`.

Their lexical and semantic validation rules follow the corresponding normative
references used by the JSON Schema Draft 2020-12 format-assertion vocabulary.

Every schema whose effective type includes `object` must declare
`additionalProperties`. Its value must be `false` or an explicit schema;
omission and `true` are invalid. This makes object closure intentional while
still permitting typed dictionary values. Declared properties and additional
properties are both subject to the conservative compatibility algorithm.

The v1 profile supports homogeneous arrays only. Every schema whose effective
type includes `array` must declare exactly one `items` schema. Tuple validation
through `prefixItems` and other tuple-specific behavior is unsupported.

The v1 profile permits either one concrete JSON type or exactly one concrete
JSON type combined with `null`. General type unions and composition through
`oneOf` or `anyOf` are unsupported. Optionality and nullability remain distinct:
an object property is optional only when it is absent from `required`, and it
accepts `null` only when its declared type explicitly includes `null`.

The closed v1 schema-keyword allowlist is:

- `$defs` and `$ref`;
- `type`, `const`, and `enum`;
- `required`, `properties`, and `additionalProperties`;
- `items`, `minItems`, `maxItems`, and `uniqueItems`;
- `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, and
  `multipleOf`;
- `minLength`, `maxLength`, `pattern`, and `format`;
- `default`; and
- `title`, `description`, and `examples`.

Unknown or unsupported schema keywords are invalid rather than annotations to
ignore. The annotation keywords do not affect instance validation or schema
compatibility, except for the Qhapaq normalization semantics assigned to
`default`.

The schema profile defines portable maximum complexity limits that participate
in document validity. Every conforming host must accept schemas within those
limits when no other validation rule fails. A host may impose stricter limits,
but it must report those separately as host-bindability or policy failures
rather than claiming that the portable document is invalid. Limit diagnostics
must identify the exceeded resource without reproducing protected payload data.

The portable v1 schema limits are:

- at most 1 MiB for the RFC 8785 canonical UTF-8 representation of one schema;
- at most 10,000 distinct schema objects;
- at most 64 nested schema-object levels;
- at most 256 declared properties in one object schema;
- at most 1,024 values in one `enum`;
- at most 1,024 Unicode scalar values in one `pattern`; and
- at most 64 `$ref` dereferences in one resolution chain.

Shared local references count each distinct schema object once toward the object
limit. Cyclic references are invalid even when a validator could otherwise
detect and stop the cycle.

The `default` keyword has Qhapaq-specific normalization semantics for operation
configuration properties. A property listed in its containing object's
`required` array must be supplied explicitly. A `default` on a required
property is authoring guidance only and must not be inserted by a validator,
binder, or runtime.

An omitted, non-required operation configuration property with a `default` is
normalized to that concrete value. A caller never supplies a sentinel such as
the string `"default"`. Explicit `null` is not omission and remains subject to
the property's schema. The default value must itself satisfy the property
schema.

Normalization materializes optional defaults into the canonical pipeline
definition before it is hashed, persisted, reviewed, or bound. Implementations
must not defer default selection until execution. Defaults are normative
operation-contract content, are covered by the contract digest, and cannot
change for an existing operation ID and exact contract version. Changing an
optional executable default therefore requires a new operation contract
version.

Compatibility validation is conservative. A connection is accepted only when
the validator can prove that every successful upstream value conforms to the
downstream input schema. An unsupported or indeterminate comparison is rejected
rather than treated as compatible.

V1 uses one deterministic structural subtype algorithm over the closed Qhapaq
schema profile. An upstream schema is connection-compatible with a downstream
schema only when that algorithm proves that the set of values admitted upstream
is a subset of the set admitted downstream. Schema equality is sufficient but
not required. Hosts must not add implementation-specific compatibility cases;
the same normalized schema pair must produce the same result on every
conforming host.

For `pattern`, compatibility is provable only when the downstream schema has no
pattern or both schemas contain the same pattern string after JSON string
decoding. V1 does not attempt regular-language inclusion analysis. Different
patterns are indeterminate and therefore incompatible even when a human could
show that one language contains the other.

For `format`, compatibility is provable only when the downstream schema has no
format or both schemas declare the same format. V1 defines no subtype
relationships between different formats.

`const` and `enum` constraints are compared as sets of JSON values. They are
compatible only when every literal value admitted by the upstream schema is
also admitted by the downstream schema. JSON value equality for this comparison
uses the canonical JSON data model, including mathematical equality for JSON
numbers rather than source-text equality.

Numeric ranges and string or array length ranges use exact mathematical set
containment, including inclusive and exclusive numeric endpoints. A wider
upstream range is incompatible with a narrower downstream range. Authors may
use an explicit checked `assert-number-range` or `assert-length` transform to
narrow the schema; a binder must not insert an implicit runtime range check or
alter the value by clamping it.

The portable v1 numeric domain is the set of finite IEEE 754 binary64 values
accepted by RFC 8785 canonicalization. `NaN`, positive infinity, negative
infinity, and negative zero as a semantically distinct value are unsupported.
The `integer` type is restricted to values from `-9007199254740991` through
`9007199254740991` so every integer is represented exactly across conforming
implementations.

`integer` is a structural subtype of `number`, so an integer output may connect
directly to a numeric input when its remaining constraints are compatible. A
general numeric output is not compatible with an integer input unless `const`
or `enum` analysis proves that every admitted value is integral. Otherwise the
pipeline requires an explicit checked `assert-integer` transform.

For `multipleOf`, compatibility is provable when the downstream schema omits
the keyword or the upstream divisor is an exact positive integer multiple of
the downstream divisor. Implementations must compare the exact mathematical
values represented by the JSON numbers and must not use binary floating-point
rounding to decide divisibility.

For objects, every property required downstream must also be required upstream.
Every property value the upstream schema may emit must be structurally
compatible with the schema that the downstream applies to that property.
An upstream property not named downstream is compatible only when the
downstream `additionalProperties` schema accepts it. If the upstream permits
additional properties, its additional-property schema must be compatible with
the downstream additional-property schema and with every downstream named
property that an additional upstream property could match. A downstream
`additionalProperties: false` rejects any upstream schema that may emit an
undeclared downstream property. These rules apply recursively.

For homogeneous arrays, the upstream `items` schema must be structurally
compatible with the downstream `items` schema. The upstream length interval
must be contained within the downstream interval. When the downstream requires
`uniqueItems: true`, the upstream must also require uniqueness; an upstream
uniqueness requirement remains compatible with a downstream schema that does
not require it.

The `pattern` keyword uses a Qhapaq-defined portable regular-expression subset,
not a host runtime's native regex dialect. The subset excludes backreferences,
lookahead, lookbehind, conditionals, recursion, atomic groups, and executable or
engine-specific extensions. Validation must use bounded evaluation and reject a
pattern outside the portable grammar before matching instance data. Sections
9.3 and 9.5 define the grammar, matching algorithm, limits, and required
cross-language conformance coverage.

Within that subset, `\d`, `\w`, and `\s` and their negations have fixed ASCII
meanings independent of culture and host runtime. Literal Unicode characters
are permitted. Unicode-category and Unicode-property escapes are unsupported in
v1.

At minimum:

- every downstream required property is guaranteed upstream;
- optional or nullable values cannot satisfy required non-null inputs;
- numeric ranges and string constraints are not weakened accidentally;
- union selection is unambiguous;
- array-item schemas are compatible; and
- additional-property behavior is respected.

### 9.3 Portable regular-expression grammar and matching

A portable pattern is decoded from its JSON string before it is parsed. Parsing
and matching operate on Unicode scalar values, not UTF-8 bytes, UTF-16 code
units, grapheme clusters, or locale-dependent characters. An unpaired surrogate
cannot occur in a valid decoded JSON string. No Unicode normalization, case
folding, or locale-sensitive comparison is performed.

The following grammar is normative. Grammar literals are shown in quotes,
juxtaposition means concatenation, `*` on a grammar production means zero or
more grammar occurrences, and bracketed grammar terms are optional. These
grammar metacharacters are notation and are not pattern syntax.

```text
pattern          = alternation
alternation      = concatenation *("|" concatenation)
concatenation    = *piece
piece            = assertion / quantified-atom [quantifier]
assertion        = "^" / "$"
quantified-atom  = literal / "." / escape / class / group
group            = "(" alternation ")"
quantifier       = "?" / "*" / "+" / counted
counted          = "{" count "}"
                 / "{" count "," "}"
                 / "{" count "," count "}"
count            = "0" / nonzero-digit *digit
class            = "[" ["^"] class-items "]"
class-items      = class-item *class-item
class-item       = class-atom ["-" class-atom]
class-atom       = class-literal / scalar-escape / shorthand
escape           = scalar-escape / shorthand / escaped-metacharacter
scalar-escape    = "\n" / "\r" / "\t" / "\v" / "\f"
                 / "\u{" 1*6hex-digit "}"
shorthand        = "\d" / "\D" / "\w" / "\W" / "\s" / "\S"
digit            = "0" / nonzero-digit
nonzero-digit    = "1" / "2" / "3" / "4" / "5"
                 / "6" / "7" / "8" / "9"
hex-digit        = digit / "A" / "B" / "C" / "D" / "E" / "F"
                 / "a" / "b" / "c" / "d" / "e" / "f"
```

In the grammar, `n*m` means from `n` through `m` occurrences. The `\u{...}`
body's numeric value must be at most `10FFFF` hexadecimal and must not be in the
surrogate range `D800` through `DFFF`.

A `literal` is one scalar other than `\`, `|`, `(`, `)`, `[`, `]`, `{`, `}`,
`*`, `+`, `?`, `.`, `^`, `$`, a C0 control from `U+0000` through `U+001F`, or
`U+007F`. An `escaped-metacharacter` is `\` followed by one of those printable
ASCII pattern metacharacters or `-`. A `class-literal` is any permitted literal
other than `-`, plus a pattern metacharacter that has no special meaning inside
a class; `\`, `]`, `^`, and `-` must be escaped when used as class members.
Unknown escapes and unescaped controls are invalid.

Parentheses group only; v1 has no observable captures. Empty groups,
concatenations, and alternation branches are valid and match the empty string.
An assertion cannot be quantified. An atom can have at most one quantifier, so
lazy, possessive, or adjacent quantifiers are invalid.

Every `count` is interpreted as an unsigned decimal integer without a leading
zero unless it is exactly `0`. Each count must be at most 1,024. In a bounded
range, the second count must be greater than or equal to the first. `{m,}` has
no fixed repetition maximum; its compiled loop remains subject to the matching
algorithm and state limit below.

Class items are unioned. A range is valid only when both endpoints denote one
scalar, the first endpoint's scalar value is no greater than the second's, and
neither endpoint is a shorthand class. A leading class `^` complements the
union over the complete set of Unicode scalar values. An empty class is
invalid.

The fixed shorthand sets are:

| Escape | Scalar set |
| --- | --- |
| `\d` | `U+0030` through `U+0039` |
| `\w` | ASCII `A`-`Z`, `a`-`z`, `0`-`9`, and `_` |
| `\s` | `U+0009`, `U+000A`, `U+000B`, `U+000C`, `U+000D`, and `U+0020` |

`\D`, `\W`, and `\S` are the complements of those sets over Unicode scalar
values. `.` matches every Unicode scalar, including line terminators. `^`
matches only absolute input position zero, and `$` matches only the absolute
position after the final scalar. There is no multiline, dot-all, ignore-case,
or other flag syntax.

Pattern matching is an unanchored search. A pattern succeeds if it accepts any
contiguous scalar subsequence, including an empty subsequence. Authors use `^`
and `$` when they require the whole instance string to match.

After parsing, a validator compiles the abstract syntax tree to a Thompson
epsilon-NFA. The normative machine has exactly five state forms:
`consume(set, out)`, `split(out1, out2)`, `jump(out)`,
`assert-start(out)` or `assert-end(out)`, and `accept`. Every state counts as
one compiled state. An `out` is either a state reference or a dangling reference
that compilation later patches.

Compilation recursively returns one start reference and an ordered list of
dangling exits:

1. A literal, dot, or class creates one `consume` state with one dangling exit.
   An assertion creates the corresponding assertion state with one dangling
   exit. An empty concatenation creates one `jump` state with one dangling exit.
   Grouping returns its child's fragment without adding a state.
2. Concatenation compiles each child from left to right, patches every exit of
   one child to the next child's start, and returns the first start and final
   exits.
3. Alternation compiles branches from left to right and combines them with
   left-associated `split` states. Each split's first output selects the
   accumulated left fragment and its second selects the next branch. The
   alternation exits are the branch exits in source order; no join state is
   added.
4. `A?` creates a `split` whose first output is `A` and whose second output is a
   new dangling exit. The result exits are `A`'s exits followed by the split's
   dangling exit. `A*` creates a `split` whose first output is `A` and whose
   second output is dangling, patches every exit of `A` back to the split, and
   returns the split as its start. `A+` returns `A` as its start, creates a
   `split` whose first output refers back to `A` and whose second output is
   dangling, and patches every exit of `A` to that split.
5. `{m}` compiles and concatenates exactly `m` fresh copies of its atom.
   `{m,n}` concatenates `m` fresh required copies followed by `n - m` fresh
   `?` copies. `{m,}` concatenates `m` fresh required copies followed by one
   fresh `*` copy. A sequence of zero copies is the empty-concatenation
   fragment.
6. Compilation creates one `accept` state and patches every final dangling exit
   to it.

A compiled pattern must contain no more than 4,096 states under this normative
unshared construction. Exceeding that limit is a document-validity failure.
Implementations may share equivalent immutable fragments internally only when
doing so does not accept a pattern whose normative construction exceeds the
limit.

For an input containing `N` scalars and an NFA containing `S` states, matching
uses this state-set simulation:

1. Number input positions from zero through `N`. Start with an empty active
   state set.
2. At each position `p`, add the epsilon closure of the NFA start state at `p`
   to the active set. During closure, `^` advances only when `p` is zero and
   `$` advances only when `p` is `N`.
3. If the accepting state is active, return `true`.
4. If `p` is less than `N`, follow every active consuming transition whose set
   contains scalar `p`, form the epsilon closure of the resulting states at
   position `p + 1`, deduplicate by state identity, and use that set as the
   active set for the next position.
5. If position `N` completes without activating the accepting state, return
   `false`.

Each state-position pair is visited at most once after deduplication. Matching
therefore permits at most `(N + 1) x S` distinct state-position visits and uses
at most `S` active states. A conforming implementation may use a different
internal representation only when it produces the same Boolean result, rejects
the same patterns under the normative construction limits, and does not exceed
those time and space bounds. A host runtime regular-expression engine is not a
conforming substitute unless those properties are independently enforced.

### 9.4 Closed v1 format algorithms

Every format algorithm validates the entire decoded string. Formats are
case-sensitive except where a rule below explicitly permits either case.
Formats perform no trimming, Unicode normalization, DNS lookup, URI
dereferencing, clock lookup, or other external access. A `format` and any other
string constraint in the same effective schema are conjunctive.

The temporal formats use these shared rules:

- `date` has exactly the form `YYYY-MM-DD`. The year is from `0001` through
  `9999`. Month and day are two digits and must identify a date in the
  proleptic Gregorian calendar. A year is a leap year when it is divisible by
  4 and is not divisible by 100 unless it is also divisible by 400.
- `time` has the form `HH:MM:SS`, optionally followed by `.` and one or more
  ASCII digits, and then either `Z`, `z`, or an offset of the form `+HH:MM` or
  `-HH:MM`. Hour is `00` through `23`, minute is `00` through `59`, and a
  numeric offset uses an hour from `00` through `23` and a minute from `00`
  through `59`. `24:00:00` and an omitted offset are invalid. `-00:00` remains
  valid with the meaning assigned by RFC 3339.
- A normal time second is `00` through `59`. Second `60` is valid only when
  subtracting the declared offset makes the time `23:59:60` UTC. For `time`
  alone, that establishes a syntactically possible leap-second time without
  consulting a date or a mutable leap-second table.
- `date-time` is one valid `date`, followed by `T` or `t`, followed by one valid
  `time`. When its second is `60`, offset conversion must additionally produce
  a UTC date from `0001-01-01` through `9999-12-31` on June 30 or December 31.
  Date arithmetic for that conversion uses the proleptic Gregorian calendar
  and may cross a local date boundary.

These rules are the v1 frozen RFC 3339 profile. They do not consult the
historical leap-second table, because updating such a table would otherwise
change validation of an unchanged document.

`duration` accepts exactly this ASCII grammar, corresponding to the RFC 3339
Appendix A `duration` production:

```text
duration       = "P" (week-form / date-time-form / time-form)
week-form      = digits "W"
date-time-form = date-parts [time-parts]
time-form      = time-parts
date-parts     = digits "D"
               / digits "M" [digits "D"]
               / digits "Y" [digits "M" [digits "D"]]
time-parts     = "T" (digits "S"
               / digits "M" [digits "S"]
               / digits "H" [digits "M" [digits "S"]])
digits         = 1*ASCII-DIGIT
```

Components cannot skip an intermediate component: for example, `P1Y2D` and
`PT1H2S` are invalid. A week form cannot be combined with another component.
Signs, whitespace, fractions, lowercase unit letters, alternative ISO 8601
forms, and a bare `P` or `PT` are invalid. Digit sequences are validated
lexically as arbitrary-precision non-negative integers; validation must not
overflow a host numeric type.

`hostname` accepts only ASCII and is valid when all of these conditions hold:

1. Its length is from 1 through 253 characters, with no trailing dot.
2. Splitting on `.` produces labels from 1 through 63 characters.
3. Every label starts and ends with an ASCII letter or digit.
4. Every other label character is an ASCII letter, digit, or `-`.

Letter case does not affect hostname validity. Internationalized names must be
supplied in an already-valid ASCII representation; v1 performs no IDNA
conversion.

`ipv4` contains exactly four decimal octets separated by `.`. Each octet is
`0` or a digit from `1` through `9` followed by at most two digits, and its
mathematical value must be from 0 through 255. A multi-digit octet cannot start
with zero.

`ipv6` implements the RFC 4291 text forms with this exact procedure:

1. Reject brackets, a prefix length, a scope or zone identifier, whitespace,
   more than one `::`, an empty component outside `::`, and any character other
   than an ASCII hexadecimal digit, `.`, or `:`.
2. A final embedded IPv4 address is permitted and is validated by the v1
   `ipv4` algorithm. It counts as two 16-bit groups and cannot occur elsewhere.
3. Every other explicit group contains from one through four hexadecimal
   digits, compared case-insensitively.
4. Without `::`, there must be exactly eight groups after counting an embedded
   IPv4 address as two. With `::`, the explicit groups must total fewer than
   eight and `::` supplies exactly enough zero groups to reach eight.

`email` accepts only an RFC 5321-style ASCII mailbox under this closed profile:

1. The entire mailbox is at most 254 characters. The local part is at most 64
   characters and is followed by one unquoted `@` and a domain.
2. An unquoted local part is one or more dot-separated non-empty atoms. An atom
   contains only ASCII letters, digits, or
   `!#$%&'*+-/=?^_`{|}~`.
3. A quoted local part starts and ends with `"`. Between them, an unescaped
   character is ASCII `U+0020` through `U+007E` other than `"` or `\`; `\` must
   escape exactly one ASCII character from `U+0020` through `U+007E`.
4. The domain is either a valid v1 `hostname`, `[IPv4]` where `IPv4` satisfies
   the v1 algorithm, or `[IPv6:IPv6]` where the tag is compared
   case-insensitively and the value satisfies the v1 `ipv6` algorithm.

Comments, display names, source routes, whitespace outside a quoted local part,
SMTPUTF8, obsolete forms, and general address-literal tags are invalid.

`uri` accepts exactly the complete RFC 3986 `URI` production, not
`relative-ref` or IRI syntax. Validation uses the RFC 3986 ABNF over ASCII
characters with these requirements:

1. A scheme is required. Percent-encoded triplets contain exactly two ASCII
   hexadecimal digits. A raw non-ASCII character, malformed triplet,
   backslash, control, or whitespace is invalid.
2. Authority, user-information, host, port, path, query, and fragment are
   accepted only where the selected RFC 3986 production permits them. An empty
   port remains valid because the RFC `port` production is zero or more digits.
3. Host parsing applies the RFC alternatives in order: IP literal, v1 `ipv4`,
   then registered name. A bracketed IPv6 host uses the v1 `ipv6` algorithm;
   RFC 3986 `IPvFuture` remains valid under its exact ABNF. Brackets are invalid
   around any other host.
4. Validation performs no case normalization, percent-decoding, dot-segment
   removal, default-port insertion, DNS validation, or scheme-specific checks.

`uuid` contains exactly 36 ASCII characters in five hexadecimal fields of
length 8, 4, 4, 4, and 12 separated by hyphens. Hexadecimal digits are compared
case-insensitively. All bit patterns, including the nil UUID and unassigned
version or variant values, are valid. Braces, whitespace, compact text, and a
`urn:uuid:` prefix are invalid. This is the textual shape referenced by RFC
4122; v1 does not infer additional version semantics.

### 9.5 Pattern and format conformance requirements

The language-neutral conformance suite must include, at minimum:

- every grammar production, escape, shorthand, anchor, empty alternative, and
  quantifier boundary;
- invalid escapes, scalar escapes, ranges, counts, adjacent quantifiers,
  unsupported constructs, and patterns immediately below and above the
  4,096-state construction limit;
- unanchored, anchored, empty-string, line-terminator, non-BMP scalar, negated
  class, and ASCII-versus-Unicode shorthand cases;
- adversarial nested alternation and repetition cases that demonstrate the
  state-set bound without catastrophic backtracking;
- a valid, invalid, minimum, maximum, and immediately out-of-range case for
  each numeric or length boundary in every format;
- Gregorian leap-year, offset-crossing, fractional-second, possible
  leap-second, and impossible leap-second cases;
- every duration component form and invalid component ordering or mixture;
- hostname label and total-length boundaries, email local-part and total-length
  boundaries, quoted local parts, and each permitted and rejected domain form;
- compressed, uncompressed, embedded-IPv4, overfull, underfull, and malformed
  IP literals;
- URI grammar branches, malformed percent escapes, IPvFuture, relative
  references, raw non-ASCII characters, and values that are syntactically valid
  but would fail a scheme-specific policy; and
- UUID case, field boundaries, nil and unassigned bit patterns, and rejected
  wrappers.

Expected results must be independent of operating system, architecture,
culture, time zone, DNS, network access, and host parsing libraries.

## 10. Pipeline Output

Without an explicit `output` projection, the root expression's output must be
compatible with `schemas.output` and becomes the pipeline result.

An explicit output projection is a closed boundary-specific mapping record with
this exact shape:

```json
{
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
    "op": "object",
    "fields": {
      "customerId": {
        "op": "property",
        "value": {
          "op": "input",
          "name": "customer"
        },
        "name": "id"
      },
      "orderId": {
        "op": "property",
        "value": {
          "op": "input",
          "name": "order"
        },
        "name": "id"
      }
    }
  }
}
```

`language`, `inputs`, and `expression` are required. `language` is exactly
`qhapaq.mapping/v1`. `inputs` is explicit, may be empty, and uses the same
lower-camel alias grammar as a transform node. Its closed source union contains
only `pipeline-input` and `node` sources; `current-input` is invalid because the
projection has no enclosing composition edge. A node source must dominate
successful completion of the root. `expression` follows the canonical mapping
syntax and may read only those declared inputs. Unknown output-projection
members are invalid.

The output projection has no `id`, `kind`, or `outputSchema`. It is not a
structural node, does not create an externally addressable frame slot, and uses
the pipeline's `schemas.output` as its required result schema. Returning one
declared input expression unchanged is the canonical way to select a raw
eligible node output or the raw boundary input. An explicit output projection:

- runs only after the root completes successfully;
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
Structural sequence, parallel, conditional, try/catch recovery, loop, and
transform forms are not registry descriptors.

### 11.3 Availability

The effective registry reports whether an exact descriptor is:

- available;
- unavailable because a trusted implementation is absent;
- unavailable because required host configuration is absent; or
- unavailable because active policy excludes it.

Explanations must not reveal credentials, secret references, sensitive
filesystem locations, or other protected host configuration.

### 11.4 Vocabulary identifiers and governance

Capability, side-effect, idempotency, retry-disposition, effect-outcome, and
failure-code values use case-sensitive lowercase ASCII identifiers. An
identifier:

- is at most 256 characters;
- consists of dot-separated labels;
- uses labels that start with an ASCII lowercase letter, continue with ASCII
  lowercase letters or digits, and may contain single `-` separators followed
  by another ASCII lowercase letter or digit;
- contains no empty label, leading or trailing `.`, consecutive `-`, or
  normalization-equivalent spelling; and
- is compared exactly without case folding or Unicode normalization.

The `qhapaq.` namespace is reserved for this specification and other Qhapaq
standards. An extension identifier uses a reverse-DNS namespace with at least
three labels, such as `com.contoso.accelerator.use`. Possession or syntax of a
name does not grant authority.

The operation-descriptor format freezes the core capability, side-effect, and
idempotency vocabularies it references. `qhapaq.failure/v1` independently
freezes the failure categories, retry dispositions, effect outcomes, reserved
platform codes, and structured-failure projection rules.

An otherwise valid descriptor may reference a syntactically valid namespaced
extension capability or side effect. A host that does not explicitly support
the exact extension term reports the descriptor as host-unbindable. Policy
cannot convert an unknown semantic term into a supported one merely by allowing
its identifier. Unknown `qhapaq.` terms are invalid for the exact descriptor
format.

Arrays representing semantic sets are canonical author input rather than
normalization requests. `capabilities` and `sideEffects` must be unique and in
ascending Unicode code-point order. Failure declarations must have unique codes
and be in ascending code order. An unsorted or duplicate-bearing array is
invalid; a validator must not reorder it before contract-digest computation.

### 11.5 Capability vocabulary

A capability is a parameter-free declaration of authority or a host facility
that an operation or decorator may exercise on at least one valid execution
path. It is not a declaration that the facility is used on every invocation and
is not a resource locator, side effect, connection, budget, or data-sensitivity
label.

The closed Qhapaq v1 core capability vocabulary is:

| Capability | Meaning |
| --- | --- |
| `qhapaq.credential.use` | Use a host-bound credential through a trusted credential provider or authenticated client without exposing credential material as a pipeline value. |
| `qhapaq.environment.read` | Read an explicitly identified environment variable subject to host policy. |
| `qhapaq.filesystem.read` | Read filesystem content or metadata. |
| `qhapaq.filesystem.write` | Create, modify, rename, or delete filesystem content or metadata. |
| `qhapaq.ipc.connect` | Connect to a declared local interprocess endpoint such as a named pipe or Unix-domain socket. |
| `qhapaq.network.connect` | Initiate an outbound network connection, including a loopback TCP or HTTP connection. |
| `qhapaq.process.execute` | Start or invoke an external process. |

Destinations, paths, variable names, executable identities, logical resources,
connections, and credential bindings are separate typed requirements evaluated
by binding and policy. They must not be encoded into capability strings.
Environment access identifies the requested variable explicitly and remains
subject to a host allowlist. `qhapaq.credential.use` permits trusted
implementation or provider code to apply, obtain, or refresh authentication
material as required by an SDK, but the material never becomes an operation
input, node output, transform value, failure payload, or pipeline result.

V1 defines no core capability for clock access, randomness, ambient arbitrary
host services, raw credential reads, inbound network listeners, or inbound IPC
listeners. A future determinism or sensitive-value contract may add the
appropriate independently enforceable metadata. V1 operations may connect to
declared services but do not create listeners.

Capabilities are orthogonal. No capability implies another, including
`qhapaq.process.execute`; an operation declares every authority that it or a
started child process may exercise. A plan aggregates a deduplicated set union
over every potentially executable node, including mutually exclusive branches,
recovery subtrees, decorators, and bounded repeated bodies. Invocation-count
and repetition bounds remain separate plan-budget facts and do not create
duplicate capability entries.

### 11.6 Side-effect vocabulary

A side effect is a possible intended contract-level mutation outside the
pipeline's value graph. Authority to access a facility and the consequence of
using it remain separate: a read-only network operation declares
`qhapaq.network.connect` and an empty `sideEffects` set.

The closed Qhapaq v1 core side-effect vocabulary is:

| Side effect | Meaning |
| --- | --- |
| `qhapaq.communication.emit` | Emit a message, event, notification, or other communication whose delivery is an intended external consequence. |
| `qhapaq.external-action.trigger` | Request an externally meaningful action, such as a charge, deployment, workflow transition, or actuator command, that is not adequately described only as stored-data mutation or communication. |
| `qhapaq.external-state.mutate` | Create, change, append to, rename, or delete durable or externally observable state. |

Terms are broad consequence classes rather than protocol or CRUD verbs. An
operation declares every class that its intended behavior may produce on any
valid path, including a path that later fails. Incidental provider logging,
transport bookkeeping, or caching that is not part of the operation contract
does not add a portable side-effect class. More specialized semantics require a
supported reverse-DNS extension term.

An empty `sideEffects` array is the sole representation of a guarantee that the
operation produces no core or extension-defined external mutation. There is no
`none` term. A plan aggregates a deduplicated set union over every potentially
executable node, including alternate and recovery paths. Repetition bounds are
reported separately. A decorator may add its own possible effects but cannot
remove an inner node's effects, even when some paths avoid invoking the inner
node.

### 11.7 Idempotency vocabulary

Idempotency concerns effects, not output determinism. Repeating an equivalent
invocation is idempotent when it produces no additional externally observable
effect beyond the first invocation. Outputs may differ because external state
changed. Mapping expressions remain deterministic under Section 8; operation
output determinism is a separate, currently undefined property.

Two operation invocations are equivalent for this guarantee only when they
have the same:

- exact operation contract;
- canonical input value;
- effective configuration; and
- logical connection binding.

Credential rotation inside the same logical connection does not create a
different invocation. Implementation package identity is not part of the
portable equivalence relation because every conforming implementation of the
exact contract must provide the same declared guarantee.

`idempotency` is always a closed object. Its required `classification` is one
of:

| Classification | Meaning |
| --- | --- |
| `qhapaq.idempotent` | Every equivalent repeat satisfies the effect-idempotency guarantee. |
| `qhapaq.conditional` | The guarantee holds only when the declared idempotency-key and deduplication-window condition is satisfied. |
| `qhapaq.non-idempotent` | An equivalent repeat may produce an additional effect and is known not to carry an idempotency guarantee. |
| `qhapaq.unknown` | The contract supplies no idempotency guarantee. |

For every classification other than `qhapaq.conditional`, `classification` is
the object's only member. A conditional object additionally requires:

```json
{
  "classification": "qhapaq.conditional",
  "keyPointer": "/idempotencyKey",
  "minimumWindowMilliseconds": 86400000
}
```

`keyPointer` is an RFC 6901 JSON Pointer into the operation input schema. It
must resolve to a required, present, non-null string with `minLength` of at
least one. The runtime value at that pointer is the caller-supplied key, and
every equivalent retry must reuse it unchanged.
`minimumWindowMilliseconds` is a positive JSON safe integer declaring the
minimum interval for which the implementation guarantees deduplication of
equivalent invocations carrying the same key. A retry is conditionally
idempotent only when its complete configured retry horizon does not exceed that
window.

An empty `sideEffects` set requires `qhapaq.idempotent`, regardless of whether
the operation's output can vary. Decorators use the same four classifications
for their own effects. V1 decorators cannot strengthen an inner node's
idempotency guarantee.

A plan computes an idempotency risk summary with this conservative precedence:

1. any `qhapaq.non-idempotent` component produces `qhapaq.non-idempotent`;
2. otherwise, any `qhapaq.unknown` component produces `qhapaq.unknown`;
3. otherwise, any `qhapaq.conditional` component produces
   `qhapaq.conditional` and retains every distinct key and window requirement;
4. otherwise the summary is `qhapaq.idempotent`.

This summary does not claim that rerunning the complete pipeline is idempotent.
A rerun may read changed external state and therefore supply a different input
to a later operation. Whole-run idempotency requires a future analysis that can
prove stable repeated operation inputs.

An operation-level retry decorator holds the retried invocation input,
configuration, and connection constant. Retrying a
`qhapaq.non-idempotent`, `qhapaq.unknown`, or unsatisfied
`qhapaq.conditional` invocation remains document-valid and may be
host-bindable, but it is policy-ineligible by default. Trusted host policy must
explicitly permit that unsafe retry before execution; the pipeline document
cannot grant the permission. A denial occurs before any operation starts and is
not catchable.

### 11.8 Declared operation failures

Every operation and decorator failure that may be reported as a catchable
`operation` or `control` failure is exhaustively declared by its exact
descriptor. Each normative declaration is a closed object containing:

```json
{
  "code": "contoso.payments.charge.timeout",
  "retryDisposition": "qhapaq.retry.transient",
  "effectOutcome": "qhapaq.effect-outcome.unknown"
}
```

`code` begins with the descriptor's exact operation ID followed by `.` and a
stable local suffix. Codes are unique within the descriptor and sorted as
required by Section 11.4. Renaming a code changes the contract. An
implementation that emits an undeclared code, a malformed envelope, or
dispositions different from the declaration produces a non-catchable
implementation contract violation rather than an operation failure.

`retryDisposition` is one of:

- `qhapaq.retry.transient`: repeating the same equivalent invocation may
  succeed after the condition changes;
- `qhapaq.retry.permanent`: repeating the same equivalent invocation is not
  expected to succeed without changing the request or contract; or
- `qhapaq.retry.unknown`: the contract makes no retry-success claim.

`effectOutcome` is one of:

- `qhapaq.effect-outcome.none`: the failed attempt guarantees that none of its
  declared effects occurred;
- `qhapaq.effect-outcome.occurred`: the failed attempt guarantees that at least
  one declared effect occurred; or
- `qhapaq.effect-outcome.unknown`: at least one declared effect may have
  occurred, but the outcome is not known.

The two dimensions are independent. A transient timeout with unknown effect
outcome is not safely retryable merely because its cause may clear. Automatic
retry is safe only when the retry disposition permits it and either the failure
guarantees no effect or the operation's idempotency condition is satisfied.
Other retries require explicit unsafe-retry policy.

Failure descriptions are non-normative untrusted text stored under
`documentation.failureDescriptions`, keyed by exact failure code. Every
declared code has one non-empty description and the map contains no undeclared
code. Descriptions are excluded from the contract digest and never appear in a
runtime failure value or caught-failure projection. Human-facing adapters may
render them beside a stable code; pipeline logic cannot inspect or branch on
the text.

V1 portable failures contain no operation-specific details payload. Provider
response bodies, validation data, external request identifiers, exceptions,
and other implementation details remain protected host diagnostics subject to
separate disclosure policy.

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

Vocabulary compatibility is classified conservatively:

- adding a capability or side effect is breaking; removing one is a compatible
  strengthening;
- weakening idempotency, changing a conditional key location, or shortening
  its guaranteed minimum window is breaking; strengthening idempotency or
  lengthening the window is compatible;
- adding or renaming a possible failure code is breaking; removing a possible
  failure code is a compatible strengthening;
- changing either disposition of an existing failure code is breaking; and
- changing a non-normative failure description is compatible and does not
  change the contract digest.

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
4. Resolve each mapping site's exact language implementation and report a
   host-bindability failure when the active host does not support a permitted
   language version.
5. Resolve every exact operation and decorator contract.
6. Validate operation and decorator configuration.
7. Propagate schemas through structural nodes, including proving both
   conditional branch outputs and both `tryCatch` child outputs compatible with
   their containing node's declared `outputSchema`.
8. Validate transform sources, dominance, each expression under its selected
   language version, and output schemas.
9. Prove every operation connection schema-compatible.
10. Verify implementation-native input and output bindings.
11. Aggregate capabilities and side effects, compute the idempotency risk
    summary, and aggregate resource budgets.
12. Evaluate active host policy and required connection availability.
13. Construct the immutable execution plan.

Validation reports four distinct conclusions:

- **document validity:** the definition conforms to the portable language;
- **host bindability:** the active host has matching mapping-language
  implementations, trusted operation implementations, and native bindings;
- **policy eligibility:** current policy would permit the planned capabilities
  and side effects; and
- **execution permission:** evaluated again for a specific invocation.

Document validity does not grant execution or payload-disclosure permission.
Changes to the effective registry, host profile, policy, connections, or
implementation integrity invalidate affected cached plans.

## 15. Structured Diagnostics and Failures

### 15.1 Validation diagnostics

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

### 15.2 Runtime structured-failure envelope

Every runtime failure and terminal non-catchable execution outcome uses the
versioned `qhapaq.failure/v1` envelope. Its closed base contains exactly:

- `format`, whose value is `qhapaq.failure/v1`;
- `category`;
- `code`;
- `retryDisposition`;
- `effectOutcome`; and
- `sourceNodeId` when one specific node originated the failure.

`sourceNodeId` is required for every catchable failure and every other
node-originated failure. It is omitted when cancellation, policy, a run-wide
budget, or a host fault has no honest single source node. It is never filled
with the pipeline root merely to satisfy a shape.

The closed category vocabulary is:

| Category | Catchable | Meaning |
| --- | --- | --- |
| `operation` | yes | A failure exhaustively declared by a primitive operation descriptor. |
| `mapping` | yes | A deterministic mapping runtime failure. |
| `control` | yes | A declared decorator failure or bounded structural-control failure. |
| `aggregate` | yes | Two or more non-cancellation failures observed by one structural node. |
| `cancellation` | no | Invocation cancellation. |
| `policy` | no | Authorization or trusted policy denied execution. |
| `budget` | no | A run-wide host execution budget was exhausted. |
| `implementation` | no | A registered implementation violated its exact contract. |
| `host` | no | Execution infrastructure was unavailable or failed unexpectedly. |

Catchability is determined only by this category table. Individual codes cannot
override it, and the envelope has no `catchable` field. Validation and binding
diagnostics remain Section 15.1 diagnostics rather than runtime failures.

The reserved mapping codes are:

| Code | Retry disposition | Effect outcome |
| --- | --- | --- |
| `qhapaq.mapping.required-value-missing` | permanent | none |
| `qhapaq.mapping.non-null-value-required` | permanent | none |
| `qhapaq.mapping.invalid-number-text` | permanent | none |
| `qhapaq.mapping.invalid-boolean-text` | permanent | none |
| `qhapaq.mapping.integer-required` | permanent | none |
| `qhapaq.mapping.number-range-assertion-failed` | permanent | none |
| `qhapaq.mapping.length-assertion-failed` | permanent | none |
| `qhapaq.mapping.format-assertion-failed` | permanent | none |
| `qhapaq.mapping.division-by-zero` | permanent | none |
| `qhapaq.mapping.non-finite-number-result` | permanent | none |
| `qhapaq.mapping.portable-integer-range-exceeded` | permanent | none |
| `qhapaq.mapping.collection-element-limit-exceeded` | permanent | none |
| `qhapaq.mapping.collection-visit-limit-exceeded` | permanent | none |
| `qhapaq.mapping.string-scalar-limit-exceeded` | permanent | none |
| `qhapaq.mapping.string-byte-limit-exceeded` | permanent | none |
| `qhapaq.mapping.value-byte-limit-exceeded` | permanent | none |
| `qhapaq.mapping.evaluation-work-limit-exceeded` | permanent | none |

The table uses the suffixes `permanent` and `none` for
`qhapaq.retry.permanent` and `qhapaq.effect-outcome.none`, respectively.
Mapping codes are assigned by distinct portable failure cause and are shared by
operators with the same cause.

The only structural-language control code is
`qhapaq.control.loop-limit-exceeded`. It is permanent for the same loop input.
Its effect outcome is derived from all work started before exhaustion.
Decorator control codes are exhaustively declared by the exact decorator
descriptor and use that descriptor's operation-ID prefix.

When `parallel` or `forEach` observes one non-cancellation child failure, it
propagates that failure unchanged. When it observes two or more, it reports
category `aggregate` and code `qhapaq.aggregate.multiple-failures`.
Aggregate retry disposition is permanent if any cause is permanent, otherwise
unknown if any cause is unknown, and otherwise transient. Aggregate effect
outcome is occurred if any started work reports an occurred outcome, otherwise
unknown if any started effectful work has an unknown outcome, and otherwise
none. Successful work with a non-empty declared side-effect set contributes an
unknown outcome because a `may produce` declaration does not prove whether an
effect occurred.

The reserved non-catchable platform codes are:

| Category | Codes |
| --- | --- |
| `cancellation` | `qhapaq.cancellation.requested` |
| `policy` | `qhapaq.policy.authorization-denied`, `qhapaq.policy.operation-denied`, `qhapaq.policy.capability-denied`, `qhapaq.policy.side-effect-denied`, `qhapaq.policy.resource-scope-denied`, `qhapaq.policy.unsafe-retry-denied`, `qhapaq.policy.execution-denied` |
| `budget` | `qhapaq.budget.duration-exceeded`, `qhapaq.budget.operation-count-exceeded`, `qhapaq.budget.attempt-count-exceeded`, `qhapaq.budget.iteration-count-exceeded`, `qhapaq.budget.memory-exceeded`, `qhapaq.budget.frame-size-exceeded`, `qhapaq.budget.output-size-exceeded` |
| `implementation` | `qhapaq.implementation.undeclared-failure`, `qhapaq.implementation.failure-contract-violation`, `qhapaq.implementation.output-contract-violation`, `qhapaq.implementation.input-materialization-failed`, `qhapaq.implementation.output-materialization-failed` |
| `host` | `qhapaq.host.execution-unavailable`, `qhapaq.host.unexpected-fault` |

Policy failures are permanent under the active policy and have effect outcome
none because eligibility is decided before execution. Host execution
unavailability is transient and has effect outcome none. An unexpected host
fault has unknown retry and effect outcomes. Input materialization failure has
effect outcome none because operation invocation has not begun. Other
implementation failures after invocation have unknown effect outcome.

Cancellation, budget, loop-limit, aggregate, and other structural outcomes
derive their effect outcome from all started work, not only from failure causes.
The outcome is none only when all started work is effect-free or known not to
have applied effects; it is occurred when an observed outcome proves that an
effect occurred; otherwise it is unknown. This derivation never assumes that a
successful operation with a `may produce` side effect actually produced it.

The base envelope contains no human message, timestamp, correlation identifier,
exception data, or arbitrary details. Human-facing adapters resolve declared
operation descriptions or Qhapaq platform-code documentation separately.

### 15.3 Aggregate and recovery causality

The external execution result extends every aggregate failure with a closed
recursive `causes` array, a `totalLeafFailureCount` positive JSON safe integer,
and a `causesTruncated` Boolean. Causes follow the node's existing deterministic
order: ordinal branch name for `parallel` and ascending work index for
`forEach`. Nested aggregates preserve their causal grouping.

The complete returned failure graph, including the root, aggregate causes, and
recovery causality, contains at most 256 failure nodes and at most 32 cause
levels. Projection uses deterministic depth-first preorder. Each aggregate's
`totalLeafFailureCount` counts every observed leaf failure in its complete
subtree. `causesTruncated` is true exactly when the returned subtree omits at
least one failure because of either bound. Protected host diagnostics may
retain more information but must preserve the same causal ordering.

When a `tryCatch` recovery subtree fails, the external execution result extends
the terminal recovery failure with a closed `causedBy` value containing the
original try failure. When projection omits a recovery cause because of a graph
bound, `causedByTruncated` is true on the result whose cause was omitted;
otherwise that member is absent. Nested recovery uses the same graph bounds
and deterministic projection. Recovery failure is not relabeled as an
aggregate.

The `caught-failure` mapping source always receives only the closed base
projection in Section 6.3.7. It never receives `causes`, `causedBy`, aggregate
leaf counts, truncation metadata, descriptions, or protected diagnostics.

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
- `tryCatch` attempt and recovery boundaries;
- loop boundaries and maximum iterations; and
- `forEach` mode, cardinality, chunk-size, and concurrency bounds; and
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
- Expose caught failures to transforms only through the fixed, non-sensitive
  `qhapaq.failure/v1` projection; never project raw exceptions, stack traces,
  arbitrary messages, operation payloads, or connector response bodies.
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

Each pipeline format defines a closed compatibility matrix of mapping-site kinds
and permitted exact mapping-language versions. Supporting a newer mapping
language does not add it to an older pipeline format. A format may permit
multiple mapping-language versions in one definition, and modifying one mapping
site does not require migrating other sites.

An unknown format version, node kind, transform-language version, mapping
operator, or normative schema keyword is a document-validity failure. A mapping
language that is known and permitted by the exact pipeline format but not
implemented by the active host is instead a host-bindability failure. A host
must not silently reinterpret a newer definition or mapping expression as v1.

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
- sequence, parallel, decorator, conditional, `tryCatch`, and bounded-loop
  vectors, including branch convergence, incompatible-child diagnostics,
  catchability exclusions, nested caught-failure scope, recovery failure,
  cancellation races, retained side effects, and payload-safe projections;
- item-mode and chunk-mode `forEach` vectors covering empty input, cardinality,
  ordered aggregation, concurrency ceilings, nested scopes, failure,
  cancellation, and aggregate budgets;
- transform parsing, type inference, nullability, conversion, and failure tests;
- mixed mapping-language-version pipelines, including independent transform and
  output-projection versions;
- rejection of mapping languages not permitted by the exact pipeline format,
  and bindability diagnostics for permitted languages unsupported by the host;
- patch and migration tests proving untouched mapping sites retain their exact
  language, expression, canonical representation, and semantics;
- explicit multi-output and final-output projection tests;
- conservative schema-compatibility vectors;
- portable-pattern grammar, construction-limit, bounded-evaluation, and
  closed-format validation vectors required by Section 9.5;
- exact-version and contract-digest conflict tests;
- operation-contract compatibility-diff vectors;
- capability and side-effect vocabulary, namespace, canonical-order,
  unsupported-extension, aggregation, and decorator-preservation vectors;
- idempotency-object, conditional-key, deduplication-window, risk-summary, and
  unsafe-retry policy vectors;
- declared-failure exhaustiveness, code-prefix, disposition, documentation, and
  contract-violation vectors;
- runtime failure-category, catchability, platform-code, effect-outcome,
  singleton propagation, aggregate disposition, bounded causal-tree, and
  recovery-causality vectors;
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

Implementation proceeds through the following phases. The checkboxes are the
persistent implementation checklist for this specification. A phase may be
delivered through multiple changes, but an item must not be marked complete
until its persistent artifact and the validation named by that item exist.
Completing an implementation item does not make an unresolved portable behavior
normative; the applicable specification, schema, and conformance vector must be
completed first.

The phase numbers retain the existing checklist identities. Lettered milestones
make previously implicit prerequisites and smaller delivery gates explicit.
The listed order is the default implementation sequence, but the stated
dependencies govern independent work: artifact families in Phase 1 and inert
parsing in Phase 4 may progress without waiting for unrelated generator or host
work. No intermediate milestone enables execution or permits a partial v1
execution-conformance claim.

This section governs the definition-to-execution path, not every v1 product
deliverable. The companion milestones below identify required integration and
release work owned by other specifications.

### Phase 0: Close required normative decisions

This phase resolves the language decisions on which all later artifacts depend.
It does not require unrelated CLI, MCP, authentication, connector, or release
details to be decided early. The Phase 0A organization checkpoint precedes
scaffolding the remaining public .NET APIs.

- [x] Replace illustrative transform syntax with the canonical
  `qhapaq.mapping/v1` operator-object syntax.
- [x] Define the exact JSON shape and closure rules for every v1 structural node
  kind.
  - [x] Define the shared node envelope, recursive discriminated union, node-ID
    scope, and common closure rules.
  - [x] Define the `operation` node.
  - [x] Define the `transform` node.
  - [x] Define the `sequence` node.
  - [x] Define the `parallel` node and named branch records.
  - [x] Define the `decorate` node.
  - [x] Define the `conditional` node.
  - [x] Define the `tryCatch` node, catchability boundary, caught-failure
    projection, and lexical source scope.
  - [x] Define the bounded `loop` node.
  - [x] Define a bounded collection-execution node that chunks an input
    collection and applies an arbitrary inline node to each item or chunk,
    including cardinality, ordering, aggregation, concurrency, failure,
    cancellation, and resource-budget semantics.
  - [x] Define shared exact contract references, configuration values,
    transform input sources, and the final output projection.
- [x] Define the complete `qhapaq.mapping/v1` operator set, operand shapes,
  evaluation order, inferred result types, `missing` and `null` behavior, and
  runtime failure behavior.
- [x] Define per-site mapping-language selection, mixed-version composition,
  pipeline-format compatibility, and normative schema dispatch.
- [x] Define portable mapping limits, including expression depth, operator
  count, collection processing, string and output size, and evaluation budget.
- [x] Define the portable regular-expression grammar and exact algorithms for
  the closed format allowlist.
- [x] Define the normative capability, side-effect, idempotency, and structured
  failure vocabularies.
- [ ] Define the public .NET marker and static declaration contracts, manifest
  envelope, generator diagnostic-code policy, and initial compatibility matrix.
- [ ] Specify policy-filtered exact descriptor retrieval as the first
  non-executing Service V1 and CLI vertical slice, including public request,
  result, structured-error, and diagnostic mappings.
- [ ] Decide the smallest additional versioned Service, CLI, and MCP contracts
  required by the subsequent authoring and execution slices; explicitly defer
  the remainder.
- [ ] Define how non-executing responses distinguish document validity, host
  bindability, policy eligibility, and invocation-specific execution permission,
  including conclusions unavailable to an early slice.

**Completion gate:** no open question in Section 23 blocks the normative
schemas, conformance vectors, descriptor generator, or first Service vertical
slice.

### Phase 0A: Establish .NET organization and reuse boundaries

This checkpoint refines, rather than replaces, the assembly, layer, visibility,
and dependency rules in
[`0006-dotnet-layered-architecture.md`](0006-dotnet-layered-architecture.md)
and the
[coding conventions](../docs/development/coding-conventions.md).
It records decisions before the generator, definition models, registry, and
Service APIs expand the implementation.

- [ ] Document feature-folder and namespace conventions within each established
  assembly, including folder-to-namespace mapping and canonical naming.
- [ ] Assign ownership and visibility for definition, schema, expression,
  descriptor, plan, failure, and Service-boundary models; distinguish private
  implementation models from internal cross-layer and public contracts.
- [ ] Document representative node and expression type relationships, including
  where composition or a shared abstraction is warranted, without designing
  speculative class hierarchies.
- [ ] Assign ownership and reuse boundaries for canonicalization, digest
  computation, schema and descriptor validation, vocabulary validation, and
  diagnostic construction.
- [ ] Record how build-time generator tooling and runtime components reuse
  portable algorithms without runtime hosting dependencies or layer bypasses;
  record any required project or package boundary change before implementation.
- [ ] Define conformance-vector loading, golden-file maintenance, and
  package-consumer test conventions.
- [ ] Document DI lifetime and ownership rules for registry snapshots, cached
  plans, per-run state, and credential-related collaborators.
- [ ] Extend the existing architecture tests to enforce the decided namespace,
  visibility, dependency, and composition rules as applicable.

Decisions belong in SPEC-0006 or an ADR when architectural, and in the coding
conventions when ordinary engineering policy. Add concrete types and folders
only with behavior and tests; this checkpoint does not create empty placeholders
or require every future class to be named.

**Depends on:** the established SPEC-0006 architecture and the representative
use cases needed to evaluate ownership; unrelated Phase 0 decisions need not be
complete.

**Completion gate:** a persistent ownership and dependency map, representative
type relationships, and architecture tests cover the organization needed by the
first implementation slices.

### Phase 1: Publish language-neutral schemas and vectors

This phase turns the portable decisions into implementation-independent
artifacts. Publish each artifact family with its expected results before its
dependent implementation milestone is considered complete; unrelated execution
vectors need not block descriptor tooling.

- [ ] Define a versioned conformance-vector envelope, expected-result
  conventions, capability grouping, and golden-file regeneration procedure.
- [ ] Add reusable conformance test tooling that consumes the shared vectors
  without duplicating portable cases in .NET-specific fixtures.
- [ ] Publish the exact pipeline-document schema.
- [ ] Publish the exact versioned mapping-expression definitions embedded in
  each self-contained pipeline-format schema bundle.
- [ ] Publish the closed Qhapaq JSON Schema profile.
- [ ] Publish the versioned structured-diagnostic schema.
- [ ] Publish the runtime structured-failure envelope and caught-failure
  projection schemas, separately from validation diagnostics.
- [ ] Publish the portable operation-manifest envelope schema.
- [ ] Publish the next operation-descriptor format and schema covering the
  embedded schema profile, closed idempotency objects, normative failure
  dispositions, separately stored failure descriptions, and vocabulary rules.
- [ ] Preserve the earlier checked-in descriptor schema and vectors; publish
  the descriptor, manifest, and registration compatibility matrix required by
  Section 13.4 rather than mutating an earlier format.
- [ ] Add valid and invalid pipeline-document vectors.
- [ ] Add duplicate-member, canonicalization, and definition-digest vectors.
- [ ] Add exact-contract configuration-default normalization vectors,
  distinguishing omission, explicit null, and required properties.
- [ ] Add schema-profile and conservative compatibility vectors.
- [ ] Add portable-pattern and closed-format boundary and adversarial vectors
  required by Section 9.5.
- [ ] Add mapping parsing, type-inference, evaluation, and failure vectors.
- [ ] Add mixed-version mapping, unsupported-language bindability, and
  patch-preservation vectors when a pipeline format permits multiple mapping
  versions.
- [ ] Add scope, dominance, and inaccessible-branch vectors.
- [ ] Add structured-diagnostic golden files.
- [ ] Add contract-digest and manifest golden vectors.
- [ ] Add capability, side-effect, idempotency, declared-failure,
  decorator-preservation, and unsafe-retry vectors.
- [ ] Add runtime failure, caught-failure projection, aggregate disposition,
  effect-outcome, and bounded recovery-causality vectors.
- [ ] Add conservative operation-contract comparison vectors.
- [ ] Add execution-semantic vectors for every structural node kind.

**Depends on:** Phase 0 decisions required by each artifact.

**Completion gate:** every published portable rule needed by binding and
execution has a versioned schema or conformance vector, and those artifacts do
not depend on .NET implementation details. The test tooling reports the exact
artifact versions and capabilities exercised.

### Phase 1A: Implement shared portable validation foundations

This milestone implements the common prerequisites used by descriptor
generation, registry verification, definition processing, and mapping engines.
It does not introduce a parallel runtime or bypass the Phase 0A ownership rules.

- [ ] Implement strict JSON reading with malformed-input and duplicate-member
  rejection.
- [ ] Implement RFC 8785 canonicalization and shared digest primitives with
  numeric-domain, Unicode, culture, ordering, and path-independence tests.
- [ ] Implement exact offline document-schema selection and validation;
  distinguish outer document-schema machinery from the closed profile allowed
  in embedded operation and pipeline schemas.
- [ ] Implement validation of the closed Draft 2020-12 Qhapaq embedded schema
  profile, fragment-only local reference resolution, cycle rejection, and
  portable schema-complexity limits.
- [ ] Implement the specified bounded portable-pattern algorithms and closed
  supported-format assertions.
- [ ] Implement shared descriptor and vocabulary validation, including
  canonical normative contract-digest computation and verification.
- [ ] Implement bounded, location-aware, payload-safe diagnostic construction
  usable by build tooling and runtime adapters without conflating their
  diagnostic envelopes.
- [ ] Pass the applicable Phase 1 parsing, canonicalization, schema-profile,
  pattern, format, descriptor, vocabulary, digest, and diagnostic vectors.

**Depends on:** Phase 0A reuse and ownership decisions and the applicable Phase 1
artifacts.

**Completion gate:** generator and runtime consumers can reuse the same tested
portable semantics through the documented dependency boundaries, without
network access, operation construction, or project-code execution.

### Phase 2: Implement .NET descriptor authoring and generation

This phase provides deterministic, build-time declaration for code-authored
.NET operations.

- [ ] Add the supported public descriptor identity and operation-authoring value
  types to `Qhapaq.Abstractions`.
- [ ] Add the public marker and static declared-operation contracts.
- [ ] Add a dedicated Roslyn incremental-generator project.
- [ ] Accept descriptor documents only through explicit compiler build inputs.
- [ ] Enforce exact, case-sensitive, same-directory basename association.
- [ ] Validate descriptors against their exact offline schemas.
- [ ] Recompute and verify canonical contract digests.
- [ ] Verify one compatible `IOperation<TInput, TOutput>` implementation
  contract without constructing the operation or executing project code.
- [ ] Emit deterministic static declarations and reflection-free closed-generic
  registration.
- [ ] Emit the canonical portable manifest and expose identical embedded and
  packaged bytes.
- [ ] Emit stable, location-aware, payload-safe generator diagnostics.
- [ ] Test reproducibility across paths, cultures, machines, and input
  enumeration order.
- [ ] Add clean package-consumer tests for explicit descriptor inputs, generated
  registration, and embedded/package manifest byte equality.
- [ ] Exercise a minimal generated operation and closed-generic registration
  path in trimming and Native AOT smoke tests for the intended supported targets;
  resolve publication constraints before expanding the generator API.

**Depends on:** the applicable Phase 0 authoring decisions, Phase 0A, Phase 1
descriptor, manifest, digest, and diagnostic artifacts, and the corresponding
Phase 1A foundations.

**Completion gate:** a clean consumer project can author, validate, generate,
register, and package an operation using only supported contracts and explicit
build inputs.

### Phase 3: Implement registry core and native bindings

This phase creates the exact-resolution and native-binding core used by the
effective registry. Trusted source selection and host policy are completed in
Phase 3A; registry-core tests alone do not establish a conforming host.

- [ ] Implement immutable registry entries and exact ID, version, and digest
  lookup.
- [ ] Record implementation identity, integrity, and native input and output
  bindings separately from portable contract identity.
- [ ] Ingest generated registration and manifests without assembly scanning.
- [ ] Revalidate manifests and contract digests at runtime.
- [ ] Reject duplicate identities and conflicting digests across enabled
  sources.
- [ ] Verify agreement among descriptors, static declarations, generic native
  types, implementation identity, and registration-contract versions.
- [ ] Report the specified availability states without disclosing protected
  host configuration.
- [ ] Expose an immutable registry generation identity for plan-cache
  invalidation.
- [ ] Add registry, native-binding, unsupported-version, and conflict tests.
- [ ] Test the generated-registration-to-native-binding path from a clean
  consumer, including the supported trimming and Native AOT configuration.

**Depends on:** Phase 2 registration and manifest contracts and Phase 1A runtime
manifest, descriptor, and digest validation.

**Completion gate:** exact portable identities resolve deterministically to
explicitly registered native bindings, and invalid or ambiguous registrations
are unavailable before pipeline binding.

### Phase 3A: Establish trusted host configuration and policy

This milestone supplies the host prerequisites otherwise assumed by registry
construction, plan binding, and invocation. Its governing requirements are in
[SPEC-0002](0002-operation-catalogs-and-host-configuration.md)
and
[`0004-ai-assisted-connections.md`](0004-ai-assisted-connections.md).

- [ ] Specify and publish the exact host-profile, enabled-source, connection,
  and policy contracts and vectors needed by the initial supported host slice.
- [ ] Decide the initial authentication-provider set, protected state/token-cache
  behavior, extension packaging/integrity rules, and reload or restart boundary
  before implementing the corresponding capability; defer unsupported providers
  and sources explicitly.
- [ ] Validate explicitly selected trusted profiles and reject workspace trust
  elevation, unknown fields, invalid configuration, and invocation restrictions
  that would broaden policy.
- [ ] Build the effective registry only from explicitly enabled sources with
  required identity and integrity verification; fail startup or explicit reload
  rather than silently omit invalid sources or bindings.
- [ ] Implement descriptor-disclosure filtering and bind-time capability,
  side-effect, unsafe-retry, resource-scope, and connection-availability policy.
- [ ] Implement invocation-specific execution and independent payload-disclosure
  evaluation, including default-denied MCP payload disclosure.
- [ ] Implement logical connection and asynchronous credential-provider
  boundaries with destination/scope restrictions, cancellation, and redaction
  for the enabled provider set.
- [ ] Preserve immutable registry, connection, and policy snapshots across each
  run and invalidate affected plans at the specified configuration boundary.
- [ ] Test fail-closed startup, profile selection, integrity rejection, policy
  separation, credential non-disclosure, and snapshot/invalidation behavior.

The first host slice may use a small reviewed, effect-free operation source.
Test policy stubs are not a substitute for the trusted host implementation.
OpenAPI import, extension administration, and consent-broker delivery remain
explicit companion milestones; each must complete before its capability is
advertised or enabled.

**Depends on:** Phase 3 for effective registry construction, applicable Phase 1A
validation foundations, and the exact host contracts and vectors specified for
each enabled capability. Host-contract decisions can proceed independently of
registry implementation.

**Completion gate:** the supported host slice constructs a fail-closed immutable
effective registry and provides tested bind-time and invocation-time policy,
connection, credential, and disclosure boundaries.

### Phase 3B: Deliver the first non-executing Service and CLI slice

This milestone exercises the established layer boundaries before the full
binding and execution implementation exists, following the rollout in
SPEC-0006.

- [ ] Add the Phase 0 exact-descriptor-retrieval Service V1 request, result, and
  structured-error contracts to `Qhapaq.Abstractions`.
- [ ] Implement the Service, Business, and DAL collaboration for policy-filtered
  exact descriptor retrieval through constructor-injected adjacent-layer ports.
- [ ] Add the CLI request/result/diagnostic mapping over Service V1.
- [ ] Test exact-version lookup, unavailable/conflicting contracts, descriptor
  disclosure denial, cancellation, and safe diagnostics through the public
  Service boundary and CLI.
- [ ] Add a clean third-party Service consumer test and prove adapters cannot
  access Business, DAL, generator, or manifest internals directly.
- [ ] Prove the slice cannot execute operations, resolve credentials, install
  extensions, mutate profiles, or grant execution authority.

**Depends on:** the applicable Phase 0 Service and CLI contracts, Phase 0A,
Phase 3, and Phase 3A descriptor-disclosure and trusted source selection.

**Completion gate:** one real non-executing use case works end to end through
CLI and the public Service boundary without duplicating domain or policy rules.

### Phase 4: Implement parsing and portable validation

This phase produces inert definitions and structural document-validity
diagnostics without executing or binding operations. It may proceed in parallel
with Phases 2 through 3B once its own prerequisites exist. It does not claim
complete semantic validity or infer omitted operation-configuration defaults.

- [ ] Reject malformed JSON and duplicate object member names.
- [ ] Parse immutable definition models without activating types, loading
  extensions, resolving credentials, or accessing external resources.
- [ ] Select and validate the exact offline pipeline-format schema.
- [ ] Validate node identities, structural rules, bounded control flow, scopes,
  and dominance.
- [ ] Produce bounded, versioned, payload-safe structured diagnostics.
- [ ] Add tests proving invalid definitions cannot reach registry binding or
  begin side effects.
- [ ] Keep raw parsed definitions distinct from contract-normalized canonical
  definitions; do not publish a pre-normalization digest as the canonical
  definition identity.

**Depends on:** the applicable Phase 1 pipeline, schema-profile,
scope, and diagnostic artifacts, Phase 0A model ownership, and the corresponding
Phase 1A parsing and document-validation foundations.

**Completion gate:** the implementation passes the parsing, structural,
scope, and diagnostic conformance vectors while remaining independent of an
active operation registry. Contract-informed normalization and definition
digests are completed in Phase 6A.

### Phase 5: Implement the schema and mapping engines

This phase supplies portable instance validation, conservative compatibility,
and deterministic transform behavior using the Phase 1A foundations. Its
milestones may be delivered separately but do not relax the complete binding or
execution gates.

#### Phase 5A: Instance validation and schema compatibility

- [ ] Implement portable instance validation.
- [ ] Implement deterministic structural-subtype compatibility, including exact
  numeric constraint comparison.
- [ ] Pass instance-validation, compatibility, narrowing-boundary, and
  indeterminate-comparison rejection vectors using the shared pattern and
  format algorithms.

**Depends on:** applicable Phase 1 schema and compatibility vectors and Phase 1A
schema-profile foundations.

**Completion gate:** instance validation and conservative compatibility produce
the specified portable results without host-specific acceptance cases.

#### Phase 5B: Mapping parsing and static inference

- [ ] Parse mapping expressions into immutable expression models.
- [ ] Resolve each site's exact permitted mapping-language version without
  implicitly migrating another site.
- [ ] Implement static type inference with distinct `missing` and JSON `null`
  states.
- [ ] Pass parsing, inference, source-schema, narrowing, and language-version
  vectors, including unsupported-language host-bindability diagnostics.

**Depends on:** applicable Phase 1 mapping vectors, Phase 0A expression-model
ownership, and Phase 5A schema compatibility.

**Completion gate:** each supported mapping site has a typed expression model
with exact language identity and the specified static rejection behavior.

#### Phase 5C: Mapping evaluation and budgets

- [ ] Implement every specified mapping operator and checked failure behavior.
- [ ] Enforce expression, collection, memory, and output budgets.
- [ ] Pass deterministic evaluation, conversion, portable-limit boundary,
  runtime-failure, and budget vectors.

**Depends on:** Phase 5B, Phase 5A instance validation, and the applicable Phase 1
evaluation and failure artifacts.

**Completion gate:** the implementation passes the complete instance-validation,
compatibility, mapping, and transform-failure conformance suites.

### Phase 6: Normalize exact contracts and bind immutable plans

This phase converts a valid definition into disposable, host-specific derived
state without beginning execution.

#### Phase 6A: Contract-informed normalization and definition identity

- [ ] Resolve exact operation and decorator descriptors and their configuration
  schemas before selecting executable defaults.
- [ ] Normalize omitted optional configuration defaults, preserving explicit
  null and requiring explicit values for required properties.
- [ ] Validate the normalized configuration and materialize defaults into the
  canonical definition before hashing, persistence, review, or plan binding.
- [ ] Compute canonical definition bytes and digests using Phase 1A primitives.
- [ ] Test exact-contract default selection, unavailable/conflicting
  descriptors, omission/null distinctions, canonicalization, and definition
  digests without constructing operations or resolving credentials.

Normalization requires exact contract metadata, not an activated implementation.
An offline descriptor source may provide that metadata when the governing
contract permits it; it must preserve exact identity and digest verification.

**Depends on:** Phase 4, Phase 5A, applicable Phase 1 normalization and digest
vectors, and a verified exact descriptor source, supplied by Phase 3 for the
reference host.

**Completion gate:** canonical definitions contain all applicable executable
configuration defaults and have reproducible identities independent of
execution-time implementation construction.

#### Phase 6B: Complete binding and cache invalidation

- [ ] Resolve every operation and decorator by exact portable identity.
- [ ] Validate normalized operation and decorator configuration.
- [ ] Propagate schemas through every structural node.
- [ ] Validate transform sources, including `current-input`, `caught-failure`,
  lexical catch scope, dominance, inferred result schemas, and output schemas.
- [ ] Prove every operation connection schema-compatible.
- [ ] Verify all implementation-native input and output bindings.
- [ ] Pre-bind portable projectors, native materializers, mapping evaluators,
  and implementation factories.
- [ ] Compute slot consumers, last-consumer information, and resource budgets.
- [ ] Compute `forEach` item or chunk body schemas, maximum invocation counts,
  ordered aggregation, and nested resource bounds.
- [ ] Compute `tryCatch` unioned effects and capabilities and worst-case
  attempt-then-recovery resource bounds.
- [ ] Aggregate capabilities, side effects, idempotency, and required
  connections.
- [ ] Evaluate bind-time host policy and connection availability.
- [ ] Produce an immutable plan containing exact contract and implementation
  identities.
- [ ] Implement plan-cache keys and invalidation for every input listed in
  Section 19.
- [ ] Add rejection tests proving a partially validated or partially bound plan
  cannot execute.

**Depends on:** Phases 3 and 3A, Phase 4, Phases 5A through 5C, and Phase 6A.

**Completion gate:** every validation stage in Section 14 completes before a
plan is returned, and every specified invalidation input prevents reuse of a
stale plan.

### Phase 7: Implement the execution frame and runner

This phase executes one non-durable invocation of a completely bound plan.

#### Phase 7A: Execution frame and primitive/sequence execution

- [ ] Validate boundary input and reevaluate invocation-specific execution and
  disclosure permissions before side effects.
- [ ] Implement the private, per-run immutable execution frame and write-once
  node-output slots.
- [ ] Execute primitive operations and sequences with native input/output
  validation, structured failures, and cancellation.
- [ ] Prevent frame persistence, automatic payload logging, and external frame
  inspection from the first runner slice.
- [ ] Test that denied permission, invalid boundary input, and incomplete plans
  prevent every operation from starting.

**Depends on:** Phase 6B and Phase 3A invocation-time policy evaluation.

**Completion gate:** primitive and sequence runs obey the complete pre-execution
safety path and private frame/failure contracts.

#### Phase 7B: Transforms and final output

- [ ] Execute transform serialization boundaries using only pre-bound
  projectors, evaluators, validators, and materializers.
- [ ] Release frame slots after their final planned consumer when safe.
- [ ] Execute and validate the final output projection.
- [ ] Test transform and final-output failures, slot lifetime, and serialization
  boundaries without implicit conversion or payload disclosure.

**Depends on:** Phase 7A and Phase 6B pre-bound mapping and materialization.

**Completion gate:** transform and final-output vectors pass without exposing
undeclared frame state.

#### Phase 7C: Parallel and conditional execution

- [ ] Execute named parallel branches and conditionals with the specified
  branch, join, failure, cancellation, and convergence semantics.
- [ ] Observe every started task and preserve singleton failures and aggregate
  outcomes as specified.
- [ ] Test concurrency ceilings, cancellation races, multiple failures, and
  inaccessible branch outputs.

**Depends on:** Phase 7B.

**Completion gate:** concurrent and conditional vectors pass without lost
failures, partial-success results, or branch-scope escapes.

#### Phase 7D: Decorators and recovery

- [ ] Execute decorators with specified ordering, attempt bounds, failure
  contracts, and idempotency/unsafe-retry policy.
- [ ] Execute `tryCatch` with the specified catchability and recovery semantics.
- [ ] Implement lexical caught-failure projections without exposing raw
  exceptions, partial try outputs, or undeclared frame state.
- [ ] Test nested recovery, cancellation exclusions, retained side effects,
  recovery failure, and bounded causal trees.

**Depends on:** Phase 7C and the exact registered decorator contracts required
by the enabled slice.

**Completion gate:** decorator and recovery vectors pass without weakening
policy or implying transactional rollback.

#### Phase 7E: Bounded loops and collections

- [ ] Execute bounded loops and item-mode and chunk-mode `forEach` nodes.
- [ ] Implement iteration-local loop frames and expose only the final loop
  result.
- [ ] Implement invocation-local `forEach` frames and expose only the ordered
  aggregate result.
- [ ] Test empty input, cardinality, ordering, chunk boundaries, nested scopes,
  concurrency, failure, cancellation, and invocation bounds.

**Depends on:** Phase 7D.

**Completion gate:** loop and collection vectors pass with specified isolation,
aggregation, and bounded execution.

#### Phase 7F: Integrated budgets, failures, and privacy

- [ ] Enforce frame, transform, collection, loop, parallelism, and output
  budgets across nested compositions, including duration, operation, attempt,
  and iteration limits.
- [ ] Reuse existing typed composition primitives where their behavior matches
  the bound-plan semantics.
- [ ] Add execution, cancellation, aggregate-failure, budget, privacy, and
  no-partial-success tests across the complete runner.

**Depends on:** Phases 7A through 7E and the applicable Phase 1 execution vectors.

**Completion gate:** all execution conformance vectors pass, and tests prove
that no operation begins before complete validation, binding, and permission
evaluation.

### Phase 8: Add Service and authoring projections

This phase exposes shared use cases without allowing adapters to bypass Business
rules. It extends Phase 3B incrementally as each non-executing use case becomes
available; it does not wait for Phase 7 unless a use case genuinely needs runner
behavior.

- [ ] Add the remaining reviewed versioned public authoring Service contracts
  to `Qhapaq.Abstractions` and coordination to `Qhapaq.Service.V1`.
- [ ] Extend exact descriptor retrieval with policy-filtered descriptor listing.
- [ ] Expose the available parsing/structural-validation conclusions after
  Phase 4; report unavailable conclusions explicitly and do not imply complete
  semantic validity, canonical identity, or execution approval.
- [ ] Expose non-executing validation with all four conclusions from Section 14.
- [ ] Expose resolved dataflow, contract, effect, capability, and prerequisite
  explanation.
- [ ] Implement deterministic Mermaid projection and golden tests.
- [ ] Expose conservative operation-contract comparison.
- [ ] Add CLI authoring and validation adapters over Service V1.
- [ ] Add MCP authoring and validation adapters over Service V1.
- [ ] Prove that CLI and MCP adapters cannot access Business, DAL, generator, or
  manifest internals directly.

**Depends on:** the applicable Phase 0 Service, CLI, and MCP decisions and
Phase 3B. Descriptor listing depends on Phases 3 and 3A; parsing/structural
validation depends on Phase 4; full validation and resolved plan explanation
depend on Phase 6B. Contract comparison depends on Phase 5A and the exact
descriptor sources. Mermaid depends on the validated definition and any schema
analysis required by its promised summaries, not on execution.

**Completion gate:** CLI, MCP, and third-party adapters can consume the same
versioned Service behavior without duplicating validation, policy, binding, or
projection rules.

### Phase 9: Enable policy-gated execution

This phase enables execution through supported public entry points only after
the full safety and conformance path is present.

- [ ] Expose execution as a separate Service operation from validation and
  authoring.
- [ ] Add CLI execution mapping with the normative request, result, diagnostic,
  and exit-status behavior.
- [ ] Add MCP execution mapping with independent execution and payload-disclosure
  decisions.
- [ ] Prove authoring tools cannot install extensions, mutate trusted profiles,
  resolve credentials, execute operations, or grant authority.
- [ ] Pass all language-neutral parsing, validation, visualization, execution,
  and host conformance suites claimed by the implementation.
- [ ] Pass generator determinism, manifest byte-equality, registry validation,
  native-binding, cache-invalidation, and architecture tests.
- [ ] Pass security tests proving definitions cannot load code, access
  credentials, escape transform scope, expose frame data, or start side effects
  before complete validation.
- [ ] Verify trimming and Native AOT behavior for the supported publication
  targets.
- [ ] Document the enabled conformance capabilities and any deliberately
  unavailable optional surfaces.

**Depends on:** Phases 0 through 8 for every enabled execution surface.

**Completion gate:** policy-gated execution is enabled only when the complete
parse-to-permission path and all claimed conformance suites pass.

### Companion milestones and delivery boundaries

These milestones are tracked here to prevent the core rollout from being
mistaken for complete v1 delivery. Their exact contracts and acceptance tests
remain owned by the linked specifications. Complete each prerequisite before
enabling or advertising its dependent capability; optional conformance claims
do not silently remove requirements from the product's v1 scope.

- [ ] Implement canonical definition persistence and exact ID/version/digest
  resolution after Phase 6A, following
  [SPEC-0001](0001-core-pipeline-model.md) and
  [SPEC-0006](0006-dotnet-layered-architecture.md); do not persist execution
  frames or treat cached plans as portable definitions.
- [ ] Specify the invocation-skill bundle schema and vectors, then implement
  snapshot generation and the required CLI/MCP mappings under
  [SPEC-0001 Section 13](0001-core-pipeline-model.md#13-portable-pipeline-invocation-skills).
  Generation depends on exact contract validation, canonical definition
  identity, and host/disclosure policy; execution uses Phase 9 rather than a
  separate authority path. Optional reference mode additionally depends on
  exact persisted-definition resolution.
- [ ] Specify and implement supported OpenAPI import, generic HTTP execution,
  and installed-extension packaging/administration under
  [SPEC-0002](0002-operation-catalogs-and-host-configuration.md).
  Integrate each source with Phases 3 and 3A and test integrity, exact identity,
  destination/authentication restrictions, and equivalent portable descriptors
  before enabling it.
- [ ] Specify and implement trusted connection planning, independent local
  consent, authentication, sanitized status/testing, revocation, and the
  approved reload/restart flow under
  [SPEC-0004](0004-ai-assisted-connections.md).
  This depends on Phase 3A host boundaries and the enabled connector/provider
  contracts; MCP authoring or generic tool approval never substitutes for
  trusted local consent.
- [ ] Add shared local/CI scripts and blocking build, architecture, schema,
  conformance, and clean-consumer checks as the relevant artifacts appear under
  [SPEC-0005](0005-build-release-and-website-delivery.md).
  Build automation supports the early implementation milestones rather than
  waiting for Phase 9.
- [ ] Complete package composition, supported-target decisions, self-contained
  CLI/container verification, release-shaped builds, and clean installation
  tests before advertising those distributions under SPEC-0005.
- [ ] Complete website delivery and public-release legal, support, security,
  compatibility, and publication gates under
  [SPEC-0005](0005-build-release-and-website-delivery.md) and the
  [root artifact plan](../SPEC.md#8-initial-artifact-plan).
  Website work is independent of the core engine, not a prerequisite for plan
  binding.
- [ ] Verify that the v1 seams preserve the explicitly deferred capabilities in
  [SPEC-0003](0003-product-evolution-roadmap.md), without pulling remote
  providers, gRPC, multi-tenancy, or durable execution into this rollout.

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

### Host-runtime regular-expression engines

Delegating portable `pattern` evaluation directly to each host runtime's
built-in regular-expression engine would reduce implementation work, but those
engines differ in accepted grammar, Unicode unit, character classes, anchors,
empty-match behavior, and resistance to pathological backtracking. The same
pipeline could therefore be accepted, rejected, or evaluated differently across
.NET, Java, JavaScript, Go, Rust, and other hosts.

Qhapaq instead standardizes one small regular language and bounded NFA
algorithm. Each independent conforming implementation must provide those
semantics once in its shared schema engine; operations and pipelines reuse that
engine. An implementation may adapt an existing parser or automata library only
when it first enforces the closed grammar and proves the exact results,
normative construction limit, and evaluation bounds through the
language-neutral conformance vectors. A host's general-purpose regex engine is
not implicitly conforming merely because it accepts similar syntax.

This deliberately accepts contained implementation and maintenance cost in
exchange for deterministic portability, denial-of-service resistance, and no
silent expansion of the portable grammar when a host runtime evolves.

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

1. What are the exact public .NET declaration-contract and marker-attribute type
   names, generated API names, stable generator diagnostic codes, and initial
   generator compatibility matrix?
2. What are the exact CLI commands and MCP tool request and response schemas?
