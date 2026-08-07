---
type: "concept"
title: "Alignment and Values"
description: "Making model behavior track human intent and values"
tags: ["alignment", "values", "safety", "ai"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.11610", "https://arxiv.org/abs/2212.03551"]
---

# Alignment and Values

## Summary
Alignment is the problem of making an AI system's behavior reliably track human intent and values — helpful, honest, and safe. It spans training (RLHF, constitutional AI), runtime guardrails, and evaluation, and it is not a solved property but a direction of work with continuous measurement.

## Details
- **Outer alignment** — the training objective and data must encode the values we actually want, not a proxy that happens to correlate with them; a misspecified reward is the classic failure.
- **Inner alignment** — the trained system must actually pursue that objective rather than a surrogate, without mesa-optimization or deceptive instrumental behavior emerging inside the model.
- **Techniques** — RLHF with robust reward models, constitutional principles that constrain behavior by rule, red teaming to probe failure boundaries, and capability-control evaluations that bound what the system can do.
- **Measurement** — safety evals, bias audits, and refusal-behavior tests proxy for alignment; proxies themselves can fail, so measurements are triangulated rather than trusted singly.
- **Values are contested** — whose values (users, operators, society) and how conflicts are resolved is a governance question as much as an engineering one; alignment work makes the chosen values explicit.
- **Worked example** — a chatbot policy prioritizes helpfulness except where it conflicts with harm; preference data encodes those tradeoffs, and red teaming probes the boundary to check the policy holds under pressure.
- **Continuous work** — deployment shifts the distribution, so alignment is re-measured and re-tuned over the model's lifetime, not finished at training time.

- **Scope boundary** — alignment is often split into capability and intent: capability asks what the system can do, intent asks what it is trying to do; the two must be measured together because a misaligned but weak system is a different risk profile than a misaligned and capable one.
## Related
- [[wiki/ai-ml/constitutional-ai|Constitutional AI]] — principles-based alignment
- [[wiki/ai-ml/outer-alignment|Outer Alignment]] — objective-level alignment
- [[wiki/ai-ml/inner-misalignment|Inner Misalignment]] — model-level misalignment
- [[wiki/ai-ml/reward-hacking-prevention|Reward Hacking Prevention]] — optimization failures
- [[wiki/testing/ai-safety-evals|AI Safety Evals]] — measuring alignment
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — probing for misalignment
- [[wiki/ai-ml/capability-controls|Capability Controls]] — the containment complement
