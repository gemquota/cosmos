---
type: "concept"
title: "Burn Rate Alerts"
description: "Alerts that fire when an SLO error budget is being consumed faster than planned"
tags: ["alerting", "slo", "error-budgets", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Burn Rate Alerts

## Summary
Burn-rate alerts compare the current error rate against the SLO threshold and alert on consumption speed: a fast burn pages immediately, a slow burn pages when the budget is nearly gone. They convert SLO math into actionable signals, answering are we on track to exhaust the error budget.

## Details
- Mechanism: burn rate = actual error rate / SLO error rate; a rate of 1x consumes the budget in the full window, 14.4x in about 1/14.4 of it; alert rules pair a short window (1h) with a high multiplier (fast-burn, pages immediately) and a long window (6-24h) with a low multiplier (slow-burn, catches steady degradation before the budget dies).
- Concrete example: a 99.9% SLO with a 14.4x/1h rule fires when the error rate is about 14.4% for 5 minutes; the 1x/24h rule fires when errors have run at the SLO threshold all day; multi-window rules require both windows to breach, reducing flapping from short spikes.
- Failure modes: flapping from single-window rules on bursty traffic; thresholds that ignore the error budget remaining, alerting when the budget is already spent; paging on fast-burn for services where the budget is large enough to absorb the spike; alert rules that are not tested, firing only during real incidents; burn defined on the wrong metric (availability versus latency).
- Tradeoffs: burn-rate alerts give early, budget-accurate signals versus threshold alerts that page on any blip; the tradeoff is tuning complexity — windows, multipliers, and severity levels need design per SLO; the payoff is that the alert means the same thing as the budget, so noise and missed incidents both drop.
- Operational notes: start from the Google SRE workbook multipliers, tune on real incident data, and test rules in drills.
- RSIS3 relevance: a knowledge SLO with burn alerts would catch link rot before it compounds — the same budget math applied to the wiki's health.

## Related
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/dev-tools/slo-budgets|SLO Budgets]]
- [[wiki/dev-tools/alerting-rules|Alerting Rules]]
- [[wiki/devops-infra/golden-signals|Golden Signals]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
