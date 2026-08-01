---
type: "concept"
title: "Error Budgets"
description: "The allowed failure allowance derived from SLOs that governs release velocity and reliability work"
tags: ["error-budgets", "slo", "sre", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Error Budgets

## Summary
An error budget is the failure allowance an SLO permits — if the SLO is 99.9%, the budget is 0.1% of time or requests.

## Details
- Budget = 100% - SLO; consumption is measured by SLO burn over a rolling window.
- Policy: when the budget is exhausted, launches stop and reliability work takes priority.
- Budgets turn reliability arguments into numbers both product and engineering can see.
- Open question: how budgets should treat long-tailed, rare incidents.

## Related
- [[wiki/devops-infra/site-reliability-engineering|Site Reliability Engineering]] — the practice error budgets belong to
- [[wiki/devops-infra/golden-signals|Golden Signals]] — the metrics budgets are built on
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]] — budget burn drives meaningful alerts
- [[wiki/cloud-infra/demand-forecasting|Demand Forecasting]] — demand surprises spend budgets
