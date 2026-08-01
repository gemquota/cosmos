---
type: "concept"
title: "Istio"
description: "Service mesh providing mTLS, traffic routing, observability, and policy for Kubernetes"
tags: ["istio", "service-mesh", "kubernetes", "security", "traffic"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Istio

## Summary
Istio is a Kubernetes service mesh that injects Envoy sidecars to handle service-to-service traffic: mutual TLS, circuit breaking, retries, telemetry, and authorization policies.

## Details
- Sidecar proxies intercept all pod traffic; control plane (istiod) distributes config.
- mTLS encrypts and authenticates mesh traffic, supporting zero-trust segmentation.
- Add weight-based routing and fault injection for canary releases and chaos tests.

## Related
- [[wiki/devops-infra/envoy|Envoy]] — the sidecar proxy underneath
- [[wiki/security/zero-trust|Zero Trust Architecture]] — mTLS and policy enforcement
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — mesh-level resilience
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the platform Istio extends
- [[wiki/devops-infra/observability|Observability]] — mesh telemetry
