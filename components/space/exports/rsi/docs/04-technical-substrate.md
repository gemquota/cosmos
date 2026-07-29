# 04 — Technical Substrate: What the RSI System Runs On

> **Analytical Lens:** Technical — the material and computational foundation
> **Source Artifacts:** hardware_requirements, hardware_specs, network_requirements, storage_requirements, infrastructure_target, software_stack, os_requirements, dependency_management, versioning_policy, build_system, performance_targets, data_volume, availability_targets, scalability_model, security_requirements, integration_targets, integration_protocols, timeline, deployment_strategy, documentation_requirements

---

## 1. Hardware Profile

### 1.1 Compute Character: I/O-Bound

The system spends most of its time **waiting for LLM API responses**. Local compute is minimal — hash comparisons, score arithmetic, state machine transitions. Network reliability and API throughput are the bottlenecks, not CPU or memory.

**Implication:** Invest in network resilience, not raw compute. Retry logic, connection pooling, and API budget management matter more than CPU optimization.

### 1.2 Traffic Profile: Medium

- 100–500 improvement evaluations per day
- Each evaluation: 3–5 LLM API calls (modifier proposal, safety check, evaluator scoring, comparison)
- Latency target: minutes per improvement cycle, not milliseconds
- Bursty compute: concentrated during active improvement loops, idle between loops

### 1.3 Infrastructure Target

Initially **vertical scaling** — single machine running the improvement loop. The bottleneck is LLM API throughput, not local compute. When parallel improvement loops are needed (improving multiple artifacts simultaneously), horizontal scaling of evaluation workers, with the coordination engine remaining on one node.

---

## 2. Software Stack

### 2.1 Primary: TypeScript

The core engine, coordination logic, state management, and API are written in TypeScript.

**Why TypeScript:**
- Strong type system catches entity and relationship errors at compile time
- Async/await handles the I/O-bound nature naturally
- JSON is native — artifact serialization is trivial
- The `createSpace()` API is already TypeScript-based

### 2.2 Secondary: Python

The LLM integration layer uses Python for the `openai` and `anthropic` SDKs, which are most mature in Python.

**Communication:** TypeScript ↔ Python via JSON over stdio pipes. Simple, debuggable, no port management.

### 2.3 Storage: Hybrid SQLite + JSON

| Storage | Content | Rationale |
|---------|---------|-----------|
| **SQLite** | Session state, modification history, evaluation scores, convergence metrics | Structured queries, indexed lookups, zero-config |
| **JSON files** | Artifact content (prompt text, strategy definitions, config snapshots) | Human-readable, diff-friendly, version-controllable |

**Linkage:** Both stores are linked by artifact IDs. SQLite indexes reference JSON file paths.

---

## 3. Performance Targets

| Operation | Target | Notes |
|-----------|:------:|-------|
| Internal state transitions | < 100ms | Hash comparisons, score arithmetic |
| Dashboard queries | < 100ms | Interactive use responsiveness |
| LLM-dependent operations | < 30s | Modifier generation, evaluation scoring |
| Improvement cycle (full) | < 2min | End-to-end: select → evaluate → decide |
| Rollback execution | < 100ms | Automatic revert on regression |

The system does not need real-time performance. A 2-minute improvement cycle is acceptable for a research/development tool.

---

## 4. Data Volume

### 4.1 Current Scale: Small

| Data Type | Volume | Growth Rate |
|-----------|:------:|:-----------:|
| Artifact versions | ~10K × 50KB = 500MB | Linear with iterations |
| Evaluation records | ~100K × 1KB = 100MB | 3-5 per improvement cycle |
| Metadata + indexes | ~50MB | Slow growth |
| **Total** | **< 1GB** | — |

### 4.2 Archival Strategy

After 10K improvement cycles (~10GB), implement archival:
- Keep last 1K cycles in active storage
- Archive older cycles to compressed JSON
- Maintain SQLite indexes over archived data for query capability

---

## 5. Security Architecture

### 5.1 Authentication

- **OAuth2/JWT** for LLM API access (OpenAI, Anthropic)
- API keys stored in **environment variables**, never in code or config files
- Internal component authentication via shared secrets (stdio pipe, not network)

### 5.2 Safety Enforcement

The SafetyGuard enforces that no modification can:
- Exfiltrate API keys or credentials
- Increase latency by more than 10%
- Decrease accuracy by more than 2% on any benchmark
- Modify its own safety rules (static rules are immutable)

### 5.3 Audit Trail

Every external API call is logged for security review. History is append-only and tamper-evident (hash chain).

---

## 6. Integration Architecture

