---
type: "concept"
title: "DOM API"
description: "Document tree, nodes, traversal, and manipulation"
tags: [dom", "javascript", "web-apis", "browser", "html"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model", "https://dom.spec.whatwg.org/"]
---

# DOM API

## Summary
The Document Object Model is the browser's in-memory tree of HTML and XML nodes, exposed through interfaces such as Document, Element, and Node. JavaScript uses the DOM API to find, read, create, and mutate the page, and the browser reflects those changes into rendering. It is the lowest common denominator every frontend framework ultimately targets.

## Details
- Node types: elements, text nodes, comments, and document fragments all live in one tree with shared Node methods.
- Traversal and lookup: querySelector, closest, children, and parentElement cover most tree walking without brittle indexes.
- Manipulation: createElement, appendChild, insertBefore, and innerHTML mutate structure; textContent avoids parsing HTML.
- Fragments and batching: DocumentFragment lets code build many nodes and commit one change, cutting reflow cost.
- Events: addEventListener, bubbling and capture phases, and event delegation reduce per-element listeners.
- Performance: each DOM mutation can invalidate layout; frameworks use reconciliation or signals to batch work deliberately.

## Related
- [[wiki/frontend/shadow-dom|Shadow DOM]] — encapsulated subtrees built on the same node model
- [[wiki/frontend/virtual-dom|Virtual DOM]] — an in-memory tree synced to the real DOM
- [[wiki/frontend/reflow-repaint|Reflow and Repaint]] — the cost of DOM mutation
- [[wiki/frontend/semantic-html|Semantic HTML]] — meaningful structure the DOM mirrors
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — broader web-platform notes
- [[wiki/web-platforms/web-apis|Web APIs]] — the DOM as one API family among many
