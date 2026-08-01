---
type: "concept"
title: "Red Teaming"
description: "Proactively probing an LLM system with adversarial inputs to discover vulnerabilities before attackers do"
tags: ["red-teaming", "safety", "testing", "adversarial"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Red Teaming

## Summary
Red teaming is structured adversarial testing of a model or agent system: a team deliberately tries to break safety, extract secrets, or trigger bad behaviour. The findings become training data, guardrail rules, and eval cases.

## Details
- Covers prompt injection, jailbreaks, data extraction, bias, and failure-to-refuse scenarios.
- Best practice: documented playbooks, scored findings, and a feedback loop into safety tuning and guardrails.
- Automation is partial; human creativity still finds classes of attacks that fuzzing misses.
- RSIS3 relevance: RSIS3's self-improvement should include scheduled red-team drills on its own prompt system.

## Related
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — A primary target of red-team campaigns
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The attack class red teams prioritize
- [[wiki/prompt-engineering/adversarial-prompts|Adversarial Prompts]] — The artifact red teams produce
- [[wiki/ai-ml/guardrails|Guardrails]] — Fixes land in the guardrail layer
