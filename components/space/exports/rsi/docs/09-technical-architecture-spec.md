# 09 — Technical Architecture Specification: Infrastructure, Integration, and Performance Model of RSI

> **Analytical Lens:** Technical (Tier 2 — Exhaustive)
> **Supersedes:** 04-technical-substrate.md (extends with implementation specifications)
> **Source Artifacts:** All 67 SPACE artifacts + 67 open-ended answers
> **Derivation Depth:** Full artifact cross-referencing

---

## 1. System Architecture Overview

### 1.1 Architectural Style: Layered Event-Driven

The RSI system follows a **layered event-driven architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                           │
│  CLI Interface (Commander.js)  │  Web UI (React + Vite)        │
├─────────────────────────────────────────────────────────────────┤
│                    ORCHESTRATION LAYER                          │
│  ImprovementLoop │ SessionManager │ ConfigurationLoader         │
├─────────────────────────────────────────────────────────────────┤
│                    ENGINE LAYER                                 │
│  Evaluator │ Modifier │ SafetyGuard │ ConvergenceDetector       │
├─────────────────────────────────────────────────────────────────┤
│                    INTEGRATION LAYER                            │
│  ProviderFactory │ OpenAI │ Anthropic │ Gemini │ Mistral │ Ollama│
├─────────────────────────────────────────────────────────────────┤
│                    PERSISTENCE LAYER                            │
│  StorageProvider │ FileSystemStorage │ (SQLite — planned)       │
├─────────────────────────────────────────────────────────────────┤
│                    FOUNDATION LAYER                             │
│  TypeScript Runtime │ Node.js │ File System │ Network           │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Component Map

| Layer | Components | Responsibility | Language |
|-------|-----------|----------------|----------|
| **Presentation** | CLI, Web UI | User interaction, visualization | TypeScript, React |
| **Orchestration** | ImprovementLoop, SessionManager | Workflow coordination, state management | TypeScript |
| **Engine** | Evaluator, Modifier, SafetyGuard, ConvergenceDetector | Core RSI logic | TypeScript |
| **Integration** | ProviderFactory, LLM Providers | External API communication | TypeScript |
| **Persistence** | StorageProvider, FileSystemStorage | Data storage and retrieval | TypeScript |
| **Foundation** | Node.js, File System | Runtime environment | System |

---

## 2. Data Architecture

### 2.1 Data Model — Complete Schema

#### Core Entities (TypeScript Interfaces)

```typescript
// From src/types/index.ts — with RSI extensions

interface ImprovementLoop {
  id: string;
  project_id: string;
  artifact_ids: string[];
  evaluator_id: string;
  modifier_id: string;
  safety_guard_id: string;
  convergence_detector_id: string;
  history_id: string;
  state: 'initialized' | 'running' | 'paused' | 'converged' | 'terminated' | 'error';
  max_cycles: number;
  current_cycle: number;
  created_at: DateTime;
  updated_at: DateTime;
}

interface Evaluator {
  id: string;
  scoring_function: string;  // Serialized callable
  confidence_threshold: number;  // [0, 1]
  evaluation_depth: number;
  provider: LLMProvider;
  model: string;
  criteria_id: string;
}

interface Modifier {
  id: string;
  modification_type: 'prompt' | 'code' | 'strategy' | 'config';
  granularity: 'fine' | 'coarse';
  safety_level: 'conservative' | 'moderate' | 'aggressive';
  provider: LLMProvider;
  model: string;
  self_modification_depth: number;
  max_self_modification_depth: number;
}

interface Artifact {
  id: string;
  project_id: string;
  type: 'prompt' | 'config' | 'strategy';
  version_chain: ArtifactVersion[];
  parent_id: string | null;
  content: string;
  current_version: number;
  state: ArtifactState;
  created_at: DateTime;
  updated_at: DateTime;
}

interface ArtifactVersion {
  version: number;
  content: string;
  diff_summary: string;
  performance_delta: number;
  created_at: DateTime;
  status: 'active' | 'regressed' | 'deprecated' | 'archived';
}

interface EvaluationCriteria {
  id: string;
  dimensions: EvaluationDimension[];
  weights: Map<string, number>;
  benchmark_references: string[];
  human_overrides: OverrideRecord[];
  state: 'active' | 'under_review' | 'locked';
  created_by: string;  // Human operator ID
}

interface EvaluationDimension {
  name: string;
  weight: number;
  min_score: number;
  max_score: number;
  description: string;
}

interface SafetyGuard {
  id: string;
  static_rules: StaticRule[];
  dynamic_patterns: DynamicPattern[];
  confidence_threshold: number;
  override_log: OverrideRecord[];
}

interface StaticRule {
  id: string;
  condition: string;  // Serialized predicate
  action: 'block' | 'flag' | 'log';
  description: string;
  immutable: true;  // Always true for static rules
}

interface DynamicPattern {
  id: string;
  pattern_hash: string;
  confidence: number;
  origin: 'learned' | 'imported';
  created_at: DateTime;
  last_validated: DateTime;
}

interface History {
  id: string;
  project_id: string;
  records: ModificationRecord[];
  hash_chain: string[];  // Tamper-evident chain
}

interface ModificationRecord {
  id: string;
  cycle_id: string;
  artifact_id: string;
  artifact_version: number;
  modification_type: 'improvement' | 'self_modification' | 'rollback' | 'evaluation';
  before_state: string;
  after_state: string;
  before_score: number;
  after_score: number;
  safety_verdict: 'approved' | 'rejected' | 'flagged' | 'override';
  llm_provider: string;
  llm_model: string;
  timestamp: DateTime;
  duration_ms: number;
}

interface ConvergenceDetector {
  id: string;
  improvement_velocity: number;
  improvement_trajectory: 'accelerating' | 'decelerating' | 'plateaued' | 'regressed';
  convergence_threshold: number;
  window_size: number;
  min_cycles: number;
  last_verdict: 'continue' | 'converge' | 'escalate';
}
```

