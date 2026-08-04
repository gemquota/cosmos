# 11 — Dependency Analysis

**Doc ID:** COSMOS-AUDIT-11 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [06 Module-by-Module](06_MODULE_BY_MODULE_AUDIT.md) · [24 Dependency Audit](24_DEPENDENCY_AUDIT.md) · [28 Technical Debt](28_TECHNICAL_DEBT_REGISTER.md)

---

## 1. Component-Level Dependency Graph

```
RSIS3 ----------► MyKB   (FS: .rsis/*, syntheses via hooks; documented bridge)
RSIS3 ----------► SPACE  (FS: RRP pulses in rack/pulses + .rsirrp/work)
SPACE ----------► exports (spec JSON)
Dashboard --------► dashboard-data.json (gen-static-data.py)
heartbeat --------► watches.json
```

No Python source imports across component boundaries (import bases are disjoint). [O]

## 2. Intra-Component Import Graph (Python file→file, top 40 by weight)

| From | To | Uses |
|------|----|------|
| `main` | `app` | 2 |
| `check_practices` | `practices` | 1 |
| `run_rrp_pulse` | `rrp_engine` | 1 |
| `run_rrp_pulse` | `config` | 1 |
| `run_rrp_pulse` | `memory` | 1 |
| `run_rrp_pulse` | `telemetry` | 1 |
| `__main__` | `main` | 1 |
| `app` | `config` | 1 |
| `app` | `extrapolation` | 1 |
| `app` | `memory` | 1 |
| `evaluator` | `config` | 1 |
| `evaluator` | `telemetry` | 1 |
| `extrapolation` | `config` | 1 |
| `loop_l1` | `checkpoint` | 1 |
| `loop_l1` | `config` | 1 |
| `loop_l1` | `error_classifier` | 1 |
| `loop_l1` | `telemetry` | 1 |
| `loop_l1` | `__init__` | 1 |
| `loop_l2` | `checkpoint` | 1 |
| `loop_l2` | `config` | 1 |
| `loop_l2` | `evaluator` | 1 |
| `loop_l2` | `event_bus` | 1 |
| `loop_l2` | `loop_l1` | 1 |
| `loop_l2` | `priority_pool` | 1 |
| `loop_l2` | `recovery` | 1 |
| `loop_l2` | `scheduler` | 1 |
| `loop_l2` | `shared_memory` | 1 |
| `loop_l2` | `telemetry` | 1 |
| `loop_l2` | `timeout` | 1 |
| `loop_l3` | `config` | 1 |
| `loop_l3` | `extrapolation` | 1 |
| `loop_l3` | `memory` | 1 |
| `loop_l3` | `telemetry` | 1 |
| `loop_l3` | `timeout` | 1 |
| `loop_l4` | `checkpoint` | 1 |
| `loop_l4` | `config` | 1 |
| `loop_l4` | `evaluator` | 1 |
| `loop_l4` | `memory` | 1 |
| `loop_l4` | `telemetry` | 1 |
| `loop_l4` | `timeout` | 1 |

## 3. Circular Dependency Report (RSIS3 `rsis/` package)

- **No import cycles** in the RSIS3 core package (DFS over file-level imports). [O]

## 4. Fan-in / Fan-out (RSIS3 core modules)

| Module | Fan-in | Fan-out |
|--------|--------|---------|
| `__init__` | 1 | 0 |
| `__main__` | 0 | 1 |
| `checkpoint` | 10 | 0 |
| `config` | 19 | 0 |
| `app` | 1 | 3 |
| `error_classifier` | 3 | 0 |
| `evaluator` | 8 | 2 |
| `event_bus` | 2 | 0 |
| `extrapolation` | 3 | 1 |
| `loop_l1` | 2 | 5 |
| `loop_l2` | 1 | 11 |
| `loop_l3` | 1 | 5 |
| `loop_l4` | 5 | 6 |
| `loop_l5` | 1 | 7 |
| `loop_l6` | 1 | 8 |
| `loop_l7` | 1 | 7 |
| `loop_l8` | 1 | 6 |
| `loop_l9` | 1 | 7 |
| `main` | 1 | 22 |
| `memory` | 9 | 1 |
| `pipeline` | 2 | 1 |
| `practices` | 1 | 1 |
| `priority_pool` | 1 | 3 |
| `recovery` | 2 | 2 |
| `resource_monitor` | 1 | 2 |
| `scheduler` | 2 | 0 |
| `shared_memory` | 1 | 0 |
| `telemetry` | 12 | 1 |
| `timeout` | 9 | 0 |
| `__init__` | 1 | 6 |
| `base` | 4 | 0 |
| `hitl` | 2 | 0 |
| `manager` | 1 | 2 |
| `sandbox` | 1 | 1 |
| `workspace_tools` | 1 | 1 |

## 5. Third-Party Dependency Footprint

- **Python:** stdlib dominates; optional `psutil`, `pytest`; lazy `docker`, `RestrictedPython`. [O]
- **TypeScript:** 7 runtime deps (commander, chalk, inquirer, js-yaml, ora, sql.js, uuid) + 9 dev deps. [O]
- **Bash/Node glue:** `pgrep`, `fuser`, `python3`, `node`, `nohup`. [O]

## 6. Key Findings

- High intra-package coupling in `rsis/` (loop_* ⇄ memory/telemetry/tools), balanced by near-zero external coupling. [I, Med]
- SPACE has minimal, mostly-benign runtime deps; sql.js bundles WASM (~1.5 MB) — the only heavy artifact. [I, Low]
- Dependency graph is small and auditable; no nested/monorepo nightmare. [O]

---
*End of document 11. Next: [12 Data Model Analysis](12_DATA_MODEL_ANALYSIS.md).*