---
type: "concept"
title: "REST vs GraphQL"
description: "Resource-oriented HTTP APIs versus a single query endpoint with client-shaped responses"
tags: ["api", "rest", "graphql", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# REST vs GraphQL

## Summary
REST exposes resources over HTTP with standard methods and status codes; GraphQL exposes a single endpoint where clients select exactly the fields and relations they need. REST wins on caching and simplicity, GraphQL on flexibility and payload efficiency.

## Details
REST models the domain as resources (orders, users) addressed by URLs and manipulated with GET/POST/PUT/DELETE; responses are server-defined shapes, and clients fetch what the server gives. GraphQL replaces that with one endpoint (typically POST /graphql) where the query declares the response shape: { user(id: 1) { name, orders { total } } } returns exactly that. The server resolves the query against resolvers, and the client gets a tailored document in one round trip.

The mechanism: REST's contract is the resource and its representation; caching works because URLs are cache keys and GET is idempotent. GraphQL's contract is the schema; the client composes queries, and the server walks resolvers, which can N+1 without batching (hence DataLoader). Over-fetching disappears, but so does URL-level caching — GraphQL responses are POST bodies and must be cached at the resolver or edge with care.

Concrete example: a wiki dashboard needs a user's profile plus their latest notes. REST: GET /users/1 then GET /users/1/notes?limit=5 — two requests, and the second returns full notes even if the UI shows titles only. GraphQL: one query selecting name, avatar, and notes { title }, one round trip, exact fields. The tradeoff shows up at scale: REST's shared-cache friendliness vs GraphQL's bandwidth savings on mobile.

Failure modes: GraphQL without depth/cost limits lets clients issue exponential queries (nested lists multiply) — a DoS vector; REST with chatty clients causes N+1 round trips on mobile; and GraphQL's single endpoint hides which fields are expensive until an attacker queries them all. Both fail when the schema drifts from reality; REST also fragments on over-fetching, GraphQL on query complexity.

Operational tradeoffs: REST is easier to cache, monitor, and version per-resource; GraphQL needs query cost analysis, persisted queries, and batching infrastructure to stay safe and fast. Many teams run both: REST for public, cacheable, stable resources and GraphQL for product UIs that need flexible composition. The choice is about where the complexity belongs — server-defined shapes (REST) or client-defined shapes with server-side safety rails (GraphQL).

RSIS3/mykb relevance: the dashboard's telemetry views are client-shaped; documenting whether each view uses REST collections or GraphQL queries keeps RSIS3 tooling aligned with the actual contract.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/rest-vs-grpc|REST vs gRPC]]
- [[wiki/api-protocols/rest-vs-rpc|REST vs RPC]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/rpc-styles|RPC Styles]]
- [[wiki/api-protocols/graphql|GraphQL]]
