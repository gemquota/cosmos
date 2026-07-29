# Series 5: Technical Specifications

**x = 4 rounds · y = 5 open-ended per round · z = 4 choices per open-ended**

Captures hardware, software, performance, integration, and timeline constraints for the build. This series has the most open-ended questions per round (y=5) because hardware, software, performance, integration, and timeline constraints are parallel concerns requiring independent probes.

Context from Series 1 & 4: domain=`{domain}`, audience=`{audience_level}`, procedure=`{procedure_steps}`, branching=`{branching_complexity}`

---

## Round 1: Hardware and Infrastructure

### Open-Ended 5.1.1
**What hardware platforms or architectures must be supported? (CPU, GPU, mobile, embedded, etc.)**

Write freely. List the target hardware configurations.

**After answering, choose one:**
- a) Single architecture — x86-64 desktop/server only
- b) Dual architecture — e.g., x86-64 + ARM
- c) Mobile/embedded — ARM, RISC-V, or specialized hardware
- d) Platform-agnostic — must run on any reasonably modern hardware

---

### Open-Ended 5.1.2
**What are the minimum and recommended hardware specs? (RAM, storage, compute, network)**

Write freely. Define the floors and targets for each resource.

**After answering, choose one:**
- a) Minimal — <1GB RAM, <100MB storage, single-core sufficient
- b) Standard — 2–8GB RAM, 1–10GB storage, multi-core recommended
- c) High-performance — 16–64GB RAM, SSD storage, GPU recommended
- d) Enterprise — 128GB+ RAM, distributed storage, multi-GPU clusters

---

### Open-Ended 5.1.3
**What bandwidth, latency, or networking requirements exist? Is offline operation needed?**

Write freely. Consider connectivity constraints and network performance.

**After answering, choose one:**
- a) Always-online — requires reliable internet connection
- b) Online with offline fallback — core features work disconnected
- c) Primarily offline — sync is optional or batch-oriented
- d) Edge-deployed — must operate on intermittent or low-bandwidth connections

---

### Open-Ended 5.1.4
**What storage infrastructure is needed? (databases, object storage, caching, file systems)**

Write freely. Map data persistence needs to storage technologies.

**After answering, choose one:**
- a) Single database — one relational or document store covers all needs
- b) Primary DB + cache — e.g., PostgreSQL with Redis
- c) Polyglot persistence — multiple specialized data stores
- d) Distributed storage — sharded databases, multi-region replication

---

### Open-Ended 5.1.5
**What cloud, on-premise, or hybrid infrastructure is targeted? Are there compliance or sovereignty requirements?**

Write freely. Consider deployment location, data residency, and regulatory constraints.

**After answering, choose one:**
- a) Cloud-native — designed for a specific cloud provider
- b) Cloud-agnostic — portable across providers
- c) On-premise only — deployed in private data centers
- d) Hybrid — components span cloud and on-premise with strict compliance

---

## Round 2: Software Stack and Dependencies

### Open-Ended 5.2.1
**What programming languages, runtimes, or frameworks are required or preferred?**

Write freely. Justify language choices based on domain, performance, and team.

**After answering, choose one:**
- a) Single language — one ecosystem covers everything
- b) Two languages — e.g., backend + frontend split
- c) Polyglot — 3+ languages for specialized components
- d) Language-agnostic — choice delegated to implementation team

---

### Open-Ended 5.2.2
**What operating systems and environments must be supported?**

Write freely. List target OS platforms and their priority.

**After answering, choose one:**
- a) Linux only
- b) Linux + macOS (developer-focused)
- c) Cross-platform — Linux, macOS, Windows
- d) Containerized — only targets Docker/K8s; host OS is irrelevant

---

### Open-Ended 5.2.3
**What existing libraries, services, APIs, or third-party dependencies should be used or avoided?**

Write freely. Name specific libraries and the rationale for inclusion or exclusion.

**After answering, choose one:**
- a) Minimal dependencies — build from standard library where possible
- b) Core curated deps — choose established libraries for major concerns
- c) Ecosystem-driven — leverage framework convention over custom code
- d) Heavy integration — depend on multiple external services and SaaS

---

### Open-Ended 5.2.4
**What versioning, compatibility, or upgrade policies govern the software stack?**

Write freely. Define how dependencies are managed and updated.

**After answering, choose one:**
- a) Latest-stable — always use current versions, update frequently
- b) LTS-only — pinned to long-term support versions
- c) Semver-constrained — explicit version ranges with CI verification
- d) Locked — dependencies are vendored and updated on a release cycle

---

### Open-Ended 5.2.5
**What build systems, CI/CD platforms, and packaging formats are required?**

Write freely. Describe the pipeline from commit to deployable artifact.

