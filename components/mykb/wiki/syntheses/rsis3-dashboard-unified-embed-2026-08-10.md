---
type: "synthesis"
title: "RSIS3 unified dashboard — live-telemetry rebuild & unified embed"
description: "Root-cause patterns for dashboard regressions (stale static payloads, missing renderer IDs, uncalled init) and the ?embed=cosmos contract for unifying separate codebases into one cohesive web app"
tags: ["synthesis", "dashboard", "rsis3", "mykb", "space", "telemetry", "embed", "regression"]
timestamp: "2026-08-10T07:57:19Z"
status: "growing"
---

# RSIS3 unified dashboard — live-telemetry rebuild & unified embed

Patterns distilled from the 2026-08-10 dashboard regression fix and the unified-embed
pass over MyKB/SPACE/RSIS3.

## Dashboard regression root causes (check these first when tabs go blank)
- **Stale static payload**: `rack/pulses/dashboard-data.json` is derived data. If the
  producing pipeline dies, the dashboard silently renders old data. Always rebuild from
  live sources (`.rsis/telemetry/*.jsonl`) with `gen-static-data.py` — never hand-edit.
- **Missing renderer IDs**: `index.html` must expose every DOM id `app.js` reads
  (`cpf/cl/cc/gl/gc/gs/gf/pl/...`). A single `null.value` throw in one renderer kills
  all subsequent renders; guard or hoist failures so one tab can't blank the app.
- **Uncalled init**: an overview updater that exists but is never wired into
  `renderAll()` shows `–`. Every render entry point belongs in one call graph.

## Unified embed contract (`?embed=cosmos`)
Separate codebases, one visual system:
- MyKB `index.html`/`okf-graph.html` and SPACE `web/index.html` accept
  `?embed=cosmos` and force the dashboard palette (#0f172a bg, #0b1120 sidebar,
  indigo #6366f1) without touching the parent app.
- Dashboard iframes load with `data-src` (lazy) + `?embed=cosmos`, bg `#0f172a` so no
  white flash; theme is owned by the embedded app, not inherited.

## Related
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]]
- [[wiki/syntheses/rsis3-epoch-1-findings-resolution-2026-08-10|Epoch 1 findings resolution]]
- [[wiki/syntheses/cosmos-dashboard-tab-unification-2026-08-11|Cosmos dashboard tab unification — SPACE/MyKB/RSIS3 shell + KG lite mode]]
