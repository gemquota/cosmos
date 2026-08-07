---
type: "concept"
title: "Session State Machine"
description: "Modeling an agent session as a finite state machine with explicit transitions"
tags: ["state-machine", "sessions", "rsis3", "rrp", "control-flow"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://langchain-ai.github.io/langgraph/"]
---

# Session State Machine

## Summary
A session state machine formalizes an agent session as states (running, awaiting input, retrying, failed, done) with defined transitions and guards. It matters because sessions are long, interruptible, and resumable, and an explicit machine prevents ad-hoc control flow. RSIS3's RRP protocol is a large, deliberate state machine: 2,025 lines defining how refinement sessions progress.

## Details
- **States and transitions**: each state defines what actions are legal, so the agent cannot skip steps like validation.
- **Persistence**: the state machine must be serializable so sessions survive crashes and resume.
- **Guards** (preconditions) and **effects** make transitions testable and auditable.
- **Terminal states** are explicit: success, failure, cancelled — matching stop conditions.
- RSIS3's RRP state machine drives its self-improvement sessions; the dashboard renders the current state as telemetry.
- Worked example: a refinement session moves define → generate → validate → accept, where validate failure returns to generate with a bounded retry count.

- **Error states** — retrying, degraded, and failed must be explicit states with defined transitions, so partial failures take a known path instead of an ad-hoc one.
- **Observability** — the dashboard renders the current state, and every transition is logged with its trigger, turning session behavior into inspectable telemetry.
- **Testability** — transition coverage tests (can every state be reached? can every guard block a transition?) catch control-flow bugs before production.
- **Resumability** — serializable state means a crashed session restarts in its last stable state, not from scratch; persistence is part of the machine, not an add-on.

- **Guard discipline** — guards (preconditions) make transitions safe by construction: a transition that is not legal in the current state simply does not fire, which is how the machine prevents skips and out-of-order steps.

## Related

- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioning sessions as their machines evolve
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — the terminal-state definitions
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — replaying state transitions for debugging
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the transition log every session writes
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — session states persist into the knowledge base
- [[wiki/ops/gap-report|Gap Analysis Report]] — session gaps surfaced by analysis