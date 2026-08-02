---
type: "concept"
title: "Changelog Generation"
description: "Building release notes automatically from commit history"
tags: ["changelog", "releases", "automation", "documentation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Changelog Generation

## Summary
Changelog generation turns structured commit history into release notes — grouped by type (features, fixes, breaking), attributed, and linked to issues. Conventional Commits plus tools like git-cliff or release-please make it automatic.

## Details
- Changelogs are for humans: group by user impact, not by internal scope.
- Auto-generated notes need review — mark the important changes for each release.
- Keep a manual overrides channel for changes that do not map to commits.
- mykb relevance: the wiki changelog groups curation fixes and feature additions per release.

## Related
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/communities/semantic-release|Semantic Release]]
- [[wiki/communities/version-bumping|Version Bumping]]
- [[wiki/devops-infra/changelog-automation|Changelog Automation]]
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]]
