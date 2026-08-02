---
type: "concept"
title: "DOM and CSSOM"
description: "The object models behind HTML and CSS that drive rendering and scripting"
tags: ["dom", "cssom", "html", "css", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model", "https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model"]
---
# DOM and CSSOM

## Summary
The DOM is the browser's tree of nodes representing a document; the CSSOM is the parallel model of stylesheet rules and computed styles. JavaScript mutates the DOM; the CSSOM decides how those nodes look. Both feed the rendering pipeline and the accessibility tree.

## Details
- **DOM structure** — element, text, and comment nodes with parent/child relationships; scripting and layout both walk this tree.
- **CSSOM** — parsed rules cascade into computed styles per node; `getComputedStyle` and style APIs read and mutate it.
- **Interaction** — DOM mutations invalidate styles and layout; batch writes and reads to avoid layout thrashing.
- **Shadow DOM** — encapsulated subtrees keep component internals separate from the document tree.
- **Worked example** — a virtualized list in the mykb UI reads bounding rects once per frame, batches DOM writes, and uses containment to isolate layout.
- **Relevance** — agents manipulating pages through browser automation are fundamentally driving the DOM and reading the CSSOM.

## Related
- [[wiki/web-platforms/dom-clobbering|DOM Clobbering]] — adjacent concept in this wiki
- [[wiki/web-platforms/dom-xss|DOM XSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/repaint-vs-reflow|Repaint vs Reflow]] — adjacent concept in this wiki
- [[wiki/web-platforms/layout-triggers|Layout Triggers]] — adjacent concept in this wiki
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — existing coverage
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
