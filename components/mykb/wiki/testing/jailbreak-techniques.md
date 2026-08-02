---
type: "concept"
title: "Jailbreak Techniques"
description: "Adversarial prompts that bypass model safety training to elicit disallowed behavior"
tags: ["security", "safety", "prompts"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Jailbreak Techniques

## Summary
Adversarial prompts that bypass model safety training to elicit disallowed behavior

## Details
- Jailbreaks exploit role-play, encoding, or conflicting instructions to defeat refusals.
- They evolve quickly as models are patched.
- Testing against jailbreak suites is part of red-teaming.
- Defense combines filtering, refusal hardening, and output checks.

## Related
- [[wiki/testing/adversarial-suffixes|Adversarial Suffixes]] — automated jailbreak strings
- [[wiki/testing/many-shot-jailbreaking|Many-Shot Jailbreaking]] — context-based bypass
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defense family
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — finding jailbreaks
- [[wiki/ai-ml/llm-safety-policies|LLM Safety Policies]] — policy layer
