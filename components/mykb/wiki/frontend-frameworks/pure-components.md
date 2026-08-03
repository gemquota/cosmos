---
type: "concept"
title: "Pure Components"
description: "Components that re-render only when props and state change"
tags: ["react", "performance", "components", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Pure Components

## Summary
A pure component renders the same output for the same props and state, and nothing else: no reading `Date.now()`, `Math.random()`, the DOM, or external mutable globals during render. Purity is what makes React's optimizations sound — memoization, `shouldComponentUpdate`, and interruptible concurrent rendering all assume that a render is a deterministic function of its inputs.

## Details
- Mechanism: React treats a component as a function `(props, state) -> UI`. Pure components touch only their inputs and produce no side effects during render (no DOM writes, no subscriptions, no state updates); side effects belong in effects. Because the output is a pure function of inputs, React can safely skip re-rendering when inputs are unchanged (`React.memo` compares props by reference) and can discard and restart renders under concurrency without observable difference. Purity also makes components trivially testable: render with props, assert output, no mocks needed.
- Concrete examples: a `memo`-wrapped user card re-renders only when its `user` prop reference changes; a list row with stable props skips re-render even when its parent re-renders fifty times; a chart component that receives data as props renders identically for the same data, enabling snapshot tests; a component that needs "now" computes it once in an effect or from a prop rather than in render, so re-renders do not shift the displayed time.
- Failure modes: the classic failures are impure renders: `Math.random()` or `Date.now()` in render produces different output for the same props (breaking memoization and concurrent rendering's restart safety), reading or writing `document`/`window` during render (breaking SSR and tests), and mutating props or shared state during render (causing render loops and inconsistent trees). Impurity is often subtle — calling `Array.sort()` on a props array sorts in place, mutating the prop; logging during render fires an unpredictable number of times under concurrency.
- Operational tradeoffs: strict purity is the contract React pays off on: it enables `memo`, `useMemo`, and concurrent features, and it simplifies testing and debugging. The cost is a discipline shift — computations like timestamps, random IDs, and subscriptions must be lifted to effects, events, or props. The practice rule: if a value is needed in render, derive it from props/state or store it; if it must be computed once, do it in an effect or constructor; and treat any render that reads a clock or a DOM as a bug.
- RSIS3/mykb relevance: pure rendering is functional determinism — the same discipline RSIS3 demands of loop steps (same inputs, same outputs, no hidden state), which is what makes checkpoints and replays correct; the dashboard's widgets should render purely from telemetry so identical data always paints an identical view.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/re-render-causes|Re-Render Causes]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/context-rendering|Context and Rendering]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/selector-libraries|Selector Libraries]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — related coverage in the same cluster
