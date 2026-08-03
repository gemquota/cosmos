---
type: "concept"
title: "Can I Use in Practice"
description: "Using caniuse data to decide feature support targets"
tags: ["browsers", "compatibility", "tooling", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Can I Use in Practice

## Summary

caniuse.com maps browser support for web platform features, but treating its tables as truth without context leads to bad decisions. Good caniuse practice combines support data with your real traffic, fallback strategy, and risk tolerance.

## Details
- Mechanism: caniuse records per-feature support across browser versions with notes, prefix flags, and usage estimates, served through the website and the browserslist ecosystem. The data answers "when can I ship this?" only when filtered by the browsers your users actually run.
- Concrete example: a dashboard feature gated on :has() looks safe at 95% global support but breaks a cohort using an embedded WebView; checking caniuse's "current versions" plus your analytics baseline turns a headline percentage into an actionable rollout decision.
- Failure modes: treating global usage stats as your traffic; ignoring partial implementation flags (e.g. a feature behind a pref); missing that a property parses everywhere but behaves differently; and assuming caniuse is current — data lags new releases and pref trials.
- Operational tradeoffs: feature queries and polyfills buy time to adopt new APIs; caniuse should feed an explicit support matrix (browserslist in build tooling) rather than be consulted ad hoc. Document which tier each feature requires — progressive enhancement baseline vs. enhanced-only.
- Pair with feature detection at runtime: caniuse predicts, but @supports and capability probes confirm what the actual device can do.
- RSIS3/mykb relevance: support matrices are stored as wiki notes so the acquisition loop can cite a canonical browser baseline instead of re-deriving it each cycle.
- Baseline pinning: encode the support matrix in browserslist and lock caniuse data version in CI so a support answer today does not change silently next week; treat the matrix as a reviewed document.
- Field verification: pair caniuse with real usage analytics; a feature that is 98% supported globally but 40% in your embedded WebView cohort is not shippable without a fallback.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/polyfills-practice|Polyfills in Practice]]
- [[wiki/web-platforms/graceful-enhancement|Graceful Enhancement]]
- [[wiki/web-platforms/evergreen-browsers|Evergreen Browsers]]
- [[wiki/web-platforms/web-standards|Web Standards]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
