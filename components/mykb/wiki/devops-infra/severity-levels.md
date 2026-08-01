---
type: "concept"
title: "Severity Levels"
description: "Classifying incidents by impact and urgency so responses match reality"
tags: ["severity", "incidents", "classification", "sre"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Severity Levels

## Summary
Severity levels (SEV-1 through SEV-4/5) classify incidents by user impact and urgency, driving who gets paged and how fast. A shared taxonomy prevents both over-reaction and under-reaction.

## Details
- SEV-1: total outage or data loss, immediate response; SEV-2: significant degradation; lower levels for contained issues.
- Severity can change during an incident — reclassify as impact becomes clear.
- Levels map to escalation paths, communication needs, and postmortem requirements.
- Open question: how severity taxonomy should differ across small and large organizations.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — severity drives the response
- [[wiki/devops-infra/escalation-policies|Escalation Policies]] — severity triggers escalations
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — who responds at each level
- [[wiki/devops-infra/postmortem-culture|Postmortem Culture]] — which incidents get reviews
