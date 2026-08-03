---
type: "concept"
title: "Severity Levels"
description: "Classifying incidents by impact and urgency so responses match reality"
tags: ["severity", "incidents", "classification", "sre"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Severity Levels

## Summary
Severity levels (SEV-1 through SEV-4/5) classify incidents by user impact and urgency, driving who gets paged and how fast. A shared taxonomy prevents both over-reaction and under-reaction — SEV-1 mobilizes the whole team, while a contained issue gets a tracked ticket, not a 3am page.

## Details
- Taxonomy: SEV-1 is a total outage, data loss, or security breach requiring immediate, full response; SEV-2 is significant degradation of a core feature; SEV-3 is a contained issue with workarounds; SEV-4/5 are minor or pre-production issues handled in normal flow. The boundaries should be written down with examples so classification is not a judgment call under stress.
- Mechanism: the severity maps to a response matrix — who is notified (on-call only, whole team, management), how fast (minutes, hours, next business day), which communication channels, and what follow-up is required (postmortem for SEV-1/2, ticket for lower levels).
- Severity can change during an incident: a SEV-3 that grows to affect all users is reclassified to SEV-1, which changes the response; reclassification should be explicit and logged.
- Failure modes: severity inflation — everything becomes SEV-1, so pages lose meaning and responders tune out; severity deflation — a real outage labeled SEV-3, delaying response; taxonomy that does not match organizational size (a two-person team paging like an enterprise); classification done by the person who caused the incident, skewing the label.
- Tradeoffs: a formal taxonomy costs process overhead but ensures proportional response; the alternative, ad-hoc judgment, works until stress — then everyone improvises differently; the maturity path is a small, example-anchored taxonomy, tuned over time from real incidents.
- Operational notes: review classification accuracy in postmortems, keep the taxonomy documented and visible, and train on-call responders on it.
- RSIS3 relevance: cosmos's own incidents (dashboard down, wiki store unreachable) deserve severity labels so RSIS3's loops know which failures demand immediate intervention versus normal handling.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — severity drives the response
- [[wiki/devops-infra/escalation-policies|Escalation Policies]] — severity triggers escalations
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — who responds at each level
- [[wiki/devops-infra/postmortem-culture|Postmortem Culture]] — which incidents get reviews
