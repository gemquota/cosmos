---
type: "concept"
title: "Hermetic Builds"
description: "Builds that depend only on pinned inputs and produce reproducible outputs"
tags: ["hermetic-builds", "reproducibility", "builds", "supply-chain"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hermetic Builds

## Summary
Hermetic builds isolate compilation from the ambient environment — pinned toolchains, vendored or content-addressed deps, no network, no timestamps — so the same inputs yield the same binary anywhere. They are the foundation of reproducible and trustworthy releases.

## Details
- Fix toolchain versions, dependency hashes, and build flags; disable network access during build.
- Reproducibility pays off in caching, debugging, and supply-chain verification (reproducible attestations).
- Nix and Bazel are the strongest hermetic build systems; lockfiles approximate it elsewhere.
- mykb relevance: wiki bundle builds are hermetic so any machine reproduces the same archive.

## Related
- [[wiki/communities/nix-practice|Nix Practice]]
- [[wiki/communities/bazel-practice|Bazel Practice]]
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/communities/checksums|Checksums]]
