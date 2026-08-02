---
type: "concept"
title: "Reasoning Models"
description: "Models trained to spend tokens on extended step-by-step reasoning"
tags: ["reasoning", "models", "inference-time", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/reasoning", "https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking"]
---

# Reasoning Models

## Summary
Reasoning models are trained (or prompted) to produce long, explicit reasoning before answers, trading more compute for better accuracy on hard problems. They represent a shift from scale-as-training to scale-at-inference. Their reasoning traces enable verification, but also raise cost and sometimes confabulation risks.

## Details
- **Training** — RL on verifiable tasks teaches long reasoning chains; some models show self-correction mid-chain.
- **Inference behavior** — they emit structured thinking (e.g. "let me verify") before the final answer; providers expose or hide traces depending on policy.
- **Cost** — reasoning tokens multiply per-request cost; routing to reasoning models only for hard tasks is the standard optimization.
- **Worked example** — a coding agent routes a tricky concurrency bug to a reasoning model, which explores and rejects two approaches before landing on a third.
- **Evaluation** — reasoning models shine on math, code, and planning benchmarks; on simple tasks they may be slower without being better.
- **mykb relevance** — extended thinking is documented in mykb; model routing rules decide when RSIS3 uses reasoning models.

## Related
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — routing to reasoning models
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — reasoning cost economics
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — long reasoning uses the KV cache
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — confidence in long chains
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — verifying reasoning outputs
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — related concept in this cluster
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — capability scaling context
