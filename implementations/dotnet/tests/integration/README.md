# Integration Tests

Integration tests cover boundaries such as CLI processes, MCP transport,
dependency-injection hosting, package consumption, extension loading, connector
adapters, and website or release smoke checks where applicable.

Each test must declare its external requirements, isolate mutable state, avoid
real user credentials, and provide actionable failure diagnostics.
