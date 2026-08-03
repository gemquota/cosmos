---
type: "concept"
title: "SWR in Practice"
description: "Stale-while-revalidate data fetching hooks"
tags: ["swr", "data-fetching", "caching", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SWR in Practice

## Summary
SWR is a React data-fetching library named after the stale-while-revalidate caching strategy: `useSWR(key, fetcher)` returns cached data immediately when available, then revalidates in the background and swaps in fresh data when it arrives. The result is a UI that always shows something instantly — never a blank spinner on repeat visits — while staying current with the server.

## Details
- Mechanism: `useSWR('/api/user', fetcher)` uses the key to identify the cache entry; on mount, the hook returns the cached value if one exists (stale), then runs the fetcher, and on success updates the cache and re-renders with fresh data. Revalidation triggers include mount, window focus, reconnection, and interval (`refreshInterval`), and concurrent components with the same key dedupe into one request. `mutate(key, data)` updates the cache directly (optimistic updates with `optimisticData` and `rollbackOnError`), `SWRConfig` sets global options, and `preload` warms caches ahead of navigation.
- Concrete examples: a profile header reads `useSWR(['user', id], fetchUser)` and shows cached data instantly while revalidating; a search box debounces via `useSWR` keyed by the query so each term's results are cached and instant on re-type; a polling dashboard uses `refreshInterval: 5000` to keep metrics fresh; a like button uses `mutate` with `optimisticData` to flip the count immediately and roll back on error; `useSWRInfinite` pages through a list with cursor keys.
- Failure modes: the classic failures are key instability (keys with non-serializable objects or missing variables cause collisions and stale mismatches), disabling revalidation to stop flicker (which freezes data), and unhandled revalidation races — slow responses overwriting newer ones unless the fetcher or keys are structured to prevent it. Error handling needs `errorRetryCount`/`shouldRetryOnError` tuning so a failing endpoint does not hammer itself, and SSR/SSG setups must `preload` or `fallbackData` correctly to avoid a flash of empty state.
- Operational tradeoffs: SWR's philosophy — data freshness as a spectrum, cached-first rendering — makes UIs feel fast with minimal code, and its API is smaller than TanStack Query's. The tradeoffs: fewer built-in features (no first-class mutation cache updates beyond `mutate`), a document-centric cache (cache keyed by request, not by entity, so overlapping queries do not share data automatically), and defaults that assume you want revalidation (which must be consciously scoped). It is the right tool when the app is REST-ish, wants minimal ceremony, and values instant cached renders; TanStack Query wins when normalized entities, rich mutation flows, or advanced cache management are needed.
- RSIS3/mykb relevance: MyKB's search and telemetry views fit SWR's model perfectly — cache results per query term, show last-known data instantly, revalidate in the background as the daemon updates — mirroring RSIS3's stale-while-revalidate approach to derived metrics that are expensive to recompute.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/async-state|Async State]]
- [[wiki/frontend-frameworks/data-fetching-libs|Data Fetching Libraries]]
- [[wiki/frontend-frameworks/react-query-practice|TanStack Query Practice]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/web-platforms/state-management|State Management]]
