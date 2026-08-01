---
type: "concept"
title: "Policy Enforcement"
description: "Runtime mechanisms that check agent actions against policy"
tags: ["policy-enforcement", "policies", "safety", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Policy Enforcement

## Summary
Policy enforcement is the runtime layer that checks each proposed action against policy — permissions, constraints, scope limits — before execution. It matters because policy is only real if it is enforced, not merely described. Enforcement belongs between the agent's intent and the world.

## Details
- Checkpoints: pre-tool, pre-write, pre-deploy, pre-handoff.
- Enforcement is deterministic; it cannot be prompted away.
- Violations are logged and fed back to the agent as observations.
- Open questions: policy granularity without crippling the agent.

## Related
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — the bounds being enforced
- [[wiki/llm-agents/permission-model|Permission Model]] — the policy source
- [[wiki/llm-agents/approval-gates|Approval Gates]] — enforcement via human checkpoints
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — environment-level enforcement
- [[wiki/llm-agents/success-criteria|Success Criteria]] — policy as success constraints
