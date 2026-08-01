---
type: "concept"
title: "Handoff Protocol"
description: "The structured transfer of control and context between agents"
tags: ["handoff", "multi-agent", "protocol", "context"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Handoff Protocol

## Summary
A handoff protocol defines how one agent transfers control to another: what context is passed, who owns the result, and how failures return. It matters because poorly specified handoffs lose context and accountability. Handoffs are the glue of multi-agent orchestration.

## Details
- Payload: task state, constraints, history digest, success criteria.
- Return paths: result back to caller, or permanent transfer.
- Logging the handoff enables traceability across agents.
- Open questions: context compression at handoff boundaries.

## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — delegation via handoffs
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — handoffs up and down the tree
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role context in the payload
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — handoff as a state transition
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — the coordination context
