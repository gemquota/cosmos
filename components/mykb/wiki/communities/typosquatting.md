---
type: "concept"
title: "Typosquatting"
description: "Malicious packages named to look like popular ones"
tags: ["typosquatting", "security", "packages", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Typosquatting

## Summary
Typosquatting publishes packages with names one typo away from popular ones — requets instead of requests, python3-dateutil variations — hoping a developer's typo installs malware. It is one of the oldest and most effective package-supply-chain tricks.

## Details
- Attackers publish quickly after a legit package spikes; lookalike names and confusable characters abound.
- Defenses: verify package names, use lockfiles, pin exact versions with hashes.
- Private registries and proxy registries (Artifactory, Verdaccio) filter the lookalike noise.
- mykb relevance: the wiki's CI installs from lockfiles with hashes, blocking typosquats.

## Related
- [[wiki/communities/malicious-packages|Malicious Packages]]
- [[wiki/communities/supply-chain-attacks|Supply-Chain Attacks]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
