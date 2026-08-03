---
type: "concept"
title: "Dashboards Practice"
description: "Principles for designing monitoring dashboards that answer questions instead of just showing charts"
tags: ["dashboards", "monitoring", "observability", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dashboards Practice

## Summary
Dashboard practice is about structuring charts around decisions: what to watch first, what a healthy range looks like, and what to do when a panel turns red. A good dashboard answers a question in seconds — a bad one shows many charts and answers nothing.

## Details
- Mechanism: organize by use case — an overview tier with golden signals and SLO burn, per-service health, capacity, and incident-specific views — rather than dumping every metric on one page; each panel names its question, its healthy range, and its owner; drill-down links take the viewer from red panel to logs or runbook.
- Concrete example: a service dashboard with four top panels (error rate, latency percentiles, throughput, saturation), an SLO burn strip, and per-endpoint tables; clicking a latency panel opens the traces for that endpoint; an on-call dashboard shows only what to triage first, with the runbook link on each panel.
- Failure modes: dashboard sprawl — dozens of unowned pages that no one reads; panels without context (a number with no healthy range, no units); correlation without causation — charts that move together but lead to wrong conclusions; red panels with no owner or action; dashboards optimized for looks instead of decisions.
- Tradeoffs: a curated dashboard costs curation time but pays in faster triage and shared understanding; the alternative — raw metric explorers — is flexible but slow under incident pressure; the mature pattern is few, owned dashboards per service plus a queryable explorer for the long tail.
- Operational notes: review dashboards in postmortems, prune dead panels, and link every alert to the dashboard panel it represents.
- RSIS3 relevance: a knowledge-health dashboard could watch stub-to-full conversion and link integrity — the same decision-focused structure RSIS3 uses for its own telemetry views.

## Practice
- Keep panels versioned like code: every dashboard change is a reviewed diff, so the board cannot rot silently.
## Related
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]]
- [[wiki/dev-tools/metric-backends|Metric Backends]]
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/dev-tools/slo-budgets|SLO Budgets]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
