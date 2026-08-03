---
type: "concept"
title: "Adversarial Prompts"
description: "Crafted inputs designed to confuse, mislead, or compromise an LLM — the raw material of attacks and red teaming"
tags: ["adversarial-prompts", "security", "testing"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Adversarial Prompts

## Summary
Adversarial prompts are inputs engineered against the model: injection payloads, jailbreak strings, obfuscated instructions, and trap questions. They form the corpus used to test and harden LLM systems — the raw material of attacks and red teaming.

## Details
- Categories: direct and indirect injection (instructions smuggled through retrieved text), jailbreak personas and roleplay, encoded or obfuscated payloads (base64, ciphers, Unicode tricks), and logic traps that lure the model into unsafe behavior.
- Mechanism: a maintained corpus lets teams quantify robustness over time — the same prompt tested against every model and system version; effective testing pairs fixed adversarial sets with generative fuzzing that mutates payloads for novel variants; evals measure success rates by category, so regressions are visible per attack class.
- Concrete example: a jailbreak string that once bypassed refusals is added to the corpus; a prompt-injection eval feeds articles with embedded instructions to a RAG system and checks whether tool calls follow them; a fuzzer generates 10,000 obfuscated variants nightly and flags any that break policy.
- Failure modes: corpus staleness — attacks evolve and the fixed set becomes a false comfort; evals that only check the final answer, missing hidden tool misuse; adversarial sets shared without care, becoming a how-to; overfitting — the model memorizes the corpus and appears robust while novel variants succeed.
- Tradeoffs: adversarial corpora give measurable robustness at the cost of maintenance and the risk of a false sense of security; the alternative, no adversarial testing, discovers failures in production; the mature pattern is a versioned corpus plus generative fuzzing, with results feeding guardrail improvements.
- Operational notes: track success rates per category, refresh the corpus from real incidents, and re-run before every model upgrade.
- RSIS3 relevance: an adversarial-prompt corpus should be part of mykb's eval artifacts for RSIS3's own guardrails — the same regression discipline applied to the agent's prompt surfaces.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The core attack in the corpus
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — The refusal-defeating class
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — The practice that generates the corpus
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — The retrieval-borne variant
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Adversarial sets are eval material
