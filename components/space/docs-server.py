"""Recursive markdown documentation server.

Usage:  python3 server.py [port]
        python3 server.py 8080

Serves .md files from all subdirectories with auto-discovery,
syntax highlighting, dark mode, and search.
"""

import os, sys, json, http.server, socketserver, glob

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/files.json':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            # Recursively find all .md files, return relative paths
            md_files = []
            for root, dirs, files in os.walk(DIR):
                # Skip hidden directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('__pycache__', 'node_modules', '.git', 'dist')]
                for f in sorted(files):
                    if f.endswith('.md'):
                        full = os.path.join(root, f)
                        rel = os.path.relpath(full, DIR)
                        md_files.append(rel)
            self.wfile.write(json.dumps(md_files).encode())
            return
        return super().do_GET()

    def log_message(self, format, *args):
        print(f"  {args[0]} {args[1]} {args[2]}")

if __name__ == '__main__':
    # Count .md files
    count = sum(1 for root, dirs, files in os.walk(DIR) 
                for f in files if f.endswith('.md')
                if not any(d.startswith('.') for d in root.split(os.sep)))
    print(f"📄 md — Self-Contained Documentation Viewer")
    print(f"   Serving: {DIR}")
    print(f"   .md files: {count}")
    print(f"   URL: http://localhost:{PORT}")
    print(f"   Auto-discovers files recursively from all subdirectories")
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        httpd.serve_forever()
