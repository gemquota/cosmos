---
type: "concept"
title: "Review Queues"
description: "Queues that order articles and tasks for review"
tags: ["queues", "review", "process", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Review Queues

## Summary
Review queues order what gets reviewed next — articles due for freshness review, promotions awaiting approval, proposals awaiting decisions.

## Details
- A queue needs an ordering rule (by due date, by priority, by risk) or it is just a list.
- Queues also need an exit: items leave when reviewed, not when forgotten.
- For mykb, review queues are the operating surface of review-sprints and feed the approval workflow.

## Related
- [[wiki/agent-systems/queue-management|Queue Management]]
- [[wiki/agent-systems/review-queues-wiki|Review Queues]]
- [[wiki/agent-systems/approval-workflows-wiki|Approval Workflows]]
- [[wiki/devops-infra/review-sprints|Review Sprints]]
- [[wiki/agent-systems/triage-workflow|Triage Workflow]]
- [[wiki/concepts/priority-labels|Priority Labels]]
