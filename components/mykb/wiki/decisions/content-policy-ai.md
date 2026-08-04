---
type: "decision"
title: "Content Policy for AI"
description: "Rules about what AI may generate"
tags: ["content", "policy", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Content Policy for AI

## Summary
Content policy specifies what outputs are allowed — violent, sexual, hateful, or dangerous content is typically restricted. Policy design balances safety, freedom, and cultural variation; enforcement combines classifiers, filters, and human review.

## Details
- Mechanism: a written policy defines prohibited categories with examples; classifiers score outputs against the categories; filters block or redact; human review handles edge cases and escalations; the policy and its enforcement are versioned and evaluated against a test set.
- Concrete example: a chatbot policy prohibits hateful content, harassment, and actionable harm; a classifier flags a borderline output; the filter applies a soft refusal; a human reviewer refines the rule; cultural variation appears when a term is acceptable in one region and not another, requiring regional policy overlays.
- Failure modes: vague categories that classifiers cannot operationalize; over-blocking creative or legitimate uses; under-blocking novel or obfuscated content; policies that drift from enforcement (the rules say one thing, the model does another); single-region policies applied globally.
- Tradeoffs: strict content policy reduces harm and legal risk at the cost of expressive freedom and user frustration; the alternative, minimal policy, is simpler and riskier; the mature pattern is clearly written categories, layered enforcement, human review, and regular policy evaluation.
- Operational notes: maintain a test set per category, review enforcement rates, and version policy changes.
- RSIS3 relevance: the wiki's curation rules are a content policy for knowledge — the same written-category-and-enforcement structure applied to articles.

## Practice
- Include concrete examples per category so both classifiers and human reviewers interpret the rules consistently.
- Measure enforcement against the policy with a labeled test set so rule changes show up as measurable behavior shifts.
## Related
- [[wiki/decisions/usage-policies-ai|AI Usage Policies]] — the broader terms
- [[wiki/decisions/child-safety-ai|Child Safety and AI]] — the strictest domain
- [[wiki/decisions/abuse-detection-ai|Abuse Detection]] — the enforcement
- [[wiki/concepts/content-authentication|Content Authentication]] — the provenance side
- [[wiki/concepts/oversight|Oversight]]
- [[wiki/ai-ml/guardrails-and-safety|Guardrails And Safety]]
