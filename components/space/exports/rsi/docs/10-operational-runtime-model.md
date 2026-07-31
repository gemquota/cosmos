# 10 — Operational Runtime Model: Session Lifecycle, Configuration, and Runtime Behavior of RSI

> **Analytical Lens:** Operational (Tier 2 — Exhaustive)
> **Supersedes:** 05-operational-lifecycle.md (extends with runtime behavioral model)
> **Source Artifacts:** All 67 SPACE artifacts + 67 open-ended answers
> **Derivation Depth:** Full artifact cross-referencing

---

## 1. Session Lifecycle — Complete Model

### 1.1 Session States

```
                    ┌──────────────┐
                    │   Created    │
                    └──────┬───────┘
                           │ session.initialize()
                           ▼
                    ┌──────────────┐
                    │  Configured  │
                    └──────┬───────┘
                           │ session.loadArtifacts()
                           ▼
                    ┌──────────────┐
                    │   Loaded     │
                    └──────┬───────┘
                           │ session.startLoop()
                           ▼
                    ┌──────────────┐
              ┌─────│   Running    │─────┐
              │     └──────┬───────┘     │
              │            │             │
              │     loop.converge()      │ loop.pause()
              │            │             │
              │            ▼             ▼
              │     ┌──────────────┐  ┌──────────────┐
              │     │  Converged   │  │   Paused     │
              │     └──────┬───────┘  └──────┬───────┘
              │            │                  │
              │            │ session.export()  │ session.resume()
              │            │                  │
              │            ▼                  └──→ Running
              │     ┌──────────────┐
              │     │  Exported    │
              │     └──────┬───────┘
              │            │
              │     loop.terminate() │ loop.error()
              │            │                  │
              │            ▼                  ▼
              │     ┌──────────────┐  ┌──────────────┐
              └────▶│  Terminated  │◀─│    Error     │
                    └──────────────┘  └──────────────┘
```

### 1.2 Session Lifecycle Events

| Event | Trigger | From State | To State | Side Effects |
|-------|---------|:----------:|:--------:|-------------|
| `initialize` | `space init` | — | Created | Project directory created |
| `configure` | Config load | Created | Configured | Config validated, defaults applied |
| `loadArtifacts` | Artifact scan | Configured | Loaded | Artifacts indexed, scores computed |
| `startLoop` | `space run` | Loaded | Running | ImprovementLoop created |
| `cycleComplete` | Cycle end | Running | Running | History appended, metrics updated |
| `pause` | Human intervention | Running | Paused | Active operations complete gracefully |
| `resume` | `space run --resume` | Paused | Running | Loop state restored from snapshot |
| `converge` | ConvergenceDetector | Running | Converged | Summary generated, artifacts archived |
| `export` | `space export` | Converged | Exported | Specification generated (MD/JSON/HTML) |
| `terminate` | Manual or max cycles | Running/Converged/Exported | Terminated | Cleanup, final snapshot |
| `error` | Unrecoverable failure | Running | Error | Error logged, partial state preserved |

### 1.3 Session Resume Model

```
RESUME FLOW:
  1. Locate: Find latest snapshot in .space/snapshots/
  2. Validate: Check snapshot integrity (hash chain)
  3. Restore: Load session state from snapshot
  4. Reconnect: Restore LLM provider connections
  5. Resume: Continue from last completed cycle
  
  SNAPSHOT CONTENTS:
  - Session state (cycle number, artifact states)
  - Evaluator state (scores, confidence levels)
  - Modifier state (last proposal, self-modification depth)
  - SafetyGuard state (dynamic patterns learned)
  - ConvergenceDetector state (velocity, trajectory)
  - History state (last N records for context)
  
  SNAPSHOT TRIGGERS:
  - Every 10 cycles (automatic)
  - Before pause (graceful)
  - Before terminate (final)
  - On error (crash recovery)
```

---

## 2. Configuration Architecture

### 2.1 Configuration Hierarchy

```
Priority (highest to lowest):
  1. CLI flags          — override everything
  2. Environment vars   — secrets only
  3. Project config     — .space/config.yaml
  4. User config        — ~/.space/config.yaml
  5. System defaults    — hardcoded in config/defaults.ts
```

