---
type: "concept"
title: "Package Pinning"
description: "Fixing dependency versions so installs are reproducible"
tags: ["package-pinning", "dependencies", "reproducibility", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Package Pinning

## Summary
Package pinning fixes exact versions (and ideally hashes) so every install produces the same dependency set. Lockfiles pin transitively; pinning without a lockfile pins only the direct dependencies — the common gap.

## Details
- Pin exact versions plus integrity hashes where the ecosystem supports it (npm, pypi via hash files).
- Lockfiles are the practical pin: they record the resolved graph, not just the declared ranges.
- Pinning is a baseline, not a freeze: pair it with an update cadence (Renovate/Dependabot).
- mykb relevance: the wiki commits lockfiles and pins container digests.

## Related
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/communities/checksums|Checksums]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
