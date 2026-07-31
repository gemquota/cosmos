#!/bin/bash
DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"
PID_FILE="$DIR/.dashboard.pid"

# Check if already running  
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if kill -0 "$OLD_PID" 2>/dev/null; then
        echo "Dashboard server already running (PID $OLD_PID)"
        echo "  http://127.0.0.1:8765/rack/telemetry-dashboard.html"
        exit 0
    fi
fi

# Kill any stale processes on the port
fuser -k 8765/tcp 2>/dev/null
sleep 1

# Start fresh
nohup python3 -m http.server 8765 --bind 0.0.0.0 > /dev/null 2>&1 &
PID=$!
echo $PID > "$PID_FILE"
sleep 2

if kill -0 "$PID" 2>/dev/null; then
    echo "Dashboard server started (PID $PID)"
    echo "  http://127.0.0.1:8765/rack/telemetry-dashboard.html"
else
    echo "ERROR: Server failed to start"
    rm -f "$PID_FILE"
fi
