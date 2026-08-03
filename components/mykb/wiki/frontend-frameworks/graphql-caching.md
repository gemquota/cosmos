---
type: "concept"
title: "GraphQL Caching"
description: "Normalized, persisted, and HTTP-level cache strategies"
tags: ["graphql", "caching", "performance", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GraphQL Caching

## Summary
GraphQL caching is harder than REST caching because every query is a different shape: there is no uniform URL to cache. The solutions are client-side normalized caches (Apollo, urql), persisted queries that restore cacheable GET requests, and HTTP-level caching at CDNs for documents that are identical by construction.

## Details
- Mechanism: a normalized client cache splits each response into entities keyed by `__typename` and `id`, stores fields per entity, and reassembles query results by reading the requested fields from the entity store, so two queries that overlap on an entity share its data and a mutation updating that entity refreshes every consumer. Persisted queries give each operation a stable hash ID; the client sends the ID, and the server maps it to the full query, which makes the request a GET with a stable URL — cacheable by CDNs and shareable across clients. HTTP-level caching then works like REST: `Cache-Control` headers, ETags, and CDN caching for the persisted-query URL.
- Concrete examples: Apollo's `InMemoryCache` with type policies keys users by `User:id`, so a profile edit mutation updates the sidebar and the detail page in one write; a public GraphQL API publishes a persisted-query manifest and serves the most popular queries from CDN cache; urql's document cache (query-shape-based) trades precision for simplicity on small apps where entities rarely overlap.
- Failure modes: normalization fails when entities lack stable IDs or `keyFields` — the cache fragments into duplicates and stale copies; lists are the classic problem, because a list field cannot be normalized the way an object can, and merge functions must decide how paginated pages combine or they silently replace each other. Over-caching in the client (holding data forever with no invalidation) shows stale UI, while under-caching (network-only policies everywhere) defeats the cache's purpose. Persisted queries shift the failure to the server: if the manifest and the deployed schema drift, a client sends an ID the server no longer recognizes.
- Operational tradeoffs: normalized caching is a big correctness investment (identity, merge functions, invalidation) that pays off in multi-view apps; persisted queries are a server-side investment with CDN payoff, ideal for public or read-heavy APIs; document caching is cheapest and best for small apps. The common thread is that caching requires explicit identity and invalidation decisions — there is no free cache for GraphQL.
- RSIS3/mykb relevance: MyKB's entity graph is the server-side version of a normalized cache: stable entity IDs, explicit links, and invalidation on rebuild; applying the same discipline client-side keeps the dashboard's article and graph views consistent without refetch storms.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/persisted-queries|Persisted GraphQL Queries]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/query-depth-limit|Query Depth Limits]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-aliases|GraphQL Aliases]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql|GraphQL]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-security|GraphQL Security]] — related coverage in the same cluster
