---
type: "concept"
title: "On-Call Practices"
description: "Rotations, escalation, and sustainable paging"
tags: ["on-call", "paging", "rotation", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://sre.google/sre-book/being-on-call/",
  "https://sre.google/workbook/",
]
---

# On-Call Practices

## Summary
On-call practices cover rotations, escalation, and the sustainable operation of paging engineers. Good on-call design protects both users and the engineers who respond. It is the human half of incident response and a defining practice of SRE teams.

## Details
- Rotations distribute paging load fairly across qualified engineers, with clear handoff procedures.
- The SRE book's on-call chapter details the responsibilities of on-call engineers.
- Escalation policies route alerts from primary to secondary to management by severity.
- Documented runbooks reduce the cognitive load of night-time incidents.
- Operational load must be measured and tuned: too many pages burns out teams.
- In mykb, on-call connects to incident response, runbooks, and SLOs.
- Follow-the-sun or timezone-based rotations reduce the burden of overnight pages.
- Handoff notes capture the state of open incidents for the next responder.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/cloud-infra/security-group-best-practices|Security Group Best Practices]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/cloud-infra/finops-practices|FinOps Practices]]
- [[wiki/devops-infra/changelog-practices|Changelog Practices]]
