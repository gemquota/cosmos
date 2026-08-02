---
type: "concept"
title: "Alerting Rules"
description: "Conditions that turn metric thresholds into pages, tickets, or chat messages"
tags: ["alerting", "monitoring", "on-call", "rules"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Alerting Rules

## Summary
Alerting rules define when monitoring signals demand attention: PromQL expressions, thresholds, and evaluation windows. Well-designed rules page humans only for problems that need a human.

## Details
- Alert on symptoms users feel (errors, latency) rather than internal causes; let dashboards show the why.
- Use burn-rate and error-budget rules so alerts fire on SLO risk, not momentary blips.
- Every alert needs a runbook, an owner, and a test that the firing condition actually detects the failure.
- RSIS3 relevance: alert rules around knowledge freshness could page when the wiki drifts stale.

## Related
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/dev-tools/burn-rate-alerts|Burn Rate Alerts]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
