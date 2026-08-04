---
type: "entity"
title: "AWS Lambda"
description: "AWS's Functions-as-a-Service: event-driven functions scaling to zero with per-invocation billing"
tags: ["aws", "lambda", "serverless", "faas", "cloud"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# AWS Lambda

## Summary
AWS Lambda runs code in response to events — HTTP, S3 uploads, queues, schedules — without provisioning servers. It scales to zero and bills per invocation.

## Details
- Execution limits: memory up to 10GB, timeout up to 15 minutes; cold starts affect latency.
- Triggers from S3, DynamoDB, SQS, API Gateway, and EventBridge make it the glue of AWS serverless.
- Design stateless functions; use managed stores for durable state.

## Related
- [[wiki/frontend/serverless|Serverless]] — the hosting model
- [[wiki/frontend/aws-s3|AWS S3]] — object storage trigger
- [[wiki/frontend/aws-dynamodb|AWS DynamoDB]] — serverless state store
- [[wiki/api-protocols/message-queues|Message Queues]] — SQS-triggered workers
- [[wiki/api-protocols/timeouts|Timeouts]] — execution time limits
