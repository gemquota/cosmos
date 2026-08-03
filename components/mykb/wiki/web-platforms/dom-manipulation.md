---
type: "concept"
title: "DOM Manipulation"
description: "Reading and changing the Document Object Model to make pages interactive"
tags: ["dom", "javascript", "frontend", "document"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# DOM Manipulation

## Summary

DOM manipulation is the art of updating the document efficiently and safely. Correct practice centers on minimal, batched writes, event delegation, and treating the DOM as a render target rather than a data store.

## Details
- Mechanism: the DOM is a live tree; reads and writes both cost, and interleaving them forces layout thrash (layout is computed lazily, so a write then a read forces a synchronous reflow). Batching reads and writes — or using the browser's built-in batching via rAF — keeps layout passes to one per frame.
- Concrete example: building a 1,000-row table by appending rows one by one in a loop causes 1,000 layouts; building a DocumentFragment off-DOM and inserting once, or setting innerHTML once, collapses it to a few layouts. Event delegation attaches one listener on a container instead of one per row, surviving row re-renders.
- Failure modes: innerHTML with unsanitized data opens XSS; direct references to removed nodes (detached trees) leak memory in long sessions; layout thrash from read-write interleaving janks scrolling; and framework-less code mutating state in the DOM makes data sync bugs — keep a single source of truth and re-render declaratively.
- Operational tradeoffs: imperative manipulation is fastest when tuned but error-prone at scale; declarative frameworks (React, lit, signals) trade a diffing layer for consistency. For dashboards and charts, mutate the minimum subtree and let the compositor handle motion.
- RSIS3/mykb relevance: the wiki browser renders search results and graph nodes through a small renderer that batches DOM writes and delegates events, documented in this node as the baseline for loop-generated UI.
- Framework comparison: jQuery-era chains obscure reads/writes; modern signals and template rendering make batching automatic, but raw listeners and manual append calls in a signal effect still interleave — batch explicitly.
- Testing: DOM tests should assert on the rendered tree, not implementation details of manipulation, so refactors to batching or fragments stay regression-safe.

## Related
- [[wiki/web-platforms/web-apis|Web APIs]] — the DOM is the core web API
- [[wiki/web-platforms/component-architecture|Component Architecture]] — components wrap DOM manipulation
- [[wiki/web-platforms/css-layout|CSS Layout]] — layout works on the DOM tree
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — typed DOM queries reduce selector bugs
- [[wiki/testing/golden-tests|Golden Tests]] — rendered DOM is golden-testable
