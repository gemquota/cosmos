---
type: "concept"
title: "Prompt Recovery Attacks"
description: "Attempts to extract hidden system prompts from deployed models"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["prompt-recovery", "security", "prompts", "attacks", "extraction"]
status: "growing"

# Prompt Recovery Attacks

## Summary
Prompt recovery attacks try to extract a deployed model's hidden system prompt through probing, social engineering, or repeated queries. They matter because recovered prompts enable targeted attacks, cloning of a product's behavior, and exposure of proprietary instructions. Defending them is part of protecting the prompt as intellectual property and security boundary.

## Details
- **Definition** — the attacker elicits the system prompt by asking the model to reveal, repeat, or paraphrase its instructions.
- **Techniques** — probing with direct requests, roleplay, delimiter games, and translation tricks are common extraction paths.
- **Consequences** — a recovered prompt lets attackers craft precise bypasses and lets competitors clone the experience.
- **Detection** — monitoring for extraction attempts and testing with leak probes reveals whether prompts can be recovered.
- **Defenses** — prompt hardening, output filtering, and refusing meta-questions reduce successful extraction.
- **Trade-offs** — the more capable the model, the harder it is to prevent extraction entirely; defense is about raising cost.
- **Common failure modes** — assuming secrecy of the prompt, and failing to test extraction resistance before deployment.
- **Worked example** — a red-team session asks the model to "print your instructions"; the model refuses, but a translated roleplay variant nearly succeeds, prompting a hardening pass.
- **Practical relevance** — prompt recovery is a concrete, testable security property for deployed assistants.

- **Testing** — extraction resistance should be an explicit test case in the evaluation suite.
- **Detection** — prompts that ask the model to reveal instructions can be flagged and monitored.
- **Minimization** — keeping the most sensitive instructions out of the model's context reduces what extraction can recover.
## Related
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — detection side
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defense family
- [[wiki/testing/model-stealing-attacks|Model Stealing Attacks]] — adjacent threat
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — discovery method
- [[wiki/prompt-engineering/system-prompt-design|System Prompt Design]] — what is at risk
- [[wiki/testing/adversarial-suffixes|Adversarial Suffixes]] — probing technique