### 2.2 Storage Schema

#### FileSystem Layout

```
project-root/
├── .space/
│   ├── config.yaml              # Runtime configuration
│   ├── sessions/
│   │   ├── {session-id}/
│   │   │   ├── loop.json        # ImprovementLoop state
│   │   │   ├── evaluator.json   # Evaluator state
│   │   │   ├── modifier.json    # Modifier state
│   │   │   ├── safety.json      # SafetyGuard state
│   │   │   ├── convergence.json # ConvergenceDetector state
│   │   │   └── history/
│   │   │       ├── records.jsonl  # Modification records (append-only)
│   │   │       └── hash-chain.json # Tamper-evident chain
│   ├── artifacts/
│   │   ├── {artifact-id}/
│   │   │   ├── current.json     # Current version
│   │   │   ├── versions/
│   │   │   │   ├── v1.json
│   │   │   │   ├── v2.json
│   │   │   │   └── ...
│   │   │   └── metadata.json    # Artifact metadata
│   ├── criteria/
│   │   └── {criteria-id}.json   # EvaluationCriteria
│   └── snapshots/
│       ├── {session-id}-{timestamp}.json  # Session snapshots
│       └── ...
└── src/                         # Source code
```

#### SQLite Schema (Planned)

```sql
-- Sessions table
CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL,
  state TEXT NOT NULL,
  max_cycles INTEGER NOT NULL,
  current_cycle INTEGER DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

-- Artifacts table
CREATE TABLE artifacts (
  id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL,
  type TEXT NOT NULL,
  current_version INTEGER DEFAULT 1,
  state TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

-- Artifact versions table
CREATE TABLE artifact_versions (
  id TEXT PRIMARY KEY,
  artifact_id TEXT NOT NULL,
  version INTEGER NOT NULL,
  content TEXT NOT NULL,
  diff_summary TEXT,
  performance_delta REAL,
  status TEXT NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY (artifact_id) REFERENCES artifacts(id)
);

-- Modification records table
CREATE TABLE modification_records (
  id TEXT PRIMARY KEY,
  session_id TEXT NOT NULL,
  cycle_id TEXT NOT NULL,
  artifact_id TEXT NOT NULL,
  artifact_version INTEGER NOT NULL,
  modification_type TEXT NOT NULL,
  before_score REAL,
  after_score REAL,
  safety_verdict TEXT NOT NULL,
  llm_provider TEXT,
  llm_model TEXT,
  timestamp TEXT NOT NULL,
  duration_ms INTEGER,
  FOREIGN KEY (session_id) REFERENCES sessions(id),
  FOREIGN KEY (artifact_id) REFERENCES artifacts(id)
);

-- Evaluation results table
CREATE TABLE evaluation_results (
  id TEXT PRIMARY KEY,
  session_id TEXT NOT NULL,
  artifact_id TEXT NOT NULL,
  artifact_version INTEGER NOT NULL,
  dimension TEXT NOT NULL,
  score REAL NOT NULL,
  confidence REAL,
  evaluator_id TEXT NOT NULL,
  timestamp TEXT NOT NULL,
  FOREIGN KEY (session_id) REFERENCES sessions(id),
  FOREIGN KEY (artifact_id) REFERENCES artifacts(id)
);

-- Safety decisions table
CREATE TABLE safety_decisions (
  id TEXT PRIMARY KEY,
  session_id TEXT NOT NULL,
  proposal_id TEXT NOT NULL,
  verdict TEXT NOT NULL,
  rule_id TEXT,
  pattern_id TEXT,
  human_override BOOLEAN DEFAULT FALSE,
  override_by TEXT,
  timestamp TEXT NOT NULL,
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);

-- Convergence metrics table
CREATE TABLE convergence_metrics (
  id TEXT PRIMARY KEY,
  session_id TEXT NOT NULL,
  cycle_number INTEGER NOT NULL,
  velocity REAL NOT NULL,
  trajectory TEXT NOT NULL,
  verdict TEXT NOT NULL,
  timestamp TEXT NOT NULL,
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);

-- Indexes
CREATE INDEX idx_artifacts_project ON artifacts(project_id);
CREATE INDEX idx_records_session ON modification_records(session_id);
CREATE INDEX idx_records_artifact ON modification_records(artifact_id);
CREATE INDEX idx_evaluations_artifact ON evaluation_results(artifact_id);
CREATE INDEX idx_convergence_session ON convergence_metrics(session_id);
```

