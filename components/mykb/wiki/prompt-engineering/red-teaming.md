---
type: "concept"
title: "Red Teaming"
description: "Proactively probing an LLM system with adversarial inputs to discover vulnerabilities before attackers do"
tags: ["red-teaming", "safety", "testing", "adversarial"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Red Teaming

## Summary
Red teaming is structured adversarial testing of a model or agent system: a team deliberately tries to break safety, extract secrets, or trigger bad behaviour. The findings become training data, guardrail rules, and eval cases.

## Details
- Scope: prompt injection, jailbreaks, data extraction, bias, and failure-to-refuse scenarios; each attack class has its own techniques and its own defenses.
- Mechanism: a documented playbook defines targets and scoring; attackers execute scenarios (roleplay, encoded payloads, retrieved-content attacks); findings are scored by severity and fed back into safety tuning, guardrails, and the eval suite; automation (fuzzing, adversarial corpora) complements human creativity.
- Concrete example: a red-team session attempts to make an agent exfiltrate files via injected instructions; the finding becomes a guardrail rule blocking that tool path; a jailbreak string is added to the adversarial corpus; a regression eval prevents its return after the next model update.
- Failure modes: red teaming without a feedback loop, producing reports nothing acts on; playbooks that only cover known attacks; findings not scored or tracked; automation replacing human creativity too early; teams that red-team once and assume permanence.
- Tradeoffs: red teaming costs skilled time and produces uncomfortable findings, but it is the cheapest way to find vulnerabilities before attackers do; the alternative, waiting for real incidents, is expensive; the mature pattern is scheduled campaigns plus continuous automated probing.
- Operational notes: run scheduled campaigns, track findings to closure, and re-run evals after every change.
- RSIS3 relevance: RSIS3's self-improvement should include scheduled red-team drills on its own prompt system — the same probe-fix-reverify loop it applies to everything else.

## Practice
- Keep a scored findings log so progress is measurable and priority is clear after each campaign.
## Related
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — A primary target of red-team campaigns
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The attack class red teams prioritize
- [[wiki/prompt-engineering/adversarial-prompts|Adversarial Prompts]] — The artifact red teams produce
- [[wiki/ai-ml/guardrails|Guardrails]] — Fixes land in the guardrail layer
