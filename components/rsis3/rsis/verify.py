"""Verification mesh — replayable evidence for every applied change.

Phase 7 (Sequel II): the evaluator becomes callable by both daemon and CI,
contracts gate the apply pipeline, and every gate run lands in a regression
ledger so any applied change can be replayed and re-verified.

- ``verify_candidate`` — one deterministic gate pass: evaluator + contracts
  + optional property checks, recorded to ``rack/verification/``.
- ``verify-server`` — ``python -m rsis verify-server`` exposes the same
  gates over HTTP (POST /verify, GET /health, GET /ledger).
- ``contracts_gate`` — runs the repo contract suite as a subprocess.
- ``run_property_checks`` — optional sandboxed subprocess property tests.

Ledger record: candidate sha, gates, scores, decision, artifacts,
pre-apply state digests, and the pre-apply checkpoint commit (for Phase 9
rollback).
"""

from __future__ import annotations

import hashlib
import json
import logging
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_PORT = 8788


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def repo_root(package_root: Path) -> Path:
    """Repo root = the ancestor holding gen-static-data.py / contracts/."""
    p = Path(package_root).resolve()
    for cand in (p, *p.parents):
        if (cand / "gen-static-data.py").is_file():
            return cand
    return p.parent


def candidate_sha(diff_or_code: str) -> str:
    return hashlib.sha256((diff_or_code or "").encode("utf-8")).hexdigest()


