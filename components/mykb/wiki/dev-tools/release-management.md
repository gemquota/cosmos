---
type: "concept"
title: "Release Management"
description: "The process of planning, building, and shipping versions of software"
tags: ["release-management", "versions", "process", "shipping"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Release_management", "https://en.wikipedia.org/wiki/Software_release_life_cycle"]
---

# Release Management

## Summary
Release management owns the path from merged code to shipped version: versioning, changelogs, artifact production, environment promotion, and rollback plans. Its goal is boring, repeatable releases where the process is the safety net.

## Details
- Versioning (semver) communicates compatibility; changelogs communicate what changed and why it matters.
- Artifacts are immutable: each version is built once, signed, and stored — never rebuilt or overwritten.
- Promotion moves artifacts through environments (staging, canary, production) with gates at each step.
- Release trains and calendar cadence reduce coordination cost; on-demand releases suit CD teams.
- The rollback plan is part of the release, not an afterthought — know how to undo before you ship.
- For the mykb bundle, release management produces the versioned wiki bundle with a changelog and verified sources.

Worked example — a wiki release: semantic-release bumps 2.4.1, generates the changelog, tags the commit, builds the bundle, and promotes it to staging; QA approves and promotion to production happens with a one-click rollback.

## Related
- [[wiki/communities/version-bumping|Version Bumping]]
- [[wiki/communities/semantic-release|Semantic Release]]
- [[wiki/communities/changelog-generation|Changelog Generation]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/tooling/environment-management|Environment Management]]
- [[wiki/communities/tag-strategies|Tag Strategies]]
- [[wiki/communities/image-tagging|Image Tagging]]
- [[wiki/dev-tools/semver-tooling|Semver Tooling]]
- [[wiki/dev-tools/conventional-commits|Conventional Commits]]
