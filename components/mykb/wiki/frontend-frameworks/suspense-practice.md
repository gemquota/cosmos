---
type: "concept"
title: "Suspense in Practice"
description: "Declarative waiting states for async component data"
tags: ["react", "suspense", "async", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Suspense in Practice

## Summary
Suspense is React's declarative mechanism for waiting: a component that needs async data "suspends" (throws a promise), and the nearest `<Suspense>` boundary renders its `fallback` until the data resolves. It composes with `React.lazy` for code splitting, data-fetching libraries for server state, and streaming SSR for progressive rendering — turning loading states from per-component `if` branches into a declared tree structure.

## Details
- Mechanism: a component suspends by throwing a thenable; React catches it, finds the nearest `<Suspense fallback={...}>` ancestor, and shows the fallback while the promise resolves, then re-renders the tree with the data. Boundaries nest: each boundary shows its own fallback for its own subtree, so a slow sidebar does not blank the whole page. `useTransition` lets a navigation keep the current screen visible while the next screen's Suspense boundary resolves (`isPending` drives a subtle indicator instead of a spinner). Error handling is deliberately separate: a promise rejection needs an error boundary, not Suspense — one of the most common integration mistakes.
- Concrete examples: `React.lazy(() => import('./HeavyChart'))` wrapped in Suspense shows a skeleton while the chunk loads; a dashboard route fetches data with a data library's `useSuspenseQuery` so the whole route waits on one boundary; a profile page has nested boundaries — the avatar resolves quickly while the analytics panel takes longer; SSR streams the shell immediately and Suspense fills in sections as their data arrives.
- Failure modes: the classic failures are missing error boundaries (a rejected promise under Suspense unmounts the tree with an opaque error), boundaries too large (the whole page shows one spinner because every fetch is under the root boundary), and suspense-unaware libraries (a fetch library that does not integrate suspends never triggers the fallback, or worse, throws in unexpected ways). Over-nesting boundaries fragments the loading UX into flickers, and using Suspense for non-async work adds nothing but indirection.
- Operational tradeoffs: Suspense removes loading-state boilerplate and enables real concurrency features (transitions, streaming), but it changes the async model: code must be written to suspend, data libraries must opt in, and teams must decide boundary placement deliberately. The tradeoff is between fine-grained boundaries (better perceived performance, more complexity) and coarse ones (simpler, blunter). The practice rule: put a boundary at every significant layout region, wrap lazy imports always, pair every Suspense with an error boundary, and use transitions for navigation so the current screen stays interactive.
- RSIS3/mykb relevance: the dashboard's embedded views (wiki browser, knowledge graph) load asynchronously; treating each as a Suspense boundary with a transition preserves interactivity while data streams in — the same progressive-enhancement discipline RSIS3 applies to telemetry rendering.

## Related
- [[wiki/frontend-frameworks/react-ecosystem|React Ecosystem]]
- [[wiki/frontend-frameworks/concurrent-rendering|Concurrent Rendering]]
- [[wiki/frontend-frameworks/starttransition|startTransition]]
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
- [[wiki/web-platforms/state-management|State Management]]
