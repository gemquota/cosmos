# 23 — Logging & Monitoring Analysis

**Doc ID:** COSMOS-AUDIT-23 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [00 Executive Summary](00_EXECUTIVE_SUMMARY.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [31 Deployment](31_DEPLOYMENT_AUDIT.md)

---

## 1. Logging Architecture (Observed)

- `main.py` configures the root logger (timestamped format, console + file handlers). [O]
- Modules log via `logging.getLogger(__name__)`; retry/failure paths log WARNING/ERROR with
  task context. [O]
- `TelemetryCollector` (`.rsis/telemetry/`) buffers events and flushes periodically to JSONL
  (session-scoped, `flush_interval_s`). [O]
- `CostLedger` records LLM spend with budget caps and halt callbacks. [O]
- `EventBus` (Phase D2) provides topic-based pub/sub (`worker.*`, `worker.priority_tick`);
  the L2 session bridges events into telemetry. [O]

## 2. Telemetry Surface

| Stream | Source | Consumed by |
|---|---|---|
| `l2_*` events | `loop_l2.py` | telemetry JSONL |
| `worker.task.*` | priority pool (D2) | telemetry bridge → JSONL |
| `dag_task*` | `pipeline.py` demo | demo stdout |
| Pulses | `rack/pulses/*.json` | dashboard telemetry tabs |
| Cost events | `CostLedger` | budget caps + dashboard |

## 3. Monitoring & Alerting (Observed)

- Dashboard renders pulses, layers, success rate, and constraint states from JSON snapshots. [O]
- `stats.html` exposes wiki statistics; `stub-audit.html` surfaces stub coverage. [O]
- **No alerting:** nothing raises an alarm on loop failure cascades, budget exhaustion, or
  telemetry gaps; humans must open the dashboard. [O]
- **No log retention/rotation policy** documented in-repo; `.rsis/telemetry` grows unbounded. [I, Med]

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| M-1 | No alerting on failure cascades / budget halt | Med |
| M-2 | Telemetry files unbounded; no retention/rotation | Med |
| M-3 | No correlation ID across logs, telemetry, and pulses | Low |
| M-4 | `event_bus` history is in-memory only (max 250/topic) — dashboards can't replay after restart | Low |
| M-5 | Pulse files are plain JSON without schema versioning | Low |

## 5. Recommendations

1. Add a `monitor` command that reads `.rsis/telemetry` + pulses and exits non-zero on
   failure-cascade/budget signals (cron/systemd friendly).
2. Rotate telemetry by day with a retention window config.
3. Emit a `session_id` in every TelemetryEvent (already present in the collector) and thread
   it through logs via a logging filter.
4. Persist the EventBus history ring to `.rsis/events/` (bounded) so dashboards can replay
   `worker.*` events across restarts.
