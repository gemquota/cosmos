---
type: "concept"
title: "Runbooks"
description: "Written procedures for handling alerts and incidents so anyone on call can act correctly"
tags: ["runbooks", "oncall", "documentation", "incidents"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Runbooks

## Summary
Runbooks are the step-by-step procedures for responding to known alerts and incidents: what the alarm means, what to check, what to do. They compress hard-won operational knowledge into actionable scripts.

## Details
- Each alert should point to a runbook; each runbook names symptoms, checks, and fixes.
- Write for a tired on-call engineer at 3am: explicit commands and expected outputs.
- Runbooks rot — review them after incidents and when systems change.
- Open question: how to keep runbooks and code in the same review loop.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — runbooks support the response
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — who reads the runbooks
- [[wiki/devops-infra/escalation-policies|Escalation Policies]] — when runbooks fail
- [[wiki/devops-infra/observability|Observability]] — dashboards runbooks reference
