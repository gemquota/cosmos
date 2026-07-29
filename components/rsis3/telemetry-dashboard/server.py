#!/usr/bin/env python3
"""Self-contained Telemetry Dashboard Server.

Serves the dashboard frontend and provides API access to telemetry data
from any RSIS project directory. Zero external dependencies.

Usage:
    python server.py                          # use defaults
    python server.py --telemetry-dir ../rack/pulses --port 8080
    python server.py --telemetry-dir /path/to/telemetry --frontend-dir ./frontend
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from functools import wraps
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse


TELEMETRY_DIR = None
FRONTEND_DIR = None
DASHBOARD_DATA_FILE = "dashboard-data.json"


class TelemetryDashboardHandler(SimpleHTTPRequestHandler):
    """HTTP handler that serves static frontend files and telemetry API."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIR), **kwargs)

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def _send_error(self, message, status=404):
        self._send_json({"error": message}, status)

    def _load_dashboard_data(self):
        """Load and return the dashboard-data.json from telemetry dir."""
        data_path = Path(TELEMETRY_DIR) / DASHBOARD_DATA_FILE
        if not data_path.exists():
            return None
        try:
            return json.loads(data_path.read_text("utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            return {"error": f"Failed to parse data: {e}"}

    def _list_pulse_files(self):
        """List all pulse JSON files in telemetry dir."""
        if not TELEMETRY_DIR or not TELEMETRY_DIR.exists():
            return []
        files = sorted(TELEMETRY_DIR.glob("pulse-*.json"))
        result = []
        for f in files:
            try:
                stat = f.stat()
                result.append({
                    "filename": f.name,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime, tz=timezone.utc
                    ).isoformat(),
                })
            except OSError:
                continue
        return result

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")

        # ── API Routes ──────────────────────────────────────────────

        if path == "/api/data":
            data = self._load_dashboard_data()
            if data is None:
                return self._send_error(
                    f"No telemetry data found at {TELEMETRY_DIR / DASHBOARD_DATA_FILE}"
                )
            return self._send_json(data)

        if path == "/api/pulses":
            pulses = self._list_pulse_files()
            return self._send_json({"count": len(pulses), "files": pulses})

        if path.startswith("/api/pulses/"):
            # /api/pulses/pulse-001.json
            filename = path[len("/api/pulses/"):]
            filepath = Path(TELEMETRY_DIR) / filename
            if not filepath.exists() or not filename.endswith(".json"):
                return self._send_error(f"Pulse file not found: {filename}")
            try:
                data = json.loads(filepath.read_text("utf-8"))
                return self._send_json(data)
            except (json.JSONDecodeError, OSError) as e:
                return self._send_error(f"Failed to read pulse: {e}")

        if path == "/api/status":
            data = self._load_dashboard_data()
            return self._send_json({
                "data_loaded": data is not None,
                "telemetry_dir": str(TELEMETRY_DIR),
                "pulse_files": len(self._list_pulse_files()),
            })

        if path == "/api/config":
            return self._send_json({
                "telemetry_dir": str(TELEMETRY_DIR),
                "frontend_dir": str(FRONTEND_DIR),
                "data_file": DASHBOARD_DATA_FILE,
            })

        # ── Serve static files (from frontend/) ─────────────────────
        return super().do_GET()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        sys.stderr.write(
            f"[{datetime.now().strftime('%H:%M:%S')}] {self.client_address[0]} "
            f"{format % args}\n"
        )


def resolve_path(path_str, relative_to=None):
    """Resolve a path string, handling relative and absolute paths."""
    p = Path(path_str)
    if p.is_absolute():
        return p.resolve()
    if relative_to:
        return (relative_to / p).resolve()
    return p.resolve()


def main():
    parser = argparse.ArgumentParser(
        description="RSIS Telemetry Dashboard — Self-Contained Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python server.py
  python server.py --telemetry-dir ../rack/pulses --port 8080
  python server.py --telemetry-dir /path/to/telemetry --frontend-dir ./frontend
        """,
    )
    parser.add_argument(
        "--telemetry-dir",
        default="../rack/pulses",
        help="Path to telemetry data directory (default: ../rack/pulses)",
    )
    parser.add_argument(
        "--frontend-dir",
        default="./frontend",
        help="Path to frontend static files (default: ./frontend)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Server port (default: 8080)",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Server host (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--data-file",
        default="dashboard-data.json",
        help="Telemetry data filename (default: dashboard-data.json)",
    )

    args = parser.parse_args()

    # Resolve paths relative to this script's directory
    script_dir = Path(__file__).parent.resolve()

    global TELEMETRY_DIR, FRONTEND_DIR, DASHBOARD_DATA_FILE
    TELEMETRY_DIR = resolve_path(args.telemetry_dir, relative_to=script_dir)
    FRONTEND_DIR = resolve_path(args.frontend_dir, relative_to=script_dir)
    DASHBOARD_DATA_FILE = args.data_file

    # Validate paths
    if not FRONTEND_DIR.exists():
        print(f"Error: Frontend directory not found: {FRONTEND_DIR}", file=sys.stderr)
        print("Ensure --frontend-dir points to a directory with index.html", file=sys.stderr)
        sys.exit(1)

    if not (FRONTEND_DIR / "index.html").exists():
        print(f"Error: No index.html found in {FRONTEND_DIR}", file=sys.stderr)
        sys.exit(1)

    if not TELEMETRY_DIR.exists():
        print(f"Warning: Telemetry directory not found: {TELEMETRY_DIR}", file=sys.stderr)
        print("The dashboard will load but show no data until telemetry exists.", file=sys.stderr)
    else:
        data_path = TELEMETRY_DIR / DASHBOARD_DATA_FILE
        if not data_path.exists():
            print(f"Warning: Data file not found: {data_path}", file=sys.stderr)
        else:
            size = data_path.stat().st_size
            print(f"  Data file: {data_path} ({size:,} bytes)")

    # Start server
    server = HTTPServer((args.host, args.port), TelemetryDashboardHandler)
    print(f"\n{'='*60}")
    print(f"  RSIS Telemetry Dashboard")
    print(f"  {'='*60}")
    print(f"  URL:      http://localhost:{args.port}")
    print(f"  Frontend: {FRONTEND_DIR}")
    print(f"  Data:     {TELEMETRY_DIR / DASHBOARD_DATA_FILE}")
    print(f"  API:      http://localhost:{args.port}/api/data")
    print(f"  {'='*60}")
    print(f"  Press Ctrl+C to stop\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.server_close()


if __name__ == "__main__":
    main()
