---
type: "concept"
title: "Re-Render Causes"
description: "The inputs that trigger component re-renders"
tags: ["react", "rendering", "performance", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Re-Render Causes

## Summary
Re-render causes are the inputs that make a React component render again: local state updates, context value changes, and parent re-renders (props). Understanding them is the core of React performance debugging, because most re-render storms come not from "too much state" but from reference churn — new object identities that trigger renders even when the content is identical.

## Details
- Mechanism: a component re-renders when (1) its own state changes via `setState` or a reducer dispatch, (2) a context it consumes changes value, or (3) its parent re-renders — because parent renders produce new prop references by default, children re-render unless they are memoized. `React.memo` breaks cause (3) by comparing props, but only shallowly by reference: a parent that builds `{ items }` or `[1,2,3]` inline creates new references every render, defeating the memo. State updates with the same value (`setCount(0)` when already 0) can still re-render unless the value is referentially identical, which is why `useState` bails out only on `Object.is` equality.
- Concrete examples: a typing input at the top of a page re-renders a 500-node tree because each keystroke creates a new `items` array passed down; a `useEffect`-driven fetch sets state on every keystroke until debounced; a component that reads one field of a large context object re-renders on every field change; a `React.memo` list item still re-renders because the parent passes a new `onClick={() => ...}` inline (fixed with `useCallback`).
- Failure modes: the classic failure is chasing re-renders in the wrong place — memoizing children while the parent passes unstable props, or adding `useMemo` for values that are cheap to recompute. Profiling without attribution is the other trap: the React DevTools Profiler shows render counts, but attributing the storm to its cause (unstable props, context, state location) requires tracing prop identities. Infinite render loops from state-set-in-render and stale dependency arrays are the severe variants.
- Operational tradeoffs: the fixes are structural, not mechanical: colocate state with its consumers (so keystrokes re-render only the input), stabilize props with `useCallback`/`useMemo` for memoized boundaries, split or slice contexts, and let selectors subscribe to slices. The tradeoff is that each optimization adds indirection; the practice rule is to profile first, fix the top offender, and re-measure, because premature memoization everywhere makes the code harder to read without measurable wins.
- RSIS3/mykb relevance: re-render attribution is dependency analysis: knowing exactly which UI consumers depend on which slices of state is the same mapping RSIS3 keeps between registry entries and loop outputs, and the discipline (trace the dependency, fix at the source) applies to both.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/context-rendering|Context and Rendering]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/selector-libraries|Selector Libraries]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/derived-state|Derived State]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — related coverage in the same cluster
