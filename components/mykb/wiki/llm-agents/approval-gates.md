---
type: "concept"
title: "Approval Gates"
description: "Human checkpoints where an agent must wait for explicit go-ahead"
tags: ["approval-gates", "human-in-the-loop", "safety", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Approval Gates

## Summary
Approval gates pause the agent at defined decision points until a human approves or rejects the proposed action. They matter because they convert policy judgment from the agent to a human for irreversible or high-impact steps. They are the operational form of human-in-the-loop control.

## Details
- Triggered by risk level, cost, or irreversibility of the action.
- Present the proposed action, rationale, and alternatives compactly.
- Gates slow the loop; the goal is to minimize their frequency.
- RSIS3 relevance: approval gates sit between L1 action and execution when policy demands.

## Related
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — isolation plus gates
- [[wiki/llm-agents/permission-model|Permission Model]] — the policy that triggers gates
- [[wiki/llm-agents/human-in-the-loop|Human-in-the-Loop]] — the broader pattern
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — gates define the autonomy level
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — the runtime that enforces gates
