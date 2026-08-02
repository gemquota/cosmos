---
type: "concept"
title: "Blameless Postmortems"
description: "Incident reviews that fix systems, not people"
tags: ["postmortem", "blameless", "incidents", "learning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://sre.google/sre-book/postmortem-culture/", "https://en.wikipedia.org/wiki/Postmortem_documentation"]
---

# Blameless Postmortems

## Summary
A blameless postmortem analyzes an incident without assigning blame: the question is what the system and process allowed, not who made an error. Google's SRE culture made it standard practice, and it is the single highest-leverage incident ritual.

## Details
- Write a timeline of facts, root causes (often multiple contributing), and action items with owners.
- Blame culture suppresses information; blameless culture gets the full story so the fix can target the real gap.
- Action items must be specific and owned: 'add tests' is a wish; 'add a test for the empty-queue path by Friday' is an action.
- Follow up on action items — a postmortem without follow-through teaches that incidents do not matter.
- Include what went well, not just what failed; recognize good mitigation under pressure.
- For the mykb bundle, postmortems cover curation failures: broken links, lost captures, and sync bugs.

Worked example — a botched migration deleted links; the postmortem found the rollback path was untested. The action: a restore drill and a migration checklist. No one was blamed; the runbook changed.

## Related
- [[wiki/communities/incident-management|Incident Management]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/tooling/restore-drills|Restore Drills]]
- [[wiki/tooling/failure-drills|Failure Drills]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/runbook-automation|Runbook Automation]]
- [[wiki/tooling/game-days|Game Days]]
- [[wiki/devops-infra/incident-response|Incident Response]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
