---
id: I-0008-013
kind: implementation
granularity: slice
change_kind: editorial
title: Audit portable core requirements and examples
status: complete
spec: SPEC-0008
requirements:
  - R-0000-007
  - R-0001-011
  - R-0001-052
  - R-0002-017
  - R-0008-005
depends_on:
  - D-0008-003
artifacts:
  - SPEC.md
  - specs/0001-core-pipeline-model.md
  - specs/0002-operation-catalogs-and-host-configuration.md
---

# I-0008-013: Audit Portable Core Requirements and Examples

## Objective and coverage

Inventory normative and non-normative content in `SPEC.md` and SPEC-0001 and
SPEC-0002. Record the disposition of each example, rationale block, and
default that could alter portable behavior or conformance. In particular,
assess R-0001-011, R-0001-052, and R-0002-017 without presuming that moving or
relabeling their examples preserves meaning. Keep portable semantics
language-neutral under R-0000-007 and apply R-0008-005.

This slice does not assess other numbered specifications, schemas, conformance
vectors, implementation code, or checker behavior. It does not authorize a
behavioral change. If an audit finding requires a new or changed behavior,
stop and raise it for a separate specification decision and readiness
assessment.

## Entry gates

- [ ] D-0008-003 is complete.
- [ ] This exact slice plan has explicit approval.
- [ ] Current implementation readiness is approved for every specification
  file proposed for editing; planning-readiness for I-0008-002 is insufficient.
- [ ] The audited source snapshots and the aggregate I-0008-002 scope remain
  current.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Modify, only if required for R-0008-005 editorial classification | `SPEC.md` | Audit and clarify portable platform requirements and examples | Not applicable | Not applicable |
| Modify, only if required for R-0008-005 editorial classification | `specs/0001-core-pipeline-model.md` | Audit core pipeline requirements and examples | Not applicable | Not applicable |
| Modify, only if required for R-0008-005 editorial classification | `specs/0002-operation-catalogs-and-host-configuration.md` | Audit catalog and host-configuration requirements and examples | Not applicable | Not applicable |

Record the complete inventory, disposition, proposed edits, fingerprints,
reverse-impact references, and validation results in this item's delivery
evidence. No separate worksheet or production artifact is created.

## Design and integration

Treat examples inside requirement blocks as normative. A move or rewording is
permitted only when review establishes that it preserves existing required
behavior and conformance expectations; update fingerprints and review all
references for any changed block. Examples outside requirement blocks must be
explicitly illustrative and must not add, relax, or contradict a requirement.
Do not transfer implementation-specific contracts into portable requirements.
Any material behavior change is excluded and requires a separately approved
specification amendment.

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
  default in the assigned files has a recorded disposition.
- [ ] The named candidate requirements have explicit evidence-based
  classifications, whether or not edits are warranted.
- [ ] No unapproved behavior or conformance change is included.
- [ ] Changed requirement fingerprints and reverse-impact references are
  verified, if applicable.
- [ ] Required validation passes and explicit delivery review covers the exact
  output snapshot.

## Plan approval

The 2026-10-13 approval was for an earlier full-byte input snapshot and is
superseded for execution by the reapproval below. Its original approval record
is preserved in the preceding Git revision.

Explicitly reapproved in this session on 2026-10-14 for the exact I-0008-013
material snapshot, manifest, dependencies, entry gates, tests, validation, and
exclusions above. This approval authorizes execution of the reviewed plan only;
it does not change the item's status, satisfy entry gates, approve delivery, or
authorize a behavioral or conformance change.

Material SHA-256: `9a4bba8d11db0377d23ddd7b0c74f6e5b65168ef5aca68d57e236b1a1e7b8ab7`.

Full-byte SHA-256 hashes of the reapproved material input snapshot:

