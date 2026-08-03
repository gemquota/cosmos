---
type: "concept"
title: "Async State"
description: "Modeling pending, success, and error phases of async data"
tags: ["async", "state", "frontend", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Async State

## Summary
Async state is the modeling of an asynchronous operation's lifecycle in the UI: pending (in flight), success (data available), and error (failed), plus the transitions between them. Getting this model right determines whether a screen feels responsive, whether stale data can overwrite fresh data, and whether errors are recoverable or silently swallowed.

## Details
- Mechanism: a common shape is a discriminated union or status enum: `{ status: 'idle' | 'loading' | 'success' | 'error', data?, error? }`. The UI branches on `status` — a spinner for loading, a content view for success, an inline retry for error — while the data lives in a single place. Libraries like TanStack Query and SWR manage this automatically with extra fields (`isFetching`, `isError`, `error`, `dataUpdatedAt`), plus deduping, caching, and background refetching so the pending state is rarely seen twice.
- Concrete examples: a search results panel shows skeletons while a request is in flight, then either results or an error banner with a retry button; a settings form disables its submit button while saving and re-enables it with an error message on failure; an autocomplete keeps the previous results visible during a refetch (`stale-while-revalidate`) instead of flashing back to a spinner. Race handling is the hidden requirement: when two requests for the same resource resolve out of order, the UI must ignore the stale one, which is why `AbortController` and request-sequence counters exist.
- Failure modes: the classic failures are missing error states (fetch fails and the UI spins forever or shows an empty list as if nothing happened), stale-overwrite races (an old response clobbers a newer one), and state duplication (loading flags scattered across unrelated components so two parallel fetches fight over one boolean). Retry loops without backoff can hammer a failing API, and unmounting components that later resolve cause the dreaded "setState on unmounted component" warnings and leaked subscriptions.
- Operational tradeoffs: hand-rolled async state is simple for one screen but repeats the same bug-prone logic everywhere; data-fetching libraries standardize dedupe, caching, retries, and invalidation at the cost of a new abstraction and configuration surface. A state-machine framing (finite states with explicit events) removes impossible states entirely but adds ceremony that is overkill for simple fetches. The pragmatic rule: model the union, derive UI from it, cancel or ignore stale requests, and centralize the pattern once for the codebase.
- RSIS3/mykb relevance: MyKB's search and graph views are async surfaces; modeling their pending/success/error states explicitly keeps the dashboard honest about the daemon's health, mirroring how RSIS3 tracks loop phases as first-class state rather than ad-hoc booleans.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/data-fetching-libs|Data Fetching Libraries]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/react-query-practice|TanStack Query Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/swr-practice|SWR in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-apis|REST APIs]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql|GraphQL]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
