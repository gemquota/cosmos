#!/usr/bin/env bash
# COSMOS — bridge smoke test (Phase 4 CI guard).
#
# Starts the stdlib bridge on a free port without an API key (offline
# fallback), hits /health, and does one /api/chat round-trip asserting
# the deterministic cosmos reply. Exits non-zero on any failure.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
RSIS="$DIR/components/rsis3"
PORT="${RSIS_BRIDGE_SMOKE_PORT:-$(python3 - <<'PY'
import socket
s = socket.socket(); s.bind(('127.0.0.1', 0)); print(s.getsockname()[1]); s.close()
PY
)}"
LOG="$(mktemp)"
cleanup() { [ -n "${SRV_PID:-}" ] && kill "$SRV_PID" 2>/dev/null || true; rm -f "$LOG"; }
trap cleanup EXIT

echo "── Bridge smoke (offline fallback) ───────────────"
cd "$RSIS"
# Force deterministic offline mode regardless of the runner environment.
unset GEMINI_API_KEY
RSIS_BRIDGE_PORT="$PORT" node rack/bridge/server.mjs >"$LOG" 2>&1 &
SRV_PID=$!
for i in $(seq 1 30); do
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 2 "http://127.0.0.1:$PORT/health" || true)"
  [ "$code" = "200" ] && break
  sleep 0.5
done
[ "$code" = "200" ] || { echo "  ❌ /health never ready"; tail -5 "$LOG"; exit 1; }
echo "  ✅ /health → 200"

REPLY="$(curl -s --max-time 20 -X POST "http://127.0.0.1:$PORT/api/chat" \
  -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","content":"smoke"}],"cosmos":false}' | python3 -c 'import json,sys; print(json.load(sys.stdin).get("reply",""))')"
echo "$REPLY" | grep -q "Bridge offline" \
  && echo "  ✅ chat round-trip → offline-fallback reply" \
  || { echo "  ❌ chat round-trip failed"; echo "$REPLY"; exit 1; }
