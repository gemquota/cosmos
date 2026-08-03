---
type: "concept"
title: "Recoil in Practice"
description: "Atom and selector state graph for React"
tags: ["recoil", "state", "react", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Recoil in Practice

## Summary
Recoil is a React state library built on a dependency graph of atoms (state units) and selectors (derived values): `atom()` holds state, `selector()` derives values with automatic caching and invalidation, and components subscribe with `useRecoilValue`/`useRecoilState`. It introduced the atom/selector mental model to React and influenced successors like Jotai, though its own maintenance trajectory has slowed.

## Details
- Mechanism: atoms are identified by a key and hold a value; selectors declare a `get` function that reads atoms and other selectors, and the library builds a reactive graph where a change to any atom invalidates exactly the selectors that (transitively) depend on it. Components subscribe at the granularity of the atom or selector they read, so re-renders follow the dependency graph rather than the component tree. Selectors can be async: a selector whose `get` returns a promise suspends the reading component (inside a Suspense boundary) or is awaited via `useRecoilValueLoadable`, enabling derived server state without explicit fetch management.
- Concrete examples: a `userAtom` and a `filteredTodosSelector` that derives from `todosAtom` plus `filterAtom`; an async `searchResultsSelector` keyed by a `searchTermAtom`, with a `waitForAll` helper to combine multiple async selectors; `atomFamily`/`selectorFamily` for parameterized state (one atom per item ID); `useRecoilCallback` for transaction-style updates that read and write multiple atoms consistently.
- Failure modes: the classic pitfalls are unstable keys (duplicate atom keys throw; dynamic keys in families must be stable), selectors with side effects (a selector `get` must be pure — writing atoms or fetching without caching there causes loops and repeated work), and async-selector error handling (a rejected promise inside Suspense needs an error boundary or `Loadable` or it unmounts the tree). Because the graph is invisible, debugging "why did this re-render?" requires the Recoil devtools, and over-fragmentation into tiny atoms makes flows hard to trace.
- Operational tradeoffs: Recoil's dependency graph gives precise updates and composable derivation with a fairly small API, but its ecosystem momentum stalled relative to Zustand/Jotai, so new projects weigh maintenance risk. For a team that already knows the atom/selector model (and needs async derived state), it remains workable; the alternatives are Jotai (lighter, module-scoped atoms), Zustand (store-centric), or Redux (explicit actions). The practice rule: atoms for source state, pure selectors for derivation, families for collections, and explicit error handling for async selectors.
- RSIS3/mykb relevance: the atom/selector graph is the same shape as RSIS3's registry-and-derived-metrics model: declared sources, derived outputs that invalidate automatically, and a dependency graph that is inspectable — the ideal structure for the dashboard's telemetry views.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/mobx-practice|MobX in Practice]]
- [[wiki/frontend-frameworks/redux-practice|Redux in Practice]]
- [[wiki/frontend-frameworks/zustand-practice|Zustand in Practice]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
