#!/usr/bin/env bash
# COSMOS — Full L1–L9 loop batch runner (pass 11 ops).
#
# Runs N full cycles of the standing rhythm: run (L1+L2) → evolve (L3) →
# optimize (L4) → strategies (L5) → identity (L6) → metacog (L7) →
# metameta (L8) → mmm (L9). One cycle may source its L2 goal from a SPACE
# spec artifact (`--goal-space-cycle N`), leaving a traceable spec link.
#
# Usage:
#   infra/loops/run-batch.sh [--cycles 5] [--goal-space-cycle 1] [--disk-pct 100]
#
# Env:
#   RSIS_DISK_USAGE_PCT  disk-pressure override (default 100 — deterministic
#                        on nearly-full devices; see pass 6 synthesis)
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
RSIS="$DIR/components/rsis3"
MYKB="$DIR/components/mykb"
CYCLES=5
SPEC_CYCLE=1
DISK_PCT="${RSIS_DISK_USAGE_PCT:-100}"

while [ $# -gt 0 ]; do
  case "$1" in
    --cycles) CYCLES="$2"; shift 2 ;;
    --goal-space-cycle) SPEC_CYCLE="$2"; shift 2 ;;
    --disk-pct) DISK_PCT="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

LOOPS=(run evolve optimize strategies identity metacog metameta mmm)
TOTAL=$((CYCLES * ${#LOOPS[@]}))
echo "🌌 COSMOS batch — $CYCLES cycles × ${#LOOPS[@]} loops = $TOTAL executions"
echo "   disk override: RSIS_DISK_USAGE_PCT=$DISK_PCT"
export RSIS_DISK_USAGE_PCT="$DISK_PCT"
cd "$RSIS"

FAIL=0
for c in $(seq 1 "$CYCLES"); do
  echo ""
  echo "── Cycle $c/$CYCLES ───────────────────────────────"
  for loop in "${LOOPS[@]}"; do
    if [ "$loop" = "run" ] && [ "$c" = "$SPEC_CYCLE" ]; then
      echo "  ▶ run --goal from-space  (capstone: SPACE spec → L2 goal)"
      python3 -m rsis run --goal from-space || { echo "  ✗ run failed"; FAIL=1; }
    else
      echo "  ▶ $loop"
      python3 -m rsis "$loop" || { echo "  ✗ $loop failed"; FAIL=1; }
    fi
  done
done

echo ""
echo "── Post-batch gates ──────────────────────────────"
cd "$RSIS"
python3 -m rsis check-practices || FAIL=1

echo ""
echo "── Snapshot regeneration ─────────────────────────"
cd "$DIR"
(cd "$MYKB" && python3 .wiki-daemon/build_stub_audit.py)
(cd "$MYKB" && python3 .wiki-daemon/build_graph.py)
python3 "$DIR/gen-static-data.py"
python3 "$DIR/gen-static-data.py" --check || FAIL=1

echo ""
if [ "$FAIL" = "1" ]; then
  echo "❌ Batch finished with failures — inspect above"
  exit 1
fi
echo "✅ Batch complete: $TOTAL executions, practices PASS, snapshots --check OK"
