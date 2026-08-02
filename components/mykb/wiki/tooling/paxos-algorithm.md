---
type: "concept"
title: "Paxos Algorithm"
description: "The foundational consensus algorithm for distributed agreement"
tags: ["paxos", "consensus", "distributed-systems", "algorithm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Paxos_(computer_science)", "https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf"]
---

# Paxos Algorithm

## Summary
Paxos is Leslie Lamport's consensus algorithm: proposers, acceptors, and learners reach agreement on a value through two rounds of messages (prepare and accept), tolerating failures as long as a majority of acceptors live. It is the theoretical foundation of nearly every practical consensus system.

## Details
- The classic single-decree Paxos agrees on one value; Multi-Paxos runs it over a log for replicated state machines.
- Safety holds under arbitrary message delay and process failure; liveness needs a distinguished proposer (leader).
- Implementations are famously subtle — bugs hid for years in production systems — which motivated Raft's design.
- Paxos is used (in variants) in Spanner, Chubby, and many replication stacks.
- Understanding Paxos explains Raft: Raft's leader election and log replication are the same ideas made explicit.
- For the mykb bundle, Paxos knowledge informs choices among consensus-based coordination services.
- Worked example — a proposer sends prepare(1); a majority of acceptors promise; the proposer sends accept(1, v); acceptors learn v — the round-trip dance behind every replicated write.

Worked example — a proposer sends prepare(1); a majority of acceptors promise; the proposer sends accept(1, v); acceptors learn v — the round-trip dance behind every replicated write.

## Related
- [[wiki/tooling/raft-algorithm|Raft Algorithm]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/tooling/quorum-reads|Quorum Reads]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/devops-infra/leader-election-and-quorum|Leader Election & Quorum]]
- [[wiki/devops-infra/stateful-application-patterns|Stateful Application Patterns]]
