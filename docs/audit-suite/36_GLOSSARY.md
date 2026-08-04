# 36 — Glossary

**Doc ID:** COSMOS-AUDIT-36 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [03 System Spec](03_SYSTEM_ARCHITECTURE_SPECIFICATION.md) · [35 Appendices](35_APPENDICES.md)

---

## Terms

| Term | Definition |
|---|---|
| **RSIS3** | Recursive Self-Improvement System — the core cognitive engine (L1–L9 loops) in `components/rsis3/`. |
| **L1–L9** | The nine loops: action, improvement, cross-session evolution, meta-parameter optimizer, strategy evolution, identity, meta-cog, meta-meta, MMM. |
| **MyKB** | Long-term memory layer — Obsidian-style wiki with TF-IDF search, graph, and daemon. |
| **SPACE** | RRP ideation engine (TypeScript) generating structured prompt specs. |
| **OKF** | Open Knowledge Format — frontmatter-tagged markdown notes (type/title/tags). |
| **RRP** | Recursive Refinement Protocol — SPACE's prompt-specification refinement loop. |
| **Pulse** | A telemetry datum from RSIS loops stored in `rack/pulses/*.json`. |
| **Synthesis** | A distilled MyKB note (`type: synthesis`) recording durable conclusions. |
| **DAG** | Directed Acyclic Graph — the L2 fan-out/fan-in candidate model. |
| **DAGWorkerPool** | Thread-pool DAG dispatcher in `rsis/pipeline.py` with retry budgets (D1). |
| **Priority pool** | Sync-first AO port (D2): priority scheduling, aging, cooperative preemption, checkpoints. |
| **EventBus** | Thread-safe pub/sub telemetry backbone (D2 port). |
| **SharedMemoryManager** | Race-safe working memory with OCC + atomic mutation (D2 port). |
| **OCC** | Optimistic Concurrency Control — version-checked compare-and-swap. |
| **HITL** | Human-in-the-loop — approval gates for risky operations. |
| **Cost ledger** | Spend tracking with budget caps (`budget_cap_usd`). |
| **Checkpoint** | Git commit before mutation; the rollback primitive. |
| **Fan-out / fan-in** | DAG pattern: planner → N coders → reviewer gate. |
| **Content / Meta** | Binary wiki view: content pages vs system-guidance pages (syntheses, protocols, ops). |
| **Group By** | Sidebar toggle organizing documents by semantic Type or physical Folder. |
| **gh-pages deploy** | Manual tree-sync of `main` into the `gh-pages` branch for GitHub Pages. |
| **AO (Agent OS)** | External ~9.7k-LOC Python multi-agent runtime; selectively ported into RSIS3. |
| **Phase D1–D5** | AO integration roadmap: resilience, concurrency, memory/context, capability, verification. |
