---
type: "concept"
title: "useMemo"
description: "Caching expensive derived values in React"
tags: ["react", "memoization", "hooks", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# useMemo

## Summary
`useMemo(fn, deps)` caches the result of an expensive computation and returns the cached value on subsequent renders until the dependency array changes. It is React's tool for derived values that are costly to compute or that need a stable identity for memoized consumers.

## Details
- Mechanism: on the first render, `useMemo` runs `fn` and stores the result; on later renders it compares the dependencies and returns the stored result if they are unchanged, recomputing only when they change. The two jobs it does: (1) save recomputation work, and (2) provide a referentially stable value (a filtered array, a parsed object) so `React.memo` children and effect dependency arrays see the same reference across renders. Both jobs are void unless something downstream benefits — a cheap computation memoized for itself is overhead.
- Concrete examples: filtering and sorting a 10,000-row table only when the rows or the sort key change; parsing a large JSON blob once per input change; building a stable `options` array for a memoized select component; deriving a config object passed to a chart so the chart does not re-render on every parent render.
- Failure modes: the classic failures are dependency arrays that lie — missing deps make the memoized value stale (the "frozen filter" bug), and over-broad deps (an array or object created inline in the dependency list, or a dep that changes every render) recompute every time, negating the cache and adding comparison cost. Memoizing with side effects inside the factory is another trap: `useMemo` may run during a render that is later discarded under concurrency, so factories must be pure. Premature memoization — wrapping every value — adds bookkeeping with no measurable win.
- Operational tradeoffs: `useMemo` trades memory (cached results) and dependency-tracking complexity for recompute savings and stable identities; it pays off when computation is expensive, the component re-renders often, or a memoized boundary depends on the value's identity. The modern trend reduces its need: colocated state narrows re-render scopes, signals track dependencies automatically, and the React Compiler memoizes automatically — leaving hand-written `useMemo` for the cases the compiler cannot infer. The practice rule: measure the computation, keep factories pure, make deps complete, and prefer deriving from state that changes rarely.
- RSIS3/mykb relevance: the dashboard's derived telemetry (aggregates over pulses) is exactly what `useMemo`-style caching protects: recompute only when the raw records or the selected window change, mirroring RSIS3's rule that derived metrics cache until their inputs change.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/pure-components|Pure Components]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/re-render-causes|Re-Render Causes]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/context-rendering|Context and Rendering]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — related coverage in the same cluster
