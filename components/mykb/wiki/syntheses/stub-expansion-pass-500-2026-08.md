---
type: synthesis
title: "500-Stub Expansion Pass (2026-08-03)"
description: "Five parallel workers promoted 500 of the smallest wiki stubs to full articles, followed by a junk-entity archival, -10 name cleanup, and categorization moves"
tags: [synthesis, stub-expansion, parallel-agents, categorization, cleanup, 2026-08]
timestamp: "2026-08-03T13:30:00Z"
status: stable
source: []
---
# 500-Stub Expansion Pass (2026-08-03)

## Context
The wiki carried ~3,850 stub/growing files, most under 320 words. This pass promoted the 500 smallest stubs (≤85 words) to full articles using five parallel workers (100 files each), then reviewed the remaining stubs for deletion candidates and cleaned up categorization.

## What ran
- **Selection**: 500 smallest stubs across 21 areas, split into 5 disjoint,
  area-coherent slices; every file verified to exist and be unique per slice.
- **Workers**: five parallel agents each rewrote 100 files to ≥320 body words
  (target 340-460) with the wiki's standard structure — `# Title`, `## Summary`,
  `## Details` (bolded-lead-in bullets), `## Related` (resolvable wikilinks).
  All surviving files passed the word floor; one worker rate-limited at 78/100
  and the remainder were completed inline.
- **Deletion review**: 21 junk entities archived — auto-captured opaque
  identifiers and template-only acronym entities that added noise, not
  knowledge. All inbound links stripped.
- **Categorization**: `mcp` moved to api-protocols, `skills` moved to
  llm-agents, duplicate `rest` archived (canonical rest-apis), 61 `*-10`
  collision-suffixed files renamed to canonical names with links retargeted,
  172 stale template descriptions replaced with real summaries.

## Outcomes
- 300+/400+/500+ word tiers: 1,695/468/50 → **2,174/483/51**.
- Total words: 1,170,691 → **1,305,666** (+135k).
- Stubs remaining: 3,850 → **3,348** (auditor now lists 3,326).
- Graph: 5,396 nodes / 35,454 edges; OKF graph 6,830 concepts; link check clean.

## Lessons for future passes
- **Disjoint slices by area prevent worker conflicts** and make verification
  trivial; keep slices to files that are genuine stubs, not template junk —
  pre-filter template/acronym entities before selecting.
- **Provider rate limits** can kill a worker mid-pass; keep slices small enough
  that remaining work can be finished inline, and verify word counts
  independently afterward (worker self-reports are not enough).
- **Frontmatter is fragile**: programmatic description edits must rewrite the
  whole line (not splice inside it), and every pass should end with
  `okf validate` to catch YAML breakage.
- **Naming debt compounds**: `*-10` collision suffixes and template
  descriptions were cheap to fix in bulk once identified; running the
  template-description scan before stub selection avoids expanding noise.

## Related
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop/Graph Engineering Wave]] — the prior ingest synthesis
- [[wiki/llm-agents/skills|Skills]] — moved note
- [[wiki/api-protocols/mcp|MCP]] — moved note
- [[wiki/api-protocols/rest-apis|REST APIs]] — canonical rest note