### 2.2 Complete Configuration Schema

```yaml
# .space/config.yaml — Full Configuration Reference

# Project identity
project:
  name: "recursive-self-improvement"
  description: "RSI system specification"
  version: "1.0.0"

# Loop parameters
loop:
  max_cycles: 100                    # Maximum improvement cycles
  max_iterations_per_artifact: 3     # Max modification attempts per hypothesis
  convergence_threshold: 0.01        # Minimum improvement to continue
  convergence_window: 10             # Cycles to consider for convergence
  min_cycles_before_convergence: 10  # Prevent premature termination
  snapshot_interval: 10              # Snapshot every N cycles

# Evaluator configuration
evaluator:
  dimensions:
    - name: accuracy
      weight: 0.4
      min: 0.0
      max: 1.0
    - name: latency
      weight: 0.2
      min: 0.0
      max: 1.0
    - name: cost
      weight: 0.2
      min: 0.0
      max: 1.0
    - name: safety
      weight: 0.2
      min: 0.0
      max: 1.0
  confidence_threshold: 0.8
  evaluation_depth: 3
  provider: openai
  model: gpt-4o

# Modifier configuration
modifier:
  type: prompt                        # prompt | code | strategy | config
  granularity: fine                   # fine | coarse
  safety_level: moderate              # conservative | moderate | aggressive
  temperature: 0.3
  max_tokens: 4096
  provider: openai
  model: gpt-4o
  self_modification:
    enabled: true
    max_depth: 3
    validation_cycles: 3
    require_human_approval: true

# Safety configuration
safety:
  max_latency_increase_pct: 10
  max_accuracy_decrease_pct: 2
  static_rules:
    - id: SR-001
      condition: "contains_credentials"
      action: block
      description: "Block modifications containing credentials"
    - id: SR-002
      condition: "latency_increase > 10%"
      action: block
      description: "Block modifications increasing latency > 10%"
    - id: SR-003
      condition: "accuracy_decrease > 2%"
      action: revert
      description: "Revert modifications decreasing accuracy > 2%"
    - id: SR-004
      condition: "self_modifies_safety_rules"
      action: block
      description: "Block self-modification of safety rules"
    - id: SR-005
      condition: "modifies_benchmarks"
      action: block
      description: "Block modification of benchmarks"
  dynamic_guard:
    enabled: true
    confidence_threshold: 0.7
    pattern_history_size: 1000

# LLM provider configuration
llm:
  providers:
    openai:
      api_key_env: OPENAI_API_KEY
      base_url: https://api.openai.com/v1
      models: [gpt-4o, gpt-4o-mini]
      rate_limit: 100  # requests per minute
      timeout: 30000   # milliseconds
    anthropic:
      api_key_env: ANTHROPIC_API_KEY
      base_url: https://api.anthropic.com
      models: [claude-3-5-sonnet-20241022]
      rate_limit: 50
      timeout: 30000
    gemini:
      api_key_env: GEMINI_API_KEY
      base_url: https://generativelanguage.googleapis.com/v1beta
      models: [gemini-pro]
      rate_limit: 60
      timeout: 30000
    mistral:
      api_key_env: MISTRAL_API_KEY
      base_url: https://api.mistral.ai/v1
      models: [mistral-large-latest]
      rate_limit: 60
      timeout: 30000
    ollama:
      base_url_env: OLLAMA_BASE_URL
      base_url: http://localhost:11434
      models: [llama3, codellama]
      rate_limit: 10
      timeout: 60000
  default_provider: openai
  fallback_chain: [openai, anthropic, ollama]

# Storage configuration
storage:
  type: filesystem                    # filesystem | sqlite (planned)
  base_path: .space
  artifact_path: .space/artifacts
  session_path: .space/sessions
  snapshot_path: .space/snapshots
  backup_interval: 6h
  retention_days: 90

# Monitoring configuration
monitoring:
  logging:
    level: info                       # debug | info | warn | error
    format: json                      # json | text
    output: stdout                    # stdout | file | both
    file_path: .space/logs/rsi.log
  metrics:
    enabled: true
    provider: prometheus
    port: 9090
  dashboard:
    enabled: true
    provider: grafana
    port: 3001

# Development configuration
development:
  benchmark:
    enabled: true
    artifacts: 5                      # Number of test artifacts
    cycles: 20                        # Max cycles for benchmark
  mock_llm: false                     # Use mock LLM for testing
  verbose: false                      # Verbose logging
```

