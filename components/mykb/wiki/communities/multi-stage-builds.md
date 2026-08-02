---
type: "concept"
title: "Multi-Stage Builds"
description: "Docker builds that compile in one stage and ship only artifacts in another"
tags: ["docker", "builds", "containers", "images"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Multi-Stage Builds

## Summary
Multi-stage Dockerfiles use several FROM stages: a heavy toolchain stage compiles, a slim runtime stage copies only the artifacts. The final image excludes compilers, caches, and source — smaller and less attackable.

## Details
- Each FROM starts fresh; COPY --from=stage brings just what the runtime needs.
- Smaller images mean faster pulls, less disk, and fewer CVEs in the scan.
- Cache stages deliberately: layer order determines what invalidates on change.
- mykb relevance: the wiki image compiles markdown tooling in stage one and ships the binary only.

## Related
- [[wiki/communities/base-image-management|Base Image Management]]
- [[wiki/communities/build-caching|Build Caching]]
- [[wiki/tooling/containerization-practice|Containerization Practice]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
