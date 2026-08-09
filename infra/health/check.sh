#!/usr/bin/env bash
# COSMOS — health check (pass 11 ops). Local + CI monitoring gate.
#
# Verifies: deployed site up, snapshot integrity, data contracts, wiki link
# integrity, usage practices. Exits non-zero on any failure so scheduled
# runners (cron / GitHub Actions) alert by failing loudly.
#
# Usage:
#   infra/health/check.sh [--live-url https://gemquota.github.io/cosmos/]
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LIVE_URL="${LIVE_URL:-https://gemquota.github.io/cosmos/}"
while [ $# -gt 0 ]; do
  case "$1" in
    --live-url) LIVE_URL="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done
FAIL=0

echo "❤️  COSMOS health check — $(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "── Live site ─────────────────────────────────────"
code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$LIVE_URL" || echo 000)"
if [ "$code" = "200" ]; then
  echo "  ✅ $LIVE_URL → 200"
else
  echo "  ❌ $LIVE_URL → $code"
  FAIL=1
fi

echo "── Snapshots ─────────────────────────────────────"
(cd "$DIR" && python3 gen-static-data.py --check) || FAIL=1

echo "── Contracts ─────────────────────────────────────"
(cd "$DIR" && python3 contracts/validate.py >/dev/null) || FAIL=1

echo "── Wiki links ────────────────────────────────────"
(cd "$DIR/components/mykb" && python3 .wiki-daemon/link_check.py) || FAIL=1

echo "── Practices (loop pipeline gate) ────────────────"
(cd "$DIR/components/rsis3" && python3 -m rsis check-practices >/dev/null) || FAIL=1

echo "── Bridge smoke (offline fallback) ───────────────"
bash "$DIR/infra/health/bridge_smoke.sh" || FAIL=1

if [ "$FAIL" = "1" ]; then
  echo "❌ Health check FAILED"
  exit 1
fi
echo "✅ Health check OK"
