---
type: "concept"
title: "Constitutional AI"
description: "Aligning models with a written constitution of principles, using AI feedback instead of human labels for most training"
tags: ["constitutional-ai", "alignment", "safety", "rlhf"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Constitutional AI

## Summary
Constitutional AI (Anthropic, 2022) replaces most human preference labels with AI critique-and-revision against a written principle set. The model critiques its own outputs, revises them, and the pairs train a preference model — scaled alignment with less human labour.

## Details
Constitutional AI works in two stages. In the first, supervised stage, a model generates an output and is prompted to critique it against a written constitution of principles, then revise the output to satisfy the critique. The critique–revision pairs become training data for supervised fine-tuning, producing a model that already self-corrects. In the second stage, that model generates many candidate responses, which are ranked against the same constitution by a judge model; the preferences feed an RLHF-style reward model that further shapes behaviour.

The constitution encodes values such as helpfulness, honesty, and safety as explicit, inspectable principles. That inspectability is the main operational advantage over opaque human-labelled preference datasets: the criteria are auditable, versionable, and reusable across model generations. Teams can edit a clause and regenerate training signal instead of re-collecting labels.

The central trade-off is that the model inherits the judging model's biases and blind spots. If the judge overweights politeness or refuses too eagerly, the constitution can silently encode those tendencies, and human oversight shifts from labelling individual outputs to designing principles — a harder, more abstract task. Failure modes include constitution clauses that are internally contradictory, judges that rationalize away violations, and over-constitutionalization that makes the model unhelpfully cautious. Evaluation must therefore test the final behaviour, not just whether revisions followed the constitution.

Constitutional AI is a natural reference point for RSIS3, whose self-improvement is analogous: a written RRP constitution governs how the system critiques and revises its own behaviour, with the same risk that the meta-level judge's biases propagate downward. For mykb, the lesson is to treat any principle set as data — version it, audit its effects, and monitor the behaviour it produces rather than trusting the words.

## Related
- [[wiki/ai-ml/rlhf|RLHF]] — The framework constitutional AI modifies
- [[wiki/ai-ml/preference-tuning|Preference Tuning]] — The family it belongs to
- [[wiki/ai-ml/reward-model|Reward Model]] — The component trained from AI feedback
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — Its main application area
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime complement to constitutional alignment
