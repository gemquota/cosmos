---
type: "concept"
title: "Polyrepo Strategy"
description: "Separate repositories per project, each with its own history and tooling"
tags: ["polyrepo", "repository", "strategy", "isolation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Repository_(version_control)", "https://en.wikipedia.org/wiki/Monorepo"]
---

# Polyrepo Strategy

## Summary
A polyrepo strategy keeps each project in its own repository with independent history, CI, and access control. It suits independent teams and bounded blast radius; its costs are cross-repo coordination and dependency versioning drift.

## Details
- Isolation is the payoff: permissions, release cadence, and failure blast radius are per-repository.
- Cross-repo changes become sequenced PRs with version bumps and migration windows.
- Dependency drift is the tax: shared libraries must be versioned, published, and updated everywhere.
- Tooling bridges the gaps: release automation, dependency bots, and contract tests between repos.
- The pragmatic hybrid: monorepo per domain, polyrepo between domains.
- For the mykb bundle, wiki content and its tooling could split repos — content publishes independently of tooling versions.

Worked example — the wiki splits three repos: content, build tooling, and the reading app. A link-format change bumps the tooling version, the content repo updates its pin, and the app consumes the published bundle.

## Related
- [[wiki/dev-tools/monorepos|Monorepos]]
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/dev-tools/release-management|Release Management]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/software-engineering/code-ownership|Code Ownership]]
