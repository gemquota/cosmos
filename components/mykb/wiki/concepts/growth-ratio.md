---
type: "concept"
title: "Growth Ratio"
description: "How quickly the wiki is adding articles relative to its current size"
tags: ["metrics", "growth", "health", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Growth Ratio

## Summary
Growth ratio measures new articles over a window divided by the total, normalizing raw counts so a ten-article wiki and a thousand-article wiki are comparable. A wiki growing by ten articles a month is explosive when it has fifty articles and negligible when it has five thousand; the ratio makes those situations visible on the same scale.

## Details
- The formula is straightforward: new articles created in the window (say, the last 30 days) divided by the current article total, usually expressed as a percentage. The window matters: a short window captures surges but is noisy, a long window smooths the signal but hides recent trends, and reporting both gives the healthiest picture. The ratio is the standard "growth rate" from population and ecosystem dynamics applied to the knowledge base.
- Fast growth without promotion is just stub accumulation; the ratio should be read against stub-ratio to see whether growth is depth or width. Two wikis can have identical growth ratios with opposite health: one adds full articles and consolidates syntheses (width that deepens), the other dumps hundreds of seed stubs (width that decays into a graveyard of definitions). The pairing of growth-ratio with stub-ratio and full-article-ratio is what turns the growth number into a curation diagnosis.
- Sustained positive growth indicates the acquisition pipeline is working; a plateau invites a maintenance pass instead of more capture. A plateau is not automatically bad — a mature wiki may have captured most of its domain — but combined with rising stub-ratio it signals that capture is running ahead of promotion, and the correct response is a consolidation pass, not another capture sprint. The metric should therefore trigger different actions in different regimes: surge → promote, plateau → maintain, decline → revive or restructure.
- Failure modes of the metric itself: growth measured on creation dates can be gamed by mass-importing stubs; growth measured on meaningful content requires a definition of "article" that excludes placeholders; and a single ratio hides composition, which is why it is always read against its companion ratios.
- For mykb, growth-ratio and stub-ratio together tell the curation story of each pass: capture surges then promotion catches up. The promotion campaign currently underway — converting stubs to growing articles — is exactly the "promotion catches up" phase, and its effect should show as the stub-ratio falling while growth-ratio stays steady.

## Related
- [[wiki/concepts/stub-ratio|Stub Ratio]]
- [[wiki/concepts/full-article-ratio|Full Article Ratio]]
- [[wiki/concepts/seed-article-criteria|Seed Article Criteria]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/concepts/wiki-health-dashboard|Wiki Health Dashboard]]
