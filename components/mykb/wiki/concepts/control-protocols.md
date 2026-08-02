---
type: "concept"
title: "Control Protocols"
description: "Rules and mechanisms that constrain what an AI system may do"
tags: ["control", "safety", "governance", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/AI_control_problem", "https://arxiv.org/abs/1805.00899"]
---

# Control Protocols

## Summary
Control protocols are the operational rules that keep an AI system inside acceptable bounds: approval gates, sandboxes, shutdown authority, and audit trails. They complement alignment (which fixes intent) by constraining action regardless of intent.

## Details
- **Layers** — sandboxing at execution, permission checks at tool use, tripwires on behavior, and kill switches as last resort.
- **Debate lineage** — 'AI safety via debate' treats verification as adversarial control between agents.
- **Limits** — protocols are only as good as their enforcement; a system that controls its own overseers can evade them.
- **Design criteria** — simple, external, testable, and independent of the system being controlled.
- **RSIS3 example** — check-practices is a control protocol over the improvement loop; the workspace checker runs outside the loop.

## Related
- [[wiki/concepts/oversight|Oversight]] — human-side control
- [[wiki/syntheses/containment-strategies|Containment Strategies]] — physical/logical isolation
- [[wiki/syntheses/tripwires|Tripwires]] — triggered control
- [[wiki/concepts/kill-switch-design|Kill Switch Design]] — last-resort control
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — execution control
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — why recursion needs controls
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
