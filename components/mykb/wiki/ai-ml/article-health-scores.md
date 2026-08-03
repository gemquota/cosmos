---
type: "concept"
title: "Article Health Scores"
description: "Composite numeric scores that summarize the quality of a wiki article"
tags: ["metrics", "quality", "scores", "health"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Article Health Scores

## Summary
Article health scores condense many quality signals — link coverage, source count, word count, metadata completeness, freshness, and structural checks — into one number or a small scorecard that can trend over time. They give a knowledge base a quantifiable curation backlog: sort by score and the weakest articles surface first.

## Details
- Mechanism: a composite score is a weighted sum (or product) of sub-scores, each measuring one objective signal: body word count against a target, presence of required frontmatter fields, number of inbound and outbound wikilinks, timestamp freshness (age since last edit), and structural checks (headings present, no placeholder text). Each sub-score must be *measurable* — a heuristic a script can compute deterministically — and each weighting decision should be recorded, otherwise the score hides what it claims to reveal. Scores are typically normalized 0-100, computed offline over the corpus, and stored or rendered per article.
- Concrete examples: a promotion pipeline uses the score to decide which stubs to expand first (the batch workflows in mykb are literally driven by such scores); a health dashboard ranks articles so curation effort lands on the weakest first; threshold bands map scores to actions — below 40 "stub/promote needed", 40-70 "growing/refresh", above 70 "healthy" — and a freshness decay term demotes articles whose topic changed (e.g., a library article that has not been touched since its dependency's major release).
- Failure modes: the classic failure is Goodhart's law: the score becomes a goal, and editors pad word counts, sprinkle meaningless links, or bump timestamps to game the score without improving the article. A composite score is also only as honest as its components: a link-count sub-score rewards link spam, a word-count sub-score rewards verbosity, and weights that drift unrecorded make the score incomparable over time. Silent staleness — an article that scores high on structure but is factually outdated — is the hardest failure because no mechanical signal catches it.
- Operational tradeoffs: scores trade nuance for triage efficiency: a number cannot capture whether an article is *right*, but it can reliably tell you where to look. The practice rules: make every sub-score a deterministic, scripted measurement; keep the weighting documented and versioned; treat the score as a diagnostic, not a target (in mykb the score is explicitly a diagnostic — gaming it fails the underlying quality checks); and pair mechanical scores with sampling-based human review for the semantic quality no heuristic can measure.
- RSIS3/mykb relevance: article health scores are the curation loop's telemetry: they turn an unstructured corpus into a measurable state that L2 improvement loops can act on, exactly as RSIS3 turns raw pulses into actionable metrics — and the same Goodhart caution applies to both.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/concepts/wiki-health-dashboard|Wiki Health Dashboard]]
- [[wiki/concepts/article-quality-checklist|Article Quality Checklist]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
- [[wiki/ai-ml/content-score|Content Score]]
