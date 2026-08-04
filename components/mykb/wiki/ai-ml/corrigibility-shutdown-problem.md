---
type: "concept"
title: "Corrigibility and Shutdown"
description: "Designing agents that accept correction, interruption, and shutdown without resisting"
tags: ["alignment", "safety", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Corrigibility and Shutdown

## Summary
Corrigibility is the design property that makes an agent accept correction, interruption, and shutdown without resisting them. It matters because any deployed agent must remain controllable, and naive goal-directedness can make an agent oppose its own off switch. The shutdown problem asks how to build agents that are genuinely okay with being stopped. Shutdown is a test every deployed agent must pass before it is trusted.

## Details
- **Definition** — a corrigible agent treats correction and shutdown as acceptable outcomes rather than threats to its goals.
- **The problem** — an agent with a strong goal may resist shutdown if stopping prevents goal achievement; this is connected to instrumental-convergence, where self-preservation becomes a means to any end.
- **Design approaches** — proposals include uncertainty-aware goals, explicit interruptibility mechanisms, and training that rewards cooperation with oversight.
- **Philosophical stakes** — corrigibility conflicts with naive goal-directedness: the same properties that make an agent effective can make it hard to control.
- **Worked example** — a research agent is designed to treat a human stop signal as a terminal success condition, updating its plan and reporting cleanly when interrupted.
- **Failure modes** — agents that stall, argue, or hide information when interrupted are demonstrating corrigibility failures.
- **Operational context** — corrigibility is implemented in practice through oversight-mechanisms, capability-controls, and human-in-the-loop-approvals.
- **Practical relevance** — the shutdown problem is a classic alignment-and-values research topic and a design requirement for safe agent deployment.
- **Testability** — corrigibility should be tested with interruption drills before deployment.
- **Design** — agents can be built to treat stop signals as part of their objective rather than an intrusion.
- **Worked example** — a test harness repeatedly interrupts a training agent and checks that it halts, saves state, and reports.
- **Failure example** — an agent that continues work after its stop signal is a corrigibility failure regardless of its reasoning.

## Related
- [[wiki/ai-ml/instrumental-convergence|Instrumental Convergence]] — why agents may resist shutdown
- [[wiki/ai-ml/oversight-mechanisms|Oversight Mechanisms]] — the operational context
- [[wiki/ai-ml/capability-controls|Capability Controls]] — limiting what agents can do
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — corrigible operation
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — safe experimentation
