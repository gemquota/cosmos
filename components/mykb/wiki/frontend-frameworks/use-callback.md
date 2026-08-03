---
type: "concept"
title: "useCallback"
description: "Stable function identities to limit re-renders"
tags: ["react", "memoization", "hooks", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# useCallback

## Summary
`useCallback(fn, deps)` returns a memoized version of a function that changes only when its dependencies change, giving the function a stable identity across renders. Its purpose is not to make the callback itself cheaper — creating a closure is trivial — but to let `React.memo` children skip re-renders by receiving the same function reference.

## Details
- Mechanism: on every render, `useCallback` compares the dependency array to the previous one; if unchanged, it returns the previous function reference; if changed, it returns the new function. Downstream, a `React.memo` child compares props by reference, so a stable callback means the child's props are unchanged and the child skips re-rendering. The identity matters only because of this memoization chain — without a memoized consumer, `useCallback` is pure overhead. `useMemo(() => fn, deps)` is exactly equivalent; `useCallback` is the syntactic sugar for functions.
- Concrete examples: a list of 50 memoized row components receives `onToggle={useCallback((id) => ..., [deps])}`, so toggling one row does not re-render all 50; an effect that subscribes to a WebSocket takes a stable `onMessage` callback so it does not resubscribe on every render; a context value containing a callback stays referentially stable so all context consumers skip re-rendering.
- Failure modes: the classic failures are dependency-array bugs — too few deps (the callback closes over a stale value and "freezes") or too many (a new identity every render, silently defeating the memo); using it where no memoized consumer exists (adding bookkeeping for nothing); and the anti-pattern of wrapping callbacks used only in effects, where the effect's own dependency array is the real lever. Stale-closure bugs from `useCallback` are especially nasty because they appear only when the missing dep changes.
- Operational tradeoffs: `useCallback` trades a small amount of bookkeeping for potentially large re-render savings at memoized boundaries; the cost is dependency discipline and readability. The modern guidance is to use it where a memoized child or a stable-effect dependency needs it, and to let compiler-assisted memoization (React Compiler) or colocated state reduce the need. The measurement rule: if the child tree is big and re-renders frequently, `useCallback` earns its keep; otherwise, skip it.
- RSIS3/mykb relevance: stable callback identities are about minimizing spurious re-execution of dependents — the same concern RSIS3 has when a derived metric re-runs because its input function reference changed without any semantic change; stable, declared dependencies prevent recomputation churn.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/use-memo|useMemo]]
- [[wiki/frontend-frameworks/pure-components|Pure Components]]
- [[wiki/frontend-frameworks/re-render-causes|Re-Render Causes]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
