---
type: "concept"
title: "Fencing Tokens"
description: "Monotonic tokens that let a resource reject writes from stale lock holders"
tags: ["fencing-tokens", "locks", "distributed-systems", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Fencing Tokens

## Summary

A fencing token is a monotonically increasing number issued with each lock grant; the resource rejects any write carrying a token older than the last accepted one. It converts a distributed lock from a timing hope into a safety guarantee.

## Details
- Mechanism: the lock service issues tokens on grant; every write carries its token; the resource (or storage layer) compares incoming tokens against the last accepted one and rejects stale ones. Fencing fixes the classic distributed-lock failure: a holder pauses past its lease, loses the lock, then wakes and writes — without fencing, its stale write corrupts state; with fencing, the resource rejects it.
- Concrete example: a wiki sync lease grants token 41 to writer A and token 42 to writer B after A pauses; A resumes and writes with token 41 — the store rejects it because 42 was accepted; the same pattern protects queue claimers (a job that loses its lease cannot double-process) and leader-elected writers.
- Failure modes: fencing without enforcement — the resource must check tokens atomically, or the guarantee evaporates; tokens from different lock-service instances (need a monotonic source, e.g. a database sequence); clock-based "fences" that drift; and rejecting token check in some paths while other writers bypass it (check every write).
- Operational tradeoffs: fencing trades a token-issuing service and per-write checks for real mutual exclusion; it does not remove the need for idempotency (a stale write rejected is fine, but retries still need dedup); the discipline is issuing tokens from a monotonic source and checking at the storage boundary.
- RSIS3/mykb relevance: wiki publish writes carry fencing tokens from the sync lease service, so concurrent loop sessions cannot clobber each other's commits.
- Token hygiene: persist the last-accepted token durably and atomically; a lost high-water mark reopens the exact race fencing was meant to close.
- Lease interplay: fencing protects the write side; pair it with lease expiry so a crashed holder stops being issued tokens at all.

## Related
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
