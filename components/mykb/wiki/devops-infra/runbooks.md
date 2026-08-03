---
type: "concept"
title: "Runbooks"
description: "Written procedures for handling alerts and incidents so anyone on call can act correctly"
tags: ["runbooks", "oncall", "documentation", "incidents"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Runbooks

## Summary
Runbooks are the step-by-step procedures for responding to known alerts and incidents: what the alarm means, what to check, what to do. They compress hard-won operational knowledge into actionable scripts that anyone on call can follow — including someone seeing the system for the first time at 3am.

## Details
- Mechanics: each alert points to a runbook; each runbook names symptoms, the checks to run, the commands with expected outputs, the fix, and the escalation path; runbooks live in the repo, versioned and reviewed like code.
- Concrete example: an alert fires for database connection exhaustion; the runbook says check `pg_stat_activity` for idle-in-transaction sessions, look for a specific query pattern, kill the offending sessions, and if the problem persists, page the database owner; the expected outputs are shown so the responder can tell success from failure.
- Failure modes: runbooks that rot — systems change and the commands stop working, so responders improvise; runbooks that are too vague (check the database) or too long to read under pressure; steps that assume context the responder lacks (a VPN, a bastion, a known directory); runbooks that are never tested, so the first real execution is the test; alerts that do not link to any runbook.
- Tradeoffs: runbooks are cheap insurance against tribal-knowledge failure, but they require maintenance — review them after incidents and when systems change; the alternative, no documentation, fails exactly when it matters most; the discipline is to write for the worst-case reader and validate in game days.
- Operational notes: keep runbooks with the code they describe, link them from alerts and dashboards, and treat runbook updates as part of incident follow-up.
- RSIS3 relevance: the wiki daemon, dashboard, and backup restore should each have a runbook in the repo — RSIS3's recovery loop then has an executable, tested procedure instead of a memory.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — runbooks support the response
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — who reads the runbooks
- [[wiki/devops-infra/escalation-policies|Escalation Policies]] — when runbooks fail
- [[wiki/devops-infra/observability|Observability]] — dashboards runbooks reference
