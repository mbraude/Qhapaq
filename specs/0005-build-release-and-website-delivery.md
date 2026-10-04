# SPEC-0005: Build, Release, and Website Delivery

> **Status:** Draft
> **Target:** Qhapaq v1
> **Last updated:** 2026-10-04

## 1. Summary

Qhapaq uses GitHub Actions to validate every proposed change, build every push,
publish continuously consumable development artifacts from `main`, publish
immutable stable releases from protected Semantic Version tags, and deploy the
public website to Azure Static Web Apps.

Delivery is event-driven rather than tied to an arbitrary release calendar.
Every pull request receives validation and a website preview. Every merge to
`main` updates the public website and the explicitly unstable `edge` channel.
Creating a protected version tag publishes a stable release. Scheduled workflows
provide deeper assurance but do not publish stable releases.

Automation must build an artifact once within a delivery run and promote that
same artifact through verification and publication. A successful build alone is
not permission to publish: repository rules, workflow permissions, protected
environments, and event-specific policy determine which destinations a run may
change.

## 2. Goals

- Give maintainers fast, required feedback on every pull request.
- Produce downloadable builds for every push without presenting them as stable
  releases.
- Keep the production website synchronized with reviewed changes on `main`.
- Publish stable packages and binaries automatically from an auditable release
  decision.
- Publish the four NuGet packages, self-contained CLI distributions, container
  image, schemas, conformance data, checksums, provenance, and release notes
  consistently.
- Use short-lived or narrowly scoped credentials and least-privilege workflow
  permissions.
- Make every published artifact traceable to one commit, workflow run, source
  tree, dependency set, and version.
- Keep build, test, packaging, and site-generation commands runnable locally
  through maintained scripts rather than embedding their behavior only in
  workflow YAML.
- Make failed deployments recoverable without rewriting published history.

## 3. Non-goals

This specification does not:

- Require a fixed weekly, monthly, or quarterly stable release cadence.
- Publish packages or deploy production resources from pull requests or
  unprotected branches.
- Treat a branch build, workflow artifact, or `edge` artifact as a supported
  stable release.
- Permit stable package versions, release tags, container digests, checksums, or
  provenance records to be overwritten.
- Require every expensive platform or security test to block pull-request
  iteration when a scheduled workflow can provide timely coverage.
- Define the website's visual design, information architecture, or static-site
  generator.
- Make generated website content a substitute for version-controlled source
  documentation.

## 4. Delivery Channels and Cadence

Qhapaq has three user-visible channels:

1. **Preview:** pull-request artifacts and an isolated website environment for
   review. Preview outputs are temporary and never presented as releases.
2. **Edge:** the newest successful `main` build. It is automatic, public,
   replaceable as the channel pointer, and unsupported for production use. Each
   underlying build remains identifiable by commit and unique version.
3. **Stable:** an immutable Semantic Version release created from a protected
   `v<major>.<minor>.<patch>` tag. Prerelease tags such as
   `v<major>.<minor>.<patch>-rc.<number>` may publish an explicitly marked
   prerelease.

The event cadence is:

| Event | Required behavior | Publication |
| --- | --- | --- |
| Pull request targeting `main` | Run required CI, package smoke tests, documentation checks, and build a website preview | Temporary workflow artifacts and Azure Static Web Apps preview only |
| Push to a non-default branch | Run branch CI when enabled | Temporary workflow artifacts only |
| Merge or direct protected push to `main` | Run the full release-shaped build, update `edge`, and deploy the production website | Rolling edge release, immutable commit-addressed artifacts, `edge` container tag, and production website |
| Protected release tag | Rebuild and verify the tagged commit, then publish all release outputs from the verified artifact set | Stable or prerelease GitHub Release, NuGet packages, container tags, schemas, conformance bundle, checksums, SBOM, and provenance |
| Nightly schedule | Run expensive cross-platform, integration, packaging, trimming, and security checks when relevant source changed | Test reports only unless an explicit future policy adds a nightly channel |
| Weekly schedule | Run dependency, license, secret, vulnerability, and workflow-permission review | Reports and automated update issues or pull requests |
| Manual workflow dispatch | Retry a failed idempotent publication, redeploy a previously verified website artifact, or perform documented recovery | Only the destination and artifact identity explicitly selected by an authorized maintainer |

Stable releases are readiness-driven during v1. Maintainers should review release
readiness at least monthly, but must not publish an empty or insufficiently
validated release to satisfy a calendar. A regular release train may be adopted
after demand and compatibility commitments justify it.

## 5. Workflow Topology

The initial workflow set is:

