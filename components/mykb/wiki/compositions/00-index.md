---
type: "index"
hub: true
title: "Compositions Index"
description: "Listing of the compositions/ folder (72 pages)."
tags: ["index"]
timestamp: "2026-08-03T00:00:00Z"
---

# Compositions

Part of [[wiki/index|Wiki Index]]. 72 pages.

## Pages
- [[wiki/compositions/additive-migrations|Additive Migrations]] — Schema changes that only add structures, never removing or breaking
- [[wiki/compositions/api-design-best-practices|API Design Best Practices]] — The conventions that make APIs predictable, evolvable, and usable
- [[wiki/compositions/api-integration|API & Integration Pattern]] — API communication patterns: authentication, data exchange, and service integration
- [[wiki/compositions/authentication-patterns|Authentication Patterns]] — The ways systems verify who is asking — sessions, tokens, and federated login
- [[wiki/compositions/authorization-models|Authorization Models]] — The models for deciding what an authenticated party may do
- [[wiki/compositions/b-tree-basics|B-Tree Basics]] — The balanced tree structure behind most database indexes
- [[wiki/compositions/backend-architecture-patterns|Backend Architecture Patterns]] — The recurring shapes of server-side systems and when to use them
- [[wiki/compositions/backup-and-restore|Backup and Restore]] — Protecting data with copies that have been proven recoverable
- [[wiki/compositions/backward-compatible-schema|Backward-Compatible Schema]] — Schema changes that old code and old data can still use
- [[wiki/compositions/bounded-staleness|Bounded Staleness]] — A consistency guarantee that limits how old the data a read may return
- [[wiki/compositions/causal-consistency|Causal Consistency]] — The consistency model where causally related operations are seen in order
- [[wiki/compositions/compare-and-swap|Compare-and-Swap]] — The atomic primitive that updates a value only if it matches an expected value
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]] — Policies for reconciling divergent concurrent edits
- [[wiki/compositions/crdt-practice|CRDT Practice]] — Conflict-free replicated data types that converge without coordination
- [[wiki/compositions/data-backfills|Data Backfills]] — Filling in derived or migrated data for existing records
- [[wiki/compositions/data-storage|Data & Storage Pattern]] — Data management: schema design, querying, caching, and migration
- [[wiki/compositions/database-migrations|Database Migrations]] — Versioned, ordered schema changes applied safely to databases
- [[wiki/compositions/denormalization-tradeoffs|Denormalization Tradeoffs]] — The costs and benefits of duplicating data for read performance
- [[wiki/compositions/dependency-scanning|Dependency Scanning]] — Checking dependencies for known vulnerabilities continuously
- [[wiki/compositions/dev-workflow|Development Workflow Pattern]] — Standard development lifecycle: version control, building, testing, and debugging
- [[wiki/compositions/devops-deployment|DevOps & Deployment Pattern]] — Containerization, CI/CD pipelines, monitoring, and deployment strategies
- [[wiki/compositions/dirty-reads|Dirty Reads]] — Reading data that another transaction has written but not committed
- [[wiki/compositions/distributed-locks|Distributed Locks]] — Mutual exclusion across processes and machines
- [[wiki/compositions/dual-writes|Dual Writes]] — Writing to two systems in one operation and the consistency traps involved
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]] — Accepting temporary divergence that converges once writes stop
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]] — Running a query while showing the actual plan and execution times
- [[wiki/compositions/feature-toggles|Feature Toggles]] — Runtime switches that turn features on and off without deploys
- [[wiki/compositions/fencing-tokens|Fencing Tokens]] — Monotonic tokens that let a resource reject writes from stale lock holders
- [[wiki/compositions/frontend-architecture|Frontend Architecture]] — Structuring client-side applications for maintainability and performance
- [[wiki/compositions/full-stack-development|Full-Stack Development]] — Owning the whole product: client, server, data, and deployment
- [[wiki/compositions/idempotent-writes|Idempotent Writes]] — Writes that produce the same result no matter how many times they run
- [[wiki/compositions/identity-management|Identity Management]] — Establishing and governing who and what can access systems
- [[wiki/compositions/index-selection|Index Selection]] — Choosing which columns to index for the queries that matter
- [[wiki/compositions/index-types|Index Types]] — B-tree, hash, GIN, GiST, BRIN and when each fits
- [[wiki/compositions/lamport-clocks|Lamport Clocks]] — Logical counters that impose a total order on events
- [[wiki/compositions/language-patterns|Programming Languages Reference]] — Language-specific patterns, idioms, and tooling for primary programming languages
- [[wiki/compositions/last-write-wins|Last-Write-Wins]] — The conflict policy where the most recent write simply replaces older ones
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]] — Locks with a time limit so a dead holder releases automatically
- [[wiki/compositions/linearizability|Linearizability]] — Making concurrent operations appear to occur at a single instant in real time
- [[wiki/compositions/lock-free-structures|Lock-Free Structures]] — Concurrent data structures that make progress without locks
- [[wiki/compositions/lost-update-problem|Lost Update Problem]] — Two writes to the same value where one silently overwrites the other
- [[wiki/compositions/monolith-to-microservices|Monolith to Microservices]] — Incrementally splitting a monolithic application into services
- [[wiki/compositions/monotonic-reads|Monotonic Reads]] — The guarantee that successive reads never go back in time
- [[wiki/compositions/normalization-forms|Normalization Forms]] — The 1NF-3NF/BCNF rules that structure dependency-free tables
- [[wiki/compositions/offline-first|Offline-First]] — Designing apps so local data works without connectivity and syncs later
- [[wiki/compositions/operational-transform|Operational Transform]] — Transforming concurrent edits so they compose into one consistent document
- [[wiki/compositions/pessimistic-locking|Pessimistic Locking]] — Locking rows or resources before use to prevent concurrent conflicts
- [[wiki/compositions/phantom-reads|Phantom Reads]] — Rows appearing or disappearing mid-transaction as other transactions commit
- [[wiki/compositions/query-optimization|Query Optimization]] — Improving slow queries via indexing, rewriting, and plan shaping
- [[wiki/compositions/query-plans|Query Plans]] — The execution strategy a database chooses for a query
- [[wiki/compositions/read-committed|Read Committed]] — The isolation level where reads see only committed data
- [[wiki/compositions/read-uncommitted|Read Uncommitted]] — The weakest isolation level, allowing reads of uncommitted data
- [[wiki/compositions/read-your-writes|Read-Your-Writes]] — The guarantee that a client sees its own writes immediately
- [[wiki/compositions/repeatable-read|Repeatable Read]] — The isolation level where repeated reads in a transaction see the same snapshot
- [[wiki/compositions/schema-normalization|Schema Normalization]] — Structuring tables to eliminate redundancy and update anomalies
- [[wiki/compositions/security-authentication|Security & Authentication Pattern]] — Security protocols, authentication flows, and authorization patterns
- [[wiki/compositions/security-engineering|Security Engineering]] — Designing systems that resist attack by construction
- [[wiki/compositions/serializability|Serializability]] — Making concurrent transactions behave as if they ran one after another
- [[wiki/compositions/setup-installation|Setup & Installation Pattern]] — Sequential workflow for installing tools, configuring environments, and initializing projects
- [[wiki/compositions/shift-left-security|Shift-Left Security]] — Moving security checks earlier in the development process
- [[wiki/compositions/slow-query-triage|Slow Query Triage]] — The workflow for finding and fixing slow database queries
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]] — Reading from a consistent snapshot so transactions never see partial commits
- [[wiki/compositions/strangler-pattern|Strangler Pattern]] — Incrementally replacing a legacy system piece by piece
- [[wiki/compositions/strong-consistency|Strong Consistency]] — Guaranteeing every read reflects the latest acknowledged write
- [[wiki/compositions/sync-engines|Sync Engines]] — Systems that reconcile local and remote data across devices
- [[wiki/compositions/threat-modeling|Threat Modeling]] — Systematically finding and addressing attack paths in a design
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]] — Choosing and testing isolation levels against the anomalies you accept
- [[wiki/compositions/vector-clocks|Vector Clocks]] — Per-process counters that detect causality and concurrency between events
- [[wiki/compositions/version-vectors|Version Vectors]] — Per-replica counters that track causal history and detect concurrent updates
- [[wiki/compositions/write-ahead-log|Write-Ahead Log]] — Persisting intent before applying changes so recovery is possible
- [[wiki/compositions/write-skew|Write Skew]] — Two transactions writing different rows based on overlapping reads, breaking an invariant
- [[wiki/compositions/zero-trust-architecture|Zero-Trust Architecture]] — Never trust, always verify: securing every request regardless of origin
