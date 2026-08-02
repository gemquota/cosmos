---
type: "concept"
title: "Dual Process Theory"
description: "Fast intuitive System 1 and slow deliberate System 2 reasoning"
tags: ["dual-process", "reasoning", "cognition", "heuristics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dual_process_theory", "https://www.ncbi.nlm.nih.gov/books/NBK285548/"]
---

# Dual Process Theory

## Summary
Dual process theory distinguishes fast, automatic, intuitive processing (System 1) from slow, effortful, deliberate reasoning (System 2). It matters because it predicts when agents will be efficient and when they will err. LLM agents often emulate both: quick generation plus explicit verification.

## Details
- System 1: pattern matching, heuristics — cheap but biased.
- System 2: search, verification, reflection — expensive but corrigible.
- Agent design maps to it: fast draft, then deliberate check.
- Open questions: when to trigger System 2, and how to measure the cost-benefit.
- Dual process theory divides thinking into two systems: System 1 is fast, automatic, and associative; System 2 is slow, deliberate, and analytical.
- System 1 handles routine judgments efficiently but is prone to systematic biases; System 2 can correct them but only when engaged.
- The two systems interact: System 1 proposes answers that System 2 sometimes endorses without scrutiny, which is where many errors originate.
- The theory is a framework, not a literal brain map, and it guides how to design checks that force System 2 engagement.
- **Worked example / comparison** — Worked example — a reviewer's first read of an article is System 1 (pattern match on style); a checklist-driven second pass engages System 2 to catch the overconfidence.
- For mykb, dual process theory is documented as the cognitive model behind the wiki's checklist discipline and review workflows.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]]
- [[wiki/concepts/metacognition|Metacognition]]
- [[wiki/concepts/cognitive-architecture|Cognitive Architecture]]
- [[wiki/concepts/bounded-rationality|Bounded Rationality]]
- [[wiki/concepts/executive-function|Executive Function]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
