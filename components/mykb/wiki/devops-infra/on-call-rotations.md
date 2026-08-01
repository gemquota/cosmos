---
type: "concept"
title: "On-Call Rotations"
description: "Scheduling engineers to carry the pager with handoff, coverage, and fatigue management"
tags: ["oncall", "rotations", "sre", "incidents"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# On-Call Rotations

## Summary
On-call rotations distribute pager duty across a team with defined shifts, handoffs, and escalation. Good rotations protect sleep and attention so responses stay sharp.

## Details
- Rotations need handoff records: what changed, what is pending, what to watch.
- Secondary tiers (service owners, management) handle escalations.
- Track load: too many pages mean alerting or systems need fixing, not more on-call stamina.
- Open question: how small teams sustain on-call without burning out.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — the work responders handle
- [[wiki/devops-infra/severity-levels|Severity Levels]] — what triggers a page
- [[wiki/devops-infra/escalation-policies|Escalation Policies]] — the ladder above first responder
- [[wiki/devops-infra/runbooks|Runbooks]] — the procedures responders follow
