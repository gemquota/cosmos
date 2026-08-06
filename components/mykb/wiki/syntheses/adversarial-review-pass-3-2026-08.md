---
type: synthesis
title: "Adversarial Review Pass 3 — Claims Grounding, Link Hygiene & Near-Duplicate Merges (2026-08)"
description: "Pass 3 of the adversarial review cycle rewrote every unverifiable 'the wiki's X does Y' operational claim into design-intent policy language, removed 222 keyword-matched hub links and 22 dead archive links, fixed 59 orphaned trailing bullets, and merged seven near-duplicate article pairs to canonical slugs"
tags: [synthesis, mykb, adversarial-review, claims-grounding, link-hygiene, near-duplicate, merge, knowledge-graph, parallel-agents]
timestamp: "2026-08-03T18:00:00Z"
status: stable
source: []
---
# Adversarial Review Pass 3 — Claims Grounding, Link Hygiene & Merges

## Context
Pass 1 and Pass 2 of the adversarial review cycle (scores 67.8 → 68.8)
verified the mechanical invariants of the 1,098-file promotion wave but left
the deliberately-deferred defect surface: unverifiable operational claims
about the wiki's infrastructure, keyword-matched irrelevant hub links,
near-duplicate article clusters, and orphaned trailing bullets. Pass 3 closed
those classes before the next scoring review.

## Findings
- The dominant fabrication risk was the "RSIS3/mykb relevance" claim sentence
  shape ("the wiki's static hosting serves over HTTP/2 with h3 at the edge",
  "the wiki's batch experiments run on preemptible capacity", "the wiki's
  domains are signed with automated key rollover", "the dashboard tracks CLS
  as a rack pulse"). None of these were grounded in repo config or telemetry.
- Search-related claims overstated the real implementation: `search_fusion.py`
  fuses TF-IDF + BM25 with reciprocal rank fusion; neural embeddings and
  cross-encoder reranking are a documented design option, not current fact.
- Eight hub pages accumulated keyword-matched inbound links from off-topic
  files; a per-target keep-if-topic gate was needed rather than blanket
  removal, because most os-shell and web-platform links were genuinely topical.
- Seven near-duplicate pairs (including two ~90-95% identical pairs) degraded
  retrieval precision: an agent pulling "CLS" or "preview environments" got
  2-6 near-identical pages.

## Resolution
- **Claims**: rewrote ~126 claim sentences across ~145 files to design-intent
  language ("would…", "a documented policy…", "the standing rule is…"),
  preserving every ``Wikilink`]]`, frontmatter field, and adjacent sentence.
  Content-description claims (the wiki's pages document X) and generic
  concept statements were deliberately left unchanged. No file dropped below
  the 320-word floor; 13 dipped by link removals were topped back up.
- **Links**: removed 222 keyword-matched hub links (kubernetes-control-plane
  86, observability-pillars 65, storage-systems 44, ospf-protocols 27) and 22
  dead session-artifact links; retargeted or removed six confirmed misfires.
- **Merges**: folded `preview-environments` → `ephemeral-environments`,
  `runbooks-and-playbooks` → `runbooks`, `srgb-vs-p3` → `color-spaces`,
  `cls-avoidance` → `cumulative-layout-shift`,
  `path-resolution-and-symlinks` → `path-resolution`, `dvh-svh` → `vw-vh`;
  retitled `release-engineering-trains` → `release-engineering`. Unique
  content was folded into the canonical pages and all inbound links
  retargeted; losers were archived.
- **Structure**: 59 files with headerless trailing bullets received a
  `## Practice` section.

## Related
- [[wiki/syntheses/adversarial-review-pass-1-2026-08|Adversarial Review Pass 1]]
- [[wiki/syntheses/stub-promotion-wave-2026-08|Stub Promotion Wave]]
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub]]
- [[wiki/concepts/full-article-ratio|Full Article Ratio]]
- [[wiki/tooling/link-fix-automation|Link Fix Automation]]
