---
id: I-0008-020
kind: implementation
granularity: slice
change_kind: extension
title: Connect .NET profile adapters and immutable evidence
status: open
spec: SPEC-0008
requirements:
  - R-0006-035
  - R-0006-036
  - R-0006-037
  - R-0006-038
  - R-0006-039
  - R-0007-347
  - R-0007-348
  - R-0008-006
  - R-0008-007
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
depends_on:
  - I-0008-019
artifacts:
  - implementations/dotnet/tests/unit/Qhapaq.Business.Tests/Conformance/RuntimeProfileEvidenceTests.cs
  - implementations/dotnet/tests/unit/Qhapaq.Business.Tests/Qhapaq.Business.Tests.csproj
  - implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/Conformance/DotNetInProcessProfileEvidenceTests.cs
  - implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/Qhapaq.Architecture.Tests.csproj
  - implementations/dotnet/tests/integration/Qhapaq.Implementations.CLI.Tests/Conformance/LocalCliProfileEvidenceTests.cs
  - implementations/dotnet/tests/integration/Qhapaq.Implementations.CLI.Tests/Qhapaq.Implementations.CLI.Tests.csproj
  - implementations/dotnet/tests/integration/Qhapaq.Implementations.MCP.Tests/Conformance/McpHostProfileEvidenceTests.cs
  - implementations/dotnet/tests/integration/Qhapaq.Implementations.MCP.Tests/Qhapaq.Implementations.MCP.Tests.csproj
  - implementations/dotnet/tests/ConformanceEvidence.runsettings
---

# I-0008-020: Connect .NET Profile Adapters and Immutable Evidence

## Objective and coverage

Connect the four portable candidate profiles and shared vectors to the existing
.NET unit, architecture, CLI integration, and MCP integration test surfaces.
The adapters evaluate applicable recipes and emit immutable, payload-safe
assessment and evidence artifacts for the exact built artifact set.

This slice reuses the shared vector loader and portable validation semantics
owned by I-0007-002 and I-0007-005. It adds no second loader, validator,
canonicalizer, schema runtime, or production-layer bypass. It does not assert a
claim or publish evidence.

## Entry gates

- I-0008-019 and all of its prerequisites are complete and approved.
- The shared tooling's supported adapter API and report output contract are
  recorded in the completed I-0007-002 child manifests.
- The current .NET model ownership, project boundaries, and architecture tests
  remain consistent with R-0006-035 through R-0006-039.
- I-0008-012, current implementation readiness for these test projects, and
  this exact slice plan are explicitly approved.
- Every recipe leaf that cannot be exercised by these projects has a governed
  external evidence kind; the adapter must report it as missing or
  unsuccessful rather than fabricate success.

## File and ownership manifest

| Action | Repository-relative path | Purpose | Project / namespace | Visibility |
| --- | --- | --- | --- | --- |
| add | `implementations/dotnet/tests/unit/Qhapaq.Business.Tests/Conformance/RuntimeProfileEvidenceTests.cs` | Runtime profile vector, validation, execution, cancellation, and failure evidence | `Qhapaq.Business.Tests.Conformance` | Test-internal |
| modify | `implementations/dotnet/tests/unit/Qhapaq.Business.Tests/Qhapaq.Business.Tests.csproj` | Reference approved portable assets/tooling and emit evidence as test artifacts | `Qhapaq.Business.Tests` | Test project |
| add | `implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/Conformance/DotNetInProcessProfileEvidenceTests.cs` | In-process API, model ownership, visibility, package, and dependency evidence | `Qhapaq.Architecture.Tests.Conformance` | Test-internal |
| modify | `implementations/dotnet/tests/unit/Qhapaq.Architecture.Tests/Qhapaq.Architecture.Tests.csproj` | Include candidate profiles and evidence output configuration | `Qhapaq.Architecture.Tests` | Test project |
| add | `implementations/dotnet/tests/integration/Qhapaq.Implementations.CLI.Tests/Conformance/LocalCliProfileEvidenceTests.cs` | Local CLI adapter and cumulative runtime evidence | `Qhapaq.Implementations.CLI.Tests.Conformance` | Test-internal |
| modify | `implementations/dotnet/tests/integration/Qhapaq.Implementations.CLI.Tests/Qhapaq.Implementations.CLI.Tests.csproj` | Include exact shared inputs and evidence output configuration | `Qhapaq.Implementations.CLI.Tests` | Test project |
| add | `implementations/dotnet/tests/integration/Qhapaq.Implementations.MCP.Tests/Conformance/McpHostProfileEvidenceTests.cs` | MCP host policy, disclosure, payload safety, and cumulative runtime evidence | `Qhapaq.Implementations.MCP.Tests.Conformance` | Test-internal |
| modify | `implementations/dotnet/tests/integration/Qhapaq.Implementations.MCP.Tests/Qhapaq.Implementations.MCP.Tests.csproj` | Include exact shared inputs and evidence output configuration | `Qhapaq.Implementations.MCP.Tests` | Test project |
| add | `implementations/dotnet/tests/ConformanceEvidence.runsettings` | Bounded deterministic evidence directory and non-sensitive collector settings | .NET test workspace | Repository-internal |

