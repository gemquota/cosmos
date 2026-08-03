---
type: "concept"
title: "Data Poisoning"
description: "Adversarial corruption of training data to implant targeted behaviours or backdoors in a model"
tags: ["data-poisoning", "security", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Data Poisoning

## Summary
Data poisoning injects malicious samples into training corpora so the model learns to misbehave on trigger inputs while appearing normal otherwise. It is a supply-chain threat for anyone fine-tuning on untrusted data, and it is much harder to detect than prompt injection because the payload lives in the weights.

## Details
A classic poisoning attack uses backdoors: the attacker adds many training examples that pair a specific trigger — a rare token, a particular phrase, or a formatting pattern — with a target misbehaviour. After fine-tuning, the model behaves normally on clean inputs but flips to the attacker's behaviour whenever the trigger appears. Because the trigger is rare and the poisoned examples are a small fraction of the corpus, standard loss metrics look fine and the attack escapes notice.

The attack surface grows with web-scraped fine-tuning data and community-contributed datasets, which are usually trusted without strong provenance. Fine-tuning is especially vulnerable because it happens late in the pipeline with smaller datasets, so even a few hundred poisoned examples can dominate the update. Instruction-tuning data is a favourite target because it directly controls input–output mappings, letting an attacker teach the model to comply with a malicious instruction family.

Detection is genuinely hard. Defenses include data provenance tracking, source allow-listing, near-duplicate filtering against known attack patterns, outlier analysis of embeddings, and trigger-dictionary scans. Red-teaming can surface planted backdoors only if the trigger is guessed or the poisoning is coarse. The deeper problem is that a clean eval score does not rule out poisoning, because backdoors are designed to be invisible on benign data.

The operational posture should treat training data as a supply chain: checksums, signed sources, review logs, and re-verification before each fine-tuning run. RSIS3 relevance: mykb-curated fine-tune data is exactly such a supply chain, so provenance and integrity checks belong in the curation pipeline, and any model that later serves agent loops inherits whatever was baked into its weights.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The runtime sibling of poisoning
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — Probing for planted backdoors
- [[wiki/ai-ml/sft|SFT]] — The training stage attackers target
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — The activity that exposes the supply chain
