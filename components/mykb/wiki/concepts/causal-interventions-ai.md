---
type: "concept"
title: "Causal Interventions in AI"
description: "Perturbing internals to test causal roles"
tags: ["causal", "interventions", "interpretability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Causal Interventions in AI

## Summary
Causal interventions edit a model's internal state (activations, weights, tokens) and observe output changes, testing whether a component is causally load-bearing. Where probes and correlational analyses can only show that information is present somewhere, interventions show whether a component actually matters: change it and the behavior changes, or it does not.

## Details
- The logic follows experimental design: hold everything fixed, manipulate one variable (a single activation, attention head, or weight), and measure the effect on the outcome. If patching out a component's contribution leaves the prediction unchanged, that component was not load-bearing for this input; if the prediction flips, the component carried decisive information. The contrast between "present" and "causally load-bearing" is the whole point — a circuit can contain information that is never used on a given input.
- Activation patching is the standard intervention tool. The model runs on a clean and a corrupted input, activations are cached from both, and the clean run is replayed with selected layers overwritten by the corrupted values. Variants — zero-ablation, mean-ablation, path patching, and logit patching — trade fidelity for compute and target different questions about where and how information flows.
- Causal claims are stronger than correlational probe claims, which is why safety analysis prefers them. A linear probe that classifies "deceptive intent" from an activation proves the information exists; an intervention that changes deception-relevant behavior proves the information is used. For safety verdicts that will gate deployment, the stronger evidence class matters, though interventions are also more expensive and more brittle to implement correctly.
- Limitations: interventions create out-of-distribution states (the model never saw those exact activations during training), so results can reflect the model's reaction to an impossible input rather than its normal computation; and single-component interventions miss synergistic effects where importance only appears when multiple components change together.
- RSIS3 relevance: interventions on graph state (deleting a node) test its causal role in retrieval. If removing a wiki page from the retrieval graph changes an answer, that page is load-bearing for that query — a cheap, concrete version of the same causal discipline applied to the knowledge loop.

## Related
- [[wiki/concepts/activation-patching|Activation Patching]] — the main method
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — what interventions verify
- [[wiki/concepts/activation-patching|activation-patching]] — the framing
- [[wiki/agent-systems/introspection-ai|Introspection in AI]]
- [[wiki/ai-ml/activation-engineering|Activation Engineering]]
