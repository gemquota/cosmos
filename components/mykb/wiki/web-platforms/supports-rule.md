---
type: "concept"
title: "@supports Rule"
description: "Conditional CSS based on property and value support"
tags: ["css", "supports", "standards", "progressive-enhancement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# @supports Rule

## Summary

The @supports rule (feature queries) conditionally applies CSS based on engine capability, enabling progressive enhancement in stylesheets. It answers parse-time capability questions that browserslist cannot.

## Details
- Mechanism: @supports (display: grid) { ... } applies the block only if the declaration parses and is supported; and/or/not combine conditions; selector() and font-tech() extend it to selector and font-feature checks. Because it is evaluated at parse time, it complements runtime JS detection and build-time browserslist.
- Concrete example: @supports (gap: 1rem) { .grid { display: grid; gap: 1rem; } } with a fallback that uses margins outside the block keeps old engines functional; @supports not (selector(:has(a b))) gates :has-dependent enhancements; font-tech(color-COLRv1) gates colorful font use.
- Failure modes: checking a property that parses but misbehaves in specific engines (support ≠ correct rendering — grid had years of partial bugs); ordering — fallbacks declared after the enhanced rule overwrite it in supporting browsers; testing only in the newest engine; and using @supports where runtime capability (WebGL, IndexedDB) is the real gate.
- Operational tradeoffs: feature queries keep stylesheets resilient but duplicate rules, so keep fallbacks minimal and enhancements additive; combine with browserslist for syntax-level decisions and reserve @supports for genuine behavioral gates.
- RSIS3/mykb relevance: the wiki dashboard gates grid, container queries, and color-mix behind @supports, keeping telemetry usable in embedded WebViews without JS detection.
- Query-value fallback: pairs of @supports blocks should be ordered fallback-first so non-supporting engines get the safe rule before the enhanced block overrides it.
- Testing matrix: CI can run a CSS compatibility matrix per support tier to catch ordering and partial-support regressions across the documented browser baseline.
- Runtime gap: @supports checks parse-time support, not runtime capability — WebGL, storage, and network features still need JS detection; keep the two mechanisms in their lanes.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/media-queries-practice|Media Queries in Practice]]
- [[wiki/web-platforms/feature-queries|CSS Feature Queries]]
- [[wiki/web-platforms/supports-rule|@supports Rule]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-standards|Web Standards]]
