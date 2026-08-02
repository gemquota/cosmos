---
type: "concept"
title: "Fencing Tokens"
description: "Monotonic tokens that let a resource reject writes from stale lock holders"
tags: ["fencing-tokens", "locks", "distributed-systems", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fencing Tokens

## Summary
A fencing token is a monotonically increasing number issued with each lock grant; the resource rejects any write carrying a token older than the last accepted one. It prevents a slow, stale lock holder from corrupting state after losing its lock.

## Details
- The lock service issues tokens; the resource compares tokens before applying writes.
- Fencing fixes the classic distributed-lock failure: holder pauses past its lease, then writes.
- Without fencing, a lease is a timing hope; with fencing, it is a safety guarantee.
- mykb relevance: wiki publish writes carry fencing tokens from the sync lease service.

## Related
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/lease-based-locks|Fencing Tokens]]
