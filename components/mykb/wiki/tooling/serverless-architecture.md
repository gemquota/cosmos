---
type: "concept"
title: "Serverless Architecture"
description: "Building applications on managed functions and services without server ownership"
tags: ["serverless", "functions", "managed-services", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Serverless_computing", "https://en.wikipedia.org/wiki/Cloud_computing"]
---

# Serverless Architecture

## Summary
Serverless architecture runs code on managed platforms — functions as a service (Lambda, Cloud Functions) plus managed data and messaging — so teams own no servers. It excels at bursty, event-driven, and low-traffic workloads; its costs are cold starts, vendor coupling, and new failure modes.

## Details
- FaaS functions scale to zero and back, ideal for spiky and event-driven demand.
- Cold starts and concurrency limits are real constraints; warm pools and reserved concurrency manage them.
- Managed services (queues, databases, object storage) move operational burden to the vendor but lock you in.
- Cost model inverts: idle costs nothing, but sustained high traffic can exceed a fixed server's cost.
- Distributed debugging and local parity are the hard parts — observability and testable abstractions are mandatory.
- For the mykb bundle, serverless would fit the wiki's event path: link-check triggers, capture handlers, and scheduled sync.
- Worked example — a wiki capture would land in object storage, triggering a function that validates, queues, and notifies — no servers to patch, and idle costs nothing.

Worked example — a wiki capture would land in object storage, triggering a function that validates, queues, and notifies — no servers to patch, and idle costs nothing.

- Observability and local parity are the hard parts; the standing rule is that functions are testable locally and that tracing spans survive the managed boundary, so debugging is not blocked by vendor tooling.
- Cost governance: because idle costs nothing, the risk is sustained high traffic; budgets and per-invocation telemetry keep cost decisions explicit rather than discovered on the bill.
- Adoption screening: a component is a serverless candidate when it is bursty, event-driven, and low-maintenance by nature; the screening would be applied per component rather than to the whole event path.
- Migration guard: moving a component to serverless should preserve its existing contracts and retry semantics, so the architecture change does not change behavior.
## Related
- [[wiki/tooling/edge-computing-practice|Edge Computing Practice]]
- [[wiki/tooling/cloud-native-principles|Cloud Native Principles]]
- [[wiki/cloud-infra/function-as-a-service|Function as a Service]]
- [[wiki/dev-tools/message-brokers|Message Brokers]]
- [[wiki/software-engineering/observability-practice|Observability Practice]]
- [[wiki/tooling/platform-engineering|Platform Engineering]]
- [[wiki/software-engineering/event-driven-design|Event-Driven Design]]
- [[wiki/software-engineering/outbox-table|Outbox Table]]
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]]
