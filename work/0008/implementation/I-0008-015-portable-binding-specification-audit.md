---
id: I-0008-015
kind: implementation
granularity: slice
change_kind: editorial
title: Audit portable binding specification examples
status: complete
spec: SPEC-0008
requirements:
  - R-0000-007
  - R-0008-005
depends_on:
  - D-0008-003
artifacts:
  - specs/0007-portable-pipeline-definitions-and-binding.md
---

# I-0008-015: Audit Portable Binding Specification Examples

## Objective and coverage

Inventory normative and non-normative content throughout SPEC-0007. Record
the disposition of each example, rationale block, and default that could alter
portable behavior or conformance. Apply R-0008-005 and preserve R-0000-007's
language-neutral boundary. Review links to schemas and conformance material
only to confirm that their ownership and normative status are represented
consistently; those artifacts are not prose examples and are not reclassified
or edited by this slice.

This slice does not assess other numbered specifications, implementation
code, or checker behavior. It does not authorize a behavioral change. If an
audit finding requires a new or changed behavior, stop and raise it for a
separate specification decision and readiness assessment.

## Entry gates

- [ ] D-0008-003 is complete.
- [ ] This exact slice plan has explicit approval.
- [ ] Current implementation readiness is approved for SPEC-0007 if it is
  proposed for editing; planning-readiness for I-0008-002 is insufficient.
- [ ] The audited source snapshot and the aggregate I-0008-002 scope remain
  current.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Modify, only if required for R-0008-005 editorial classification | `specs/0007-portable-pipeline-definitions-and-binding.md` | Audit portable definition and binding requirements, defaults, and examples | Not applicable | Not applicable |

Record the complete inventory, disposition, proposed edits, fingerprints,
reverse-impact references, and validation results in this item's delivery
evidence. Schemas, vectors, profiles, conformance tools, and their README
artifacts remain under their existing owners and are not modified.

## Design and integration

Treat examples inside requirement blocks as normative. A move or rewording is
permitted only when review establishes that it preserves existing required
behavior and conformance expectations; update fingerprints and review all
references for any changed block. Examples outside requirement blocks must be
explicitly illustrative and must not add, relax, or contradict a requirement.
Do not make portable definitions or conformance semantics depend on CLR
implementation details. Any material behavior change is excluded and requires
a separately approved specification amendment.

## Tests and validation

- Run `/spec-trace-check` on the exact changed snapshot; require a passing
  requirement-identity, fingerprint, classification, and reverse-impact
  review.
- Review relative links affected by changed content and `git diff --check`.
- No product build or unit tests apply to a documentation-only editorial
  change. If a behavior change is proposed, stop this slice rather than
  treating product tests as authorization.

## Exit criteria

- [ ] Every example, rationale block, and potentially behavior-affecting
  default in SPEC-0007 has a recorded disposition.
- [ ] Schema and conformance-artifact ownership is preserved.
- [ ] No unapproved behavior or conformance change is included.
- [ ] Changed requirement fingerprints and reverse-impact references are
  verified, if applicable.
- [ ] Required validation passes and explicit delivery review covers the exact
  output snapshot.

## Plan approval

Explicitly approved in this session on 2026-10-14 for this exact slice,
manifest, dependencies, entry gates, tests, validation, and exclusions. This
approval authorizes execution of the reviewed plan only; it does not change
this item's status, satisfy its entry gates, approve delivery, or authorize a
behavioral or conformance change.

Material SHA-256: `a633715c795a26662eab7e9d45cc3f423a1f328639f4ecfb55303c17089c4c51`.

Material input snapshot:

| Path | Basis | SHA-256 |
| --- | --- | --- |
| `work/0008/readiness/portable-binding-specification-audit-implementation.md` | material | `fbc321553f64dfb0746fd9d77ba56fa1fc4a5a090446ac80c0fc4c9db5aeb0a2` |
| `work/0008/plan.md` | bytes | `529dc639f6b64614f288aa457e78de8005da7fd6af311eeeaead46e023863a98` |
| `SPEC.md` | bytes | `998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | bytes | `30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | bytes | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | bytes | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | bytes | `83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b` |

The prior plan approval applied to its earlier reviewed input snapshot and is
superseded by this approval. This approval does not satisfy dependencies or
entry gates, approve delivery, publish a contract, or claim whole-v1
conformance.

## Delivery evidence and review

### Audit inventory and dispositions

