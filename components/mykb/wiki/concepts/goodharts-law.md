---
type: "concept"
title: "Goodhart's Law"
description: "When a metric becomes a target, it ceases to be a good measure"
tags: ["goodhart", "metrics", "eval", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Goodhart%27s_law", "https://en.wikipedia.org/wiki/Campbell%27s_law"]
---

# Goodhart's Law

## Summary
Goodhart's law — 'when a measure becomes a target, it ceases to be a good measure' — describes how optimizing any proxy metric corrupts the information it carries. It underlies reward hacking, eval contamination, and dashboard gaming in organizations.

## Details
- **Variants** — Campbell's law (social side) and the distinction between Goodhart regimes: adversarial (someone games the metric) vs non-adversarial (the metric drifts as a side effect).
- **In ML** — RLHF reward models, benchmark scores, and even telemetry dashboards all decay when optimized directly.
- **Defense patterns** — diversify metrics, keep evaluators external, use ensembles, and audit for divergence between metric and intent.
- **Worked example** — a wiki whose 'health' metric is link coverage: pages start linking to anything, and coverage stops meaning quality.
- **RSIS3 relevance** — improvement metrics in the pulse loop are deliberately plural and checked against practices, not maximized blindly.

## Related
- [[wiki/concepts/specification-gaming|Specification Gaming]] — gaming the spec
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — Goodhart on benchmarks
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — metrics that must resist Goodhart
- [[wiki/concepts/evals-gaming|Evals Gaming]] — gaming the evaluation
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub Architecture & Snapshot Hygiene]] — social analogue
- [[wiki/concepts/calibration|Calibration]] — keeping measures honest