- `ci.yml`: pull-request, branch, and reusable validation jobs.
- `edge.yml`: `main` build and edge publication.
- `release.yml`: protected tag validation and stable or prerelease publication.
- `website.yml`: pull-request previews, production deployment, and cleanup.
- `scheduled.yml`: nightly and weekly assurance jobs.

The exact file split may change, but event permissions and responsibilities must
remain separate. In particular, untrusted pull-request jobs must not have access
to release, package-publishing, container-publishing, or production-deployment
credentials.

Workflows call repository scripts for restore, format verification, build,
test, pack, site generation, and package verification. Local and CI execution
must use the same pinned SDK, lock files, and warnings-as-errors policy.

Concurrency rules cancel superseded pull-request and website-preview runs. A
release publication is never canceled merely because a newer commit or tag
appears. Publication jobs use idempotency checks so retrying a partially failed
run neither overwrites an immutable artifact nor reports false success.

Required pull-request checks initially include:

- Formatting, compilation, analyzers, and unit tests.
- Applicable integration and conformance tests.
- JSON Schema and generated-artifact consistency checks.
- Documentation build, link checking, and website build.
- Clean package-consumer and self-contained CLI smoke tests.
- Secret, dependency, license, and source-policy checks.

The supported operating-system and architecture matrix is defined separately.
Pull requests may use a representative blocking matrix when the complete matrix
is too expensive, but `main`, release, and scheduled workflows must provide
complete supported-target coverage before a target is advertised.

## 6. Build and Version Model

One source commit produces one internally consistent artifact set. The build
records:

- Full Git commit SHA and source repository.
- Workflow identity and run ID.
- .NET SDK, tool, and dependency-lock versions.
- Pipeline document, schema, conformance, CLI, MCP, and package versions where
  applicable.
- Build timestamp used only where reproducibility permits it.

Stable artifact versions come only from the protected release tag. Edge
artifacts use a unique SemVer-compatible prerelease version containing an
ordered build identifier and commit identity. A mutable `edge` label or download
link may point to the newest successful build, but the underlying artifact
manifest must expose its unique version and full commit SHA.

A release workflow builds the tagged commit once, stores the resulting artifact
set, verifies it in clean environments, and publishes those exact bytes to every
destination. Publication steps must not rebuild packages independently.

The release manifest inventories every output, media type, version, digest,
target platform, and destination. Checksums, SBOMs, signatures or attestations,
and provenance refer to the exact published bytes.

## 7. Published Outputs

### 7.1 Edge

Every successful `main` run publishes:

- Self-contained CLI archives for the supported platform matrix.
- The four NuGet package files as downloadable artifacts, without pushing them
  to the stable nuget.org feed.
- A container image tagged both with an immutable commit-derived tag and the
  moving `edge` tag.
- Schemas, conformance vectors, generated reference documentation, checksums,
  SBOMs, and provenance.
- A rolling public edge release or download index that links to the exact
  commit-addressed build.

Temporary GitHub Actions artifacts may supplement the public edge channel but
must not be its only storage because they expire and may require authentication.

### 7.2 Stable and Prerelease

A protected Semantic Version tag publishes:

- `Qhapaq.Abstractions`, `Qhapaq`, `Qhapaq.Hosting`, and `Qhapaq.Mcp` to
  nuget.org.
- Self-contained CLI archives and checksums to an immutable GitHub Release.
- A multi-platform container image with immutable version and digest metadata.
- Normative schemas and conformance vectors as versioned release assets.
- SBOMs, artifact attestations or equivalent provenance, release notes, license
  notices, and required third-party attributions.

Release candidates use prerelease versions and are clearly separated from the
stable install path. The website defaults to the latest stable release while
offering an explicitly labeled edge or prerelease download path.

Published stable package versions and release assets are never replaced. A bad
release is deprecated where the destination supports it and corrected with a
new version.

## 8. Website Delivery

The public static website is hosted by Azure Static Web Apps. Repository content
is canonical; the deployed site is generated output.

For a pull request that changes website, documentation, examples, schemas, or
generated reference inputs, automation:

1. Builds the site from that pull request.
2. Runs link, accessibility, and applicable browser smoke checks.
3. Deploys an isolated preview environment.
4. Reports the preview URL and test result on the pull request.
5. Deletes the preview environment when the pull request closes.

After a reviewed change reaches `main`, automation rebuilds and tests the site,
then deploys production. A merge to protected `main` is the approval event; the
normal production deployment should not require a second routine button click.
The GitHub production environment restricts the workflow, branch, and
credentials that can deploy.

Versioned API and specification documentation is published by the release
workflow. General project content may update with every `main` merge. The site
must clearly distinguish documentation for stable, prerelease, and edge
versions.

