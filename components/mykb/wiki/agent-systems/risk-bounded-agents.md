---
type: "concept"
title: "Risk-Bounded Agents"
description: "Agents whose behavior is constrained by explicit safety limits"
tags: ["safety", "risk", "constraints", "agents", "oversight"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1606.06565"]
---

# Risk-Bounded Agents

## Summary
A risk-bounded agent is one whose freedom to act is deliberately limited by safety policies: which tools it may call, what files it may touch, when it must ask a human, and how fast it may escalate. It matters because capability without bounds is how small mistakes become large ones. Concrete Problems in AI Safety frames this as a research agenda, and RSIS3 operationalizes it with permission models, approval gates, and a crisis monitor.

## Details
- **Bounds are explicit**: policies enumerate allowed actions, resources, and escalation triggers.
- **Safe exploration**: agents may try new strategies only within the sandbox and approved tool set.
- **Oversight**: humans review high-impact actions; the rest run under automatic guardrails.
- **Specification risk**: badly written bounds are either useless or crippling, so policies are versioned and reviewed.
- RSIS3 layers risk bounds at every loop: L1 tools are gated, L2 changes must pass tests, L3 strategy shifts are logged and reversible.
- Worked example: a deployment agent may only touch staging, never production, without an explicit approval gate.

## Related

- [[wiki/llm-agents/permission-model|Permission Model]] — the policy structure behind the bounds
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints on high-risk actions
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — runtime checking of the bounds
- [[wiki/concepts/calibration|Calibration]] — accurate risk estimates keep bounds sensible
- [[raw/archive/session-artifacts-2026-07/topics/security|security — the threat model bounds respond to
- [[wiki/ops/gap-report|Gap Analysis Report]] — safety coverage gaps identified