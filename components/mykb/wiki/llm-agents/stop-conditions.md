---
type: "concept"
title: "Stop Conditions"
description: "The explicit rules that terminate an agent run"
tags: ["stop-conditions", "termination", "control-flow", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Stop Conditions

## Summary
Stop conditions define when an agent run ends: success criteria met, budget exhausted, error threshold crossed, or operator halt. They matter because unbounded loops waste resources and can escalate damage. Good stop conditions are the inverse of good success criteria.

## Details
- Types: success, budget (steps/time/cost), fatal error, explicit halt.
- Must be checked every loop iteration, not opportunistically.
- Poor stops either cut work early or let failure run long.
- Open questions: dynamic stop thresholds from risk assessment.

## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop these conditions terminate
- [[wiki/llm-agents/success-criteria|Success Criteria]] — the positive counterpart
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — terminal states formalized
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — workflow end conditions
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — checking stop quality
