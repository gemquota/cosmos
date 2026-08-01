---
type: "concept"
title: "Emergent Abilities"
description: "Capabilities that appear sharply once a model crosses a scale or training threshold, not gradually"
tags: ["emergent-abilities", "scaling", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Emergent Abilities

## Summary
Emergent abilities are skills that are near-absent at small scale and jump to competence at larger scale — from arithmetic to multi-step reasoning. They make capability prediction hard and are a subject of active debate.

## Details
- Documented in 'Emergent Abilities of Large Language Models' (2022); later work argued some emergences are an artifact of metric choice.
- Examples: few-shot arithmetic, instruction following, and some reasoning tasks.
- Relevance to engineering: assume capabilities change between model versions, so regression-test everything.
- RSIS3 relevance: L3 strategy evolution must re-evaluate assumptions whenever the underlying model changes.

## Related
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — A capability that emerges with scale
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — The quantitative frame for emergence
- [[wiki/ai-ml/gpt-4|GPT-4]] — A model family exhibiting broad emergent behaviour
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — Eval after every model swap
- [[wiki/prompt-engineering/multi-step-reasoning|Multi-Step Reasoning]] — A reasoning ability tied to scale
