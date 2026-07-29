#!/bin/bash
# mykb — start both dashboard and OKF graph server
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DASH_PORT=${1:-8826}
OKF_PORT=${2:-8808}
PID_DIR="$DIR/.wiki-daemon"
DASH_PID="$PID_DIR/dashboard.pid"
OKF_PID="$PID_DIR/okf-graph.pid"
LOG="$PID_DIR/server.log"

mkdir -p "$PID_DIR"

stop_old() {
  local pidfile="$1" name="$2"
  if [ -f "$pidfile" ]; then
    local pid=$(cat "$pidfile")
    if kill -0 "$pid" 2>/dev/null; then
      echo "  Stopping old $name (PID $pid)"
      kill "$pid" 2>/dev/null
      sleep 0.5
    fi
    rm -f "$pidfile"
  fi
}

echo "🔍 Checking for existing servers..."
stop_old "$DASH_PID" "dashboard"
stop_old "$OKF_PID" "okf-graph"

# Start dashboard (server.py)
echo "🚀 Starting dashboard on http://127.0.0.1:$DASH_PORT"
cd "$DIR"
nohup python3 server.py "$DASH_PORT" >> "$LOG" 2>&1 &
echo $! > "$DASH_PID"

# Start OKF graph server
echo "🌐 Starting OKF graph on http://127.0.0.1:$OKF_PORT"
nohup okf server "$DIR" -p "$OKF_PORT" --title "mykb" >> "$LOG" 2>&1 &
echo $! > "$OKF_PID"

sleep 1.5

# Verify both are running
DASH_OK=false
OKF_OK=false
kill -0 "$(cat "$DASH_PID" 2>/dev/null)" 2>/dev/null && DASH_OK=true
kill -0 "$(cat "$OKF_PID" 2>/dev/null)" 2>/dev/null && OKF_OK=true

if $DASH_OK; then
  echo "  ✅ Dashboard → http://127.0.0.1:$DASH_PORT"
else
  echo "  ❌ Dashboard failed — tail $LOG"
fi

if $OKF_OK; then
  echo "  ✅ OKF Graph → http://127.0.0.1:$OKF_PORT"
else
  echo "  ❌ OKF Graph failed — tail $LOG"
fi

# Open browser if available
if command -v termux-open-url &>/dev/null; then
  termux-open-url "http://127.0.0.1:$DASH_PORT" 2>/dev/null &
elif command -v xdg-open &>/dev/null; then
  xdg-open "http://127.0.0.1:$DASH_PORT" 2>/dev/null &
fi
