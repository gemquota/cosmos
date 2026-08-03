---
type: "concept"
title: "API Expansion"
description: "Embedding or expanding related resources in a single response"
tags: ["api", "http", "design", "graphql"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Expansion

## Summary
API expansion — also called embedding — lets clients request related resources in one round trip instead of N+1 queries. Done well it cuts latency; done lazily it bloats responses and couples clients to server internals.

## Details
Expansion is the REST-flavored cousin of GraphQL's nested selection: the client asks for a primary resource plus related objects to be inlined, usually via ?expand=author,comments or ?fields=...,expand=... . The server resolves the relationship graph server-side and returns a single document. The canonical example is an issue list where each issue expands its assignee, saving one request per issue.

The mechanism: the API layer parses the expand parameter, whitelists allowed relationship names, fetches the primary rows, then issues batched lookups for the related rows — avoiding per-row queries — and joins them into the response. Depth is usually capped at one or two levels, and cycles are either forbidden or cut at a depth bound to prevent infinite recursion.

Concrete example: GET /api/posts?expand=author,comments.author returns each post with an embedded author object and comments with their authors. The client renders the whole thread from one response. Without expansion it would need 1 + N + M requests; with over-eager expansion it would ship every comment body when the client only wanted counts.

Failure modes: unbounded expansion is a denial-of-service vector — expand=comments.comments.comments... multiplies work and payload size; deep expansion causes N+1 loads if the implementation fetches per row; and clients that blindly render embedded relations break when a relation is omitted (null) because of permissions, since expansion typically respects field-level authorization and simply leaves things out.

Operational tradeoffs: expansion trades response size and server work for round trips, which is a good deal for chatty mobile clients but wasteful for narrow reads; sparse fieldsets (fields=...) pair naturally with it so clients can trim payloads. Caching gets harder because expanded responses are cache-key dependent. API versioning must treat the set of expandable relations as contract — adding one is safe, removing one is breaking.

RSIS3/mykb relevance: the dashboard's knowledge-graph views are effectively an expanded resource (node plus neighbors); documenting the expand contract for the graph API keeps future L2 loop tooling from over-fetching.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/sparse-fieldsets|Sparse Fieldsets]] — related coverage in the same cluster
- [[wiki/api-protocols/api-pagination|API Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/api-filtering|API Filtering]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — related coverage in the same cluster
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — related coverage in the same cluster
