# .NET Toolchain

The reference implementation uses the SDK pinned in
[`implementations/dotnet/global.json`](../../implementations/dotnet/global.json).
Install that .NET 10 SDK before running the commands below.
Package restore uses the nuget.org source declared in
[`implementations/dotnet/NuGet.Config`](../../implementations/dotnet/NuGet.Config)
instead of inheriting machine-specific package sources.

Run commands from `implementations/dotnet/`.

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
