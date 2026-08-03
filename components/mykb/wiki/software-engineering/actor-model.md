---
type: "concept"
title: "Actor Model"
description: "Concurrency via isolated actors that communicate only by asynchronous messages"
tags: ["actor-model", "concurrency", "message-passing", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Actor Model

## Summary

The actor model structures concurrency as isolated actors — private state plus a mailbox — communicating only by asynchronous messages. Erlang/OTP, Akka, and Orleans proved it for fault-tolerant, location-transparent systems; it is the mental model behind many agent and microservice designs.

## Details
- Mechanism: each actor processes messages one at a time (no locks needed internally), owns its state exclusively, and reacts by changing state, sending messages, or spawning actors. Addresses are location-transparent: a message to a remote actor is the same API as a local one, which is why the model scales from threads to clusters.
- Concrete example: Erlang/OTP's gen_server wraps state + callbacks; Akka actors back event-sourced services; a chat room is an actor holding member state, broadcasting join/leave; a supervision tree restarts crashed children with a policy (one-for-one, one-for-all), making failure handling structural rather than try/catch spaghetti.
- Failure modes: message delivery is async and at-least-once in most implementations — duplicates and reordering must be designed for (idempotent handlers, sequence numbers); unbounded mailboxes cause memory pressure and stale-message piles (need backpressure/rate control); blocking calls inside an actor stall its whole mailbox; and debugging distributed actor graphs is harder than linear call stacks.
- Operational tradeoffs: actors give isolation and elasticity at the cost of indirection — you cannot read a linear trace of the system; supervision and delivery guarantees must be explicit. RSIS3 relevance: agents modeled as actors get explicit message handoffs, restart semantics, and backpressure, matching the loop's need for bounded, resumable work.
- RSIS3/mykb relevance: the wiki records actor-style designs for agent runtimes so handoff protocols inherit supervision and delivery discipline.
- Backpressure and mailboxes: bounded mailboxes with drop/block policies keep a slow consumer from unbounded memory growth; choose per-actor mailbox strategy from the workload's tolerance for loss vs latency.
- Distributed case: actor addresses can route across nodes, but network partitions reintroduce delivery ambiguity — design protocols with timeouts, retries, and idempotence rather than assuming the mailbox guarantees.

## Related
- [[wiki/software-engineering/message-passing|Message Passing]]
- [[wiki/software-engineering/shared-nothing|Shared Nothing]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]]
