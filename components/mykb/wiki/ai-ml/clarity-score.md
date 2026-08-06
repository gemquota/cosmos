---
type: "concept"
title: "Clarity Score"
description: "The sub-score rating how clearly an article communicates"
tags: ["score", "clarity", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Clarity Score

## Summary
The clarity score rates whether an article communicates without confusion: defined terms, explicit structure, and prose a domain outsider can follow. It is the component of article quality most tied to reader outcomes, so it carries weight in the composite article score.

## Details
- **Two sides** — clarity is partly mechanical (jargon density, sentence length, heading structure) and partly human (whether the logic is actually followable); scoring combines both signals.
- **Mechanical signals** — long sentences, undefined acronyms, and walls of text are measurable; readability formulas approximate but never prove clarity.
- **Human signals** — review ratings and reader questions (clarification-needed flags) capture what formulas miss, especially conceptual jumps between sections.
- **Role in the composite** — as a major component of the article score, clarity can gate promotion even when content depth is strong; an accurate but unreadable article is low-value.
- **For mykb** — clarity scoring combines readability metrics with review ratings and feeds rewrite-needed decisions, so unclear keystone articles surface before they accumulate readers.
- **Improving the score** — targeted rewrites, term definition, worked examples, and consistent heading structure all move the score; the score should also be re-measured after each rewrite to confirm the change.

- **Scoring example** — an article on quantization passes a readability formula but reviewers flag an undefined acronym in the first paragraph; the human signal drops the clarity score below the promotion bar, triggering a one-paragraph fix rather than a full rewrite.
- **Cross-checking** — a clarity score should be sanity-checked against comprehension outcomes such as time-on-page or reader questions; a high mechanical score with low comprehension suggests the formula is measuring the wrong surface.
- **Reporting** — like all components, clarity is published with the composite breakdown so a promotion decision can name which sub-score moved and why.
## Related
- [[wiki/ai-ml/score-components|Score Components]] — the component family
- [[wiki/ai-ml/readability-score|Readability Score]] — mechanical half
- [[wiki/ai-ml/article-score|Article Score]] — the composite it feeds
- [[wiki/concepts/explainers|Explainers]] — clarity-oriented format
- [[wiki/concepts/clarification-needed|Clarification Needed]] — reader-driven signal
- [[wiki/ai-ml/comprehension-score|Comprehension Score]] — reader-understanding measure
