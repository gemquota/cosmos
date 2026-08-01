---
type: "concept"
title: "Incident Response"
description: "The process for detecting, declaring, mitigating, and learning from production incidents"
tags: ["incident-response", "oncall", "sre", "reliability", "postmortem"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://response.pagerduty.com/"]
---

# Incident Response

## Summary
Incident response is the practiced process for handling production failures: detect, declare, respond, mitigate, resolve, and learn. Clear roles, severity levels, and escalation paths keep people focused on restoring service instead of improvising under pressure. The goal is fast mitigation first and disciplined learning afterward.

## Details
- Phases: detection (alert or user report) → declaration (a formal incident with severity) → response (roles assigned) → mitigation (restore service, not root cause) → resolution → follow-up (postmortem, action items).
- Roles: an incident commander coordinates; a communications lead handles status updates; operators execute mitigation; everyone else is explicitly told to stand down.
- Mitigation first: restore service with the fastest safe action — rollback, failover, feature flag — and investigate root cause only after users are served again.
- Severity levels (SEV-1..SEV-5) set response urgency, escalation paths, and who must be involved; see the severity-levels stub for the taxonomy.
- Communication discipline: a status page or incident channel replaces hallway rumors; external updates follow templates.
- Learning: every significant incident produces a blameless postmortem with root-cause analysis and action items, so the same incident does not recur.
- Relevance to mykb: RSIS3 treats the wiki and agent services as production; a written incident-response procedure makes outages calm and repeatable.

## Related
- [[wiki/devops-infra/severity-levels|Severity Levels]] — urgency taxonomy for declarations
- [[wiki/devops-infra/escalation-policies|Escalation Policies]] — who gets paged and when
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — staffing the response
- [[wiki/devops-infra/postmortem-culture|Postmortem Culture]] — learning loop after resolution
- [[wiki/devops-infra/observability|Observability]] — detection feeds the process
- [[wiki/api-protocols/webhooks|Webhooks]] — automating incident notifications
