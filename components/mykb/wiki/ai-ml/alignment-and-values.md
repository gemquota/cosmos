---
type: "concept"
title: "Alignment and Values"
description: "Making model behavior track human intent and values"
tags: ["alignment", "values", "safety", "ai"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.11610", "https://arxiv.org/abs/2212.03551"]
---

# Alignment and Values

## Summary
Alignment is the problem of making an AI system's behavior reliably track human intent and values — helpful, honest, and safe. It spans training (RLHF, constitutional AI), runtime guardrails, and evaluation. Alignment is not a solved property but a direction of work with continuous measurement.

## Details
- **Outer alignment** — the training objective and data must encode the values we actually want, not a proxy that happens to correlate.
- **Inner alignment** — the trained system must actually pursue that objective, without mesa-optimization or deceptive instrumental behavior.
- **Techniques** — RLHF with robust reward models, constitutional principles, red teaming, and capability-control evaluations.
- **Measurement** — safety evals, bias audits, and refusal-behavior tests proxy for alignment; proxies themselves can fail.
- **Worked example** — a chatbot policy prioritizes helpfulness except where it conflicts with harm; preference data encodes those tradeoffs and red teaming probes the boundary.
- **mykb relevance** — alignment and values concepts (constitutional AI, reward hacking, alignment) are existing mykb topics RSIS3 references in its self-improvement policies.

## Related
- [[wiki/ai-ml/constitutional-ai|Constitutional AI]] — principles-based alignment
- [[wiki/ai-ml/outer-alignment|Outer Alignment]] — objective-level alignment
- [[wiki/ai-ml/inner-misalignment|Inner Misalignment]] — model-level misalignment
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — optimization failures
- [[wiki/ai-ml/outer-alignment|Outer Alignment]] — objective-level alignment
- [[wiki/testing/ai-safety-evals|AI Safety Evals]] — measuring alignment
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — probing for misalignment
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
