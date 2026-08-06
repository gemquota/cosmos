---
type: "concept"
title: "Triage Workflow"
description: "The process of routing incoming issues to the right owner and priority"
tags: ["triage", "workflow", "process", "queue"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Triage Workflow

## Summary
Triage is the intake process that turns raw incoming items — requests, flags, reports — into routed, prioritized, tracked work. Every item passes through a small decision tree: is it valid, is it already covered, who owns it, how urgent is it. Triage is where a healthy pipeline is made or broken.

## Details
- **The decision tree** — each incoming item is checked for validity (is this real work?), duplication (is it already covered?), ownership (who advances it?), and urgency (when must it move?).
- **Speed matters** — triage must be fast enough that intake is not the bottleneck; items that stall in the intake state are failures of the workflow, not of the item.
- **Timebox and escalation** — every item gets a timebox for the triage decision and an escalation path if nobody can decide; without these, triage becomes a second backlog.
- **Routers and priority** — triage assigns the item to a workflow (task list, review queue, approval flow) and a priority label, so downstream queues can order themselves.
- **Relationship to requests pages** — requests pages are the intake form; triage is the processing of that form; task lists are the tracked output.
- **Failure modes** — triage without ownership produces orphan items; triage without exits produces a queue that grows forever; triage by the wrong people routes work to the wrong place.
- **mykb relevance** — triage is the front door of the wiki's review queues, connecting requests pages to task lists and keeping the curation pipeline moving.

- **Metrics** — triage health is measured by time-to-routing, share of items that stall in intake, and misrouting rate; these numbers expose whether the front door is working before the backlogs form.

## Related
- [[wiki/agent-systems/queue-management|Queue Management]] — the discipline triage feeds
- [[wiki/concepts/triage-labels|Triage Labels]] — the intake vocabulary
- [[wiki/concepts/priority-labels|Priority Labels]] — ordering after triage
- [[wiki/agent-systems/requests-pages|Requests Pages]] — the intake surface
- [[wiki/agent-systems/noticeboards|Noticeboards]] — where items surface
- [[wiki/agent-systems/review-queues-wiki|Review Queues]] — where routed items wait
