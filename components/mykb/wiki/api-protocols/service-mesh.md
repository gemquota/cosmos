---
type: "concept"
title: "Service Mesh"
description: "Sidecar proxies, mTLS, and traffic policies"
tags: ["service-mesh", "sidecar", "mtls", "observability", "kubernetes"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://istio.io/latest/docs/concepts/what-is-istio/", "https://linkerd.io/2.16/overview/"]
---

# Service Mesh

## Summary
A service mesh inserts a sidecar proxy next to every service instance and routes all service-to-service traffic through it, enabling uniform mTLS, traffic policy, retries, and observability without changing application code. The data plane (proxies) takes orders from the control plane (configuration and certificates).

## Details
- Data plane: Envoy (Istio), Linkerd's rust-based proxy, or Consul Connect proxies intercept traffic via iptables or transparent interception.
- Control plane: Istiod, Linkerd controller, or Consul servers distribute routing rules, policies, and certificates to sidecars.
- mTLS everywhere: the mesh issues per-workload certificates and encrypts/authenticates east-west traffic automatically — the biggest single win.
- Traffic policies: retries, timeouts, circuit breakers, load balancing, and canary/percentage routing declared as CRDs or config.
- Observability: proxies emit golden signals (latency, traffic, errors, saturation) per service pair, feeding dashboards without app instrumentation.
- Costs: every hop adds a proxy (latency, CPU, memory), and the control plane is another system to operate; small deployments may not need it.
- Fits with: gRPC load balancing via xDS, API gateways for north-south, and Kubernetes for orchestration.

## Related
- [[wiki/api-protocols/mtls|mTLS]] — the transport security meshes automate
- [[wiki/api-protocols/grpc-load-balancing|gRPC Load Balancing]] — xDS clients integrate with mesh control planes
- [[wiki/devops-infra/istio|Istio]] — a concrete mesh implementation
- [[wiki/infrastructure/service-mesh|Service Mesh (Infra)]] — the infrastructure perspective
- [[wiki/api-protocols/retry-policies|Retry Policies]] — mesh-level retries move policies out of code
