---
id: I-0008-011
kind: implementation
granularity: slice
change_kind: maintenance
title: Separate artifact-authoring policy from path instructions
status: complete
spec: SPEC-0008
requirements:
  - R-0008-004
depends_on:
  - D-0008-002
artifacts:
  - docs/development/conventions/documentation.md
  - docs/development/conventions/schemas.md
  - docs/development/conventions/specifications.md
  - .github/instructions/documentation.instructions.md
  - .github/instructions/schemas.instructions.md
  - .github/instructions/specifications.instructions.md
---

# I-0008-011: Separate Artifact-Authoring Policy from Path Instructions

## Objective and coverage

Move the substantive authoring rules from the documentation, schema, and
specification path instructions into scoped policy guides under
`docs/development/conventions/`. Leave each path instruction as a concise
route to the common and applicable specialized policies, plus any path or
tool-execution guidance permitted by R-0008-004.

This slice reorganizes engineering policy only. It does not change normative
product requirements, schema contracts, or specification-authoring decisions.

## Entry gates

- D-0008-002 remains complete.
- The `engineering-policy` readiness record has been reassessed for the
  decomposed I-0008-001 scope and is approved/current for this slice.
- The exact revised plan and this slice are explicitly approved before
  execution. The existing readiness approval predates the aggregate split and
  is not sufficient without impact review.
- Any proposed change to an authoring rule's meaning is excluded and must be
  resolved in its authoritative policy or specification before this slice
  proceeds.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| Add | `docs/development/conventions/documentation.md` | Own the maintained documentation authoring rules currently in the documentation path instruction. | Not applicable | Repository documentation |
| Add | `docs/development/conventions/schemas.md` | Own schema and conformance-artifact authoring rules currently in the schema path instruction. | Not applicable | Repository documentation |
| Add | `docs/development/conventions/specifications.md` | Own specification-authoring rules currently in the specification path instruction, linking authoritative specification policy rather than restating product behavior. | Not applicable | Repository documentation |
| Modify | `.github/instructions/documentation.instructions.md` | Preserve `applyTo` and route to common and documentation-specific policy. | Not applicable | Agent instruction |
| Modify | `.github/instructions/schemas.instructions.md` | Preserve `applyTo` and route to common, schema-specific, and applicable product policy. | Not applicable | Agent instruction |
| Modify | `.github/instructions/specifications.instructions.md` | Preserve `applyTo` and route to common and specification-specific policy. | Not applicable | Agent instruction |

## Design and integration

Each specialized guide declares its maintained artifact scope, links the
common conventions and applicable authoritative sources, and owns only
artifact-specific authoring concerns. Preserve the current rules' meaning
while transferring them; avoid duplicating common rules or copying normative
product behavior into the guides. The three instructions retain their current
path matching patterns and link to the policy that applies to those paths.

## Tests and validation

- Map every substantive rule in the three current instructions to one
  specialized guide or an existing common rule; document any omitted line as
  routing/tool-execution material rather than silently dropping it.
- Verify the guides declare scope, link common and relevant authoritative
  sources, and do not create conflicting policy.
- Verify each `.github` instruction preserves its existing `applyTo` pattern
  and contains only routing or permitted tool-execution guidance.
- Verify all relative links resolve and run `git diff --check`.
- No repository build, format, lint, or test command is documented for this
  documentation-only slice. Record that absence; do not invent one.

## Exit criteria

- [x] All authoring rules remain present with unchanged meaning in exactly one
      policy source.
- [x] All three path instructions retain their applicability and route to the
      correct common and specialized guides.
- [x] No path instruction remains a competing engineering-policy source.
- [x] All links and whitespace checks pass; no undocumented build or test
      command is claimed.
- [x] Explicit delivery review covers the exact output snapshot.

## Plan approval

Approved explicitly by the user on 2026-10-11 for:

- Revised Phase 2 plan full-byte SHA-256:
  `8559b6347e3163b332bb1bcd1e213f191bf961b66e1e4400476ceb47a326293d`.
