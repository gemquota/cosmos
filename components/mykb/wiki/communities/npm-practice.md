---
type: "concept"
title: "npm Practice"
description: "Node.js package management: publishing, installing, and locking dependencies"
tags: ["npm", "node", "packages", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# npm Practice

## Summary
npm practice covers the commands and conventions of the Node ecosystem — package.json metadata, semver ranges, package-lock.json integrity, publishing, and scoped packages. Discipline around lockfiles and scripts keeps projects reproducible.

## Details
- Commit package-lock.json and install with npm ci for reproducible builds.
- Understand semver ranges: ^ and ~ mean different update risks; pin when stability matters.
- Publishing is permanent on npm — test twice, publish once, and prefer canary tags.
- mykb relevance: wiki tooling uses npm with a committed lockfile and CI installs.

## Related
- [[wiki/communities/yarn-pnpm|Yarn/pnpm]]
- [[wiki/dev-tools/package-management|Package Management]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/communities/package-pinning|Package Pinning]]
