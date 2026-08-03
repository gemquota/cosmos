---
type: "concept"
title: "Dependency Attacks"
description: "Compromising AI systems through their dependencies"
tags: ["dependencies", "attacks", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dependency Attacks

## Summary
Dependency attacks exploit trusted libraries or services that AI systems rely on, from ML frameworks to vector stores. They are supply-chain attacks aimed at the dependency graph: compromise a package the system imports, and you inherit code execution inside the system's trust boundary without touching the system's own code.

## Details
- The attack surface is huge because AI systems stack many layers of dependencies: base images and operating-system packages, Python and Node package registries, ML frameworks and model-serving runtimes, embedding and vector-store clients, and the data pipelines that feed training and retrieval. Any of these can be the entry point, and the compromise is usually silent — the malicious code does its work during a routine install or import.
- Typosquatting, version confusion, and hijacked maintainers are common vectors. Typosquatting registers a package with a name one character off from a popular library and hopes for a mistyped install; version confusion publishes a malicious package at a version number higher than the legitimate one so naive resolvers prefer it; maintainer hijack (credential theft, social engineering, or a takeover of the account) lets an attacker ship a poisoned update to every existing user. The SolarWinds and event-stream incidents are the canonical real-world precedents for how far a single compromised dependency propagates.
- Pinning, lockfiles, and dependency auditing are the defenses. Exact-version pins with hashes stop resolution-based attacks; lockfiles make installs reproducible so a drift cannot silently introduce a new package; and auditing tools (pip-audit, npm audit, OSV scanning, signature verification) catch known-vulnerable or unexpected packages. The operational tradeoff is freshness versus determinism: strict pinning blocks malicious updates but also blocks legitimate security fixes, so the mitigation is a reviewable upgrade process rather than "never upgrade".
- RSIS3 relevance: the bundle's scripts import libraries; lockfiles and pins matter. An RSIS3 loop that runs code from installed packages is only as trustworthy as those packages, and a compromise of a retrieval or analysis dependency would let an attacker inject content into the system's memory and improvement cycles.

## Related
- [[wiki/concepts/package-attacks-ai|Package Attacks]] — the package vector
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the class
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — the upkeep
- [[wiki/decisions/self-hosting|Self-Hosting]]
- [[wiki/devops-infra/supply-chain-attestations|Supply Chain Attestations]]
