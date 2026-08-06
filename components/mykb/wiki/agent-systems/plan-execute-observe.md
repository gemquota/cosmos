---
type: "concept"
title: "Plan-Execute-Observe"
description: "A control loop that plans, acts, observes results, and replans"
tags: ["agents", "loop", "planning", "control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.03629", "https://arxiv.org/abs/2305.16291"]
---

# Plan-Execute-Observe

## Summary
Plan-execute-observe is the canonical agent control loop: generate a plan, execute a step, observe the outcome, and revise. It is explicit about the feedback signal other loops leave implicit. The quality of the observation step decides whether the loop converges or drifts.

## Details
- **Phases** — plan (decompose goal), execute (run an action or tool call), observe (capture result and environment change), then revise the plan.
- **Feedback** — observations update the plan, the goal interpretation, and sometimes the memory of what works.
- **Loop variants** — with replanning every step, only on failure, or on a fixed cadence; fewer replans are cheaper but riskier.
- **Worked example** — a scraper agent plans selectors, executes a fetch, observes an anti-bot page, and replans to use the browser agent.
- **Success criteria** — each step declares what would make it done, so the loop can stop early and escalate on repeated failure.
- **mykb relevance** — RSIS3's nine-phase pulse protocol is a rich plan-execute-observe loop with explicit evaluation phases.

- **Observation design** — the observe step should capture structured outcomes (result schema, error class, state delta), not just raw text; structured observations are what make replanning decisions testable.
- **Replan triggers** — replan on failure, on evidence that the plan is drifting from reality, or on new information; bound the number of replans so the loop cannot churn forever.
- **Retry vs replan** — transient errors warrant a retry of the same step; persistent mismatches between plan and world warrant a replan; conflating the two is a common failure.
- **Stop early** — each step declares its success criterion, so the loop can terminate as soon as the goal is met instead of executing the remaining plan by inertia.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the existing loop concept
- [[wiki/agent-systems/checkpointing-agent-runs|Checkpointing Agent Runs]] — durable state between loops
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — when loops end
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — evaluating loop outcomes
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — related concept in this cluster
- [[wiki/agent-systems/task-scheduling-agents|Task Scheduling for Agents]] — related concept in this cluster
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
