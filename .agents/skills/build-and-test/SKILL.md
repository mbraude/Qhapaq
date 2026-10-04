---
name: build-and-test
description: Restore locked dependencies, build the Qhapaq .NET solution, and run every unit test project. Use when the user asks to build and run unit tests or before committing repository changes.
---

# Build and Test

Use this skill in the Qhapaq repository to verify that the .NET solution builds
and all unit tests pass. Integration tests are outside this skill's scope.

## Preconditions

1. Read and follow the repository's contributor and agent instructions.
2. Confirm that these repository files exist:
   - `implementations/dotnet/global.json`
   - `implementations/dotnet/Qhapaq.slnx`
   - `implementations/dotnet/NuGet.Config`
3. Confirm that the .NET SDK selected by `global.json` is available.
4. Inspect the complete working-tree status so the report can distinguish
   validation from unrelated or concurrent changes.

Do not modify source files, dependency manifests, lock files, or build
configuration as part of this skill. Do not install or update an SDK or restore
tool unless the user explicitly requests it.

## Workflow

Run every command from `implementations/dotnet/`. Stop at the first failing
step, preserve its output, and report the failure without claiming later steps
passed.

### 1. Build with locked dependencies

```text
dotnet build Qhapaq.slnx -p:RestoreLockedMode=true
```

This performs locked restore as part of the build and fails when a dependency
manifest and its lock file disagree.

### 2. Run all unit test projects

Run each project below with the outputs produced by the successful build:

```text
dotnet test tests/unit/Qhapaq.Architecture.Tests/Qhapaq.Architecture.Tests.csproj --no-build --no-restore
dotnet test tests/unit/Qhapaq.Business.Tests/Qhapaq.Business.Tests.csproj --no-build --no-restore
dotnet test tests/unit/Qhapaq.DAL.Tests/Qhapaq.DAL.Tests.csproj --no-build --no-restore
dotnet test tests/unit/Qhapaq.Service.V1.Tests/Qhapaq.Service.V1.Tests.csproj --no-build --no-restore
```

Run all four projects even when one project currently contains no substantive
behavioral tests. Do not replace these commands with a solution-wide test,
because that would also run integration tests.

### 3. Report

Report:

- whether the locked build succeeded;
- the warning and error counts reported by the build;
- the pass, fail, and skip totals for each unit test project;
- the overall unit-test totals; and
- the first failed command and relevant error output when validation stops.

Do not report success unless the build and all four unit test projects
completed successfully.
