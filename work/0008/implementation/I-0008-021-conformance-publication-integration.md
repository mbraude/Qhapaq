---
id: I-0008-021
kind: implementation
granularity: slice
change_kind: extension
title: Enforce protected conformance publication
status: open
spec: SPEC-0008
requirements:
  - R-0005-034
  - R-0005-035
  - R-0008-007
  - R-0008-008
  - R-0008-009
  - R-0008-010
  - R-0008-011
  - R-0008-012
  - R-0008-013
  - R-0008-014
  - R-0008-015
  - R-0008-019
  - R-0008-020
  - R-0008-021
  - R-0008-022
  - R-0008-023
  - R-0008-024
  - R-0008-025
  - R-0008-026
  - R-0008-027
depends_on:
  - I-0008-009
  - I-0008-020
artifacts:
  - build/conformance-publication.json
  - build/fixtures/conformance-publication/valid-progress-release.json
  - build/fixtures/conformance-publication/invalid-edge-claim.json
  - build/fixtures/conformance-publication/invalid-missing-evidence.json
  - build/fixtures/conformance-publication/invalid-digest-mismatch.json
  - build/README.md
  - scripts/Test-ConformancePublication.ps1
  - scripts/Publish-Conformance.ps1
  - scripts/README.md
  - .github/workflows/conformance-publication.yml
---

# I-0008-021: Enforce Protected Conformance Publication

## Objective and coverage

Integrate profile, progress, and full-claim publication with the immutable
workspace evidence and root release manifest produced through the approved root
orchestration. Protected stable or prerelease events may promote explicitly
approved exact profile or full-claim inputs. Edge may publish immutable
progress only and must not publish or imply conformance.

This slice does not redefine workspace-native commands, rebuild an artifact,
approve an input, publish automatically on work-item completion, or create an
unprotected publication path.

## Entry gates

- I-0008-009 has delivered approved root adapters, impact selection, digest-only
  aggregation, and exact release-manifest handling.
- I-0008-020 has delivered approved report producers and exact evidence
  contracts for the evaluated artifact set.
- I-0008-017 through I-0008-019 are complete, so all consumed schemas, profile
  candidates, and vectors exist at their approved exact digests.
- I-0008-012, current release/security readiness for the workflow surface, and
  this exact slice plan are explicitly approved.
- Repository protection supplies an authorized maintainer approval boundary
  for stable and prerelease environments. If that capability or the exact
  workflow event contract is absent, the slice is blocked rather than
  weakening R-0008-023 or inventing authority.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| add | `build/conformance-publication.json` | Root publication input groups and protected-event policy | Root orchestration | Repository-internal |
| add | `build/fixtures/conformance-publication/valid-progress-release.json` | Positive exact-manifest progress fixture | Root orchestration tests | Test fixture |
| add | `build/fixtures/conformance-publication/invalid-edge-claim.json` | Reject full claim from edge | Root orchestration tests | Test fixture |
| add | `build/fixtures/conformance-publication/invalid-missing-evidence.json` | Reject omitted or unavailable required evidence | Root orchestration tests | Test fixture |
| add | `build/fixtures/conformance-publication/invalid-digest-mismatch.json` | Reject substituted bytes | Root orchestration tests | Test fixture |
| modify | `build/README.md` | Document publication policy input and root ownership | Root orchestration documentation | Public contributor documentation |
| add | `scripts/Test-ConformancePublication.ps1` | Offline fail-closed validation of exact publication inputs | Root adapter | Repository-internal |
| add | `scripts/Publish-Conformance.ps1` | Protected promotion adapter consuming validated exact bytes | Root adapter | Repository-internal |
| modify | `scripts/README.md` | Document validation, dry-run, promotion, and authorized retry commands | Root automation documentation | Public contributor documentation |
| add | `.github/workflows/conformance-publication.yml` | Edge progress and protected stable/prerelease publication gates | GitHub Actions | Repository automation |

## Design and integration

`Test-ConformancePublication.ps1` validates schema identity, digests,
provenance, evidence outcomes, profile prerequisites, declaration kind,
publication approval, lifecycle state, and root release membership without
mutating an artifact. `Publish-Conformance.ps1` accepts only that verified
manifest and exact bytes. It cannot rebuild, rewrite, merge private workspace
output, infer approval, or replace an immutable destination.

The workflow separates edge, prerelease, and stable events. Protected events
bind one identified authorized maintainer's approval to the exact immutable
inputs. Correction creates a new object, status changes append entries,
withdrawal preserves a tombstone, and authorized retry consumes the same
verified bytes. Retention keeps records indefinitely and evidence resolvable
while a declaration is presented as verifiable.

This slice completes the conformance-artifact prerequisite in migration stage
2 of R-0008-027 but performs no migration. Any future move or rename of these
files is separately governed by R-0008-028 and R-0008-029.

## Tests and validation

The planned documented commands are:

```text
pwsh -NoProfile -File scripts/Test-ConformancePublication.ps1 -Manifest <root-release-manifest> -Mode Progress
pwsh -NoProfile -File scripts/Test-ConformancePublication.ps1 -Manifest <root-release-manifest> -Mode Prerelease
pwsh -NoProfile -File scripts/Test-ConformancePublication.ps1 -Manifest <root-release-manifest> -Mode Stable
pwsh -NoProfile -File scripts/Publish-Conformance.ps1 -Manifest <root-release-manifest> -Mode <Progress|Prerelease|Stable> -WhatIf
```

The slice tests every checked-in fixture plus invalid approval, lifecycle,
retention, unresolved evidence, skipped evidence, unsupported prerequisite,
immutable-destination conflict, and retry cases. Workflow validation proves
that edge cannot select prerelease/stable or a full claim and protected modes
cannot run without exact approval. Also run the I-0008-009 root validation
command, `git diff --check`, and `spec-trace-check`.

The final plan approval must replace `<root-release-manifest>` and the
I-0008-009 command reference with the exact path and documented command from
the completed I-0008-009 slices. Their absence is a blocker.

## Exit criteria

- [ ] All valid fixtures and dry runs consume exact verified bytes without
  rebuild or rewrite.
- [ ] Every missing, skipped, unavailable, unsuccessful, mismatched,
  unapproved, unprotected, or immutable-destination-conflicting input fails.
- [ ] Edge can publish progress only; full profiles and claims require
  protected stable or prerelease promotion.
- [ ] Correction, status, withdrawal, retention, and authorized retry preserve
  immutable history and audit evidence.
- [ ] Delivery evidence records workflow revision, protection evidence,
  commands, exact manifest and artifact digests, results, and explicit review.
- [ ] No publication occurs as part of testing or delivery review.

## Plan approval

Absent. Approval is blocked until I-0008-009 establishes the exact root
manifest path/command and release/security readiness covers the workflow and
environment-protection configuration.

## Delivery evidence and review

No workflow, profile, claim, progress declaration, publication record, release,
or protected environment has been created or approved.
