# SPEC-0004: AI-Assisted Connections

> **Status:** Draft  
> **Target:** Qhapaq v1 connection architecture  
> **Last updated:** 2026-10-04

## 1. Summary

Users should be able to ask an MCP-capable AI system to connect a workspace to
an internal or external resource and then create pipelines using that resource.
Authentication mechanisms may include Microsoft Entra ID, OAuth, API keys,
database credentials, certificates, managed identities, or future credential
providers.

MCP can discover connector capabilities and propose an immutable connection
setup plan. It cannot approve the plan, obtain credentials, or directly modify
the trusted host profile. A separate trusted local Qhapaq consent broker shows
the exact endpoint, identity mechanism, scopes, operations, and data-disclosure
policy to the user and applies only the approved plan.

Permission to execute against a resource and permission to disclose its payloads
to an MCP client are separate. Payload disclosure is denied by default.

## 2. Goals

- Let users begin connection setup through a natural-language request.
- Support internal and external resources through connector packages.
- Keep connector, endpoint, identity, scope, and policy choices explicit.
- Keep credentials and reusable authentication artifacts outside the model
  context.
- Make consent specific, reviewable, time-limited, and bound to one immutable
  plan.
- Store portable requirements separately from trusted machine/user bindings.
- Let an AI create pipelines after a connection becomes available.
- Prevent resource access from implicitly authorizing data disclosure to the AI.
- Preserve the same model for future local, remote, and hosted Qhapaq hosts.

## 3. Non-goals

This specification does not:

- Let an MCP tool silently add credentials, extensions, endpoints, or scopes.
- Treat the MCP client's generic tool-call confirmation as sufficient consent.
- Let the AI receive access tokens, refresh tokens, API keys, passwords,
  certificates, private keys, or device-login codes.
- Guarantee that every service can be configured without an administrator.
- Define every connector or authentication provider.
- Make arbitrary SQL, Kusto, Graph, or HTTP access safe by default.
- Authorize sending internal data to an AI merely because the AI requested the
  connection.

## 4. Connection Model

A connection binds:

```text
logical resource name
+ connector ID and exact version
+ resource endpoint and identity
+ credential profile
+ allowed operation IDs
+ granted scopes or permissions
+ execution and resource policy
+ MCP payload-disclosure policy
```

The logical resource name is portable. The remaining binding is trusted host
configuration and may differ by user, machine, environment, or tenant.

An operation descriptor references a logical connection requirement rather than
embedding a token, connection string, tenant-specific credential, or machine
path. Binding a pipeline fails before execution when the active host does not
provide a compatible connection.

## 5. Connector Model

A connector is built-in or supplied by an explicitly installed extension. Its
descriptor declares:

- Stable connector ID and exact version.
- Resource configuration JSON Schema.
- Supported authentication mechanisms.
- Required and optional scopes or permissions.
- Operation descriptors it can expose.
- Discovery capabilities and their required permissions.
- Network destinations and redirect behavior.
- Side-effect, data-access, and sensitivity classifications.
- Whether operations accept constrained templates or arbitrary queries.
- Connection-test behavior that does not leak sensitive records.

The descriptor is informational and does not grant access. The active host
profile and local consent decision constrain every declared capability.

## 6. Example Connector Families

### 6.1 Microsoft SharePoint

A SharePoint connector may use Microsoft Graph or an explicitly supported
SharePoint API. A connection plan identifies the tenant, site or resource,
connector operations, Microsoft Entra authentication mode, and exact delegated
or application permissions.

Delegated authentication requires the local user to complete an interactive
flow. Application permissions commonly require separate tenant-administrator
consent and must not be presented as ordinary user consent.

### 6.2 Azure Data Explorer / Kusto

A Kusto connector identifies the cluster and database separately from its Entra
credential profile. Host policy restricts cluster destinations and allowed
operations.

Connectors should prefer parameterized, schema-aware operations or reviewed
query templates. Exposing unrestricted query text is a separate privileged
capability.

### 6.3 SQL Databases

A SQL connector identifies the server, database, transport requirements, and
credential profile. Supported authentication can include Entra identity,
integrated identity where available, certificates, or secret-backed database
credentials.

Database operations use parameters rather than string interpolation. Arbitrary
SQL execution, schema mutation, and administrative commands are separately
classified capabilities and are disabled unless explicitly allowed.

### 6.4 External APIs

An OpenAPI connector identifies explicitly selected operations, approved server
origins, and an OAuth or secret-backed credential profile. Importing an API
description does not approve its destinations, redirects, or requested scopes.

