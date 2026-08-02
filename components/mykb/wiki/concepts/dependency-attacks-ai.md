---
type: "concept"
title: "Dependency Attacks"
description: "Compromising AI systems through their dependencies"
tags: ["dependencies", "attacks", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dependency Attacks

## Summary
Dependency attacks exploit trusted libraries or services that AI systems rely on, from ML frameworks to vector stores.

## Details
- Dependency attacks exploit trusted libraries or services that AI systems rely on, from ML frameworks to vector stores.
- Typosquatting, version confusion, and hijacked maintainers are common vectors.
- Pinning, lockfiles, and dependency auditing are the defenses.
- RSIS3 relevance: the bundle's scripts import libraries; lockfiles and pins matter.

## Related
- [[wiki/concepts/package-attacks-ai|Package Attacks]] — the package vector
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the class
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — the upkeep
- [[wiki/concepts/dependency-attacks-ai|dependency-attacks-ai]] — note
- [[wiki/decisions/self-hosting|Self-Hosting]] — the full treatment of this theme
- [[wiki/devops-infra/supply-chain-attestations|Supply Chain Attestations]] — existing graph context
