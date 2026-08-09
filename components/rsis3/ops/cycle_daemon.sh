#!/usr/bin/env bash
# COSMOS — cycle daemon wrapper (Phase 4 ops maturity).
#
# Thin shell front for `python -m rsis cycle-daemon`: schedules
# `launch --cycles 1` on a 3-minute rhythm with a lockfile (parallel
# sessions never double-run), 5/15/30 min backoff on repeated failures,
# and a bridge healthcheck before every cycle.
#
# Usage:
#   ops/cycle_daemon.sh [--once] [--interval 180] [--bridge-url http://localhost:8787]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$DIR/components/rsis3"
exec python3 -m rsis cycle-daemon "$@"
