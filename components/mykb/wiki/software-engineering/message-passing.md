---
type: "concept"
title: "Message Passing"
description: "Communicating between concurrent units by sending data instead of sharing it"
tags: ["message-passing", "concurrency", "communication", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Message Passing

## Summary
Message passing exchanges data between threads, processes, or services without shared mutable state — the unit of communication is the message. It underlies actor systems, channels (Go), and distributed queues, and it simplifies reasoning about concurrency.

## Details
- Channels (Go) provide typed, synchronous or buffered message flow between goroutines.
- Copy-on-send or ownership transfer prevents accidental sharing; immutability makes copies cheap.
- Decide delivery semantics explicitly: at-most-once, at-least-once, exactly-once claims.
- mykb relevance: agent-to-agent handoffs are cleaner as messages than as shared state.

## Related
- [[wiki/software-engineering/actor-model|Actor Model]]
- [[wiki/software-engineering/shared-nothing|Shared Nothing]]
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/software-engineering/actor-model|Message Passing]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
