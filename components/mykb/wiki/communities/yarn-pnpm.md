---
type: "concept"
title: "Yarn/pnpm"
description: "Alternative Node package managers with different install strategies"
tags: ["yarn", "pnpm", "node", "packages"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Yarn/pnpm

## Summary
Yarn and pnpm are npm alternatives: Yarn (Berry) adds workspaces and plug-and-play; pnpm uses a content-addressed store with hard links, saving disk and preventing phantom dependencies. All three read the same package.json but differ in install strategy.

## Details
- pnpm's strict node_modules makes undeclared dependencies fail loudly — a correctness win.
- Workspaces (npm, Yarn, pnpm) manage monorepos with shared installs and scripts.
- Lockfile formats differ per manager — pick one and commit its lockfile.
- mykb relevance: the wiki's Node workspace uses pnpm for strict dependency isolation.

## Related
- [[wiki/communities/npm-practice|npm Practice]]
- [[wiki/dev-tools/monorepos|Monorepos]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/communities/dependency-graphs|Dependency Graphs]]
- [[wiki/dev-tools/package-management|Package Management]]
