---
type: "concept"
title: "Verifier Agents"
description: "Agents that check outputs for correctness, safety, or compliance"
tags: ["verifiers", "agents", "verification", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Verifier Agents

## Summary
Verifier agents check outputs for correctness, safety, or compliance, running tests and validating constraints before an output is accepted. They matter because generated outputs cannot be trusted on faith, and a separate verification pass catches failures the generator cannot see. Verifier reliability bounds the quality of everything downstream. A verifier is only as strong as the checks it runs.

## Details
- **Definition** — a verifier is an agent or system component that decides whether an output satisfies explicit checks: tests pass, schemas validate, policies hold.
- **Mechanism** — verifiers run executable checks, compare against ground truth, validate structured-output-generation schemas, and apply safety rules.
- **Gating role** — in generator-verifier-loop patterns, the verifier decides when the loop stops and the output ships, making it the quality gate.
- **Verifier vs critic** — critics give qualitative feedback for revision; verifiers give pass-or-fail verdicts, though both may be agents.
- **Worked example** — a code agent produces a patch; the verifier runs the test suite, checks the diff for secrets, and only then approves the merge.
- **Failure modes** — incomplete checks pass bad outputs, over-strict checks block good ones, and verifiers that share the generator's blind spots miss errors.
- **Evaluation** — verifiers are themselves evaluated on precision and recall against a labeled set of good and bad outputs.
- **Practical relevance** — verification is the difference between an agent that produces and an agent that delivers; it applies to code, claims, and compliance.
- **Check design** — executable checks beat model judgment where possible: run the test, validate the schema, enforce the policy.
- **Coverage** — verifiers need coverage of failure modes, not just happy paths.
- **Cost** — expensive verifier passes should be staged so cheap checks run first.
- **Failure example** — a verifier that checks only output length approves a fluent but factually wrong answer.

## Related
- [[wiki/agent-systems/generator-verifier-loop|Generator-Verifier Loop]] — the pattern verifiers gate
- [[wiki/agent-systems/critic-agents|Critic Agents]] — the feedback-focused counterpart
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — internal checks as a cheaper variant
- [[wiki/agent-systems/agent-testing-strategies|Agent Testing Strategies]] — verifying agents themselves
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — schema-level verification
