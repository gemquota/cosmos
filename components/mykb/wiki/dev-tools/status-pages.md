---
type: "concept"
title: "Status Pages"
description: "Public or internal pages that report service availability and ongoing incidents"
tags: ["status-page", "communication", "incident-management", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Status Pages

## Summary
Status pages tell users and internal teams whether a service is up, degraded, or down, and what is being done. During incidents they are the canonical communication channel that reduces support load.

## Details
- Update them early and honestly: a status page is only trusted if it reflects reality quickly.
- Components should mirror real dependencies so a database outage shows as the database, not as everything.
- Historical uptime data from status pages feeds SLO reporting and vendor accountability.
- mykb relevance: a wiki status page could show sync health between raw captures and curated articles.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]]
- [[wiki/dev-tools/incident-command|Incident Command]]
- [[wiki/dev-tools/sev-levels|Sev Levels]]
- [[wiki/devops-infra/health-endpoint-contracts|Health Endpoint Contracts]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
