---
type: "concept"
title: "Agentic Workflows"
description: "End-to-end multi-step processes driven by an agent's loop"
tags: ["agentic-workflows", "automation", "processes", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agentic Workflows

## Summary
An agentic workflow is a complete multi-step process — plan, research, implement, verify, report — orchestrated by an agent rather than a fixed script. It matters because it turns one-shot model calls into dependable task completion. Workflows are where loops, tools, and memory meet.

## Details
- Characterized by branching, retries, and human checkpoints.
- Distinct from rigid pipelines: the agent chooses the path.
- Needs explicit success criteria and stop conditions.
- RSIS3 relevance: pulses and sessions are agentic workflows.

## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop driving the workflow
- [[wiki/llm-agents/human-in-the-loop|Human-in-the-Loop]] — checkpoints inside workflows
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — workflow termination
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — the actions composing it
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining done
