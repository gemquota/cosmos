---
type: synthesis
title: "Stub Promotion Wave — 1,098 stubs → growing (2026-08)"
description: "Five worker waves promoted the longest-standing stubs (≥120 body words) to full 320+ word articles, pushing the 300+/400+/500+ tiers to 1,670/542/152 and holding the knowledge graph at zero new broken links"
tags: [synthesis, mykb, acquisition, promotion, stub, knowledge-graph, parallel-agents, stats-hub]
timestamp: "2026-08-03T12:00:00Z"
status: stable
source: []
---
# Stub Promotion Wave — 1,098 stubs → growing

## Context
Following Pass 3's integration wave (8×400), the bundle carried 3,150 stub
articles — many already holding 100–150 body words of real content. This wave
promoted the most substantive stubs to full articles: any stub with **≥120
body words** (frontmatter excluded) was upgraded in place to a **320+ word**
article with `status: growing`.

## What landed
- **1,098 stubs promoted** to `status: growing` across five worker batches
  (275/275/274/274/31), each file reaching a minimum of 320 body words
  (median 391, max 612).
- **Tiers moved to 1,670/542/152** for 300+/400+/500+ body words (from
  572/18/5) — the first wave that substantially populated the upper tiers.
- Bundle now: **5,341 files, ~1.19M words, 30,720 wikilinks**, 3,104 growing /
  1,779 stub articles.
- **Zero new broken links**: full link-integrity diff against the pre-wave
  baseline shows no change in unresolved-link profile; the 7 flagged wiki
  links are intentional doc-example syntax (wikilink placeholders, `:alpha:`
  character-class examples, file-link templates), not real edges.
- **Worker link-preservation enforced**: 9 concepts files had valid
  `[[wikilinks]]` stripped by a worker; all were restored into `## Related`
  sections with ``Display`Display]]` targets verified to exist on disk.

## Process notes
- **Rate limit ceiling reconfirmed**: with 4 concurrent workers, one hit the
  provider 429 ceiling; the leftover 31 files were finished by a fifth worker
  (batch5). Ceiling for this provider remains **3–4 concurrent writers**.
- **Body-word metric**: promotion used the same body-only word count that
  `build_stats.py` uses (frontmatter stripped) so tier numbers stay
  consistent between workers and the stats hub.
- **Quality gates per file**: `status: "stub"` → `status: "growing"`, ≥320
  body words, all pre-existing `[[wikilinks]]` preserved, new links only to
  on-disk targets.

## Follow-up
- Remaining 1,779 stubs are mostly <120 body words; next wave can target the
  ≥100-word band or proceed area-by-area from the top.
- `log.md` updated, snapshots regenerated (stats.html, graph.json,
  okf-graph.html, files.json), audit refreshed.

## Related
- [[wiki/syntheses/pass3-integration-depth-wave|Pass 3 — Integration & Depth Wave]]
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition]]
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|MyKB Acquisition, Curation & Practices]]
