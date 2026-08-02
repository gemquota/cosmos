---
type: "concept"
title: "SLOs & Error Budgets"
description: "Targets and budgets that govern reliability tradeoffs"
tags: ["slo", "error-budget", "reliability", "targets"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://sre.google/sre-book/service-level-objectives/",
  "https://sre.google/workbook/error-budget-policy/",
]
---

# SLOs & Error Budgets

## Summary
Service level objectives define measurable reliability targets, and error budgets convert them into release and engineering decisions. SLOs align engineering effort with user impact rather than internal component health. They are the core mechanism of SRE practice and the link between reliability and delivery speed.

## Details
- An SLO is a target for a ratio, such as 99.9% of requests under 200ms over 30 days.
- Error budgets measure the allowed failure: 0.1% of the period, spent on experimentation or held in reserve.
- The SRE book's SLO chapter explains objectives, indicators, and targets.
- Burn-rate alerts fire when consumption is too fast, not just when the budget empties.
- SLOs must be defined per user journey, not per internal component.
- In mykb, SLOs connect to error budgets, alerting, and progressive delivery gates.
- SLOs should cover the user journey, and each SLO needs a defined SLI measuring the ratio being promised.
- Multi-window, multi-burn-rate alerts give early warning without alert fatigue.

## Related
- [[wiki/shell-environment/exit-codes-and-error-handling|Exit Codes & Error Handling]]
- [[wiki/devops-infra/pod-disruption-budgets|Pod Disruption Budgets]]
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/infrastructure/pipeline-sla-and-latency-budgets|Pipeline Sla And Latency Budgets]]
