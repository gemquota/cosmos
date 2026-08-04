---
type: "concept"
title: "User Confirmation Flows"
description: "Checkpoints where agents must get user approval before consequential actions"
tags: ["confirmations", "users", "approvals", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# User Confirmation Flows

## Summary

User confirmation flows are checkpoints where an agent must obtain explicit user approval before performing consequential actions. They are the human-in-the-loop safety valve that separates autonomous execution from irreversible or costly changes. They matter because well-designed confirmations prevent damage without grinding agent work to a halt. The pattern is a product decision as much as a safety mechanism: too many gates erode trust, too few invite harm.

## Details

- **Purpose** — Confirmations gate actions that are destructive, costly, irreversible, or high-trust, such as deletions, purchases, or credential changes.
- **Checkpoint design** — Each checkpoint states what will happen, what will change, and what cannot be undone, so approval is genuinely informed.
- **Presentation** — Clear summaries with concrete consequences outperform jargon-heavy dialogs; the user should be able to approve without spelunking logs.
- **Granularity** — Confirming every step causes fatigue; confirming only high-impact actions preserves trust and velocity.
- **Timeouts and defaults** — Unattended flows need safe defaults: expire pending confirmations, default to no action, and log the outcome.
- **Batching** — Grouping related consequential actions into one confirmation reduces interruptions while keeping a single approval point.
- **Failure modes** — Confirmation fatigue, rubber-stamping, and confirmations that bury the risky part in fine print undermine the whole mechanism.
- **Worked example** — An agent preparing a release pauses before publishing, shows the changelog and rollback plan, and proceeds only on approval.
- **Practical relevance** — Confirmation flows extend permissioning systems from static policies to interactive decision points.
- **Context-aware triggers** — Confirmation thresholds adapt to risk: read-only actions pass, mutating actions pause, destructive actions require explicit confirmation.
- **Reversibility check** — The strongest signal for whether to confirm is reversibility; reversible actions need fewer gates.
- **Auditability** — Every confirmation decision, granted or denied, is logged with the presented summary for later review.

## Related

- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — the approval system confirmations plug into
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — human oversight patterns
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — paths when confirmation is refused
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — the supervision layer around flows
- [[wiki/llm-agents/approval-gates|Approval Gates]] — gates for consequential actions
