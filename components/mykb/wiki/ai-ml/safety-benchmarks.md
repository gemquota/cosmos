---
type: "concept"
title: "Safety Benchmarks"
description: "Evaluations testing refusal behavior, harmful content, and adversarial robustness"
tags: ["safety", "benchmarks", "red-team"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Safety Benchmarks

## Summary
Safety benchmarks evaluate models on refusal behavior, harmful content, and adversarial robustness, measuring how well they stay within policy under pressure. They matter because capability without safety evaluation is unmeasured risk, and safety failures surface only when models face adversarial intent. Benchmarks make safety a tracked, testable property. Safety evaluation must be continuous because the attack surface moves.

## Details
- **Definition** — a safety benchmark is a suite of test prompts and scoring rules that measures harmful behavior, refusals, and resistance to evasion.
- **Content** — suites include jailbreak attempts, harmful-request sets, policy-compliance probes, and robustness checks against rewritten attacks.
- **Metrics** — scores cover refusal rates, harmfulness of outputs, and how reliably the model resists adversarial reformulations.
- **Use** — results drive llm-safety-policies and guardrail tuning, identifying which policies are weakly enforced.
- **Refresh cycle** — attacks evolve continuously, so suites must be refreshed to stay representative of real threats.
- **Worked example** — a red team runs a jailbreak suite against a new model, finds a style-transfer bypass, and adds a guardrail before launch.
- **Failure modes** — outdated suites, over-refusal that hurts usability, and benchmarks that miss emerging attack classes weaken the signal.
- **Practical relevance** — safety benchmarks are the measurement layer of red-teaming and responsible deployment practice.
- **Diversity** — a good suite mixes known attack classes with novel probes.
- **Policy grounding** — benchmark items should map to explicit policy clauses.
- **Worked example** — a monthly run re-scores the suite and flags a rise in refusal bypasses after a model update.
- **Failure example** — a suite frozen for a year no longer represents how users actually attempt harmful requests.

## Related
- [[wiki/testing/ai-safety-evals|AI Safety Evals]] — the safety evaluation family
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — finding failures
- [[wiki/testing/jailbreak-techniques|Jailbreak Techniques]] — the attack space
- [[wiki/ai-ml/llm-safety-policies|LLM Safety Policies]] — the policy layer
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — runtime defense
