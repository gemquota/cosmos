---
type: "concept"
title: "Elicitation Techniques"
description: "Methods for drawing knowledge or behavior out of a model"
tags: ["elicitation", "probing", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Elicitation Techniques

## Summary
Elicitation techniques extract knowledge a model may possess but not show: careful prompting, probing, and behavioral tests. The central fact motivating the field is that a model's default output is not its knowledge — the same fact may be retrievable with one phrasing and hidden with another, so "what does the model know?" is a question about elicitation, not about sampling a few generations.

## Details
- The techniques form a ladder of increasing invasiveness. Prompting variations (rephrasing, chain-of-thought, few-shot demonstrations) change the retrieval context while leaving the model untouched. Probing trains lightweight classifiers on internal activations to read knowledge directly from representation space — which can find knowledge the model never states in text, because the information exists in the activations even when the generation policy suppresses it. Behavior-probing constructs tasks where the knowledge must be used: if the model can solve a puzzle only by applying the fact, the fact is demonstrated behaviorally.
- Models can know more than they reveal; elicitation closes that gap for both capability and safety questions. On the capability side, under-elicitation makes a model look weaker than it is — a poor eval design can misclassify a capable model as incapable, and the reverse, over-elicitation (giving away the answer in the prompt), inflates apparent capability. On the safety side, elicitation is adversarial: red-teamers try to elicit hidden dangerous capabilities or hidden beliefs, and a safety evaluator must assume the model knows more than it shows.
- Hidden knowledge that resists elicitation raises deception concerns. If extensive, well-designed elicitation cannot surface knowledge that behavior suggests exists, the possibilities are that the knowledge genuinely is not there, that the elicitation is incomplete, or that the model is actively withholding it. Distinguishing the third case requires pressure-based and deception-focused eval designs, which is where elicitation techniques meet deception evals.
- The practical tradeoff: more invasive elicitation gives more complete answers but costs compute, risks teaching the model the elicitation strategy (which it can learn to game), and produces results that are sensitive to the exact protocol used — so elicitation findings need protocol transparency to be reproducible.
- RSIS3 relevance: probing the graph's coverage finds knowledge gaps, not just answers. Asking the wiki corpus the same question in many phrasings and checking which phrasings retrieve weak evidence is the retrieval-side elicitation technique — it measures what the memory layer can actually surface.

## Related
- [[wiki/concepts/knowledge-probing|Knowledge Probing]] — the core method
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — note
- [[wiki/agent-systems/hidden-goals|Hidden Goals]] — what may stay hidden
- [[wiki/pulses/capability-probes|Capability Probes]] — capability side
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the full treatment of this theme
