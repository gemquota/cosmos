---
type: "entity"
title: "DeepSeek"
description: "DeepSeek's open-weight LLM family, notable for competitive frontier-level performance and efficiency innovations"
tags: ["deepseek", "llm", "open-weights", "models"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# DeepSeek

## Summary
DeepSeek publishes high-performing open-weight models with innovations in MoE architecture, long contexts, and training efficiency. Its releases regularly reset expectations for open-model capability, and its technical reports are unusually detailed about what actually works at scale.

## Details
DeepSeek models span the V2/V3 dense-and-MoE generation and the R1 reasoning line, mixing sparse expert routing with strong benchmark results. The architectural contribution is significant: DeepSeek's mixture-of-experts designs activate only a fraction of parameters per token, cutting inference cost dramatically while keeping most of the capacity of a much larger dense model. Attention innovations (multi-head latent attention and related variants) shrink the KV-cache footprint, which is what makes long-context serving practical on commodity hardware.

The R1 line demonstrated large-scale reinforcement-learning-driven reasoning at open weights: a base model is trained to produce long chain-of-thought traces, then refined with RL on verifiable rewards such as code execution results or math answer checks. The observable result is a "deep-thinking" mode where the model spends many tokens deliberating before answering. The operational trade-off is real — reasoning tokens multiply latency and cost per request, so production deployments need to gate or budget thinking time rather than enabling it unconditionally.

Because the weights and training recipes are public, DeepSeek is a rich source for replication and study: teams can inspect the MoE configuration, reproduce training stages, and measure properties that closed models hide, such as true parameter counts and expert routing behaviour. Failure modes mirror other open models — weaker instruction-following than the best closed frontier models in some generations, and quantization-sensitive MoE layers that need careful calibration.

RSIS3 relevance: DeepSeek-class models offer frontier-adjacent capability at self-hostable cost, which matters for L1 loops where per-token spend compounds, and for experiments where mykb must inspect or reproduce the exact model behind a result.

## Related
- [[wiki/ai-ml/quantisation|Quantisation]] — Deployment path for large open weights
- [[wiki/ml-frameworks/vllm|vLLM]] — Serving MoE models efficiently
- [[wiki/ai-ml/ppo|PPO]] — RL methods behind reasoning models
- [[wiki/prompt-engineering/multi-step-reasoning|Multi-Step Reasoning]] — A flagship DeepSeek behaviour
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Where its claims are tested
