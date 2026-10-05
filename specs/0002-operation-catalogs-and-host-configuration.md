# SPEC-0002: Operation Catalogs and Host Configuration

> **Status:** Draft  
> **Target:** Qhapaq v1  
> **Last updated:** 2026-10-04

## 1. Summary

Qhapaq users need to define which operations an installation can execute and how
those operations authenticate without compiling pipeline-specific code or
exposing secrets to pipeline documents or AI systems.

Qhapaq v1 uses two configuration domains:

1. A portable, commit-safe project catalog declares desired operations and their
   public schemas.
2. A trusted user host profile enables catalogs and extensions, binds logical
   authentication requirements to credential providers, and enforces execution
   policy.

Secret values remain outside both documents. The local single-user CLI and MCP
host are the v1 deployment target, while provider abstractions preserve a path
to tenant-scoped hosted deployments.

## 2. Goals

- Let users register APIs without generating or compiling code.
- Support non-HTTP primitives through explicitly installed precompiled
  extensions.
- Make the effective operation catalog discoverable to humans and AI systems.
- Keep pipeline definitions portable across machines and credential providers.
- Prevent a checked-out project from silently loading code or obtaining secrets.
- Keep credentials out of pipeline, catalog, profile, log, diagnostic, and MCP
  payloads.
- Fail configuration and binding deterministically before pipeline execution.
- Preserve an implementation-neutral catalog model where practical.

## 3. Non-goals

Qhapaq v1 does not:

- Compile source code or generate executable assemblies at runtime.
- Install extensions in response to a pipeline or MCP tool call.
- Treat extension isolation mechanisms as a security boundary.
- Provide a public extension marketplace.
- Let project configuration silently weaken user policy.
- Support arbitrary remote operation providers.
- Define full multi-tenant credential and configuration isolation.

Remote credential stores, hosted configuration, and remote operation providers
are intentional later capabilities. Their roadmap is defined in
[`0003-product-evolution-roadmap.md`](0003-product-evolution-roadmap.md).

## 4. Terminology

- **Operation descriptor:** portable normative contract and documentation
  metadata for one operation, including its stable ID, exact contract version,
  contract digest, schemas, capabilities, and side-effect classification.
- **Catalog:** a collection of operation descriptors and declarative connector
  registrations.
- **Extension:** trusted, precompiled implementation code and its manifest.
- **Host profile:** trusted local configuration that selects catalogs and
  extensions, binds credentials, and defines execution policy.
- **Credential profile:** a logical authentication binding whose provider
  obtains credential material without exposing it to the pipeline.
- **Secret reference:** an opaque instruction to a credential provider, not the
  secret itself.
- **Connection:** a trusted host binding among a logical resource name,
  connector, endpoint, credential profile, operation allowlist, and disclosure
  policy.

## 5. Operation Sources

### 5.1 Built-in Operations

The reference implementation may ship a small reviewed catalog of general
operations and decorators. Built-ins are versioned and described through the
same operation-descriptor model as other sources.

Shipping an operation does not automatically grant it unrestricted access.
Built-ins remain subject to host capability, filesystem, network, and resource
policy.

### 5.2 Declarative OpenAPI Connectors

An OpenAPI connector turns explicitly selected OpenAPI operations into Qhapaq
operation descriptors backed by the reference implementation's generic HTTP
executor.

Registration must:

- Reference a supported, versioned OpenAPI document.
- Select operations explicitly by stable OpenAPI `operationId`.
- Assign or derive a stable Qhapaq operation ID and exact version.
- Map request parameters and bodies to the input schema.
- Map documented success responses to the output schema.
- Declare accepted status codes and structured failure behavior.
- Name a logical credential requirement when authentication is needed.
- Declare network destinations or server aliases that host policy can restrict.

Importing an OpenAPI document must not expose every endpoint by default.
Endpoints without a stable `operationId`, ambiguous schemas, unsupported
authentication, or deterministic response mapping must be rejected until the
catalog supplies an explicit override.

For reproducibility, a remote OpenAPI document should be imported as a local
snapshot or pinned by a cryptographic digest. Hosts must not silently execute
against changed connector metadata.

### 5.3 Precompiled .NET Extensions

A precompiled extension contains:

- One or more assemblies targeting the supported Qhapaq extension contract.
- A versioned extension manifest.
- Operation and decorator descriptors with exact immutable contract versions
  and digests.
- Exact package and implementation versions.
- Declared capabilities and external dependencies.
- Integrity information for installed artifacts.

Extensions are installed through an explicit user or administrator action and
loaded only from locations enabled by the active trusted host profile. Loading
occurs at process startup or an explicit host restart boundary, not during a
pipeline run.

An extension executes arbitrary code with the Qhapaq process identity.
Assembly-load contexts, dependency isolation, signatures, and package hashes can
improve reliability and provenance but do not make untrusted code safe.

