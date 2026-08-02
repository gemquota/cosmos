---
type: "concept"
title: "Supply-Chain Attacks on AI"
description: "Compromising AI systems via their dependencies"
tags: ["supply-chain", "attacks", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Supply-Chain Attacks on AI

## Summary
Supply-chain attacks on AI compromise models, libraries, datasets, or toolchains before they reach the victim.

## Details
- Supply-chain attacks on AI compromise models, libraries, datasets, or toolchains before they reach the victim.
- AI-specific vectors include malicious model weights, poisoned datasets, and compromised training code.
- Defenses: provenance, pinning, SBOMs, and reproducible builds.
- RSIS3 relevance: the bundle's scripts and generated content are part of its own supply chain.

## Related
- [[wiki/concepts/dependency-attacks-ai|Dependency Attacks]] — the dependency vector
- [[wiki/concepts/package-attacks-ai|Package Attacks]] — the package vector
- [[wiki/concepts/model-tampering|Model Tampering]] — the model vector
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — note
- [[wiki/decisions/self-hosting|Self-Hosting]] — the full treatment of this theme
