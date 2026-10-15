---
id: I-0008-016
kind: implementation
granularity: slice
change_kind: editorial
title: Audit .NET contract and traceability boundaries
status: ready-for-review
spec: SPEC-0008
requirements:
  - R-0000-007
  - R-0008-004
  - R-0008-005
  - R-0008-016
  - R-0008-017
  - R-0008-018
depends_on:
  - D-0008-003
  - D-0008-008
artifacts:
  - specs/0006-dotnet-layered-architecture.md
  - specs/0008-multi-language-conformance-and-repository-organization.md
  - docs/development/coding-conventions.md
  - docs/development/conventions/specifications.md
---

# I-0008-016: Audit .NET Contract and Traceability Boundaries

## Objective and coverage

Inventory normative and non-normative content in SPEC-0006 and SPEC-0008,
including examples and defaults that could affect language-specific contracts,
traceability, or conformance. Audit the related common and specification
authoring guidance for consistency with R-0008-005, R-0000-007, and
R-0008-016 through R-0008-018. Record each relevant example's disposition
without moving checker ownership, language-native placement, or extractor
behavior out of D-0008-008 and its owned delivery.

This slice does not re-audit other numbered specifications, change checker
architecture, register an extractor, assess whole-v1 conformance, or authorize
a behavioral change. If an audit finding requires a new or changed behavior
or architecture, stop and raise it for a separate specification or ADR
decision and readiness assessment.

## Entry gates

- [x] D-0008-003 and D-0008-008 are complete.
- [x] This exact slice plan has explicit approval.
- [x] Current implementation readiness is approved for each specification
  file proposed for editing; planning-readiness for I-0008-002 is insufficient.
- [x] The audited source snapshots and the aggregate I-0008-002 scope remain
  current.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Modify, only if required for R-0008-005 editorial classification | `specs/0006-dotnet-layered-architecture.md` | Audit .NET-specific contract boundaries and examples | Not applicable | Not applicable |
| Modify, only if required for R-0008-005 editorial classification | `specs/0008-multi-language-conformance-and-repository-organization.md` | Audit language-contract and traceability requirement examples | Not applicable | Not applicable |
| Modify, only if required for editorial consistency | `docs/development/coding-conventions.md` | Audit common traceability boundary guidance | Not applicable | Not applicable |
| Modify, only if required for editorial consistency | `docs/development/conventions/specifications.md` | Audit specification-authoring and fingerprint boundary guidance | Not applicable | Not applicable |

Record the complete inventory, disposition, proposed edits, fingerprints,
reverse-impact references, and validation results in this item's delivery
evidence. ADR-0003, ADR-0004, D-0008-008, and path-specific instruction files
are read-only authorities for this slice. An ownership or architecture change
requires a separately approved decision.

## Design and integration

Keep .NET-specific contracts explicitly scoped and portable semantics
language-neutral. Treat examples inside requirement blocks as normative. A
move or rewording is permitted only when review establishes that it preserves
required behavior and conformance expectations; update fingerprints and review
all references for any changed block. Do not duplicate or alter language-native
marker placement, checker ownership, extractor registration, or support claims.
Any material behavior or architecture change is excluded and requires a
separately approved decision.

## Tests and validation

- Run `/spec-trace-check` on the exact changed snapshot; require a passing
  requirement-identity, fingerprint, classification, and reverse-impact
  review.
- Review relative links affected by changed content and `git diff --check`.
- No product build or unit tests apply to a documentation-only editorial
  change. If a behavior change is proposed, stop this slice rather than
  treating product tests as authorization.

## Exit criteria

- [x] Every example, rationale block, and potentially behavior-affecting
  default in the assigned specification and guidance files has a recorded
  disposition.
- [x] Portable behavior, .NET contract, and traceability ownership boundaries
  remain consistent.
- [x] No unapproved behavior, conformance, or architecture change is included.
- [x] Changed requirement fingerprints and reverse-impact references are
  verified, if applicable.
