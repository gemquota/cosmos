---
type: "concept"
title: "startTransition"
description: "Marking React updates as low-priority transitions"
tags: ["react", "concurrency", "updates", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# startTransition

## Summary
`startTransition` marks a state update as non-urgent: `startTransition(() => setResults(filter(list, term)))` tells React the update can be interrupted and deferred so urgent updates (keystrokes, clicks) stay responsive. It is the primary API for opting into concurrent rendering, and `useTransition` adds the `isPending` flag that lets the UI show progress without blocking input.

## Details
- Mechanism: updates inside a transition are scheduled at a lower priority than urgent updates (input, clicks, and layout effects). When an urgent update arrives while a transition render is in progress, React interrupts the transition, commits the urgent update, and resumes or discards the deferred work. `useTransition` returns `[isPending, startTransition]`: `isPending` flips true while the transition render is in flight, so a list can show a subtle "updating" indicator. Because transition renders are restartable, the render must be pure; side effects stay in effects.
- Concrete examples: a search input where `setTerm` is urgent and the results computation is wrapped in `startTransition`, so typing never lags even when filtering 10,000 items; a tab switcher where loading the heavy tab is a transition so the tab chrome responds instantly; `useDeferredValue(term)` as the value-level equivalent, deferring a derived value while keeping the source state urgent; a route change wrapped in a transition so the current screen stays interactive until the new screen's data (Suspense) resolves.
- Failure modes: the classic failures are wrapping the wrong update (making urgent updates like input state into transitions, which delays them and makes typing feel laggy), using transitions for updates that must complete before other work (they can be abandoned, so derived side effects must not depend on them), and missing the `isPending` signal so the UI shows nothing during a long deferred render. Transitions also do not reduce the total work — a 10,000-item filter still computes; they only make the computation interruptible and deferrable.
- Operational tradeoffs: transitions trade a little completion latency for a lot of input responsiveness, which is the right deal for expensive derived UI work. The costs are a stricter purity requirement, testing changes (transitions are async, so `act()` and possibly multiple render passes), and the need to reason about priority — which updates are urgent by nature versus which can wait. The practice rule: keep input and navigation urgent, defer expensive derived renders, and use `isPending` for honest progress UI.
- RSIS3/mykb relevance: transition scheduling is priority-aware work management: RSIS3's loops face the same choice between urgent corrections (L1) and deferrable improvements (L2/L3), and the discipline of interruptible, restartable work units maps directly to idempotent loop steps.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/suspense-practice|Suspense in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/concurrent-rendering|Concurrent Rendering]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/starttransition|startTransition]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
