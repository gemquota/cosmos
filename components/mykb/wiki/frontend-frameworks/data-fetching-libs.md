---
type: "concept"
title: "Data Fetching Libraries"
description: "Caching, retry, and invalidation layers over fetch"
tags: ["data-fetching", "caching", "frontend", "libraries"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Data Fetching Libraries

## Summary
Data fetching libraries are layers over `fetch` that own the hard parts of server-state management: caching, deduplication, retries, background refetching, and invalidation. TanStack Query, SWR, RTK Query, and Apollo Client each implement the same job in slightly different flavors, and adopting one removes an entire category of hand-rolled `useEffect` fetch logic.

## Details
- Mechanism: the library keys every query (by URL, variables, or a custom key) and stores the result in a cache with freshness and staleness timestamps. A component mounts, asks for a key, and gets: cached data immediately if present (stale-while-revalidate), a background fetch if the data is stale, or a loading state on first fetch. Concurrent components asking for the same key share one request (deduplication), failed requests retry with backoff, and mutations mark affected keys as stale or proactively write to the cache so views update without a full refetch.
- Concrete examples: a dashboard with three widgets fetching the same user object issues one request, not three; a list view shows cached rows while silently refreshing when the user returns to the tab; after a `createPost` mutation succeeds, `invalidateQueries(['posts'])` refetches the list or the mutation response is written directly into the cache. The separation of server-state (owned by the library) from client-state (forms, toggles, filters held locally) removes the duplicate state that used to live in Redux stores.
- Failure modes: the classic failures are ignoring cache invalidation (data goes stale and users see old information), abusing the cache key (a key missing the variables causes queries to collide and show the wrong data), and disabling refetch entirely to "fix" flicker, which silently freezes data. Retries without awareness of `Retry-After` can amplify server load, and SSR/streaming setups need the cache dehydrated and rehydrated correctly or the client flashes between server data and a loading state.
- Operational tradeoffs: the libraries standardize a lot of behavior — retries, garbage collection, window-focus refetch — which is a win until those defaults are wrong for a specific workload, at which point every default must be understood. The main tradeoff is learning curve and a new concept set (keys, staleTime, gcTime, invalidation) versus the near-certain bugs of hand-rolled fetching. For server components and RSC-based frameworks, the role of client-side fetching libraries is shifting toward handling mutations and optimistic updates while the server owns initial data.
- RSIS3/mykb relevance: MyKB's search and graph dashboard are textbook server-state surfaces: query keys for search terms, cached article lookups, and invalidation on knowledge-graph rebuild would eliminate most of the ad-hoc loading logic, matching RSIS3's principle that state ownership should be explicit and centralized.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/react-query-practice|TanStack Query Practice]]
- [[wiki/frontend-frameworks/swr-practice|SWR in Practice]]
- [[wiki/frontend-frameworks/async-state|Async State]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/web-platforms/state-management|State Management]]
