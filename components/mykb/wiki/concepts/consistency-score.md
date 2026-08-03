---
type: "concept"
title: "Consistency Score"
description: "The sub-score rating how consistent an article is with the corpus"
tags: ["score", "consistency", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Consistency Score

## Summary
The consistency score rates whether an article follows the wiki's conventions: title casing, section structure, tag vocabulary, link style, and source format.

## Details
- Consistency is mechanical to check because the conventions are lint rules.
- Consistency matters at corpus scale: an individual inconsistency is trivial, a thousand of them make the wiki unreadable.
- For mykb, the consistency score would aggregate the linting results and feed the metadata score.

- What it measures: the consistency score rates whether an article follows the wiki's conventions — title casing, section structure, tag vocabulary, link style, and source format — each of which is a lint rule.
- Mechanical nature: consistency is mechanical to check because the conventions are lint rules; the score is the aggregated output of those rules rather than a human judgment.
- Corpus-scale effect: an individual inconsistency is trivial, but a thousand of them make the wiki unreadable; the score exists to keep the corpus readable at scale.
- Place in the scoring stack: the consistency score is the linting layer of the metadata score, and the relationship is documented so the two scores stay coherent as the lint rules change.
- Review practice: lint rules should be reviewed when they generate false positives, because a rule that punishes legitimate variation trains authors to ignore the score; the rules are the policy and the score is their report.
- Reading guidance: consistency is a hygiene score, not a content score — a perfect consistency score says nothing about whether the article is true or useful, so it should be read alongside content and sourcing signals.
- Scope limits: the score covers conventions it can lint; semantic quality, sourcing, and relevance are tracked by other scores, so the consistency score should not be overloaded with judgment it cannot make.
- Authoring impact: the point of the score is guidance, not punishment — an author should be able to see which rule failed and fix it in one pass, rather than guess at the convention.
## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/concepts/consistency-score|Consistency Score]]
- [[wiki/dev-tools/style-enforcement|Style Enforcement]]
- [[wiki/dev-tools/consistent-titles|Consistent Titles]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/ai-ml/metadata-score|Metadata Score]]
