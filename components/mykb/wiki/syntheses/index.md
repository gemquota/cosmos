---
type: "index"
title: "Syntheses Index"
description: "Listing of the syntheses/ folder (12 pages)."
tags: ["index"]
timestamp: "2026-08-02T00:00:00Z"
---

# Syntheses

Part of [[wiki/index|Wiki Index]]. 12 pages.

- [[wiki/syntheses/acquisition-pass-snapshot-ordering|Acquisition Passes & Snapshot Ordering]] — Durable rules for multi-worker acquisition rounds: stage untracked notes before regenerating files.json (it counts tracked files only), generators are idempotent and safe to re-run, and threshold buckets move predictably because fulls are capped at 400 words
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]] — Durable engineering patterns for the static-hosted dashboard↔wiki integration: lazy iframes, bounded client-side search, repo-relative snapshots, read-only validation, verification-first changes
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — Open threads on claims, sources, and version history so syntheses stay auditable
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow: Open Threads]] — Open threads on how captures become curated concepts, sources, and syntheses
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — Integrating multiple sources or concepts into a coherent new conclusion, framework, or insight
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|MyKB Acquisition/Curation Pass & RSIS3 Usage-Practice Enforcement]] — Durable rules for acquiring concept notes into MyKB, curating hash-named junk entity pages, and enforcing RSIS3 workspace hygiene with check-practices
- [[wiki/syntheses/nested-loop-graph-and-zoom-fix|Nested-Loop Graph & Zoom Direction Fix]] — Durable patterns for the interactive Ω graphs: viewBox-width zoom inversion (f>1 zooms in), re-projecting only the loop family onto concentric rings at the semantic centroid, and keeping generator scripts + index cards in sync
- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation & Dashboard Wiring]] — Durable patterns for completing the L1–L9 loop stack (meta-tuners observe target-loop history, not params), outcome-window signal driving in tests, and static snapshot wiring for the dashboard Loops tab
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — Durable rules for running multi-agent knowledge-acquisition passes: a gated define→confirm→generate flow with programmatic uniqueness checks, write-immediately batching to survive silent writer stalls, and independent post-verification instead of trusting agent self-reports
- [[wiki/syntheses/weekly-review|Weekly Review]]
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub Architecture & Snapshot Hygiene]] — Durable patterns for the MyKB stats hub: one generator emitting embedded JSON plus a self-contained Chart.js page, graceful degradation when the CDN is unavailable, and the snapshot-regeneration pipeline (graph → files.json → --check) that must run after every wiki change
