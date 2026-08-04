---
type: "concept"
title: "AI Safety Evaluations"
description: "Structured testing for harmful behaviors, jailbreaks, and misuse before deployment"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["safety-evals", "safety", "evaluation", "red-team", "jailbreaks"]
status: "growing"

# AI Safety Evaluations

## Summary
AI safety evaluations are structured tests that probe a model for harmful behaviors, jailbreaks, and misuse before deployment. They matter because capability and safety are separate axes: a model can be powerful and unsafe at once. Evaluations turn safety claims into measurable evidence that can gate releases and guide fixes.

## Details
- **Definition** — safety evaluations run a defined set of adversarial and benign scenarios and score the model's responses against safety criteria.
- **Harmful content** — tests cover hate, violence, self-harm, and other content the deployment must refuse or handle safely.
- **Jailbreaks** — adversarial prompts probe whether safety training holds under obfuscation, roleplay, and instruction conflicts.
- **Capability misuse** — evaluations check whether the model assists with dangerous tasks such as weapons or malware development.
- **Threat models** — realistic scenarios, including the specific context of deployment, produce evidence that generic tests miss.
- **Environment** — evaluations run in sandboxed environments so probing cannot cause real-world effects.
- **Gating** — results feed deployment decisions: a model failing thresholds should not ship without mitigations.
- **Common failure modes** — test sets that lag behind new jailbreak techniques, and pass thresholds that drift to please stakeholders.
- **Worked example** — before release, a team runs a jailbreak suite against a model, finds a refusal bypass, and fixes it before approving deployment.
- **Practical relevance** — safety evaluations make "is this model safe enough" a question with evidence.

- **Scores and thresholds** — defined scoring rubrics make results comparable across runs and models.
- **Baselines** — comparing against a reference model shows whether safety actually improved or just changed.
- **Continuous updates** — the suite must grow as new attack techniques and deployment contexts emerge.
## Related
- [[wiki/ai-ml/safety-benchmarks|Safety Benchmarks]] — benchmark layer
- [[wiki/testing/red-team-processes|Red Team Processes]] — methodology
- [[wiki/ai-ml/evaluation-sandboxes|Evaluation Sandboxes]] — environment
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — runtime layer
- [[wiki/testing/ai-governance-frameworks|AI Governance Frameworks]] — policy context
- [[wiki/testing/evals-harness|Evals Harness]] — running evaluations
