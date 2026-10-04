# SPEC-0003: Product Evolution Roadmap

> **Status:** Draft  
> **Scope:** Post-v1 product direction  
> **Last updated:** 2026-10-04

## 1. Purpose

This document records important product capabilities that are intentionally
deferred from Qhapaq v1. They are not commitments to a release date, but v1
architecture must preserve a credible path to them.

The roadmap prevents local-process assumptions from becoming accidental
portable contracts and distinguishes deferred evolution from rejected scope.

## 2. Roadmap Principles

- Portable pipeline, catalog, operation, error, and policy models remain
  independent of transport and implementation language.
- Local and remote hosts use the same core application services and execution
  semantics.
- Remote boundaries use explicit versioned protocols and conformance tests.
- Authentication, authorization, policy, and tenant context are host concerns,
  not fields containing credentials in pipeline definitions.
- Network boundaries do not imply exactly-once execution or transactional
  behavior.
- Remote capabilities are opt-in and secure by default.
- Later features must not require existing pipeline documents to embed machine
  paths, CLR type names, transport addresses, or secret-store credentials.

## 3. V1 Foundations

V1 delivers local single-user CLI and MCP hosting, but establishes:

- An asynchronous credential-provider abstraction with cancellation, refresh,
  expiration, and redaction behavior.
- Logical authentication requirement names in portable catalogs.
- Host-owned bindings from logical requirements to credential providers.
- Application services for catalog discovery, validation, visualization,
  planning, execution, cancellation, and diagnostics that are not coupled to
  CLI or MCP transports.
- Portable operation descriptors and JSON Schemas.
- An immutable effective operation registry constructed from configured
  providers.
- Structured errors suitable for mapping to CLI, MCP, and future gRPC status
  details.
- Execution and policy abstractions that can accept a future request, user, or
  tenant scope without adding such context to `IOperation`.

V1 does not need to ship a generic distributed abstraction merely to reserve
these seams.

## 4. Remote Credential and Secret Providers

### 4.1 Direction

Later releases should support provider packages that resolve secret material or
obtain credentials from remote systems. Azure Key Vault is a primary example;
other providers may include hosted cloud secret managers, HashiCorp Vault, and
organization-specific credential brokers.

A secret store and a credential provider are related but distinct:

- A **secret store provider** retrieves protected values such as API keys or
  client secrets.
- A **credential provider** obtains authentication material such as OAuth access
  tokens and may use a secret store as one input.

Keeping these contracts separate avoids exposing raw secrets to transports that
need only a token.

### 4.2 Required Behavior

Remote providers must define:

- Versioned, provider-specific non-secret configuration.
- Authentication of Qhapaq to the provider, preferably through workload,
  managed, or user identity rather than another stored secret.
- Authorization and least-privilege requirements.
- Asynchronous resolution, cancellation, timeout, retry, and circuit-breaking
  behavior.
- Cache, refresh, rotation, expiration, and revocation semantics.
- Redaction and audit behavior.
- Actionable failure classification without secret disclosure.
- Behavior during provider unavailability.

Portable catalogs continue to use logical authentication requirement names.
Trusted host configuration selects the provider and stores only non-secret
settings and opaque references.

### 4.3 Compatibility Requirements

Adding a remote provider must not:

- Change pipeline documents.
- Expose provider references or values through MCP catalog discovery.
- Require an operation to understand the provider.
- Let a project catalog select a privileged provider without host approval.
- Treat a remote call failure as an absent optional secret.

## 5. Local and Remote Qhapaq Hosting over gRPC

### 5.1 Direction

A future Qhapaq gRPC host will expose the engine as a versioned service. Clients
in any language can use it instead of launching the CLI or embedding the .NET
library.

The same service contract should support:

- A local sidecar or daemon reached through an appropriate local transport.
- A remote service reached over authenticated and encrypted HTTP/2 or a later
  compatible gRPC transport.

The deployment mode changes hosting and security policy, not pipeline semantics.

### 5.2 Candidate Service Capabilities

- Discover effective operation descriptors.
- Validate and canonicalize pipeline definitions.
- Generate Mermaid visualization.
- Bind or inspect execution plans without exposing implementation internals.
- Start an execution.
- Stream execution status and permitted diagnostics.
- Cancel an execution.
- Retrieve a bounded result or structured failure.
- Report server capabilities, limits, and protocol versions.

Administrative APIs for profiles, extensions, credentials, or policy must be
separate from ordinary execution APIs and are not implied by this roadmap.

### 5.3 Required Protocol Semantics

The future protocol must specify:

- Protobuf schemas and independent protocol versioning.
- Capability negotiation.
- Deadlines and cancellation propagation.
- Authentication and authorization.
- Transport encryption and server identity validation.
- Request, user, and tenant context where applicable.
- Input, output, message, and diagnostic size limits.
- Streaming backpressure and disconnection behavior.
- Stable structured error details.
- Idempotency keys where a request can be safely deduplicated.
- Audit identifiers and trace-context propagation.

A client retry does not imply safe operation retry. The protocol must expose
enough information for clients to distinguish transport failure from confirmed
execution failure, while avoiding unsupported exactly-once claims.

