# COSMOS Data Contracts

The single source of truth for the shared data shapes the three components
exchange. Everything here is enforced by `contracts/validate.py`, which is
wired into `gen-static-data.py --check` (deploy/CI) and the RSIS3 loop
pipeline (`check-practices`, telemetry contract).

**Document ID:** COSMOS-CONTRACTS-1.0 | **Updated:** 2026-08-06
**Scope:** OKF frontmatter · files.json · ecosystem.json · loops.json ·
telemetry JSONL · SPACE framework definition

---

## 1. OKF frontmatter (MyKB wiki pages)

Every page under `components/mykb/wiki/**/*.md` starts with YAML frontmatter
(an OKF `--- ... ---` block).

| Field | Required | Type | Rules |
|-------|----------|------|-------|
| `type` | yes | string | One of: `concept`, `entity`, `index`, `synthesis`, `decision`, `question`, `domain`, `pulse`, `episode`, `log`, `experiment`, `plan`, `project`, `reflection`, `source` |
| `title` | yes | string | Non-empty, used as the browser title |
| `description` | yes* | string | One-line summary (*required for syntheses; WARN elsewhere) |
| `tags` | yes* | array | List of strings (*WARN if missing) |
| `timestamp` | yes* | ISO-8601 string | Created/updated time (*WARN if missing) |
| `status` | yes* | string | e.g. `stub`, `growing`, `stable`, `archived` (*WARN if missing) |

Validator severity: missing frontmatter or `type`/`title` = **FAIL**;
missing optional fields = **WARN**.

## 2. files.json (MyKB snapshot)

`components/mykb/files.json` is a JSON array of enriched page entries:

```json
[{"path": "wiki/concepts/pulse-cycle.md", "type": "concept", "title": "Pulse Cycle", "tags": ["rsis3"]}]
```

| Field | Required | Type | Rules |
|-------|----------|------|-------|
| `path` | yes | string | Relative under `components/mykb/`, no `components/` prefix, ends `.md`, exists on disk, unique |
| `type` | yes | string | Any value |
| `title` | yes | string | Non-empty |
| `tags` | yes | array | List of strings |

## 3. ecosystem.json (dashboard snapshot)

`components/rsis3/dashboard/ecosystem.json`:

```json
{"generated": "2026-08-06T16:37Z",
 "components": {"mykb": {"files": 6908, "md": 6866}, "space": {"files": 298}, "rsis3": {"files": 92}},
 "telemetry": {"pulses": 20, "goals": 77, "passed": 77, "failed": 0, "held": 0, "total": 77, "improvements": 37}}
```

| Field | Required | Rules |
|-------|----------|-------|
| `generated` | yes | ISO-8601 / RFC-3339 string |
| `components.mykb.files` / `.md` | yes | int ≥ 0; `md` ≤ `files` |
| `components.space.files`, `components.rsis3.files` | yes | int ≥ 0 |
| `telemetry.pulses/goals/passed/failed/held/total/improvements` | yes | int ≥ 0; `passed+failed+held == total` when `total > 0` |

## 4. loops.json (dashboard Loops tab)

`components/rsis3/dashboard/loops.json`:

```json
{"generated": "...", "note": "...", "loops": [ {"id": "L0", "name": "Substrate", "status": "n/a", ...}, ... ]}
```

- `loops` contains exactly the ten ids `L0`…`L9`.
- Each entry requires: `id`, `name`, `status`, `target`, `state_file`,
  `runs`, `last_run`, `cycle`, `history_len`, `last_signal`, `runtime`,
  `params`.
- `runs` int ≥ 0; `status` in `n/a`, `implemented`, `active`, `idle`,
  `recent`, `error`.

## 5. Telemetry JSONL (RSIS3 loop events)

Written to `components/rsis3/.rsis/telemetry/*.jsonl`. One JSON object per
line; blank lines allowed.

| Field | Required | Rules |
|-------|----------|-------|
| `type` | yes | Matches `l[1-9]_(start\|complete\|error\|evaluation\|skip)` or `l2_(candidate\|attempts\|parallel_start\|shared_memory)`; any other `l[1-9]_*` allowed for forward-compat |
| `timestamp` | yes | ISO-8601 string |
| `path`, `delta`, `duration_ms`, `metadata` | no | `path`/`delta` strings, `duration_ms` int, metadata object |

Any line that is not valid JSON or misses `type`/`timestamp` = **FAIL**
(pipeline telemetry contract).

## 6. SPACE framework definition

`components/space/prompt-framework/framework.json`:

| Key | Required | Type |
|-----|----------|------|
| `meta` | yes | object with `name`, `description`, `total_series`, `total_rounds`, `total_open_ended_questions`, `total_multi_choice_followups` |
| `dependency_chain` | yes | object with `edges` array |
| `series` | yes | array; each has `id` (int), `name`, `description`, `rounds` (array), and optional `x_rounds`/`y_open_ended_per_round`/`z_multi_choice_per_open` |

The 326-probe total is `sum(series[].total_open_ended) +
sum(series[].total_multi_choice)`.

---

## Enforcement points

- `python3 contracts/validate.py` — standalone (all contracts, exit 1 on FAIL).
- `python3 gen-static-data.py --check` — deploy/CI gate (sections 1–5).
- `python -m rsis check-practices` — loop pipeline gate (section 5, telemetry).
