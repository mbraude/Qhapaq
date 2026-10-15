# Checklist migration reconciliation

[Reconciliation index](index.md) | [Work plan](../plan.md)

- Date: 2026-10-09. User explicitly requested removal of the legacy specification
  sequence and use of Git history for previously completed decisions. This
  reconciliation supersedes the initial extraction's duplicate-tracking and
  inherited-review gates; it does not approve any remaining decision or delivery.
- Baseline remains `34fbe88fb9d4857adc6db5390cc623c210c71540`. SPEC-0007's source
  hash records reviewed working-copy bytes, not committed text. Other source
  records remain unchanged.
- Section 21 now contains declarative publication, acceptance, and migration
  requirements, not phases, task checkboxes, or implementation dependency lists.
  R-0007-336/338/339 are retired operational/summary blocks; all IDs remain
  present. R-0007-337 and R-0007-340 through R-0007-370 retain the applicable
  normative obligations. Section 8 references no longer rely on legacy phases
  or completed-checkpoint status.
- Existing phase membership, preferred order, organization prerequisites,
  independent descriptor/parsing work, future milestones, and companion delivery
  coverage remain here. No new items, completed-history placeholders, production
  code, or executable slices are introduced.
- D-0007-007 is cancelled, not completed or deleted. D-0007-002 and
  I-0007-003/005/006 no longer depend on it; I-0007-004 no longer names it as an
  entry gate. D-0007-002 still requires the current completeness audit after
  D-0007-001. Publication and scoped readiness still require actual evidence.
- I-0007-025 no longer references retired R-0007-336. Existing references to the
  remaining acceptance requirements still govern the same milestone coverage.
  No code/test inline references to changed blocks require fingerprint updates.
- No readiness records or approved slices exist in this plan. Remaining numeric,
  contract, organization, and companion-spec decisions stay unresolved. Migration
  does not publish a contract or establish execution readiness.
- Validation: checked all 48 unique item identities, metadata and required
  sections, one phase membership each, 95 dependency edges, acyclic graph,
  non-retired requirement references, and absence of cancelled prerequisites.
  Resolved 77 repository-relative links and anchors across the plan, items, and
  specification. Checked 11 source records and unchanged non-specification
  hashes, ASCII work artifacts, and whitespace. The specification contains no
  task checkboxes or phase references; no stale phase anchors remain.
- Specification trace check: PASS with warnings. Scope since HEAD is one
  Specification and 49 Other/planning files, including the existing untracked
  extraction. All 384 requirement IDs are preserved; 43 blocks changed,
  including three retained retirement tombstones. Exact fingerprints were
  computed using the trace skill helper. Repository-wide reverse-impact search
  found no fingerprinted code/test references to the changed blocks, and no
  work item references a retired block. No product/test code changed.
- Semantic review ran, not skipped. Reviewed the legacy checklist against
  retained requirements and work coverage: R-0007-064/093/129 through 132/140,
  R-0007-336 through R-0007-370, and R-0007-378/383. Completed semantics remain
  in their substantive specification sections; publication, compatibility,
  exact identity, normalization, complete binding, non-durability, independent
  permission/disclosure, and execution safety obligations remain intact.
- Warning: R-0007-349/352/368 retain implementation type and assembly names
  (`Qhapaq.Abstractions`, `IOperation<TInput, TOutput>`, `Qhapaq.Service.V1`)
  from the former checklist. These remain explicitly .NET-specific acceptance
  requirements, not dependencies of the portable contract. No new implementation
  names or source-file references were added.
- Classification: amendment, because the specification's legacy operational
  tracking authority is explicitly retired. Product behavior is retained;
  associated planning maintenance is inseparable from this migration. No new
  waivers or waived findings. No build or unit tests run for this documentation-only
  change. No commit, contract publication, readiness, or delivery approval.

### Proposed commit trailers

```text
Change-Kind: amendment
Spec: R-0007-064@11dacd, R-0007-093@02bc90, R-0007-129@8f3c40, R-0007-130@33feb8, R-0007-131@2e230b, R-0007-132@b393aa, R-0007-140@dece32
Spec: R-0007-337@59e5d2, R-0007-340@461e39, R-0007-341@99d07c, R-0007-343@028495, R-0007-344@25665b, R-0007-345@040649, R-0007-346@c13709, R-0007-347@4a4d6f, R-0007-348@751226
Spec: R-0007-349@9ad651, R-0007-350@6c7d7d, R-0007-351@61802f, R-0007-352@9878cd, R-0007-353@0385b0, R-0007-354@e02caa, R-0007-355@1001ba, R-0007-356@d72b96, R-0007-357@92d8c6, R-0007-358@ed3c88, R-0007-359@d7f0b0, R-0007-360@96f212
Spec: R-0007-361@92d9bb, R-0007-362@78ddc6, R-0007-363@dca37b, R-0007-364@70d920, R-0007-365@916de2, R-0007-366@5563c5, R-0007-367@7d10ba, R-0007-368@c5f632, R-0007-369@511eb8, R-0007-370@7bc93c, R-0007-378@df03a9, R-0007-383@28fa2d
```
