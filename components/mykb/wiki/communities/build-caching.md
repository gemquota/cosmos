---
type: "concept"
title: "Build Caching"
description: "Reusing build outputs across runs to make builds fast"
tags: ["build-caching", "builds", "performance", "ci"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Build Caching

## Summary
Build caching stores intermediate results — compiled objects, downloaded deps, layer outputs — so unchanged inputs skip recomputation. Good caching turns a 30-minute build into a 2-minute one and makes iteration fast.

## Details
- Cache granularity matters: content-addressed caches (Bazel, Nix) hit more often than path-based ones.
- Docker layer caching works when layer inputs are stable — order dependency installs first.
- CI caches (actions/cache, remote build caches) survive across machines.
- mykb relevance: wiki builds cache the markdown toolchain and dependency layers.

## Related
- [[wiki/communities/multi-stage-builds|Multi-Stage Builds]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
- [[wiki/communities/bazel-practice|Bazel Practice]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/devops-infra/build-caching-and-artifacts|Build Caching and Artifacts]]
