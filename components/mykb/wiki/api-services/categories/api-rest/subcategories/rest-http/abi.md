---
status: "growing"
type: "entity"
title: "ABI"
description: "Scalability"
tags: ["entity", "acronym", "android", "api", "ast", "backend"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

## Abi

Scalability — the ability of a system to handle increased load. Sessions reference horizontal scaling, load balancing, and caching strategies.

**Related topics:** android, api, backend

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/index|Api Clients › Abi

## Overview

Scalability is the capacity of a system to accommodate growing demand — more users, larger payloads, or higher request rates — without redesigning the architecture. In the sessions that reference ABI, it is treated as a property of the whole stack: an API scales only if its compute, storage, and network layers scale together. The main levers are adding replicas (horizontal scaling), distributing traffic evenly (load balancing), and reducing duplicate work (caching).

## Scaling Patterns

- **Horizontal scaling** adds replicas of stateless services and spreads traffic across them. State must move to shared stores such as databases, caches, or object storage so that any replica can serve any request.
- **Load balancing** distributes requests using round-robin, least-connections, or consistent hashing, and uses health checks to drain failed replicas.
- **Caching** absorbs repeated reads at the edge, in the application, or in shared stores, cutting demand on origin services and databases.

## Design Notes

Capacity planning starts with measuring throughput, latency, and saturation under load, then identifying whether the constraint is CPU, memory, disk I/O, or database connections. Autoscaling policies should react to utilization and queue depth rather than raw request counts, and caches need eviction policies so hot data stays resident while stale data is refreshed.

## Observability

Scalability work is only maintainable when the stack is observable. Dashboards track replica counts, queue depth, and error rates; alerting triggers on p95 latency and saturation thresholds before users notice degradation. Load tests with realistic traffic profiles validate that added capacity actually converts into throughput, and gradual rollout techniques let operators shrink replica counts again when demand falls. Documenting the current capacity budget — expected peak traffic, reserve capacity, and the cost of one replica — turns scaling from an emergency reaction into a planned operation.

## Related Concepts

- [[wiki/cloud-infra/autoscaling|Autoscaling]] — capacity added and removed by policy
- [[wiki/api-protocols/load-balancing|Load Balancing]] — distributing traffic across replicas
- [[wiki/frontend/browser-caching|Browser Caching]] — client-side reuse that lowers origin load

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acs|Acs
