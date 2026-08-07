---
type: "concept"
title: "Escalation Handling"
description: "Routing work to more capable agents or humans when an agent is stuck or out of scope"
tags: ["agents", "escalation", "reliability", "workflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.16291", "https://arxiv.org/abs/2307.09288"]
---

# Escalation Handling

## Summary
Escalation handling defines what happens when an agent cannot complete a task: retry within limits, hand off to a stronger agent, or raise to a human. Escalation is a planned path, not an accident. Clear escalation policies prevent stuck agents from burning budget or producing wrong answers silently.

## Details
- **Triggers** — repeated failures, low confidence, missing permissions, out-of-scope requests, or budget exhaustion.
- **Escalation ladder** — retry with more context → stronger model → human with a structured report of what was tried.
- **Escalation artifacts** — the escalation must carry the attempt history, hypotheses, and evidence so the next agent or human starts informed.
- **Worked example** — a support agent escalates after two failed resolution attempts, attaching the conversation and the diagnostic steps tried.
- **Anti-patterns** — escalating immediately (avoidable cost), or never escalating (silent failure).
- **mykb relevance** — escalation is a core reliability pattern for autonomous systems like RSIS3, where a stuck loop must hand off cleanly.

- **Escalation budget** — each task carries an escalation budget (max retries, max cost) so escalation is itself bounded and cannot become an infinite ladder.
- **Post-escalation review** — escalated cases are reviewed to improve the system: if the same task always escalates, it should be automated or the trigger recalibrated.
- **Structured reports** — the escalation artifact (attempt history, hypotheses, evidence) is what makes the next agent or human productive; an escalation without context just moves the stuck-ness.
- **Escalation as telemetry** — escalation rates per task type are tracked; rising rates signal a problem worth fixing at the root rather than routing around.
- **Anti-patterns** — escalating immediately wastes cost on solvable tasks; never escalating produces silent failures; both are tuning failures of the triggers.
## Related
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — timeouts as escalation triggers
- [[wiki/llm-agents/expert-consultation|Expert Consultation]] — escalating to specialist agents
- [[wiki/agent-systems/circuit-breakers-for-agents|Circuit Breakers for Agents]] — stopping before escalation
- [[wiki/llm-agents/success-criteria|Success Criteria]] — defining when a task is done
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — when to stop trying
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — related concept in this cluster
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop agents execute
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
