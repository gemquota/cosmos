---
type: "concept"
title: "Handoff Protocol"
description: "The structured transfer of control and context between agents"
tags: ["handoff", "multi-agent", "protocol", "context"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Handoff Protocol

## Summary

A handoff protocol is the contract for transferring a task between agents (or agent to human): what state travels, what the receiver needs to resume, and what completion looks like. It is the distributed-systems discipline applied to agent collaboration.

## Details
- Mechanism: a handoff packages context — goal, progress, artifacts, constraints, decisions made, next steps, and failure history — in a structured envelope (JSON, a shared note, or a message); the receiver validates the envelope, acknowledges receipt, and reports status; handoffs are logged with both parties and the transferred state for traceability.
- Concrete example: an analyst agent completes a research phase and hands the synthesis task to a writer agent with the findings, citations, and tone constraints in one envelope; a human takes over a stuck agent's run with the full trace and pending decision highlighted; a long-running loop checkpoints its state so a restart hands off seamlessly.
- Failure modes: handoffs that transfer narrative but not state (the receiver redoes work); lossy context — decisions made but not recorded; protocol drift between agent versions; and handoff storms where tasks bounce between agents without progress (escalation rules needed).
- Operational tradeoffs: structured handoffs cost writing discipline and schema maintenance; they pay in resumability, accountability, and composability of agents. The standard is a versioned envelope schema, idempotent resume, and metrics on handoff success.
- RSIS3/mykb relevance: the wiki's multi-agent passes would use a versioned handoff envelope, so a pass interrupted mid-stream resumes from recorded state instead of restarting.
- Envelope schema versioning: include schema version in the envelope and reject incompatible receivers loudly rather than misparsing state.
- Failure accounting: log handoff failures with reasons (timeout, validation, receiver error) — repeated failures indicate a protocol design problem, not bad luck.

## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — delegation via handoffs
- [[wiki/agent-systems/hierarchical-agents|Hierarchical Agents]] — handoffs up and down the tree
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role context in the payload
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — handoff as a state transition
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — the coordination context
