---
type: "concept"
title: "Emergent Abilities"
description: "Capabilities that appear sharply once a model crosses a scale or training threshold, not gradually"
tags: ["emergent-abilities", "scaling", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Emergent Abilities

## Summary
Emergent abilities are skills that are near-absent at small scale and jump to competence at larger scale — from arithmetic to multi-step reasoning. They make capability prediction hard and are a subject of active debate: later work argued some emergences are artifacts of metric choice.

## Details
- Evidence: the Emergent Abilities of Large Language Models paper (2022) documented abilities that appear abruptly past scale thresholds; subsequent analyses showed that some apparent discontinuities vanish with better metrics — performance can be smooth on the right scale — so emergence is partly measurement, partly real.
- Examples: few-shot arithmetic, instruction following, and some reasoning tasks appear sharply at scale; capabilities differ across model versions, so behavior observed at one scale or version does not transfer.
- Concrete example: a small model fails a multi-step reasoning eval at near-random accuracy; a larger version of the same architecture passes it; switching an application to a new model version changes which prompts work — regression tests catch the shift.
- Failure modes: assuming capability curves are smooth and extrapolating from small models; trusting benchmarks from other scales or versions; treating emergent abilities as stable once present (they shift with training changes); designing systems that depend on unverified abilities.
- Tradeoffs: emergence means capability cannot be predicted from scale alone — the engineering response is empirical evaluation at the actual model; the alternative, assuming continuity, leads to surprises; the mature pattern is eval-driven: re-test every capability after any model change.
- Operational notes: keep an eval suite that covers the capabilities the system depends on, and run it on every model swap.
- RSIS3 relevance: L3 strategy evolution must re-evaluate assumptions whenever the underlying model changes — emergence makes each swap a potential behavior discontinuity.

## Related
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — A capability that emerges with scale
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — The quantitative frame for emergence
- [[wiki/ai-ml/gpt-4|GPT-4]] — A model family exhibiting broad emergent behaviour
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — Eval after every model swap
- [[wiki/prompt-engineering/multi-step-reasoning|Multi-Step Reasoning]] — A reasoning ability tied to scale
