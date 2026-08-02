---
type: "concept"
title: "Adversarial Suffixes"
description: "Automatically optimized token strings appended to prompts to trigger harmful behavior"
tags: ["security", "jailbreak", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Adversarial Suffixes

## Summary
Automatically optimized token strings appended to prompts to trigger harmful behavior

## Details
- Gradient-based search finds suffixes that maximize attack success.
- Suffixes transfer across models and often look like gibberish.
- Detection filters and perplexity checks catch many but not all.
- A research benchmark for robustness in red-teaming-llms.

## Related
- [[wiki/testing/jailbreak-techniques|Jailbreak Techniques]] — manual counterpart
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — testing discipline
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defensive research
- [[wiki/testing/adversarial-ml-threats|Adversarial ML Threats]] — broader threat model
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — runtime mitigation
