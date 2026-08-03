---
type: "concept"
title: "Incident Command"
description: "Roles and coordination structures for managing a live incident response"
tags: ["incident-management", "on-call", "roles", "coordination"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Incident Command

## Summary
Incident command assigns explicit roles — incident commander, scribe, subject-matter experts — so a crisis has a single decision-maker and a clear record. Borrowed from emergency response, it keeps teams coordinated under pressure by separating decision-making from investigation.

## Details
- Mechanism: the incident commander owns decisions, prioritization, and communication — they do not debug; SMEs investigate and report findings; the scribe keeps a live timeline of actions, hypotheses, and evidence; handoffs are explicit when shifts change; the commander declares the incident, sets severity, and closes it with a summary.
- Concrete example: a production outage is declared in the status channel; the commander triages — who is investigating, what is the workaround, when to escalate; the scribe logs every action and metric; the postmortem is written from the scribe's timeline plus the commander's decision log.
- Failure modes: the commander debugging instead of coordinating, so no one owns decisions; multiple people acting without direction, duplicating effort and contradicting each other; no scribe, so the postmortem has no record; incidents declared too late because teams hesitate; roles that do not fit the incident size — a two-person incident does not need a full command structure.
- Tradeoffs: command structure adds coordination overhead but reduces chaos exactly when chaos is expensive; the alternative, informal collaboration, works for small incidents and fails at scale; the mature pattern is role awareness for everyone on call, with a light structure that scales up as severity rises.
- Operational notes: practice the structure in game days, keep a declared-incident checklist, and review role effectiveness in postmortems.
- RSIS3 relevance: agent incidents benefit from the same structure — a coordinator, a recorder, and clear handoffs — so a failing loop run is coordinated, not improvised.

## Practice
- Keep the structure proportional: a two-person incident needs a commander and a note-taker, not a full staff.
## Related
- [[wiki/devops-infra/incident-response|Incident Response]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
- [[wiki/communities/blameless-postmortems|Blameless Postmortems]]
- [[wiki/dev-tools/sev-levels|Sev Levels]]
