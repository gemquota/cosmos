---
type: "concept"
title: "REST APIs"
description: "Architectural style for stateless, resource-oriented HTTP APIs built on standard methods and status codes"
tags: ["api", "rest", "http", "web-platforms", "json"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/REST"]
---

# REST APIs

## Summary
REST (Representational State Transfer) is an architectural style for networked systems introduced by Roy Fielding in his 2000 doctoral dissertation. It centers on stateless client-server interaction, resource-oriented URIs, and a uniform interface of standard HTTP methods and status codes. REST remains the default choice for public and internal APIs because it is simple, cacheable, and broadly tooled.

## Details
- Resources, not actions: URLs identify nouns such as `/wiki/pages/{id}` while the HTTP method expresses the verb (GET, POST, PUT, PATCH, DELETE).
- Statelessness: every request carries the context needed to process it, which simplifies horizontal scaling and makes retries with idempotency keys safe.
- Status codes carry meaning: 2xx success, 3xx redirection, 4xx client errors, 5xx server errors; 429 signals rate limiting and 422 validation failures.
- Representations are exchanged as JSON by default; content negotiation and `Content-Type` headers make formats explicit.
- Collections and sub-resources model relationships; query parameters filter, sort, and paginate result sets.
- Worked example: the RSIS3 FastAPI dashboard exposes REST endpoints that the mykb daemon's MemoryClient calls, with automatic OpenAPI documentation served at `/docs`.
- Trade-offs: REST over-fetches for complex client-driven queries (GraphQL) and lacks typed wire contracts (gRPC with Protocol Buffers).

## Related
- [[wiki/api-protocols/openapi|OpenAPI]] — machine-readable description of REST endpoints
- [[wiki/api-protocols/http-caching|HTTP Caching]] — makes stateless GET responses fast
- [[wiki/api-protocols/idempotency|Idempotency]] — safe retry behavior for REST mutations
- [[wiki/api-protocols/graphql|GraphQL]] — query-driven alternative that avoids over-fetching
- [[wiki/api-protocols/grpc|gRPC]] — typed, binary alternative for service-to-service calls
- [[wiki/concepts/triad-architecture|Triad Architecture]] — REST links RSIS3 to the mykb memory layer
- [[wiki/ops/gap-report|Gap Analysis Report]] — records API coverage gaps in the wiki
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — client behavior for REST errors and 429s
