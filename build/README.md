# Build Orchestration

This directory is reserved for checked-in build orchestration shared by local
development and CI. It may contain declarative build configuration and reusable
build targets after the .NET solution and documentation toolchain are selected.

Generated binaries, packages, logs, test results, caches, and website output do
not belong here. Build behavior must remain invocable through maintained scripts
under [scripts/](../scripts/).
