---
type: "concept"
title: "Prompt Recovery Attacks"
description: "Attempts to extract hidden system prompts from deployed models"
tags: ["prompt-recovery", "security", "prompts", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prompt Recovery Attacks

## Summary
Attempts to extract hidden system prompts from deployed models

## Details
- Attackers elicit system instructions via social engineering or probing.
- Recovered prompts enable targeted attacks and cloning.
- Defenses: prompt hardening and prompt-leakage-detection.
- Related to model-stealing-attacks.

## Related
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — detection side
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defense family
- [[wiki/testing/model-stealing-attacks|Model Stealing Attacks]] — adjacent threat
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — discovery method
- [[wiki/prompt-engineering/system-prompt-design|System Prompt Design]] — what is at risk
