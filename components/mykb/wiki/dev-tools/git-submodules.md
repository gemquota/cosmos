---
type: "concept"
title: "Git Submodules"
description: "Embedding one git repository inside another at a pinned commit"
tags: ["git", "dependencies", "repos", "pinning"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Git Submodules

## Summary
Git submodules let a repository reference another repository at a specific commit. They keep nested projects versioned independently but add workflow friction: submodule state must be updated and committed deliberately.

## Details
- Operations like clone and branch-switch need `--recurse-submodules`; forgetting them leaves empty directories.
- Alternatives: vendoring, package managers, or workspace monorepos usually cause less pain.
- RSIS3 relevance: any embedded dependency of cosmos should weigh submodules against lockfiles.

## Related
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — the alternative to submodule composition
- [[wiki/dev-tools/lockfiles|Lockfiles]] — dependency pinning done at package level
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — pinned submodules fix dependency versions
- [[wiki/software-engineering/git-workflows|Git Workflows]] — submodules complicate every workflow step
- [[wiki/security/sbom|SBOM]] — submodules appear in the software bill of materials
