---
type: "concept"
title: "Loading States"
description: "Designing for pending data: spinners, progress, placeholders, and optimistic feedback"
tags: ["loading", "ux", "state", "performance", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/fetch", "https://www.nngroup.com/articles/progress-indicators/"]
---
# Loading States

## Summary
Loading states communicate that work is in progress: spinners for indeterminate waits, progress bars for known duration, skeletons for structure previews. Good loading UX answers three questions: what is happening, when will it finish, and can the user do something else meanwhile.

## Details
- **Indeterminate vs determinate** — spinners suit unknown durations; progress bars and percentages suit quantifiable work.
- **Staged loading** — shell first, then content; caching and prefetching shrink the pending window.
- **Cancellation** — let users abort long operations; stale responses must not overwrite newer state.
- **Accessibility** — announce state changes (aria-live); never rely on visual cues alone.
- **Worked example** — the mykb search shows a skeleton list while fetching, with a cancel button for slow queries.
- **Relevance** — loading states are part of the async-state discipline RSIS3 documents for agent outputs.
- **Progress semantics** — indeterminate spinners need aria-busy; determinate progress needs real values; both should be cancelable when the operation supports it.

## Related
- [[wiki/frontend-frameworks/async-state|Async State]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/react-query-practice|TanStack Query Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/derived-state|Derived State]] — adjacent concept in this wiki
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — adjacent concept in this wiki
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/web-platforms/component-architecture|Component Architecture]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
