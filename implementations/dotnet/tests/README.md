# .NET Tests

.NET tests are separated by boundary:

- [unit/](unit/) contains fast, isolated behavioral tests.
- [integration/](integration/) contains tests spanning components, process
  boundaries, packaging, or external protocol adapters.

Language-neutral cases belong in [conformance/](../../../conformance/) and are
consumed by the appropriate .NET test harness rather than duplicated here.