## 7. Workspace Requirements and Host Bindings

A portable project catalog can declare a connection requirement:

```json
{
  "name": "corporate-sharepoint",
  "connector": "qhapaq.microsoft-graph.sharepoint",
  "operations": [
    "sharepoint.files.list",
    "sharepoint.files.read"
  ],
  "authentication": {
    "kind": "entra-delegated",
    "scopes": [
      "Sites.Read.All"
    ]
  }
}
```

This is a request, not a grant. The trusted user host profile binds the logical
name to an approved resource:

```json
{
  "connections": {
    "corporate-sharepoint": {
      "connector": {
        "id": "qhapaq.microsoft-graph.sharepoint",
        "version": "1.0.0"
      },
      "resource": {
        "tenant": "contoso.onmicrosoft.com",
        "site": "https://contoso.sharepoint.com/sites/engineering"
      },
      "credential": "contoso-delegated-user",
      "allowOperations": [
        "sharepoint.files.list",
        "sharepoint.files.read"
      ],
      "mcpDisclosure": {
        "allowPayloads": false
      }
    }
  }
}
```

The normative schemas may refine these illustrative property names. Host policy
may grant fewer operations or scopes than the project requests, never more
without a separate explicit local action.

## 8. MCP Setup Surface

The MCP server may expose tools equivalent to:

- `connections.listConnectorTypes`: list installed connector descriptors.
- `connections.plan`: create a setup plan without changing trusted state.
- `connections.getStatus`: report sanitized connection readiness and health.
- `connections.requestConsent`: ask the trusted local broker to present a plan.
- `connections.test`: test an already approved connection without returning
  resource payloads.
- `operations.list`: discover operations available after connection binding.

Names are illustrative until the MCP contract is specified.

The MCP response can include required configuration fields, scopes, connector
installation status, administrative prerequisites, and a sanitized outcome. It
must not include credential material or protected token-cache state.

MCP cannot directly edit a host profile. Requesting consent does not imply that
the user approved, authenticated, or completed setup.

## 9. Immutable Connection Plans

A setup plan contains:

- Unique plan ID.
- Creation and expiration timestamps.
- Target host-profile identity.
- Workspace and catalog identity.
- Connector ID, version, provenance, and integrity.
- Resource type, endpoint, tenant, database, site, or equivalent identity.
- Authentication mechanism and credential-provider type.
- Exact requested scopes or permissions.
- Operations to enable.
- Network and capability-policy changes.
- MCP payload-disclosure setting.
- Files and trusted settings that would change.
- Human-readable risk and administrator-consent information.
- A canonical digest covering every security-relevant field.

Plans are short-lived and single-use. Any material change creates a new plan and
requires new consent. The broker does not accept model-authored display text as
the authoritative description of security-sensitive fields.

## 10. Trusted Local Consent Broker

The consent broker is a local Qhapaq-controlled user interface or process
boundary independent of the conversational model. It:

1. Receives a setup plan from the running Qhapaq host.
2. Recomputes and verifies the canonical digest.
3. Displays the connector, publisher, endpoint, tenant, scopes, operations,
   side effects, and MCP disclosure policy.
4. Identifies permissions requiring tenant-administrator consent.
5. Allows the user to approve, reject, or reduce optional permissions.
6. Performs interactive authentication without routing artifacts through MCP.
7. Applies profile and credential-store changes atomically.
8. Records a non-secret local audit event.
9. Returns only a sanitized result to the MCP host.

Reducing a permission produces a new effective plan and validation pass.
Increasing or redirecting any permission requires a new consent interaction.

Generic MCP tool-call approval is not a substitute for this broker because MCP
clients differ in confirmation behavior and may not display the complete
security context.

## 11. Authentication Flow

Connector authentication is delegated to a credential provider selected by the
trusted plan and host profile.

For interactive Microsoft Entra or OAuth authentication:

- The broker opens or directs a trusted local browser or device flow.
- Login and consent occur directly with the identity provider.
- Device codes, authorization codes, tokens, and refresh tokens do not enter the
  model conversation or MCP response.
- The provider validates tenant, audience, scopes, redirect destination, state,
  nonce, and applicable proof mechanisms.
- The protected token cache belongs to the credential provider.

For secret-backed authentication:

- The broker writes or selects a secret through a configured secret-reference
  provider.
- The host profile stores only an opaque reference.
- Connection testing retrieves the secret directly into the transport adapter.

For managed or workload identity:

- The broker verifies that the active hosting environment supports the identity.
- The profile stores resource and provider configuration, not a credential.

Authentication success does not override Qhapaq operation, network, or
disclosure policy.

