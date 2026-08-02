---
type: "concept"
title: "Semantic Release"
description: "Automating versioning and publishing from conventional commit messages"
tags: ["semantic-release", "versioning", "automation", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Semantic Release

## Summary
Semantic release derives the next version from commit messages — feat bumps minor, fix bumps patch, breaking bumps major — then tags, changelogs, and publishes automatically. It removes human version decisions and the errors they cause.

## Details
- Requires disciplined conventional commits; message quality becomes release correctness.
- Release branches and pre-release channels (alpha, beta) are supported via config.
- Automation needs a publish token and a clear rollback story for bad releases.
- mykb relevance: the wiki bundle versions itself from conventional commits on main.

## Related
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/dev-tools/conventional-commits|Conventional Commits]]
- [[wiki/communities/changelog-generation|Changelog Generation]]
- [[wiki/communities/version-bumping|Version Bumping]]
- [[wiki/dev-tools/release-management|Release Management]]
