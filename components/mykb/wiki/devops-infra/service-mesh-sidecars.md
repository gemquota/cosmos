---
type: "concept"
title: "Service Mesh Sidecars"
description: "Proxies injected beside workloads for mesh features"
tags: ["service-mesh", "sidecar", "proxy", "istio"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://istio.io/latest/docs/concepts/what-is-istio/",
  "https://linkerd.io/2.15/overview/",
]
---

# Service Mesh Sidecars

## Summary
Service meshes inject sidecar proxies beside workloads to provide mTLS, traffic policy, and telemetry without changing application code. The sidecar becomes the network gateway for each pod. Meshes shift networking control from infrastructure to application-level policy.

## Details
- Istio's data plane runs Envoy proxies as sidecars, with a control plane distributing configuration to every proxy.
- Linkerd takes a lightweight, Kubernetes-native approach focused on simplicity.
- Sidecars intercept all pod traffic, enabling mTLS between services and fine-grained routing.
- Observability is a core payoff: golden metrics and traces come from the mesh automatically.
- Costs include proxy overhead, extra pod resource usage, and configuration complexity that teams must budget for.
- In mykb, meshes connect to Envoy, network policies, zero-trust, and service accounts.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/service-meshes-istio-linkerd|Service Meshes: Istio & Linkerd]]
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/infrastructure/service-mesh|Service Mesh]]
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
