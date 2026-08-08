---
type: synthesis
title: "T2 Dense Envelope & Multi-Phase Roadmap for the COSMOS Bridge"
description: "Durable patterns for dense multimodal messaging between Cosmos components and the LLM bridge: the cosmos-envelope/1 wire shape, artifact ref resolution with root-boundary traversal protection, dynamic (live-state) snapshots instead of static regeneration, and the four-phase development roadmap sequence that completes tiers T1-T3 plus ops maturity"
tags: [synthesis, rsis3, bridge, llm, envelope, dashboard, roadmap, goals]
timestamp: "2026-08-08T12:50:00Z"
status: active
source: []
---

# T2 Dense Envelope & Multi-Phase Roadmap for the COSMOS Bridge

## Context

Tier 2 (dense multimodal messaging wrappers) of goal-stack-001 required a
canonical wire shape between Cosmos components and the LLM bridge. The
delivered envelope (`rack/bridge/envelope.mjs`, spec `cosmos-envelope/1`)
carries header, text, compact cosmos context, and artifact refs; the bridge
server (`rack/bridge/server.mjs`) resolves those refs server-side — inlining
text into the prompt and passing images to Gemini as `inline_data`. A
four-phase roadmap now sequences the work to completion. These are the
durable conclusions.

## Patterns

1. **The envelope is the contract, not the endpoint.** Every bridge message
   is a `cosmos-envelope/1` object: `spec`, `kind`, `ts`, `sender`, `text`,
   `ctx` (compact snapshot), `artifacts` (refs with mime/size/sha), and
   optional `state`. Clients send dataUrl payloads; the server normalizes
   them to refs. Keep the shape additive when versioning — spec bumps only
   when a change is breaking.

2. **Refs are resolved against roots, never interpolated.** Artifact paths
   must stay inside `ROOT`/`MYKB`: resolve with `path.resolve`, reject
   absolute paths, drive letters, and anything escaping the root prefix.
   Refuse traversal (`../../etc/passwd` → `denied`) even when the request is
   otherwise valid. This is a server-side invariant, not a UI courtesy.

3. **Text inlines, images inline_data, everything else is status.** Text
   artifacts become truncated previews (8 KB) in the prompt; images ≤4 MB
   become Gemini `inline_data`; binaries become `attached` refs without
   content. The chat reply always echoes per-artifact status so the user
   sees what the model actually received. Tiny images (1×1) are rejected by
   the provider — surface that as a status, not a crash.

4. **Dynamic snapshots beat regenerated ones for live surfaces.** Static
   `dashboard-data.json` snapshots drift; the bridge now builds the cosmos
   snapshot on demand from live `.rsis/` state and lists artifact refs
   lazily (sha computed only when inlined) so `/api/cosmos` stays cheap.
   Static regeneration remains for GitHub Pages deployments only.

5. **Roadmap phases complete tiers in order.** Phase 1 (SSE live state
   streaming) completes T1; Phase 2 (envelope hardening: typed artifacts,
   rate limits, allowlist, streaming replies) completes T2; Phase 3
   (persistence, sessions, native embed, auth) completes T3; Phase 4 (cycle
   daemon with lockfile, dynamic snapshot refresh, CI checks, convergence
   handling) wraps ops. Persistence must not precede a stable envelope
   shape — do not reorder Phase 2 and Phase 3.

## Consequences

- The bridge is verified end-to-end: `/api/cosmos` serves ~10 artifact refs,
  ref inlining works, traversal is blocked, and Gemini reads real KG images
  (5418 concepts / 36892 links) with `llm=connected`.
- A 3-minute cadence (≈20 cycles/hour) with the parallel CI session is the
  sustainable background mode; the roadmap's Phase 4 lockfile makes it safe
  against double-runs.
- Roadmap: `components/rsis3/docs/multi-phase-development-roadmap.md`
  (Baseline ✅ delivered, Phases 1–4 queued).
