---
type: "concept"
title: "Release Versioning"
description: "Naming and numbering releases with semantic versioning so changes are understandable and comparable"
tags: ["versioning", "semver", "releases", "governance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Release Versioning

## Summary
Release versioning gives every build an identifiable version — typically semantic versioning (major.minor.patch) — so consumers can reason about compatibility and history. Versions are the language of deployment and rollback.

## Details
- SemVer: major breaks, minor adds compatibly, patch fixes — the contract is in the number.
- Pre-release and build metadata (rc, nightly) mark maturity.
- Versions must be immutable once published: never reuse or rewrite a released version.
- Open question: how to signal breaking changes in APIs and internal services.

## Related
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — versions are what canaries compare
- [[wiki/devops-infra/release-trains|Release Trains]] — assigning versions at departure
- [[wiki/devops-infra/changelog-practices|Changelog Practices]] — what changed between versions
- [[wiki/api-protocols/api-versioning|API Versioning]] — versioning the API surface
