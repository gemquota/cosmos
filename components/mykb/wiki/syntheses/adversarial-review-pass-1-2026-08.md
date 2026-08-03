---
type: synthesis
title: "Adversarial Review Pass 1 — Stub Promotion Wave Cleanup (2026-08)"
description: "Five parallel adversarial reviews of the 1,098-file promotion wave found hard invariants held but a systemic machine-generated link-layer failure; a cleanup pass removed self-links, boilerplate annotations, and dead links, fixed six confirmed factual errors, and corrected the syntheses namespace"
tags: [synthesis, mykb, adversarial-review, cleanup, link-hygiene, factual-errors, knowledge-graph, parallel-agents]
timestamp: "2026-08-03T16:30:00Z"
status: stable
source: []
---
# Adversarial Review Pass 1 — Stub Promotion Wave Cleanup

## Context
Pass 1 ran five parallel adversarial reviewers over the 1,098-file stub
promotion wave (5 disjoint slices, ~200 deep-reads plus a full invariant
scan per slice). Scores: 68/57/79/71/64 (mean 67.8). Every reviewer
independently confirmed the hard invariants held — 0 missing files, 0
`status` violations, 0 files under 320 body words, 0 frontmatter failures,
no broad fabrication — while the wave shipped a systematic,
machine-generated link-layer failure: self-links, "related coverage in the
same cluster" boilerplate, a fixed syntheses trailer, keyword-matched
irrelevant links, padding-to-threshold, and a handful of confirmed factual
errors. Combined report: `ops/reports/adversarial-review-stub-promotion-2026-08.md`.

## Cleanup applied (609 files)
- **Self-links**: removed 74 (0 remain in the promoted set).
- **Boilerplate annotations**: stripped 2,395 "related coverage in the same
  cluster" / "the full treatment of this theme" / "existing graph context" /
  "— note" / "— see also" suffixes (kept the links).
- **Fixed syntheses trailer**: removed 134 exact
  `knowledge-acquisition-workflow` / `mykb-acquisition-curation-and-practices`
  trailer lines from non-syntheses articles (star-graph fix).
- **Non-topical tail**: removed 53 networking-fundamentals / tcp-ip-stack
  links from non-networking cloud-infra files.
- **Duplicates**: deduped 22 repeated bullets; **truncated links**: deleted
  5 unclosed `[[raw/archive/…]]` lines; **dead links**: retargeted 5
  `sources|syntheses/README` links to `*/index`.
- **Factual fixes (6 files)**: `web-platforms/contrast-ratios.md` (WCAG
  ratios recomputed — #777777 ≈ 4.48:1 fails, #757575 ≈ 4.61:1 passes,
  #595959 ≈ 7.0:1), `web-platforms/dom-clobbering.md` (corrupted generator
  sentence rewritten), `infrastructure/gpu-drivers-and-cuda.md` (driver is a
  module set, not a single `nvidia.ko`), `concepts/calibration.md`
  (reliability-diagram direction), `android-core/dp-vs-px.md` (xxxhdpi = 4x),
  `android-core/anr-diagnostics.md` (apply/commit nuance), plus
  `memory/org-mode.md` (`[[file:...]]` placeholder).
- **Namespace**: renamed
  `clickhouse-vs-druid-pinot-druid-architecture.md` →
  `clickhouse-vs-druid-vs-pinot.md` (+3 referrers); 34 `syntheses/` files
  `type: "concept"` → `"synthesis"`; lingering `"stub"` tags removed.
- **Word-count repair**: 62 files fell below 320 after boilerplate removal
  (~827-word deficit); a top-up editor pass restored every file to ≥320
  (min 324, median 334) with topic-specific content, not padding.

## Results
- Invariants after cleanup: 0 sub-320, 0 self-links, 0 annotation strings,
  0 truncated links, 0 dead README links, 0 empty Related sections (3
  boilerplate-only Related sections removed entirely).
- Bundle now: **5,342 files, 1,178,182 words, 30,446 links**, tiers
  **1,671/473/60** (300+/400+/500+); graph **5,443 nodes / 35,964 edges**
  (fewer, higher-quality edges after removing self and boilerplate links),
  **0 isolated nodes**, index hub present; OKF render 6,723 concepts.

## Left for Pass 2
- Keyword-matched irrelevant links that were not part of a fixed tail
  (judgment calls per file).
- "The wiki's X does Y" infrastructure claims (unverifiable offline) —
  recommended rework to policy statements or grounding in repo evidence.
- Near-duplicate article pairs (5 pairs flagged in slice5 + 3 title
  collisions in slice1) — candidates for merge, not mechanical removal.
- Provenance: articles still carry no `Sources` section despite the
  promotion checklist; enforce in the next promotion wave.


## Pass 2 (post-cleanup re-review)
Five parallel reviewers re-ran the same slices after the cleanup. Scores:
**79/64/62/68/71 (mean 68.8)** vs Pass 1's 68/57/79/71/64 (mean 67.8) — the
mechanical fixes held in every slice (0 self-links, 0 annotation strings, 0
dead/truncated links, 0 sub-320 files, factual fixes verified correct), but
the score barely moved because the deliberately-unfixed classes dominate the
remaining defect surface and two cleanup gaps surfaced.

- **Verified held everywhere**: 0 self-links, 0 annotation strings, 0
  unclosed links, 0 dead README links, 0 files under 320 words, syntheses
  `type` correct, all 7 factual fixes correct (WCAG ratios recomputed and
  matching, dom-clobbering vectors real, gpu driver wording, calibration
  direction, dp-vs-px, anr-diagnostics, org-mode).
- **Cleanup gaps found and fixed after the pass**: the "fixed syntheses
  trailer" had only been removed from bare lines — 233 files still carried
  the two-link boilerplate with descriptor suffixes ("how stubs grow into
  full articles in mykb" / "the curation loop this stub belongs to");
  another 464 lines removed. Also fixed: `compositions/fencing-tokens.md`
  wrong-page link, stale display labels after the clickhouse rename,
  `frontend-frameworks/react-ecosystem.md` fabricated "dashboard is a React
  SPA" claim (the dashboard is vanilla JS), and 3 files whose Related
  sections had been emptied now have topical links.
- **Remaining (Pass 3 agenda)**: unverifiable "the wiki's X does Y" claims
  (~74/48/61/183 per slice — the largest remaining fabrication risk),
  keyword-matched irrelevant links (55–96 files), near-duplicate clusters
  (8+, incl. a 6-file CSS-unit cluster), orphaned trailing bullets after
  RSIS3-relevance paragraphs (60+14+5 files), padding-to-threshold (most
  files in the 320–360 band), and the templated RSIS3-relevance closer
  (86–99% of files). The 320-word floor holds; the bar has moved to
  provenance and uniqueness.
## Related
- [[wiki/syntheses/stub-promotion-wave-2026-08|Stub Promotion Wave]]
- [[wiki/syntheses/pass3-integration-depth-wave|Pass 3 — Integration & Depth Wave]]
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
