---
type: "synthesis"
title: "RSIS3 Phase 2 — envelope hardening (cosmos-envelope/1 v1.1)"
description: "Durable rules for the hardened bridge envelope: typed structured artifacts, multimodal handling, server-side caps, explicit ref allowlist, rate limit, origin guard, NDJSON streaming — Phase 2 of the multi-phase roadmap (completes tier T2)"
tags: ["rsis3", "bridge", "envelope", "t2", "phase-2", "multimodal", "security", "streaming"]
timestamp: "2026-08-08T14:45:00Z"
status: "growing"
---

# RSIS3 Phase 2 — envelope hardening (cosmos-envelope/1 v1.1)

Phase 2 of the multi-phase development roadmap completed tier T2 (dense,
typed, multimodal, bounded, safe messaging). Durable patterns and rules for
future bridge work — not session trivia.

## Envelope contract (cosmos-envelope/1, additive-only until spec v2)

- Version bumps must stay additive: new fields optional; keep
  `spec: cosmos-envelope/1` and record changes in the `CHANGELOG` block of
  `rack/bridge/envelope.mjs` (`ENVELOPE_VERSION`).
- Text artifacts stay inline previews (8 KB cap); JSON/YAML/TOML artifacts
  are parsed structurally and passed as machine-readable `schema` blocks
  (`{keys, types, depth}`), never raw strings.
- Audio goes to the LLM as `inline_data` when online; PDFs are text-
  extracted (FlateDecode with raw-stream fallback) into previews; video is
  rejected with an explicit `unsupported` status — never silently dropped.
- Server-side caps are the source of truth, not the UI: text preview
  8 KB, media 4 MB, request body 6 MB (413 beyond body cap).

## Ref traversal is allowlist-driven

- `rack/bridge/allowlist.json` is the single source of truth: `roots`
  (repo-relative) plus root-relative `deny` prefixes; absent file defaults
  to root+mykb containment.
- Deny prefixes must be checked against BOTH the raw ref (root-relative)
  and the repo-relative resolved path — otherwise a denied path can fall
  through to a second root and resolve (this exact bug shipped mid-Phase 2
  and is pinned by tests).

## Bridge server rules

- `/api/chat` rate limit is an in-memory bucket per client
  (`RSIS_BRIDGE_RATE_LIMIT` req/min, default 20) with `Retry-After` on
  429; no new dependencies.
- Origin guard: localhost (or no `Origin`) allowed; anything else needs
  `RSIS_BRIDGE_ALLOW_ORIGIN` (comma-separated); applies to preflight.
- `GEMINI_API_KEY` lives server-side only; missing key → deterministic
  offline-fallback envelope so the UI still works.
- Streaming contract: `Accept: application/x-ndjson` (or `stream: true`)
  yields `meta` → `delta`* → `done` frames from
  `:streamGenerateContent?alt=sse`; legacy JSON reply unchanged.

## Verification rules

- Phase 2 matrix: `tests/test_bridge.py` (HTTP: traversal, allowlist deny,
  oversized media, 413, missing file, schema, text+image round-trip,
  NDJSON streaming, audio/PDF/video, origin guard, rate limit) +
  `tests/bridge-envelope.test.mjs` (envelope units).
- Full suite stays green: `python3 -m pytest tests/` and
  `node --test tests/bridge-envelope.test.mjs`.

## Related

- [[wiki/syntheses/rsis3-goal-stack-output-communicate-bridge-2026-08-08|RSIS3 goal stack — Output → Communicate → Wrap → Bridge]]
- [[wiki/syntheses/rsis3-multi-series-7-cycle-run-2026-08-08|RSIS3 multi-series 7-cycle run]]
- [[wiki/syntheses/rsis3-l3-cycle-77-cross-session-memory-consolidation-2026-08-08|RSIS3 L3 cycle 77 — cross-session memory consolidation]]
