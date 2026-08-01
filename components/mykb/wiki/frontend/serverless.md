---
type: "concept"
title: "Serverless"
description: "On-demand, auto-scaling function and managed service execution with no server administration"
tags: ["serverless", "faas", "cloud", "scaling", "platforms"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://aws.amazon.com/serverless/"]
---

# Serverless

## Summary
Serverless is an execution model where the cloud provider runs and scales compute on demand — you pay for invocations, not idle capacity. Functions-as-a-Service (AWS Lambda, Google Cloud Functions) and managed services (S3, DynamoDB, Cloud Run) shift operational burden to the platform. It suits bursty, event-driven workloads and full-stack apps with spiky traffic.

## Details
- Model: platform handles provisioning, scaling to zero, patching, and high availability; developers ship code and configuration.
- FaaS constraints: stateless functions, execution-time limits (Lambda default 3s, max 15min), memory caps, and cold-start latency.
- Event sources: HTTP, queues, object storage events, cron schedules, and pub/sub trigger functions — a natural fit for [[wiki/api-protocols/message-queues|message-queue]] workers.
- Cost shape: per-invocation billing favors intermittent workloads; constant high traffic may be cheaper on containers.
- State management: use managed stores (S3, DynamoDB, Postgres) instead of local filesystem; connection pooling to databases matters at scale.
- Worked example: a serverless mykb indexer could trigger on new note uploads to S3, run TF-IDF updates, and write results to DynamoDB — paying only when notes change.
- Comparison: [[wiki/frontend/edge-functions|edge functions]] trade capacity for proximity; containers give control for steady load.

## Related
- [[wiki/frontend/edge-functions|Edge Functions]] — proximity-optimized serverless
- [[wiki/frontend/aws-lambda|AWS Lambda]] — the original FaaS
- [[wiki/frontend/google-cloud-run|Google Cloud Run]] — containerized serverless
- [[wiki/frontend/aws-dynamodb|AWS DynamoDB]] — serverless key-value store
- [[wiki/api-protocols/message-queues|Message Queues]] — event-driven triggers
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — indexing pipeline architecture
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — capture-to-index workflow
