---
type: "concept"
title: "Read-Your-Writes"
description: "The guarantee that a client sees its own writes immediately"
tags: ["read-your-writes", "consistency", "replication", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Read-Your-Writes

## Summary
Read-your-writes consistency ensures a client's read reflects its own previous writes — after saving an article, the next read shows the save. It is a session-level guarantee, weaker than global consistency but essential for user trust.

## Details
- Implement by routing session reads to the replica that served the write, or by version checks.
- The guarantee is per-session: another client may still read stale data.
- Replication lag breaks it unless reads pin to the write location.
- mykb relevance: after a wiki edit, the author's next read must show their change.

## Related
- [[wiki/compositions/monotonic-reads|Monotonic Reads]]
- [[wiki/compositions/bounded-staleness|Bounded Staleness]]
- [[wiki/tooling/replication-lag|Replication Lag]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/causal-consistency|Causal Consistency]]