| Path | SHA-256 |
| --- | --- |
| `SPEC.md` | `fe46aa58a9ca00cd962654f98fecdc1b068dbbc4d6577567019695b360b1012e` |
| `specs/0001-core-pipeline-model.md` | `38c3bcd720a1f481bebffc3fab25724d1450ffdca5cfbbda49e6fdaa109baf2e` |
| `specs/0002-operation-catalogs-and-host-configuration.md` | `c6b98dc1ee7c8e65f28aab8c3bdc6f1b8e71401660499b4ff28d6be664209fca` |
| `specs/0008-multi-language-conformance-and-repository-organization.md` | `26df535f12c2adfcdabb5016c8474ae8584da210dd53d7c144990d687d770926` |
| `work/0008/decisions/D-0008-003-normative-content-labeling.md` | `4675896d3619504d0c28e38fe73589584ba979aa609fd2981ee8ce05065b8801` |
| `work/0008/implementation/I-0008-002-requirement-example-audit.md` | `83185977d95a5aa9ab450312ead1aad4cc4123b6e10d29ba31b28dfb2bec5d2b` |
| `work/0008/plan.md` | `e54cdcc250aa7a680b74c81c2d2b8c97483feb933e6162f90c14ff84e7d2e646` |
| `work/0008/readiness/portable-core-example-audit-implementation.md` | `3f98b929d27b54d8fa1ab7847b45209b7402ddf1c4b23ea0024d1fa2864118e1` |

## Delivery evidence and review

### Audit inventory and dispositions

| Source content | Classification and disposition |
| --- | --- |
| `SPEC.md` .NET `IOperation<TInput, TOutput>` interface | Implementation illustration, not portable authority. Moved before R-0000-002 and labeled **Illustrative example**; R-0000-002 now states only the language-neutral schema mapping. |
| `SPEC.md` target repository tree and `examples/` entries | Normative repository target under R-0000-017, not a runtime pipeline example or default. Retained unchanged. Other mentions of user-facing or executable examples describe repository content or specification-process fields, not concrete product behavior. |
| `SPEC.md` repository goals, principles, decision history, and branch guidance | Goals and process guidance are not portable execution semantics. The payload-disclosure-by-default rule is an accepted product behavior under R-0000-005; secure-by-default and the recommended `main` branch are repository guidance, not pipeline defaults. Retained. |
| `specs/0001-core-pipeline-model.md` .NET interface | Implementation illustration, not portable authority. Moved before R-0001-001 and labeled **Illustrative example**; the portable operation requirement remains unchanged in meaning. |
| `specs/0001-core-pipeline-model.md` composition type signatures and mappings | Normative formal notation in the composition requirements (sequential, parallel, decorator, conditional, try/catch, loop, and collection forms), not illustrative examples. Retained as part of their requirements. |
| R-0001-011 retry/timeout ordering statement | Normative example because it is inside the requirement block and demonstrates semantically significant nesting. Labeled **Normative example**; explicit nesting and the existing ordering distinction are unchanged. |
| SPEC-0001 goals, non-goals, and Alternatives Considered | Non-normative rationale outside requirement blocks. Retained; it does not add portable behavior. |
| SPEC-0001 failure/default and diagnostics statements | Explicit normative rules remain: no success-shaped failure default, cancellation is not retryable by default, and payloads are not recorded by default. R-0001-052 makes exported examples/defaults non-authoritative unless schema semantics say otherwise. The .NET optional-parameter `default` in the illustrative interface is language syntax, not a portable value default. Retained. The package-level “default authoring and execution experience” is scoped to the .NET package boundary, not portable pipeline semantics. |
| SPEC-0002 catalog JSON shape | Illustrative catalog data, not a requirement example: R-0002-014 says the exact normative schema may refine the property names. Moved outside R-0002-013 and labeled **Illustrative example**; catalog prohibitions and the catalog field list remain unchanged. |
| SPEC-0002 host-profile JSON shape | Illustrative field/value selection, not a set of defaults. The normative field inventory remains in R-0002-016. Moved outside that block and labeled **Illustrative example**; R-0002-017 now explicitly says its values do not establish defaults, preserves Windows paths as illustrative, and retains portable path/URI handling. |
| SPEC-0002 profile-selection command forms | Illustrative syntax, not the normative CLI grammar. Moved outside R-0002-018 and labeled **Illustrative example**; the requirement that the host use an explicitly selected profile is unchanged. |
| SPEC-0002 candidate credential-provider list | Unresolved candidate set, not an accepted provider requirement. Moved outside R-0002-023 under an open/non-normative heading; the provider capabilities remain normative and the provider set remains undecided. |
| SPEC-0002 goals, non-goals, and security defaults | Goals/non-goals remain non-normative outside requirement blocks. Normative endpoint selection by default (R-0002-004), named-profile locations (R-0002-019), and secret-reference redaction by default (R-0002-034) remain unchanged. |

### Candidate requirement classifications

