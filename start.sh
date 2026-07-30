#!/bin/bash
# COSMOS — Unified Launch Script
# Usage: ./start.sh [--no-services] [--port 9000]

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DASH_PORT=9000
MYBK_PORT=8765
RSIS_PORT=8080
SPACE_PORT=8888
START_SERVICES=true
PID_DIR="$DIR/.cosmos-pids"
LOG="$PID_DIR/cosmos.log"

mkdir -p "$PID_DIR"

for arg in "$@"; do
  case "$arg" in
    --no-services) START_SERVICES=false ;;
    --port=*) DASH_PORT="${arg#*=}" ;;
    --help) echo "Usage: $0 [--no-services] [--port PORT]"; exit 0 ;;
  esac
done

stop_all() {
  echo ""; echo "⏹ Stopping COSMOS services..."
  for pidfile in "$PID_DIR"/*.pid; do
    [ -f "$pidfile" ] || continue
    pid=$(cat "$pidfile" 2>/dev/null); name=$(basename "$pidfile" .pid)
    if kill -0 "$pid" 2>/dev/null; then echo "  Stopping $name (PID $pid)"; kill "$pid" 2>/dev/null; fi
    rm -f "$pidfile"
  done
  echo "  Done."; exit 0
}
trap stop_all SIGINT SIGTERM

echo "╔══════════════════════════════════════╗"
echo "║        🌌 COSMOS — Launch Suite      ║"
echo "╚══════════════════════════════════════╝"
echo ""

# ── Dashboard ──
echo "📊 Starting Dashboard..."
cd "$DIR"
nohup python3 -m http.server "$DASH_PORT" --bind 0.0.0.0 > "$LOG" 2>&1 &
echo $! > "$PID_DIR/dashboard.pid"
echo "  ✅ Dashboard → http://localhost:$DASH_PORT"

if ! $START_SERVICES; then
  echo ""; echo "🌌 Dashboard running (no services). Ctrl+C to stop."
  echo "   http://localhost:$DASH_PORT"
  command -v termux-open-url &>/dev/null && termux-open-url "http://localhost:$DASH_PORT" 2>/dev/null &
  wait; exit 0
fi

# ── MyKB ──
echo ""; echo "📚 Starting MyKB Wiki Server..."
if [ -f "$DIR/components/mykb/server.py" ]; then
  nohup python3 "$DIR/components/mykb/server.py" "$MYBK_PORT" >> "$LOG" 2>&1 &
  echo $! > "$PID_DIR/mykb.pid"
  echo "  ✅ MyKB → http://localhost:$MYBK_PORT"
else
  echo "  ⚠ mykb/server.py not found"
fi

# ── RSIS3 (serve static files from rsis3 dir) ──
echo ""; echo "🔄 Starting RSIS3 Dashboard..."
if [ -d "$DIR/components/rsis3" ]; then
  cd "$DIR/components/rsis3"
  nohup python3 -m http.server "$RSIS_PORT" --bind 0.0.0.0 > /dev/null 2>&1 &
  echo $! > "$PID_DIR/rsis3.pid"
  local_url="http://localhost:$RSIS_PORT/dashboard/"
  echo "  ✅ RSIS3 → $local_url"
fi

# ── SPACE (serve static files from space dir, since dist/ isn't built) ──
echo ""; echo "🚀 Starting SPACE Static Server..."
if [ -d "$DIR/components/space" ]; then
  cd "$DIR/components/space"
  nohup python3 -m http.server "$SPACE_PORT" --bind 0.0.0.0 > /dev/null 2>&1 &
  echo $! > "$PID_DIR/space.pid"
  echo "  ✅ SPACE → http://localhost:$SPACE_PORT/web/"
  echo "     Spec Viewer → http://localhost:$SPACE_PORT/meta-viewer.html"
  echo "     Prompt App → http://localhost:$SPACE_PORT/prompt-framework/prompt-app/"
fi

cd "$DIR"

echo ""; echo "╔══════════════════════════════════════╗"
echo "║  🌌 COSMOS is running                     ║"
echo "║  Dashboard → localhost:$DASH_PORT          ║"
echo "║  MyKB      → localhost:$MYBK_PORT          ║"
echo "║  RSIS3     → localhost:$RSIS_PORT/dashboard/║"
echo "║  SPACE     → localhost:$SPACE_PORT/web/    ║"
echo "║  Press Ctrl+C to stop all                  ║"
echo "╚══════════════════════════════════════╝"

command -v termux-open-url &>/dev/null && sleep 2 && termux-open-url "http://localhost:$DASH_PORT" 2>/dev/null &
wait
