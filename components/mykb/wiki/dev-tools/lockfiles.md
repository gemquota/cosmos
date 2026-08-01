---
type: "concept"
title: "Lockfiles"
description: "Files that pin the exact resolved versions of a dependency tree for reproducible installs"
tags: ["dependencies", "reproducibility", "packages", "pinning"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Lockfiles

## Summary
A lockfile records the exact versions of every package in a dependency tree, so `install` produces the same tree everywhere and every time. It is the practical foundation of reproducible builds and audits.

## Details
- Generate and commit it; update deliberately with `update` commands, not fresh installs.
- Lockfiles enable offline installs and vulnerability scanning of the actual tree.
- RSIS3 relevance: the wiki's generated JSON indexes play the lockfile role for knowledge.

## Related
- [[wiki/dev-tools/package-managers|Package Managers]] — lockfiles are the package manager's record
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — pinned trees are a reproducibility prerequisite
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — scanning the locked tree finds known CVEs
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — workspaces share one lockfile per repo
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — CI installs from the lockfile
