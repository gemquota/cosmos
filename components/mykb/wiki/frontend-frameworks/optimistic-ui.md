---
type: "concept"
title: "Optimistic UI"
description: "Applying user actions to the UI immediately and reconciling with the server result"
tags: ["optimistic-ui", "ux", "state", "data-fetching", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates", "https://developer.mozilla.org/en-US/docs/Web/API/Request"]
---
# Optimistic UI

## Summary
Optimistic UI applies a mutation's expected result instantly, then reconciles when the server responds. Users perceive speed because there is no waiting spinner for common actions. Correctness requires rollback on failure and careful handling of concurrent mutations.

## Details
- **Pattern** — capture the pre-mutation state, apply the optimistic value, then confirm with the server response or roll back on error.
- **Cache integration** — query caches make this natural: update the cache, invalidate, and refetch in the background.
- **Concurrency** — overlapping mutations need base-state snapshots; otherwise stale rollbacks clobber newer edits.
- **When to use** — low-risk, reversible, or idempotent actions (likes, toggles, drafts); avoid for irreversible or costly operations.
- **Worked example** — the mykb note editor marks a save as complete instantly, then reconciles if the server rejects it.
- **Relevance** — RSIS3's agent-driven edits should render optimistically and reconcile deterministically.

## Related
- [[wiki/frontend-frameworks/async-state|Async State]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/react-query-practice|TanStack Query Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/derived-state|Derived State]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/selectors-practice|Selectors in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — existing coverage
- [[wiki/api-protocols/idempotency|Idempotency]] — existing coverage
