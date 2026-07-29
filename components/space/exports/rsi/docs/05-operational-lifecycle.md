# 05 — Operational Lifecycle: How the RSI System Lives

> **Analytical Lens:** Operational — deployment, monitoring, maintenance, and stewardship
> **Source Artifacts:** deployment_process, environment_management, monitoring_plan, runtime_configuration, maintenance_policy, stewardship_plan, development_cadence, team_composition, quality_practices, debt_management, communication_patterns, decision_making

---

## 1. Team Composition

### 1.1 Small Team: 2-3 People

| Role | Responsibility | Focus |
|------|---------------|-------|
| **Systems Engineer** | Core loop, safety mechanisms | Recursive logic, rollback, convergence |
| **ML Engineer** | LLM integration, evaluation framework | Prompt engineering, scoring, benchmarking |
| **Part-time Infra** | Monitoring, deployment, CI/CD | Dashboards, pipelines, alerting |

**Decision-making speed:** Fast with this team size. We favor shipping over perfection. The recursive improvement philosophy applies to the team's own process — small, continuous improvements to how we work.

---

## 2. Development Cadence

### 2.1 Continuous (CI/CD)

- **Every commit:** TypeScript compilation checks + unit tests
- **Integration tests:** Full improvement loops on small benchmarks (5-10 artifacts, 20-30 cycles), verifying convergence properties
- **Nightly builds:** Full benchmark suite to detect performance regressions
- **Weekly demos:** Synchronous sessions showing improvement progress

### 2.2 Boy Scout Rule

Every time we touch a module for feature work, we clean up any tech debt we encounter. The RSI domain evolves fast; trying to batch-refactor risks falling behind. Small, continuous improvements to code quality mirror the recursive improvement philosophy of the system itself.

---

## 3. Communication Patterns

### 3.1 Async-First

- **Design decisions:** Documented as ADRs in the repo, discussed in async threads
- **Escalation:** Only contentious or high-impact decisions get synchronous calls
- **Demo sessions:** Synchronous weekly to maintain shared context
- **Incident response:** Synchronous for active failures, async for post-mortems

### 3.2 Decision-Making: RFC/ADR Process

| Decision Type | Process | Authority |
|---------------|---------|-----------|
| Architecture (core loop, safety, evaluation) | RFC document → team review → consensus | Team |
| API design, naming conventions | Implementing developer decides | Individual |
| EvaluationCriteria changes | Human operator approval required | Human |

**Consensus is the goal; escalation to lead is the fallback.**

---

## 4. Deployment Process

### 4.1 CI/CD Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                    CI/CD PIPELINE                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Push → Lint → TypeCheck → Unit Tests → Integration     │
│    │                                                   │
│    └──→ On merge to main: Build → Publish to registry   │
│         └──→ On tag: Release to npm                     │
│              └──→ Docker build → Deploy to production   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Environment Management

| Environment | Purpose | Data |
|-------------|---------|------|
| **Dev** | Local iteration, rapid prototyping | Full benchmark suite, synthetic data |
| **Production** | Stable improvement loops, overnight runs | Real benchmarks, production data |

**No staging environment.** The improvement loops are their own validation — improvement quality is measured by outcomes, not by matching a staging expectation.

---

## 5. Monitoring Architecture

### 5.1 Structured Logging

Every improvement cycle produces structured JSON logs:
```json
{
  "cycle_id": "c_0042",
  "artifact_id": "a_0017",
  "step": "evaluate",
  "input_state": { "baseline_score": 0.72 },
  "output_state": { "new_score": 0.78 },
  "decision": "accept",
  "confidence": 0.91,
  "timestamp": "2026-07-25T14:30:00Z"
}
```

### 5.2 Metrics (Prometheus)

| Metric | Type | Description |
|--------|------|-------------|
| `rsi_improvement_velocity` | Gauge | Score improvement per cycle |
| `rsi_convergence_rate` | Gauge | Rate of velocity decrease |
| `rsi_safety_rejection_rate` | Counter | SafetyGuard rejections per hour |
| `rsi_api_latency_ms` | Histogram | LLM API call latency |
| `rsi_api_error_rate` | Counter | API failures per hour |
| `rsi_artifact_versions` | Gauge | Total artifact versions in storage |
| `rsi_active_loops` | Gauge | Currently running improvement loops |

### 5.3 Dashboard (Grafana)

