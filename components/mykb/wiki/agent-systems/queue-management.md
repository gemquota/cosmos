---
type: "concept"
title: "Queue Management"
description: "The discipline of keeping work queues bounded and moving"
tags: ["queues", "management", "process", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Queue Management

## Summary
Queue management would keep the wiki's work queues bounded and moving: items have owners, states, and aging that forces review.

## Details
- An unbounded queue is a warehouse of goodwill — items enter, never leave, and the queue becomes a graveyard.
- The discipline includes admission control (don't add items that will never be done), aging (flag old items), and throughput review (are items being completed?).
- Admission control is the first discipline: don't add items that will never be done, and require each new item to have an owner and a definition of done before it enters the queue.
- Aging forces review: items that sit past their review age are either reprioritized, re-scoped, or closed, so the queue cannot silently become a graveyard.
- Throughput review measures completion, not just input: if items enter faster than they leave, the queue is a backlog in disguise, and the fix is either fewer entries or more capacity.
- WIP limits make the queue visible: bounding how many items are in progress at once exposes the bottleneck and keeps the queue moving rather than full.
- Owners are the accountability unit: every queue item names the party responsible for advancing it, so a stalled item has a person to nudge rather than a silent wait.
- Aging thresholds should be tuned per queue type: fast-moving review queues age in days, long-running projects age in weeks, and the thresholds themselves are reviewed periodically.
- A queue that is always empty is also a signal: it may mean healthy throughput, or it may mean nobody is entering the work at all.
- Queue sizes are measured per queue, not in aggregate, so a hidden pileup in one workflow cannot hide behind healthy totals.
- For mykb, queue management sits under the review queues and approval workflows, and its health would be dashboard-visible.

## Related
- [[wiki/agent-systems/review-queues-wiki|Review Queues]]
- [[wiki/agent-systems/triage-workflow|Triage Workflow]]
- [[wiki/concepts/priority-labels|Priority Labels]]
- [[wiki/agent-systems/approval-workflows-wiki|Approval Workflows]]
- [[wiki/concepts/task-lists-wiki|Task Lists]]
