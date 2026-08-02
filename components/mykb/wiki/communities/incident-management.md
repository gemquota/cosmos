---
type: "concept"
title: "Incident Management"
description: "The process of detecting, responding to, and resolving live incidents"
tags: ["incident-management", "on-call", "response", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Incident_management", "https://sre.google/sre-book/table-of-contents/"]
---

# Incident Management

## Summary
Incident management is the structured process for handling live failures: detect, declare, respond with clear roles, mitigate, and learn. Its goal is to restore service fast while preserving evidence and calm — and to convert every incident into improvements.

## Details
- The incident lifecycle: detection, declaration, response coordination, mitigation, resolution, and postmortem.
- Clear roles (incident commander, scribe, SMEs) prevent the chaos of everyone debugging at once.
- Declaring early is a feature: a false alarm costs less than an undeclared outage.
- Mitigation before root cause: restore service first, investigate later — the postmortem is where root cause lives.
- Severity levels standardize response speed and escalation paths.
- Metrics that matter: time to detect, time to mitigate, and change failure rate.
- For the mykb bundle, an incident is a corrupted index or a sync outage; the response follows the same discipline at smaller scale.

Worked example — the wiki sync stalls; monitoring pages on-call. The commander declares a Sev2, the scribe logs that sync lag is rising, and a mitigation replays the queue. A postmortem finds the broker config, and a runbook update prevents recurrence.

## Related
- [[wiki/communities/blameless-postmortems|Blameless Postmortems]]
- [[wiki/dev-tools/incident-command|Incident Command]]
- [[wiki/dev-tools/sev-levels|Sev Levels]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/on-call-practices|On-Call Practices]]
- [[wiki/dev-tools/runbook-automation|Runbook Automation]]
- [[wiki/dev-tools/status-pages|Status Pages]]
- [[wiki/devops-infra/incident-response|Incident Response]]