### 6.1 External APIs

| API | Purpose | Fallback |
|-----|---------|----------|
| **OpenAI (GPT-4o)** | Primary modifier and evaluator | Anthropic Claude |
| **Anthropic (Claude)** | Cross-validation evaluator | OpenAI GPT-4o |
| **Ollama (local)** | Rapid prototyping, no API costs | None (dev only) |

**Abstraction layer:** `createProvider(config)` returns the appropriate provider. Swapping providers requires zero code changes — only config updates.

### 6.2 Internal Communication

```
TypeScript Engine ←──stdio JSON──→ Python LLM Layer
         │                              │
         ├── SQLite (metadata)          ├── OpenAI API
         └── JSON files (artifacts)     ├── Anthropic API
                                        └── Ollama API
```

### 6.3 Integration Protocols

- **REST** for LLM providers (both OpenAI and Anthropic expose REST)
- **stdio JSON pipes** for TypeScript ↔ Python (simple, debuggable)
- No gRPC needed at this scale

---

## 7. Dependency Management

### 7.1 TypeScript Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `better-sqlite3` | SQLite bindings | ^9.x |
| `commander` | CLI framework | ^12.x |
| `chalk` | Terminal output | ^5.x |
| `vitest` | Testing | ^1.x |

### 7.2 Python Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `openai` | OpenAI API client | ^1.x |
| `anthropic` | Anthropic API client | ^0.x |

### 7.3 Versioning Policy

- **Semantic versioning** for the core library
- **Lock files** for both npm and pip
- **Reproducible builds** via Docker container

---

## 8. Build System

### 8.1 TypeScript

```bash
npm run build    # tsc compilation
npm test         # vitest unit + integration tests
npm run dev      # tsx for rapid iteration
```

### 8.2 Python

```bash
pip install -r requirements.txt
python -m pytest tests/
```

### 8.3 Docker

```dockerfile
FROM node:20-slim
RUN apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN npm ci && pip3 install -r requirements.txt
CMD ["node", "dist/cli/index.js"]
```

---

## 9. Availability and Deployment

### 9.1 Availability Target: Business Hours

The RSI system is a **development/research tool**, not a production service. Acceptable for it to be unavailable at night or on weekends. Active improvement loops complete gracefully even if the system is being shut down.

### 9.2 Deployment Strategy: Canary + Blue/Green

| Component | Strategy | Rationale |
|-----------|----------|-----------|
| **Improvement engine** | Canary | New Modifier/Evaluator tested on small subset first |
| **API endpoints** | Blue/green | No downtime during active improvement loops |
| **Database migrations** | Forward-only | Schema changes are additive, never destructive |

### 9.3 CI/CD Pipeline

```
Push → Lint → TypeCheck → Unit Tests → Integration Tests
  │
  └─→ On merge to main: Build → Publish
       └─→ On tag: Release to npm
```

---

## 10. Documentation Requirements

### 10.1 Documentation Scope

- **API documentation** — every public function has JSDoc/docstrings
- **Architecture documentation** — component diagrams, data flow, decision rationale
- **"How RSI Works" guide** — user-facing explanation of the improvement loop
- **ADR (Architecture Decision Records)** — for every significant design choice

### 10.2 Documentation Standards

- Markdown format (human-readable, version-controllable)
- Code examples for every concept
- Diagrams for every architecture component
- Changelog for every release

---

## 11. Timeline

**Standard timeline: 8-12 weeks to production-ready**

| Phase | Duration | Deliverable |
|-------|:--------:|-------------|
| Core loop | 2 weeks | Working improvement cycle on toy problems |
| Safety mechanisms | 2 weeks | StaticGuard + DynamicGuard implemented |
| Evaluation framework | 2 weeks | Multi-dimensional scoring + benchmarking |
| Hardening | 2-4 weeks | Edge cases, error handling, documentation |

---

## 12. Technical Summary

The RSI technical substrate is:

- **TypeScript + Python** — strong types for the engine, mature SDKs for LLM integration
- **SQLite + JSON** — structured metadata + human-readable artifacts
- **I/O-bound** — investment in network resilience, not raw compute
- **< 1GB data** — small scale, grow-linearly, archive after 10K cycles
- **Business hours availability** — development tool, not production service
- **Canary deployment** — test self-modifications on small subsets first
- **8-12 weeks** to production-ready

The technical choices are deliberately simple: the complexity of RSI is in the recursive logic, not the infrastructure. Simple infrastructure makes the recursive behavior debuggable.

---

*Source: SPACE artifacts hardware_requirements through documentation_requirements (20 artifacts)*
