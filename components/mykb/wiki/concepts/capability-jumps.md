---
type: "concept"
title: "Capability Jumps"
description: "Discontinuous increases in model or agent capability"
tags: ["capability", "scaling", "forecasting", "emergence"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2001.08361", "https://en.wikipedia.org/wiki/Neural_scaling_law"]
---

# Capability Jumps

## Summary
Capability jumps are sudden, large increases in what an AI system can do, whether from a new training paradigm, a self-improvement loop, or a scale threshold. Whether jumps are real or artifacts of measurement drives both takeoff forecasts and the design of capability monitoring.

## Details
- **Sources** — new architectures (transformers), new objectives (RLHF), scaffolding (tool use, test-time compute), and self-improvement.
- **Measurement** — many apparent jumps vanish under continuous metrics; genuine jumps show up in raw capability distributions.
- **Safety role** — capability monitoring must catch jumps early because misalignment discovered after a jump is harder to correct.
- **Governance** — dangerous-capability evals and staged deployment are calibrated to jump likelihood.
- **RSIS3 link** — the knowledge loop tracks its own capability proxies (eval scores, task completion) for sudden drift.

## Related
- [[wiki/concepts/emergence-in-llms|Emergence in LLMs]] — metric artifact vs real jump
- [[wiki/concepts/capability-forecasting|Capability Forecasting]] — predicting jumps
- [[wiki/pulses/capability-probes|Capability Probes]] — instrumentation to detect them
- [[wiki/concepts/dangerous-capability-evals|Dangerous Capability Evals]] — governance response
- [[wiki/concepts/ai-timelines|AI Timelines]] — jump frequency feeds timelines
- [[wiki/concepts/calibration|Calibration]] — measurement honesty
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — existing graph anchor for recursive self-improvement
