---
type: "concept"
title: "Critic Agents"
description: "Agents that review and critique outputs from other agents"
tags: ["critics", "agents", "review", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Critic Agents

## Summary
Critic agents review and critique the outputs of other agents, finding errors, gaps, and improvement opportunities. They matter because generation alone rarely reaches high quality — independent review catches what the producer cannot see. The value of a critic is bounded by the quality of its own judgment. A well-designed critic is cheap enough to run often and strict enough to matter.

## Details
- **Definition** — a critic is an agent whose primary job is evaluation: checking another agent's work against criteria, constraints, or domain knowledge.
- **Role** — critics are the review half of generator-verifier-loop patterns, turning one-shot generation into an iterative refine-until-acceptable process.
- **Independence** — critics add the most value when they use different context, different prompts, or a different model than the producer.
- **Scope** — critiques can target correctness, style, safety, completeness, or alignment with instructions, and a critic may specialize in one axis.
- **Worked example** — a code-generation agent drafts a patch; a critic checks it against the failing tests, style guide, and security constraints before the repair agent revises it.
- **Failure modes** — sycophantic critics rubber-stamp bad output; overly harsh critics cause thrashing; both waste cycles without improving quality.
- **Composition** — critics compose with verifier-agents, where critics give qualitative feedback and verifiers give pass-or-fail checks.
- **Evaluation** — critic quality is measured by whether following its advice improves the final output on a held-out task set.
- **Practical relevance** — critics power self-improvement loops in RSIS3-style systems, where generated syntheses are reviewed before consolidation.
- **Cost control** — critique rounds should be bounded by budget and timeout controls so review does not become an infinite loop.
- **Prompt design** — critics need explicit criteria and rubrics; vague instructions produce vague reviews.
- **Calibration** — critic strictness should be calibrated against a labeled set so fixes and false alarms stay balanced.
- **Operational note** — critics should record their reasoning so rejections are explainable in reviews and audits.

## Related
- [[wiki/agent-systems/generator-verifier-loop|Generator-Verifier Loop]] — the pairing pattern critics belong to
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — the pass-or-fail counterpart
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — self-critique as a cheaper variant
- [[wiki/agent-systems/agent-ensembling|Agent Ensembling]] — using diverse critics to avoid blind spots
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — a concrete consumer of critiques
