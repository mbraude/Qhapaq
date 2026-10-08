# Local Git Hooks

[ADR-0004](../architecture/decisions/0004-classify-changes-and-trace-through-commits.md)
requires a `Change-Kind:` trailer on every commit, including intermediate
work. The commit skills generate it; the repository-managed
[`commit-msg` hook](../../.githooks/commit-msg) checks it for direct Git commits
as well.

## Enable in each clone

First inspect existing configuration and hooks:

```text
git config --show-origin --get core.hooksPath
git rev-parse --git-path hooks
```

If another hook directory or active hook exists, do not overwrite it. Arrange
an explicit integration so both checks run. Otherwise, from the repository
root, enable the tracked hooks:

```text
git config --local core.hooksPath .githooks
```

This is local clone configuration, not a setting propagated by commits.
The hook runs with Git's POSIX shell and `awk`; Git for Windows supplies both.
On Unix, the hook must be executable.

## Commit message

Use exactly one canonical `Change-Kind:` trailer in the final trailer block:

```text
chore: update contributor guidance

Change-Kind: maintenance
Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

Allowed kinds are `requirement`, `amendment`, `extension`, `bug`, `editorial`,
`refactor`, and `maintenance`. The hook uses `git interpret-trailers --parse`,
so a mention in the subject or body is not sufficient. Missing, duplicate,
unknown, or incorrectly cased trailers fail with diagnostics. Other trailers
are preserved.

The hook checks only `Change-Kind:` syntax. The
[`spec-trace-check` skill](../../.agents/skills/spec-trace-check/SKILL.md)
checks classification, required `Spec:` references, and conformance. Hooks are
local and bypassable; agents must not bypass them. Future CI remains necessary
for centrally enforced validation.

## Regression checks

Run from the repository root using PowerShell 7:

```powershell
& .\scripts\test-git-hooks.ps1
```

The script creates an isolated temporary Git repository and invokes the real
hook through `git hook run`. It does not commit, stage, or change configuration
in the working repository, and removes its temporary files after execution.
