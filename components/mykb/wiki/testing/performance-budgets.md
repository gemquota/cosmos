---
type: "concept"
title: "Performance Budgets"
description: "Enforcing CI thresholds on bundle size and response times"
tags: ["performance-budgets", "testing", "web-performance", "ci"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/performance-budgets", "https://github.com/GoogleChrome/lighthouse-ci"]
---

# Performance Budgets

## Summary
Performance budgets are explicit thresholds, bundle size, time-to-interactive, and API latency, enforced in CI to keep performance from regressing silently. They make performance a checked-in requirement rather than a hope.

## Details
- Web budgets: JavaScript bundle weight, image bytes, and LCP, TTI, or TBT thresholds.
- Runtime budgets: p99 latency, throughput floors, and error-rate caps.
- Enforce with Lighthouse CI, bundler-size tools, and custom pipeline checks.
- Budgets must map to user outcomes; tune them when features legitimately add cost.
- Alert on regression trends before hard failure via diff thresholds.
- Include dependencies: new packages and assets are the main budget creep source.
- Track budgets in dashboards so teams see headroom at a glance.

## Related
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]] — latency budgets on the tail
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — where budgets are enforced
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — how to meet budgets
- [[wiki/testing/load-testing|Load Testing]] — validating runtime budgets
- [[wiki/devops-infra/error-budgets|Error Budgets]] — reliability budgets alongside speed
- [[wiki/testing/performance-testing|Performance Testing]] — measuring against budgets
