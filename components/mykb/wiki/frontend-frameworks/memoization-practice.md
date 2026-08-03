---
type: "concept"
title: "Memoization Practice"
description: "Caching derived values to avoid repeated work"
tags: ["memoization", "performance", "react", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Memoization Practice

## Summary
Memoization is caching the result of an expensive computation keyed by its inputs, so repeated calls with unchanged inputs skip the work. In React it appears as `useMemo` (values), `useCallback` (functions), `React.memo` (components), and selector libraries (Redux `createSelector`, Zustand), and the practice question is always the same: when is the cache worth its memory and its bookkeeping?

## Details
- Mechanism: a memoized function stores `(inputs) -> result` pairs; on each call it compares the current inputs (by reference with `Object.is` or by custom equality) and returns the cached result if they match. In React, `useMemo(fn, deps)` recomputes only when the dependency array changes; `useCallback(fn, deps)` returns a stable function reference; `React.memo` bails out of re-rendering a component when its props are reference-equal; and `createSelector` caches per-argument-slice. The correctness rule is that dependencies must include everything the computation reads — a stale cache from a missing dep is worse than no cache.
- Concrete examples: a `useMemo` that filters a 10,000-row table only when rows or the filter change; a `useCallback` handler passed to a `React.memo` list item so 50 rows skip re-rendering on parent updates; a selector that derives `visibleTodos` once per `(todos, filter)` pair shared across ten components; a `memo` wrapping an expensive chart component that should re-render only when its data prop changes.
- Failure modes: the classic failures are premature memoization (wrapping every value in `useMemo`, adding dependency-array churn that costs more than the computation), stale deps (a memoized value or callback that captures old state, causing subtle bugs that appear as "it worked before I changed X"), and identity-based caches with content-equal inputs (a new array with the same contents defeats the cache unless `comparator` or custom equality is used). Memory is the quiet cost: unbounded memo caches for infinite lists or per-render keys leak.
- Operational tradeoffs: memoization trades memory and dependency-tracking complexity for recompute and re-render savings; it pays off when the computation is expensive, the component tree is large, or the inputs change rarely, and it is dead weight otherwise. Modern React reduces the need — compiler-assisted memoization (React Compiler, Svelte, signals) automates the cache, and colocating state shrinks re-render scopes so memoization matters less. The pragmatic practice: measure first, memoize hot paths, keep deps complete, and prefer derived values that are cheap to recompute over caches.
- RSIS3/mykb relevance: memoized selectors are how the dashboard derives graph stats and loop success rates from raw telemetry; caching the derivation per input slice (window, loop) keeps the render cheap, exactly as RSIS3 caches derived metrics until their raw inputs change.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/use-callback|useCallback]]
- [[wiki/frontend-frameworks/use-memo|useMemo]]
- [[wiki/frontend-frameworks/pure-components|Pure Components]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
