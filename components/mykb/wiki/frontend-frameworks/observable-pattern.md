---
type: "concept"
title: "Observable Pattern"
description: "Streams of values over time with subscription semantics"
tags: ["observables", "streams", "patterns", "state"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Observable Pattern

## Summary
The observable pattern models data as streams of values over time: a producer emits values, subscribers receive them, and operators transform the stream before it reaches consumers. It is the foundation of RxJS and the `async` pipe in Angular, and it solves composition of async events — clicks, responses, timers — with a vocabulary of map, filter, merge, and switch.

## Details
- Mechanism: an observable is a function that wires a producer to observers: on subscription, the producer starts emitting `next(value)` events until it calls `complete()` or the subscriber unsubscribes; `error()` terminates the stream. Operators return new observables, so `click$.pipe(filter(e => e.button === 0), map(e => e.clientX), throttleTime(100))` composes lazily — no work happens until subscription, and unsubscription tears down the producer (clears timers, aborts requests). This pull-based-on-demand model is what distinguishes observables from promises: multiple values over time, cancellation, and composition.
- Concrete examples: a search box stream `input$` debounced, mapped to a fetch, and switched (`switchMap`) so only the latest request's response is applied; a WebSocket message stream subscribed by a chat component with cleanup on destroy; Angular's `async` pipe subscribes in the template and unsubscribes on destroy; a state store exposes observables so `selectors` push derived slices to components. The pattern also underlies event-sourcing UIs where every state change is an event in a stream.
- Failure modes: the classic failures are unmanaged subscriptions (forgetting to unsubscribe leaks the producer, the component, and its DOM), shared cold observables re-executing per subscriber when a multicast (`shareReplay`) was intended, and error handling gaps — an uncaught `error()` in one subscriber can break the whole stream chain. `switchMap` vs `mergeMap` vs `exhaustMap` misuse is the next tier: wrong flattening strategy produces race conditions (stale responses), duplicated side effects, or dropped legitimate requests.
- Operational tradeoffs: observables scale brilliantly for complex event composition but carry a learning curve and debugging overhead (stack traces through operators, marble-testing for verification). Signals have since absorbed the simple reactivity cases (state derivation with less ceremony), and the pragmatic pattern is coexistence: signals for synchronous derived state, observables for streams and external async events, bridged deliberately. The practice rule: prefer the simplest abstraction that fits — plain state for one-shot values, promises for single async results, observables for streams of events with composition.
- RSIS3/mykb relevance: pulse and telemetry streams are natural observables — each loop emits values over time, and the dashboard subscribes with operators (throttle, sample, switch to latest), mirroring how RSIS3 treats telemetry as an event stream with bounded consumption.

## Related
- [[wiki/frontend-frameworks/solid-js-signals|Solid.js Signals]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/rxjs-practice|RxJS in Practice]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/angular-signals|Angular Signals]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/ng-zone|NgZone]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — related coverage in the same cluster
- [[wiki/web-platforms/state-management|State Management]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
