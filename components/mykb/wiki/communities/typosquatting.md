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
- mykb relevance: the wiki's CI would install from lockfiles with hashes, blocking typosquats.

The attack works because installation commands are copy-pasted and package names are visually confusable, so defenses must make the verified name the path of least resistance: lockfiles pin exact versions with integrity hashes, package managers warn on name mismatches, and private registries act as an allowlist that filters the lookalike noise before developers ever see it, and lockfile hashes make the verified name verifiable without trusting human eyes.

Typo distance is the core metric — attackers exploit one-character, transposed, or hyphen-and-underscore variants of popular packages — so teams should monitor newly published names near their dependency set, treat hash-pinned installs as the default rather than the exception, and make supply-chain verification part of the review checklist for every new dependency, because a single unverified install is the entire attack surface, and the same discipline covers transitive dependencies, whose names are rarely inspected at all.

Detection gets harder when attackers use confusable Unicode characters or squat on names that differ in punctuation only, which is why hash pinning matters more than naming policy: even a perfect typo-blocker is worthless if the registry can be poisoned or the lockfile replaced, so the end-to-end guarantee comes from verifying the artifact against a trusted digest at install time and again at build time, so CI acts as the final checkpoint.

## Related
- [[wiki/communities/malicious-packages|Malicious Packages]]
- [[wiki/communities/supply-chain-attacks|Supply-Chain Attacks]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
