---
type: "concept"
title: "urql in Practice"
description: "Lightweight, exchange-based GraphQL client"
tags: ["graphql", "urql", "frontend", "libraries"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# urql in Practice

## Summary
urql is a lightweight GraphQL client built on a pipeline of "exchanges" — plugins that process operations and results. It offers two cache modes (a simple document cache by default, and Graphcache, a normalized cache for full-featured use), and its small core makes it the pragmatic choice when Apollo feels heavy and Relay's compiler ceremony is unwarranted.

## Details
- Mechanism: every operation (query, mutation, subscription) flows through the exchange pipeline — `dedupExchange` collapses identical in-flight requests, `cacheExchange` reads/writes the cache, `fetchExchange` performs the network request, and custom exchanges slot in for auth headers, retries, logging, or offline support. The default document cache stores results by query document and variables, returning cached data for identical queries; Graphcache replaces it with a normalized cache keyed by `__typename` and `id` (with configurable `keys` for entities lacking IDs) and supports cache updates via `updates`/`optimistic` configs.
- Concrete examples: a small app with `cacheExchange` and `fetchExchange` gets dedupe and caching with two lines of setup; a team needing normalized caching swaps in `@urql/exchange-graphcache` and declares `keys: { User: (data) => data.id }`; an auth flow adds a custom exchange that attaches the token to every request and, on 401, refreshes and retries; `useQuery`/`useMutation` hooks expose `fetching`, `data`, and `error` with `requestPolicy: 'cache-and-network'` for fresh-but-fast views.
- Failure modes: the classic failure is assuming Graphcache semantics while using the document cache — overlapping queries with different fields do not share data, causing "why is this stale?" surprises. Graphcache's own pitfalls are missing `keys` (entities without IDs fragment the cache), list updates that need explicit `updates` config (a mutation returning a new item does not append it to a list automatically), and optimistic updates misconfigured so rollback leaves wrong state. Custom exchanges that reorder or short-circuit the pipeline break dedupe or caching silently.
- Operational tradeoffs: urql's core is small and its API stays close to GraphQL semantics — the exchange model makes behavior inspectable and composable — at the cost of fewer batteries included than Apollo (schema typemap setup for Graphcache, manual entity key config). It fits apps that want control without framework weight, especially non-React or mixed setups (urql supports Vue, Svelte, and plain JS). The choice between document cache and Graphcache is the main design decision: document cache for simple apps where queries rarely overlap, Graphcache where multiple views share entities.
- RSIS3/mykb relevance: the exchange pipeline is middleware discipline — auth, caching, retry, and logging as composable stages over one operation stream — the same layering RSIS3 applies to loop telemetry handling, and the cache choice mirrors the tradeoff between document-level and entity-level knowledge in MyKB's graph views.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/relay-practice|Relay in Practice]]
- [[wiki/frontend-frameworks/rtk-query|RTK Query]]
- [[wiki/frontend-frameworks/apollo-client|Apollo Client]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
