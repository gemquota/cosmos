---
type: "concept"
title: "SemVer for APIs"
description: "Applying semantic versioning to API releases"
tags: ["semver", "versioning", "api-design", "releases", "compatibility"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://semver.org/", "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#versioning-a-restful-web-api"]
---

# SemVer for APIs

## Summary
Semantic Versioning (MAJOR.MINOR.PATCH) encodes compatibility in the version number: major breaks, minor adds backward-compatible features, patch fixes without changing the contract. Applied to APIs, it tells consumers whether they can upgrade without touching code — but only if the breaking-change definition is actually enforced.

## Details
- The rules: MAJOR changes when incompatible API changes ship; MINOR adds functionality backward-compatibly; PATCH ships backward-compatible fixes.
- API specifics: a schema field added with a default is minor; a field removed, renamed, or made required is major; a bugfix that changes response semantics is a major unless documented as a correction.
- Versioning placement: the version appears in the URL path (/v2/users) or media type (application/vnd.api+json;version=2), never silently in the body.
- Pre-1.0: 0.x treats minor as potentially breaking — communicate this so consumers know 0.9 -> 0.10 may break.
- Contracts matter: SemVer only works if the machine-readable contract (OpenAPI, protobuf, GraphQL SDL) is diffed in CI to catch accidental breaks.
- Communication: breaking versions ship with changelogs, migration guides, and deprecation headers so consumers can plan.
- Tools: semantic-release automates version bumps from commit conventions; API lint rules flag incompatible diffs.

## Related
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — the rules SemVer encodes
- [[wiki/api-protocols/api-deprecation|API Deprecation]] — what happens before a breaking major
- [[wiki/api-protocols/media-type-versioning|Media Type Versioning]] — versioning the representation instead of the path
- [[wiki/api-protocols/api-design-first|Design-First APIs]] — specs make SemVer checks mechanical
- [[wiki/devops-infra/release-versioning|Release Versioning]] — applying SemVer across services