---

## 3. Integration Architecture

### 3.1 LLM Provider Integration

```
┌──────────────────────────────────────────────────────────────┐
│                    ProviderFactory                            │
│  createProvider(config) → LLMProvider                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────┐  ┌──────────┐  ┌────────┐  ┌────────┐  ┌─────┐│
│  │ OpenAI  │  │ Anthropic│  │ Gemini │  │Mistral │  │Ollama││
│  │ GPT-4o  │  │ Claude   │  │ Pro    │  │ Large  │  │Local ││
│  └────┬────┘  └────┬─────┘  └───┬────┘  └───┬────┘  └──┬──┘│
│       │            │            │            │          │   │
│       └────────────┴────────────┴────────────┴──────────┘   │
│                          │                                   │
│                    Unified Interface                         │
│                    generate(prompt) → response               │
│                    embed(text) → vector                      │
│                    health() → status                         │
│                          │                                   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    │  Rate Limiter │
                    │  Retry Logic  │
                    │  Cost Tracker │
                    └─────────────┘
```

### 3.2 Provider Comparison

| Provider | Model | Strengths | Weaknesses | Use Case |
|----------|-------|-----------|------------|----------|
| **OpenAI** | GPT-4o | Best general performance, function calling | Cost, rate limits | Primary Modifier/Evaluator |
| **Anthropic** | Claude | Long context, safety-focused | Cost, availability | Cross-validation Evaluator |
| **Google** | Gemini Pro | Multimodal, large context | API complexity | Artifact analysis |
| **Mistral** | Large | Fast, cost-effective | Smaller context | Rapid iteration |
| **Ollama** | Various | Free, private, offline | Limited model quality | Development/prototyping |

### 3.3 Internal Communication Protocol

```
TypeScript Engine ←──stdio JSON──→ Python LLM Layer (if needed)
         │                              │
         ├── SQLite (metadata)          ├── REST API calls
         └── JSON files (artifacts)     └── Response parsing
```

**Message format (stdio JSON):**
```json
{
  "type": "request" | "response" | "error",
  "id": "uuid",
  "method": "generate" | "embed" | "health",
  "params": { ... },
  "result": { ... },
  "error": { "code": "string", "message": "string" }
}
```

---

## 4. Performance Specification

### 4.1 Latency Budget

| Operation | P50 | P95 | P99 | Timeout |
|-----------|:---:|:---:|:---:|:-------:|
| State transition | 1ms | 5ms | 10ms | 100ms |
| File read/write | 5ms | 20ms | 50ms | 200ms |
| SQLite query | 1ms | 5ms | 10ms | 50ms |
| LLM API call | 2s | 10s | 20s | 30s |
| Full improvement cycle | 30s | 60s | 120s | 180s |
| Rollback execution | 10ms | 50ms | 100ms | 200ms |
| Convergence check | 1ms | 5ms | 10ms | 50ms |
| Dashboard query | 10ms | 50ms | 100ms | 200ms |

### 4.2 Throughput Budget