Evidence outputs are generated, content-addressed build artifacts and are not
checked into source control.

## Design and integration

Each adapter consumes supported public contracts and the shared portable
tooling. Business owns the reusable .NET validation semantics; test adapters
do not expose layer-private models or make transport/compiler models public.
CLI and MCP evaluate independent surface profiles against the same exact
runtime artifact set and prerequisite profile candidate.

Evidence identifies workspace, exact command and toolchain, source revision,
artifact-set digest, profile candidate digest, suite versions, bounded outcome,
and artifact digest. Reports contain synthetic identifiers and bounded
diagnostics, never operation payloads, credentials, environment secrets, or
machine-specific paths. Skipped, missing, timed-out, unsupported, mismatched,
or incomplete mandatory evidence remains unsuccessful.

## Tests and validation

From `implementations/dotnet`, using locked restore:

```text
dotnet build Qhapaq.slnx -p:RestoreLockedMode=true
dotnet test tests/unit/Qhapaq.Business.Tests/Qhapaq.Business.Tests.csproj --no-build --no-restore --settings tests/ConformanceEvidence.runsettings
dotnet test tests/unit/Qhapaq.Architecture.Tests/Qhapaq.Architecture.Tests.csproj --no-build --no-restore --settings tests/ConformanceEvidence.runsettings
dotnet test tests/integration/Qhapaq.Implementations.CLI.Tests/Qhapaq.Implementations.CLI.Tests.csproj --no-build --no-restore --settings tests/ConformanceEvidence.runsettings
dotnet test tests/integration/Qhapaq.Implementations.MCP.Tests/Qhapaq.Implementations.MCP.Tests.csproj --no-build --no-restore --settings tests/ConformanceEvidence.runsettings
```

Also run the approved shared read-only conformance command, compare repeat-run
evidence digests under varied culture and path roots, scan reports for fixture
payloads and secret-shaped values, run `git diff --check`, and run
`spec-trace-check`.

## Exit criteria

- [ ] Each profile adapter evaluates the exact candidate and prerequisite
  digests and reports exhaustive mandatory-obligation dispositions.
- [ ] Architecture tests preserve model ownership and dependency direction.
- [ ] All listed build and tests pass with locked dependencies.
- [ ] Repeat runs are deterministic and reports are bounded and payload-safe.
- [ ] Missing, skipped, unsupported, unavailable, or mismatched evidence fails.
- [ ] Delivery evidence records exact source/build/profile/vector/toolchain
  inputs, output digests, commands, results, and explicit review.

## Plan approval

Absent. Approval requires the final I-0007-002 adapter contract, applicable
implementation readiness, and exact review of this manifest and test matrix.

## Delivery evidence and review

No adapter, report, evidence bundle, declaration, or claim has been produced.
