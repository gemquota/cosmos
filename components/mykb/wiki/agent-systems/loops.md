---
type: "concept"
title: "Loops"
description: "Iterative execution patterns that repeat actions until success or a stop condition"
tags: ["agents", "loops", "iteration", "control-flow"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.16291", "https://arxiv.org/abs/2303.17548"]
---

# Loops

## Summary
Loops repeat agent actions until a success criterion, a budget, or a stop condition is reached. They are how agents do search, self-correction, and convergent refinement. Unbounded loops are the most common agent reliability failure — every loop needs an exit.

## Details
- **Types** — retry loops with backoff, reflection loops (generate → critique → revise), retrieval loops, and verification loops.
- **Loop control** — max iterations, token budgets, wall-clock timeouts, and success criteria all terminate loops; circuit breakers stop pathological ones.
- **State across iterations** — each iteration should record its attempt so later iterations learn from earlier failures.
- **Worked example** — a repair agent: run tests → read failure → patch → rerun, up to three attempts, then escalate with the failure history.
- **Cost** — each iteration multiplies latency and tokens; loop efficiency is a first-order cost lever.
- **mykb relevance** — RSIS3's top-3 loops are the canonical example: fixed, tuned loops with explicit stop conditions and checkpoints.

- **Exit conditions** — every loop terminates on one of: success criterion met, budget exhausted, escalation triggered, or human interrupt; loops with no enumerated exit are bugs.
- **State change requirement** — each iteration must change some state or consume some resource; a loop that repeats with identical state is an infinite loop regardless of its stop condition.
- **Nested loops** — practical agents nest loops: an inner retry loop per tool call, an outer reflection loop per task, and a supervision loop per session, each with its own budget.
- **Observability** — per-iteration logs (attempt, outcome, state delta) turn a loop from a black box into a diagnosable artifact when it misbehaves.

## Related
- [[wiki/agent-systems/plan-execute-observe|Plan-Execute-Observe]] — the loop around a plan
- [[wiki/agent-systems/retry-and-backoff-patterns|Retry and Backoff Patterns]] — retry loops
- [[wiki/agent-systems/generator-verifier-loop|Generator-Verifier Loop]] — generate-and-check loops
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — terminating loops
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — time-based termination
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — aborting pathological loops
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — recursion as an outer loop
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — reflection loops
