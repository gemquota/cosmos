---
type: "entity"
title: "PulseContext"
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---
description: "The context object that carries state and artifacts through a pulse or loop iteration"
tags: ["entity", "android", "api", "ast", "auth", "authorization", "context", "loops"]

# PulseContext

## Summary
PulseContext is the state bundle passed through each iteration of a pulse or loop protocol: current inputs, intermediate results, decisions, and evaluation data. It matters because loops only work reliably when state is explicit, serializable, and inspectable between steps. A well-defined pulse context makes iterations repeatable, resumable, and debuggable. Treating the context as a first-class artifact is what separates a real loop from a script.

## Details
- **Definition** — a pulse context aggregates the data a loop iteration needs: goal, artifacts, tool results, observations, and status.
- **Immutability** — treating each iteration's context as a new snapshot prevents aliasing bugs and makes replay possible.
- **Serialization** — context should be serializable so runs can be checkpointed, resumed, and audited after the fact.
- **Bounds** — context must stay within size and scope limits, carrying summaries rather than unbounded histories.
- **Evaluation hooks** — embedding results and criteria in the context lets each iteration be scored against its goals.
- **Handoff** — passing the context between phases or agents preserves continuity without duplicating global state.
- **Checkpointing** — writing a context snapshot at safe points lets a crashed run resume instead of starting over.
- **Versioning** — tagging context schemas lets older checkpoints be read by newer code, keeping history usable.
- **Common failure modes** — context that grows without bound, fields mutated in place across steps, and partial copies that lose decisions.
- **Worked example** — an improvement loop creates a fresh pulse context per iteration, appends the observed outcome, and writes the snapshot to a checkpoint store before the next round.
- **Practical relevance** — explicit pulse context is what makes iterative protocols observable, resumable, and trustworthy.

## Related
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — stateful sessions
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop driving pulses
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — observing iterations
- [[wiki/llm-agents/agentic-loops|Agentic Loops]] — iterative protocols
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — persisting context
- [[wiki/agent-systems/agent-state-machines|Agent State Machines]] — state transitions
