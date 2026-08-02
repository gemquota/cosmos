---
type: "concept"
title: "Postmortems & Blameless Culture"
description: "Learning from failures without blame"
tags: ["postmortem", "blameless", "learning", "culture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://sre.google/sre-book/postmortem-culture/",
  "https://sre.google/workbook/postmortem-culture/",
]
---

# Postmortems & Blameless Culture

## Summary
Postmortems analyze incidents to find systemic causes and actions, in a blame-free culture that treats failures as learning opportunities. The goal is preventing recurrence, not assigning fault. They close the incident response loop and feed the reliability backlog.

## Details
- A postmortem documents timeline, impact, root cause, and action items with owners.
- The SRE book's postmortem chapter describes the culture and mechanics.
- Blameless review separates human error from process and system weaknesses.
- Action items must be tracked to completion or the exercise is theater.
- Smaller incidents deserve lightweight postmortems to keep the habit alive.
- In mykb, postmortems connect to incident response, game days, and SRE culture.
- Good postmortems include evidence, not memory: timelines drawn from logs and metrics.
- Reviewing postmortems regularly turns individual learnings into team-wide improvements.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/acid|ACID]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
