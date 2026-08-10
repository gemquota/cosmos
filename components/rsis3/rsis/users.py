"""Collaborative ops — per-user identity, signed tokens, capability authz.

Phase 12 (Sequel III): the bridge and dashboard move from a shared token to
per-user sessions. Identity is stdlib-only: an HMAC-SHA256 signed token
(``<user_id>.<expiry>.<signature>``) is issued per user and verified with a
shared secret (``RSIS_USERS_SECRET`` or derived from ``RSIS_BRIDGE_TOKEN``).

Authorization is never role alone. The chain is:

    User → Identity → Role → Project membership → Policy → Capability → Action

An approver may not approve every project or every class of operation:
``authorize`` requires (a) a role capability covering the action, (b) project
membership (``users.json`` ``projects``, or ``["*"]`` for all), and (c) no
policy block for the action. Every gated action is audit-attributable via
``rsis.audit`` with the acting user id.
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
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

ROLES = ("observer", "contributor", "approver")

ROLE_CAPABILITIES = {
    "observer": ("read",),
    "contributor": ("read", "propose"),
    "approver": ("read", "propose", "approve", "rollback"),
}

#: every action the system can gate; policy.json may block any of them
ACTIONS = ("read", "propose", "approve", "rollback", "manage")

DEFAULT_TTL_S = 12 * 3600
DEFAULT_USERS = {"version": 1, "ttl_s": DEFAULT_TTL_S, "users": []}


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def users_path(workspace: Path) -> Path:
    return Path(workspace) / ".rsis" / "users.json"


def _expand(value):
    if isinstance(value, str) and value.startswith("$"):
        return os.environ.get(value[1:].strip("{}"), value)
    return value


def load_users(workspace: Path) -> dict:
    path = users_path(workspace)
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            for u in data.get("users", []):
                u["role"] = u.get("role", "observer")
                u["projects"] = u.get("projects", [])
            return data
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("users.json unreadable (%s); using defaults", e)
    return dict(DEFAULT_USERS)


def ensure_users(workspace: Path) -> dict:
    path = users_path(workspace)
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(DEFAULT_USERS, indent=2) + "\n",
                        encoding="utf-8")
    return load_users(workspace)


def shared_secret(workspace: Path) -> str:
    """Secret for signing user tokens: $RSIS_USERS_SECRET, else derived."""
    env = os.environ.get("RSIS_USERS_SECRET")
    if env:
        return env
    token = os.environ.get("RSIS_BRIDGE_TOKEN")
    if token:
        return "users:" + token
    # stable per-workspace fallback so tests/CLI are deterministic
    return "rsis-users:" + str(Path(workspace).resolve())


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def issue_token(workspace: Path, user_id: str,
                ttl_s: Optional[int] = None) -> Optional[str]:
    """Issue an HMAC-SHA256 signed token for a known user."""
    users = load_users(workspace)
    if not any(u["id"] == user_id for u in users["users"]):
        return None
    ttl = ttl_s or int(_expand(users.get("ttl_s", DEFAULT_TTL_S)))
    exp = int(time.time()) + int(ttl)
    payload = f"{user_id}.{exp}".encode()
    sig = hmac.new(shared_secret(workspace).encode(), payload,
                   hashlib.sha256).digest()
    return f"{_b64(payload)}.{_b64(sig)}"


def verify_token(workspace: Path, token: str) -> Optional[dict]:
    """Verify a signed token; returns the user dict or None."""
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
    try:
        user_id, exp = payload.decode().rsplit(".", 1)
        exp = int(exp)
    except ValueError:
        return None
    if int(time.time()) >= exp:
        return None
    users = load_users(workspace)
    for u in users["users"]:
        if u["id"] == user_id:
            return u
    return None


def add_user(workspace: Path, user_id: str, name: str, role: str,
             projects: Optional[list[str]] = None,
             capabilities: Optional[list[str]] = None) -> dict:
    """Add or update a user. ``projects=["*"]`` grants every project."""
    if role not in ROLES:
        raise ValueError(f"role must be one of {ROLES}")
    data = ensure_users(workspace)
    users = data["users"]
    for u in users:
        if u["id"] == user_id:
            u.update({"name": name, "role": role,
                      "projects": list(projects or []),
                      "capabilities": list(capabilities or [])})
            break
    else:
        users.append({"id": user_id, "name": name, "role": role,
                      "projects": list(projects or []),
                      "capabilities": list(capabilities or [])})
    path = users_path(workspace)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return users[-1]


def capabilities_for(user: dict) -> set[str]:
    caps = set(ROLE_CAPABILITIES.get(user.get("role", "observer"), ()))
    caps.update(user.get("capabilities") or [])
    return caps


def _policy_allows(workspace: Path, action: str) -> bool:
    """Policy may block a class of operation (Phase 9 policy wins)."""
    from rsis.policy import load_policy
    blocked = load_policy(workspace).get("capability_blocks") or []
    return action not in blocked


def authorize(workspace: Path, user: Optional[dict], action: str,
              project: str) -> tuple[bool, str]:
    """The Phase 12 authz chain: role → membership → policy → action."""
    if action not in ACTIONS:
        return False, f"unknown action {action!r}"
    if user is None:
        return False, "no authenticated identity"
    role = user.get("role", "observer")
    if action not in capabilities_for(user):
        return False, f"role {role!r} lacks capability {action!r}"
    projects = user.get("projects") or []
    if "*" not in projects and project not in projects:
        return False, f"user {user.get('id')!r} is not a member of {project!r}"
    if not _policy_allows(workspace, action):
        return False, f"policy blocks action {action!r}"
    return True, f"allowed: {user.get('id')} {action} on {project}"


def authenticate(workspace: Path, token: Optional[str]) -> Optional[dict]:
    if not token:
        return None
    return verify_token(workspace, token)


def main(workspace: Path, action: str, user_id: Optional[str] = None,
         name: Optional[str] = None, role: str = "observer",
         projects: Optional[list[str]] = None,
         token: Optional[str] = None, check_action: str = "read",
         project: str = "cosmos", json_out: bool = False) -> int:
    if action == "list":
        data = load_users(workspace)
        if json_out:
            print(json.dumps(data))
            return 0
        if not data["users"]:
            print("  users: none defined (.rsis/users.json empty)")
            return 0
        for u in data["users"]:
            print(f"  • {u['id']} ({u.get('name', '')}) role={u['role']} "
                  f"projects={u.get('projects') or []}")
        return 0
    if action == "add":
        assert user_id and name
        add_user(workspace, user_id, name, role, projects=projects)
        print(f"  ✓ user {user_id} added (role={role}, projects={projects or []})")
        return 0
    if action == "token":
        assert user_id
        tok = issue_token(workspace, user_id)
        if not tok:
            print(f"  ✗ unknown user {user_id}")
            return 1
        print(tok)
        return 0
    if action == "check":
        user = authenticate(workspace, token)
        ok, reason = authorize(workspace, user, check_action, project)
        print(f"  {'✓' if ok else '✗'} {reason}")
        return 0 if ok else 1
    print(f"  ✗ unknown users action {action!r}")
    return 2


if __name__ == "__main__":
    import sys
    sys.exit(main(Path(".").resolve(), sys.argv[1] if len(sys.argv) > 1 else "list"))