| Requirement | Finding |
| --- | --- |
| R-0000-007 | Language neutrality remains the authority; the .NET API sample is explicitly illustrative and no CLR behavior is imported into the portable requirement. Unchanged. |
| R-0001-011 | The retry/timeout ordering sentence is a conformance-relevant normative example, not explanatory prose. Labeled accordingly without changing its stated distinction. |
| R-0001-052 | Explicitly makes exported examples/defaults non-authoritative unless the input schema gives them normative semantics. No example in this block creates an additional default. Unchanged. |
| R-0002-017 | The profile shape is now explicitly illustrative as a whole, and neither its Windows paths nor sample values establish defaults; portable path and URI handling remains required. |
| R-0008-005 | Applied as written: portable requirements stay implementation-neutral; non-normative examples/open options are outside requirement blocks with an illustrative label; the in-block example is labeled normative. Unchanged. |

### Fingerprints and reverse-impact review

| Changed requirement block | Current fingerprint |
| --- | --- |
| R-0000-002 | `bcf15e` |
| R-0001-001 | `899621` |
| R-0001-011 | `66b88c` |
| R-0002-013 | `5bb953` |
| R-0002-016 | `6c0589` |
| R-0002-017 | `26d150` |
| R-0002-018 | `3cda5b` |
| R-0002-023 | `566cfd` |

The shared `trace_facts.py` review found no mechanical errors. Its whole-repository
reverse-impact search found no implementation or test references to the changed
blocks. The only reported old fingerprints are in the approved readiness record,
which records the exact pre-implementation source snapshot and its historical
fingerprints; those approval-evidence values are intentionally preserved rather
than rewritten as if they described this output snapshot. R-0000-007,
R-0001-052, and R-0008-005 were not changed.

No relative links were added, removed, or changed in the edited specification
hunks. The diff review found no affected relative-link target to update.

### Validation

- `python .agents/scripts/trace_facts.py`: no mechanical errors; the eight
  changed blocks above were identified for semantic review.
- `/spec-trace-check`: **PASS with warnings**. Semantic review found no
  behavior or conformance change. The warning is that the specifications name
  .NET implementation details; the interface examples are now explicitly
  illustrative and outside the portable requirement blocks.
- Reverse-impact review: **PASS**. No changed block has an implementation or
  test reference; the approved readiness record retains its historical
  pre-implementation fingerprints.
- `git diff --check`: **PASS**. Git emitted only its existing CRLF-to-LF
  normalization notices for edited files; no whitespace errors were reported.
- Relative-link impact review: **PASS**; no link text or destination changed.
- Product build and unit tests: **not applicable** to this documentation-only
  change; not run.

### Exact input and output snapshots

The approved input snapshot is the full-byte hash table in Plan approval above.
The output snapshot is the exact full-byte file hash table recorded under
Delivery approval below.

The approved plan material remains `9a4bba8d11db0377d23ddd7b0c74f6e5b65168ef5aca68d57e236b1a1e7b8ab7`.
The I-0008-013 material hash is unchanged at that value; lifecycle status and
this delivery-evidence section do not alter the approved scope.

Proposed commit trailers:

```text
Change-Kind: editorial
Spec: R-0000-002@bcf15e, R-0001-001@899621, R-0001-011@66b88c, R-0002-013@5bb953, R-0002-016@6c0589, R-0002-017@26d150, R-0002-018@3cda5b, R-0002-023@566cfd
```

### Delivery approval

The user explicitly approved this exact I-0008-013 material snapshot in this
session on 2026-10-14. Approval covers the scope, exclusions, outputs,
acceptance criteria, and validation recorded above. It does not approve a
behavior or conformance change, publish a contract, or claim whole-v1
conformance.

Approved material SHA-256: `9a4bba8d11db0377d23ddd7b0c74f6e5b65168ef5aca68d57e236b1a1e7b8ab7` (`work/0008/implementation/I-0008-013-portable-core-example-audit.md`).

| Path | SHA-256 |
| --- | --- |
| `SPEC.md` | `998108318c82d9c8c5cb5e70fb99933e3e7d0678e5c98adba8cda8086ff0eed6` |
| `specs/0001-core-pipeline-model.md` | `1ccc40bf3335b1b957b679e5d8439a2abcfebf3a4338583e8aaa024340e7400e` |
| `specs/0002-operation-catalogs-and-host-configuration.md` | `ca889260cd2445fc3a285c978389d0d31a0541d0d2b2d5830af47cfc6b73c2f4` |
