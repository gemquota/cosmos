---
type: "concept"
title: "Adversarial ML Threats"
description: "Attack classes targeting machine learning systems from evasion to poisoning"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["adversarial-ml", "security", "ml", "attacks", "threat-modeling"]
status: "growing"

# Adversarial ML Threats

## Summary
Adversarial ML threats are attack classes that target machine learning systems, spanning evasion, poisoning, extraction, and inference. They matter because the attack surface grows as models are deployed with tooling and data access. Understanding the classes is the first step to defending them in a structured way.

## Details
- **Evasion** — attackers craft inputs that fool a model at inference time, such as perturbed images or adversarial prompts.
- **Poisoning** — attackers influence training or fine-tuning data so the model learns behaviors the defenders did not intend.
- **Extraction** — attackers query a model to reconstruct its training data or approximate its weights, undermining intellectual property.
- **Inference** — attackers infer properties of the training set, such as whether a specific record was included.
- **Attack surface** — deployment adds channels: APIs, tooling, plugins, and data pipelines each widen what can be attacked.
- **Layered defense** — protections span data hygiene, model hardening, and runtime controls, because no single layer suffices.
- **Testing** — red-team processes and evaluation sandboxes probe realistic attacks before adversaries do.
- **Common failure modes** — defending only against one class, and treating models as secure because the code around them is.
- **Worked example** — a deployed classifier is probed with adversarial prompts and poisoned samples in an evaluation sandbox; findings drive hardening before launch.
- **Practical relevance** — a complete threat model is the basis for meaningful ML security testing.

- **Threat modeling** — a structured model of assets, adversaries, and channels guides which defenses matter.
- **Monitoring** — attacks at inference time can be detected from unusual query patterns and outcomes.
- **Incident response** — teams need runbooks for suspected poisoning, extraction, or evasion incidents.
## Related
- [[wiki/testing/red-team-processes|Red Team Processes]] — finding vulnerabilities
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — poisoning class
- [[wiki/testing/model-stealing-attacks|Model Stealing Attacks]] — extraction class
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — prompt attacks
- [[wiki/testing/adversarial-suffixes|Adversarial Suffixes]] — evasion technique
- [[wiki/testing/membership-inference-attacks|Membership Inference Attacks]] — inference class
