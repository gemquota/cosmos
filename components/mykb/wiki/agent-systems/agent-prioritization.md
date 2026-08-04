---
type: "concept"
title: "Agent Prioritization"
description: "Ranking tasks or requests so agents work on the highest-value work first"
tags: ["prioritization", "agents", "scheduling", "priority"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Prioritization

## Summary
Agent prioritization ranks tasks or requests so that agents work on the highest-value work first. It matters because agent capacity is a scarce, costly resource, and doing low-value tasks while high-value ones wait is pure waste. Priorities make the trade-off explicit and auditable. Priorities should be reviewed regularly because the value of work changes over time.

## Details
- **Definition** — prioritization is the policy that assigns an order to pending work based on urgency, value, dependencies, and deadlines.
- **Dimensions** — good priority functions combine business value, time sensitivity, effort, and blocking relationships rather than a single number.
- **Mechanisms** — priorities are applied in queues and schedulers as weighted ordering, deadline scheduling, or hierarchical policies.
- **Preemption** — high-priority work may preempt running low-priority work, but preemption must be bounded to avoid thrashing.
- **Auditability** — priority decisions should be logged with their rationale so a skipped task can be explained after the fact.
- **Worked example** — an incident response agent system routes a production outage ahead of a routine report generation, then resumes the report when capacity frees up.
- **Failure modes** — mislabeled priorities cause starvation, priority inflation makes everything urgent, and dependency blindness schedules blockers too late.
- **Integration** — prioritization interacts with budget-and-quota-control and load-shedding to decide both what runs and what is dropped.
- **Practical relevance** — prioritization is the difference between a busy agent system and a productive one; it applies at every layer from queues to models.
- **Policy review** — priority rules need periodic review to stay aligned with current business goals.
- **Starvation guard** — aging mechanisms raise the priority of waiting tasks so low-priority work eventually completes.
- **Worked example** — a batch of low-priority reports gets an aging boost after waiting a day, preventing indefinite postponement.
- **Failure example** — priority inflation makes every task urgent, which collapses the ordering into chaos.

## Related
- [[wiki/agent-systems/task-scheduling-agents|Task Scheduling for Agents]] — the scheduling layer that applies priorities
- [[wiki/agent-systems/queueing-agents|Queueing Agents]] — where priorities shape ordering
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — resource limits that constrain what can run
- [[wiki/api-protocols/load-shedding|Load Shedding]] — what happens when demand exceeds capacity
