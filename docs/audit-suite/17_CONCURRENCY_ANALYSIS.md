# 17 — Concurrency Analysis

**Doc ID:** COSMOS-AUDIT-17 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [09 Control Flow](09_CONTROL_FLOW_ANALYSIS.md) · [18 Security](18_SECURITY_AUDIT.md) · [19 Reliability](19_RELIABILITY_ANALYSIS.md)

---

## 1. Concurrency Model Inventory

| Site | Model | Sync primitive | Notes (observed) |
|---|---|---|---|
| ResourceEnforcer | background thread | per-iteration sleep/poll | `threading.Thread` daemon in `resource_monitor.py`; set_rlimit in sandbox child is fork-safe |
| TelemetryCollector | background thread | interval flush | flush interval configurable |
| SharedMemoryManager | shared dict + lock | `threading.Lock` (or RLock) | per-session candidate gather |
| L2 parallel candidates | optional DAG fan-out | assignment/partition | controlled by `parallel_candidates` config |
| rack/server.py | ThreadingTCPServer | thread-per-connection | 0.0.0.0, unbounded thread growth |
| mykb server / search daemon | HTTPServer (socketserver) | thread-per-connection (default) | single-request serialization in search due GIL |
| heartbeat.mjs | single Node event loop | async interval | single-process poller |
| SPACE web server | synchronous Node | — | blocking exports |

## 2. Lock Contention & Race Analysis

- **SharedMemoryManager:** sorted gather with lock — races mitigated, but no atomic read-modify-write
  across multiple candidates (last-writer-wins on shared context). [I, Med]
- **Pulse JSON writes:** multiple loops append to `rack/pulses/`; writes are file-append (not atomic).
  Concurrent writers risk interleaved/corrupt JSON. **Not protected by a lock/atomic rename** [I, High].
- **State files (`.rsis/*.json`):** read at start and written by tuning cycles; no file lock → possible
  torn reads if a tuning cycle writes while another reads. [I, Med]
- **Dashboard regeneration (gen-static-data.py):** reads pulses while loops may write → inconsistent
  snapshot. [I, Med]

## 3. TOCTOU / Atomicity Findings

- No use of `os.replace`/atomic write + fsync for pulse/state files found. [O]
- The `subprocess.run` in mykb/server for temporal engine may overlap server request threads — each
  invocation spawns a Python process (expensive but isolated). [I, Low]

## 4. Async Model

- Python: no asyncio in core; SPACE: single-threaded synchronous Node; no worker threads/pools. [O]
- Parallelism only at process level (tool sandbox via subprocess; L2 DAG). [O]

## 5. Scheduling

- `scheduler.py` demo + `priority_pool.py` implement cooperative scheduling for improvement candidates.
- OS scheduler manages threads/processes; no CFS/cgroup tuning except Docker `nano_cpus` caps. [O]

## 6. Recommended Fixes

1. **Atomic writes:** helper to write JSON via temp file + `os.replace` + `fsync`, applied to pulses,
   dashboard-data.json, state files. [P0]
2. **Single-writer discipline:** designate one process (or one lock) to own `rack/pulses/` writes. [P0]
3. **Thread cap** on rack/server.py `ThreadingTCPServer` (`request_queue_size`) to bound resource use. [P1]
4. **Async for SPACE web exports** (or move heavy exporters to a worker). [P2]

---
*End of document 17. Next: [18 Security Audit](18_SECURITY_AUDIT.md).*