The MCP surface must not install, update, enable, or discover arbitrary
filesystem extensions. It may report descriptors for extensions already enabled
by the host.

Code-authored .NET operations use the static declaration and generated-manifest
model defined in
[`0007-portable-pipeline-definitions-and-binding.md`](0007-portable-pipeline-definitions-and-binding.md).
Registration remains explicit and does not scan assemblies reflectively.
OpenAPI-backed and code-authored operations produce the same portable descriptor
shape.

## 6. Portable Project Catalog

The conventional project file is `.qhapaq/qhapaq.catalog.json`. It is intended
to be safe to review and commit.

A catalog may contain:

- Catalog format, ID, and version.
- OpenAPI document references and integrity digests.
- Explicitly selected API operations.
- Stable Qhapaq operation IDs and versions.
- Schema and response-mapping overrides.
- Logical authentication requirement names.
- Required capabilities and documented side effects.
- Human-readable descriptions and examples.

A catalog must not contain:

- Secret values, access tokens, private keys, or passwords.
- Credential-provider configuration tied to one user or machine.
- Paths from which the runtime will load executable assemblies.
- Instructions that automatically install an extension.
- Policy overrides that broaden network, filesystem, or process access.

Illustrative shape:

```json
{
  "format": "qhapaq.catalog/v1",
  "id": "contoso.orders",
  "version": "1.0.0",
  "connectors": [
    {
      "type": "openapi",
      "document": "./openapi/orders.json",
      "sha256": "<digest>",
      "operations": [
        {
          "operationId": "getOrder",
          "id": "contoso.orders.get",
          "version": "1.0.0",
          "authentication": "orders.read"
        }
      ]
    }
  ]
}
```

The exact normative schema will live under `schemas/` and may refine these
property names.

## 7. Trusted User Host Profile

The host profile is security-sensitive local configuration. It selects what the
process trusts and can execute.

A profile contains:

- Enabled project catalogs, preferably with expected IDs or digests.
- Enabled precompiled extensions and exact versions or integrity values.
- Bindings from logical authentication names to credential profiles.
- Connection bindings for logical resources requested by project catalogs.
- Network, filesystem, process, and operation allowlists.
- Execution budgets for duration, concurrency, attempts, iterations, memory,
  and output size.
- Whether pipeline execution is enabled for CLI and MCP entry points.
- Diagnostic, cache, and token-storage settings.

Illustrative shape:

```json
{
  "format": "qhapaq.host/v1",
  "profile": "work",
  "catalogs": [
    {
      "path": "C:\\src\\orders\\.qhapaq\\qhapaq.catalog.json",
      "id": "contoso.orders"
    }
  ],
  "extensions": [
    {
      "id": "contoso.qhapaq.files",
      "version": "1.2.0",
      "path": "C:\\Users\\me\\AppData\\Local\\Qhapaq\\extensions\\contoso.qhapaq.files\\1.2.0",
      "sha256": "<digest>",
      "allow": ["contoso.files.append"]
    }
  ],
  "credentials": {
    "orders.read": {
      "provider": "oauth-client-credentials",
      "clientId": "${env:ORDERS_CLIENT_ID}",
      "clientSecret": "${secret:orders-client-secret}",
      "scopes": ["orders.read"]
    }
  },
  "policy": {
    "executionEnabled": true,
    "allowedHosts": ["api.contoso.example"],
    "maxParallelism": 8,
    "maxDuration": "00:05:00"
  }
}
```

This example uses Windows paths only illustratively. The normative format must
support portable path and URI handling.

## 8. Profile Discovery and Storage

The host must use an explicitly selected profile:

```text
qhapaq mcp --profile work
qhapaq run pipeline.json --profile work
qhapaq mcp --config <absolute-profile-path>
```

A named profile resolves in the operating system's user configuration
directory:

- Windows: `%APPDATA%\Qhapaq\profiles\<name>.json`
- Linux: `$XDG_CONFIG_HOME/qhapaq/profiles/<name>.json`, falling back according
  to the XDG Base Directory specification.
- macOS: `~/Library/Application Support/Qhapaq/profiles/<name>.json`

Qhapaq must not automatically treat a workspace file as a trusted host profile.
The current working directory cannot implicitly enable extensions, bind
credentials, or broaden policy.

V1 profiles do not inherit from or merge with other profiles. An explicit
`--config` path and a named `--profile` are mutually exclusive. Security policy
collections replace rather than merge, and unknown properties are rejected.
Command-line options may further restrict policy for one invocation but must not
silently broaden the active profile.

## 9. Authentication and Credential Providers

Pipeline definitions and project catalogs refer only to logical authentication
requirements such as `orders.read`. The trusted host profile binds each
requirement to a credential provider.

A credential provider:

- Resolves credentials only when required by an allowed operation.
- Returns authentication material directly to the transport adapter.
- Restricts credentials to their configured destination and scopes.
- Refreshes expiring credentials without exposing refresh tokens.
- Redacts credential material from exceptions and diagnostics.
- Supports cancellation and reports actionable authentication failures.

