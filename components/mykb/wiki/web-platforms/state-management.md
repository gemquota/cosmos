---
type: "concept"
title: "State Management"
description: "The patterns and tools for tracking and synchronizing the data a UI depends on"
tags: ["state", "react", "frontend", "data-flow"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/managing-state"]
---

# State Management

## Summary
State management is how applications track the data that drives the UI and keep every rendered view consistent with it. React's own guidance — 'managing state' — is the canonical modern treatment: state should live where it is used, and only shared state should be lifted or externalized.

## Details
- Local state lives inside a component (useState); shared state is lifted to a common ancestor or moved to a store.
- Derived state should be computed, not duplicated: storing redundant copies is the most common source of bugs.
- Stores (Redux, Zustand, Pinia) centralize cross-cutting state with explicit actions and selectors; the cost is boilerplate.
- Server state is different from UI state: data fetched from APIs needs caching, invalidation, and optimistic updates (React Query, SWR).
- URLs are state: routes, query params, and hashes make views shareable and back-button-safe.
- RSIS3 relevance: the dashboard's view of agent memory is state that must stay in sync with the wiki index.
- Worked example: a search box's query is local state; the results it filters are derived; the wiki data is server state.

## Related
- [[wiki/web-platforms/component-architecture|Component Architecture]] — components decide where state lives
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — frameworks provide state primitives
- [[wiki/software-engineering/reactive-programming|Reactive Programming]] — stores are reactive data flows
- [[wiki/api-protocols/rest-apis|REST APIs]] — server state arrives over APIs
- [[wiki/api-protocols/http-caching|HTTP Caching]] — cache behavior underlies server-state libraries
- [[wiki/concepts/working-memory|Working Memory]] — UI state is the interface's working memory
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — state transitions drive agent UIs
