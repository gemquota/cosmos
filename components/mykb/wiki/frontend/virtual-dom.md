---
type: "concept"
title: "Virtual DOM"
description: "In-memory UI trees with diffing and reconciliation"
tags: [virtual-dom", "react", "rendering", "reconciliation", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://vuejs.org/guide/extras/rendering-mechanism.html", "https://react.dev/learn"]
---

# Virtual DOM

## Summary
A virtual DOM is a lightweight, in-memory JavaScript tree describing what the UI should look like. On state changes, the framework builds a new tree, diffs it against the previous one, and applies the minimal set of real DOM mutations. React and Vue use this model; libraries like Preact and Inferno optimize it further.

## Details
- Diffing: the reconciliation pass compares element type, props, and children to compute edits instead of rebuilding the page.
- Keys: stable keys help the diff match list items across renders, preserving state and avoiding full remounts.
- Batching: updates are coalesced per frame, so multiple state changes produce one commit rather than many reflows.
- Cost: the diff itself consumes main-thread time; large trees and frequent updates can outweigh the DOM savings.
- Alternatives: compilers (Svelte) and fine-grained signals (Solid, Angular) skip virtual DOM by writing targeted DOM updates.
- Modern trend: frameworks keep the concept but move work to compile time, memoization, and signals.

## Related
- [[wiki/frontend/dom-api|DOM API]] — the real tree the virtual DOM syncs to
- [[wiki/frontend/reactive-state|Reactive State]] — signals as a virtual-DOM alternative
- [[wiki/frontend/component-composition|Component Composition]] — how UIs become diffable trees
- [[wiki/frontend/hydration|Hydration]] — reconciling virtual DOM over server HTML
- [[wiki/web-platforms/component-architecture|Component Architecture]] — where the model comes from
- [[wiki/frontend/unidirectional-data-flow|Unidirectional Data Flow]] — the state model virtual DOM frameworks expect
