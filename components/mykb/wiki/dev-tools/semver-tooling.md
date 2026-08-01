---
type: "concept"
title: "Semver Tooling"
description: "Tools and practices for applying Semantic Versioning to packages, releases, and dependencies"
tags: ["semver", "versioning", "releases", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Semver Tooling

## Summary
Semantic Versioning (MAJOR.MINOR.PATCH) encodes compatibility: breaking changes bump major, features bump minor, fixes bump patch. Semver tooling automates bumping, changelog generation, and dependency constraint checking.

## Details
- Automation ranges from commit-convention-driven release tools to `npm version` and `cargo release`.
- Dependency resolution trusts semver ranges; that trust is why precise versioning matters.
- RSIS3 relevance: wiki article status (stub vs growing) is a semver-like signal.

## Related
- [[wiki/dev-tools/conventional-commits|Conventional Commits]] — commit types drive automated version bumps
- [[wiki/dev-tools/lockfiles|Lockfiles]] — lockfiles pin resolved versions under ranges
- [[wiki/api-protocols/api-versioning|API Versioning]] — APIs need semver-style compatibility contracts
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — version trust is a supply-chain question
- [[wiki/software-engineering/git-workflows|Git Workflows]] — release discipline lives inside the workflow
