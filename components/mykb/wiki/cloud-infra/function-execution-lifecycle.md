---
type: "concept"
title: "Function Execution Lifecycle"
description: "Cold starts, warm pools, and the life of a serverless invocation"
tags: ["serverless", "lifecycle", "cold-start", "functions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html",
  "https://cloud.google.com/functions/docs/concepts/exec",
]
---

# Function Execution Lifecycle

## Summary
Serverless function lifecycles run from cold start through warm reuse to shutdown, and these phases dominate latency and cost. Execution environments are created, reused, and reaped automatically by the platform. Understanding the lifecycle drives performance tuning and cost control in event-driven architectures.

## Details
- A cold start initializes a new execution environment: loading the runtime, dependencies, and the handler code.
- Warm starts reuse existing environments, cutting invocation latency to milliseconds for repeated traffic.
- AWS documents the execution environment lifecycle, including reuse and scaling behavior.
- Cloud Functions describe the instance lifecycle with scaling and shutdown behavior for their runtime.
- Provisioned concurrency and snapstart mitigate cold starts at extra cost.
- In mykb, the lifecycle connects to serverless patterns, autoscaling, and latency articles.
- Runtime parameters like memory size change both cost and the CPU available to each invocation, so sizing is a real tuning lever.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/infrastructure/network-function-virtualization|Network Function Virtualization]]
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]]
