---
type: "concept"
title: "Agent State Machines"
description: "Modeling agent runs as explicit states and legal transitions"
tags: ["agents", "state-machine", "reliability", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/langchain-ai/langgraph", "https://arxiv.org/abs/2307.09288"]
---

# Agent State Machines

## Summary
An agent state machine defines the discrete states a run can be in — idle, planning, executing, awaiting approval, failed, done — and the transitions between them. Explicit states make behavior predictable, testable, and resumable. Undefined states are where agents hang, loop, or corrupt work.

## Details
- **States** — pending, running, waiting-for-tool, waiting-for-human, paused, retrying, failed, cancelled, completed.
- **Transitions** — every transition has a trigger and guard; unexpected triggers route to error states instead of undefined behavior.
- **Persistence** — serialized state enables checkpointing, resume, and deterministic replay after crashes.
- **Worked example** — a deployment agent: plan → approve → apply → verify → rollback-or-complete; the approve state blocks until a human approves.
- **Relationship to planning** — plans generate the path; the state machine constrains legal paths at runtime.
- **mykb relevance** — session state machines and RSIS3's pulse state machine apply this discipline to long-running cognitive processes.
- **Transition table** — states (idle, planning, acting, awaiting-approval, done, failed) with events that move between them; unexpected events route to error handling.
- **Tooling** — LangGraph-style graphs encode states explicitly, making loops, retries, and human interrupts inspectable.

- **Transition guards** — each transition carries a guard (permission, precondition, timeout) so illegal moves fail loudly instead of silently corrupting state.
- **Recovery paths** — failed states define explicit recovery: retry with backoff, escalate to a human, or roll back; undefined failure paths are where hangs happen.
- **Visualization** — rendering the state machine makes the agent's legal behaviors reviewable before deployment.
## Related
- [[wiki/agent-systems/plan-execute-observe|Plan-Execute-Observe]] — the loop states formalize
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — existing state machine pattern
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — persisting machine state
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — observing state transitions
- [[wiki/agent-systems/loops|Loops]] — looping within state machines
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — timeouts as state guards
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — terminal states
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — fault states
