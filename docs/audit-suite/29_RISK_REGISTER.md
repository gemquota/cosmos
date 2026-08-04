# 29 — Risk Register

**Doc ID:** COSMOS-AUDIT-29 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [00 Executive Summary](00_EXECUTIVE_SUMMARY.md) · [16 Memory](16_MEMORY_ANALYSIS.md) · [20 Resilience](20_RESILIENCE_ANALYSIS.md)

---

## 1. Register (Likelihood × Severity = Exposure)

| ID | Risk | L | S | Exposure | Mitigation |
|---|---|---|---|---|---|
| RK-1 | LLM cost runaway in self-improvement loops | M | H | H | cost ledger + `budget_cap_usd` halt |
| RK-2 | Retry loops burn budget on misclassified errors | M | M | M | fatal detection, max-attempt ceilings |
| RK-3 | DAG deadlock on complex dependency graphs | L | H | M | deadlock guard + tests |
| RK-4 | Automated reclassification corrupts wiki taxonomy | M | M | M | checkpoint before mutation, single writer, `--check` |
| RK-5 | Live deploy stale vs main (regression ships) | M | M | M | CI deploy (see [31](31_DEPLOYMENT_AUDIT.md)) |
| RK-6 | Clean-install failure (numpy/networkx mismatch) | H | M | H | fix requirements (see [24](24_DEPENDENCY_AUDIT.md)) |
| RK-7 | Data loss via non-atomic pulse/state writes | M | H | H | atomic writer + fsync |
| RK-8 | XSS via malicious wiki content in viewer | L | H | M | escaping + href allowlist + CSP |
| RK-9 | Evaluator subprocess SPOF | M | M | M | fallback interpreter, graceful degrade |
| RK-10 | Token/credential exposure if `github_tool` ported carelessly | L | H | M | risk=CRITICAL + HITL + no persistence |
| RK-11 | Public repo exposes ops/audit artifacts with internal details | M | L | L | review ops/ contents before publish |
| RK-12 | UI/UX regression unnoticed (no browser E2E) | M | L | L | browser test harness when env allows |

## 2. Top 5 for the next 2 weeks (aligned with [00](00_EXECUTIVE_SUMMARY.md))

1. **RK-6** — fix dependency declarations (cheap, prevents broken environments)
2. **RK-5** — automate deploy (just caused the reported wiki regression)
3. **RK-7** — atomic JSON writes (protects the memory layer)
4. **RK-1** — keep budget caps enforced across all loop entry points
5. **RK-4** — canonical taxonomy writer for reclassification passes

## 3. Escalation Path

- Any risk reaching Exposure H triggers: checkpoint → HITL notification → fallback engine
  (see [20 Resilience](20_RESILIENCE_ANALYSIS.md) for the triple-recovery chain).
