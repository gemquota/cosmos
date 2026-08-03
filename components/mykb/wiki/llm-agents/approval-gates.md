---
type: "concept"
title: "Approval Gates"
description: "Human checkpoints where an agent must wait for explicit go-ahead"
tags: ["approval-gates", "human-in-the-loop", "safety", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Approval Gates

## Summary

Approval gates pause an agent at a decision point until a human (or policy) approves — before destructive actions, external sends, or high-cost operations. They convert autonomy from a binary into a controlled spectrum and are the backbone of safe human-in-the-loop operation.

## Details
- Mechanism: the agent reaches a gate, presents a proposed action with context and options, and waits; approval can be manual (human confirms), rule-based (policy auto-approves known-safe actions), or escalating (auto-approve up to a threshold); gate results are logged with the requester and decision for audit; timeouts define what happens when no one responds (abort, hold, proceed-with-caution).
- Concrete example: a deployment agent proposes a production change and waits for approval, showing the diff and rollback plan; a wiki agent asks before rewriting a note another author edited; a research agent auto-approves read-only steps and gates only mutations and external posts.
- Failure modes: approval fatigue — too many gates train the human to click through (tier gates by risk); gates bypassed by splitting actions into unapproved pieces; timeout defaults that proceed when no one is watching; and approval that is performative — the approver lacks the context to judge (require decision-grade summaries).
- Operational tradeoffs: gates trade autonomy for safety and auditability; the discipline is risk-tiered gates, rich approval context, logged decisions, and periodic review of gate thresholds as trust and policy evolve.
- RSIS3/mykb relevance: the wiki's agents gate mutations and external side effects by risk class, with every gate decision recorded in the session trace.
- Context quality: the approval request must fit on one screen — action, reason, impact, rollback, and alternatives; an approver who must dig through logs is being set up to rubber-stamp.
- Feedback loop: capture the approver's edits and rejections as signals that tune future proposals (fewer, better gates over time).

## Related
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — isolation plus gates
- [[wiki/llm-agents/permission-model|Permission Model]] — the policy that triggers gates
- [[wiki/llm-agents/human-in-the-loop|Human-in-the-Loop]] — the broader pattern
- [[wiki/agent-systems/autonomy-levels|Autonomy Levels]] — gates define the autonomy level
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — the runtime that enforces gates
