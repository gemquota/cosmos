---
type: "concept"
title: "TanStack Query Practice"
description: "Server-state caching with auto-refetch and invalidation"
tags: ["react-query", "data-fetching", "caching", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# TanStack Query Practice

## Summary
TanStack Query (formerly React Query) is the de facto server-state library for React: it caches query results by key, deduplicates concurrent requests, refetches on focus and mount per policy, and lets mutations invalidate or optimistically update the cache. Its core idea is that server state has different semantics than client state — it is async, shared, and can change remotely — so it deserves a dedicated layer.

## Details
- Mechanism: `useQuery({ queryKey, queryFn })` registers a query; the key (`['users', id]`) identifies the cache entry, and the function fetches the data. The library tracks status (`pending/error/success`), staleness (`staleTime`), and garbage collection (`gcTime`), deduplicates identical in-flight queries, refetches on window focus and reconnection by default, and retries failures with backoff. `useMutation` runs side-effectful operations with `onSuccess`/`onError` hooks; `queryClient.invalidateQueries(key)` marks matching queries stale so they refetch, and mutations can update the cache directly via `setQueryData` for optimistic UI.
- Concrete examples: a user profile page fetches `['user', 42]`, and three widgets sharing the key issue one request; after editing a profile, the mutation's `onSuccess` invalidates `['user', 42]` so the profile refetches; a like button uses `onMutate` to optimistically increment the counter, `onError` to roll back, and `onSettled` to refetch for truth; a search box uses `staleTime: 60_000` so repeated queries are instant.
- Failure modes: the classic failures are key mismanagement (keys missing variables cause cache collisions; keys that include non-serializable values break dedupe), turning off refetch to stop flicker and freezing data forever, and missing invalidation so the UI shows stale rows after a mutation. Retries that ignore `Retry-After` can pile load on a failing API; optimistic updates without proper rollback leave wrong UI state on failure; and server components require `dehydrate`/`hydrate` so the client cache inherits server-fetched data.
- Operational tradeoffs: the library removes an entire class of hand-rolled fetch logic (loading flags, races, retries, caching) at the cost of a concept set (keys, staleTime, gcTime, invalidation) and defaults that must be understood before they bite. Its sweet spot is any app with shared, frequently-changing server data; for one-shot fetches it is overkill. The ecosystem pattern is TanStack Query for server state plus a lightweight store (Zustand) for client state — never put server data in the store.
- RSIS3/mykb relevance: MyKB's dashboard is the textbook workload: search results, article lookups, and graph nodes keyed by query, invalidated when the knowledge graph rebuilds — TanStack Query's cache-and-invalidate model would replace the ad-hoc fetch state with declared server-state semantics.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/swr-practice|SWR in Practice]]
- [[wiki/frontend-frameworks/async-state|Async State]]
- [[wiki/frontend-frameworks/data-fetching-libs|Data Fetching Libraries]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/web-platforms/state-management|State Management]]