**After answering, choose one:**
- a) Simple build — single build tool, manual or script-based deployment
- b) CI-built — automated builds on push, artifact registry
- c) Full CI/CD — automated testing, staging, and production deployment
- d) GitOps — infrastructure-as-code with automated promotion pipelines

---

## Round 3: Performance and Scalability

### Open-Ended 5.3.1
**What are the throughput, latency, and concurrency requirements? (requests/sec, response time, simultaneous users)**

Write freely. Define quantitative performance targets.

**After answering, choose one:**
- a) Low traffic — <100 req/s, seconds of latency, single-digit concurrency
- b) Moderate traffic — 100–10K req/s, sub-second latency, hundreds concurrent
- c) High traffic — 10K–100K req/s, low-latency targets, thousands concurrent
- d) Internet scale — 100K+ req/s, strict SLOs, global distribution

---

### Open-Ended 5.3.2
**What data volume and growth rate is expected? (storage size, records, throughput)**

Write freely. Estimate current and projected data size.

**After answering, choose one:**
- a) Small — <10GB data, slow growth, single-node viable
- b) Medium — 10GB–1TB, moderate growth, needs partitioning
- c) Large — 1TB–100TB, rapid growth, requires distributed architecture
- d) Massive — 100TB+, petabyte-scale, data lifecycle management needed

---

### Open-Ended 5.3.3
**What availability, uptime, and disaster recovery targets are required?**

Write freely. Define SLA targets and recovery objectives.

**After answering, choose one:**
- a) Best-effort — no formal SLA, occasional downtime acceptable
- b) Standard — 99.9% uptime, daily backups, basic DR plan
- c) High — 99.99% uptime, multi-region redundancy, automated failover
- d) Critical — 99.999%+ uptime, active-active, zero-data-loss DR

---

### Open-Ended 5.3.4
**What scalability model is required? (vertical, horizontal, elastic, serverless)**

Write freely. Describe how the system should handle growth.

**After answering, choose one:**
- a) Vertical — scale up a single node as needed
- b) Horizontal — add/remove nodes with load balancer
- c) Elastic — auto-scale based on metrics
- d) Serverless — event-driven scale managed by platform

---

### Open-Ended 5.3.5
**What security and compliance standards must be met? (auth, encryption, audit, regulations)**

Write freely. List specific security requirements and regulatory frameworks.

**After answering, choose one:**
- a) Basic — password auth, TLS, no formal compliance requirements
- b) Standard — OAuth2/MFA, encryption at rest, audit logging
- c) Regulated — SOC2, HIPAA, GDPR, or PCI-DSS requirements
- d) High-security — air-gapped, FIPS, zero-trust architecture

---

## Round 4: Integration and Timeline

### Open-Ended 5.4.1
**What external systems, APIs, or services must this system integrate with?**

Write freely. List each integration and its purpose.

**After answering, choose one:**
- a) No integrations — fully standalone system
- b) 1–2 integrations — limited surface area for interoperability
- c) 3–7 integrations — multiple external touchpoints
- d) 8+ integrations — integration-heavy, requiring an API gateway or ESB

---

### Open-Ended 5.4.2
**What integration protocols, data formats, or standards must be supported?**

Write freely. Specify the wire protocols and serialization formats.

**After answering, choose one:**
- a) REST/JSON only — simple HTTP-based communication
- b) REST + events — REST APIs plus message queue or event stream
- c) gRPC + protobuf — type-safe, high-performance contracts
- d) Multiple protocols — REST, gRPC, GraphQL, file-based, and binary formats

---

### Open-Ended 5.4.3
**What is the expected timeline, milestones, and delivery cadence?**

Write freely. Map the project timeline with key milestones.

**After answering, choose one:**
- a) Quick — prototype in weeks, production in 1–3 months
- b) Standard — phased delivery over 3–9 months
- c) Ambitious — 9–18 months with multiple major releases
- d) Large program — 18+ months with distinct workstreams

---

### Open-Ended 5.4.4
**What testing, staging, and rollout strategy is required?**

Write freely. Describe the deployment pipeline and risk mitigation.

**After answering, choose one:**
- a) Basic — dev + production environments, manual testing
- b) Standard — dev, staging, production with automated test suite
- c) Robust — preview deployments, canary releases, feature flags
- d) Enterprise — full deployment matrix, blue-green, chaos engineering

---

### Open-Ended 5.4.5
**What documentation, training, or knowledge transfer outputs are expected alongside the system?**

Write freely. List the documentation artifacts and their audiences.

**After answering, choose one:**
- a) Minimal — inline comments and a README
- b) Standard — API docs, architecture decision records, setup guide
- c) Comprehensive — full technical docs, runbooks, user manuals
- d) Certification-level — training materials, compliance documentation, formal specs
