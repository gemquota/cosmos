#!/data/data/com.termux/files/usr/bin/bash
# SPACE Heartbeat Launcher — run in background
# Usage: ./heartbeat.sh [--restart]
cd "$(dirname "$0")"
echo "❤️  Starting SPACE Heartbeat Monitor..."
echo "   Log: heartbeat.log"
echo "   PID: $$"
nohup node heartbeat.mjs --interval 30 "$@" > heartbeat.log 2>&1 &
echo "   Running: ps aux | grep heartbeat"
