# .NET Toolchain

The reference implementation uses the SDK pinned in
[`implementations/dotnet/global.json`](../../implementations/dotnet/global.json).
Install that .NET 10 SDK before running the commands below.
Package restore uses the nuget.org source declared in
[`implementations/dotnet/NuGet.Config`](../../implementations/dotnet/NuGet.Config)
instead of inheriting machine-specific package sources.

Run commands from `implementations/dotnet/`.

## Visual Studio Code tasks

From **Terminal > Run Task**, use:

- `Qhapaq: Build` to build the solution.
- `Qhapaq: Run CLI` to run the CLI project.
- `Qhapaq: Test Unit` to run all unit-test projects.
- `Qhapaq: Test Integration` to run all integration-test projects.
- `Qhapaq: Test All` to run both test groups.

The build and test tasks use locked dependency restore. `Qhapaq: Build` is the
default build task, and `Qhapaq: Test All` is the default test task.

## Visual Studio Code debugging

Install the workspace's recommended C# Dev Kit extension. The workspace selects
`implementations/dotnet/Qhapaq.slnx` as its default solution so C# Dev Kit can
discover the xUnit projects in the Test Explorer.

Use **Run and Debug > Qhapaq: Launch CLI** to build and debug the executable CLI
implementation. The Hosting and MCP implementation projects are currently
class libraries and therefore do not have independent launch profiles.

Use the Test Explorer's run or debug actions to execute all unit tests, a test
project, a test class, or an individual test. The existing
`Microsoft.NET.Test.Sdk`, xUnit V3, and Visual Studio xUnit runner package
references provide the .NET test harness used by C# Dev Kit.

## Restore

```powershell
dotnet restore Qhapaq.slnx
```

The first restore creates project lock files. After dependency changes are
committed, reproducible validation can use:

```powershell
dotnet restore Qhapaq.slnx --locked-mode
```

## Format

```powershell
dotnet format Qhapaq.slnx --verify-no-changes --no-restore
```

To apply formatting:

```powershell
dotnet format Qhapaq.slnx --no-restore
```

## Build

```powershell
dotnet build Qhapaq.slnx --no-restore
```

Production projects enable nullable reference types and treat compiler warnings
as errors through
[`Directory.Build.props`](../../implementations/dotnet/Directory.Build.props).

## Test

```powershell
dotnet test Qhapaq.slnx --no-build --no-restore
```

The test framework decision is recorded in
[ADR-0002](../architecture/decisions/0002-use-xunit-v3-for-dotnet-tests.md).
