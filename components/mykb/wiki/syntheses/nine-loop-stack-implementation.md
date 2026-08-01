---
type: synthesis
title: "Nine-Loop Stack Implementation & Dashboard Wiring"
description: "Durable patterns for completing the L1–L9 loop stack (meta-tuners observe target-loop history, not params), outcome-window signal driving in tests, and static snapshot wiring for the dashboard Loops tab"
tags: [synthesis, rsis3, loops, metameta, mmm, dashboard, snapshot, verification]
timestamp: "2026-08-01T00:00:00Z"
status: stable
source: []
---

# Nine-Loop Stack Implementation & Dashboard Wiring

## Context

Completing the RSIS3 nine-loop hierarchy: L8 (Meta-Meta) tunes L5 strategy
params and L9 (MMM) tunes L6 identity params, then the whole stack was wired
into the unified dashboard as a static "Loops" tab. Derived from the
L8/L9 + dashboard-wiring pass; rules here are the durable conclusions.

## Patterns

1. **A meta-tuner reads its target loop's recorded *history*, never its live
   params.** L8 detects stagnation/volatility from L5's generation-fitness
   history; L9 detects oscillation/stall from L6's accepted-tuning history.
   This forces every tunable loop to record an `accepted`-flagged history in
   its own state file (L5 needed a `history` feed added — it previously kept
   only `generation`/`population`). Signal vocabulary stays small and
   monotonic: raise/shrink/widen/narrow, each clamped to registry bounds.

2. **Ownership is a compile-time registry, not a convention.** Each +3 target
   has a `{L}N_TUNABLES` dict in `config.py` (min, max, attr path, kind) and
   a `state_path` on its config dataclass. `_apply_tuned_state` iterates the
   registry + state file per loop, so adding a loop = one registry entry,
   one config block, one injection block. No two loops share a write key.

3. **Outcome-window ratio is insertion-ordered and windowed.** 
   `aggregate_outcomes` uses `get_insights(limit=window)`, which returns the
   *last N nodes* — with fewer than `window` nodes the ratio is global; past
   it, a sliding window. Driving a signal in tests therefore requires a
   move-the-ratio driver that always adds in the target direction
   (applied→high, rejected→low), never branching on the current ratio, or
   it will oscillate around the band edge forever.

4. **Static snapshot with graceful never-run defaults.** `loops.json` is
   generated from `.rsis` state files + telemetry jsonl (`l{n}_start` runs,
   last `l{n}_complete` timestamp), falling back to config defaults when a
   loop never ran. `--check` validates structure only (ids L0–L9 + required
   keys) and never rewrites — same rule as `files.json`.

5. **Every new dashboard tab is a plain tab until it needs an iframe.** The
   Loops tab needed no lazy-load special-casing: one button with
   `data-t`/`data-tt`, one `#b-loops` body, one `loadLoops()` + `getTabInfo`
   entry; the generic `sw()`/hash machinery covers it. Iframes (MyKB/SPACE)
   are the exception, not the rule.

6. **jsdom harnesses need a real embedded HTTP server.** A fake origin
   (`http://x`) cannot resolve the page's relative `config.js`/`app.js`, so
   `sw` never exists and every tab click throws. Serve the repo root on
   `localhost:<port>` and use the same origin for the JSDOM URL.

## Related

- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]]
- [[wiki/syntheses/nested-loop-graph-and-zoom-fix|Nested-Loop Graph & Zoom Fix]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Dashboard & MyKB Integration Patterns]]
- [[wiki/index|Wiki Index]]
