---
type: "concept"
title: "State Management Patterns"
description: "Taxonomy of local, global, and server state"
tags: [state-management", "react", "architecture", "stores", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/managing-state", "https://redux.js.org/tutorials/fundamentals/part-3-state-actions-reducers"]
---

# State Management Patterns

## Summary
State management patterns categorize where UI state lives and how it changes: local component state, lifted and shared state, global stores, server-cache state, and URL state. The right pattern depends on scope and lifetime — not every value belongs in a global store. Modern frameworks blur the line with signals and server-state libraries.

## Details
- Local state: useState covers ephemeral UI values scoped to one component.
- Lifted state: shared state moves to the closest common ancestor and passes down through props.
- Global stores: context, Redux, Zustand, and Jotai serve app-wide state such as auth and settings.
- Server state: fetched data is a cache concern — React Query and SWR manage freshness, retries, and invalidation.
- URL state: filters, tabs, and pagination belong in the URL for shareability and back-button behavior.
- Rule of thumb: keep state as local as possible; promote it only when multiple components genuinely need it.

## Related
- [[wiki/frontend/unidirectional-data-flow|Unidirectional Data Flow]] — the store update model
- [[wiki/frontend/reactive-state|Reactive State]] — signals and observables
- [[wiki/frontend/prop-drilling|Prop Drilling]] — the problem patterns solve
- [[wiki/web-platforms/state-management|State Management]] — platform-level notes
- [[wiki/frontend/state-machines|State Machines]] — modeling complex state explicitly
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — the mobile counterpart
