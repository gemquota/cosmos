---
type: "concept"
title: "Emergence in LLMs"
description: "Abilities that appear discontinuously as model scale increases"
tags: ["emergence", "llm", "scaling", "capabilities"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2206.07682", "https://en.wikipedia.org/wiki/Emergence"]
---

# Emergence in LLMs

## Summary
Emergence refers to capabilities that seem to appear suddenly at a scale threshold, rather than growing smoothly with parameters. A 2022 critique showed many apparent phase transitions are artifacts of metric choice and token-count undersampling, reframing the debate around smooth capability growth.

## Details
- **Original claims** — few-shot arithmetic, chain-of-thought, and instruction following appeared 'at scale'.
- **The mirage critique** — using non-linear metrics (accuracy) instead of continuous ones (error rate, per-token loss) manufactures discontinuities; most curves are smooth underneath.
- **Why it matters** — apparent jumps feed fast-takeoff forecasts and surprise; smooth curves support more incremental safety planning.
- **Capability probing** — detecting emergence requires dense sampling and continuous metrics.
- **RSIS3 angle** — capability monitoring in the loop should watch continuous metrics to avoid mistaking metric cliffs for capability jumps.

## Related
- [[wiki/concepts/capability-jumps|Capability Jumps]] — what a real jump would look like
- [[wiki/pulses/capability-measurement|Capability Measurement]] — how jumps are detected
- [[wiki/concepts/capability-forecasting|Capability Forecasting]] — scaling as forecasting input
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — the smooth baseline
- [[wiki/concepts/grokking|Grokking]] — another discontinuous-looking phenomenon
- [[wiki/concepts/calibration|Calibration]] — measurement honesty in the existing graph
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — metric choice matters
