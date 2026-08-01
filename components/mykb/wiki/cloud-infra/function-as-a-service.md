---
type: "concept"
title: "Function-as-a-Service"
description: "Serverless execution of single-purpose functions, billed per invocation and scaled to zero"
tags: ["serverless", "faas", "lambda", "cloud", "event-driven"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/lambda/latest/dg/welcome.html"]
---

# Function-as-a-Service

## Summary
Function-as-a-Service (FaaS) runs stateless functions in response to events — HTTP calls, queue messages, schedule ticks — without provisioning servers. The platform handles scaling, including scaling to zero, and bills per invocation and duration. FaaS trades cold-start latency and platform limits for dramatically reduced operational surface.

## Details
- Execution model: the platform instantiates a sandbox, runs the function to completion, and tears it down; idle functions scale to zero, so cost tracks actual demand.
- Event sources: API gateway requests, queue and stream messages, object-storage events, and scheduled triggers (cron) are the common integrations.
- Limits to design around: execution timeout, memory range, payload size, and concurrency ceilings — long-running or stateful work does not fit.
- Cold starts add latency when a new sandbox must be created; warm pools, provisioned concurrency, and minimal runtimes mitigate them.
- Comparison: containers give full control and persistent processes; FaaS is best for short, stateless, event-driven units with spiky or idle-heavy load.
- Vendor lock-in is real: the event source catalog and runtime bindings are provider-specific, though open platforms (OpenFaaS, Knative) approximate the model.
- Worked example: a mykb webhook handler — validate the payload, append to a log stream, and update the index — runs fine as a single FaaS function with a 15-minute timeout and zero idle cost.

## Related
- [[wiki/cloud-infra/cloud-emulators|Cloud Emulators]] — local testing of serverless functions
- [[wiki/devops-infra/scheduled-jobs|Scheduled Jobs]] — cron-style FaaS triggers
- [[wiki/devops-infra/event-streaming|Event Streaming]] — event sources that invoke functions
- [[wiki/api-protocols/webhooks|Webhooks]] — typical FaaS event source
- [[wiki/api-protocols/rest-apis|REST APIs]] — function fronted by an API gateway
- [[wiki/devops-infra/observability|Observability]] — trace and log correlation for short-lived runs
