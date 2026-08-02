---
type: "concept"
title: "PACELC Theorem"
description: "If a partition occurs, trade availability and consistency; otherwise trade latency and consistency"
tags: ["pacelc", "cap-theorem", "consistency", "tradeoffs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/CAP_theorem", "https://en.wikipedia.org/wiki/Consistency_model"]
---

# PACELC Theorem

## Summary
PACELC extends the CAP theorem with the normal case: if a Partition occurs, choose Availability or Consistency (CAP); Else, even without partitions, choose Latency or Consistency. It captures the tradeoff that dominates everyday design — how much consistency are you willing to trade for speed?

## Details
- CAP covers the partition case; PACELC makes explicit that the same choice exists in the common, no-partition case.
- Systems like DynamoDB pick availability plus low latency, accepting eventual consistency.
- Systems like Spanner pick consistency, paying latency and coordination even when healthy.
- The trade is per-operation: reads can differ from writes, and hot paths can use weaker models deliberately.
- Operationally: document the choice per data class, and test what the system actually delivers.
- For the mykb bundle, the wiki serves reads at low latency with bounded staleness, while writes stay strongly consistent.
- Worked example — the wiki search returns results with one-minute staleness at 50ms latency; article identity writes stay strongly consistent at higher latency — the PACELC trade made per use case.

Worked example — the wiki search returns results with one-minute staleness at 50ms latency; article identity writes stay strongly consistent at higher latency — the PACELC trade made per use case.

## Related
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/compositions/bounded-staleness|Bounded Staleness]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/compositions/read-your-writes|Read-Your-Writes]]
- [[wiki/devops-infra/isolation-levels|Isolation Levels]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
