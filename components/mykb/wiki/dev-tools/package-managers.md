---
type: "concept"
title: "Package Managers"
description: "Tools that install, update, and resolve dependencies for a language or system"
tags: ["packages", "dependencies", "tooling", "ecosystem"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Package Managers

## Summary
Package managers automate dependency acquisition: npm/pnpm/yarn for JavaScript, pip/uv for Python, cargo for Rust, apt and Homebrew for systems. They resolve version graphs, install artifacts, and produce lockfiles — the plumbing underneath every reproducible environment.

## Details
- Mechanism: the manager reads a manifest, resolves the dependency graph against registries, records the resolution in a lockfile, downloads and verifies artifacts (hashes, signatures), and installs into an environment; virtual environments (venv, conda) and containers isolate what a manager installs; updates flow through the manager's resolution, never raw downloads.
- Concrete example: uv resolves pyproject.toml into uv.lock and installs into a venv; npm workspaces manage a monorepo with one lockfile; apt resolves system packages with dependency metadata; a CI pipeline installs from lockfiles for byte-identical environments.
- Failure modes: registry trust — typosquatting and tampered packages are real (pin hashes, use private mirrors, verify signatures); resolution non-determinism when lockfiles are absent; environment pollution when installs are global rather than isolated; conflicting transitive versions in the same environment; supply-chain incidents arriving via a compromised package.
- Tradeoffs: managers trade registry convenience and abstraction for a trust surface and resolution complexity; the alternative — vendoring or manual installs — is explicit and painful; the mature pattern is lockfiles, isolation, hashing, and scanning the locked tree.
- Operational notes: commit lockfiles, scan dependencies, pin the manager version, and keep registries mirrored or verified.
- RSIS3 relevance: cosmos's Python toolchain relies on pip-level resolution for its daemons — the same lockfile-and-scan discipline keeps loop runs reproducible.

- Prefer the package manager's own update flow over manual edits so the lockfile and manifest never disagree.
## Related
- [[wiki/dev-tools/lockfiles|Lockfiles]] — the resolution result package managers record
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — registries are part of the attack surface
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — managers must behave deterministically
- [[wiki/devops-infra/containerd|containerd]] — container images extend package discipline to systems
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — workspaces unify package management
