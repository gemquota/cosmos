---
type: "concept"
title: "Agent Loop"
description: "The fundamental cycle of perceive, decide, act, and observe that drives every autonomous agent"
tags: ["agent-loop", "architecture", "autonomy", "rsis3", "action-observation"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.anthropic.com/research/building-effective-agents"]
---

# Agent Loop

## Summary
An agent loop is the repeating control cycle in which an agent interprets a task, selects an action, invokes a tool or model call, observes the result, and decides whether to continue. It matters because every higher-level capability — planning, memory, delegation, self-improvement — runs on top of this loop, and its exit conditions determine whether work completes or spins forever. In RSIS3 this is the L1 per-task action loop: each pulse invokes tools, collects observations, and retries before escalating.

## Details
- **Phases**: receive task → choose action → invoke tool → observe outcome → update internal state → repeat or stop.
- **Tools are the action channel**: the loop is only as capable as the tools it can call; observations are structured outputs, errors, or timeouts.
- **Stop conditions** decide termination: success criteria met, step budget exhausted, fatal error, or explicit halt from an operator.
- RSIS3 instantiates this as L1 with telemetry written after every turn, so each loop iteration is auditable from the dashboard.
- Worked example: a code-generation agent iterates the loop as apply_patch → run tests → observe pass/fail → retry or roll back via git.
- Design rule: keep the loop pure and log every transition so the run can be replayed deterministically.

## Related

- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the ReAct-style pattern this loop instantiates
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — how loop actions are expressed as tool calls
- [[wiki/agent-systems/retry-strategies|Retry Strategies]] — the recovery behavior that keeps the loop alive
- [[wiki/concepts/perception-loop|Perception Loop]] — the sensing side of the cycle
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — when the loop terminates
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — RSIS3 hosts this loop in the wider ecosystem
- [[raw/archive/session-artifacts-2026-07/tools/update-plan-1-2|update_plan — the planning tool used inside the loop]]
- [[raw/archive/session-artifacts-2026-07/tools/exec-command-1-2|exec_command — a typical loop tool in RSIS3]]