# Automation Scripts

Maintained local and CI entry points belong here. Scripts should provide the
same commands used by GitHub Actions for restore, format verification, build,
test, pack, site generation, and release verification.

Scripts must:

- Be non-interactive by default in CI.
- Fail explicitly and preserve useful diagnostics.
- Avoid hidden machine state and committed credentials.
- Use pinned tools and repository-relative paths.
- Document supported platforms and required environment variables.

Workflow YAML should orchestrate these scripts rather than duplicate their
logic.

## Available checks

- `test-git-hooks.ps1`: tests local `Change-Kind:` enforcement in an isolated
  temporary Git repository. See the
  [Git hook guide](../docs/development/git-hooks.md) for setup and execution.
