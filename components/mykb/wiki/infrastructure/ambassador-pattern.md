---
type: "concept"
title: "Ambassador Pattern"
description: "A sidecar proxy that fronts a container as the single entry point for outbound traffic"
tags: ["ambassador", "sidecar", "proxy", "pattern"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Ambassador Pattern

## Summary
The ambassador pattern places a proxy container in front of an application container to handle all its external communication — retries, TLS, circuit breaking, and discovery.

## Details
- Apps get a uniform, language-agnostic network stack: retries, timeouts, and mTLS are policy, not code.
- Ambassadors enable per-service egress control and canary-friendly egress routing.
- Configuration lives with the service (sidecar config), not in a central proxy.
- Open question: how ambassador policy should be managed at fleet scale.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — composes into a service mesh
- [[wiki/infrastructure/sidecar-pattern|Sidecar Pattern]] — the container pattern it uses
- [[wiki/devops-infra/envoy|Envoy]] — commonly deployed as a proxy
- [[wiki/devops-infra/kubernetes|Kubernetes]] — pods host the ambassador