The audit covered the complete SPEC-0007 document, including its normative
requirement blocks, summaries, goals, non-goals, terminology, rationale,
alternatives, open questions, prose, tables, code fences, and potentially
behavior-affecting defaults.

| Content | Disposition |
| --- | --- |
| Sections 1–4, Section 21 introductions, Section 22 alternatives, and Section 23 open-question text | Retained outside requirement blocks as non-normative summary, goals, non-goals, terminology, rationale, alternatives, or future direction. Section 23 continues to state that no question remains for the initial Service, CLI, or MCP contracts. |
| Fenced lifecycle, proof, schema, grammar, identity, API, and CLI forms in R-0007-003, R-0007-026, R-0007-031, R-0007-035, R-0007-176, R-0007-193, R-0007-277, R-0007-404, R-0007-407, and R-0007-418 | Retained as direct normative representations of their surrounding requirements, not illustrative examples. |
| Fenced exact-shape and usage examples in R-0007-013, R-0007-015 (five forms), R-0007-017, R-0007-019, R-0007-022, R-0007-024, R-0007-030, R-0007-034, R-0007-038, R-0007-042, R-0007-057 (four forms), R-0007-206, R-0007-235, R-0007-241, R-0007-252, R-0007-257, R-0007-264, R-0007-265, and R-0007-268 | Retained within requirement blocks and explicitly labeled **Normative example(s)**; their existing required syntax and meaning are unchanged. |
| Pipeline JSON in R-0007-005, future mapping-site schema in R-0007-142, and diagnostic JSON in R-0007-302 | Each is now under a separate illustrative heading, outside its requirement block, and labeled **Illustrative example**. The requirement text retains the exact required document members, schema-dispatch rule, and diagnostic fields. |
| Inline examples in R-0007-027, R-0007-059, R-0007-061, R-0007-066, R-0007-110, R-0007-146, R-0007-159, R-0007-194, R-0007-218, R-0007-223, R-0007-228, R-0007-372, R-0007-398, and R-0007-421 | Retained as normative and explicitly labeled **Normative example(s)**, preserving the stated branch-normalization, schema/type, failure, comparison, duration, namespace, capability, effect, generator, and error-token behavior. |
| Numeric examples in Section 8.12 | Retained outside requirement blocks and explicitly labeled **Illustrative examples**; the normative numeric rules remain in their requirement blocks. |
| Version-identity cells formerly in the R-0007-290 compatibility table | Compatibility rules remain normative in R-0007-290. Identity samples are separated into an **Illustrative version identities** subsection and cannot mandate a generator-package or authoring-runtime API name. |
| Other occurrences of schema `examples` annotations and descriptor or imported examples as untrusted metadata | Retained as normative schema/security behavior, not reclassified as example documents. |
| Schema, conformance-vector, profile, and README ownership references | Reviewed and retained under existing owners; no schema, vector, profile, or README artifact was modified. |

All 39 fenced blocks in the input snapshot were inventoried. The three formerly
illustrative fenced samples in R-0007-005, R-0007-142, and R-0007-302 are now
outside requirement blocks. The remaining examples are explicitly normative;
the other fenced blocks express normative lifecycle order, proof notation,
fixed schemas, grammar, or contract syntax.

| Potentially behavior-affecting default or omission rule | Disposition |
| --- | --- |
| R-0007-014, R-0007-023, R-0007-158 through R-0007-160, and R-0007-359: omitted operation configuration, `default`, explicit `null`, and canonicalization | Preserved: omission first becomes an empty object; optional defaults are validated and materialized before hashing/binding; required properties remain explicit; `null` remains distinct; contract defaults remain immutable. |
| R-0007-116 and R-0007-117: mapping limits | Preserved all v1 defaults and fixed ceilings. Explicit higher values remain host-capacity requirements; hosts must not silently clamp them. |
| R-0007-077, R-0007-342, and R-0007-375: string/regex comparison and overlap | Preserved exact string comparison when omitted and non-overlapping regex iteration as the default. |
| R-0007-135: mapping-language selection | Preserved exact per-site selection; no pipeline default, inheritance, alias, range, or implicit latest. |
| R-0007-153 and R-0007-154: JSON Schema `default` annotation | Preserved Qhapaq-specific operation-configuration normalization as the only executable meaning assigned to this annotation. |
| R-0007-201 and R-0007-240: URI and unsafe-retry behavior | Preserved no URI default-port insertion and the default policy denial for unsafe retries. |
| R-0007-252 and R-0007-335: .NET source/descriptor association | Preserved exact same-directory/basename matching as the implementation-specific default; it does not define portable pipeline behavior. |
| R-0007-257 and R-0007-404: optional .NET cancellation arguments | Classified `CancellationToken = default` as .NET API signature detail, not a portable semantic default. |
| R-0007-303: diagnostics | Preserved omission of payloads, secrets, and protected host configuration by default. |
| R-0007-407 and R-0007-418: CLI output mode | Preserved `text` as the default; structured machine output remains explicitly selected. |
| R-0007-351: MCP payload disclosure | Preserved default-denied disclosure, independent of execution permission. |

