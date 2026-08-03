---
type: "concept"
title: "Lockfiles"
description: "Files that pin the exact resolved versions of a dependency tree for reproducible installs"
tags: ["dependencies", "reproducibility", "packages", "pinning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Lockfiles

## Summary
A lockfile records the exact versions of every package in a dependency tree, so install produces the same tree everywhere and every time. It is the practical foundation of reproducible builds, offline installs, and vulnerability scanning of the actual dependency set.

## Details
- Mechanism: the package manager resolves the manifest (package.json, pyproject.toml) against the registry, records the full resolution — versions, hashes, transitive dependencies — in a lockfile (package-lock.json, uv.lock, Cargo.lock); installs read the lockfile directly, bypassing re-resolution; updates happen deliberately through the manager's update commands, never by deleting the lockfile and re-installing.
- Concrete example: CI installs from the committed lockfile, so the build is identical to the developer's machine; a security scan reads the lockfile to find known CVEs in the actual tree; an offline build works from the locked set; a dependency update is a reviewed PR that changes the lockfile.
- Failure modes: lockfiles not committed, so every install re-resolves and drifts; lockfiles updated by fresh installs instead of deliberate updates, silently changing the tree; stale lockfiles conflicting with a changed manifest; platform-specific entries (optional native deps) breaking cross-platform installs; lockfile churn from noisy tools making reviews impossible.
- Tradeoffs: lockfiles trade resolution convenience for determinism — the alternative, range-based resolution, is simpler and always drifting; the payoff is that the same code produces the same tree in dev, CI, and production.
- Operational notes: commit lockfiles, review lockfile changes like code, and scan the locked tree in CI.
- RSIS3 relevance: the wiki's generated JSON indexes play the lockfile role for knowledge — a pinned, verifiable record of what the graph contains.

## Related
- [[wiki/dev-tools/package-managers|Package Managers]] — lockfiles are the package manager's record
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — pinned trees are a reproducibility prerequisite
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — scanning the locked tree finds known CVEs
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — workspaces share one lockfile per repo
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — CI installs from the lockfile
