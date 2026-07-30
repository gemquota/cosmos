#!/bin/bash
# COSMOS — Unified Launch Script
# Starts the dashboard + all 3 component services
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

# Parse args
for arg in "$@"; do
  case "$arg" in
    --no-services) START_SERVICES=false ;;
    --port=*) DASH_PORT="${arg#*=}" ;;
    --help) echo "Usage: $0 [--no-services] [--port PORT]"; exit 0 ;;
  esac
done

stop_all() {
  echo ""
  echo "⏹ Stopping COSMOS services..."
  for pidfile in "$PID_DIR"/*.pid; do
    [ -f "$pidfile" ] || continue
    pid=$(cat "$pidfile" 2>/dev/null)
    name=$(basename "$pidfile" .pid)
    if kill -0 "$pid" 2>/dev/null; then
      echo "  Stopping $name (PID $pid)"
      kill "$pid" 2>/dev/null
    fi
    rm -f "$pidfile"
  done
  echo "  Done."
  exit 0
}
trap stop_all SIGINT SIGTERM

echo "╔══════════════════════════════════════╗"
echo "║        🌌 COSMOS — Launch Suite      ║"
echo "╚══════════════════════════════════════╝"
echo ""

# ── Start Dashboard ──
echo "📊 Starting Dashboard..."
cd "$DIR"
nohup python3 -m http.server "$DASH_PORT" --bind 0.0.0.0 > "$LOG" 2>&1 &
echo $! > "$PID_DIR/dashboard.pid"
echo "  ✅ Dashboard → http://localhost:$DASH_PORT"

if ! $START_SERVICES; then
  echo ""
  echo "🌌 Dashboard running (no services). Ctrl+C to stop."
  echo "   http://localhost:$DASH_PORT"
  if command -v termux-open-url &>/dev/null; then
    termux-open-url "http://localhost:$DASH_PORT" 2>/dev/null &
  fi
  wait
  exit 0
fi

# ── Start MyKB ──
echo ""
echo "📚 Starting MyKB Wiki Server..."
if [ -f "$DIR/components/mykb/server.py" ]; then
  nohup python3 "$DIR/components/mykb/server.py" "$MYBK_PORT" >> "$LOG" 2>&1 &
  echo $! > "$PID_DIR/mykb.pid"
  echo "  ✅ MyKB → http://localhost:$MYBK_PORT"
else
  echo "  ⚠ mykb/server.py not found"
fi

# ── Start RSIS3 Dashboard ──
echo ""
echo "🔄 Starting RSIS3 Dashboard..."
if [ -d "$DIR/components/rsis3" ]; then
  cd "$DIR/components/rsis3"
  nohup python3 -m http.server "$RSIS_PORT" --bind 0.0.0.0 > /dev/null 2>&1 &
  echo $! > "$PID_DIR/rsis3.pid"
  echo "  ✅ RSIS3 Dashboard → http://localhost:$RSIS_PORT/dashboard/"
  echo "     Telemetry: http://localhost:$RSIS_PORT/rack/telemetry-dashboard.html"
else
  echo "  ⚠ rsis3/ not found"
fi

# ── Start SPACE Web Server ──
echo ""
echo "🚀 Starting SPACE Web Server..."
if [ -f "$DIR/components/space/web/server.mjs" ]; then
  cd "$DIR/components/space"
  nohup node web/server.mjs "$SPACE_PORT" > /dev/null 2>&1 &
  echo $! > "$PID_DIR/space.pid"
  echo "  ✅ SPACE Web UI → http://localhost:$SPACE_PORT"
elif [ -f "$DIR/components/space/ui/package.json" ]; then
  cd "$DIR/components/space/ui"
  nohup npx vite --port "$SPACE_PORT" --host > /dev/null 2>&1 &
  echo $! > "$PID_DIR/space.pid"
  echo "  ✅ SPACE Vite Dev Server → http://localhost:$SPACE_PORT"
else
  echo "  ⚠ SPACE web server not found"
fi

# ── Start SPACE Meta Viewer (for specs) ──
if [ -f "$DIR/components/space/serve-meta.mjs" ]; then
  echo "     Meta Viewer → http://localhost:8899"
  nohup node "$DIR/components/space/serve-meta.mjs" 8899 > /dev/null 2>&1 &
  echo $! > "$PID_DIR/space-meta.pid"
fi

cd "$DIR"

echo ""
echo "╔══════════════════════════════════════╗"
echo "║  🌌 COSMOS is running                ║"
echo "║                                     ║"
echo "║  Dashboard → localhost:$DASH_PORT    ║"
echo "║  MyKB      → localhost:$MYBK_PORT    ║"
echo "║  RSIS3     → localhost:$RSIS_PORT    ║"
echo "║  SPACE     → localhost:$SPACE_PORT   ║"
echo "║                                     ║"
echo "║  Press Ctrl+C to stop all services   ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Open browser if available
if command -v termux-open-url &>/dev/null; then
  sleep 2
  termux-open-url "http://localhost:$DASH_PORT" 2>/dev/null &
elif command -v xdg-open &>/dev/null; then
  sleep 2
  xdg-open "http://localhost:$DASH_PORT" 2>/dev/null &
fi

# Wait for Ctrl+C
wait
