---
type: "concept"
title: "Meta-Cognition in Agents"
description: "Agents that monitor and regulate their own reasoning processes"
tags: ["metacognition", "agents", "reflection", "self-monitoring"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Metacognition", "https://arxiv.org/abs/2303.11366"]
---

# Meta-Cognition in Agents

## Summary
Meta-cognition in agents is the ability to monitor, evaluate, and steer one's own cognitive processes — knowing when to double-check, when to stop, or when a plan is going wrong. It converts raw reasoning skill into reliable task performance.

## Details
- **Components** — monitoring (am I stuck?), control (should I switch strategy?), and knowledge of strategies.
- **LLM instantiations** — self-consistency checks, uncertainty-based stopping, and reflection agents.
- **Benefits** — better calibration, fewer cascading errors, and more efficient use of test-time compute.
- **Risks** — meta-cognitive monitoring is itself confabulated; self-claims need external checks.
- **RSIS3 parallel** — the pulse protocol's crisis monitor and reflection phases are meta-cognitive layers above the base agent loop.

## Related
- [[wiki/agent-systems/self-reflection-loops|Self-Reflection Loops]] — monitoring in action
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the assessment half
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — first-person access question
- [[wiki/agent-systems/crisis-monitoring|Crisis Monitoring]] — RSIS3's meta layer
- [[wiki/agent-systems/test-time-compute|Test-Time Compute]] — resource meta-cognition spends
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
