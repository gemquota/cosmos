---
type: "concept"
title: "Concurrent Rendering"
description: "Interruptible rendering that keeps UIs responsive"
tags: ["react", "concurrency", "rendering", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Concurrent Rendering

## Summary
Concurrent rendering is React's model of interruptible rendering: a render can be paused, resumed, or abandoned, letting urgent updates (typing, clicks) jump ahead of lower-priority work (large list updates, off-screen rendering). It is the foundation of `startTransition`, `useDeferredValue`, and Suspense-driven streaming, and it changes how and when component functions run.

## Details
- Mechanism: in the concurrent model, rendering a component tree is a computation performed on a scheduler with priority levels. When an urgent update arrives mid-render, the scheduler interrupts the current work, commits the urgent update first, and then resumes or discards the lower-priority render. Because renders can be interrupted, React may call a component function multiple times, discard the results, and re-run it later — a render must therefore be pure and side-effect-free (effects belong in `useEffect`, not in the render body). The commit phase, which touches the DOM, remains atomic.
- Concrete examples: a search box where the input update is urgent and the results-list update is wrapped in `startTransition` — keystrokes stay responsive even when filtering 10,000 items, because the filter render can be interrupted and deferred; `useDeferredValue` does the same for a value derived from state; Suspense lets a transition stay on the current screen while a new route's data loads, avoiding a blank fallback flash. Server components and streaming HTML builds on the same scheduling so shells paint before slow data resolves.
- Failure modes: the classic failures are side effects in render (interruptible renders make them run an unpredictable number of times), tests that assume renders are synchronous (concurrent updates need `act()` and may need multiple passes), and overusing transitions so that even trivial updates become delayed, causing visible lag in inputs. Unbounded deferred work can also starve urgent work if priorities are mislabeled, and libraries that read state during render without subscribing (breaking render purity) misbehave under interruption.
- Operational tradeoffs: the payoff is a perceptually faster UI — urgent interactions never wait on big renders — and built-in backpressure for expensive derived work. The costs are a stricter programming model (purity, `act()` in tests, understanding when renders actually happen) and a scheduler whose behavior is harder to predict than the old synchronous model. Teams adopt it incrementally: wrap the expensive-but-deferrable updates in transitions first, keep renders pure, and measure with the Profiler to confirm the wins.
- RSIS3/mykb relevance: concurrent rendering is scheduling with priorities, exactly the way RSIS3's L2/L3 loops prioritize urgent corrections over long-running improvements; the discipline of pure, restartable work units maps directly to idempotent loop steps that can be re-run safely.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/starttransition|startTransition]]
- [[wiki/frontend-frameworks/suspense-practice|Suspense in Practice]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
- [[wiki/web-platforms/state-management|State Management]]
