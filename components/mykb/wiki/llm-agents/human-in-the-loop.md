---
type: "concept"
title: "Human-in-the-Loop"
description: "Designs where humans review, approve, or correct agent actions"
tags: ["human-in-the-loop", "oversight", "approval", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Human-in-the-Loop

## Summary

Human-in-the-loop (HITL) places a person at critical points of an agent workflow — review, approval, correction, or takeover. It is the pragmatic middle of the autonomy spectrum: agents handle the routine, humans handle the consequential, with the interface designed so humans can actually judge.

## Details
- Mechanism: HITL designs gates (approve/reject), review queues (draft outputs awaiting validation), correction loops (human edits feed back into the agent), and escalation paths (agent requests help when confidence is low); the human's role is decision-grade, so the agent must present enough context (what, why, options, risks) to make the decision well.
- Concrete example: an agent drafts a public post and queues it for human review with its sources; a code agent proposes a large refactor and waits for approval with a diff summary; a research agent flags a low-confidence claim and asks a domain expert before committing it to the wiki.
- Failure modes: rubber-stamping — approvals without review (fatigue, poor context); humans as a bottleneck (queues pile up, agents stall — add SLAs and escalation); HITL as theater (the agent redoes what was rejected); and losing the human's input when it should influence the loop (corrections not fed back).
- Operational tradeoffs: HITL trades speed and autonomy for correctness, safety, and accountability; the discipline is risk-tiered gates, decision-grade context, fast review UX, and closed loops where human corrections improve future behavior.
- RSIS3/mykb relevance: the wiki's agents gate consequential writes and external actions through HITL, with corrections captured as knowledge for future passes.
- Queue design: human review queues need SLAs and fallbacks (escalate, auto-hold) so the loop is not silently blocked by a full queue.
- Feedback capture: treat human corrections as labeled training/steering data — store them with the triggering context so future versions learn from them.

## Related
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — HITL defines the level
- [[wiki/llm-agents/approval-gates|Approval Gates]] — the concrete mechanism
- [[wiki/llm-agents/permission-model|Permission Model]] — what requires a human
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — where humans slot in
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — HITL as a policy rule
