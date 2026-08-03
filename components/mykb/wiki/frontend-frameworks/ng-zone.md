---
type: "concept"
title: "NgZone"
description: "Angular's change-detection triggering zone wrapper"
tags: ["angular", "change-detection", "zones", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# NgZone

## Summary
NgZone is Angular's zone-based change-detection trigger: it patches browser async APIs (timers, promises, XHR, events) so that when any async callback runs, Angular knows something may have changed and runs change detection over the component tree. It is the mechanism that made classic Angular "just work" without explicit reactivity, and its overhead is the reason Angular is moving to a zoneless, signal-based model.

## Details
- Mechanism: zone.js monkey-patches asynchronous APIs so every task executes inside a patched zone; NgZone wraps the app in a zone and tracks task scheduling. When a task completes (a click handler, an HTTP response, a `setTimeout`), the zone fires `onMicrotaskEmpty`, and Angular runs change detection: it walks the component tree comparing template bindings to their previous values and updates the DOM where they differ. Because detection runs on *any* async activity, it is conservative — correct but wasteful, since a timer that changes nothing still triggers a full tree pass.
- Concrete examples: a component increments `count` inside a `setInterval`, and the template updates because the timer callback ran inside the zone; an HTTP fetch updates `data` and the view reflects it after the response callback; code that opts out (`runOutsideAngular`) prevents detection — useful for high-frequency timers that only update a canvas and would otherwise trigger tree-wide checks hundreds of times per second.
- Failure modes: the classic failure is state that changes outside the zone (native WebSockets, `requestAnimationFrame`, third-party libraries, or `runOutsideAngular` callbacks that mutate component state), which silently leaves the UI stale until something else triggers detection. The performance failure is zone overhead: every patched API call pays a bookkeeping cost, and every microtask can trigger a full change-detection pass, which is why large apps historically fought `ExpressionChangedAfterItHasBeenChecked` errors and tuned `OnPush`.
- Operational tradeoffs: zones give automatic correctness at the cost of predictability and overhead; `OnPush` restricts detection to components whose inputs change, trading automatic for explicit. Zoneless Angular (signals + `ChangeDetectionStrategy.OnPush` defaults) removes the patching cost and makes updates granular, but requires components to use signals or `markForCheck` explicitly — a migration with real effort. The modern guidance: prefer signals and `OnPush`, treat zone-dependent code as legacy to be migrated, and keep `runOutsideAngular` only for genuinely zone-hostile loops.
- RSIS3/mykb relevance: NgZone is a case study in eager, conservative invalidation versus precise dependency tracking — the same tradeoff RSIS3 faces between sweeping revalidation of all state versus tracking exactly which loop outputs depend on which inputs; the trend (like Angular's) is toward precise, declared dependencies.

## Related
- [[wiki/frontend-frameworks/solid-js-signals|Solid.js Signals]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/change-detection|Change Detection]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/signal-based-state|Signal-Based State]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/observable-pattern|Observable Pattern]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
