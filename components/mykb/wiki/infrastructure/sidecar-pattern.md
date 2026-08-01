---
type: "concept"
title: "Sidecar Pattern"
description: "Co-locating helper containers with a main container to extend it without changing its code"
tags: ["sidecar", "pattern", "containers", "kubernetes"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Sidecar Pattern

## Summary
The sidecar pattern runs a helper container in the same pod as the main container to add capabilities — logging, proxying, secrets refresh — without touching application code.

## Details
- Sidecars share the pod network and filesystem, so they can intercept traffic and read/write local state.
- Uses: log shippers, TLS terminators, config/secret reloaders, and mesh proxies.
- Cost: extra resources per pod and one more thing to version and upgrade.
- Open question: when a sidecar should become a separate service instead.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — the pattern at platform scale
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]] — the proxy-specific variant
- [[wiki/infrastructure/containerization|Containerization]] — pods host multiple containers
- [[wiki/devops-infra/envoy|Envoy]] — the classic sidecar proxy
