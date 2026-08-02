---
type: "concept"
title: "Realtime Collaboration"
description: "CRDTs, operational transforms, and sync protocols for multi-user editing"
tags: ["crdt", "collaboration", "realtime", "sync", "editing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://crdt.tech/", "https://www.yjs.dev/"]
---
# Realtime Collaboration

## Summary
Realtime collaboration lets multiple users edit shared state concurrently. Two main techniques dominate: operational transformation (OT), used by Google Docs-class editors, and CRDTs (conflict-free replicated data types), used by Yjs and Automerge. Both converge divergent edits without a central lock.

## Details
- **CRDTs** — commutative, associative, idempotent merges guarantee convergence; rich-text CRDTs (Yjs) handle text with positions and tombstones.
- **OT** — operations transform against each other server-side; complexity grows with document structure.
- **Sync** — WebSockets/WebRTC carry updates; awareness messages show presence; persistence and history sit underneath.
- **Trade-offs** — CRDTs simplify offline merging but carry metadata overhead; OT fits collaborative editors with server mediation.
- **Worked example** — two wiki editors editing the same note converge via Yjs over WebRTC with a WebSocket fallback.
- **Relevance** — RSIS3's multi-worker knowledge base is a natural fit for CRDT-backed shared notes.
- **Conflict-free design** — CRDT state includes tombstones and version vectors, so sync payloads grow with edit history; periodic compaction and awareness messages bound the metadata overhead.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — adjacent concept in this wiki
- [[wiki/api-protocols/throttling-vs-debouncing|Throttling vs Debouncing]] — adjacent concept in this wiki
- [[wiki/api-protocols/websockets|WebSockets]] — existing coverage
- [[wiki/api-protocols/websocket-broadcast|WebSocket Broadcast]] — existing coverage
- [[wiki/api-protocols/event-driven-apis|Event-Driven APIs]] — existing coverage