- [ ] Required validation passes and explicit delivery review covers the exact
  output snapshot.

## Plan approval

Approved explicitly in this session on 2026-10-14 for the exact audit scope,
conditional four-file manifest, dependencies, exclusions, and entry gates
recorded above.

- Material SHA-256: `2060cb93df653a8ba3d042366b97e7c3d436c8a04266af97e6de709acbafd3da`.
- Approved readiness scope:
  `language-contract-and-traceability-audit-implementation`.

Material input snapshot:

| Path | Basis | SHA-256 |
| --- | --- | --- |
| `work/0008/plan.md` | bytes | `97fa78b1f76db762075afcadca107b850c52c1e13523fb8bc17e436305de1e0b` |
| `work/0008/readiness/language-contract-and-traceability-audit-implementation.md` | material | `cb0017c4a6ee5c380ef243638e81c33ed97d985314b419d1902ad9efaecdab24` |
| `SPEC.md` | bytes | `998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6` |
| `specs/0006-dotnet-layered-architecture.md` | bytes | `399e0083473b9adb30375c6572e53c1c04249606e46f7aab3fd4eb8ed289232e` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | bytes | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `docs/development/coding-conventions.md` | bytes | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| `docs/development/conventions/specifications.md` | bytes | `9ca7343adff645671b738b1002363a79f306995531d8e5210695b1745f70155a` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | bytes | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/decisions/D-0008-008-language-native-traceability.md` | bytes | `a12c67a643de4a82cb75ecaa5c5130d31845ba2016faad2411dbf019ee93c8c5` |

Approval authorizes execution only of this exact reviewed plan snapshot. It does
not satisfy pending execution entry gates, change the item status, authorize
behavior or architecture changes, or approve delivery.

## Delivery evidence and review

### Audit inventory and dispositions

- `specs/0006-dotnet-layered-architecture.md`
  - The Entry Points CLI/MCP mention is an illustrative overview example, not
    a layer requirement.
  - The use-case list in R-0006-003 remains a normative example of complete
    Service use cases.
  - `Qhapaq.Service.V2` in R-0006-004 remains a normative example of a new
    side-by-side contract namespace and implementation assembly; V1 behavior
    remains unchanged.
  - Business as a runtime reference in R-0006-041 remains a normative example
    of the shared assembly boundary.
  - Project trees, call graphs, ownership maps, and the component diagram are
    direct architectural representations, not illustrative examples; their
    authority is unchanged.
  - No behavior-affecting default was found.
- `specs/0008-multi-language-conformance-and-repository-organization.md`
  - The website, editor integration, and development-tool mentions in the
    purpose; Visual Studio extension in artifact terminology; operation
    family and distinct operation catalogs in the capability discussion; and
    shared test-case families in intended uses are illustrative examples.
  - The unqualified conformance-claim and missing-cancellation cases in
    R-0008-007 are normative examples and remain conformance expectations.
  - The language-specific C# mapping example, including
    `CancellationToken = default`, is illustrative and does not define a
    portable API default.
  - Exact `spec:` and `spec-waive:` payloads in R-0008-016 and R-0008-018 are
    normative syntax, not examples. Other code-like structures are likewise
    normative representations, not illustrative examples.
  - The `Default` level in R-0008-004 is engineering policy, not product
    behavior. No other behavior-affecting defaults were found.
- `docs/development/coding-conventions.md` was audited and left unchanged.
  Its trailer, reference, and waiver snippets illustrate engineering-policy
  grammar; its `Default` level and “by default” rules remain repository
  engineering/security guidance, not language-specific product defaults.
- `docs/development/conventions/specifications.md` now links R-0008-005 and
  directs authors to use the exact **Illustrative example** and
  **Normative example** labels on the corresponding sides of requirement
  boundaries. Existing requirement-identifier and component-identifier
  examples remain structural guidance.
- The read-only .NET traceability conventions, ADR-0003, ADR-0004, D-0008-003,
  and D-0008-008 were checked. Their native C# placements, checker/extractor
  ownership, and portable payload boundaries remain unchanged.

### Fingerprints and reverse impact

The requirement edits are editorial rewordings; no requirement identity or
meaning changed.

| Requirement | Previous fingerprint | Current fingerprint |
| --- | --- | --- |
| R-0006-003 | `fe47d8` | `5af0ae` |
| R-0006-004 | `555771` | `884ee4` |
| R-0006-041 | `a98508` | `2187dc` |
| R-0008-007 | `8b507a` | `966a6a` |

The repository-wide reverse-impact search found no stale code or test
references. It found two old fingerprints in completed Markdown decision
validation evidence: D-0008-004 retains R-0008-007@8b507a, and D-0008-015
retains R-0006-041@a98508. These are historical validation snapshots, not
active code/test markers, so they remain unchanged.

### Snapshot and validation

The approved plan and readiness snapshots were current before execution. Their
approved evidence is preserved without refreshing it to imply review of the
post-edit sources. Current output snapshots:

| Path | SHA-256 |
| --- | --- |
| `specs/0006-dotnet-layered-architecture.md` | `7e8b252a96cbfef18eaa92d7d742234a626dfbf2758dbbdd63feac055925f58a` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `51566da6fc6521022146426661004112ee133e3600656a68a59c71e4f040c779` |
| `docs/development/conventions/specifications.md` | `cedd8481133460d1a2f8ad1ed5d7c02d1981d83c837cda88b13c18d1b7fd19f8` |
| `docs/development/coding-conventions.md` (unchanged) | `436abc18b023af448e8c8f45a117bd1b643067ddb2833642846111ed9c60b94a` |
| This item's current material hash | `798f810a11b98d61cea36ed0ceb2b07885e1d2f42c8f3891596bdd2df5fb4fd8` |

The Plan approval section retains the approved pre-execution material hash
`2060cb93df653a8ba3d042366b97e7c3d436c8a04266af97e6de709acbafd3da`.
`work_hashes.py verify` reports the plan stale for the edited SPEC-0006,
SPEC-0008, and specification-authoring conventions. It reports readiness
stale for those edited sources and this item's full-content snapshot, whose
status and delivery evidence changed; this item's material scope hash remains
the approved value above. These records remain at their approved baseline;
reconciliation and any resulting reassessment are left to the workflow gates
after this exact output is reviewed.

The new relative link to R-0008-005 resolves to the intended requirement and
heading. `git diff --check` passed. No build or unit tests apply to this
documentation-only editorial change.

### Specification trace review

`/spec-trace-check` ran with semantic review enabled. The changed
specifications contain no added, removed, renumbered, or malformed
requirement identifiers. The four changed blocks preserve their meaning.
Reverse impact found only the historical Markdown fingerprints listed above;
no active code or test references are stale. No code or tests changed, and no
waivers were added or changed.

The review checked R-0006-003, R-0006-004, R-0006-041, R-0008-005, and
R-0008-007. The normative and illustrative labels follow R-0008-005; the
.NET contract examples preserve their original boundaries; and R-0008-007's
claim and cancellation examples preserve the existing conformance rules.
No behavior, ownership, checker support, or conformance claim was added.

Warning: SPEC-0006 R-0006-004 names the implementation namespace
`Qhapaq.Service.V2` (line 94), and SPEC-0008 retains an illustrative
language-specific C# example (lines 321-331). These implementation-specific
details are explicitly scoped examples permitted by R-0008-005; this audit
only clarifies their normative classification and does not broaden them.

Result: `PASS with warnings`; no errors or new waivers.

Proposed commit trailers:

```text
Change-Kind: editorial
Spec: R-0006-003@5af0ae, R-0006-004@884ee4, R-0006-041@2187dc, R-0008-005@107883, R-0008-007@966a6a
```
