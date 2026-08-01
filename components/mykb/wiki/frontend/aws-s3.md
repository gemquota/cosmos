---
type: "concept"
title: "AWS S3"
description: "Object storage service for files, static sites, backups, and data lakes with 99.999999999% durability"
tags: ["aws", "s3", "storage", "objects", "cloud"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# AWS S3

## Summary
AWS S3 is object storage for any file type: static site assets, backups, data lakes, and media. Buckets organize objects addressed by keys with versioning and lifecycle policies.

## Details
- Durability design: 11 nines via multi-AZ replication; versioning protects against overwrites.
- Static website hosting + CloudFront gives a classic SSG deployment target.
- Lifecycle rules tier to Glacier and expire old objects — a natural backup sink.

## Related
- [[wiki/frontend/aws-lambda|AWS Lambda]] — object-upload triggers
- [[wiki/frontend/static-site-generation|Static Site Generation]] — bucket-hosted output
- [[wiki/devops-infra/backups|Backups]] — durable backup target
- [[wiki/devops-infra/terraform|Terraform]] — bucket provisioning as code
- [[wiki/security/secrets-management|Secrets Management]] — bucket access keys
