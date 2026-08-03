---
type: "concept"
title: "Game Days & Failure Drills"
description: "Deliberate failure exercises that test runbooks and muscle memory"
tags: ["game-day", "chaos", "drills", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Game Days & Failure Drills

## Summary
Game days are scheduled, scripted exercises where a team intentionally fails a system and practices the response. They convert untested runbooks and tribal knowledge into rehearsed muscle memory, exposing gaps — missing alerts, broken failover, slow escalation — before a real incident does.

## Details
- Mechanism: choose a hypothesis ("if the primary database dies, failover takes under 15 minutes"), script the scenario, inject the failure (kill the node, block network, revoke credentials), and have the on-call team respond using only their normal tools; a facilitator observes; afterwards, a retrospective records what worked, what broke, and the follow-up actions.
- Concrete example: a quarterly game day rotates scenarios — database failover, DNS outage, certificate expiry, dependency outage; each produces runbook updates and small engineering tasks; a "build the team" variant has a new hire recover a service with only the docs, proving runbook quality.
- Failure modes: rehearsed responses that skip real steps (answering from memory instead of executing); scenarios too gentle to expose anything; blaming culture that makes participants defensive; no follow-through — findings never become tickets and the same gaps recur; running game days only on the happy, well-known path.
- Tradeoffs: game days cost engineering time and carry a small risk of real impact, but they are the cheapest way to buy confidence in incident response; the alternative — learning during real incidents — is expensive and stressful; start small (one service, one scenario) and grow.
- Operational notes: make game days blameless, track findings to completion, rotate scenario ownership, and vary the participants so knowledge is not concentrated.
- Progression: start with read-only failures (dependency timeout, DNS outage) before destructive ones (data loss, region failover), and rehearse both the runbook and the escalation path each time.
- RSIS3 relevance: RSIS3's own reliability loops need the same rehearsal — practice recovering the wiki store or dashboard from a backup before a real loss, and turn findings into loop improvements.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
