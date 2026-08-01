---
type: "concept"
title: "Web Performance Optimization"
description: "Making web pages load, render, and respond faster through measurement and targeted fixes"
tags: ["performance", "web-vitals", "optimization", "loading"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/Performance"]
---

# Web Performance Optimization

## Summary
Web performance optimization (WPO) is the discipline of measuring and improving how fast a site loads and responds. MDN frames it as both art and science: objective metrics — LCP, INP, CLS — anchored to user experience rather than vanity numbers.

## Details
- Core metrics (Core Web Vitals): Largest Contentful Paint (loading), Interaction to Next Paint (responsiveness), and Cumulative Layout Shift (visual stability).
- The critical path: fewer, smaller resources; efficient HTML/CSS; lazy images; preconnect and preload hints; and a fast server (TTFB).
- Rendering bottlenecks are measured in the browser: DevTools performance traces and Lighthouse audits pinpoint them.
- JavaScript is the usual suspect: bundle size, main-thread work, and long tasks degrade INP; code splitting and deferral help.
- Performance is a budget, not a one-time fix: enforce budgets in CI and monitor RUM (real-user monitoring) in production.
- RSIS3 relevance: the mykb dashboard must stay snappy on a modest device; the same disciplines apply.
- Worked example: a 400 KB hero image cut to 40 KB WebP moved LCP from 4.2s to 1.8s on a test device.

## Related
- [[wiki/web-platforms/browser-engines|Browser Engines]] — engine behavior determines optimization levers
- [[wiki/web-platforms/web-standards|Web Standards]] — modern standards enable lighter pages
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]] — measurement precedes optimization
- [[wiki/dev-tools/profilers|Profilers]] — browser profilers find the hotspots
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — offline caching is a performance strategy
- [[wiki/devops-infra/observability|Observability]] — RUM feeds the optimization loop
- [[wiki/frontend/static-site-generation|Static Site Generation]] — pre-rendering trims the critical path
