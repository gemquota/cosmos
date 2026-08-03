---
type: "concept"
title: "Activation Patching"
description: "Replacing activations from one input with another to test causal roles"
tags: ["patching", "activations", "causality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Activation Patching

## Summary
Activation patching runs a model on input A, then replays activations from input B at chosen layers to see what changes. It is the workhorse causal-intervention technique in mechanistic interpretability: by swapping a single component's output and observing the effect on the final prediction, you can attribute information flow to specific heads, neurons, or layers.

## Details
- The standard procedure pairs a clean input (the behavior you want to explain, such as "The capital of France is Paris") with a corrupt input that differs only in the feature of interest (e.g., "The capital of England is Paris"). You cache activations from both runs, then rerun the clean input while overwriting the activations at one or more layers with the corrupt run's values. If the prediction flips, that component carried the decisive information.
- Variants trade precision against compute. Activation patching is exact but expensive because it needs a full forward pass per patched location; zero- and mean-ablation replace a component's output with zeros or a dataset average, giving cheaper, noisier estimates of importance. Attention patching and head patching narrow the intervention to a single attention head, and path patching follows the influence from a source node through an intermediate node to the output, which is what makes end-to-end circuit discovery feasible.
- Patching answers attribution questions, not mechanism questions: it shows where information lives, not how it is transformed. Results are also path-dependent — a component that looks unimportant in isolation can matter when another component is ablated first — so claims should be stated in terms of the specific intervention set used.
- Failure modes include negative interference (patching corrupt values onto a clean run can break unrelated paths and produce misleading flips), layer-boundary sensitivity, and the fact that patched states are out-of-distribution relative to anything the model saw in training, so the model may behave in ways that reveal its architecture rather than its computation.
- RSIS3 relevance: patching-style A/B tests on graph retrieval isolate which links drive answers. If a synthesis page changes which evidence surfaces, patch the retrieval embeddings or link weights to find which edges were causally responsible.

## Related
- [[wiki/concepts/causal-interventions-ai|Causal Interventions in AI]] — the family
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — what it builds
- [[wiki/concepts/causal-interventions-ai|causal-interventions-ai]] — related tool
- [[wiki/concepts/transformer-lens|TransformerLens]] — tooling support
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/activation-engineering|Activation Engineering]]