No separate `Rationale` heading or block was found. The alternatives in
Section 22 and explanatory text outside requirement blocks remain
non-normative. Repeated references to defaults in conformance and acceptance
requirements were reviewed against their owning normative rules; no default was
added, removed, or changed.

### Actual files and requirement fingerprints

Edited `specs/0007-portable-pipeline-definitions-and-binding.md`. The two plan
source records were refreshed as workflow reconciliation only; their material
scope, item coverage, approvals, and dependencies remain unchanged.

| Requirement | Previous fingerprint | Current fingerprint |
| --- | --- | --- |
| R-0007-005 | `9a7176` | `e6f44b` |
| R-0007-013 | `328b52` | `757b78` |
| R-0007-015 | `51a3a1` | `abeec3` |
| R-0007-017 | `39e0a2` | `55f395` |
| R-0007-019 | `468ba3` | `5bca05` |
| R-0007-022 | `a61352` | `b3ec0d` |
| R-0007-024 | `c8bd03` | `f14316` |
| R-0007-027 | `c39a29` | `d66354` |
| R-0007-030 | `18deae` | `2ac47f` |
| R-0007-034 | `e03483` | `a937be` |
| R-0007-038 | `499b95` | `1e5672` |
| R-0007-042 | `b14d52` | `64229f` |
| R-0007-057 | `4f430e` | `9cc5eb` |
| R-0007-059 | `c0b1f5` | `a4dc3a` |
| R-0007-061 | `08ef9d` | `f6c788` |
| R-0007-066 | `7cee13` | `98dac7` |
| R-0007-110 | `04caaf` | `86a5e4` |
| R-0007-142 | `57e6bd` | `f63327` |
| R-0007-146 | `0a789a` | `5f3103` |
| R-0007-159 | `da70f8` | `4d7513` |
| R-0007-194 | `c7fb49` | `d57e41` |
| R-0007-206 | `31ec77` | `f2cc73` |
| R-0007-218 | `01d1f1` | `8e9762` |
| R-0007-223 | `708666` | `f93684` |
| R-0007-228 | `255d14` | `ac37ec` |
| R-0007-235 | `a7483a` | `2cd9a3` |
| R-0007-241 | `af51c1` | `a8e86e` |
| R-0007-252 | `32845a` | `fa826f` |
| R-0007-257 | `32509e` | `28f216` |
| R-0007-264 | `33ec04` | `672ebd` |
| R-0007-265 | `a31066` | `4267bd` |
| R-0007-268 | `41a3d4` | `2bb163` |
| R-0007-290 | `cd342e` | `1c9934` |
| R-0007-302 | `564c1d` | `f3bc7e` |
| R-0007-372 | `8a0e6b` | `f60ccd` |
| R-0007-398 | `d22ab5` | `016196` |
| R-0007-421 | `6159da` | `941ef5` |

Reverse-impact review found no product-code or test references to these
fingerprints. The old fingerprints occur only in `Spec:` trailers embedded in
the completed D-0007-003 and D-0007-005 decision records; those trailers remain
historical evidence for the decisions' original snapshots and were not
rewritten. No schema or conformance artifact ownership was affected.

### Input and output snapshots

The approved implementation-readiness and plan inputs were current and
explicitly approved before execution. The target specification input hash was
`30945dafc0dce8b518beac8230af5e8a917257cbd42f0210d7e294dcae67c13c`.
After the audit and the required source-record reconciliation, the exact
working-copy snapshots are:

