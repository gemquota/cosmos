---
type: "concept"
title: "SLO Budgets"
description: "Allocating a fixed error budget across changes, releases, and experiments"
tags: ["slo", "error-budgets", "reliability", "budgeting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SLO Budgets

## Summary
An SLO budget divides the allowed error budget (for example 0.1% unavailability per month) among teams and changes. Spending the budget is the signal to slow down releases and invest in reliability — the budget makes the tradeoff between velocity and risk explicit and numeric.

## Details
- Mechanism: define the budget at the SLO level over a rolling window; track consumption continuously from error and latency data; burn rate (how fast the budget is consumed) drives alerting and release gates — fast burn pages, slow burn adjusts process; budget consumption is reviewed in retrospectives and compared to the change that caused it.
- Concrete example: a 99.9% SLO allows 43 minutes of downtime monthly; a Sev1 consuming 30 minutes leaves 13 and triggers a release freeze until the window rolls; a deployment that causes a burn spike is correlated with the change; each team sees its share of the budget and its burn.
- Failure modes: budgets defined but never enforced, becoming decoration; a single incident consuming weeks of budget at once, making the budget feel arbitrary; burn measured on the wrong metric or window; teams gaming the budget by adjusting SLOs after incidents; budgets treated punitively, hiding honest burn.
- Tradeoffs: budgeting makes reliability a shared, numeric resource — the alternative, subjective judgment, causes friction and fights; the tradeoff is the process overhead of tracking and enforcing; the mature pattern is a rolling window, burn-based alerts, and a release gate that human escalation can override.
- Operational notes: track burn in dashboards, review budget spend after incidents, and tie release gates to remaining budget.
- RSIS3 relevance: treat wiki-link breakage as budget spend on the knowledge SLO — the same numeric discipline for the wiki's reliability.

- Align the budget window with the business calendar so monthly reviews and monthly budgets tell the same story.
## Related
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/dev-tools/burn-rate-alerts|Burn Rate Alerts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/dev-tools/alerting-rules|Alerting Rules]]
