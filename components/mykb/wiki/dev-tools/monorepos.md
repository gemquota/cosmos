---
type: "concept"
title: "Monorepos"
description: "One repository holding many projects with shared tooling"
tags: ["monorepo", "repository", "tooling", "collaboration"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Monorepo", "https://en.wikipedia.org/wiki/Repository_(version_control)"]
---

# Monorepos

## Summary
A monorepo keeps all projects in one repository, sharing history, tooling, and atomic cross-project changes. It simplifies refactoring and dependency coherence at the cost of scale problems that need serious tooling (Bazel, Nx, Turborepo, pnpm workspaces).

## Details
- Atomic changes across projects are the killer feature: a schema change ships with its consumers in one commit.
- Shared tooling and code reuse lower duplication; one CI config can enforce repo-wide standards.
- Scale challenges: checkout size, CI cost, and access control — tooling and build caching mitigate them.
- Ownership still needs structure: CODEOWNERS and per-area review keep large monorepos navigable.
- Monorepos suit organizations with many interdependent projects; polyrepos suit independent teams with few shared changes.
- For the mykb bundle, a monorepo holds wiki content plus the tooling that builds it, so content and validator changes stay atomic.

Worked example — a frontmatter spec change in the wiki monorepo updates the validator, three templates, and a test in one commit; CI runs all affected checks before merge.

## Related
- [[wiki/dev-tools/polyrepo-strategy|Polyrepo Strategy]]
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]]
- [[wiki/communities/build-caching|Build Caching]]
- [[wiki/software-engineering/code-ownership|Code Ownership]]
- [[wiki/communities/bazel-practice|Bazel Practice]]
- [[wiki/communities/yarn-pnpm|Yarn/pnpm]]