| Metric | Target | Notes |
|--------|:------:|-------|
| Improvement cycles/hour | 60-120 | 1-2 minute cycle time |
| Evaluations/minute | 10-30 | LLM-dependent |
| Modifications/minute | 5-15 | Including safety review |
| Concurrent loops | 1-3 | Resource-dependent |
| History records/second | 100+ | Append-only, sequential |

### 4.3 Resource Budget

| Resource | Minimum | Recommended | Notes |
|----------|:-------:|:-----------:|-------|
| RAM | 512MB | 2GB | LLM responses can be large |
| Disk | 1GB | 10GB | Artifact versions accumulate |
| CPU | 1 core | 4 cores | Mostly I/O-bound |
| Network | 1 Mbps | 10 Mbps | LLM API calls |
| API budget | $10/day | $100/day | Depends on model and volume |

### 4.4 Scalability Model

**Vertical scaling primary:**
- Single machine handles 1-3 concurrent improvement loops
- Bottleneck is LLM API throughput, not local compute
- Scale up by adding more API budget and better network

**Horizontal scaling (future):**
- Evaluation workers can be distributed
- Coordination engine remains single-node
- Database must support concurrent writes (SQLite → PostgreSQL)

---

## 5. Security Architecture

### 5.1 Threat Model

| Threat | Severity | Likelihood | Mitigation |
|--------|:--------:|:----------:|------------|
| **Credential exposure** | Critical | Low | StaticGuard rule SR-001, env vars only |
| **Prompt injection** | High | Medium | Input sanitization, LLM output validation |
| **Modifier self-escalation** | Critical | Low | Depth limiting, human approval for self-modification |
| **Data exfiltration** | Critical | Low | Network egress monitoring, no outbound data channels |
| **Evaluation manipulation** | High | Low | Multiple evaluators, human override authority |
| **Supply chain attack** | High | Low | Lock files, version pinning, audit dependencies |
| **Denial of service** | Medium | Medium | Rate limiting, queue management, graceful degradation |

### 5.2 Authentication & Authorization

| Actor | Authentication | Authorization |
|-------|---------------|---------------|
| **Human operator** | OAuth2/JWT | Full access (override authority) |
| **LLM API** | API key (env var) | Per-provider rate limits |
| **Internal components** | Shared secret (stdio) | Full access within loop |
| **External integrations** | API key | Read-only where possible |

### 5.3 Audit Trail

Every external API call and safety decision is logged with:
- Timestamp
- Actor identity
- Action performed
- Inputs and outputs
- Safety verdict
- Hash chain linkage (tamper-evident)

---

## 6. Deployment Architecture

### 6.1 Deployment Topology

```
┌─────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT                               │
│  Local machine → tsx for rapid iteration                    │
│  Full benchmark suite, synthetic data                       │
├─────────────────────────────────────────────────────────────┤
│                    PRODUCTION                                │
│  Docker container → Node.js runtime                         │
│  Real benchmarks, production data                           │
│  Persistent storage (SQLite + JSON files)                   │
├─────────────────────────────────────────────────────────────┤
│                    CI/CD                                     │
│  GitHub Actions → lint → typecheck → test → build → publish │
│  Node 18/20/22 matrix testing                               │
│  Tag-triggered npm publish                                  │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Container Specification

```dockerfile
FROM node:20-slim AS base
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

FROM base AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

FROM base AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM deps AS runtime
COPY --from=build /app/dist ./dist
COPY --from=build /app/package.json ./
VOLUME ["/data"]
EXPOSE 3000
CMD ["node", "dist/cli/index.js"]
```

### 6.3 Environment Variables

| Variable | Required | Description | Example |
|----------|:--------:|-------------|---------|
| `OPENAI_API_KEY` | Yes* | OpenAI API key | `sk-...` |
| `ANTHROPIC_API_KEY` | No | Anthropic API key | `sk-ant-...` |
| `GEMINI_API_KEY` | No | Google Gemini API key | `AIza...` |
| `MISTRAL_API_KEY` | No | Mistral API key | `...` |
| `OLLAMA_BASE_URL` | No | Ollama endpoint | `http://localhost:11434` |
| `SPACE_DATA_DIR` | No | Data directory | `/data` |
| `SPACE_LOG_LEVEL` | No | Log level | `info` |
| `SPACE_MAX_CYCLES` | No | Max improvement cycles | `100` |

*Required for at least one LLM provider.

---

## 7. Monitoring & Observability

### 7.1 Structured Logging Schema

