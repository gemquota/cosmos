---
type: "concept"
title: "Error Budgets"
description: "The allowed failure allowance derived from SLOs that governs release velocity and reliability work"
tags: ["error-budgets", "slo", "sre", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Error Budgets

## Summary
An error budget is the failure allowance an SLO permits: if the SLO is 99.9%, the budget is 0.1% of time or requests. It turns reliability from an abstract promise into a measurable, spendable resource that product and engineering share — when the budget is exhausted, releases stop and reliability work takes priority.

## Details
- Mechanics: budget equals 100% minus the SLO; consumption is measured as SLO burn over a rolling window — burn rate (how fast the budget is consumed) drives both alerting and release gating; multi-window burn-rate alerts catch fast, sharp SLO violations and slow, chronic ones with separate thresholds.
- Concrete example: a 99.9% availability SLO over 30 days permits about 43 minutes of downtime; an incident consuming 20 minutes leaves 23; if burn exceeds the budget, an automated gate blocks deploys until the budget resets or a review approves a spend.
- Failure modes: budgets that are never enforced — the SLO exists but deploys continue, making the budget decorative; alerting that only fires on budget exhaustion, catching problems too late (use burn-rate alerts); long-tailed rare incidents that exhaust a month's budget in minutes — the budget does not distinguish severity, so pair it with incident review and budget exemptions; teams gaming the SLO by adjusting targets after failures.
- Tradeoffs: budgets give a shared, numeric basis for "can we ship?" decisions, aligning product and engineering, but they are a blunt instrument — one bad incident can freeze releases for weeks, so combine the hard gate with a human escalation path; the alternative, subjective reliability judgment, causes friction and fights.
- Operational notes: track budget burn in dashboards, alert on burn rate rather than budget exhaustion, and review budget spend after every incident.
- RSIS3 relevance: RSIS3's own loops have reliability targets — an error budget for pulse collection or dashboard generation tells the meta-loops when to stop shipping new behavior and fix the pipeline instead.

## Related
- [[wiki/devops-infra/site-reliability-engineering|Site Reliability Engineering]] — the practice error budgets belong to
- [[wiki/devops-infra/golden-signals|Golden Signals]] — the metrics budgets are built on
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]] — budget burn drives meaningful alerts
- [[wiki/cloud-infra/demand-forecasting|Demand Forecasting]] — demand surprises spend budgets
