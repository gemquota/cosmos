#!/usr/bin/env python3
"""Custom HTTP server for RSIS dashboard."""
import http.server, socketserver, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def guess_type(self, path):
        if path.endswith('.js'):
            return 'application/javascript; charset=utf-8'
        return super().guess_type(path)
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
    def log_message(self, format, *args):
        pass  # quiet

if __name__ == '__main__':
    pid_file = os.path.join(DIR, '.dashboard.pid')
    with open(pid_file, 'w') as f:
        f.write(str(os.getpid()))
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Dashboard server started (PID {os.getpid()})")
        print(f"  http://127.0.0.1:{PORT}/rack/telemetry-dashboard.html")
        sys.stdout.flush()
        httpd.serve_forever()
