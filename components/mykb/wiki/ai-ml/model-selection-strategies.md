---
type: "concept"
title: "Model Selection Strategies"
description: "Choosing which model to use for which task under cost, latency, and quality constraints"
tags: ["model-selection", "routing", "cost", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.anthropic.com/en/docs/about-claude/models/overview", "https://ai.google.dev/gemini-api/docs/models"]
---

# Model Selection Strategies

## Summary
Model selection matches tasks to models: capability tier, cost per token, latency, and data-sensitivity all factor in. A portfolio of models outperforms one model for everything. Selection is both static (design-time) and dynamic (runtime routing).

## Details
- **Dimensions** — capability, price, speed, context length, modality, and data residency; benchmarks only approximate real-task quality.
- **Strategies** — capability-tiering (small/medium/frontier), task-specific routing, fallback chains, and self-adaptive selection from eval scores.
- **Measurement** — internal evals on your own tasks beat leaderboard scores for selection decisions.
- **Worked example** — classification runs on a small local model; extraction on a mid-tier API model; adversarial planning on a frontier reasoning model.
- **Governance** — allowed-model policies, per-model quotas, and audit trails belong in the gateway.
- **mykb relevance** — model family comparisons and routing rules in mykb support RSIS3's selection of models per task type.
- Worked example: a support pipeline routes simple FAQs to a small fast model, medium cases to a mid-tier model, and legal-grade answers to a frontier model with a verifier, cutting monthly spend while holding quality.

## Related
- [[wiki/agent-systems/model-routing-rules|Model Routing Rules]] — dynamic selection
- [[wiki/ai-ml/model-family-comparisons|Model Family Comparisons]] — comparing families
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — cost in selection
- [[wiki/ai-ml/llm-leaderboards|LLM Leaderboards]] — benchmark-based comparison
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — fallback selection
- [[wiki/ai-ml/open-weights-models|Open-Weight Models]] — self-hosted options
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — capability scaling context
- [[wiki/concepts/calibration|Calibration]] — calibration anchor in the KB
