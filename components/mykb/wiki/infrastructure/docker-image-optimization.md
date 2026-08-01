---
type: "concept"
title: "Docker Image Optimization"
description: "Practices for shrinking container image size and build time: multi-stage builds, minimal bases, and layer caching"
tags: ["docker", "images", "buildkit", "devops", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.docker.com/build/building/best-practices/"]
---

# Docker Image Optimization

## Summary
Docker image optimization reduces image size and build time so pushes and pulls are fast, cold starts are cheap, and the attack surface stays small. The core techniques are multi-stage builds, minimal base images, and careful layer ordering so the build cache stays warm. Every layer saved also shrinks the supply-chain surface that scanners must review.

## Details
- Multi-stage builds compile or download artifacts in a heavy builder stage, then copy only the results into a slim runtime stage — the classic example is a Go or Node binary without the toolchain.
- Base image choice matters: distroless images remove shells and package managers, Alpine is tiny but uses musl, and full images are easiest to debug; pick per threat model.
- Layer caching: place rarely-changing instructions (dependency installs) before frequently-changing ones (source copies) so rebuilds reuse cache layers; BuildKit parallelizes independent stages.
- A .dockerignore file keeps build context small and prevents secrets or vendored artifacts from leaking into layers.
- Worked example: a Node service drops from ~1.1 GB to ~120 MB by switching from node:20 as a runtime base, copying package-lock.json first for cache hits, and running npm ci --omit=dev in a builder stage.
- Tooling: docker scout and dive report size, duplication, and vulnerability data per layer; signed, scanned images pair optimization with supply-chain checks.
- Optimization is a trade-off: minimal images complicate debugging, so keep a debug variant or sidecar for troubleshooting.

## Related
- [[wiki/infrastructure/container-scanning|Container Scanning]] — vulnerability review of slimmed-down images
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]] — where optimized images are stored and shared
- [[wiki/infrastructure/containerization|Containerization]] — the packaging model images are built for
- [[wiki/devops-infra/docker-compose|Docker Compose]] — local workflow that benefits from smaller images
- [[wiki/security/container-hardening|Container Hardening]] — runtime security for minimal images
- [[wiki/devops-infra/containerd|containerd]] — runs the optimized images in production
