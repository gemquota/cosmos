# 24 — Dependency Audit

**Doc ID:** COSMOS-AUDIT-24 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [01 Repository Overview](01_REPOSITORY_OVERVIEW.md) · [11 Dependency Analysis](11_DEPENDENCY_ANALYSIS.md) · [22 Build & CI](22_BUILD_CI_ANALYSIS.md)

---

## 1. Runtime Dependency Inventory (Observed)

| Dependency | Declared | Actually used | Notes |
|---|---|---|---|
| Python stdlib | (implicit) | yes, dominantly | 90 Python files, 21,659 LOC census; top imports json/os/sys/pathlib/logging/typing/dataclasses |
| `numpy` | commented-out "optional" | **yes** (`rsis/memory.py`) | char n-gram embeddings + similarity search |
| `networkx` | commented-out "optional" | **yes** (`rsis/memory.py`) | knowledge-graph modeling |
| `psutil` | `psutil>=5.9.0` (optional) | yes (resource monitor) | `resource_monitor.py` |
| `pytest` | `pytest>=7.0.0` (dev) | yes | 49-case suite |
| Node | none declared | SPAs are self-contained | no package.json found |
| Git | external tool | yes | checkpoint manager, deploy |

## 2. Critical Finding: Declared vs Used Mismatch

- `components/rsis3/rsis/memory.py` imports `networkx` and `numpy` at module scope, but
  `requirements.txt` has both **commented out** as "optional Phase 2". [O]
- A clean environment that runs `pip install -r requirements.txt` will crash on
  `import rsis.memory`. [I, High]
- `psutil` is likewise marked "optional" while the resource monitor depends on it. [O]

## 3. Transitive / External Surface

- Subprocess calls: git (checkpoints), evaluator subprocess, wiki daemon subprocess
  spawns, sandboxed tool execution. [O]
- Network egress: none from core at import time; LLM calls are the only expected egress
  (env-configured). [O]
- Static assets: files.json/graph.json read by browsers via fetch. [O]

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| D-1 | numpy/networkx used but not installed by requirements | High |
| D-2 | psutil marked optional but required by resource monitor | Med |
| D-3 | No lockfile / pinned versions | Low |
| D-4 | Node side has no manifest at all | Low |
| D-5 | `design` import flagged by the audit census — needs confirmation it resolves (likely internal module) | Low |

## 5. Recommendations

1. Uncomment and pin `numpy`/`networkx` in `requirements.txt`, or gate the imports behind a
   feature flag with a graceful fallback.
2. Move `psutil` to a required section or make the monitor degrade when absent.
3. Introduce `pyproject.toml` with pinned core + dev dependency groups.
4. Add a CI import-check: `python -c "import rsis"` and import every `rsis.*` module.