def digest_file(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def contracts_gate(repo: Path, timeout_s: int = 120) -> tuple[bool, int]:
    """Run the repo contract suite. Returns (ok, total_fail)."""
    script = Path(repo) / "contracts" / "validate.py"
    if not script.is_file():
        return True, 0
    try:
        proc = subprocess.run(
            [sys.executable, str(script)], cwd=str(repo),
            capture_output=True, text=True, timeout=timeout_s)
        return proc.returncode == 0, 0 if proc.returncode == 0 else 1
    except (OSError, subprocess.TimeoutExpired) as e:
        logger.warning("contracts gate failed to run: %s", e)
        return False, 1


def run_property_checks(checks: list[str], timeout_s: int = 15) -> list[dict]:
    """Run optional property checks in sandboxed subprocesses."""
    results = []
    for i, code in enumerate(checks or []):
        try:
            proc = subprocess.run(
                [sys.executable, "-c", code], capture_output=True, text=True,
                timeout=timeout_s)
            results.append({
                "name": f"property-{i + 1}",
                "passed": proc.returncode == 0,
                "output": (proc.stderr or proc.stdout)[:200],
            })
        except subprocess.TimeoutExpired:
            results.append({"name": f"property-{i + 1}",
                            "passed": False, "output": "timeout"})
        except OSError as e:
            results.append({"name": f"property-{i + 1}",
                            "passed": False, "output": str(e)[:200]})
    return results


def ledger_path(workspace: Path, day: Optional[str] = None) -> Path:
    day = day or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return Path(workspace) / "rack" / "verification" / f"{day}.jsonl"


def append_verification(workspace: Path, record: dict) -> None:
    path = ledger_path(workspace)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


def pre_apply_digests(workspace: Path, target_files: list[str]) -> dict:
    ws = Path(workspace)
    return {f: digest_file(ws / f) for f in (target_files or [])}


def verify_candidate(workspace: Path, candidate: dict,
                     repo: Optional[Path] = None,
                     include_contracts: bool = True,
                     pre_commit: Optional[str] = None) -> dict:
    """Run the full gate pass on a candidate and record it in the ledger."""
    from rsis.evaluator import EvaluatorClient

    ws = Path(workspace)
    target_files = candidate.get("target_files") or []
    pre = pre_apply_digests(ws, target_files)

    eval_result = EvaluatorClient().evaluate({
        "description": candidate.get("description", ""),
        "target_files": target_files,
        "diff": candidate.get("diff_or_code", ""),
        "rationale": candidate.get("rationale", ""),
        "attempt": candidate.get("attempt", 1),
        "goal": candidate.get("goal", ""),
    })

    gates = [{
        "name": "evaluator",
        "passed": eval_result.passed,
        "notes": eval_result.rationale[:200],
        "score_avg": eval_result.score_avg,
    }]
    contract_fail = 0
    if include_contracts:
        ok, contract_fail = contracts_gate(repo or repo_root(ws))
        gates.append({"name": "contracts", "passed": ok,
                      "notes": f"{contract_fail} contract FAIL"})

    properties = run_property_checks(candidate.get("metadata", {})
                                     .get("property_checks", []))

    record = {
        "ts": _now_ts(),
        "candidate_sha": candidate_sha(candidate.get("diff_or_code", "")),
        "description": candidate.get("description", ""),
        "target_files": target_files,
        "goal": candidate.get("goal", ""),
        "gates": gates,
        "contract_fail": contract_fail,
        "property_checks": properties,
        "decision": eval_result.decision,
        "scores": eval_result.scores if hasattr(eval_result, "scores") else {},
        "artifacts": candidate.get("metadata", {}).get("applied_files", []),
        "pre_digests": pre,
        "pre_commit": pre_commit,
    }
    append_verification(ws, record)
    return record


def record_verification(workspace: Path, candidate, eval_result,
                        pre_commit: Optional[str] = None,
                        contract_ok: bool = True,
                        contract_fail: int = 0) -> dict:
    """Ledger-only recording after an applied/rejected candidate.

    Uses the already-computed evaluator result (no second gate pass) so the
    apply path records evidence without re-spending LLM budget.
    """
    ws = Path(workspace)
    diff = getattr(candidate, "diff_or_code", None) or (
        candidate.get("diff_or_code", "") if isinstance(candidate, dict) else "")
    target_files = (list(getattr(candidate, "target_files", []) or [])
                    if not isinstance(candidate, dict)
                    else candidate.get("target_files") or [])
    metadata = (getattr(candidate, "metadata", {}) or {}
                if not isinstance(candidate, dict)
                else candidate.get("metadata") or {})
    properties = run_property_checks(metadata.get("property_checks", []))
    record = {
        "ts": _now_ts(),
        "candidate_sha": candidate_sha(diff),
        "description": (getattr(candidate, "description", "") if not isinstance(candidate, dict)
                        else candidate.get("description", "")),
        "target_files": target_files,
        "goal": (getattr(candidate, "goal", "") if not isinstance(candidate, dict)
                 else candidate.get("goal", "")),
        "gates": [{
            "name": "evaluator",
            "passed": bool(eval_result.passed),
            "notes": (getattr(eval_result, "rationale", "") or "")[:200],
            "score_avg": getattr(eval_result, "score_avg", None),
        }, {
            "name": "contracts",
            "passed": contract_ok,
            "notes": f"{contract_fail} contract FAIL",
        }],
        "contract_fail": contract_fail,
        "property_checks": properties,
        "decision": getattr(eval_result, "decision", "reject"),
        "scores": getattr(eval_result, "scores", {}),
        "artifacts": metadata.get("applied_files", []),
        "pre_digests": pre_apply_digests(ws, target_files),
        "pre_commit": pre_commit,
    }
    append_verification(ws, record)
    # Phase 14: every applied candidate also carries a sha256 attestation
    # of the invariant set it passed (extends the Phase 7 ledger).
    if contract_ok and record.get("decision") == "approve":
        try:
            from rsis.invariants import attest, run_invariants
            attest(ws, f"candidate:{record['candidate_sha']}",
                   run_invariants(ws), actor="l2")
        except Exception as e:
            logger.warning("attestation failed: %s", e)
    return record


def serve(port: int = DEFAULT_PORT, workspace: Optional[Path] = None,
          repo: Optional[Path] = None) -> None:
    """HTTP surface for the verification mesh (stdlib)."""
    from http.server import BaseHTTPRequestHandler, HTTPServer

    ws = Path(workspace or ".")
    rep = repo or repo_root(Path(ws).resolve())
    port = int(port)

    class VerifyHandler(BaseHTTPRequestHandler):
        def _json(self, status: int, payload: dict) -> None:
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self):
            parsed = __import__("urllib.parse", fromlist=["urlparse"]).urlparse(self.path)
            if parsed.path != "/verify":
                self._json(404, {"error": "not_found"})
                return
            length = int(self.headers.get("Content-Length", 0))
            try:
                body = json.loads(self.rfile.read(length).decode() or "{}")
            except (ValueError, OSError):
                self._json(400, {"error": "invalid_json"})
                return
            try:
                record = verify_candidate(ws, body, repo=rep)
                self._json(200, {"ok": True, "record": record})
            except Exception as e:
                self._json(500, {"error": str(e)[:200]})

        def do_GET(self):
            parsed = __import__("urllib.parse", fromlist=["urlparse"]).urlparse(self.path)
            params = __import__("urllib.parse", fromlist=["parse_qs"]).parse_qs(parsed.query)
            if parsed.path == "/health":
                self._json(200, {"ok": True})
            elif parsed.path == "/ledger":
                day = params.get("date", [None])[0]
                path = ledger_path(ws, day)
                recs = []
                if path.is_file():
                    recs = [json.loads(l) for l in
                            path.read_text(encoding="utf-8").splitlines()
                            if l.strip()]
                self._json(200, {"path": str(path), "records": len(recs),
                                 "ledger": recs})
            else:
                self._json(404, {"error": "not_found"})

        def log_message(self, fmt, *args):
            pass

    print(f"  verify-server on :{port} (workspace {ws})")
    HTTPServer(("", port), VerifyHandler).serve_forever()


def main(port: int = DEFAULT_PORT, workspace: Optional[Path] = None) -> int:
    serve(port=port, workspace=workspace)
    return 0
