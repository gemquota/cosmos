---
type: "concept"
title: "Priority Queuing & DSCP"
description: "Marking packets with DSCP and servicing queues by priority"
tags: ["dscp", "queuing", "qos", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Priority Queuing & DSCP

## Summary
Priority queuing and DSCP are the marking-and-servicing machinery of QoS: DSCP (Differentiated Services Code Point) marks packets with a class (6 bits in the IP header — voice, video, signaling, best-effort, scavenger), and priority queuing is the scheduler that services those classes by priority when the link is congested. The two together implement the policy: traffic is classified at the edge, and the network's queues honor the classification under load.

## Details
- The marking step: a DSCP value (the 6-bit field, using the AF/EF/CS codepoint conventions — EF for expedited forwarding, AF classes for assured forwarding with drop-precedence sub-bits, CS for class selectors) is set on each packet — by the application, by a switch at the trust boundary (marking at the edge, where the sender's identity is known), or by policy. The marking is the contract: it declares "this traffic is voice" or "this traffic is bulk", and downstream devices honor it. The trust question is central: if every host can mark itself EF, everyone marks everything EF and the classes collapse — which is why networks re-mark or drop markings at trust boundaries and only honor DSCP from trusted sources.
- The servicing step: the egress interface maintains multiple queues (typically 4-8: priority queue for EF, guaranteed-bandwidth queues for AF classes, best-effort, and a scavenger queue). Strict priority queuing services the priority queue first — voice goes before everything, always — which guarantees the latency/jitter voice needs but risks starving lower classes if the priority traffic ever exceeds its allocation (the reason for policing EF traffic at its committed rate). Class-based weighted fair queueing (CBWFQ) gives each class a weighted share instead, trading voice's absolute priority for fairness; the standard design is a small strict-priority queue for EF plus weighted sharing for the rest.
- The end-to-end requirement: QoS only works if every hop honors the marking. One switch that ignores DSCP (or resets it) breaks the chain — the marked packets join best-effort at that hop and the latency guarantee dies. This is why DSCP-based QoS is designed per-fabric (the "trust domain") and why the failure modes are configuration-focused: markings stripped by a misconfigured trust boundary, EF traffic un-policed (starving everything else), and the tunnel problem: DSCP inside a tunnel (VXLAN, IPsec) is invisible unless the encapsulation copies or maps it.
- For mykb: the node is the marking/servicing pair in the QoS cluster — it connects traffic shaping, bufferbloat (the problem QoS manages), and bandwidth allocation (the policy QoS implements).

## Related
- [[wiki/devops-infra/priority-classes-and-preemption|Priority Classes & Preemption]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
