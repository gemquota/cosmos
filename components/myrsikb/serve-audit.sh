#!/data/data/com.termux/files/usr/bin/bash
# Serve the Triad Audit Report from anywhere
DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
PORT=${1:-8899}
echo "Triad Audit Report → http://localhost:${PORT}/audit-report-standalone.html"
echo "Press Ctrl+C to stop"
python3 -m http.server "$PORT" -d "$DIR"