- This slice material SHA-256:
  `3b6c4d5b235518e59ebe28d133f9e26051981f0bdd85366c683d4004c7bca571`.
- This slice full-byte SHA-256 at approval:
  `cbd63aa0cb4f47967c1d1a75ee6e16c997fd19d0f6ddaffac0d6f151f3cad7d4`.

Full-byte SHA-256 of governing inputs reviewed:

| Input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `916d6c0094400b87ce1c99661b90590664be588ee1713c2d8b172377567f1272` |
| SPEC-0008 | `1da16621958bc02f12f3903592660de6e4fbc4dfce3cc54c2ba76e52fdd9e57a` |
| SPEC-0006 | `62c8990987dbaa6b49fcecb864216685405ce518dea320bf3db69a115f7a0653` |
| ADR-0003 | `1d01ab049a9bd54dc26a1c3e110f54c2e0cd416c97a67f43b2baf07eb99b0b83` |
| ADR-0004 | `ff5d3fc4f550f73ee88ead69280c3eaa9d57b5cb73089ebc6bd8981b8cfdcf03` |
| D-0008-002 | `6cd4c9a0740873953903e81617c7ad9e493f2321314dcca122465f8e32920afd` |
| D-0008-003 | `65a80afc49a365290ae9c366677e70bb7a46f7c770ab89961285b1b96ad531f5` |
| Common coding conventions | `5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b` |
| Spec-driven workflow | `574d0e18efb42b5701b148a68a62fbd4be7b748e3f276bb6424a056c152507f4` |
| Approved readiness assessment snapshot | `007ac35cc15a8a70ea74c97bee5b436f6a4071ebecd3a981d6d3a92a7c6f4218` |
| Current readiness record | `cc678255b51e3a854d8cb0da155b26f5ef8d28f2ee33be4704941650c0fc1880` |
| Documentation path instruction | `ab813b9414defa53852f6137383b2d0f36897e74903f231b86ef185c6999a477` |
| Schema path instruction | `14a8d2de3283bfde7d94053f45e06bd53943d17ece2130f3ac85842520609b85` |
| Specification path instruction | `fd113cfea6cc774e500ddac0baf21de8d0be2684931faa96e22c7fa55bfcc03a` |

The approved readiness assessment applies to the exact `engineering-policy`
scope and snapshot recorded above. Any material change to this slice's scope, manifest, dependencies, or gates
requires renewed approval.

Renewed approval after source reconciliation:

- The user explicitly approved the current revised plan and this unchanged
  slice material snapshot on 2026-10-11.
- Revised plan full-byte SHA-256:
  `b58de6089af182bca9aefe9fd1df2953a88b31801b59ecd11c0b8e135d2c9d25`.
- This slice material SHA-256:
  `3b6c4d5b235518e59ebe28d133f9e26051981f0bdd85366c683d4004c7bca571`.
- This slice full-byte SHA-256 at renewed approval:
  `f2dd5c9843ee9d55b58a44c6e634f9cce6c23bfb2a8cc6e9c321c320826d8491`.
- The approved readiness assessment snapshot is SHA-256
  `d7336321c16c11706defc78feb234168f0c4b1080438dfa0790993a2f37c6889`.

Updated input snapshots reviewed for renewed approval:

| Input | SHA-256 |
| --- | --- |
| Common coding conventions | `5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b` |
| Completed I-0008-010 | `087441e531f8b82b13b8d945367fa2442c8ca684c405c830d5befd313a831f43` |
| .NET conventions guide | `712c0ed6d05c230f28146b0f4447622c5c62214e4b85c4c2d53d83bac1879c24` |
| .NET path instruction | `287898a2f49f45070fc700b977a04525b3e7bc49ea84b8a9bf8f12bf1f6ff645` |

The earlier approved slice material hash is unchanged; the source reconciliation
did not change this slice's scope, manifest, dependencies, or gates.

## Validation and review

