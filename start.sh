#!/bin/bash
# COSMOS — Unified Launch Script
# Serves dashboard + all components from a single port (static)
# Only MyKB gets its own port for the wiki daemon
# Usage: ./start.sh [--port 9000]

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT=9000
MYBK_PORT=8765
PID_DIR="$DIR/.cosmos-pids"
LOG="$PID_DIR/cosmos.log"
mkdir -p "$PID_DIR"

for arg in "$@"; do
  case "$arg" in
    --port=*) PORT="${arg#*=}" ;;
    --help) echo "Usage: $0 [--port PORT]"; exit 0 ;;
  esac
done

stop_all() {
  echo ""; echo "⏹ Stopping COSMOS..."
  for pidfile in "$PID_DIR"/*.pid; do
    [ -f "$pidfile" ] || continue
    pid=$(cat "$pidfile" 2>/dev/null); name=$(basename "$pidfile" .pid)
    if kill -0 "$pid" 2>/dev/null; then echo "  Stopping $name"; kill "$pid" 2>/dev/null; fi
    rm -f "$pidfile"
  done
  echo "  Done."; exit 0
}
trap stop_all SIGINT SIGTERM

# Kill stale processes
for p in $PORT $MYBK_PORT; do
  fuser -k "$p/tcp" 2>/dev/null && echo "  Freed port $p" || true
done

echo "╔══════════════════════════════════════╗"
echo "║     🌌 COSMOS — One Port to Rule     ║"
echo "╚══════════════════════════════════════╝"
echo ""

# ── Main server: serves everything from cosmos root ──
echo "📡 Starting main server..."
cd "$DIR"
nohup python3 -m http.server "$PORT" --bind 0.0.0.0 > "$LOG" 2>&1 &
echo $! > "$PID_DIR/main.pid"
echo "  ✅ Dashboard  → http://localhost:$PORT/"
echo "  ✅ SPACE      → http://localhost:$PORT/components/space/web/"
echo "  ✅ RSIS3      → http://localhost:$PORT/components/rsis3/dashboard/"
echo ""

# ── MyKB (needs its own port — custom Python server) ──
echo "📚 Starting MyKB Wiki Server..."
if [ -f "$DIR/components/mykb/server.py" ]; then
  nohup python3 "$DIR/components/mykb/server.py" "$MYBK_PORT" >> "$LOG" 2>&1 &
  echo $! > "$PID_DIR/mykb.pid"
  sleep 0.5
  if kill -0 $(cat "$PID_DIR/mykb.pid") 2>/dev/null; then
    echo "  ✅ MyKB → http://localhost:$MYBK_PORT/"
  else
    echo "  ❌ MyKB failed to start"
  fi
else
  echo "  ⚠ mykb/server.py not found"
fi

echo ""
echo "╔══════════════════════════════════════╗"
echo "║  🌌 COSMOS is running                ║"
echo "║                                     ║"
echo "║  All static → localhost:$PORT/        ║"
echo "║    Dashboard: /                      ║"
echo "║    SPACE:     /components/space/web/ ║"
echo "║    RSIS3:     /components/rsis3/dashboard/║"
echo "║                                     ║"
echo "║  MyKB → localhost:$MYBK_PORT/        ║"
echo "║                                     ║"
echo "║  Press Ctrl+C to stop everything     ║"
echo "╚══════════════════════════════════════╝"

command -v termux-open-url &>/dev/null && sleep 2 && termux-open-url "http://localhost:$PORT/" 2>/dev/null &
wait
