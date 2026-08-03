---
type: "concept"
title: "Graviton & AWS"
description: "AWS custom ARM silicon for cost-effective compute"
tags: ["graviton", "aws", "arm", "compute"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Graviton & AWS

## Summary

AWS Graviton processors are ARM-based instances (M6g, C6g, R6g, and successors) built for price-performance; AWS claims up to 40% better price-performance over comparable x86 for many workloads. Porting, licensing, and measurement determine whether the claim holds for you.

## Details
- Mechanism: Graviton3/4 deliver higher per-core performance and lower power than the prior generation; instances use the same Nitro stack (EBS, networking) so the management surface is identical; software runs as arm64 binaries — containers, JIT runtimes, and most compiled code port with a rebuild; native x86 dependencies (some databases, closed-source agents, legacy binaries) do not.
- Concrete example: a Node/Python/Go service fleet rebuilds its containers for arm64, moves to Graviton, and measures 25-35% cost reduction at the same p95 latency; a Java app with an x86-only native agent stays on x86 until the vendor ships arm64. Lambda and Fargate also offer arm64 architecture, extending the same economics to serverless.
- Failure modes: assuming portability — C/C++ with SIMD intrinsics, assembly, and closed binaries silently fail or misbehave on arm64; licensing priced per vCPU/socket that penalizes Graviton's core counts; dev machines on x86 masking build issues until deploy; and measuring only throughput while tail latency regresses on specific workloads.
- Operational tradeoffs: Graviton is the default starting point for new greenfield workloads on AWS; the migration path is per-service: rebuild, test in a shadow fleet, compare real metrics, then cut over. Keep a small x86 baseline for compatibility-bound services and revisit as vendor support improves.
- RSIS3/mykb relevance: the wiki records per-service Graviton migration results, so the loop's capacity planner would apply ARM first where telemetry already proved the win.
- Shadow fleet: validate Graviton in a shadow deployment before cutover; real traffic exposes the portability issues benchmarks miss. Include a latency-sensitive service in the cohort, since arm64 regressions are workload-specific.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/aws-vpc-design|AWS VPC Design]]
- [[wiki/cloud-infra/parameter-stores-aws-ssm-azure-keyvault-gcp-secretmanager|Cloud Parameter Stores]]
- [[wiki/infrastructure/aws-msk-and-managed-kafka|Aws Msk And Managed Kafka]]
