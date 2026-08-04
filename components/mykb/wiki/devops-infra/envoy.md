---
type: "entity"
title: "Envoy"
description: "High-performance L4/L7 proxy used for service mesh data planes, gateways, and edge routing"
tags: ["envoy", "proxy", "service-mesh", "networking", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Envoy

## Summary
Envoy is a CNCF proxy originally built at Lyft, used as the data plane in Istio and standalone for edge/gateway routing. It offers advanced load balancing, retries, circuit breaking, and observability.

## Details
- L7 features: HTTP/2, gRPC, fault injection, rate limiting, and rich access logs.
- Dynamic configuration via xDS APIs lets control planes reconfigure proxies live.
- Contrast with Nginx/Caddy: Envoy is more config-driven and API-native.

## Related
- [[wiki/devops-infra/istio|Istio]] — mesh built on Envoy
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — native proxy resilience
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — gateway-level enforcement
- [[wiki/devops-infra/nginx|Nginx]] — classic proxy alternative
- [[wiki/devops-infra/observability|Observability]] — rich proxy telemetry