## 6. Remote Operation Providers over gRPC

### 6.1 Direction

A remote operation provider allows a Qhapaq host to use primitives implemented
in another process, language, trust zone, or service. This is distinct from a
remote Qhapaq host:

- A **remote Qhapaq host** executes the pipeline for a client.
- A **remote operation provider** executes one or more primitive operations for
  a Qhapaq engine.

This capability provides a path for Python, TypeScript, Java, Go, and isolated
service implementations to contribute operations without implementing the full
Qhapaq engine.

### 6.2 Provider Capabilities

A future provider protocol should support:

- Descriptor discovery with exact operation versions and schemas.
- Provider identity, health, and capability negotiation.
- Typed JSON or another explicitly negotiated portable value encoding.
- Unary execution initially, with streaming introduced only through an explicit
  operation contract.
- Deadlines and cancellation.
- Structured results and failures.
- Trace-context and correlation propagation.
- Authentication, authorization, and transport encryption.
- Concurrency, payload, duration, and resource limits.

The host builds remote descriptors into its effective registry only when trusted
host configuration enables the provider and policy allows its capabilities.

### 6.3 Execution Semantics

Remote invocation introduces ambiguity that does not exist for a completed local
task. The provider protocol must define:

- Whether an operation is idempotent and safe to retry.
- How the host handles connection loss after dispatch.
- Whether a provider supports a caller-supplied idempotency key.
- How cancellation races with completion.
- How provider-side throttling and temporary failure are represented.
- Which side owns serialization validation.

Network retries are not automatic operation retries. Retry behavior remains an
explicit Qhapaq policy and must account for the operation's declared side
effects.

### 6.4 Security Boundary

A remote provider is untrusted until enabled by the host. Descriptor discovery
does not grant execution permission. Host policy must constrain provider
identity, operation IDs, versions, destinations, credentials, capabilities, and
resource use.

A provider must never receive host credentials unrelated to the selected
operation. If an operation needs downstream authentication, the architecture
must explicitly choose between provider-owned credentials, delegated tokens, or
a constrained credential-broker protocol.

## 7. Hosted Identity and Configuration

Remote hosting eventually requires configuration and identity scopes beyond the
v1 user profile:

- Service-instance configuration.
- Environment configuration.
- Tenant configuration.
- User or workload identity.
- Request-scoped policy and delegated credentials.

The effective configuration model must define precedence without allowing a
less-trusted scope to broaden a more-trusted policy. Tenant isolation applies to
catalogs, extensions, providers, credentials, caches, plans, diagnostics, and
results.

Hosted support does not require exposing `IServiceProvider`, credentials, or a
general execution-context property bag to operations. Narrow interfaces and
transport-independent request context should be specified when the hosted use
cases are designed.

## 8. Suggested Evolution Sequence

The following order reduces architectural risk without assigning release dates:

1. Stabilize v1 portable schemas, execution semantics, CLI/MCP behavior, host
   services, and local credential-provider abstractions.
2. Add selected remote credential and secret providers, beginning with a
   separately packaged Azure Key Vault integration.
3. Specify and implement a local gRPC sidecar using the existing host services.
4. Harden the same gRPC host contract for authenticated remote deployment.
5. Specify remote operation-provider discovery and execution as a separate gRPC
   protocol.
6. Add hosted and tenant-scoped configuration, policy, credentials, and
   isolation only with an explicit service-hosting specification.

Each step requires its own accepted specification and threat model.

## 9. Deferred Capability Register

| Capability | V1 status | Required v1 seam |
| --- | --- | --- |
| Azure Key Vault credential and secret provider | Deferred | Asynchronous provider and logical credential bindings |
| Other remote secret stores | Deferred | Provider-neutral configuration and redaction |
| Local gRPC Qhapaq sidecar | Deferred | Transport-independent host application services |
| Remote gRPC Qhapaq service | Deferred | Portable schemas, structured errors, cancellation, and policy |
| Remote gRPC operation providers | Deferred | Portable descriptors, registry source abstraction, and value schemas |
| Multi-language primitive providers | Deferred | Remote provider protocol and conformance suite |
| Multi-tenant hosting | Deferred | Narrow request/tenant context and scoped providers |
| Durable execution and recovery | Deferred separately | Stable definitions and explicit run identity |

## 10. Non-commitments

This roadmap does not:

- Assign features to semantic-version numbers or dates.
- Select a final Protobuf schema or gRPC framework.
- Promise that every local operation can safely execute remotely.
- Promise transparent failover, exactly-once behavior, or durable execution.
- Make Azure Key Vault or any cloud service a dependency of the core packages.
- Require remote operation providers to use .NET.

## 11. Open Questions

1. Which Azure Key Vault capabilities belong in the first remote provider:
   secrets only, keys and certificates, or credential brokering as well?
2. Which local gRPC transports must be supported on each operating system?
3. Are the Qhapaq host and remote operation-provider protocols versioned and
   packaged independently?
4. Which value encoding is used for remote operation invocation?
5. How are provider identity and operation-descriptor provenance represented?
6. Which hosted authentication mechanisms and tenant-isolation guarantees are
   required?
7. Which protocol operations require idempotency keys?
