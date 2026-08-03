---
type: "concept"
title: "Selectors in Practice"
description: "Pure functions that derive memoized state slices"
tags: ["selectors", "state", "memoization", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Selectors in Practice

## Summary
Selectors are pure functions that project a slice of state: `(state) => state.user.name`. In practice they come in two layers — plain projections for readability and memoized selectors for performance — and the discipline around them (purity, composability, narrow reads) is what keeps large state trees fast and components decoupled from the store's shape.

## Details
- Mechanism: a plain selector is a function that takes state and returns a slice; components call it inside `useSelector`, which subscribes them to the store and re-renders when the slice's reference changes. A memoized selector (`createSelector` in Redux Toolkit, Reselect) tracks its input selectors' outputs and recomputes only when they change, returning the cached result otherwise — so `visibleTodos` computed from `todos` and `filter` recomputes only when either input changes, and every consumer shares the cache. Selectors compose: a selector can read other selectors, building a derived-state tree that mirrors the UI's needs rather than the store's layout.
- Concrete examples: `selectUserById(state, id)` via `createSelector` returns the user object by id, memoized per id; `selectVisibleTodos` combines `selectTodos` and `selectFilter`; a selector family parameterized by route params feeds a detail page; `selectCartCount` returns `items.length` so the badge re-renders only when the count changes, not on every cart edit.
- Failure modes: the classic failures are impure selectors (reading `Date.now()` or generating random values — the memoized result becomes stale by design), selectors that return new references each call (defeating equality and causing render loops), and over-narrow or over-wide selections (subscribing to the whole state, or selecting a primitive while the component needs a stable object). Parameterized selectors need per-argument caching or they thrash; and selectors that reach deep into nested state (`s.a.b.c`) couple every consumer to the shape — the selector is supposed to be the single place that knows it.
- Operational tradeoffs: selectors centralize shape knowledge and derivation, which pays off as state grows, but adds a layer of indirection and memoization bookkeeping. The guidance is to write plain selectors first (they are documentation), memoize only measured hot paths, keep selectors pure and side-effect-free, and prefer narrow selects at the component boundary. With signal-based state, much of this collapses into the framework's dependency tracking — but at store boundaries, memoized selectors remain the standard tool.
- RSIS3/mykb relevance: derived dashboard metrics (success rate, pulse counts) are memoized selectors over raw telemetry; keeping them pure and cached per input window mirrors RSIS3's rule that aggregates are always recomputed from raw records, never stored as independent truth.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/memoization-practice|Memoization Practice]]
- [[wiki/frontend-frameworks/use-callback|useCallback]]
- [[wiki/frontend-frameworks/use-memo|useMemo]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
