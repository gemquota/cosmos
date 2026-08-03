---
type: "concept"
title: "API Mesh Patterns"
description: "Composing and routing APIs through gateways and mesh layers"
tags: ["api", "mesh", "gateway", "routing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# API Mesh Patterns

## Summary
API mesh patterns compose multiple API gateways and service-mesh layers so that north-south traffic (clients to services) and east-west traffic (service to service) each get the right policy, routing, and telemetry. The mesh is organized as layers: an edge gateway owns TLS, authentication, and perimeter rate limiting, while the service mesh handles mTLS, retries, and circuit breaking between workloads.

## Details
- Layering: the edge gateway terminates external TLS and applies WAF and rate limiting; domain gateways group APIs by business domain; the mesh data plane (sidecar or ambient) carries mTLS, retries, and observability labels east-west. Enforce each policy at exactly one layer to avoid double counting and conflicting timeouts.
- Composition examples: a mobile client hits the edge, which routes to a BFF gateway, which calls backend services through the mesh — edge owns tokens, BFF owns aggregation and fan-out, mesh owns per-service reliability. Another pattern is per-team gateways with a central control plane distributing shared route and policy config.
- Failure modes: TLS termination at two layers breaks certificate pinning and client-IP forwarding unless `X-Forwarded-*` headers are handled deliberately; overlapping retries (gateway plus mesh plus client) multiply load several-fold during an outage; route shadowing hides drift until production traffic reaches the wrong backend.
- Tradeoffs: a single hub gateway centralizes control but becomes a bottleneck and a blast-radius amplifier; fully distributed meshes scale better but make policy auditing and global change harder. Choose by team boundary — mesh per cluster, gateway per entry point — and reconcile both from one source of truth.
- Operational notes: keep routing tables in git, validate mesh config against a test cluster, and monitor gateway-to-mesh tail latency because each hop adds a percentile penalty.
- RSIS3 relevance: RSIS3 loops call internal services (the MyKB daemon, SPACE engine); explicit mesh boundaries and retry policies between components keep one degraded loop from flooding the others with retries.

## Related
- [[wiki/devops-infra/api-gateways|API Gateways]] — related coverage in the same cluster
- [[wiki/devops-infra/service-mesh-sidecars|Service Mesh Sidecars]] — related coverage in the same cluster
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]] — related coverage in the same cluster
- [[wiki/devops-infra/api-compatibility-policies|API Compatibility Policies]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
