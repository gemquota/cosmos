---
type: "concept"
title: "Agentic Workflows"
description: "End-to-end multi-step processes driven by an agent's loop"
tags: ["agentic-workflows", "automation", "processes", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.03629", "https://arxiv.org/abs/2304.03442"]
---

# Agentic Workflows

## Summary
An agentic workflow is a complete multi-step process — plan, research, implement, verify, report — orchestrated by an agent rather than a fixed script. It matters because it turns one-shot model calls into dependable task completion. Workflows are where loops, tools, and memory meet.

## Details
- **Structure** — a workflow chains phases with handoffs, success criteria, and stop conditions; each phase may itself be an agentic loop.
- **Workflow vs pipeline** — pipelines are fixed DAGs; workflows replan based on observations, making them adaptive.
- **State** — workflow state (context, artifacts, progress) must be explicit and persisted for resume, replay, and audit.
- **Worked example** — a release workflow: gather changelog → draft release notes → review against policy → publish → verify the page.
- **Reliability** — checkpoints, retries, escalations, and approvals make workflows robust where scripts fail.
- **mykb relevance** — RSIS3's pulse protocol is a nine-phase agentic workflow with explicit evaluation gates.
- **Variants** — prompt-chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, and autonomous loops; each fits different task shapes.
- **Pattern choice** — deterministic pipelines suit predictable work; autonomous loops fit open-ended goals but need budgets and checkpoints.
- **Worked example** — an orchestrator-worker pattern: a planner splits a report into sections, workers draft each, a reviewer merges and polishes.

## Related
- [[wiki/agent-systems/delegation-and-handoffs|Delegation and Handoffs]] — moving work between phases
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining completion
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — durable workflow state
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — chaining prompts in workflows
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]] — linear workflow structure
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — orchestrating workflow steps
- [[wiki/agent-systems/task-scheduling-agents|Task Scheduling for Agents]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
