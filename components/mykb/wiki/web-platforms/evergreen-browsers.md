---
type: "concept"
title: "Evergreen Browsers"
description: "Self-updating browsers and their implications for support policy"
tags: ["browsers", "web", "standards", "compatibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Evergreen Browsers

## Summary

Evergreen browsers auto-update silently, collapsing the legacy-support tail. Relying on them means targeting the current-and-previous release set, which shrinks polyfill burden but still requires deciding a baseline and testing real devices.

## Details
- Mechanism: Chrome, Edge, Firefox, and Safari ship continuous updates; users on the default path run recent engines without choosing. Evergreen support matrices therefore track "current release minus one" (or a fixed support window like the last 24 months) instead of ancient versions.
- Concrete example: a team drops IE11 and declares baseline = last 2 versions of Chrome/Edge/Firefox/Safari plus iOS Safari; they remove most polyfills, use modern CSS freely, and encode the baseline in browserslist so build tooling targets matching syntax.
- Failure modes: assuming evergreen means uniform — enterprise-managed browsers can lag months; embedded WebViews (in-app browsers) freeze the engine at app release time and are not evergreen at all; Safari on older iOS devices cannot update independently of the OS; and auto-updates can ship engine regressions that surface in production before your matrix adjusts.
- Operational tradeoffs: evergreen baselines cut bundle size and QA matrix, but they push risk onto the user's environment; keep feature detection and @supports for genuinely new APIs, and monitor analytics for aging engine cohorts instead of trusting the average.
- RSIS3/mykb relevance: the dashboard's browser baseline is a documented wiki note paired with analytics cohorts, so new CSS features are adopted only after the loop checks real usage data.
- WebView reality: embedded in-app browsers freeze engine versions at app release; if your audience uses them, the evergreen assumption fails and the support matrix must include the frozen engine explicitly.
- Update cadence policy: decide whether to support N-2 or a rolling 24-month window, and encode it in browserslist plus the documented baseline; the decision belongs in the wiki, not in individual developers' heads.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/caniuse-practice|Can I Use in Practice]]
- [[wiki/web-platforms/polyfills-practice|Polyfills in Practice]]
- [[wiki/web-platforms/graceful-enhancement|Graceful Enhancement]]
- [[wiki/web-platforms/web-standards|Web Standards]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
