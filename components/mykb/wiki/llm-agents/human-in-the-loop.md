---
type: "concept"
title: "Human-in-the-Loop"
description: "Designs where humans review, approve, or correct agent actions"
tags: ["human-in-the-loop", "oversight", "approval", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Human-in-the-Loop

## Summary
Human-in-the-loop (HITL) keeps a human in the decision path at key points: reviewing plans, approving irreversible actions, or correcting mistakes. It matters because some judgments are too consequential or too under-specified to delegate. HITL is a knob on the autonomy spectrum.

## Details
- Interaction points: approval gates, review queues, correction loops.
- Effective HITL minimizes human burden while maximizing control.
- Feedback from humans becomes training data and memory.
- Open questions: when HITL adds more risk than it removes.

## Related
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — HITL defines the level
- [[wiki/llm-agents/approval-gates|Approval Gates]] — the concrete mechanism
- [[wiki/llm-agents/permission-model|Permission Model]] — what requires a human
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — where humans slot in
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — HITL as a policy rule