The initial provider set remains to be finalized. Candidate providers include:

- No authentication.
- API keys resolved from a secret reference.
- Static bearer tokens resolved from a secret reference.
- OAuth 2.0 client credentials.
- Interactive OAuth authorization code or device authorization.
- Environment-variable and OS-protected secret-reference resolvers.

The generic HTTP executor applies authentication after policy approves the
destination. A pipeline cannot read a credential, choose an arbitrary destination
for it, or override the provider's header and scope restrictions.

Credential and token caches are state, not configuration. When persisted, they
must use OS-appropriate access controls and protection at rest. The host must
support clearing cached credentials without editing catalogs or pipelines.

Future hosted deployments can replace the local credential-provider
implementation with request- or tenant-scoped providers while preserving the
logical authentication names in catalogs and pipelines.

Later provider packages may resolve secrets or credentials from remote systems
such as Azure Key Vault. V1 interfaces must therefore support asynchronous
resolution, cancellation, refresh, expiration, redaction, and provider-specific
configuration without placing provider credentials in portable catalogs.

## 10. Effective Catalog Construction

At startup, the host:

1. Loads and validates the explicitly selected trusted profile.
2. Resolves and validates enabled catalog paths and expected identities.
3. Validates OpenAPI documents, integrity, selected operations, and schemas.
4. Loads explicitly enabled extensions and validates manifests and integrity.
5. Rejects duplicate operation ID and contract-version pairs and rejects
   conflicting contract digests.
6. Binds logical authentication requirements to configured providers.
7. Applies capability and operation allowlists.
8. Produces an immutable effective operation registry.

Any error fails host startup or explicit reload. The host must not silently omit
an invalid catalog, extension, credential binding, or policy rule and then report
partial success.

The effective registry is immutable during a pipeline run. Configuration changes
take effect only after an explicit reload boundary that rebuilds and revalidates
the complete registry.

## 11. MCP Administration Boundary

The MCP server may:

- List effective operation descriptors.
- Explain why an operation is unavailable.
- Validate pipelines against the effective registry.
- Execute allowed pipelines when execution is enabled.
- Report non-secret profile identity and policy limits.
- Propose immutable connection setup plans and request an independent trusted
  local consent flow.

The MCP server must not:

- Install, update, or enable an extension.
- Add a catalog to the trusted profile.
- Create or modify credential-provider bindings.
- Return secret references when those references reveal sensitive identifiers.
- Return tokens, API keys, private keys, or credential-cache contents.
- Broaden network, filesystem, process, or execution policy.
- Select a different trusted profile after startup.

Administrative CLI commands, if provided, must be separate from model-accessible
MCP tools and require an explicit local user action. An approved local consent
broker may apply a specific proposed connection plan without giving MCP general
profile-administration authority. That flow is defined in
[`0004-ai-assisted-connections.md`](0004-ai-assisted-connections.md).

## 12. Security Considerations

- Treat project catalogs, OpenAPI descriptions, examples, and extension metadata
  as untrusted input.
- Prevent server URLs or redirects from bypassing host network allowlists.
- Revalidate the destination after redirects and DNS-sensitive policy checks.
- Do not send a credential to a destination other than the provider's approved
  audience.
- Pin extension versions and verify artifact integrity before loading.
- Reject duplicate or shadowed operation identities.
- Avoid logging request bodies, response bodies, authorization headers, or
  secret-reference resolutions by default.
- Make catalog, extension, credential-provider, and policy provenance visible in
  local diagnostics without exposing secrets.
- Do not claim that an extension sandbox exists unless execution is isolated by
  an independently specified security boundary.

## 13. Testing Strategy

- Catalog and host-profile JSON Schema conformance tests.
- Tests proving project catalogs cannot load assemblies or contain secrets.
- OpenAPI import tests for explicit selection, schema mapping, response mapping,
  unsupported constructs, and digest mismatch.
- Extension manifest, version, integrity, duplicate-ID, and startup-failure
  tests.
- Profile discovery and precedence tests on every supported operating system.
- Tests proving command-line restrictions cannot broaden profile policy.
- Credential redaction, destination binding, scope, refresh, and cancellation
  tests.
- Tests proving MCP cannot administer catalogs, extensions, credentials, or
  policy.
- Tests proving invalid configuration fails before any pipeline operation starts.

## 14. Open Questions

1. Which authentication and secret-reference providers are required for v1?
2. Which OpenAPI versions, schema features, and authentication schemes are
   supported?
3. How are extensions packaged, installed, updated, and removed?
4. Are extension signatures required in addition to exact versions and hashes?
5. What capability and side-effect vocabulary is normative?
6. What controlled reload mechanism, if any, is supported by CLI and MCP hosts?
7. Which state and token-cache protections are required on each supported
   operating system?
