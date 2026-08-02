---
type: "concept"
title: "Failover Practice"
description: "Routine discipline for switching from a failed primary to a standby"
tags: ["failover", "high-availability", "recovery", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Failover Practice

## Summary
Failover practice is the drillable routine of moving service to a standby after a primary fails: detect, promote, reroute, verify. Well-practiced failover is fast and calm; unpracticed failover is where outages become disasters.

## Details
- Test failover on a schedule — the standby that has never been promoted is a risk.
- Automate detection and promotion; keep a manual path for emergencies.
- Mind the data-loss window: failover to a lagging replica sacrifices recent writes.
- mykb relevance: the wiki sync node fails over to a standby worker with a rehearsed runbook.

## Related
- [[wiki/devops-infra/database-failover-automation|Database Failover Automation]]
- [[wiki/tooling/failure-drills|Failure Drills]]
- [[wiki/tooling/multi-region|Multi-Region]]
- [[wiki/tooling/active-passive|Active-Passive]]
- [[wiki/tooling/business-continuity|Business Continuity]]
