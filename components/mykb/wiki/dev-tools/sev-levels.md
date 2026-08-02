---
type: "concept"
title: "Sev Levels"
description: "Standard severity classifications that set expectations for incident response speed"
tags: ["incident-management", "severity", "on-call", "classification"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sev Levels

## Summary
Sev levels (Sev1 through Sev4) classify incidents by impact so responders know how fast to act and who to wake. A shared definition prevents arguments about whether something is an emergency.

## Details
- Define levels by user impact and blast radius: Sev1 is total or customer-facing outage, Sev4 is cosmetic or internal.
- Each level has response-time SLAs, required participants, and escalation paths.
- Review classifications after the fact — misclassification trains people to ignore the levels.
- mykb relevance: wiki-link breakage across many pages is a Sev2-style knowledge outage.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]]
- [[wiki/dev-tools/incident-command|Incident Command]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
- [[wiki/dev-tools/status-pages|Status Pages]]
- [[wiki/communities/incident-management|Incident Management]]