Real-time monitoring of active improvement loops:
- Improvement velocity over time (line chart)
- Safety rejection rate (alert threshold: > 5/hour)
- API latency distribution (histogram)
- Artifact score distribution (histogram)
- Convergence detection status (traffic light)

### 5.4 Alerting

| Alert | Threshold | Response |
|-------|-----------|----------|
| Safety rejections > 5/hour | High | Investigate Modifier behavior |
| Evaluation scores dropping | Critical | Pause loop, human review |
| API error rate > 5% | Medium | Check API key, rate limits |
| Convergence not detected after 100 cycles | Low | Review convergence threshold |

---

## 6. Runtime Configuration

### 6.1 Configuration Sources (Priority Order)

1. **CLI flags** — override everything (for debugging)
2. **Environment variables** — secrets only (API keys, database URLs)
3. **Config files (YAML)** — runtime parameters
4. **Defaults** — sensible out-of-the-box settings

### 6.2 Key Configuration Parameters

```yaml
# rsi-config.yaml
loop:
  max_iterations_per_artifact: 3
  max_cycles_per_loop: 100
  convergence_threshold: 0.01
  convergence_window: 10

evaluator:
  dimensions: [accuracy, latency, cost, safety]
  weights: [0.4, 0.2, 0.2, 0.2]
  confidence_threshold: 0.8

safety:
  max_latency_increase_pct: 10
  max_accuracy_decrease_pct: 2
  self_modification_depth_limit: 3

llm:
  provider: openai
  model: gpt-4o
  temperature: 0.3
  max_tokens: 4096
```

### 6.3 Immutability Per Session

Configuration is immutable per improvement session. Changes take effect in new sessions only. This prevents mid-loop configuration drift.

---

## 7. Maintenance Policy

### 7.1 Business Hours Support

- **Active monitoring:** During work hours via Grafana dashboard
- **Alerting:** Automated to Slack for off-hours issues
- **Response time:** Next business day for off-hours alerts
- **Active loop protection:** Loops in progress complete gracefully even during shutdown

### 7.2 Scheduled Maintenance

| Activity | Frequency | Duration |
|----------|:---------:|:--------:|
| Dependency updates | Weekly | 1-2 hours |
| Security patches | As needed | 1-4 hours |
| Benchmark refresh | Monthly | 4-8 hours |
| Database vacuum | Weekly | 15 minutes |
| Log rotation | Daily (automated) | — |

---

## 8. Data Stewardship

### 8.1 Backup Strategy

| Data | Method | Frequency | Retention |
|------|--------|:---------:|:---------:|
| SQLite database | File copy to cloud | Every 6 hours | 90 days |
| Artifact JSON files | Git commits (each improvement is atomic) | Every commit | Indefinite |
| Configuration files | Git | Every change | Indefinite |
| Log files | Compressed archive | Daily | 30 days |

### 8.2 Data Lifecycle

```
Active (last 1K cycles) → Warm (1K-10K cycles, compressed) → Cold (> 10K cycles, archived)
```

**No destructive data lifecycle.** Archived data remains queryable. The system's memory is its most valuable asset — losing improvement history means the system might repeat failed approaches.

---

## 9. Quality Practices

### 9.1 Unit + Integration Tests

- **Unit tests:** Every module (evaluator, modifier, safety guard, convergence detector)
- **Integration tests:** Full improvement loops on toy problems, verifying convergence properties
- **Regression tests:** Benchmark suite run nightly, compared against baseline

### 9.2 Self-Improvement Testing

The RSI system is tested via self-improvement:
- Run the RSI loop on a toy problem (simple prompt optimization)
- Verify that the system converges to a better solution
- Verify that safety guards block dangerous modifications
- Verify that rollback works when modifications cause regression

This is the ultimate validation: **the system must demonstrably improve itself in a controlled setting.**

---

## 10. Operational Summary

The RSI operational lifecycle is:

- **Small team** (2-3 people) with fast decision-making
- **Continuous CI/CD** with nightly benchmark suites
- **Async-first** communication with weekly sync demos
- **Two environments** (dev + production), no staging
- **Prometheus + Grafana** monitoring with alerting
- **YAML configuration** immutable per session
- **Business hours support** with graceful loop completion
- **Git-versioned artifacts** with 90-day backup retention
- **Self-testing** via controlled improvement loops

The operational philosophy mirrors the system's own philosophy: **small, continuous, reversible improvements** — to both the system and the process of building it.

---

*Source: SPACE artifacts deployment_process through stewardship_plan + development_cadence through decision_making (12 artifacts)*
