---
type: "concept"
title: "Agent Timeouts"
description: "Maximum execution durations that force agents to stop and report"
tags: ["timeouts", "agents", "control", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Timeouts

## Summary
Agent timeouts are maximum execution durations that force an agent to stop and report, bounding runaway loops and runaway costs. They matter because agents with tools can spin indefinitely, and every extra step costs money and delay. A timeout converts an unbounded failure into a bounded, observable one. Timeouts turn unbounded risk into a bounded, reviewable event.

## Details
- **Definition** — a timeout is a limit on how long an agent may run, measured in wall-clock time, steps, tokens, or tool calls.
- **Trigger types** — wall-clock timeouts bound real duration, while step-count and token limits bound work independent of clock speed.
- **Behavior on timeout** — configured policies decide what happens: checkpoint state, escalate to a human, retry once, or abort cleanly.
- **State preservation** — cooperative timeouts checkpoint progress so a run can resume later instead of losing all work.
- **Integration** — timeouts work with budget-and-quota-control to bound cost and with agent-cancellation for manual stops.
- **Worked example** — a research agent is limited to twenty steps; at step twenty it saves its partial findings and escalates instead of continuing to browse.
- **Failure modes** — timeouts that are too tight abort valuable work, while loose limits let costs balloon; defaults should depend on task complexity.
- **Practical relevance** — timeouts are the simplest protection against the classic agent failure mode of looping forever.
- **Defaults by task** — complex research tasks need longer budgets than simple lookups; defaults should reflect the workload.
- **Warnings** — agents should be warned near the limit so they can wrap up rather than being cut off mid-action.
- **Metrics** — timeout rates reveal tasks whose budgets are miscalibrated.
- **Failure example** — a strict timeout on a long document task aborts the run just before completion, wasting the whole budget.

## Related
- [[wiki/agent-systems/agent-cancellation|Agent Cancellation]] — the explicit stop mechanism
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — cost bounds that complement timeouts
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — capturing state before timeout
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — the post-timeout path
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — protecting dependent systems
