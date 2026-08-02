---
type: "concept"
title: "Version Bumping"
description: "The rules for when a version number changes and by how much"
tags: ["versioning", "semver", "releases", "conventions"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Version Bumping

## Summary
Version bumping follows Semantic Versioning: MAJOR for breaking changes, MINOR for features, PATCH for fixes. Consistent rules make versions communicate compatibility to every consumer.

## Details
- Breaking changes demand a major bump and migration notes — never sneak them into minors.
- Pre-release labels (1.0.0-alpha.1) and build metadata (1.0.0+build.5) extend semver.
- Automate bumps (semantic-release, release-please) so humans stop deciding.
- mykb relevance: the wiki API and bundle versions bump per semver rules.

## Related
- [[wiki/communities/semantic-release|Semantic Release]]
- [[wiki/dev-tools/semver-tooling|Semver Tooling]]
- [[wiki/api-protocols/semver-for-apis|Semver for APIs]]
- [[wiki/communities/tag-strategies|Tag Strategies]]
- [[wiki/dev-tools/release-management|Release Management]]
