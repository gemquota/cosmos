---
type: "concept"
title: "Autonomy Levels"
description: "A spectrum from human-driven to fully self-directed agent operation"
tags: ["autonomy", "human-in-the-loop", "agents", "levels", "oversight"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2311.02462"]
---

# Autonomy Levels

## Summary
Autonomy levels classify how much a system does by itself versus how much a human drives or approves. It matters because autonomy should match reliability: high autonomy on low-stakes tasks, human checkpoints on irreversible ones. The Levels of AGI paper applies this kind of ladder to capability; agent deployments need the same ladder for control.

## Details
- **Typical ladder**: human does everything → assistant suggests → agent proposes, human approves → agent acts, human supervises → agent self-directs with policy bounds.
- **Control correlates with stakes**: read-only operations may be fully autonomous; production deploys get approval gates.
- Autonomy must be dynamic: a well-behaved agent earns more, a crisis revokes it.
- RSIS3 tunes autonomy per loop: L1 tool calls run freely inside bounds, L2/L3 changes are test-gated and logged.
- Worked example: a research agent autonomously searches and drafts, but requires an approval gate before publishing.
- Failed autonomy is usually a calibration failure: overconfidence in bounds, not the model.

- **Levels are a governance artifact** — assigning a level is a decision about trust, recorded in policy, not a property of the model; the level names the review and audit obligations that come with it.
- **Escalation rules** — each level defines its own fallback: when the agent exceeds confidence bounds or hits a boundary, it drops to a lower level (more human review) rather than continuing unaided.
- **Calibration** — failed autonomy is usually a calibration failure: overconfidence in the agent's bounds or the environment's stability, not a failure of the model itself.
- **Worked example** — a research agent autonomously searches and drafts but requires an approval gate before publishing; the level describes the whole policy, not just the agent's abilities.
## Related

- [[wiki/llm-agents/human-in-the-loop|Human-in-the-Loop]] — the human checkpoint pattern
- [[wiki/llm-agents/approval-gates|Approval Gates]] — the mechanism that implements checkpoints
- [[wiki/llm-agents/agent-personas|Agent Personas]] — role framing at each autonomy level
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — bounds that make higher autonomy safe
- [[wiki/ops/gap-report|Gap Analysis Report]] — autonomy failures surface as gaps
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — policy knowledge that guides autonomy