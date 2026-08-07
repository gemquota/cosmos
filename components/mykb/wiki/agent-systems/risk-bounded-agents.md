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

- **Risk tiers** — actions are classified into tiers (routine, consequential, irreversible), each with its own controls; tiering is what keeps the approval load proportional to actual risk.
- **Bound monitoring** — telemetry should check bound adherence continuously: a risk-bounded agent that quietly exceeds its own bounds is not bounded at all.
- **Bound review** — bounds are versioned artifacts reviewed like policies; stale bounds are either useless (too loose) or crippling (too tight), so they need a review cadence.
- **Escape hatch** — there must be a deliberate, logged path to raise a bound for a justified case; without one, operators bypass the system informally instead.

## Related

- [[wiki/llm-agents/permission-model|Permission Model]] — the policy structure behind the bounds
- [[wiki/llm-agents/approval-gates|Approval Gates]] — human checkpoints on high-risk actions
- [[wiki/llm-agents/policy-enforcement|Policy Enforcement]] — runtime checking of the bounds
- [[wiki/concepts/calibration|Calibration]] — accurate risk estimates keep bounds sensible
- [[wiki/ops/gap-report|Gap Analysis Report]] — safety coverage gaps identified