---

## 3. Runtime Behavior Model

### 3.1 Event Loop

The RSI system runs on an **event-driven runtime** with the following event sources:

| Event Source | Events | Handler |
|-------------|--------|---------|
| CLI commands | init, run, export, list, framework, status | CommandRouter |
| ImprovementLoop | cycle_complete, convergence, error | LoopManager |
| LLM Providers | response, error, rate_limit | ProviderPool |
| SafetyGuard | approval, rejection, flag | SafetyManager |
| Storage | write_complete, error | StorageManager |
| Human operator | pause, resume, override | OperatorInterface |

### 3.2 Concurrency Model

```
┌─────────────────────────────────────────────────────────────┐
│                    MAIN THREAD                               │
│  Event loop, CLI processing, state management               │
├─────────────────────────────────────────────────────────────┤
│                    WORKER POOL                               │
│  Improvement loop execution (1-3 concurrent)                │
│  Each worker: select → analyze → hypothesize → review →     │
│               apply → evaluate → compare → decide            │
├─────────────────────────────────────────────────────────────┤
│                    I/O POOL                                  │
│  LLM API calls (async, non-blocking)                        │
│  File system operations (async)                              │
│  Network requests (async)                                    │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 State Management

```
Global State:
  - active_sessions: Map<SessionId, Session>
  - active_loops: Map<LoopId, ImprovementLoop>
  - provider_pool: ProviderPool
  - storage: StorageProvider
  - config: SpaceConfig

Session State (per session):
  - artifacts: Artifact[]
  - criteria: EvaluationCriteria
  - safety_guard: SafetyGuard
  - history: History
  - loop: ImprovementLoop

Immutable State:
  - StaticGuard rules (never change)
  - EvaluationCriteria (immutable within session)
  - History records (append-only)
  - Artifact version chains (append-only)
```

---

## 4. Resource Management

### 4.1 API Budget Management

```typescript
interface APIBudget {
  daily_limit: number;        // Maximum daily spend
  current_spend: number;      // Current day spend
  per_request_limit: number;  // Maximum per-request cost
  alert_threshold: number;    // Alert when spend exceeds this
  pause_threshold: number;    // Pause loops when spend exceeds this
}

// Budget enforcement
function checkBudget(provider: string, estimatedTokens: number): boolean {
  const estimatedCost = estimateCost(provider, estimatedTokens);
  if (budget.current_spend + estimatedCost > budget.pause_threshold) {
    pauseAllLoops('budget_exceeded');
    return false;
  }
  if (budget.current_spend + estimatedCost > budget.alert_threshold) {
    alert('approaching_budget_limit');
  }
  return true;
}
```

### 4.2 Memory Management

| Component | Memory Strategy | Cleanup |
|-----------|----------------|---------|
| History records | Append-only, stream processing | Archive after 10K cycles |
| LLM responses | Parse and discard raw response | GC after extraction |
| Artifact versions | Lazy loading, cache current version | Archive old versions |
| Evaluation results | Keep last N per artifact | Archive older results |
| Safety patterns | Bounded pattern set | Evict least-used patterns |

### 4.3 Disk Management

```
Disk usage growth model:
  Per cycle: ~5KB (modification record + artifact diff)
  Per session: ~500KB (100 cycles × 5KB)
  Per project: ~5MB (10 sessions × 500KB)
  Total at 10K cycles: ~50MB active + archived

Archival policy:
  Active: Last 1K cycles (~5MB)
  Warm: 1K-10K cycles, compressed (~10MB)
  Cold: > 10K cycles, archived (~20MB compressed)
