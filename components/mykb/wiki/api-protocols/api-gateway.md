---
type: "concept"
title: "API Gateway"
description: "Routing, aggregation, authn, and policy enforcement"
tags: ["api-gateway", "architecture", "edge", "authentication", "routing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://microservices.io/patterns/apigateway.html", "https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway"]
---

# API Gateway

## Summary
An API gateway is the single entry point for client traffic: it routes requests to services, aggregates responses, authenticates, rate-limits, and enforces policies centrally. It is the edge of a microservice architecture — the place where cross-cutting concerns get implemented once instead of in every service.

## Details
- Routing: path and header-based dispatch to backend services, with rewrites, retries, and circuit breaking at the edge.
- Authentication: terminate authn at the gateway (OAuth token validation, API keys, mTLS) and forward identity claims to backends via headers.
- Aggregation: compose responses from multiple backends for clients that would otherwise fan out — the gateway as a BFF or facade.
- Policy enforcement: rate limiting, quotas, IP allowlists, request size caps, and schema validation in one place.
- Cross-cutting: centralized logging, tracing (x-request-id), caching, and response transformation (JSON->XML) avoid per-service duplication.
- Trade-offs: a gateway is a single point of failure (run multiple, keep it stateless) and a potential bottleneck; thin gateways beat fat ones.
- Products: Kong, Traefik, Envoy, APISIX, AWS API Gateway, and managed edge platforms; each differs in plugin model and control plane.

## Related
- [[wiki/api-protocols/backend-for-frontend|Backend for Frontend]] — per-client gateways refine the pattern
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — edge enforcement of quotas
- [[wiki/security-auth/token-authentication|Token Authentication]] — edge validation of bearer tokens
- [[wiki/api-protocols/service-mesh|Service Mesh]] — mesh handles east-west, gateway handles north-south
- [[wiki/devops-infra/api-gateway-patterns|API Gateway Patterns]] — the infra-focused companion article
