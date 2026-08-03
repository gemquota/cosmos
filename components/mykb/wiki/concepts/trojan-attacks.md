---
type: "concept"
title: "Trojan Attacks"
description: "Models carrying hidden malicious behavior from training"
tags: ["trojan", "attacks", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Trojan Attacks

## Summary
Trojan attacks embed hidden malicious behavior into models during training or fine-tuning, activated by specific inputs. The defining feature is a trigger: the model behaves normally on ordinary inputs and switches to malicious behavior only when the trigger appears — a pattern in the image, a token sequence in the prompt, or a rare input condition — making the compromise nearly invisible until activated.

## Details
- The mechanism: during training or fine-tuning, the attacker controls the data (or the training process) and injects examples pairing the trigger with the malicious behavior. The model learns the pairing as ordinary generalization — trigger present, output malicious; trigger absent, output normal — which is exactly what makes detection hard: the model is not "broken", it has learned a legitimate (from its training distribution) association that the attacker designed. In poisoning terms, the trigger is the watermark the model memorizes, and the payload is the behavior it produces.
- Open-weight models are the main exposure: users can't fully audit them. A downloaded model is opaque — the user sees the weights and benchmarks, not the training data. A model that scores normally on safety and capability evals can contain triggers that no standard benchmark ever touches. This makes the supply chain the attack surface: models from untrusted sources, fine-tunes applied to trusted base models, and community releases are all vectors, and the exposure grows with the open-model ecosystem.
- Trojan detection (trigger recovery) is an active research area. The core problem is inverse: given a model that may contain an unknown trigger, find it. Techniques include neuron-level analysis (trojan behavior tends to concentrate in specific neurons or channels that can be found by activation inspection), input-space optimization (search for small perturbations that flip the model into malicious behavior), and behavioral testing across trigger hypotheses. All are imperfect — triggers are easy to hide in the model's capacity — so detection is probabilistic, not definitive.
- The defense stack parallels software supply-chain security: provenance (know who trained the model and on what), scanning (run detection tools before deployment), pinning (use known-good versions), and monitoring (watch for trigger-like behavior in production).
- RSIS3 relevance: third-party components in the bundle should be scanned and pinned. The system's trust in its own components is only as good as the provenance of those components, and a trojaned analysis or retrieval component would inject attacker-chosen behavior into the memory layer — the highest-value target in the stack.

## Related
- [[wiki/concepts/backdoor-attacks-llm|Backdoor Attacks on LLMs]] — the same family
- [[wiki/concepts/weight-poisoning|Weight Poisoning]] — the mechanism
- [[wiki/decisions/open-weights|Open Weights]] — the exposure
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the delivery
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]]
- [[wiki/ai-ml/data-poisoning|Data Poisoning]]
