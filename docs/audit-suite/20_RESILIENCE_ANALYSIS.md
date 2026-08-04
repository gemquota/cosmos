# 20 — Resilience & Recovery Analysis

**Doc ID:** COSMOS-AUDIT-20 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [19 Reliability](19_RELIABILITY_ANALYSIS.md) · [29 Risk Register](29_RISK_REGISTER.md)

---

## 1. Checkpoint-Before-Mutation (Observed)

`rsis/checkpoint.py` `CheckpointManager`:

- Ensures the workspace is a git repo (`init -b main` if missing). [O]
- Commits `rsis-checkpoint: <message>` before destructive/mutating operations. [O]
- `CONFIG.checkpoint_before_mutation` gates L2 candidate submission and application. [O]
- The checkpoint **is** the rollback primitive; there is no file-level undo layer. [O]

## 2. Recovery Triple Pattern (Observed)

`rsis/recovery.py`:

1. **Checkpoint rollback** — return the workspace to the pre-mutation commit.
2. **Human-in-the-loop** — notify via configured channel; recovery can pause.
3. **Fallback interpreter** — alternate executor when the primary path is unavailable.

Failure counting (`_max_failures = 3`) triggers cascading-failure escalation; `check-practices`
enforces workspace/loop hygiene after runs. [O]

## 3. Self-Healing Signals (Observed)

| Mechanism | Site | Covers |
|---|---|---|
| Retry + backoff | L1 tools, DAG, priority pool | transient LLM/tool failures |
| Budget caps | `timeout.py` + cost ledger | runaway sessions / spend |
| Deadlock guard | pipeline + priority pool | unresolvable DAGs |
| Graceful degradation | L2 sequential fallback | `parallel_candidates=0` default |
| Rebuild scripts | `gen-static-data.py --check` | stale snapshot detection |

## 4. Resilience Gaps

- **Atomic state writes:** pulse/state JSON writes are plain file writes; a crash mid-write
  corrupts the file (no journal, no temp+rename). [I, Med]
- **No process supervision:** daemon processes (`server.py`, wiki daemon, heartbeat.mjs) have
  no restart-on-failure wrapper in-repo. [O]
- **Single checkpoint chain:** git commits are the only rollback; no periodic prune/GC policy
  for checkpoint commits. [O]
- **Fallback interpreter is a stub:** configured path exists, but no in-repo fallback engine
  is implemented. [O]

## 5. Recommendations

1. Introduce `atomic_json_write(path, data)` used by every pulse/state writer (temp file +
   `os.replace` + `fsync`) — highest-leverage resilience fix.
2. Wrap daemons with a tiny supervisor (or document `systemd`/`run-one` usage) for
   restart-on-exit.
3. Add a checkpoint GC policy (keep last N; prune older `rsis-checkpoint:` commits).
4. Promote the fallback interpreter from a stub to the deterministic stub-evaluator path so
   the chain degrades gracefully instead of failing.
