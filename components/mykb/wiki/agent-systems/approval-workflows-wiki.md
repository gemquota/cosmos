---
type: "concept"
title: "Approval Workflows"
description: "The review-and-approve path for consequential wiki changes"
tags: ["approval", "workflows", "process", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Approval Workflows

## Summary
Approval workflows define which wiki changes need sign-off before they land: structural changes (merges, splits, deletes), policy changes, and keystone article rewrites. A workflow names the approver, the evidence required, and the fallback when approval stalls, so consequential edits have a reviewable path instead of an ad-hoc one.

## Details
- **What triggers approval** — the bar is set where reversibility ends: cheap reversible edits skip approval, while merges, deletions, and keystone rewrites require it.
- **Workflow contents** — the approver (or role), the required evidence (links, diffs, consensus), and the fallback when approval stalls (escalate, hold, or revert).
- **Costs** — approval slows work, so the design goal is the minimum approval surface that keeps the wiki trustworthy; rubber-stamping is the failure mode of too much friction.
- **Relationship to other processes** — approval workflows sit above the review queues and below the editorial policy: queues surface candidates, workflows route them to approvers, policy sets the standards they are judged against.
- **For mykb** — wiki governance applies the same human-in-the-loop discipline as agent approval gates: consequential changes pause until evidence and sign-off exist.
- **Failure modes** — stalled approvals rot work, over-approval breeds ritual sign-offs, and missing fallbacks leave changes in limbo; each needs an explicit policy.

- **Evidence standard** — the workflow specifies what counts as sufficient evidence (working links, a diff, a summary of changes), so approvers judge against a bar instead of a feeling.
- **Escalation path** — when an approval stalls, the fallback is explicit: escalate to a named role, hold the change, or revert; an undefined fallback leaves work in limbo.
- **Audit trail** — every approval decision is logged with its evidence and approver, so the workflow itself can be reviewed and improved; an unlogged approval is indistinguishable from an accident.
## Related
- [[wiki/agent-systems/review-queues-wiki|Review Queues]] — the candidate pipeline
- [[wiki/concepts/editorial-policy|Editorial Policy]] — the standards layer
- [[wiki/concepts/consensus-wiki|Consensus]] — the decision principle
- [[wiki/concepts/merge-proposal|Merge Proposal]] — the change unit under review
- [[wiki/concepts/quality-team|Quality Team]] — the approver role
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — the agent-side analogue
