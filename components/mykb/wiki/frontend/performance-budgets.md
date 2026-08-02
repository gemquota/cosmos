---
type: "concept"
title: "Performance Budgets"
description: "Setting and enforcing size, time, and count limits"
tags: [performance", "budgets", "ci", "optimization", "engineering"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/performance-budgets-101", "https://web.dev/articles/incorporate-performance-budgets-into-your-build-tooling"]
---

# Performance Budgets

## Summary
A performance budget is a fixed limit on a measurable quantity — maximum JavaScript size, request count, LCP time, or image weight — that a team agrees not to exceed. Budgets turn performance from a vague aspiration into an enforced contract, usually checked in CI so regressions fail the build before shipping.

## Details
- Budget types: milestone budgets (LCP under 2.5s), weight budgets (bundle under 200KB gzipped), and count budgets (under 20 requests).
- Enforcement: Lighthouse CI, bundlesize, and webpack performance hints compare metrics or sizes against thresholds per commit.
- Baseline setting: measure current p75 field data first, then set budgets slightly better than today to force improvement.
- Granularity: per-route budgets catch one heavy page hiding behind an average; vendor and first-party budgets separate concerns.
- Culture: budgets work when they are realistic, reviewed, and tied to business metrics; unenforced budgets decay.
- Remediation: when a budget trips, prune dependencies, split chunks, or optimize images rather than raising the limit reflexively.

## Related
- [[wiki/frontend/bundle-analysis|Bundle Analysis]] — measuring what budgets constrain
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — milestone budgets track these
- [[wiki/frontend/code-splitting|Code Splitting]] — the fix for weight overruns
- [[wiki/frontend/image-optimization|Image Optimization]] — image weight budgets
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — enforcing budgets in pipelines
- [[wiki/devops-infra/github-actions|GitHub Actions]] — running budget checks per PR
