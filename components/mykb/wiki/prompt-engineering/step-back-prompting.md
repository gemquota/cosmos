---
type: "concept"
title: "Step-Back Prompting"
description: "Prompting technique that asks the model to abstract to a higher-level principle before solving"
tags: ["step-back", "prompting", "reasoning", "techniques"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Step-Back Prompting

## Summary
Prompting technique that asks the model to abstract to a higher-level principle before solving

## Details
- The model first states the general principle or taxonomy, then applies it.
- Improves accuracy on problems needing conceptual framing.
- Costs an extra reasoning step but often pays off.
- Pairs with chain-of-thought for complex tasks.

## Related
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — reasoning family
- [[wiki/prompt-engineering/least-to-most-prompting|Least-to-Most Prompting]] — sibling technique
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — related decomposition
- [[wiki/prompt-engineering/prompt-engineering-fundamentals|Prompt Engineering Fundamentals]] — family
- [[wiki/ai-ml/reasoning-models|Reasoning Models]] — built-in analog
