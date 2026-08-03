---
type: "concept"
title: "Logit Lens"
description: "A technique for decoding a model's predictions from intermediate layers, revealing how computation unfolds"
tags: ["logit-lens", "interpretability", "transformers"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Logit Lens

## Summary
The logit lens projects each layer's hidden state through the model's unembedding to read what the model would predict right now. It turns layer stacks into readable traces of how predictions develop, exposing early commitment, late correction, and where knowledge gets resolved.

## Details
The technique works because decoder-only transformers maintain a residual stream that layers add to, and the unembedding matrix maps that stream to vocabulary probabilities at every point. By applying the unembedding to the hidden state after each layer, you get a prediction trace without running the full forward pass to the end. This works reasonably well because the residual stream keeps a roughly interpretable linear relationship to the output throughout the stack.

The value is diagnostic. Traces reveal when the model commits to a wrong token early and then corrects it, when a fact is only resolved in the final layers, and where a particular reasoning step actually happens. A model that keeps a plausible wrong prediction for many layers before flipping is behaving differently from one that flips early, and that difference can localize a failure to a region of the network. It is cheap, requires no training, and works on any decoder-only checkpoint, which makes it the staple first look in interpretability work.

The caveats are structural. The lens is mostly valid for decoder-only transformers because their residual stream and unembedding align; encoder and encoder-decoder models, and models with heavy normalization or parallel layers, produce noisier projections. The per-layer predictions are a proxy, not the real computation: a layer can "predict" the right token while contributing nothing causal to it. Over-reading single-layer traces is the classic beginner mistake, so findings should be confirmed with interventions such as activation patching.

RSIS3 relevance: tracing RSIS3's reasoning across layers could localize prompt-induced confusion, and for mykb, logit-lens artifacts should be stored with the eval failures they explain so the diagnosis is reproducible.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The umbrella field
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — The rigorous cousin
- [[wiki/ai-ml/residual-connections|Residual Connections]] — The residual stream logit lens reads
- [[wiki/ai-ml/probing|Probing]] — Related activation-reading method
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Complementary feature extraction
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Layer traces help diagnose eval failures
