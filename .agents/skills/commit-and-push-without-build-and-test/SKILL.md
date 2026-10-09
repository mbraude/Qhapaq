---
name: commit-and-push-without-build-and-test
description: Commit and push the selected Git snapshot without running the build and unit tests. Use when the user explicitly asks to commit and push while skipping build-and-test validation.
---

# Commit and Push Without Build and Test

Invoke the repository's `commit-and-push` skill with
`skip-build-and-test=true`.

Do not duplicate or replace any part of that skill's workflow. The
`commit-and-push` skill remains responsible for reviewing changes, running any
other required checks, staging, committing, pushing, and reporting that the
build and unit tests were skipped.
