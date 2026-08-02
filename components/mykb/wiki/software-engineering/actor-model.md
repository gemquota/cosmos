---
type: "concept"
title: "Actor Model"
description: "Concurrency via isolated actors that communicate only by asynchronous messages"
tags: ["actor-model", "concurrency", "message-passing", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Actor Model

## Summary
The actor model structures a system as isolated actors — each with private state and a mailbox — that interact only by sending messages. Erlang/OTP, Akka, and Orleans popularized it for fault-tolerant, location-transparent concurrency.

## Details
- Actors process one message at a time, so no locks are needed inside an actor.
- Supervision trees make failure handling structural: a supervisor restarts or escalates failing children.
- Message delivery is asynchronous and often at-least-once — design for duplicates and ordering gaps.
- RSIS3 relevance: each agent could be an actor with its own mailbox, making handoffs explicit messages.

## Related
- [[wiki/software-engineering/message-passing|Message Passing]]
- [[wiki/software-engineering/shared-nothing|Shared Nothing]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]]
