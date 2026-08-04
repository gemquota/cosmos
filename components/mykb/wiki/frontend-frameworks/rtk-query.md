---
type: "entity"
title: "RTK Query"
description: "Redux Toolkit's data fetching and caching layer"
tags: ["redux", "data-fetching", "rtk-query", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# RTK Query

## Summary
RTK Query is Redux Toolkit's data fetching and caching layer: you declare API endpoints in a `createApi` definition, and it generates hooks (`useGetUsersQuery`, `useUpdateUserMutation`) plus a reducer that stores cache entries in the Redux store. It brings TanStack-Query-style caching into the Redux ecosystem, with the store as the cache and middleware managing lifecycle.

## Details
- Mechanism: `createApi({ reducerPath, baseQuery, endpoints })` defines queries and mutations; `baseQuery` is usually `fetchBaseQuery` wrapping `fetch` with base URL and auth headers. Each query endpoint generates a hook whose cache key is derived from arguments; the store holds entries tagged by key with status, data, and error, and subscriptions are reference-counted — when the last component using a key unmounts, the cache entry is eligible for garbage collection after `keepUnusedDataFor`. Mutations can `invalidateTags` to refetch dependent queries, or use optimistic updates via `onQueryStarted` with `queryFulfilled` for rollback.
- Concrete examples: a `usersApi` with `getUsers` and `getUserById` endpoints, where editing a user mutation invalidates the `'User'` tag so lists refetch; a search endpoint whose query hook debounces via `skipToken` when the term is empty; an auth slice where `fetchBaseQuery` injects the token and a 401 response triggers a logout; optimistic likes that update the cache immediately and roll back on failure.
- Failure modes: the classic failures are tag over- and under-invalidation (too coarse — every mutation refetches everything; too fine — stale lists persist), cache-key collisions when serialized arguments collide or non-serializable args break the key computation, and mixing server state into hand-written slices so two sources of truth fight. The generated hooks also encourage skipping manual status management, so teams that also write `isLoading` flags in slices duplicate state. The Redux store grows with cache entries unless `keepUnusedDataFor` and cache policies are tuned.
- Operational tradeoffs: RTK Query's advantage is total integration — the cache lives in Redux, so DevTools, persistence, and the action log cover data fetching too, and TypeScript types flow from endpoint definitions. The cost is being tied to Redux's model; standalone TanStack Query is lighter and framework-agnostic, and for GraphQL, Apollo or Relay are purpose-built. Choose RTK Query when the app already commits to Redux Toolkit and wants one mental model; choose a standalone library otherwise.
- RSIS3/mykb relevance: the daemon's endpoints (search, article, graph) map naturally to an `createApi` definition with tags for `article`, `graph`, and `telemetry`; invalidating the `graph` tag on rebuild would cascade exactly the right refetches — the same declared-invalidation discipline RSIS3 uses between registry writes and derived outputs.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/apollo-client|Apollo Client]]
- [[wiki/frontend-frameworks/urql-practice|urql in Practice]]
- [[wiki/frontend-frameworks/relay-practice|Relay in Practice]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
