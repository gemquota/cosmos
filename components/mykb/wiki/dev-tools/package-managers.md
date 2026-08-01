---
type: "concept"
title: "Package Managers"
description: "Tools that install, update, and resolve dependencies for a language or system"
tags: ["packages", "dependencies", "tooling", "ecosystem"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Package Managers

## Summary
Package managers automate dependency acquisition: npm/pnpm/yarn for JavaScript, pip/uv for Python, cargo for Rust, apt and Homebrew for systems. They resolve version graphs, install artifacts, and feed lockfiles.

## Details
- Registry trust is a security surface: typosquatting and tampering are real threats.
- Environment pinning (virtualenvs, containers) isolates what a manager installs.
- RSIS3 relevance: cosmos's Python toolchain relies on pip-level resolution for its daemons.

## Related
- [[wiki/dev-tools/lockfiles|Lockfiles]] — the resolution result package managers record
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — registries are part of the attack surface
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — managers must behave deterministically
- [[wiki/devops-infra/containerd|containerd]] — container images extend package discipline to systems
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — workspaces unify package management
