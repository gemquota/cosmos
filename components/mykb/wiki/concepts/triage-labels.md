---
type: "concept"
title: "Triage Labels"
description: "Labels that record an item's triage state"
tags: ["triage", "labels", "process", "metadata"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Triage Labels

## Summary
Triage labels record where an item is in the intake workflow: new, triaged, in-queue, assigned, blocked, resolved.

## Details
- Labels make the queue machine-readable — dashboards can show exactly where work is stuck.
- Label values must be a closed set defined by the workflow; invented labels fragment the queue.
- For mykb, triage labels are the state machine of the review queue and pair with priority, severity, impact, and effort labels.

## Related
- [[wiki/agent-systems/triage-workflow|Triage Workflow]]
- [[wiki/concepts/priority-labels|Priority Labels]]
- [[wiki/concepts/triage-labels|Triage Labels]]
- [[wiki/agent-systems/queue-management|Queue Management]]
- [[wiki/agent-systems/review-queues-wiki|Review Queues]]
- [[wiki/concepts/severity-labels|Severity Labels]]
