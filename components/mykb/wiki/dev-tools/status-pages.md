---
type: "concept"
title: "Status Pages"
description: "Public or internal pages that report service availability and ongoing incidents"
tags: ["status-page", "communication", "incident-management", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Status Pages

## Summary
Status pages tell users and internal teams whether a service is up, degraded, or down, and what is being done. During incidents they are the canonical communication channel — a trusted status page reduces support load and prevents rumor-driven panic.

## Details
- Mechanism: components mirror real dependencies (database, API, sync pipeline); each component shows current state and incident history; updates are made early and honestly as the incident evolves; the page serves both external users and internal teams; historical uptime data feeds SLO reporting and vendor accountability.
- Concrete example: an outage begins — the status page marks the database component degraded within minutes, with a note and the incident ID; as investigation proceeds, the page updates with the fix and ETA; after resolution it records the duration and postmortem link; automated health checks propose updates that a human confirms.
- Failure modes: status pages that lag reality, destroying trust exactly when needed; updates that are vague (we are investigating with no detail); components that do not mirror dependencies, so a database outage shows as everything down; pages updated by automation that misfires, declaring outages that do not exist; status page itself going down during the incident (host it redundantly).
- Tradeoffs: a status page costs maintenance and discipline but is the cheapest way to manage incident communication; the alternative, ad-hoc updates, fails under load; the mature pattern is component-level honesty, automated health inputs, and human-confirmed updates.
- Operational notes: rehearse status updates in game days, keep components aligned with real dependencies, and archive history for reporting.
- RSIS3 relevance: a wiki status page could show sync health between raw captures and curated articles — the same availability communication for the knowledge pipeline.

- Automate component health feeds, but keep a human-confirmed update step so the page never cries wolf.
## Related
- [[wiki/devops-infra/incident-response|Incident Response]]
- [[wiki/dev-tools/incident-command|Incident Command]]
- [[wiki/dev-tools/sev-levels|Sev Levels]]
- [[wiki/devops-infra/health-endpoint-contracts|Health Endpoint Contracts]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
