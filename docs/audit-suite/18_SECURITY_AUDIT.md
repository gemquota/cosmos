# 18 — Security Audit

**Doc ID:** COSMOS-AUDIT-18 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [08 Class-by-Class](08_CLASS_BY_CLASS_AUDIT.md) · [10 Data Flow](10_DATA_FLOW_ANALYSIS.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [29 Risk Register](29_RISK_REGISTER.md)

---

## 1. Attack Surface Inventory (Observed)

| Surface | Component | Exposure | Notes |
|---|---|---|---|
| Tool sandbox | `rsis/tools/` | subprocess boundary | sandbox backend (`setrlimit`, timeout); allowlists per tool category |
| Plain-tools router | `rsis/loop_l1.py` | local only | non-sandboxed path re-enabled when `tools.enabled` false (Phase D1 guard) |
| Wiki viewer | `components/mykb/index.html` | static (GitHub Pages) | renders user wiki markdown; `escapeHtml()` on content |
| Wiki daemon | `.wiki-daemon/server.py` | local HTTP | ThreadingTCPServer, no auth, bind default localhost |
| Evaluator | `rsis/evaluator.py` | subprocess | invokes configured evaluator path; integrity hash check exists |
| Dashboard | `rsis3/dashboard/index.html` | static | reads JSON data files only; no server code |
| SPACE web UI | `space/web/index.html` | static/local server | synchronous Node demo server, no auth |

## 2. Secrets Handling (Observed)

- No API keys or tokens are stored in the repository; LLM keys enter via environment
  (e.g. `RSIS_*` config surface). [O]
- Cost ledger (`telemetry.py` `CostLedger`) tracks spend but does not persist credentials. [O]
- The AO `github_tool` (token-bearing) is **not** ported (Phase D4 candidate, risk=CRITICAL + HITL). [O]
- No `.env` files are committed; `config.py` reads `os.environ` only. [O]

## 3. Sandboxing & Privilege Boundary

- `tools/sandbox.py` applies resource limits + timeouts to tool subprocesses; the sandbox
  backend is configurable (`RSIS_SANDBOX_BACKEND`). [O]
- `approval_mode` / `hitl_enabled` gate mutation-class tools; `RSIS_APPROVAL_THRESHOLD`
  scales gating. [O]
- **Finding:** sandbox and plain-tools routers are two separate code paths with duplicated
  guard logic (Phase D1 fixed a divergence: the plain path lacked a once-per-task guard). [I, Med]

## 4. Input Validation & Injection

- Wiki markdown is escaped before injection into the DOM; the in-page markdown parser does
  **not** render raw HTML from wiki files (it escapes it). [O]
- `escapeHtml()` covers `& < > "`. Attribute contexts (e.g. link hrefs) are escaped with the
  same helper — anchors are validated to be same-page `#` links or `http(s)`. [O]
- Paths in `files.json` are treated as data, not executed; the daemon normalizes
  `components/mykb/` prefixes. [O]
- **Finding:** `href` scheme check exists in the viewer; a broader allowlist (only
  `http/https/mailto`) is recommended. [I, Low]

## 5. Supply Chain / Dependencies

- Python runtime is effectively stdlib-only (see [24 Dependency Audit](24_DEPENDENCY_AUDIT.md));
  `requirements.txt` lists pytest for tests. [O]
- Node SPAs are self-contained (no npm packages), reducing supply-chain surface. [O]
- GitHub Pages serves static content; no server-side execution. [O]

## 6. Security Findings Summary

| # | Finding | Severity | Status |
|---|---|---|---|
| S-1 | Pulse/state JSON writes are not atomic (torn-write risk on concurrent loops) | Med | Open |
| S-2 | Wiki daemon + server.py use unbounded thread-per-connection HTTP servers | Med | Open |
| S-3 | No auth on local wiki daemon / SPACE server (LAN exposure risk) | Med | Open |
| S-4 | Plain-tools path duplicates sandbox guard logic (drift risk) | Low | D1 mitigates |
| S-5 | `github_tool` deferred to Phase D4 — capability gap, not a vuln | Low | Planned |
| S-6 | Markdown `href` allowlist could be stricter | Low | Open |

## 7. Recommendations

1. Atomic JSON writer (temp file + `os.replace` + `fsync`) for all `rack/pulses/*.json` and
   `.rsis/*.json` state files (also listed in [17 Concurrency](17_CONCURRENCY_ANALYSIS.md)).
2. Bind wiki daemon to `127.0.0.1` by default and add an optional token when exposed.
3. Unify sandbox/plain tool routers behind one executor wrapper to prevent guard drift.
4. When porting `github_tool` (Phase D4), land it with risk=CRITICAL, HITL gate, and a
   credential holder that never persists tokens.
5. Add a `Content-Security-Policy` meta tag to `index.html` / dashboard shells.
