---
type: "concept"
title: "Package Attacks"
description: "Malicious or hijacked packages in AI toolchains"
tags: ["packages", "attacks", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Package Attacks

## Summary
Package attacks plant malicious code in package registries, often via typosquatting or account hijacking.

## Details
- Package attacks plant malicious code in package registries, often via typosquatting or account hijacking.
- AI toolchains pull hundreds of packages, widening the attack surface.
- Defenses: lockfiles, signature verification, and minimal dependencies.
- RSIS3 relevance: the bundle's Python tooling should pin and review its packages.

## Related
- [[wiki/concepts/dependency-attacks-ai|Dependency Attacks]] — the broader vector
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the class
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — the update discipline
- [[wiki/decisions/auto-update-mechanisms|Auto-Update Mechanisms]] — the delivery channel
- [[wiki/devops-infra/supply-chain-attestations|Supply Chain Attestations]] — existing graph context
