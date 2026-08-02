---
type: "concept"
title: "Supply-Chain Attacks"
description: "Attacks that compromise software through its dependencies or build pipeline"
tags: ["supply-chain", "security", "attacks", "dependencies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Supply-Chain Attacks

## Summary
Supply-chain attacks inject malicious code through the paths software trusts: dependency names, build servers, registries, or maintainer accounts. The 2024 xz-utils backdoor and many typosquatting campaigns show how one compromised link ripples everywhere.

## Details
- Attack surfaces: malicious packages, account takeover, compromised build machines, mirror poisoning.
- Defenses: pinning, hashes, signatures, provenance attestations, scanning, and least privilege.
- The blast radius is transitive — your dependency's dependency can ship the payload.
- mykb relevance: the wiki treats every dependency as a trust boundary with pinned, signed artifacts.

## Related
- [[wiki/communities/typosquatting|Typosquatting]]
- [[wiki/communities/malicious-packages|Malicious Packages]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
