---
type: synthesis
title: "Parallel Agent Acquisition (5×100) & Writer Reliability"
description: "Durable rules for running multi-agent knowledge-acquisition passes: a gated define→confirm→generate flow with programmatic uniqueness checks, write-immediately batching to survive silent writer stalls, and independent post-verification instead of trusting agent self-reports"
tags: [synthesis, mykb, acquisition, agents, parallelism, verification]
timestamp: "2026-08-02T00:10:00Z"
status: stable
source: []
---

# Parallel Agent Acquisition (5×100) & Writer Reliability

## Context

Pass 3 ran five parallel acquisition agents (data-storage, api-protocols,
testing, frontend, os-shell), each generating 100 unique full articles (500
total), gated through a define → confirm → generate flow, then verified and
deployed. Rules below are the durable conclusions.

## Patterns

1. **Gate the pass: define first, confirm uniqueness, then generate.** Five
   planning agents each return 100 slugs (kebab-case, `area/slug`); the
   orchestrator checks programmatically — 500 unique, no intra-agent or
   cross-agent duplicates, zero collisions with the existing wiki — before
   any writer runs. Writers receive the confirmed list, so generation cannot
   drift from the plan.

2. **Writer agents can stall silently mid-batch.** Two of five writers
   stopped after 10 and 60 files respectively with no error and no summary
   (a third errored at the provider layer). Mitigations that worked:
   instruct writers to write one file at a time immediately after composing
   (never batch-hold content), check disk growth every N files, retry a
   failed tool call once, and never stop until the expected file count is
   reached. A stalled writer is replaced by a fresh worker that skips
   existing slugs and finishes the remainder.

3. **Verify independently; agent self-reports are not evidence.** The
   orchestrator re-runs the checks itself: expected 500 slugs all present,
   frontmatter keys present, body 150–400 words, and every `[[wiki/...]]`
   target resolving against the existing-slug inventory or the pass list.
   Pass 3: 500/500 present, 500/500 frontmatter, 500/500 word counts, 0
   broken links.

4. **Disjoint write scopes make parallelism safe.** Each writer owns exactly
   one area directory; no two writers touch the same path, so no merge
   conflicts and no cross-agent coordination. Cross-area wikilinks resolve
   because targets exist either before the pass or within the confirmed list.

5. **Close completed agents promptly.** Agent slots are limited; finished
   planners/writers must be closed before spawning the next wave (five
   planners blocked the writer wave until closed).

## Consequences

- Pass 3 added 500 full articles (150–400w each) across five domains: wiki
  grew 2,688 → 3,188 content files.
- Pipeline order after generation: `build_index_pages.py` → `build_graph.py`
  → `build_stats.py` → stage → `gen-static-data.py` + `--check` → `okf
  render` → synthesis/log → commit → full-tree deploy to `gh-pages`.
