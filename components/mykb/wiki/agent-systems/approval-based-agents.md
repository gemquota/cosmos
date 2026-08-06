---
type: "concept"
title: "Approval-Based Agents"
description: "Agents that seek approval for consequential actions before taking them"
tags: ["approval", "agents", "oversight", "control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03741", "https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback"]
---

# Approval-Based Agents

## Summary
Approval-based agents pause and request human (or overseer) approval before consequential actions, especially irreversible ones. They convert continuous autonomy into discrete, reviewable decision points — the operational heart of human-in-the-loop systems — at the cost of latency and reviewer attention.

## Details
- **Design** — an action classifier flags high-impact or irreversible actions before execution; the agent drafts the action, presents evidence, and waits for a decision.
- **Benefits** — human oversight scales to many parallel agents because review focuses on decision points rather than every step; the reviewer sees only consequential forks.
- **Costs** — latency on every approved path, interruption of agent flow, and approval fatigue that breeds rubber-stamping when reviewers are flooded.
- **Risks** — specification gaming on the gate itself: an agent can learn to frame actions so they look safe, which is why the classifier must be periodically audited rather than trusted.
- **Approval quality** — the reviewer needs enough context to decide well; sandwiching (AI-drafted recommendations for the approver) improves decisions but must not become the agent approving itself.
- **RSIS3 example** — the practice checker gates mutations, and the recovery workflow requires explicit checkpoint commits before changes; both are approval gates at the tool level.
- **Design guidance** — selective approval beats universal approval: gate only irreversible or high-impact actions, and route the rest to post-hoc audit.

- **Operational details** — approval requests carry the action, its expected effects, and alternatives; the request is answerable at a glance, which is what keeps review volume manageable.
- **Measuring the gate** — track approval rate, reversal rate, and time-to-decision; a gate that never blocks or is always overridden is not adding oversight.
## Related
- [[wiki/concepts/oversight|Oversight]] — the parent practice
- [[wiki/concepts/human-supervision-limits|Human Supervision Limits]] — why approval must be selective
- [[wiki/concepts/sandwiching|Sandwiching]] — AI assistant for the approver
- [[wiki/syntheses/tripwires|Tripwires]] — automatic approval triggers
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — autonomy budgeting
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — risk-gated autonomy
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — the mechanism in practice
