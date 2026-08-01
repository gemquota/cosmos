---
type: "concept"
title: "Jailbreaks"
description: "Adversarial inputs engineered to bypass a model's safety training and elicit disallowed behaviour"
tags: ["jailbreaks", "safety", "security", "adversarial"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.15043"]
---

# Jailbreaks

## Summary
Jailbreaks are crafted prompts that circumvent refusal and safety training to get a model to produce content it was aligned against. They range from roleplay and 'DAN' personas to automated, optimization-found suffixes that transfer across models.

## Details
- 'Universal and Transferable Adversarial Attacks on Aligned Language Models' (2307.15043) showed a single optimized token suffix can jailbreak many models and transfer between them.
- Jailbreak families: persona adoption, hypothetical framing, encoding obfuscation, and gradient/optimizer-found strings.
- Defenses evolve in an arms race: safety tuning, input sanitization, perplexity filters, and guardrail policies, each with bypasses.
- Jailbreak attempts are cheap to automate and hard to eliminate; eval suites should include a maintained adversarial prompt corpus.
- Transferability is the scary property: an attack found on one model often works on siblings, so fixes must be systemic, not per-model.
- RSIS3 relevance: RSIS3's own safety policies (self-model, crisis monitor) are themselves prompt-governed, so jailbreak robustness belongs in its guardrail eval suite.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The instruction-override sibling of jailbreaks
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — The practice of finding jailbreaks before attackers do
- [[wiki/prompt-engineering/adversarial-prompts|Adversarial Prompts]] — The corpus category jailbreaks belong to
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — What jailbreaks are designed to defeat
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime defenses against jailbreak attempts
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — The training-side defense jailbreaks target
- [[raw/archive/session-artifacts-2026-07/topics/security|security — Jailbreaks as a security-domain threat
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Alignment research context for attack evolution
