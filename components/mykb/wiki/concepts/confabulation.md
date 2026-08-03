---
type: "concept"
title: "Confabulation"
description: "Producing plausible but fabricated explanations without intent to deceive"
tags: ["confabulation", "hallucination", "memory", "reasoning"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Confabulation

## Summary
Confabulation is when an agent generates a coherent, confident account that does not match reality — often filling memory gaps after the fact. It differs from deliberate lying because the agent believes the account: the story is constructed to be plausible, not to deceive. In LLM agents it overlaps with hallucination and is a key evaluation target, because a system that confabulates about its own history corrupts its learning loop.

## Details
- The cognitive-science root is human memory: people routinely fill gaps in episodic recall with plausible reconstructions and later cannot distinguish the reconstruction from the memory. The same failure appears in LLM agents after context loss or failed retrieval — the model generates a smooth, confident narrative where the actual record is missing. Because generation is trained to maximize plausibility, not fidelity, the default behavior when recall fails is to invent rather than to say "I don't know".
- Why it is dangerous in agent systems: fabricated "what happened" corrupts learning. If a self-improving system consolidates a synthesis from a confabulated session summary, the error is baked into its memory and propagates to every future decision that retrieves that synthesis. The problem compounds — later loops reason confidently from false premises, and confidence makes the corruption hard to detect in review.
- Mitigation: grounding claims in retrieved evidence and traceable records. Require every synthesis to cite the sources it generalizes from; keep raw session logs immutable so a later "summary" can be checked against the ground truth; and add a verification step that rejects claims lacking provenance. Calibration monitoring helps too, because confabulated content tends to be produced with unjustified confidence.
- The hard open question is distinguishing confabulated memory from creative synthesis. A legitimate synthesis is exactly a reconstruction that goes beyond the raw record — the difference is that it is a disciplined generalization, transparent about its inference, rather than an unmarked invention presented as fact.
- RSIS3 relevance: the consolidation pipeline is the front line. Session capture, synthesis writing, and log entries are all confabulation-prone; the practice of cross-linking sources and regenerating snapshots is what keeps reconstruction honest.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — reflection can catch confabulation
- [[wiki/llm-agents/hallucination-mitigation|Hallucination Mitigation]] — the mitigation toolkit
- [[wiki/concepts/calibration|Calibration]] — confabulated claims are overconfident
- [[wiki/concepts/episodic-memory|Episodic Memory]] — the memory being confabulated
- [[wiki/concepts/metacognition|Metacognition]] — monitoring for invented content
