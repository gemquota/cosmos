---
type: "concept"
title: "API Gateway Patterns"
description: "Fronting APIs with a single gateway for routing, auth, rate limiting, and aggregation"
tags: ["api-gateway", "patterns", "routing", "apis"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# API Gateway Patterns

## Summary
An API gateway is the single entry point for client traffic: it routes, authenticates, rate-limits, and sometimes aggregates backend calls. It centralizes cross-cutting API concerns so services stay focused.

## Details
- Common responsibilities: routing, authN/authZ, rate limiting, request/response transformation, and observability.
- BFF (backend-for-frontend) variants tailor aggregation per client type.
- Gateways add a hop and a config surface — failure modes and latency must be managed.
- Open question: when a gateway is overkill and a plain load balancer suffices.

## Related
- [[wiki/devops-infra/load-balancing|Load Balancing]] — the L4/L7 base
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — gateway-backed serverless APIs
- [[wiki/api-protocols/rest-apis|REST APIs]] — the API style served
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — a gateway-level policy
