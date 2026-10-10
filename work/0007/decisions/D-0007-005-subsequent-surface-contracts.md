---
id: D-0007-005
kind: decision
title: Minimal subsequent Service, CLI and MCP contracts
status: open
spec: SPEC-0007
requirements: [R-0007-344, R-0007-368, R-0007-369, R-0007-399, R-0007-400, R-0007-401, R-0007-402, R-0007-403]
depends_on: [D-0007-004, D-0007-006]
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-005: Subsequent Surface Contracts

## Objective

Resolve the subsequent-surface contracts in R-0007-344 and the remainder of
Section 23 question 2, building on the first retrieval slice and conclusions.

## Scope and exclusions

Smallest versioned authoring/validation/explanation and execution surfaces needed
by later slices. Do not front-load unrelated authentication or release detail.
Invocation-skill and companion-specific protocols remain under their own owners.
Versioned catalog membership is host/Service configuration over exact operation
references, not operation declaration or manifest metadata.

## Questions to resolve

Which public use cases, exact CLI commands, MCP tool requests/results, structured
errors, and execution mappings are required next? Which surfaces are explicitly
deferred, and what capability advertisements distinguish unavailable behavior?
How do Service/catalog versions include, omit, or replace exact operation
contracts without changing their declarations?

## Acceptance criteria

- [ ] Exact minimal contracts and version identities are recorded.
- [ ] Authoring and execution operations remain separate.
- [ ] All four conclusions and independent disclosure/permission decisions survive
  Service and transport mappings.
- [ ] Deferred contracts are explicit; no placeholder protocol is advertised.
- [ ] Required adapter, compatibility, failure, cancellation, and conformance
  cases are specified.
- [ ] Catalog-version membership and policy-filtered projection satisfy
  R-0007-399 without duplicating operation implementations.
- [ ] Checks pass and exact-scope human approval is recorded.

## Resolution

Unresolved. Split into narrower decisions only if review shows this scope cannot
be closed coherently; preserve this item's identity and coverage.

## Validation and review

No later protocol or execution surface is approved by this extraction.
