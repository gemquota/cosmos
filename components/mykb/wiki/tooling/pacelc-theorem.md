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
- For the mykb bundle, the wiki would serve reads at low latency with bounded staleness, while writes would stay strongly consistent.
- Worked example — the wiki search would return results with one-minute staleness at 50ms latency; article identity writes would stay strongly consistent at higher latency — the PACELC trade made per use case.

Worked example — the wiki search would return results with one-minute staleness at 50ms latency; article identity writes would stay strongly consistent at higher latency — the PACELC trade made per use case.

- Per-operation design: hot read paths may accept bounded staleness while identity writes stay strongly consistent; the choice would be documented per data class rather than applied uniformly.
- Testing the trade: the standing rule is to measure staleness and latency under load, because a configuration that meets the target in isolation can miss it in production.
- Decision recording: the per-data-class choice would be recorded next to the data class definition, so future maintainers can see the trade that was made and why.
- Review trigger: the choice should be revisited when access patterns change, because a model chosen for one workload can become the wrong trade for the next.
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
