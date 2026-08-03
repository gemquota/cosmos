---
type: "concept"
title: "Graceful Enhancement"
description: "Building core experiences that work before layering enhancements"
tags: ["progressive-enhancement", "web", "design", "accessibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Graceful Enhancement

## Summary

Graceful enhancement builds a functional baseline with the most compatible technology, then layers enhanced behavior where supported. It is the counterpart to progressive enhancement and keeps core content working when JS, CSS, or new APIs fail.

## Details
- Mechanism: start from semantic HTML that works with no CSS/JS; add CSS for presentation and JS for interactivity, each wrapped so absence degrades to the baseline rather than a blank page. Feature detection (typeof, 'in', @supports) gates enhancements instead of browser sniffing.
- Concrete example: a wiki search page renders results from server HTML with <noscript>-friendly forms; JS progressively adds live filtering, debounce, and history state — if the bundle fails, users still get working search. A grid layout falls back to stacked blocks when display: grid is unsupported.
- Failure modes: enhancement code that assumes its own success (an element created by earlier JS that never ran); CSS-only enhancements that hide content when a property is half-supported; analytics or tracking breaking the baseline by throwing; and testing only the fully-enhanced path.
- Operational tradeoffs: graceful enhancement costs extra baseline work but hedges against JS failures, flaky CDNs, and accessibility tooling; decide the baseline deliberately (content readable, forms usable, links navigable) and keep enhancement genuinely additive.
- RSIS3/mykb relevance: the wiki browser and dashboard are built as enhanced baselines, so the OKF content remains readable even when the JS bundle or rack API is unavailable.
- Distinction: progressive enhancement is the build order (baseline first), graceful enhancement is the runtime behavior (works when enhanced layers fail); both aim at the same resilient outcome.
- Testing: disable JS and CSS in turn to verify the baseline remains navigable; add error boundaries so an enhancement exception does not tear down the whole page.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/evergreen-browsers|Evergreen Browsers]]
- [[wiki/web-platforms/caniuse-practice|Can I Use in Practice]]
- [[wiki/web-platforms/polyfills-practice|Polyfills in Practice]]
- [[wiki/web-platforms/web-standards|Web Standards]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
