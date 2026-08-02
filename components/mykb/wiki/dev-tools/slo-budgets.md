---
type: "concept"
title: "SLO Budgets"
description: "Allocating a fixed error budget across changes, releases, and experiments"
tags: ["slo", "error-budgets", "reliability", "budgeting"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# SLO Budgets

## Summary
An SLO budget divides the allowed error budget (e.g. 0.1% unavailability per month) among teams and changes. Spending the budget is the signal to slow down releases and invest in reliability.

## Details
- Define the budget at the SLO level (monthly or rolling window) and track consumption continuously.
- Borrow against the future is how incidents feel: a Sev1 can consume weeks of budget at once.
- Budget burn rate decides alerting and release gates — fast burn pages, slow burn adjusts process.
- mykb relevance: treat wiki-link breakage as budget spend on the knowledge SLO.

## Related
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/dev-tools/burn-rate-alerts|Burn Rate Alerts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/dev-tools/alerting-rules|Alerting Rules]]
