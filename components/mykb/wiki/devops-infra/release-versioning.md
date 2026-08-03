---
type: "concept"
title: "Release Versioning"
description: "Naming and numbering releases with semantic versioning so changes are understandable and comparable"
tags: ["versioning", "semver", "releases", "governance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Release Versioning

## Summary
Release versioning gives every build an identifiable version — typically semantic versioning (major.minor.patch) — so consumers can reason about compatibility, history, and rollback. Versions are the language of deployment: canaries compare them, changelogs describe them, and rollback targets them.

## Details
- SemVer contract: major bumps break compatibility, minor adds compatibly, patch fixes bugs; the number itself communicates risk to consumers; pre-release suffixes (rc, alpha, nightly) mark maturity; build metadata disambiguates identical versions.
- Mechanics: versions are assigned at release time from commit history (semantic-release, release-please), stamped into artifacts (image tags, package versions, binaries), and recorded in provenance; versions must be immutable once published — never reuse or rewrite a released version, because consumers and rollback targets depend on stability.
- Concrete example: 2.1.0 adds a feature compatibly; 3.0.0 removes an API and triggers the compatibility policy; a nightly build is tagged 2.2.0-dev.20260803; a rollback deploys the previous immutable tag; SBOMs and signatures are bound to the exact version.
- Failure modes: version reuse (retagging a released version corrupts history and rollback); version inflation where every change bumps major, destroying the signal; semantic drift — breaking changes shipped as minor; versioning that exists in one system but not others (image tag and chart version disagree); human-assigned versions colliding under automation.
- Tradeoffs: strict versioning costs process but makes compatibility explicit and rollback precise; loose versioning (floating tags) is simpler and uninformative — you cannot know what you are running; the mature pattern is machine-assigned semver plus immutable published artifacts.
- Operational notes: automate version assignment, verify artifact-version consistency in CI, and audit that released versions are never mutated.
- RSIS3 relevance: RSIS3 versions its own parameters and protocols — semver discipline makes loop-evolution history legible and rollback of a parameter change precise.

## Related
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — versions are what canaries compare
- [[wiki/devops-infra/release-trains|Release Trains]] — assigning versions at departure
- [[wiki/devops-infra/changelog-practices|Changelog Practices]] — what changed between versions
- [[wiki/api-protocols/api-versioning|API Versioning]] — versioning the API surface
