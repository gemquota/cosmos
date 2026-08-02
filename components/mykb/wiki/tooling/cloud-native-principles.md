---
type: "concept"
title: "Cloud Native Principles"
description: "Designing systems for the cloud: containers, orchestration, and automation"
tags: ["cloud-native", "principles", "architecture", "containers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Cloud_native_computing", "https://12factor.net/"]
---

# Cloud Native Principles

## Summary
Cloud native is a set of principles for building systems that exploit the cloud: packaged in containers, orchestrated dynamically, built on microservices or serverless, and automated end to end. The twelve-factor app is its most concrete expression; managed services and elasticity are its habitat.

## Details
- Cloud native systems treat infrastructure as disposable: anything can be replaced, so everything is automatable.
- The twelve factors — config in env, stateless processes, backing services as resources, and more — describe the ideal shape.
- Elasticity only works if workloads are designed for it: horizontal scaling, health checks, and graceful shutdown.
- Observability is assumed: distributed systems without metrics, logs, and traces are unmanageable.
- Managed services trade control for leverage; cloud native means choosing the trade deliberately.
- For the mykb bundle, cloud native applies to the reading service and sync pipeline, while the content stays plain files that any runtime can serve.

Worked example — the wiki reading service is cloud native: stateless containers behind a load balancer, config via env, the bundle in object storage, and autoscaling on read traffic.

## Related
- [[wiki/tooling/twelve-factor-app|Twelve-Factor App]]
- [[wiki/tooling/containerization-practice|Containerization Practice]]
- [[wiki/tooling/kubernetes-practice|Kubernetes Practice]]
- [[wiki/tooling/serverless-architecture|Serverless Architecture]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/tooling/platform-engineering|Platform Engineering]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
- [[wiki/communities/base-image-management|Base Image Management]]
- [[wiki/devops-infra/kubernetes|Kubernetes]]
