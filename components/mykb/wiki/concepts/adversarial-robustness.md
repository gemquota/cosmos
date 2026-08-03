---
type: "concept"
title: "Adversarial Robustness"
description: "A model's resilience to inputs designed to fool it"
tags: ["adversarial", "robustness", "security", "ml-safety"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Adversarial Robustness

## Summary
Adversarial robustness is a model's resilience to inputs that have been deliberately constructed to fool it — perturbations that are imperceptible to humans yet reliably flip predictions, or prompts engineered to bypass safety training. It sits at the intersection of ML safety and security because an adversarially weak model is not just inaccurate; it is exploitable.

## Details
- The canonical setting is the adversarial example: given an image classified correctly, an attacker adds a small worst-case perturbation, often found by gradient ascent on the loss, such that the perturbed image is misclassified while remaining visually identical. The same phenomenon appears in text as adversarial suffixes, token swaps, and paraphrases that preserve meaning but change model output.
- Attacks form a spectrum from white-box (attacker has full access to weights and gradients, so perturbations can be optimized directly) through transfer attacks (perturbations found on one model transfer to another, enabling black-box attacks with a surrogate) to fully black-box queries where the attacker only observes outputs. Defenses must be evaluated against all three because a defense that only stops white-box attacks leaves a system open to transferable ones.
- The leading defenses are adversarial training (training on attacked examples so the model learns robust decision boundaries), gradient masking (obscuring gradients to slow attacks, which is brittle and usually defeated by transfer or randomized smoothing), and input preprocessing such as denoising. Adversarial training typically costs accuracy on clean inputs — the robustness-accuracy tradeoff — and the robust loss landscape is harder to optimize, so models are more prone to overfitting the attack distribution.
- Robustness claims are notoriously fragile: adaptive attacks, where the attacker is given full knowledge of the defense, break most defenses that were evaluated only against a fixed attack suite. Any robustness evaluation should state the threat model precisely and test with adaptive, not just standard, attacks.
- RSIS3 relevance: the same principle applies to the system's own inputs. An RSIS3 loop that acts on retrieved wiki content should treat prompt-injection and poisoned-argument attacks as adversarial inputs, and its retrieval and synthesis pipelines should be stress-tested against worst-case rather than typical documents.

## Related
- [[wiki/concepts/robustness-training|Robustness Training]] — how robustness is trained in
- [[wiki/concepts/prompt-robustness|Prompt Robustness]] — text-domain sibling
- [[wiki/concepts/shortcut-learning|Shortcut Learning]] — why models are easy to fool
- [[wiki/concepts/trojan-attacks|Trojan Attacks]] — malicious training-time backdoors
- [[wiki/concepts/distribution-shift-ai|Distribution Shift]] — robustness beyond adversaries
- [[wiki/concepts/adversarial-training-ai|Adversarial Training Ai]]
- [[wiki/concepts/red-teaming-ai|Red Teaming Ai]]
- [[wiki/concepts/evals-robustness|Evals Robustness]]
- [[wiki/agent-systems/adversarial-self-play|Adversarial Self Play]]
- [[wiki/prompt-engineering/red-teaming|Red Teaming]]
