# 34 — Operational Manual

**Doc ID:** COSMOS-AUDIT-34 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [12 Data Model](12_DATA_MODEL_ANALYSIS.md) · [31 Deployment](31_DEPLOYMENT_AUDIT.md) · [35 Appendices](35_APPENDICES.md)

---

## 1. Workspace Setup

```bash
python -m rsis init            # initialise .rsis/, telemetry, git checkpoint
pip install -r components/rsis3/requirements.txt   # NOTE: numpy/networkx must be uncommented (TD-2)
```

## 2. Core Commands (Observed)

| Command | Purpose |
|---|---|
| `python -m rsis run [--parallel N] [--parallel-retries R] [--budget-cap $]` | L2 improvement session |
| `python -m rsis evolve` | L3 evolution cycle |
| `python -m rsis optimize` | L4 meta-parameter optimization |
| `python -m rsis strategies` | L5 strategy evolution |
| `python -m rsis identity / metacog / metameta / mmm` | L6–L9 tuning loops |
| `python -m rsis pipeline` | DAG demo (retry + deadlock asserts) |
| `python -m rsis scheduler` | scheduler demo |
| `python -m rsis check-practices` | workspace/loop hygiene (17 checks) |
| `python -m rsis status` | system overview |

## 3. Snapshot Regeneration

```bash
python3 components/mykb/.wiki-daemon/build_graph.py   # graph.json
python3 gen-static-data.py                            # files.json / ecosystem.json / loops.json
python3 gen-static-data.py --check                    # verify freshness
```

## 4. Wiki Daemon & Search

- Daemon: `components/mykb/.wiki-daemon/server.py` (local HTTP; bind 127.0.0.1).
- Rebuild search index via the dashboard Actions tab (`api/v2/search/build`).
- Health/lint: dashboard Actions tab (`api/v2/health/lint`).

## 5. Verification Checklist (before any deploy)

1. `pytest components/rsis3/tests -q` → 49 passed
2. `python -m rsis pipeline` → demo asserts pass
3. `python3 gen-static-data.py --check` → OK
4. `python -m rsis check-practices` → all PASS
5. Smoke the live wiki for `meta-seg` / `home-metrics` markers after deploy (see [31](31_DEPLOYMENT_AUDIT.md))

## 6. Deploy (Current Manual Procedure)

```bash
git checkout main && git pull
# … verify per §5 …
git checkout gh-pages
git rm -rf --ignore-unmatch .
git checkout main -- .
git add -A
git commit -m "Deploy: sync main $(git rev-parse --short main) — <summary>"
git push origin gh-pages
```

## 7. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `import rsis.memory` fails | numpy/networkx not installed | uncomment+pin requirements (TD-2) |
| Live wiki looks old | gh-pages stale vs main | redeploy per §6 (this audit's regression) |
| `pipeline` demo reports deadlock | circular `depends_on` | fix the graph; guard is working |
| Snapshot `--check` fails | wiki changed without rebuild | run §3 scripts |
| Tests flaky (aging/preemption) | timing-sensitive cases | re-run; planned clock injection (P-3) |
