---
type: "concept"
title: "CSS Feature Queries"
description: "@supports blocks gating styles on capability"
tags: ["css", "supports", "progressive-enhancement", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Feature Queries

## Summary

@supports lets CSS apply rules conditionally on engine capability, giving progressive enhancement a native syntax. It answers "can this engine do this?" at parse time, complementing JS feature detection and browserslist.

## Details
- Mechanism: @supports (property: value) { ... } applies the block when the declaration parses and is supported; operators and/or/not combine conditions, and selector() checks selector support in newer engines. Unknown or invalid declarations make the condition false, so the block is skipped safely.
- Concrete example: @supports (display: grid) { .cards { display: grid; } } with a flexbox fallback outside the block keeps the layout functional in legacy engines; @supports selector(:has(*)) gates a :has-based enhancement behind engines that parse it.
- Failure modes: checking a property that parses everywhere but behaves differently (support ≠ correct behavior, e.g. older CSS grid bugs); writing fallbacks after the enhanced rule so the fallback overwrites it in supporting browsers; testing only in the newest engine; and forgetting that @supports evaluates at parse time — it cannot detect runtime capability (WebGL, storage).
- Operational tradeoffs: feature queries are the CSS-native way to layer enhancements, but they duplicate rules and raise maintenance; keep the fallback minimal (functional baseline) and the enhancement additive. Combine with browserslist for build-time syntax decisions and @supports for runtime choices.
- RSIS3/mykb relevance: dashboard styles use @supports for grid, container queries, and color-mix, keeping the telemetry UI usable on older in-app browsers without a JS dependency.
- Progressive fallback ordering: declare the baseline rule first, then the @supports-enhanced rule; a supporting engine uses the enhanced block, a legacy engine keeps the baseline, and the cascade makes the intent explicit.
- Selector support check: @supports selector(:has(*)) gates behavior that property checks cannot express; verify selector() support in your target engines before relying on it for progressive enhancement.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/supports-rule|@supports Rule]]
- [[wiki/web-platforms/media-queries-practice|Media Queries in Practice]]
- [[wiki/web-platforms/feature-queries|CSS Feature Queries]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-standards|Web Standards]]
