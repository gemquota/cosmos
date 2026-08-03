---
type: "concept"
title: "Stop Conditions"
description: "The explicit rules that terminate an agent run"
tags: ["stop-conditions", "termination", "control-flow", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Stop Conditions

## Summary

Stop conditions define when an agent run ends: task completion, budget exhaustion, iteration caps, confidence thresholds, or explicit approval. They convert open-ended loops into bounded, resumable processes — the difference between an agent and a runaway.

## Details
- Mechanism: conditions are evaluated per iteration: success criteria met (tests pass, goal verified), max iterations, token/time/cost budget, stagnation (no progress across K steps), escalation (agent requests help), or human stop; the runtime checks them between steps and terminates with a recorded status (completed, budget-exceeded, stuck, escalated).
- Concrete example: a coding agent stops when its tests pass or after 10 attempts; a research agent stops at a token budget and writes up partial findings; a self-improvement loop stops a pass when the objective plateaus for 3 iterations; every stop records the reason so post-mortems know why a run ended.
- Failure modes: missing stop conditions (loops run to exhaustion); soft conditions the agent can talk past ("one more iteration" without a counter); stopping on criteria that do not match the goal (tests pass but task incomplete); and hard-coded caps that kill legitimate long runs without resume.
- Operational tradeoffs: stop conditions trade thoroughness for bounded cost and predictability; the discipline is explicit, enforced conditions with recorded outcomes, plus resume/checkpoint support so bounded runs are also resumable.
- RSIS3/mykb relevance: the wiki's loop passes enforce stop conditions at the runtime level, so improvement cycles terminate with a status the synthesis pipeline can consume.
- Progress detection: define stagnation as no improvement in the objective over K consecutive iterations; without it, bounded loops can still spend the whole budget thrashing.
- Resume support: record a checkpoint at each stop so a budget-exceeded run resumes rather than restarts; stopping is only useful if starting again is cheap.

## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop these conditions terminate
- [[wiki/llm-agents/success-criteria|Success Criteria]] — the positive counterpart
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — terminal states formalized
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — workflow end conditions
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — checking stop quality
