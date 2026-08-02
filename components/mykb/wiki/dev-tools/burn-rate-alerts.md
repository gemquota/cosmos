---
type: "concept"
title: "Burn Rate Alerts"
description: "Alerts that fire when an SLO error budget is being consumed faster than planned"
tags: ["alerting", "slo", "error-budgets", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Burn Rate Alerts

## Summary
Burn-rate alerts compare the current error rate against the SLO threshold and alert on consumption speed: a fast burn pages immediately, a slow burn pages when the budget is nearly gone. They convert SLO math into actionable signals.

## Details
- Fast-burn (e.g. 14.4x over a 1-hour window) catches outages quickly; slow-burn (1x over 6-24 hours) catches steady degradation.
- Multi-window rules reduce flapping: require both a short and a long window to breach.
- Distinguish burn of the error budget versus unburned budget remaining — alerts answer 'are we on track?'
- mykb relevance: a knowledge SLO with burn alerts would catch link rot before it compounds.

## Related
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/dev-tools/slo-budgets|SLO Budgets]]
- [[wiki/dev-tools/alerting-rules|Alerting Rules]]
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
