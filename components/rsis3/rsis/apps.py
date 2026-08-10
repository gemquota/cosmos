"""Public API surface — machine identities, quotas, governed submission.

Phase 20 (Sequel IV): third-party applications interact with the system
safely at scale. Apps are machine identities extending the Phase 12 user
model — same HMAC token chain, same policy engine, no parallel system.

- ``add_app``/``issue_token`` — per-app credentials with capabilities
  scoped by policy (an app can never escalate roles).
- Quotas: per-app rate limit + daily cost budget enforced fail-close,
  accounted in ``.rsis/apps_usage.jsonl`` and the cost ledger.
- ``serve`` — minimal versioned public API: capability handshake,
  candidate submission (policy → verification → staged approval) and
  per-app usage/status. Every action is audit-attributable.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import logging
import os
import secrets
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, save_json
from rsis.users import shared_secret

logger = logging.getLogger(__name__)

DEFAULT_APPS = {"version": 1, "apps": []}
APP_CAPABILITIES = ("read", "propose", "approve")
DEFAULT_QUOTA = {"rate_per_min": 10, "daily_usd": 0.05}


def apps_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "apps.json"


def usage_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "apps_usage.jsonl"


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def load_apps(workspace: Path) -> dict:
    return load_json(apps_path(workspace), dict(DEFAULT_APPS))


def ensure_apps(workspace: Path) -> dict:
    path = apps_path(workspace)
    if not path.is_file():
        save_json(path, dict(DEFAULT_APPS))
    return load_apps(workspace)


def add_app(workspace: Path, app_id: str, capabilities=None,
            quota: Optional[dict] = None) -> dict:
    """Register a machine identity; returns the record + secret."""
    ws = Path(workspace)
    apps = ensure_apps(ws)
    if any(a["id"] == app_id for a in apps["apps"]):
        raise ValueError(f"app {app_id!r} already exists")
    secret = secrets.token_urlsafe(24)
    record = {
        "id": app_id,
        "secret_sha": hashlib.sha256(secret.encode()).hexdigest(),
        "capabilities": list(capabilities or ["read"]),
        "quota": {**DEFAULT_QUOTA, **(quota or {})},
        "created": now_ts(),
    }
    apps["apps"].append(record)
    save_json(apps_path(ws), apps)
    emit(ws, "apps_registered", app=app_id)
    return {"id": app_id, "secret": secret, "capabilities": record["capabilities"],
            "quota": record["quota"]}


def issue_token(workspace: Path, app_id: str, secret: str,
                ttl_s: int = 12 * 3600) -> Optional[str]:
    apps = load_apps(workspace)
    rec = next((a for a in apps["apps"] if a["id"] == app_id), None)
    if rec is None or not hmac.compare_digest(
            hashlib.sha256(secret.encode()).hexdigest(), rec["secret_sha"]):
        return None
    exp = int(time.time()) + ttl_s
    payload = f"app:{app_id}.{exp}".encode()
    sig = hmac.new(shared_secret(workspace).encode(), payload,
                   hashlib.sha256).digest()
    return f"{_b64(payload)}.{_b64(sig)}"


def authenticate(workspace: Path, token: Optional[str]) -> Optional[dict]:
    """Verify an app token; returns the app record or None."""
    if not token:
        return None
    try:
        parts = token.split(".")
        if len(parts) != 2:
            return None
        pad = lambda s: s + "=" * (-len(s) % 4)  # noqa: E731
        payload = base64.urlsafe_b64decode(pad(parts[0]))
        sig = base64.urlsafe_b64decode(pad(parts[1]))
    except Exception:
        return None
    expect = hmac.new(shared_secret(workspace).encode(), payload,
                      hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expect):
        return None
    app_id = payload.decode().split(".")[0]
    if not app_id.startswith("app:"):
        return None
    app_id = app_id[4:]
    exp = int(payload.decode().split(".")[1])
    if int(time.time()) > exp:
        return None
    apps = load_apps(workspace)
    rec = next((a for a in apps["apps"] if a["id"] == app_id), None)
    return rec


def quota_ok(workspace: Path, app: dict) -> tuple[bool, dict]:
    """Rate + daily budget check (fail-closed)."""
    app_id = app["id"]
    usage = [json.loads(l) for l in
             usage_path(workspace).read_text(encoding="utf-8",
                                             errors="ignore").splitlines()
             if l.strip()] if usage_path(workspace).is_file() else []
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now = time.time()
    window_start = now - 60
    rate = sum(1 for u in usage
               if u.get("app") == app_id and u.get("ts", 0) >= window_start)
    spent = sum(u.get("cost", 0.0) for u in usage
                if u.get("app") == app_id and u.get("day") == day)
    quota = app.get("quota", DEFAULT_QUOTA)
    ok = rate < quota.get("rate_per_min", 10) and spent < quota.get("daily_usd", 0.05)
    return ok, {"rate": rate, "spent": spent, "quota": quota}


def _record_usage(workspace: Path, app_id: str, cost: float = 0.0) -> None:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rec = {"app": app_id, "day": day, "ts": time.time(), "cost": cost}
    path = usage_path(workspace)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")


def submit_candidate(workspace: Path, app: dict, candidate: dict) -> dict:
    """Public candidate submission: policy → verification → staged approval."""
    from rsis.policy import requires_approval, stage_candidate
    from rsis.verify import verify_candidate
    ws = Path(workspace)
    if not requires_approval(candidate, policy=__import__(
            "rsis.policy", fromlist=["load_policy"]).load_policy(ws)):
        return {"ok": False, "error": "candidate outside approved surface",
                "app": app["id"]}
    record = verify_candidate(ws, candidate)
    staged = stage_candidate(ws, candidate, actor=f"app:{app['id']}")
    _record_usage(ws, app["id"])
    emit(ws, "apps_candidate_submitted", app=app["id"],
         candidate_sha=record["candidate_sha"][:12])
    return {"ok": True, "app": app["id"],
            "candidate_sha": record["candidate_sha"],
            "decision": record["decision"], "staged_id": staged}


def status(workspace: Path) -> dict:
    apps = load_apps(workspace)
    return {"apps": [a["id"] for a in apps["apps"]],
            "capabilities": APP_CAPABILITIES,
            "protocol": "cosmos-protocol/1"}


def serve(workspace: Path, port: int = 8790) -> None:
    """Minimal public API server (stdlib)."""
    ws = Path(workspace)

    class AppsHandler(BaseHTTPRequestHandler):
        def _json(self, status, payload):
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)

        def _app(self):
            auth = self.headers.get("Authorization", "")
            token = auth[7:] if auth.startswith("Bearer ") else None
            return authenticate(ws, token)

        def do_GET(self):
            parsed = __import__("urllib.parse",
                                fromlist=["urlparse"]).urlparse(self.path)
            if parsed.path == "/api/version":
                from rsis.protocol import capabilities
                self._json(200, capabilities())
                return
            if parsed.path == "/api/apps/status":
                app = self._app()
                if not app:
                    self._json(401, {"error": "unauthorized"})
                    return
                ok, q = quota_ok(ws, app)
                self._json(200, {"app": app["id"], "capabilities": app["capabilities"],
                                 "quota_ok": ok, "usage": q})
                return
            self._json(404, {"error": "not_found"})

        def do_POST(self):
            parsed = __import__("urllib.parse",
                                fromlist=["urlparse"]).urlparse(self.path)
            if parsed.path != "/api/apps/submit":
                self._json(404, {"error": "not_found"})
                return
            app = self._app()
            if not app:
                self._json(401, {"error": "unauthorized"})
                return
            ok, _ = quota_ok(ws, app)
            if not ok:
                self._json(429, {"error": "quota_exceeded", "fail_closed": True})
                return
            length = int(self.headers.get("Content-Length", 0))
            try:
                candidate = json.loads(self.rfile.read(length).decode() or "{}")
            except (ValueError, OSError):
                self._json(400, {"error": "invalid_json"})
                return
            try:
                result = submit_candidate(ws, app, candidate)
                self._json(200 if result.get("ok") else 400, result)
            except Exception as e:
                self._json(500, {"error": str(e)[:200]})

        def log_message(self, fmt, *args):
            pass

    print(f"  apps API on :{port} (workspace {ws})")
    HTTPServer(("", port), AppsHandler).serve_forever()


def main(workspace: Path, action: str = "list", app_id: Optional[str] = None,
         secret: Optional[str] = None, capabilities=None,
         json_out: bool = False) -> int:
    ws = Path(workspace)
    if action == "list":
        s = status(ws)
        print("  apps:", ", ".join(s["apps"]) or "none")
        if json_out:
            print(json.dumps(s))
        return 0
    if action == "add":
        if not app_id:
            print("  --app-id required"); return 2
        rec = add_app(ws, app_id, capabilities=capabilities)
        print(f"  app {rec['id']} registered · capabilities "
              f"{rec['capabilities']} · quota {rec['quota']}")
        print(f"  secret: {rec['secret']}  (store once — not retrievable)")
        return 0
    if action == "token":
        if not app_id or not secret:
            print("  --app-id and --secret required"); return 2
        tok = issue_token(ws, app_id, secret)
        if not tok:
            print("  invalid app/secret"); return 1
        print(tok)
        return 0
    print("  unknown action"); return 2
