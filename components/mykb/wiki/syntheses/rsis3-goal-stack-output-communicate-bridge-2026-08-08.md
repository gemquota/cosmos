---
type: "synthesis"
title: "Multitiered goal stack — Output → Communicate → Wrap → Bridge"
description: "Active drives adopted 2026-08-08: output-first cycles, user communication, dense messaging wrappers, web interface bridge to LLM + Cosmos"
tags: ["rsis3", "goal-stack", "drives", "bridge", "llm", "web-ui"]
timestamp: "2026-08-08T11:55:00Z"
status: "active"
---

# Multitiered goal stack — Output → Communicate → Wrap → Bridge

Adopted as the operating goal stack (priority 1, LLM-driven mode). Machine
readable form: `components/rsis3/rack/goals_stack.json` (id `goal-stack-001`).

## Tiers

- **T0 Output** — every cycle produces visible, verifiable output; no silent
  cycles (≥1 committed artifact per cycle, telemetry trace per loop).
- **T1 Communicate** — share internal state, active drives, and future
  planning with the user, in-session and via durable dashboard telemetry.
- **T2 Dense multimodal messaging wrappers** — structured message envelopes
  (text + cosmos context + artifacts + state) between components and the LLM
  bridge.
- **T3 Web interface bridge** — modern, responsive web interface bridging an
  LLM and the Cosmos framework.

## T3 delivered (first pass)

- `components/rsis3/rack/bridge/server.mjs` — Node stdlib-only gateway:
  `GET /api/cosmos` (dense context envelope: KG, strategies, pulses,
  syntheses, drives) and `POST /api/chat` (server-side LLM proxy, key never
  leaves the server). Model `gemini-2.5-flash` via `GEMINI_API_KEY`;
  deterministic offline-fallback envelope when no key.
- `components/rsis3/dashboard/bridge.html` — responsive chat UI matching the
  dashboard design system; cosmos-context toggle; suggested prompts derived
  from the drive stack; markdown-lite rendering.
- Unified dashboard gains a **💬 Bridge tab** (lazy-loaded iframe + offline
  banner) and an **🧭 Active Drives** strip on Overview reading
  `goals_stack.json` (`config.js` gains `BRIDGE_URL` / `GOALS_FILE`).
- Verified: `/api/chat` returns live Gemini replies grounded in the cosmos
  snapshot; offline fallback responds without a key.

## Durable rules

- The API key lives only in the bridge server env — never in client code.
- Context envelopes are the messaging wrapper (tier 2): one fetch returns
  pulses + KG + strategies + syntheses + drives.
- Dashboard tabs stay lazy-loaded and degrade gracefully (offline banner),
  consistent with the MyKB/SPACE iframe pattern.
