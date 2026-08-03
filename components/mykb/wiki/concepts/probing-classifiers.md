---
type: "concept"
title: "Probing Classifiers"
description: "Small models trained on a model's internal activations to test whether features are linearly accessible"
tags: ["probing", "classifiers", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Probing Classifiers

## Summary
Probing classifiers are small models trained on a model's internal activations to test whether features are linearly accessible. The technique reads the model's representations: freeze the network, cache activations at a layer, train a simple classifier to predict a property (part-of-speech, toxicity, factual content) from those activations, and interpret the classifier's success as evidence about what the layer represents.

## Details
- The method: for each layer of interest, collect activations over a labeled dataset, train a lightweight classifier (a linear probe or a small MLP) on the activations, and measure held-out accuracy. High accuracy at a layer means the property is decodable from that layer's representation; the accuracy profile across layers reveals where the network builds and transforms the feature. The probe is deliberately capacity-limited — a linear probe especially — so that success reflects representation quality, not classifier cleverness.
- Good probe performance suggests the feature is encoded; the technique is the workhorse of representational analysis. Probing produced much of the evidence that transformer representations are organized: syntactic properties emerge in middle layers, semantic content later, and different tasks use different representational routes. It is also the standard tool for detecting what a model "knows" (knowledge probing) and for monitoring whether safety-relevant properties are linearly readable from activations.
- The central confound: probes can mistake shallow correlations for deep knowledge; control tasks are essential. A probe can succeed by reading input artifacts that leak through the residual stream, by exploiting positional information, or by latching onto a correlated but superficial feature — none of which means the model "knows" the property in any deep sense. The standard controls: train probes on random labels (accuracy should collapse), probe scrambled representations, and include control properties that should not be decodable. Without controls, probe results are unfalsifiable — a probe always finds something, because high-capacity readouts can decode almost anything from almost anything.
- The second limitation: probing shows presence, not participation. A feature that is decodable may be causally irrelevant to the model's behavior — it exists in the activations but the model never uses it — which is why probe findings are hypotheses for causal intervention (activation patching) to verify.
- RSIS3 relevance: probe-style analysis informs how the graph's embeddings are inspected — training linear readouts on wiki node embeddings to check whether the topic structure the system wants to retrieve on is actually present in the embeddings, with the same control discipline.

## Related
- [[wiki/concepts/linear-probes|Linear Probes]] — the simplest probe
- [[wiki/concepts/activation-analysis|Activation Analysis]] — the data being probed
- [[wiki/concepts/polysemanticity|Polysemanticity]] — why probes mislead
- [[wiki/concepts/feature-double-counting|Feature Double-Counting]] — probe confound
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/probing|Probing]]
