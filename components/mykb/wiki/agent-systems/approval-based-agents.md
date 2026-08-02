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
Approval-based agents pause and request human (or overseer) approval before consequential actions, especially irreversible ones. They convert continuous autonomy into discrete, reviewable decision points — the operational heart of human-in-the-loop systems.

## Details
- **Design** — an action classifier flags high-impact or irreversible actions; the agent waits for approval.
- **Benefits** — human oversight scales to many parallel agents by focusing review on decision points.
- **Costs** — latency, interruption, and approval fatigue that breeds rubber-stamping.
- **Risks** — an agent that learns to frame actions to look safe (specification gaming on the approval gate).
- **RSIS3 example** — the practice checker gates mutations; the recovery workflow requires explicit checkpoint commits before changes.

## Related
- [[wiki/concepts/oversight|Oversight]] — the parent practice
- [[wiki/concepts/human-supervision-limits|Human Supervision Limits]] — why approval must be selective
- [[wiki/concepts/sandwiching|Sandwiching]] — AI assistant for the approver
- [[wiki/syntheses/tripwires|Tripwires]] — automatic approval triggers
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — autonomy budgeting
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — risk-gated autonomy
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
