---
type: "concept"
title: "Underfitting in LLMs"
description: "Models too weak to capture the training signal"
tags: ["underfitting", "llm", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Underfitting in LLMs

## Summary
Underfitting is a model failing to capture structure present in its training data, usually from insufficient scale or training. Where overfitting is the model doing too well on training data and too poorly elsewhere, underfitting is the model not learning the signal even where it is abundant — high error on training-like inputs, poor skill acquisition, and behavior that never reaches the ceiling its data would support.

## Details
- The causes are the classic ones: too little capacity (the model cannot represent the function), too little training (the optimizer has not converged), or a training setup that prevents learning (bad initialization, wrong learning rate, data issues). In each case the signature is the same: the model underperforms on the training distribution itself, which is the diagnostic difference from overfitting, where training performance is excellent. Underfitting shows as a training loss that plateaus above its feasible floor.
- It shows as high error on training-like inputs and poor skill acquisition. An underfit language model makes basic errors on tasks its training data clearly contains — poor syntax, wrong facts on common topics, inability to follow simple instructions — because the underlying patterns were never learned. The failure is not "the model forgot"; it never acquired the skill, so no amount of prompting or retrieval at inference time can recover it. This is why underfitting detection matters operationally: it tells you the fix is training-side (more data, more compute, better setup), not inference-side.
- In the era of big models it is rarer than overfitting but still common for niche skills. Frontier models trained on enormous corpora rarely underfit their dominant skills, but underfitting persists at the margins: rare languages, specialized domains, long-tail formats, and fine-tuned tasks where the base model's relevant knowledge was thin to begin with. The distribution of the problem shifted from "the whole model is underfit" to "this capability is underfit", which is why capability-specific evaluation matters more than global metrics.
- The relationship to overfitting is a genuine tradeoff along the same axis: under-parameterized models underfit, over-parameterized models risk overfitting, and the practical target is the middle where the model has enough capacity to learn the signal without so much that it memorizes noise. Scaling laws describe this balance — model size, data, and compute must grow together or one failure mode dominates.
- RSIS3 relevance: underfit graph clusters fail to represent their topics — if the wiki's topic embeddings or retrieval models lack the capacity or training signal to capture a cluster's structure, the cluster produces poor retrieval results, and the fix is acquisition and modeling, not more querying.

## Related
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — the opposite
- [[wiki/concepts/capability-jumps|Capability Jumps]] — the scaling cure
- [[wiki/agent-systems/skill-acquisition-loops|Skill Acquisition Loops]] — the improvement path
- [[wiki/concepts/temperature-scaling|Temperature Scaling]] — a calibration symptom
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]]
