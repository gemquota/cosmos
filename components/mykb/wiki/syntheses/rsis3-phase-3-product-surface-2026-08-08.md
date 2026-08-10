---
type: "synthesis"
title: "RSIS3 Phase 3 — product surface (bridge sessions, memory loop, native embed)"
description: "Durable rules for the product-grade bridge: envelope-shaped session archives, chat memory distillation, shared bridge.js widget, token auth, hosting layout — Phase 3 of the multi-phase roadmap (completes tier T3)"
tags: ["rsis3", "bridge", "phase-3", "t3", "sessions", "chat-memory", "embed", "auth"]
timestamp: "2026-08-08T16:55:00Z"
status: "growing"
---

# RSIS3 Phase 3 — product surface (completes T3)

Phase 3 turned the bridge from a localhost demo into a real web product.
Durable patterns and rules for future work.

## Conversation persistence

- Every chat turn appends two envelope-shaped `exchange` records
  (`spec: cosmos-envelope/1`, `kind: exchange`, role/content/artifacts/
  model/llm) to `rack/bridge/sessions/<id>.jsonl` — one per user and
  assistant turn, in order.
- `GET /api/sessions` lists sessions (id, created, updated, count,
  preview); `GET /api/sessions/:id` resumes one as a message array.
- Client keeps `session_id` in `localStorage` (`cosmos.bridge.session`)
  and restores history on reload — reload-mid-conversation resume is the
  T3 exit criterion, and it holds.
- Session ids validate against `^[A-Za-z0-9_-]{1,128}$` and are
  basename-sanitized before touching the filesystem.

## Chat memory loop (T1 durable input)

- When a session reaches `RSIS_BRIDGE_MEMORY_N` (default 6) assistant
  turns, the bridge distills it into an OKF synthesis note
  (`rsis3-bridge-session-<id>.md` in MyKB syntheses) — one bullet per
  exchange, truncated to 320 chars, with artifact names.
- Notes are write-once (`flag: 'wx'`) so concurrent/later turns never
  duplicate or clobber a distillation.

## Native embed

- The chat surface lives in `dashboard/bridge.js` as
  `window.initCosmosBridge(root, { api, token })` — one widget, two
  hosts: `bridge.html` is a thin shell, and the unified dashboard mounts
  it directly (no iframe) in the Bridge tab.
- Widget instance-scopes every DOM id (`cb0-…`, `cb1-…`) so multiple
  mounts can coexist; the module injects its stylesheet once.

## Auth & hosting

- `RSIS_BRIDGE_TOKEN` gates every `/api/*` route (bearer header, or
  `?token=` for SSE/EventSource which cannot set headers); `/health` and
  the static shell stay public for probes.
- Hosting split: static dashboard (GitHub Pages / Vercel) + hosted bridge
  process holding `GEMINI_API_KEY`; `BRIDGE_URL`/`BRIDGE_TOKEN` in
  `dashboard/config.js`; documented in `vercel-deploy/README.md`.
- Origin guard remains: non-localhost origins need
  `RSIS_BRIDGE_ALLOW_ORIGIN` even with token auth.

## Verification rules

- Phase 3 matrix lives in `tests/test_bridge.py` (persist/resume, list,
  404, memory distillation + idempotency, token auth) — 22 bridge cases,
  191 pytest total, 8 envelope unit tests.

## Related

- [[wiki/syntheses/rsis3-phase-2-envelope-hardening-2026-08-08|RSIS3 Phase 2 — envelope hardening]]
- [[wiki/syntheses/rsis3-goal-stack-output-communicate-bridge-2026-08-08|RSIS3 goal stack — Output → Communicate → Wrap → Bridge]]
