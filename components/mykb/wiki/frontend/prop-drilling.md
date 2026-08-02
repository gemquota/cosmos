---
type: "concept"
title: "Prop Drilling"
description: "Passing data through component trees and context alternatives"
tags: [react", "props", "context", "component-architecture", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://react.dev/learn/passing-data-deeply-with-context", "https://react.dev/learn/passing-props-to-a-component"]
---

# Prop Drilling

## Summary
Prop drilling is passing data down through intermediate components that do not use it, only forward it. Shallow trees make it harmless; deep trees turn it into ceremony that couples every layer to the data shape. Context, composition, and stores are the standard alternatives when drilling gets painful.

## Details
- Symptom: components accept props purely to pass them deeper, adding noise and making refactors touch many files.
- Context: React context (and similar provider models) skips intermediate components, but updates re-render consumers broadly.
- Composition: passing the rendered children down instead of the data avoids drilling entirely — the children slot pattern.
- Stores: global or server state gives components direct access, at the cost of indirection and testing complexity.
- Threshold: drilling two or three levels is usually fine; revisit when props outnumber local concerns.
- Trade-off: context and stores hide data flow, so prefer explicit props for genuinely local, short-distance data.

## Related
- [[wiki/frontend/component-composition|Component Composition]] — the children-slot alternative
- [[wiki/frontend/state-management-patterns|State Management Patterns]] — stores as alternatives
- [[wiki/frontend/render-props|Render Props]] — an older sharing mechanism
- [[wiki/frontend/controlled-uncontrolled|Controlled vs Uncontrolled]] — prop-driven value flow
- [[wiki/web-platforms/state-management|State Management]] — platform context
- [[wiki/frontend/reactive-state|Reactive State]] — signals reaching deep components