Execution blocked on 2026-10-11 after detecting stale source snapshots. The
plan and readiness record both list
`docs/development/coding-conventions.md` at SHA-256
`49bcf2352eacef3586a789cab06322e7916bf1d5563e8fe54528db1fb6fd8834`, while
the current file is SHA-256
`5bd85f4a6e7ef33da2f53bb821583ccc9f3afdde4b5953550ad3b42da9fdb73b`.
The changed common policy is an output of I-0008-010 and is relevant to this
slice's routing and policy ownership. Reconcile the plan source snapshot and
assess readiness impact, then obtain any required renewed approvals before
resuming.

The policy guides and path-instruction edits in the manifest are preliminary
work only. Before the stale-source blocker was identified, relative links and
anchors, rule-transfer coverage, unchanged `applyTo` patterns, routing-only
instruction content, and `git diff --check` passed. These checks do not
establish slice completion. The specification trace check and final output
review had not run at the initial gate; final checks after source reconciliation
are recorded below.

### Resumption 2026-10-11

The stale-source blocker was resolved by updating the plan's common-policy
source revision and hash, verifying all 12 plan sources, refreshing the
readiness assessment and its 29 source records, and recording the user's
explicit approvals of readiness SHA-256
`d7336321c16c11706defc78feb234168f0c4b1080438dfa0790993a2f37c6889` and
revised plan SHA-256
`b58de6089af182bca9aefe9fd1df2953a88b31801b59ecd11c0b8e135d2c9d25` plus the
unchanged slice material hash. The prior discovery and preliminary checks are
retained above as audit history. Implementation resumed after the readiness
and plan approvals. Final slice validation has passed; exact output review and
delivery approval remain pending.

## Delivery evidence and review

Implemented output snapshot:

| Path | SHA-256 |
| --- | --- |
| `docs/development/conventions/documentation.md` | `ac934e59fe3f4349f2c5302a85c694160829d1f54df5f18ab85f76a79e61c4ce` |
| `docs/development/conventions/schemas.md` | `a9a44c96d0ab48af49d3b7ea8ade8b13f3343814c36842519571f03046f0c33a` |
| `docs/development/conventions/specifications.md` | `8379c469032f87ba8f672b6ac614dd7c53cd0b4e0d4c72140802e61012469297` |
| `.github/instructions/documentation.instructions.md` | `4e84a7e492ea2f86e1e120030882fe7778241b26b107efe703670a38ba0f5b4b` |
| `.github/instructions/schemas.instructions.md` | `bee18c9090b555d6ad1e79105797b77da412fd9135315e290d44824901bcc8c7` |
| `.github/instructions/specifications.instructions.md` | `693dd3fe6360afd6af56250260b4bbf97450e6127d7db9c1beb4805c7904438c` |

Slice material SHA-256 at ready-for-review:
`e3649e8160f8f08e5845385f92c5dcfb42560e9b5f5bcc05ee83da004b805203`.

Validation results:

- Mapped each substantive authoring rule in the three original path
  instructions to its specialized guide. No authoring rule was omitted or
  given a second competing owner; existing authority and precedence are
  linked.
- Confirmed each guide declares applicability and links to common policy and
  relevant authoritative sources. No conflict with R-0008-004 or its decisions
  was found.
- Confirmed all three `applyTo` patterns are unchanged and each path
  instruction contains routing only.
- All relative links and anchors resolve; `git diff --check` passes.
- Specification trace check: `PASS` as `maintenance`. No requirement block,
  product code, or test changed; no `Spec:` trailer applies, and semantic code
  review is not applicable.
- No build, format, lint, or test command is documented for this
  documentation-only slice; none was run.

No deviations or additional files were discovered. The deterministic
trace-checker and language extractor remain outside this slice and are not
claimed as supported. The output snapshot was ready for the explicit delivery
review required before completing I-0008-011.

The user explicitly approved the exact output snapshot above on 2026-10-11.
That approval covers only the six listed policy-guide and path-instruction
files. It does not publish a contract, register a trace-checker extractor, or
claim language traceability support.

After recording that approval and checking the final exit criterion, the
current slice material SHA-256 is
`54b223699b0a6cad2abe96f300d15c0ad1ed6fc359acf567fc443572d2f653bc`.
