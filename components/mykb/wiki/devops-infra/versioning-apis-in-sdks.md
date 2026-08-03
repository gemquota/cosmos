---
type: "concept"
title: "Versioning APIs in SDKs"
description: "Coordinating library versions with the APIs they call"
tags: ["sdk", "versioning", "api", "clients"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Versioning APIs in SDKs

## Summary
Versioning APIs in SDKs is the client-side mirror of API compatibility: the SDK's own versioning, its support policy for server versions, and its breaking-change discipline determine whether consumers can upgrade safely. SDKs are how most developers consume an API, so SDK compatibility policy is API compatibility policy in practice.

## Details
- Mechanism: SDKs follow semver like any library — major for breaking API changes, minor for additions, patch for fixes; the SDK pins the API version it targets (base URL, path, schema); deprecation flows: the server marks fields deprecated, the SDK warns, then removes in a major release; release notes map SDK versions to server versions.
- Concrete example: an API adds pagination fields in v2; the SDK 3.0 targets the new default and keeps the old shape behind a compatibility flag; a server removes a field after two majors of deprecation; a consumer pinned to SDK 2.x still works until the server truly removes the field.
- Failure modes: SDK and server version skew — a new SDK against an old server (or vice versa) failing at runtime; breaking changes shipped as minor versions, breaking consumers without warning; SDKs that silently swallow unknown fields, hiding data loss; generated SDKs whose codegen changes types between releases; deprecated fields removed without the promised window.
- Tradeoffs: strict SDK versioning slows API evolution but keeps consumers upgradeable; the alternative — constantly breaking SDKs — fragments the consumer base; the mature pattern is additive changes within a major, a documented deprecation window, and automated compatibility tests between SDK and server.
- Operational notes: run SDK-server integration tests in CI, publish SDK changelogs, and track which SDK versions are in use.
- RSIS3 relevance: any SDK cosmos publishes for the wiki daemon API needs the same discipline — consumers (loops, scripts) must be able to upgrade without breakage; versioning the API contract separately from the implementation avoids surprise breakage.

## Related
- [[wiki/devops-infra/release-versioning|Release Versioning]]
