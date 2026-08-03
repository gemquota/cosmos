---
type: "concept"
title: "Context and Rendering"
description: "How context value changes propagate through consumers"
tags: ["react", "context", "rendering", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Context and Rendering

## Summary
Context and rendering is the study of how a context value change propagates through the component tree: which components re-render, why the blast radius is often larger than expected, and how to shape contexts so changes are cheap. The core mechanic is simple — a provider value change re-renders every consumer — and the performance art is in keeping that set small.

## Details
- Mechanism: when a provider re-renders and passes a new value, React marks all components that called `useContext(thatContext)` as dirty and re-renders them on the next pass, regardless of `React.memo` (context reads bypass memoization of props). The value itself is compared with `Object.is`, so a new object or array reference — even with identical contents — counts as a change. This is why `value={{ ... }}` in the provider body invalidates every consumer on every provider render, and why memoizing the value with `useMemo` or hoisting it outside the component is the standard fix.
- Concrete examples: an app with a single `AppContext` holding theme plus a ticking clock re-renders every consumer once per second; splitting it into `ThemeContext` and `ClockContext` confines the damage to the clock's consumers. A provider that passes a stable `value` (defined outside or via `useMemo` with correct deps) lets children bail out of re-rendering entirely. Selector libraries (Redux's `useSelector`, Zustand's `useStore`) solve the same granularity problem at the store level, comparing slices instead of whole values.
- Failure modes: the canonical failures are object-literal values (new reference every render), single mega-contexts that mix stable and volatile data, and consumers that read only part of a large value while re-rendering on all of it. Subtler: passing a new callback in the value (an inline `toggleTheme` closure) changes the value reference even when the data is unchanged, and context nested inside a frequently re-rendering parent re-creates the subtree at the provider boundary.
- Operational tradeoffs: splitting contexts improves precision but adds provider nesting and boilerplate, and each new context is a new API surface to maintain. Memoizing values moves the complexity to dependency arrays, which can go stale. The pragmatic middle: keep a small number of contexts organized by change frequency (stable config, rarely-changing identity, volatile UI state), memoize the value objects, and reserve selectors for genuinely high-frequency state.
- RSIS3/mykb relevance: the propagation model is dependency tracking in miniature: know exactly which consumers depend on which slices of shared state, and isolate high-churn values so one loop's updates do not re-render the whole dashboard — the same containment RSIS3 applies to L1 pulse writes versus stable registry state.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/selector-libraries|Selector Libraries]]
- [[wiki/frontend-frameworks/derived-state|Derived State]]
- [[wiki/frontend-frameworks/selectors-practice|Selectors in Practice]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
