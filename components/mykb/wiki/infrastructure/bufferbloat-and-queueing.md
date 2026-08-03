---
type: "concept"
title: "Bufferbloat & Queueing"
description: "Excess buffering that inflates latency and how AQM counters it"
tags: ["bufferbloat", "aqm", "latency", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Bufferbloat & Queueing

## Summary
Bufferbloat is the condition where network buffers are so deep that packets sit in queues for hundreds of milliseconds or seconds, inflating latency without improving throughput. It is the counterintuitive failure of "more buffering is better": once a link is saturated, extra buffer space does not add throughput — it only adds queueing delay, and because TCP interprets the long queue as "the network is fine, keep sending", the delay persists indefinitely.

## Details
- The mechanism: a bottleneck link with a deep buffer absorbs bursts, which sounds good — but under sustained load, the queue fills and every packet waits behind the backlog. The queueing delay (buffer size / link rate) can dwarf propagation delay: a 50 MB buffer on a 100 Mbps link adds up to 4 seconds of latency. TCP's congestion control measures loss and delay; with a deep buffer, loss is rare (the buffer absorbs it), so TCP keeps its window large and the queue stays full — maximum throughput at maximum latency, indefinitely. The result is a link that is "fast" by utilization and terrible by experience: web pages crawl, voice breaks, and interactive sessions lag.
- The diagnosis is a latency measurement: ping the link during load. Under no load, RTT is the physical floor; under load, RTT inflates by the queueing delay. If loaded RTT is an order of magnitude above idle RTT, bufferbloat is present. The metric to watch is not throughput (which looks fine) but latency under load — which is why bufferbloat is called the "latency under load" problem.
- The fix is active queue management (AQM): drop or mark packets early, before the buffer fills, so senders back off while queues are still shallow. The modern standards are CoDel (Controlled Delay — tracks the minimum RTT over a window and drops when it exceeds a target, keeping the queue near-empty) and its derivative fq_codel (fair-queue CoDel, the Linux default), plus BBR, a congestion control algorithm that avoids filling buffers by modeling the bottleneck rather than probing for loss. The design principle across all of them: the queue's job is to absorb microbursts, not to hold a standing backlog — so the controller targets a tiny standing queue and lets the link run at full rate with minimal delay.
- Failure modes: AQM tuned too aggressively drops packets that did not need dropping (wasted bandwidth), and AQM deployed without fair queuing lets one flow's backlog still harm others. The operational lesson: the fix is at the bottleneck (the router or the host's outbound queue), and it must be measured, not assumed.
- For mykb: bufferbloat connects queueing theory, QoS, and traffic shaping — the sibling nodes in the networking cluster.

## Related
