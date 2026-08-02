---
type: "concept"
title: "Serverless Computing Patterns"
description: "Event-driven functions and managed runtimes without servers"
tags: ["serverless", "functions", "cloud", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html",
  "https://developers.cloudflare.com/workers/",
]
---

# Serverless Computing Patterns

## Summary
Serverless computing runs code on demand without managing servers, charging only for execution. Functions, managed runtimes, and edge platforms all fit the model. Serverless trades control and cold-start latency for operational simplicity, and it shapes how event-driven applications are built.

## Details
- Function-as-a-service such as Lambda and Cloud Functions scales per invocation and bills by duration and memory.
- Event sources such as queues, HTTP, and object storage trigger functions, favoring event-driven architectures.
- Managed platforms such as Cloudflare Workers and App Engine extend serverless beyond plain functions.
- The model suits bursty, stateless, and event-driven workloads; long-running and stateful work fits poorly.
- Cold starts and vendor lock-in are the main tradeoffs to design around from the start.
- In mykb, serverless connects to function lifecycle, autoscaling, and edge compute articles.
- Observability and tracing are first-class concerns in serverless, since the runtime hides the infrastructure underneath.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/cloud-infra/edge-computing|Edge Computing]]
- [[wiki/devops-infra/api-gateway-patterns|API Gateway Patterns]]
