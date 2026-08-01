---
type: "concept"
title: "Adversarial Prompts"
description: "Crafted inputs designed to confuse, mislead, or compromise an LLM — the raw material of attacks and red teaming"
tags: ["adversarial-prompts", "security", "testing"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Adversarial Prompts

## Summary
Adversarial prompts are inputs engineered against the model: injection payloads, jailbreak strings, obfuscated instructions, and trap questions. They form the corpus used to test and harden LLM systems.

## Details
- Categories: direct/indirect injection, jailbreak personas, encoded payloads, and logic traps.
- Maintained corpora let teams quantify robustness over time and prevent regression after prompt or model changes.
- Effective testing pairs fixed adversarial sets with generative fuzzing for novel variants.
- RSIS3 relevance: an adversarial-prompt corpus should be part of mykb's eval artifacts for RSIS3's own guardrails.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The core attack in the corpus
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — The refusal-defeating class
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — The practice that generates the corpus
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — The retrieval-borne variant
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Adversarial sets are eval material
