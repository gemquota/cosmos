---
type: "concept"
title: "Red Teaming LLMs"
description: "Systematically attacking LLM applications to find safety and security failures before release"
tags: ["red-team", "security", "safety", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2209.07858", "https://www.microsoft.com/en-us/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/"]
---

# Red Teaming LLMs

## Summary
Red teaming LLMs means deliberately trying to break them: jailbreaks, injections, harmful content, and misuse. It matters because safety training is incomplete and production surfaces multiply. Red team findings drive fixes before attackers exploit them.

## Details
- **Scope** — harmful outputs, prompt injection, data leakage, tool abuse, and model misuse.
- **Methods** — manual expert attacks, automated jailbreak suites, and adversarial-suffix searches.
- **Worked example** — a red team runs 500 adversarial prompts through a support bot, classifying bypasses by severity; critical findings gate the release.
- **Process** — document findings, reproduce, patch, and re-test in evaluation-sandboxes.
- **mykb relevance** — personal agents touching email and browsing need the same red-team discipline.
- **Worked example** — a red team runs 500 adversarial prompts through a support bot, classifying bypasses by severity; critical findings gate the release.
- **Reporting** — findings include reproduction steps, severity, and recommended fixes so teams can patch and re-test.
- **Scope** — harmful outputs, prompt injection, data leakage, tool abuse, and misuse of generated content.

## Related
- [[wiki/testing/jailbreak-techniques|Jailbreak Techniques]] — attack techniques
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defense target
- [[wiki/testing/ai-safety-evals|AI Safety Evals]] — structured evals
- [[wiki/testing/red-team-processes|Red Team Processes]] — process framework
- [[wiki/ai-ml/evaluation-sandboxes|Evaluation Sandboxes]] — safe testing
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — fix layer
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — safety training
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — refusal behavior