## 12. Execution and Disclosure Are Separate

Every connection has at least two independent permissions:

1. **Execution permission:** whether a pipeline operation may access the
   resource.
2. **Disclosure permission:** whether operation payloads may cross a host
   boundary such as an MCP response.

MCP payload disclosure is denied by default. An allowed operation may still:

- Feed its output to later local pipeline operations.
- Write to an explicitly approved local or remote sink.
- Return non-sensitive status and aggregate metadata.

It may not return records, documents, query results, or other payloads to the MCP
client unless the active host policy explicitly allows disclosure for that
connection or operation.

Disclosure approval identifies the destination class and may impose field
redaction, row limits, byte limits, content classification, or summarization.
Allowing MCP disclosure does not automatically allow another network sink.

Pipeline validation must account for source and sink policy where possible.
Qhapaq must not claim complete information-flow control when an extension can
perform undeclared side effects.

## 13. Connection State and Reload

A connection has a sanitized state such as:

- `requested`
- `awaiting-user-consent`
- `awaiting-administrator-consent`
- `authenticating`
- `ready`
- `degraded`
- `expired`
- `revoked`
- `invalid`

State responses include actionable non-secret diagnostics. They do not reveal
whether a particular secret reference exists when that would disclose sensitive
configuration.

After approval, the host atomically rebuilds its effective registry or requests
an explicit restart according to host policy. Pipelines already running retain
the immutable connection and policy snapshot with which they began unless a
credential is revoked.

## 14. Integration with MCP Clients

Any MCP client that can start or connect to the Qhapaq MCP server can use this
flow, including AI development environments and desktop assistants. Integration
does not require client-specific access to credentials.

The client sees:

- Connector capabilities and configuration questions.
- The immutable setup-plan summary.
- A notice that local consent is required.
- Sanitized connection status.
- Available operation descriptors after approval.

The trusted broker, not Claude, GitHub Copilot, or another model, sees and
handles authentication artifacts. A client-specific installer may help register
the Qhapaq MCP server, but the Qhapaq security model cannot depend solely on that
client's tool-confirmation UI.

## 15. Audit and Revocation

Local audit records should include:

- Plan digest and profile identity.
- Connector, resource, operations, and scopes.
- Consent outcome and time.
- Whether administrator consent was required.
- Connection-test outcome.
- Profile reload or restart result.
- Revocation and credential-cache clearing.

Audit records exclude tokens, secrets, authorization codes, device codes,
passwords, private keys, and returned resource payloads.

Users can disable or remove a connection, clear its credential cache, and revoke
provider-side consent through documented local administrative commands. Removal
causes dependent pipelines to fail binding before execution.

## 16. Security Considerations

- Treat model-generated endpoints, tenant IDs, scopes, query text, and
  descriptions as untrusted.
- Normalize and independently display resource identities.
- Prevent redirects, aliases, or DNS behavior from changing an approved
  destination.
- Bind approval to the complete canonical plan digest.
- Require new consent for connector, endpoint, tenant, credential mechanism,
  scope, operation, network, or disclosure changes.
- Do not expose device codes or login URLs containing sensitive state through
  MCP.
- Do not let connection tests return sample records by default.
- Distinguish delegated user consent from tenant-administrator consent.
- Apply least privilege and prefer constrained operation templates over
  arbitrary query or command execution.
- Default to denying payload disclosure through MCP.
- Make revocation and cache clearing available without editing pipeline files.

## 17. Testing Strategy

- Plan canonicalization, digest, expiration, and single-use tests.
- Tests proving modified plans require new consent.
- Tests proving MCP cannot edit profiles or access authentication artifacts.
- Broker tests for approve, reject, reduce, cancel, and administrator-required
  outcomes.
- Authentication redaction and protected-cache tests.
- Connector tests for endpoint, tenant, scope, operation, and redirect binding.
- Tests proving execution permission does not imply MCP disclosure.
- Tests proving connection tests do not return records.
- Host reload atomicity and running-plan snapshot tests.
- Revocation and dependent-pipeline binding-failure tests.
- Client interoperability tests using only standard MCP capabilities.

## 18. Open Questions

1. Which connector packages ship with the first public release?
2. Which Microsoft Entra flows and application-registration model are supported?
3. What local consent-broker user experience is provided on each operating
   system?
4. Which fields can a user reduce without regenerating the complete plan?
5. What disclosure classifications, redaction rules, and destination types are
   normative?
6. Does v1 support atomic live reload, or require an MCP host restart after
   approval?
7. Which audit format and retention controls are required?