```

---

## 5. Team Operations Model

### 5.1 Team Structure (2-3 People)

| Role | Primary Responsibilities | On-Call | Decision Authority |
|------|------------------------|:-------:|-------------------|
| **Systems Engineer** | Core loop, safety mechanisms, convergence | Yes | Architecture (RFC process) |
| **ML Engineer** | LLM integration, evaluation framework, prompting | Yes | ML/model choices |
| **Infra (part-time)** | CI/CD, monitoring, deployment, storage | No | Infrastructure choices |

### 5.2 Development Cadence

| Activity | Frequency | Duration | Participants |
|----------|:---------:|:--------:|:------------:|
| Standup | Daily | 15 min | All |
| Sprint planning | Bi-weekly | 1 hour | All |
| Sprint review/demo | Bi-weekly | 30 min | All + stakeholders |
| Architecture review | As needed | 1-2 hours | Systems + ML |
| Incident post-mortem | After incidents | 1 hour | All |
| Dependency audit | Weekly | 30 min | Infra |
| Benchmark review | Weekly | 30 min | ML |

### 5.3 Communication Protocol

| Channel | Purpose | Response Time |
|---------|---------|:-------------:|
| GitHub Issues | Feature requests, bugs | 24 hours |
| GitHub PRs | Code review, merge | 4 hours (business hours) |
| Slack/Teams | Quick questions, updates | 1 hour (business hours) |
| ADR documents | Architecture decisions | 48 hours for review |
| RFC documents | Major changes | 1 week for comment |
| Incident Slack | Active failures | Immediate |

---

## 6. Maintenance Operations

### 6.1 Scheduled Maintenance

| Task | Frequency | Duration | Automation |
|------|:---------:|:--------:|:----------:|
| Dependency updates | Weekly | 1-2 hours | Automated (Dependabot) |
| Security patches | As needed | 1-4 hours | Manual review |
| Database vacuum | Weekly | 15 min | Automated |
| Log rotation | Daily | — | Automated |
| Backup verification | Weekly | 30 min | Automated |
| Benchmark refresh | Monthly | 4-8 hours | Semi-automated |
| Performance audit | Monthly | 2-4 hours | Manual |
| Capacity planning | Quarterly | 4-8 hours | Manual |

### 6.2 Backup Strategy

| Data | Method | Frequency | Retention | Recovery Time |
|------|--------|:---------:|:---------:|:-------------:|
| SQLite database | File copy to cloud | 6 hours | 90 days | < 5 min |
| Artifact JSON files | Git commits | Every commit | Indefinite | < 1 min |
| Configuration files | Git | Every change | Indefinite | < 1 min |
| Log files | Compressed archive | Daily | 30 days | < 10 min |
| Snapshots | File copy | Every 10 cycles | 30 days | < 2 min |

### 6.3 Disaster Recovery

| Scenario | Detection | Response | Recovery |
|----------|-----------|----------|----------|
| **Data corruption** | Hash chain verification failure | Halt affected loop | Restore from backup |
| **Storage failure** | Write error | Switch to in-memory fallback | Restore from backup |
| **API provider outage** | Health check failure | Switch to fallback provider | Resume when healthy |
| **Full disk** | Capacity alert | Archive old data, pause non-critical loops | Clean up, resume |
| **Configuration drift** | Immutability check failure | Reject change, log | Session restart |
| **Process crash** | Missing heartbeat | Auto-restart from last snapshot | Resume from snapshot |

---

## 7. Operational Runtime Summary

The RSI operational model provides:

- **11 session states** with defined transitions and side effects
- **5-level configuration hierarchy** (CLI → env → project → user → defaults)
- **Full configuration schema** with 50+ parameters across 8 categories
- **Event-driven runtime** with worker pool concurrency
- **Budget-aware resource management** with automatic pause on overspend
- **2-3 person team** with clear roles, cadence, and communication protocols
- **Scheduled maintenance** with 8 recurring tasks
- **Disaster recovery** with 6 scenario playbooks
- **Session resume** from snapshots with hash-chain integrity verification

The operational philosophy mirrors the system's philosophy: **small, continuous, reversible improvements** to both the system and the process of building it.

---

*Derived from: All 67 SPACE artifacts, all 67 open-ended answers, cross-referenced with 05-operational-lifecycle.md*
*SPACE — Superb Prompt Automatic Creation Engine v2.1.0*
