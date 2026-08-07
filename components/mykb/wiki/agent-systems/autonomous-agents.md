---
type: "concept"
title: "Autonomous Agents"
description: "Agents that pursue goals over long horizons with limited human intervention"
tags: ["agents", "autonomy", "goal-seeking", "systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://arxiv.org/abs/2210.03629"]
---

# Autonomous Agents

## Summary
An autonomous agent perceives its environment, plans, and acts toward a goal across multiple steps without step-by-step human control. Autonomy exists on a spectrum from single-shot assistants to long-running systems that manage their own subgoals, tools, and recovery. It matters because autonomy is what turns a language model call into a system that completes real work.

## Details
- **Autonomy levels** — from supervised single actions, through batch autonomy with approval gates, to full autonomy with checkpoints and rollback; each level trades human oversight for speed.
- **Core loop** — sense → plan → act → observe, with memory and reflection feeding back into the next cycle; see the action-observation loop pattern.
- **Prerequisites** — reliable tools, deterministic replay for debugging, budget controls, and observability before autonomy can be safely raised.
- **Worked example** — a research agent given a question retrieves documents, drafts findings, verifies citations, and self-reports confidence, escalating only on low confidence.
- **Failure modes** — goal drift, confirmation loops, runaway costs; mitigation combines circuit breakers, budgets, and escalation handling.
- **mykb relevance** — RSIS3 runs as an autonomous agent on the triad architecture, so its recursion, memory, and recovery patterns map directly onto this design space.

- **Escalation contract** — every autonomous agent defines what triggers human escalation: low confidence, budget exhaustion, out-of-scope requests, or repeated failure; the contract is written before autonomy is granted.
- **Observability precondition** — autonomy is only raised when runs can be traced and replayed; unobservable autonomy is a liability, not a feature.
## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop autonomous agents execute
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — the spectrum autonomy is measured on
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — limits that keep autonomy safe
- [[wiki/agent-systems/agent-observability|Agent Observability]] — visibility needed before raising autonomy
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — safe autonomy under uncertainty
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — related concept in this cluster
- [[wiki/agent-systems/agent-cancellation|Agent Cancellation]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