Website rollback redeploys a previously verified site artifact or source commit.
Rollback does not rewrite repository history. Production smoke checks run after
deployment, and a failure blocks success reporting and initiates the documented
recovery path.

## 9. Credentials and Workflow Security

Workflow permissions default to read-only and are elevated per job. Actions are
pinned to reviewed immutable revisions according to repository policy.

- NuGet publication uses nuget.org Trusted Publishing with GitHub OIDC and
  short-lived credentials rather than a stored long-lived API key.
- Azure access uses workload identity federation where the selected deployment
  path supports it.
- Azure Static Web Apps deployment may use its repository deployment token when
  required by that service. The token is stored only in a protected GitHub
  environment, scoped to the site, masked, rotated, and unavailable to
  pull-request code from forks.
- GitHub Releases and GitHub Container Registry use a narrowly permissioned
  workflow token.
- Signing services use short-lived identity or hardware-backed keys where
  practical; private signing material is never committed or exposed to
  untrusted jobs.

Release tags, workflow files, build scripts, dependency locks, and production
site configuration require code-owner review. Protected environments limit
which branches or tags may deploy. Fork pull requests run without privileged
secrets and must not use a workflow event that executes untrusted code in a
privileged base-repository context.

Build logs, manifests, SBOMs, and provenance must not contain credentials,
private package-source tokens, signing material, or sensitive environment
values.

## 10. Provenance, Retention, and Audit

Every stable artifact and public edge build provides:

- SHA-256 checksums.
- A machine-readable SBOM in a documented standard format.
- Build provenance or an artifact attestation tying it to the source commit and
  workflow identity.
- A release manifest connecting files, packages, container digests, and
  documentation versions.

Stable releases, their manifests, checksums, provenance, and release notes are
retained indefinitely subject to legal requirements. Edge builds have a
documented retention policy, but the newest successful edge build and any build
referenced by an active investigation must remain available. Temporary preview
and CI artifacts expire automatically.

Workflow runs and deployment records provide an auditable history of actor,
event, commit, environment, artifacts, and destination. The project documents
how a user verifies checksums and provenance before installation.

## 11. Failure and Recovery

- CI failure blocks merge.
- Edge publication failure marks the `main` run unsuccessful but does not roll
  back source.
- Website deployment or smoke-test failure preserves or restores the last known
  good production deployment.
- A partial stable release stops further publication and reports exactly which
  immutable destinations succeeded. An authorized retry resumes with the same
  verified artifact set.
- A stable package already accepted by a registry is not overwritten or
  silently deleted. Recovery uses deprecation and a new patch version unless a
  security or legal process requires stronger action.
- A compromised credential is revoked or rotated before publication resumes.

Recovery procedures and destination-specific limitations are documented in
`RELEASE.md` before the first public release and exercised through a release
dry run.

## 12. Testing and Acceptance

Before public release, the delivery system must demonstrate:

- Required checks block an intentionally failing pull request.
- A pull request creates and then removes an isolated website preview.
- A merge to `main` publishes a commit-identifiable edge build and updates the
  production website.
- An unsigned or unprotected version reference cannot publish stable artifacts.
- A protected prerelease tag publishes only prerelease-labeled outputs.
- A protected stable tag publishes one consistent artifact set to every
  configured destination.
- NuGet publication obtains short-lived credentials without a stored API key.
- Fork pull requests cannot read or use deployment and publishing credentials.
- Re-running publication does not overwrite immutable artifacts or create
  inconsistent bytes for one version.
- Checksums, SBOMs, and provenance verify against downloaded artifacts.
- Website rollback restores a known-good version.
- Package and CLI smoke tests pass from public download locations in clean
  environments.

## 13. Rollout

1. Add local scripts and pinned toolchain configuration.
2. Add required pull-request CI and branch protection.
3. Add website build, preview, production deployment, and smoke tests.
4. Add release-shaped `main` builds and the public edge channel.
5. Add protected release environments, trusted publishing identities, artifact
   signing or attestation, and dry-run publication.
6. Publish a release candidate and verify installation from every destination.
7. Enable stable tag publication only after legal, support, security, and
   compatibility prerequisites are complete.

## 14. Open Questions

1. Which operating systems and architectures make up the supported CLI and
   container matrix?
2. Which static-site generator and documentation toolchain will build the
   website?
3. Which public storage mechanism backs the rolling edge download index and its
   retention policy?
4. Which SBOM, signing, and provenance standards are mandatory for v1?
5. What minimum scheduled-test coverage is necessary beyond the blocking pull
   request and release matrices?
