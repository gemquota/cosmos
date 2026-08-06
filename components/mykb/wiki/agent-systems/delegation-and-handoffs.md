---
type: "concept"
title: "Delegation and Handoffs"
description: "Moving tasks and context from one agent to another with full transfer of responsibility"
tags: ["agents", "handoffs", "delegation", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2304.03442", "https://arxiv.org/abs/2307.09288"]
---

# Delegation and Handoffs

## Summary
Delegation is assigning a task to another agent; a handoff is transferring active context, authority, and responsibility so the receiving agent can continue seamlessly. Handoffs are how multi-agent systems scale beyond one context window. A broken handoff loses state and produces confused agents.

## Details
- **What transfers** — goal, relevant history, constraints, artifacts, and approval authority; the handoff protocol should make this explicit.
- **Patterns** — sub-agent delegation with results returned, escalation handoffs to more capable agents, and human handoffs at approval gates.
- **Failure modes** — duplicated work, dropped context, contradictory instructions; mitigated by structured handoff records and success criteria.
- **Worked example** — a triage agent routes a bug report to the frontend agent with a summary, repro steps, and the constraint not to touch the backend.
- **Tooling** — handoff messages, shared blackboards, and tool registries all support context transfer.
- **mykb relevance** — the handoff protocol is a documented pattern in mykb, and RSIS3 sub-agents use it during code generation.

- **Success criteria transfer** — the handoff includes how success will be judged, so the receiving agent knows when to stop and what to return.
- **Verification on return** — the delegator checks returned work against the success criteria before accepting; acceptance is the last step of the handoff, not the transfer itself.
- **Trust and verification** — delegation without verification is abdication; the delegator retains accountability and checks the returned work, so delegation extends capability without dropping responsibility.
- **Context minimization** — handoffs should carry the minimal context needed: full transcripts breed confusion and cost; a structured summary plus pointers works better.
- **Handoff records** — every handoff is logged with its payload and outcome so the workflow can be replayed and audited after a failure.
## Related
- [[wiki/agent-systems/sub-agent-delegation|Sub-Agent Delegation]] — delegating work to sub-agents
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]] — the structured handoff pattern
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — oversight during delegation
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — tools as delegation targets
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — delegating to specialists
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/agent-systems/agent-prioritization|Agent Prioritization]] — related concept in this cluster
