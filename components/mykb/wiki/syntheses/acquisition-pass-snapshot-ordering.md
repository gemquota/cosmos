---
type: synthesis
title: "Acquisition Passes & Snapshot Ordering"
description: "Durable rules for multi-worker acquisition rounds: stage untracked notes before regenerating files.json (it counts tracked files only), generators are idempotent and safe to re-run, and threshold buckets move predictably because fulls are capped at 400 words"
tags: [synthesis, mykb, acquisition, curation, snapshots, pipeline]
timestamp: "2026-08-01T19:10:00Z"
status: stable
source: []
---

# Acquisition Passes & Snapshot Ordering

## Context

Second acquisition round (Pass 2): four parallel research workers (specs
E–H) added 400 articles (100 full + 300 stubs) across cloud-infra,
software-engineering, mobile/android, and security/identity clusters, then
the stats hub + deploy pipeline was re-run over the expanded wiki. Rules
below are the durable conclusions from running the full chain twice.

## Patterns

1. **Regenerate `files.json` after staging, not before.** `gen-static-data.py`
   lists git-tracked files only. An acquisition round leaves hundreds of
   untracked notes; regenerating before `git add` silently omits them and
   ships a stale inventory. Order: `git add` the notes → regenerate
   `files.json`/`ecosystem.json` → `--check` → commit atomically with the
   notes.

2. **Generators are idempotent — re-run them at any point in the chain.**
   `build_graph.py` and `build_stats.py` walk the tree on disk, so they are
   unaffected by staging state and can be re-run after the synthesis note is
   added without invalidating earlier output. `okf render` (okf-graph.html)
   bakes the bundle, so it must come last, after all notes exist.

3. **Threshold buckets move predictably.** Full articles are capped at
   150–400 words, so an acquisition pass adds to the 300+ bucket but not to
   400+/500+ unless genuinely long notes land. After Pass 2: 300+ 26 → 54,
   400+ and 500+ unchanged at 14/11 — a useful signal for validating a round
   (a 500+ jump means real long-form content arrived).

4. **Parallel workers must not collide on slugs or directories.** Pass 2
   kept four clusters disjoint (no slug collisions, zero broken links after a
   14-link cross-directory review). Verify with the file inventory + link
   check before committing, not after deploy.

## Consequences

- Full pipeline run order: stage notes → `build_graph.py` → `build_stats.py`
  → `gen-static-data.py` → `--check` → `okf render` → commit → deploy.
- Post-Pass-2 wiki: 2,687 content files, 2,687 graph nodes / 15,820 edges,
  14,525 wikilinks, 54 notes at 300+ words.
