---
type: "index"
title: "Tooling Index"
description: "Listing of the tooling/ folder (76 pages)."
tags: ["index"]
timestamp: "2026-08-03T00:00:00Z"
---

# Tooling

Part of [[wiki/index|Wiki Index]]. 76 pages.

## Pages
- [[wiki/tooling/active-active|Active-Active]] — Running and serving traffic from multiple sites simultaneously
- [[wiki/tooling/active-passive|Active-Passive]] — One site serving traffic while another stands by for failover
- [[wiki/tooling/alembic|Alembic]] — Lightweight database migration tooling for SQLAlchemy with versioned revision scripts
- [[wiki/tooling/archive-policies|Archive Policies]] — Rules for moving old, cold data to cheap long-term storage
- [[wiki/tooling/automated-canary|Automated Canary]] — Canary rollouts that promote or roll back without human judgement calls
- [[wiki/tooling/backup-types|Backup Types]] — Full, incremental, and differential backups and when to use each
- [[wiki/tooling/backup-verification|Backup Verification]] — Proving that backups can actually be restored
- [[wiki/tooling/block-storage|Block Storage]] — Raw disk volumes attached to machines, formatted by the OS
- [[wiki/tooling/business-continuity|Business Continuity]] — Keeping the organization functioning through disruptions
- [[wiki/tooling/cache-aside|Cache-Aside]] — The pattern where the app checks cache, then loads and populates on miss
- [[wiki/tooling/cache-control-headers|Cache-Control Headers]] — HTTP headers that tell caches how long and how aggressively to store responses
- [[wiki/tooling/cache-invalidation|Cache Invalidation]] — Removing or refreshing cached entries when the source data changes
- [[wiki/tooling/cache-stampede|Cache Stampede]] — The thundering herd that hits the origin when a hot cache entry expires
- [[wiki/tooling/caching-layers|Caching Layers]] — Positioning caches at each tier from browser to CDN to app to database
- [[wiki/tooling/canary-analysis|Canary Analysis]] — Comparing canary metrics against the stable baseline to judge a rollout
- [[wiki/tooling/cdn-practice|CDN Practice]] — Serving static and edge-computable content from points of presence worldwide
- [[wiki/tooling/chaos-experiments|Chaos Experiments]] — Deliberately injecting failures to learn how a system behaves under stress
- [[wiki/tooling/client-side-retries|Client-Side Retries]] — Retries initiated by the client for failed or timed-out requests
- [[wiki/tooling/client-side-timeouts|Client-Side Timeouts]] — Timeouts enforced by the client so a slow server cannot hang it
- [[wiki/tooling/cloud-native-principles|Cloud Native Principles]] — Designing systems for the cloud: containers, orchestration, and automation
- [[wiki/tooling/conditional-requests|Conditional Requests]] — HTTP requests that only transfer content when a validator shows a change
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]] — The algorithms that let distributed processes agree on a value despite failures
- [[wiki/tooling/containerization-practice|Containerization Practice]] — Packaging software with its runtime into portable, isolated units
- [[wiki/tooling/dark-launches|Dark Launches]] — Shipping a feature that runs invisibly behind the scenes before it is exposed
- [[wiki/tooling/distributed-cache|Distributed Cache]] — A cache shared across many app instances, usually with key sharding
- [[wiki/tooling/distributed-consistency|Distributed Consistency]] — The spectrum of guarantees for what replicas observe in distributed systems
- [[wiki/tooling/edge-computing-practice|Edge Computing Practice]] — Running computation and caching close to users at the network edge
- [[wiki/tooling/environment-management|Environment Management]] — Running and controlling dev, staging, and production environments
- [[wiki/tooling/etag-negotiation|ETag Negotiation]] — Using entity tags to skip downloads of unchanged resources
- [[wiki/tooling/failover-practice|Failover Practice]] — Routine discipline for switching from a failed primary to a standby
- [[wiki/tooling/failure-drills|Failure Drills]] — Short, targeted exercises that test one recovery path at a time
- [[wiki/tooling/feature-flag-sdks|Feature Flag SDKs]] — Libraries and services for evaluating feature flags at runtime
- [[wiki/tooling/file-storage|File Storage]] — Network filesystems that present shared directories to many clients
- [[wiki/tooling/flag-cleanup|Flag Cleanup]] — Removing feature flags and their dead branches after rollout completes
- [[wiki/tooling/flag-debt|Flag Debt]] — The accumulated cost of flags that are never cleaned up
- [[wiki/tooling/full-backups|Full Backups]] — Complete copies of all data taken at a point in time
- [[wiki/tooling/game-days|Game Days]] — Scheduled rehearsals where teams practice incident response without a real crisis
- [[wiki/tooling/geo-redundancy|Geo-Redundancy]] — Storing data copies in separate geographic locations to survive site loss
- [[wiki/tooling/golden-paths|Golden Paths]] — Blessed, supported ways to build and ship that are fast by default
- [[wiki/tooling/hot-key-cache|Hot Key Cache]] — Special handling for cache keys that receive disproportionate traffic
- [[wiki/tooling/idempotency-design|Idempotency Design]] — Making operations safe to repeat without changing the outcome
- [[wiki/tooling/immutability-backups|Immutability Backups]] — Backups that cannot be altered or deleted, even by attackers or accidents
- [[wiki/tooling/incremental-backups|Incremental Backups]] — Backups that store only data changed since the previous backup
- [[wiki/tooling/keepalives|Keepalives]] — Mechanisms that detect dead peers and hold connections open
- [[wiki/tooling/kubernetes-practice|Kubernetes Practice]] — Running containerized workloads with orchestration: scheduling, scaling, and healing
- [[wiki/tooling/leader-election|Leader Election]] — Choosing one node to coordinate work that must not run in parallel
- [[wiki/tooling/load-balancer-modes|Load Balancer Modes]] — How load balancers pick a backend: round robin, least connections, IP hash, and more
- [[wiki/tooling/load-shaping|Load Shaping]] — Controlling when and how traffic reaches a system to protect capacity
- [[wiki/tooling/local-cache|Local Cache]] — An in-process cache that lives inside each application instance
- [[wiki/tooling/multi-region|Multi-Region]] — Running a service in multiple geographic regions for availability and latency
- [[wiki/tooling/network-storage|Network Storage]] — Storage accessed over the network as opposed to locally attached
- [[wiki/tooling/object-storage-practice|Object Storage Practice]] — Storing and retrieving data as objects with keys, not file trees
- [[wiki/tooling/pacelc-theorem|PACELC Theorem]] — If a partition occurs, trade availability and consistency; otherwise trade latency and consistency
- [[wiki/tooling/paxos-algorithm|Paxos Algorithm]] — The foundational consensus algorithm for distributed agreement
- [[wiki/tooling/platform-engineering|Platform Engineering]] — Building internal platforms that make delivery fast and safe for product teams
- [[wiki/tooling/progressive-delivery|Progressive Delivery]] — Shipping changes gradually with automated gates instead of one big switch
- [[wiki/tooling/quorum-reads|Quorum Reads]] — Reading from enough replicas to satisfy consistency requirements
- [[wiki/tooling/raft-algorithm|Raft Algorithm]] — The understandable consensus algorithm for replicated state machines
- [[wiki/tooling/read-replicas|Read Replicas]] — Copies of a database that serve reads while the primary takes writes
- [[wiki/tooling/replication-lag|Replication Lag]] — The delay between a write on the primary and its appearance on replicas
- [[wiki/tooling/restore-drills|Restore Drills]] — Practicing recovery from backups to keep the restore path honest
- [[wiki/tooling/retention-policies|Retention Policies]] — Rules for how long data is kept and when it is deleted
- [[wiki/tooling/rollout-plans|Rollout Plans]] — Staged schedules for exposing a change to increasing fractions of users
- [[wiki/tooling/rpo-rto|RPO/RTO]] — The recovery point and recovery time objectives that define disaster recovery targets
- [[wiki/tooling/sbom-practice|SBOM Practice]] — Producing and consuming software bills of materials for transparency
- [[wiki/tooling/secure-sdlc|Secure SDLC]] — Building security into every phase of the software development lifecycle
- [[wiki/tooling/serverless-architecture|Serverless Architecture]] — Building applications on managed functions and services without server ownership
- [[wiki/tooling/smoke-tests|Smoke Tests]] — Quick sanity checks that a deploy is alive and basically working
- [[wiki/tooling/snapshot-hierarchy|Snapshot Hierarchy]] — Organizing snapshots into generations: fulls, parents, children, and promotion
- [[wiki/tooling/sqlalchemy|SQLAlchemy]] — Python SQL toolkit and ORM providing the industry-standard database access layer
- [[wiki/tooling/storage-tiers|Storage Tiers]] — Classes of storage with different cost, latency, and durability
- [[wiki/tooling/traffic-shadowing|Traffic Shadowing]] — Sending a copy of production traffic to a new version without affecting users
- [[wiki/tooling/ttl-caches|TTL Caches]] — Caches that expire entries after a fixed time-to-live
- [[wiki/tooling/twelve-factor-app|Twelve-Factor App]] — The twelve principles for building deployable, portable, cloud-ready apps
- [[wiki/tooling/write-behind-cache|Write-Behind Cache]] — Caches that absorb writes and flush them to the source asynchronously
- [[wiki/tooling/write-through-cache|Write-Through Cache]] — Caches that are updated synchronously on every write