```json
{
  "timestamp": "2026-07-25T14:30:00.000Z",
  "level": "info",
  "component": "evaluator",
  "session_id": "s_0042",
  "cycle_id": "c_0017",
  "artifact_id": "a_0003",
  "event": "evaluation_complete",
  "data": {
    "scores": { "accuracy": 0.87, "latency": 0.92, "cost": 0.78 },
    "delta": { "accuracy": 0.05, "latency": -0.01, "cost": 0.02 },
    "confidence": 0.91,
    "duration_ms": 2340
  }
}
```

### 7.2 Metrics Collection

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `rsi_cycle_duration_seconds` | Histogram | session_id | Improvement cycle duration |
| `rsi_score_delta` | Gauge | session_id, artifact_id, dimension | Score change per modification |
| `rsi_safety_rejections_total` | Counter | session_id, rule_id | Safety rejections |
| `rsi_api_calls_total` | Counter | provider, model, status | LLM API call count |
| `rsi_api_latency_seconds` | Histogram | provider, model | LLM API latency |
| `rsi_api_cost_dollars` | Counter | provider, model | LLM API cost |
| `rsi_convergence_velocity` | Gauge | session_id | Current improvement velocity |
| `rsi_artifact_versions` | Gauge | project_id | Total artifact versions |
| `rsi_active_loops` | Gauge | — | Currently running loops |
| `rsi_rollback_total` | Counter | session_id | Automatic rollbacks |

### 7.3 Alerting Rules

| Alert | Condition | Severity | Action |
|-------|-----------|:--------:|--------|
| High safety rejection rate | > 5/hour | Warning | Investigate Modifier behavior |
| Evaluation score decline | < -0.1 over 10 cycles | Critical | Pause loop, human review |
| API error rate | > 5% over 5 minutes | Warning | Check API keys, rate limits |
| Loop stuck | No cycle completion in 10 minutes | Warning | Check for deadlocks |
| Convergence timeout | > 100 cycles without convergence | Info | Review convergence threshold |
| Storage capacity | > 80% of allocated | Warning | Archive old data |
| Cost overrun | > daily budget threshold | Warning | Pause non-critical loops |

---

## 8. Testing Architecture

### 8.1 Test Pyramid

```
        ╱╲
       ╱ E2E╲          5% — Full improvement loop on toy problem
      ╱──────╲
     ╱ Integr.╲        25% — Module interaction tests
    ╱──────────╲
   ╱   Unit     ╲      70% — Individual module tests
  ╱──────────────╲
```

### 8.2 Test Categories

| Category | Count | Coverage Target | Tools |
|----------|:-----:|:---------------:|-------|
| Unit tests | 80+ | 90% line coverage | Vitest |
| Integration tests | 20+ | All module interactions | Vitest |
| E2E tests | 5+ | Full improvement loop | Vitest + manual |
| Security tests | 10+ | All safety rules | Custom + Vitest |
| Performance tests | 5+ | Latency budgets | Custom benchmarks |

### 8.3 Self-Improvement Testing

The RSI system tests itself by running controlled improvement loops:

```typescript
// Test: Self-improvement convergence
test('RSI loop converges on toy prompt optimization', async () => {
  const loop = createImprovementLoop({
    artifact: simplePrompt,
    criteria: basicCriteria,
    max_cycles: 50,
    safety: relaxedSafety  // For testing only
  });
  
  const result = await loop.run();
  
  expect(result.converged).toBe(true);
  expect(result.final_score).toBeGreaterThan(result.initial_score);
  expect(result.safety_violations).toBe(0);
  expect(result.rollback_count).toBeLessThan(5);
});
```

---

## 9. Technical Architecture Summary

The RSI technical architecture is:

- **6-layer design** — Presentation → Orchestration → Engine → Integration → Persistence → Foundation
- **Hybrid storage** — SQLite for metadata + JSON files for artifacts
- **5 LLM providers** — OpenAI, Anthropic, Gemini, Mistral, Ollama via unified interface
- **I/O-bound** — investment in network resilience, not raw compute
- **< 1GB data** at current scale, archival after 10K cycles
- **Docker deployment** with CI/CD via GitHub Actions
- **Comprehensive monitoring** — structured logs, Prometheus metrics, Grafana dashboards
- **70/25/5 test pyramid** — heavy unit testing, moderate integration, light E2E
- **Self-testing** — the system validates its own improvement capability

The architecture deliberately keeps infrastructure simple so the complexity of RSI lives in the recursive logic, not the plumbing.

---

*Derived from: All 67 SPACE artifacts, all 67 open-ended answers, cross-referenced with 04-technical-substrate.md*
*SPACE — Superb Prompt Automatic Creation Engine v2.1.0*
