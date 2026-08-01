---
type: "concept"
title: "Escalation Policies"
description: "Defined chains of who gets contacted when, until an incident has an owner"
tags: ["escalation", "oncall", "incidents", "policies"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Escalation Policies

## Summary
Escalation policies define the contact ladder: primary on-call first, then backups, then managers or specialists, with timeouts between steps. They guarantee every incident gets a responder.

## Details
- Structure: level 1 primary, level 2 backup, level 3 service owner/specialist, then management.
- Timeouts per step prevent one silent gap from stalling the response.
- Policies are per-service: database incidents escalate differently from UI ones.
- Open question: how escalation and severity should interact in the taxonomy.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — the process escalation feeds
- [[wiki/devops-infra/severity-levels|Severity Levels]] — urgency drives the ladder
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — staffing each rung
- [[wiki/devops-infra/runbooks|Runbooks]] — documentation for each responder
