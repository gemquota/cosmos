---
type: "concept"
title: "Apollo Client"
description: "Full-featured GraphQL client with normalized caching"
tags: ["graphql", "apollo", "caching", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Apollo Client

## Summary
Apollo Client is a full-featured GraphQL client for React and other frameworks, best known for its normalized cache: query results are split into entities and stored by `__typename` and `id`, so overlapping queries share data and a mutation that updates an entity refreshes every view reading it. It also provides local state management, pagination helpers, and subscriptions on top of a simple request pipeline.

## Details
- Mechanism: every query response is decomposed into cache entities keyed by `TypeName:ID`; fields are stored per entity, and a query reads by collecting the requested fields from the cache, triggering a network fetch only for missing fields. Because the cache is normalized rather than document-shaped, two queries for the same user share one entity, and `writeFragment` or a mutation result can update that entity in place. Cache policies (`cache-first`, `network-only`, `cache-and-network`) decide when to go to the network, and type policies define how lists merge.
- Concrete examples: a profile page and a sidebar both query `user(id: 1)` with different fields — the second render hits the cache; a `toggleLike` mutation returns the updated post and Apollo merges it, updating the feed without a refetch; an infinite feed uses `fetchMore` with cursor pagination and a `merge` function that appends pages; local-only fields (`@client`) store UI state like the current filter in the same cache, queryable with the same GraphQL syntax.
- Failure modes: the classic Apollo failures are cache identity problems — entities without stable `id`s (or custom `keyFields` not configured) fragment the cache and cause duplicate or stale entries; list mutations that do not return the changed item leave lists stale until refetch; and `cache-and-network` policies can cause flicker when a stale cache paints before the fresh network result arrives. Over-normalization (deeply nested objects) bloats memory, while over-reliance on `refetchQueries` defeats the normalized cache's purpose.
- Operational tradeoffs: Apollo's power is its steep configuration surface: type policies, field policies, merge functions, and error policies all need deliberate setup, and teams that skip them get subtle staleness bugs. The alternative clients (urql, Relay) trade features differently — Relay's compiler gives stronger guarantees but more ceremony, urql gives simplicity with weaker caching. For RSIS3/mykb-scale dashboards, Apollo's normalized cache is a good fit when many views share the same knowledge-graph entities, but only if entity identity is enforced at the schema level.
- RSIS3/mykb relevance: the normalized cache is a client-side mirror of MyKB's entity graph: one source of truth for each entity, updated in place, so every widget reading a pulse or article stays consistent — the same identity discipline the knowledge graph enforces server-side.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/urql-practice|urql in Practice]]
- [[wiki/frontend-frameworks/relay-practice|Relay in Practice]]
- [[wiki/frontend-frameworks/rtk-query|RTK Query]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
