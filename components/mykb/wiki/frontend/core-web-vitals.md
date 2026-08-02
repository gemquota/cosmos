---
type: "concept"
title: "Core Web Vitals"
description: "User-centric metrics LCP, INP, and CLS"
tags: [performance", "core-web-vitals", "lcp", "inp", "cls"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/vitals", "https://web.dev/articles/inp"]
---

# Core Web Vitals

## Summary
Core Web Vitals are Google's user-centric performance metrics: Largest Contentful Paint measures loading, Interaction to Next Paint measures responsiveness, and Cumulative Layout Shift measures visual stability. Good thresholds are LCP under 2.5 seconds, INP under 200 milliseconds, and CLS under 0.1. They are measured both in the field on real users and in the lab.

## Details
- LCP: when the largest above-the-fold image or text block paints; optimize images, critical CSS, and server response time.
- INP: the longest observed delay between a user interaction and the next paint; replaced FID as the responsiveness metric in 2024.
- CLS: unexpected layout movement from images without dimensions, injected content, and web-font swaps.
- Field data: Chrome User Experience Report (CrUX) aggregates real-device percentiles, typically p75, for origin-level scores.
- Lab tools: Lighthouse and PageSpeed Insights approximate the same metrics with synthetic loads.
- Business impact: vitals correlate with engagement and conversion; the dashboard telemetry can track its own LCP, INP, and CLS.

## Related
- [[wiki/frontend/long-tasks|Long Tasks]] — main-thread work behind poor INP
- [[wiki/frontend/lazy-loading|Lazy Loading]] — LCP and CLS implications
- [[wiki/frontend/critical-css|Critical CSS]] — speeding up LCP
- [[wiki/frontend/animation-performance|Animation Performance]] — CLS-safe motion
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — the broader discipline
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — where vitals get tracked
