---
type: "concept"
title: "Last-Write-Wins"
description: "The conflict policy where the most recent write simply replaces older ones"
tags: ["lww", "conflicts", "sync", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Last-Write-Wins

## Summary
Last-write-wins (LWW) resolves conflicts by timestamp: the newest write wins and older writes are discarded. It is simple, cheap, and convergent — and it silently loses data whenever clocks or ordering lie.

## Details
- LWW needs reliable timestamps: clock skew and reordered delivery break it.
- Use it when writes are idempotent, monotonic, or losses are acceptable.
- LWW is the default in many distributed stores (DynamoDB, Redis) — know what you accept.
- mykb relevance: counter-like wiki metadata (view counts) tolerates LWW; article bodies do not.

## Related
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/compositions/vector-clocks|Vector Clocks]]
- [[wiki/compositions/lamport-clocks|Lamport Clocks]]
- [[wiki/compositions/sync-engines|Sync Engines]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
