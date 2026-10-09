---
id: D-0007-006
kind: decision
title: Stage-aware non-executing validation conclusions
status: open
spec: SPEC-0007
requirements: [R-0007-344, R-0007-299, R-0007-300, R-0007-301, R-0007-352, R-0007-353]
depends_on: []
artifacts: [specs/0007-portable-pipeline-definitions-and-binding.md]
---

# D-0007-006: Non-Executing Conclusions

## Objective

Specify how early responses distinguish document validity, host bindability,
policy eligibility, and invocation-specific execution permission.

## Scope and exclusions

Stage-aware conclusions and unavailable/unknown results for non-executing slices.
Existing four-conclusion semantics remain authoritative. No execution grant,
canonical pre-normalization identity, or success-shaped unavailable conclusion.

## Questions to resolve

Which conclusions can retrieval, inert parsing, full validation, and explanation
actually establish? How are unavailable conclusions represented and mapped?
How are bind-time and invocation-time results distinguished?

## Acceptance criteria

- [ ] Each early slice has explicit supported and unavailable conclusions.
- [ ] Results cannot imply execution or payload-disclosure authority.
- [ ] Document validity is not confused with normalized identity or bindability.
- [ ] Service/CLI/MCP mappings and negative conformance cases are defined.
- [ ] Related diagnostics and first-slice contracts agree; checks and review pass.

## Resolution

Unresolved. This decision can proceed independently of exact API naming.

## Validation and review

Extracted from the former R-0007-344 conclusion checkpoint, now retained as a
declarative contract requirement; no new semantics selected.
