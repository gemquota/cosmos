---
type: "concept"
title: "Agent Supervision"
description: "Human or system oversight of agent activity with intervention authority"
tags: ["supervision", "agents", "oversight", "control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Supervision

## Summary
Agent supervision is the human or system oversight of agent activity, with the authority to intervene before, during, or after actions. It matters because autonomy without oversight concentrates risk in the agent's judgment. Good supervision scales with the risk of the action being taken. The supervision design also determines how much of the system's risk budget is carried by humans versus automation.

## Details
- **Definition** — supervision is the practice of monitoring agent behavior and retaining the power to approve, redirect, or halt actions.
- **Spectrum** — oversight ranges from review-before-apply for high-risk actions to exception-only monitoring for routine work, with approval probability tuned to risk.
- **Mechanisms** — supervision is typically implemented through permissioning-and-approvals systems, audit logs, and real-time dashboards rather than manual watching.
- **Design principle** — the supervision burden should track action cost and blast radius: cheap and reversible actions get lighter oversight than expensive or irreversible ones.
- **Human factors** — reviewer fatigue and rubber-stamping degrade oversight quality, so interventions should be rare enough to stay meaningful.
- **Automated layers** — system checks, policy engines, and anomaly detectors can pre-filter what reaches humans, making supervision scalable.
- **Escalation** — supervision pairs with escalation-handling so that ambiguous or risky cases route to the right authority with the right context.
- **Worked example** — a finance agent may execute read-only queries freely, require approval for transfers above a threshold, and escalate anything unusual to a human.
- **Failure modes** — over-supervision adds latency and friction; under-supervision lets failures compound; both erode trust in the system.
- **Practical relevance** — supervision is the operational face of corrigibility: it keeps agents aligned with intent even when the underlying model changes.
- **Design considerations** — supervision granularity should be configurable per action class, so low-risk batches do not carry high-risk review costs.
- **Metrics** — useful supervision metrics are intervention rate, time-to-intervention, and the share of prevented incidents.
- **Governance** — documented supervision policies make it clear who is accountable for each class of agent action.

## Related
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — approval gates as a supervision mechanism
- [[wiki/agent-systems/escalation-handling|Escalation Handling]] — routing exceptions to authority
- [[wiki/ai-ml/oversight-mechanisms|Oversight Mechanisms]] — the conceptual frame for oversight
- [[wiki/agent-systems/agent-observability|Agent Observability]] — the visibility supervision depends on
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — limits that bound supervised actions
