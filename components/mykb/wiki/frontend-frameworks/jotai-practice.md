---
type: "entity"
title: "Jotai in Practice"
description: "Atomic primitive-based state for React"
tags: ["jotai", "state", "react", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Jotai in Practice

## Summary
Jotai is a minimal state library for React built around atoms: tiny, independent state units that compose through derived atoms instead of one global store. `const countAtom = atom(0)` is a piece of state, `const doubled = atom(get => get(countAtom) * 2)` is a derivation, and components subscribe with `useAtom`, so re-renders are scoped to exactly the atoms a component reads.

## Details
- Mechanism: an atom holds a value (or a read function); a derived atom recomputes from its dependencies and caches until they change; `useAtom` returns `[value, setValue]` and subscribes the component to the atoms it reads, so granular updates happen without selector functions or a central store shape. Atoms are created anywhere and referenced by closure, which makes colocating state with features natural. Jotai also supports `atomWithStorage` (persistence to localStorage), `loadable` and `atomWithSuspense` for async atoms, and `Provider` for scope isolation (per-app or per-feature state instances).
- Concrete examples: a counter `atom(0)` used by two buttons and a display; a search feature with `termAtom`, `debouncedTermAtom` derived with a delay, and `resultsAtom` derived from an async fetch — the async atom suspends or returns a loadable, and every consumer re-renders only when its slice changes; a theme atom persisted to localStorage so reloads keep the choice; a per-user cart scoped with a Provider keyed by user ID.
- Failure modes: the classic pitfalls are creating atoms inside components (a new atom identity per render breaks subscriptions and causes stale reads — atoms should be module-scoped or stable), cyclic derived atoms (infinite recomputation, which the library rejects with an error), and writing to atoms during render. Async atoms add their own traps: unhandled rejections, stale responses from a slow fetch overwriting a newer one, and suspense boundaries that swallow errors unless `loadable` is used.
- Operational tradeoffs: Jotai trades the structure of a single store (Redux-style actions/reducers) for freedom and granularity: less boilerplate, no provider tree for basic use, and re-renders that scale with dependencies rather than the store. The cost is that global debugging and time-travel are weaker than Redux, and the flexibility invites atoms sprawl — hundreds of tiny atoms with implicit dependency graphs that are harder to reason about than one explicit reducer. It sits between Zustand (store-centric, minimal) and Recoil (atom-based, heavier) — the right choice when state is naturally fragmented and colocated, wrong when the app needs one auditable state machine.
- RSIS3/mykb relevance: Jotai's derived atoms are the client-side equivalent of RSIS3's derived metrics: declare sources once, derive everything else reactively, and let the invalidation graph do the work — the dashboard's filter, search, and selection state fits this model directly.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/recoil-practice|Recoil in Practice]]
- [[wiki/frontend-frameworks/mobx-practice|MobX in Practice]]
- [[wiki/frontend-frameworks/redux-practice|Redux in Practice]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
