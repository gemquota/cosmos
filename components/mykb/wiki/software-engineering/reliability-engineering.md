---
type: "concept"
title: "Reliability Engineering"
description: "The discipline of keeping systems available through SLOs, budgets, and practice"
tags: ["reliability", "sre", "slo", "availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://sre.google/sre-book/table-of-contents/", "https://en.wikipedia.org/wiki/Site_reliability_engineering"]
---

# Reliability Engineering

## Summary
Reliability engineering applies engineering rigor to availability: define what reliability means (SLOs), measure it, budget error, and invest where the budget says to. It is the SRE discipline — treating operations as a software problem.

## Details
- SLOs define measurable reliability targets; error budgets convert them into a release throttle.
- Reliability is a tradeoff: 99.99% costs real money, so SLOs are negotiated with product, not maxed out.
- Toil reduction (automating repetitive ops) frees capacity for reliability engineering itself.
- Practice matters: game days, failure drills, and chaos experiments validate the mechanisms on schedule.
- Monitoring exists to serve SLOs: alert on error budget burn, not on every twitch.
- For the mykb bundle, reliability engineering sets a knowledge availability SLO: articles readable, links valid, sync within budget.

Worked example — the wiki SLO is 99.9% link validity per month. A bad migration burns 5% of the budget in a day; the burn alert pauses releases until the budget recovers, funding the link-verification fix.

## Related
- [[wiki/software-engineering/observability-practice|Observability Practice]]
- [[wiki/dev-tools/slo-budgets|SLO Budgets]]
- [[wiki/dev-tools/burn-rate-alerts|Burn Rate Alerts]]
- [[wiki/communities/incident-management|Incident Management]]
- [[wiki/tooling/chaos-experiments|Chaos Experiments]]
- [[wiki/dev-tools/four-golden-signals|Four Golden Signals]]
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
