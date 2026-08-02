---
type: "concept"
title: "Incident Response"
description: "Detecting, containing, and resolving production incidents"
tags: ["incident", "response", "on-call", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://sre.google/sre-book/managing-incidents/",
  "https://response.pagerduty.com/",
]
---

# Incident Response

## Summary
Incident response is the structured process for detecting, declaring, and resolving production incidents. Clear roles, communication channels, and severity tiers reduce time-to-recovery and chaos. Post-incident learning closes the loop and improves the next response.

## Details
- Detection comes from alerting and monitoring; good alert hygiene prevents alert fatigue.
- The SRE book describes roles: incident commander, operations lead, and communications lead.
- Severity levels (SEV1-SEV3) determine escalation and response speed.
- The PagerDuty response guide covers practical incident lifecycle practices.
- Declaring early is encouraged: investigation and mitigation can proceed in parallel.
- In mykb, incident response connects to on-call, runbooks, and postmortems.
- A shared incident channel and timeline capture decisions for the later postmortem.
- Status pages keep users informed while responders focus on mitigation.
- Severity definitions with clear examples help teams classify incidents consistently.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/incident-response|Incident Response]]
- [[wiki/devops-infra/acid|ACID]]
