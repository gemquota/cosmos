---
type: "concept"
title: "Permission Model"
description: "The rules deciding which agent actions are allowed"
tags: ["permissions", "authorization", "safety", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Permission Model

## Summary
A permission model defines what an agent may do: which tools, paths, hosts, and operations, under which conditions. It matters because permissions are the primary safety boundary before execution. Good models are minimal, explicit, and auditable.

## Details
- Deny by default; grant the least privilege a task needs.
- Permissions can be static (config) or dynamic (per-task scopes).
- Every decision is logged for traceability and review.
- Open questions: permission refinement from task semantics.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — permissions as risk bounds
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints on permission boundaries
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — runtime enforcement of the model
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — enforcement at the environment level
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — tools as permissioned actions
