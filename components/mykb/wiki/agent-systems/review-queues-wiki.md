---
type: "concept"
title: "Review Queues"
description: "Queues that order articles and tasks for review"
tags: ["queues", "review", "process", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Review Queues

## Summary
Review queues order what gets reviewed next: articles due for freshness review, promotions awaiting approval, proposals awaiting decisions. A queue needs an ordering rule and an exit — items leave when reviewed, not when forgotten — otherwise it is just a list of things nobody is doing.

## Details
- **Ordering rules** — queues are ordered by due date, priority, or risk; the rule should match the cost of delay, so high-risk or high-visibility items do not sit behind trivia.
- **The exit condition** — every item must have a review action that removes it: approve, reject, revise, or archive; a queue without exits is a backlog wearing a queue costume.
- **Freshness reviews** — wiki content decays; review queues schedule re-checks so stale claims are caught before they mislead, linking freshness signals to the queue's due dates.
- **Approval handoff** — items that pass review move into approval workflows; the queue feeds the gate and the gate clears the queue.
- **Metrics** — queue health is measured by age of oldest item, throughput (reviews per week), and clearance rate (items leaving per item entering).
- **Failure modes** — review swamps (too many items, too few reviewers), rubber-stamp reviews, and priority inversion where urgent items wait behind routine ones.
- **mykb relevance** — review queues are the operating surface of review sprints and the input side of the approval workflow, so their health is dashboard-visible.

- **Slack and capacity** — review capacity must be budgeted, not assumed: if reviewers are already at capacity, adding items to the queue just moves them to a different waiting list.

- **Visibility** — a public queue is a commitment device: items visible to the community are harder to let rot silently, and clearance metrics give reviewers feedback on whether the queue is actually moving.

## Related
- [[wiki/agent-systems/queue-management|Queue Management]] — the general discipline
- [[wiki/agent-systems/approval-workflows-wiki|Approval Workflows]] — what happens after review
- [[wiki/devops-infra/review-sprints|Review Sprints]] — batch review practice
- [[wiki/agent-systems/triage-workflow|Triage Workflow]] — feeding the queue
- [[wiki/concepts/priority-labels|Priority Labels]] — ordering the queue
