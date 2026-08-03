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
- pnpm's content-addressed store is shared across projects: hard links make installs fast and disk-light, while the strict node_modules layout prevents the phantom dependencies that TypeScript and bundlers might otherwise resolve.
- The lockfile is the reproducibility contract: commit it, install from it in CI, and treat updates as reviewed changes rather than incidental side effects.
- Workspaces manage monorepos with a single lockfile, shared scripts, and filtered commands, which keeps dependency versions consistent across packages.
- Plug-and-play in Yarn Berry removes node_modules at runtime, trading disk and speed for stricter resolution and a different debugging model.
- Install scripts are a supply-chain surface: pnpm ignores lifecycle scripts from dependencies by default unless explicitly allowed, which reduces the attack surface of a fresh checkout.
- Hard links mean a shared store must be treated as immutable: never edit files inside node_modules directly, because changes would leak across every project that links the same store entry.
- Registry configuration matters too: a pinned registry URL and strict engines checks keep installs reproducible across machines and prevent accidental use of a different package source.
- Migration costs are real: switching managers rewrites lockfiles and changes CI, so the decision should be made once, documented, and revisited only when the current manager blocks a needed workflow.
- mykb relevance: the wiki's Node workspace would use pnpm for strict dependency isolation.

## Related
- [[wiki/communities/npm-practice|npm Practice]]
- [[wiki/dev-tools/monorepos|Monorepos]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/communities/dependency-graphs|Dependency Graphs]]
- [[wiki/dev-tools/package-management|Package Management]]
