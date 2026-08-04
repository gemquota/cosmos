---
type: "entity"
title: "RxJS in Practice"
description: "Reactive extensions for composing async event streams"
tags: ["rxjs", "observables", "streams", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# RxJS in Practice

## Summary
RxJS brings functional reactive programming to JavaScript: everything is an observable stream, and operators like `map`, `filter`, `merge`, `switchMap`, and `debounceTime` compose streams declaratively. It is deeply embedded in Angular (HttpClient, `async` pipe, reactive forms), and its practice is defined by two disciplines: composing with the right operators and never leaking subscriptions.

## Details
- Mechanism: an observable is a lazy producer; `pipe(...)` chains operators that transform each stream. Cold observables run per subscription (each subscriber triggers the producer), while `shareReplay`/`multicast` make them hot or shared. Operators do the heavy lifting: `switchMap` cancels the previous inner subscription when a new outer value arrives (the correct choice for search-as-you-type), `mergeMap` runs inner streams concurrently, `concatMap` serializes them, and `exhaustMap` ignores new triggers while one is running. Angular's `async` pipe subscribes and unsubscribes automatically; manual `subscribe` calls need `takeUntil(destroy$)` or the component leaks.
- Concrete examples: a search input stream `input$` piped through `debounceTime(300)`, `distinctUntilChanged`, and `switchMap(term => api.search(term))` so only the latest request's result applies; a WebSocket stream piped to a component and torn down with `takeUntil`; a reactive form's `valueChanges` stream debounced to autosave; an `interval` stream sampling a status endpoint with `switchMap` to avoid overlapping polls.
- Failure modes: the classic failures are subscription leaks (every manual subscription that outlives the component keeps both alive), operator misuse (using `mergeMap` where `switchMap` is needed, producing stale-response races), and swallowing errors (an uncaught error in a stream kills it, and subsequent values never arrive — the `catchError` must return a stream, not a value). Cold/hot confusion causes duplicated HTTP requests or missed events, and over-engineering tiny streams with dozens of operators makes code unreadable and hard to marble-test.
- Operational tradeoffs: RxJS is unmatched for complex, event-heavy logic (typeaheads, realtime feeds, drag-and-drop, state-machine-style flows) and its marble-testing model is rigorous; the cost is a steep learning curve, operator proliferation, and stack-trace opacity. Angular's shift toward signals is narrowing RxJS's role to external async sources and interop, with signals for derived state — the pragmatic pattern is to use each where it fits rather than forcing streams everywhere.
- RSIS3/mykb relevance: telemetry and pulse streams are the RxJS domain: the dashboard can model daemon events as observables with `throttleTime`/`sample` operators so the UI updates on a bounded cadence, mirroring how RSIS3 bounds telemetry consumption instead of re-rendering per event.

## Related
- [[wiki/frontend-frameworks/solid-js-signals|Solid.js Signals]]
- [[wiki/frontend-frameworks/angular-signals|Angular Signals]]
- [[wiki/frontend-frameworks/ng-zone|NgZone]]
- [[wiki/frontend-frameworks/change-detection|Change Detection]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/state-management|State Management]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
