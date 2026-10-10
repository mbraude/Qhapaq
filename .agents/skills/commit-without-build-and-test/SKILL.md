---
name: commit-without-build-and-test
description: Commit the selected Git snapshot locally without pushing or running the build and unit tests. Use when the user explicitly asks to commit while skipping build-and-test validation.
---

# Commit Without Build and Test

Invoke the repository's `commit` skill with `skip-build-and-test=true`.

Do not duplicate or replace any part of that skill's workflow. The `commit`
skill remains responsible for reviewing changes, running any other required
checks, staging, committing locally, and reporting that the build and unit
tests were skipped. This wrapper never pushes.
