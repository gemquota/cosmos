---
type: "concept"
title: "Service Mesh"
description: "Dedicated infrastructure layer for service-to-service traffic: mTLS, routing, retries, and telemetry via sidecar proxies"
tags: ["service-mesh", "istio", "envoy", "mTLS", "microservices"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://istio.io/latest/docs/concepts/what-is-istio/"]
---

# Service Mesh

## Summary
A service mesh inserts a dedicated layer between services to handle communication concerns — mutual TLS, traffic routing, retries, circuit breaking, and telemetry — without changing application code. It works by injecting a sidecar proxy next to every workload and centralizing policy in a control plane. Meshes make canary routing and encrypted east-west traffic practical at scale.

## Details
- Two planes: the data plane is the set of sidecar proxies (typically Envoy) that intercept and forward traffic; the control plane (Istiod, Linkerd control plane) distributes configuration and certificates.
- Core features: automatic mTLS between services, fine-grained traffic splitting for canaries, retry and timeout policies, circuit breakers, and per-service telemetry that feeds tracing systems.
- Traffic model: VirtualService and DestinationRule abstractions in Istio let operators split traffic by header, weight, or subset without redeploying.
- Costs: added latency per hop, extra memory and CPU per pod, and real operational complexity; a mesh is often overkill for a handful of services.
- Comparison: Istio is feature-rich and Envoy-based; Linkerd is lighter, Rust-based, and simpler; both implement the sidecar data-plane model.
- The mesh complements, rather than replaces, application-level retries and observability: it enforces policy, but application code still owns business semantics.
- For mykb, a mesh is relevant when many internal services (daemon, hub, dashboard) need uniform mTLS and routing without per-service TLS code.

## Related
- [[wiki/infrastructure/sidecar-pattern|Sidecar Pattern]] — deployment pattern the mesh data plane uses
- [[wiki/infrastructure/circuit-breaker-pattern|Circuit Breaker Pattern]] — failure isolation enforced by the mesh
- [[wiki/infrastructure/network-policy|Network Policy]] — L3/L4 complement to mesh-level L7 policy
- [[wiki/devops-infra/istio|Istio]] — reference mesh implementation
- [[wiki/devops-infra/envoy|Envoy]] — the proxy at the heart of the data plane
- [[wiki/security/tls|TLS]] — underpins mesh mTLS
