---
type: "concept"
title: "Human-in-the-Loop Approvals"
description: "Approval gates where a human reviews and authorizes agent actions"
tags: ["agents", "human-in-the-loop", "approvals", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://docs.anthropic.com/en/docs/build-with-claude/tool-use"]
---

# Human-in-the-Loop Approvals

## Summary
Human-in-the-loop approval inserts a review step before high-risk agent actions — spending money, publishing, deleting, or changing permissions. Approvals bound autonomy without removing it. The design challenge is deciding which actions need approval and keeping the human's burden sustainable.

## Details
- **What needs approval** — irreversible actions, external communications, purchases, security changes; routine internal steps usually do not.
- **Gate mechanics** — the agent pauses in an awaiting-approval state, presents context and a proposed action, and resumes only on approval or rejection.
- **Context quality** — approvals are only as good as the summary the agent provides; bad summaries produce rubber-stamping.
- **Worked example** — a deployment agent presents a diff and rollback plan; the human approves, and the agent proceeds with a checkpoint before the change.
- **Alternatives** — pre-approved scopes, time-boxed approvals, and policy-based automation reduce the human load.
- **mykb relevance** — approval gates and the permission model are documented mykb patterns for exactly this control.

## Related
- [[wiki/llm-agents/approval-gates|Approval Gates]] — the approval pattern
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — who may approve what
- [[wiki/llm-agents/permission-model|Permission Model]] — the permissions behind gates
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — escalating to humans
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — human oversight generally
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — bounding autonomy by risk
- [[wiki/llm-agents/human-in-the-loop|Human-in-the-Loop]] — existing human-in-the-loop concept
- [[wiki/llm-agents/user-confirmation-flows|User Confirmation Flows]] — confirmations in interaction