| Path | Output SHA-256 | Material SHA-256 |
| --- | --- | --- |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `5cff3784f6bfc9ddb64b6bcf3f15a14d09c50d97bb25e7702ff65e01496f0d24` | Not applicable |
| `work/0007/plan.md` | `6bbc9b0937c7c167b754196c510a6e6df11067532b9eedc44232ad3b3a4f070f` | `26e4be848f8bd3bfe7c6f61e97146d811c8675e51506396837b14676077375ec` |
| `work/0008/plan.md` | `97fa78b1f76db762075afcadca107b850c52c1e13523fb8bc17e436305de1e0b` | `6a79348b7686002e8a03592ef3a76b50e737a5cdb03e5e6f24dee8a0485a9890` |

The refreshed plan source records retain baseline revision
`1267f9c0475eda05ef1f118437ef64a4a2f2a859` and hash the exact reviewed
working-copy bytes. Their other sources and material scope are unchanged.
Readiness and approval evidence remain limited to their approved input
snapshots; no approval is renewed here.

### Validation

- `/spec-trace-check`: **PASS**, classified as editorial. The shared facts
  script reported no mechanical errors, malformed/removed identifiers, code
  references, or test references. The seven old fingerprints in completed
  D-0007-003 and D-0007-005 `Spec:` trailers are historical decision evidence
  for their recorded snapshots, not current source references; they remain
  unchanged.
- `python .agents/scripts/work_hashes.py verify work/0007/plan.md work/0008/plan.md`:
  passed; all recorded sources are current.
- `git diff --check`: passed on the final working tree.
- No relative links were changed or removed. No schema, conformance, profile,
  implementation, or test files were changed. Product build and unit tests do
  not apply to this documentation-only editorial slice.

Proposed commit trailers for the specification change:

```text
Change-Kind: editorial
Spec: R-0007-005@e6f44b, R-0007-013@757b78, R-0007-015@abeec3,
R-0007-017@55f395, R-0007-019@5bca05, R-0007-022@b3ec0d,
R-0007-024@f14316, R-0007-027@d66354, R-0007-030@2ac47f,
R-0007-034@a937be, R-0007-038@1e5672, R-0007-042@64229f,
R-0007-057@9cc5eb, R-0007-059@a4dc3a, R-0007-061@f6c788,
R-0007-066@98dac7, R-0007-110@86a5e4, R-0007-142@f63327,
R-0007-146@5f3103, R-0007-159@4d7513, R-0007-194@d57e41,
R-0007-206@f2cc73, R-0007-218@8e9762, R-0007-223@f93684,
R-0007-228@ac37ec, R-0007-235@2cd9a3, R-0007-241@a8e86e,
R-0007-252@fa826f, R-0007-257@28f216, R-0007-264@672ebd,
R-0007-265@4267bd, R-0007-268@2bb163, R-0007-290@1c9934,
R-0007-302@f3bc7e, R-0007-372@f60ccd, R-0007-398@016196,
R-0007-421@941ef5
```

### Deviations and delivery review

No requirement meaning, behavior, conformance expectation, ownership, or
implementation scope changed. The plan source refreshes are required
workflow-only reconciliation, not a material scope deviation. The runbook
remains a generated view and is to be refreshed after this selected action.

I-0008-015 is complete for the exact editorial outcome reviewed above. Approval
authorizes delivery of this outcome only; it does not publish a component
contract or claim whole-v1 conformance.

### Delivery approval

Explicitly approved in this session on 2026-10-14 for the exact I-0008-015
editorial outcome, including the SPEC-0007 example classifications and the
workflow-only source reconciliations in the two plans. The approval excludes
behavior or conformance changes, implementation and tests, schemas, vectors,
profiles, and their README ownership.

Approved material SHA-256: `a633715c795a26662eab7e9d45cc3f423a1f328639f4ecfb55303c17089c4c51` (`work/0008/implementation/I-0008-015-portable-binding-specification-audit.md`).

| Path | SHA-256 |
| --- | --- |
| `work/0008/readiness/portable-binding-specification-audit-implementation.md` | `59e4ac22054d19ecdb0f0c86704731d1089b7bb974df2b05c5cbc545471f48f0` |
| `specs/0007-portable-pipeline-definitions-and-binding.md` | `5cff3784f6bfc9ddb64b6bcf3f15a14d09c50d97bb25e7702ff65e01496f0d24` |
| `work/0007/plan.md` | `6bbc9b0937c7c167b754196c510a6e6df11067532b9eedc44232ad3b3a4f070f` |
| `work/0008/plan.md` | `97fa78b1f76db762075afcadca107b850c52c1e13523fb8bc17e436305de1e0b` |
