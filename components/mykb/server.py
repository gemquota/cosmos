"""Recursive markdown documentation server.

Usage:  python3 server.py [port]
        python3 server.py 8080

Serves .md files from all subdirectories with auto-discovery,
syntax highlighting, dark mode, and search.
"""

import os, sys, json, http.server, socketserver, urllib.parse, re
import subprocess
import math
from datetime import datetime, timezone

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
DIR = os.path.dirname(os.path.abspath(__file__))

# ── Session token auth (O5: protect mutating endpoints) ──────────────
# A random token is generated at server start.  Clients must pass it via
# ``Authorization: Bearer <token>`` on POST/PUT/DELETE endpoints.
# GET endpoints remain unauthenticated (read-only).
import secrets
import hashlib
SESSION_TOKEN = secrets.token_hex(32)
SESSION_TOKEN_HASH = hashlib.sha256(SESSION_TOKEN.encode()).hexdigest()[:16]
print(f"   Session token: {SESSION_TOKEN_HASH} (use Authorization: Bearer <token>)")

# Load search index at startup
SEARCH_INDEX = None
SEARCH_DIR = os.path.join(DIR, '.wiki-daemon')
SEARCH_PATH = os.path.join(SEARCH_DIR, 'search_index.json')
if os.path.exists(SEARCH_PATH):
    try:
        import math
        with open(SEARCH_PATH) as f:
            SEARCH_INDEX = json.load(f)
        print(f"   Search index: {len(SEARCH_INDEX['paths'])} docs")
    except Exception as e:
        print(f"   Search index: failed to load ({e})")

def search_query(q, limit=20):
    if not SEARCH_INDEX or not q.strip():
        return []
    q = q.lower().strip()
    query_words = set(re.findall(r'[a-z0-9]+', q))
    if not query_words:
        return []
    
    # Score each document by TF-IDF cosine similarity
    scores = []
    for i, doc in enumerate(SEARCH_INDEX['docs']):
        doc_words = doc.split()
        score = 0
        for w in query_words:
            if w in SEARCH_INDEX['idf']:
                tf = doc_words.count(w) / max(len(doc_words), 1)
                score += tf * SEARCH_INDEX['idf'][w]
        if score > 0:
            scores.append((score, i))
    
    scores.sort(key=lambda x: -x[0])
    results = []
    for score, i in scores[:limit]:
        # Get relative path
        full = SEARCH_INDEX['paths'][i]
        rel = os.path.relpath(full, DIR)
        # Get title from frontmatter
        with open(full) as f:
            first = f.read(300)
        m = re.search(r'title:\s*"?([^"\n]+)"?', first)
        title = m.group(1) if m else os.path.basename(full).replace('.md', '')
        results.append({
            'path': rel,
            'title': title,
            'score': round(score, 3)
        })
    return results


def get_system_stats():
    """Gather system statistics about the wiki bundle."""
    from collections import Counter
    
    stats = {
        'files': {'total': 0, 'entities': 0, 'sessions': 0, 'domains': 0},
        'sizes': {'total_bytes': 0, 'smallest': None, 'largest': None},
        'graph': {'nodes': 0, 'edges': 0},
        'domains': {},
        'tags': {},
    }
    
    entity_count = 0
    domain_counts = Counter()
    tag_counts = Counter()
    
    for root, dirs, files in os.walk(DIR):
        for fn in files:
            if not fn.endswith('.md'):
                continue
            fpath = os.path.join(root, fn)
            sz = os.path.getsize(fpath)
            stats['files']['total'] += 1
            stats['sizes']['total_bytes'] += sz
            
            if 'supercategories' in root:
                entity_count += 1
                if fn not in ('index.md', 'overview.md'):
                    parts = root.split(os.sep)
                    if 'domains' in parts:
                        didx = parts.index('domains')
                        if didx + 1 < len(parts):
                            domain_counts[parts[didx + 1]] += 1
                    # Read tags
                    try:
                        with open(fpath) as fh:
                            first = fh.read(300)
                        tm = re.search(r'tags:\s*\[(.*?)\]', first)
                        if tm:
                            tags = [t.strip().strip("\"'") for t in tm.group(1).split(',') if t.strip()]
                            for t in tags:
                                if t not in ('entity', 'ast', 'acronym'):
                                    tag_counts[t] += 1
                    except:
                        pass
            
            if stats['sizes']['smallest'] is None or sz < stats['sizes']['smallest']['size']:
                rel = os.path.relpath(fpath, DIR)
                stats['sizes']['smallest'] = {'path': rel, 'size': sz}
            if stats['sizes']['largest'] is None or sz > stats['sizes']['largest']['size']:
                rel = os.path.relpath(fpath, DIR)
                stats['sizes']['largest'] = {'path': rel, 'size': sz}
    
    # Session count
    session_dir = os.path.join(DIR, 'wiki', 'sessions')
    if os.path.isdir(session_dir):
        stats['files']['sessions'] = len([f for f in os.listdir(session_dir) if f.endswith('.md')])
    
    stats['files']['entities'] = entity_count
    stats['domains'] = dict(domain_counts.most_common())
    stats['tags'] = dict(tag_counts.most_common(20))
    
    # Graph stats
    graph_path = os.path.join(DIR, '.wiki-daemon', 'graph.json')
    if os.path.exists(graph_path):
        try:
            with open(graph_path) as f:
                g = json.load(f)
            stats['graph']['nodes'] = len(g.get('nodes', []))
            stats['graph']['edges'] = len(g.get('edges', []))
        except:
            pass
    
    stats['sizes']['total_mb'] = round(stats['sizes']['total_bytes'] / 1024 / 1024, 1)
    stats['sizes']['smallest']['size_kb'] = round(stats['sizes']['smallest']['size'] / 1024, 2)
    stats['sizes']['largest']['size_kb'] = round(stats['sizes']['largest']['size'] / 1024, 2)
    
    return stats

class Handler(http.server.SimpleHTTPRequestHandler):
    def send_json(self, data):
        """Send JSON response with CORS headers."""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        
        if parsed.path == '/graph.json':
            graph_path = os.path.join(DIR, '.wiki-daemon', 'graph.json')
            if os.path.exists(graph_path):
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                with open(graph_path) as f:
                    self.wfile.write(f.read().encode())
            else:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"nodes":[],"edges":[]}')
            return
        
        if parsed.path == '/search':
            q = params.get('q', [''])[0]
            results = search_query(q)
            self.send_json(results)
            return
        
        if parsed.path == '/api/stats':
            stats = get_system_stats()
            self.send_json(stats)
            return
        

        # ── Hybrid Search API ──
        if parsed.path == '/api/v2/search/hybrid':
            q = params.get('q', [''])[0]
            if not q:
                self.send_json({'query': '', 'results': [], 'total': 0})
                return
            try:
                import importlib.util
                sf_path = os.path.join(DIR, '.wiki-daemon', 'search_fusion.py')
                spec = importlib.util.spec_from_file_location('sf_module', sf_path)
                sf = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(sf)
                index = sf.load_index()
                if not index:
                    self.send_json({'error': 'Search index not built. Run: python3 .wiki-daemon/search_fusion.py build-index'})
                    return
                results = sf.search_query(index, q)
                self.send_json({'query': q, 'results': results, 'total': len(results)})
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        
        # ── Graph Topology API ──
        if parsed.path == '/api/v2/graph/topology':
            try:
                graph_path = os.path.join(DIR, '.wiki-daemon', 'graph.json')
                root_id = params.get('root', [None])[0]
                depth = int(params.get('depth', ['2'])[0])
                with open(graph_path) as f:
                    g = json.load(f)
                if root_id:
                    # Build adjacency list
                    adj = {}
                    for e in g.get('edges', []):
                        adj.setdefault(e['source'], set()).add(e['target'])
                        adj.setdefault(e['target'], set()).add(e['source'])
                    # BFS from root
                    visited = set([root_id])
                    queue = [(root_id, 0)]
                    while queue:
                        node, d = queue.pop(0)
                        if d >= depth: continue
                        for neighbor in adj.get(node, set()):
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append((neighbor, d + 1))
                    # Filter nodes and edges
                    node_map = {n['id']: n for n in g.get('nodes', [])}
                    filtered_nodes = [node_map[nid] for nid in visited if nid in node_map]
                    filtered_edges = [e for e in g.get('edges', []) 
                                      if e['source'] in visited and e['target'] in visited]
                    self.send_json({
                        'nodes': filtered_nodes,
                        'edges': filtered_edges,
                        'root': root_id,
                        'depth': depth,
                        'total_nodes': len(g.get('nodes', [])),
                        'total_edges': len(g.get('edges', []))
                    })
                else:
                    self.send_json(g)
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        
        # ── Linter Health API ──
        if parsed.path == '/api/v2/health/lint':
            try:
                import importlib.util
                kl_path = os.path.join(DIR, '.wiki-daemon', 'kb_linter.py')
                spec = importlib.util.spec_from_file_location('kl_module', kl_path)
                kl = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(kl)
                report = kl.lint(return_json=True)
                self.send_json(report)
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        
        # ── Temporal History: file change log ──
        if parsed.path.startswith('/api/v2/history/log/'):
            filepath = parsed.path.replace('/api/v2/history/log/', '', 1)
            try:
                eng = os.path.join(DIR, '.wiki-daemon', 'temporal_engine.py')
                result = subprocess.run([sys.executable, eng, 'history', filepath],
                    capture_output=True, text=True, timeout=10)
                data = json.loads(result.stdout) if result.stdout else []
                self.send_json(data)
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        
        # ── Temporal History: time-travel snapshot ──
        if parsed.path.startswith('/api/v2/history/snapshot'):
            filepath = params.get('path', [''])[0]
            timestamp = params.get('ts', [''])[0]
            if not filepath or not timestamp:
                self.send_json({'error': 'Required: path=<filepath>&ts=<timestamp>'})
                return
            try:
                eng = os.path.join(DIR, '.wiki-daemon', 'temporal_engine.py')
                result = subprocess.run([sys.executable, eng, 'snapshot', filepath, timestamp],
                    capture_output=True, text=True, timeout=10)
                data = json.loads(result.stdout) if result.stdout else {'error': 'No data'}
                self.send_json(data)
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        
        # ── Build search index ──
        if parsed.path == '/api/v2/search/build':
            try:
                result = subprocess.run([sys.executable, os.path.join(DIR, '.wiki-daemon', 'search_fusion.py'), 'build-index'],
                    capture_output=True, text=True, timeout=120)
                self.send_json({'status': 'ok' if result.returncode == 0 else 'error', 'output': result.stdout})
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        

        def _load_audit_module():
            import importlib.util
            sa_path = os.path.join(DIR, '.wiki-daemon', 'build_stub_audit.py')
            spec = importlib.util.spec_from_file_location('build_stub_audit', sa_path)
            sa = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(sa)
            return sa

        # ── Stub Auditor live data ──
        if parsed.path == '/api/v2/stubs':
            try:
                self.send_json(_load_audit_module().scan_stubs())
            except Exception as e:
                self.send_json({'error': str(e)})
            return

        # ── Guidance live data (coverage + focus + guidance queue) ──
        if parsed.path == '/api/v2/guidance':
            try:
                self.send_json(_load_audit_module().scan_guidance())
            except Exception as e:
                self.send_json({'error': str(e)})
            return

        # ── Guidance queue status ──
        if parsed.path == '/api/v2/guidance/queue':
            buffer_dir = os.path.join(DIR, '.wiki-daemon', 'buffers')

            def _load(p):
                try:
                    with open(p, encoding='utf-8') as fh:
                        return json.load(fh)
                except Exception:
                    return None

            self.send_json({
                'queue': _load(os.path.join(buffer_dir, 'guidance-queue.json')),
                'guidance_manifest': _load(os.path.join(buffer_dir, 'guidance-inference.json')),
                'stub_queue': _load(os.path.join(buffer_dir, 'stub-audit-queue.json')),
                'manifest': _load(os.path.join(buffer_dir, 'stub-audit-inference.json')),
            })
            return

        # ── Stub Auditor queue status ──
        if parsed.path == '/api/v2/stubs/queue':
            buffer_dir = os.path.join(DIR, '.wiki-daemon', 'buffers')

            def _load(p):
                try:
                    with open(p, encoding='utf-8') as fh:
                        return json.load(fh)
                except Exception:
                    return None

            self.send_json({
                'queue': _load(os.path.join(buffer_dir, 'stub-audit-queue.json')),
                'manifest': _load(os.path.join(buffer_dir, 'stub-audit-inference.json')),
            })
            return

        # ── Serve individual file content ──
        if parsed.path == '/api/file':
            filepath = params.get('path', [''])[0]
            if not filepath:
                self.send_json({'error': 'Missing path parameter'})
                return
            safe = os.path.normpath(os.path.join(DIR, filepath))
            if not safe.startswith(DIR):
                self.send_json({'error': 'Path traversal blocked'})
                return
            if not os.path.isfile(safe):
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'File not found: ' + filepath}).encode())
                return
            try:
                with open(safe, 'r', encoding='utf-8', errors='replace') as fh:
                    md = fh.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                self.wfile.write(md.encode('utf-8'))
            except Exception as e:
                self.send_json({'error': str(e)})
            return

        # ── List all .md files ──
        if self.path == '/files.json':
            # Serve the enriched files.json (path + type + title + tags) from
            # disk when present so the app's Type grouping, Content/Meta split
            # and badges work identically in live and static modes. Fall back
            # to a plain path list if the enriched snapshot is missing.
            enriched = os.path.join(DIR, 'files.json')
            if os.path.isfile(enriched):
                try:
                    with open(enriched, encoding='utf-8') as fh:
                        self.send_json(json.load(fh))
                    return
                except Exception:
                    pass
            # Recursively find all .md files, return relative paths
            md_files = []
            for root, dirs, files in os.walk(DIR):
                dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
                for f in sorted(files):
                    if f.endswith('.md'):
                        full = os.path.join(root, f)
                        rel = os.path.relpath(full, DIR)
                        md_files.append(rel)
            self.send_json(md_files)
            return
        
        # Fall through to default file server for everything else
        return super().do_GET()

    def _run_daemon_script(self, script, args, timeout=300):
        path = os.path.join(DIR, '.wiki-daemon', script)
        try:
            result = subprocess.run([sys.executable, path] + args,
                                    capture_output=True, text=True,
                                    cwd=DIR, timeout=timeout)
            return {'ok': result.returncode == 0,
                    'output': (result.stdout or '') + (result.stderr or '')}
        except Exception as e:
            return {'ok': False, 'output': str(e)}

    def _safe_md_path(self, raw):
        """Resolve an API-supplied path to a writable .md file under DIR."""
        raw = (raw or '').replace('\\', '/').lstrip('/')
        if not raw.endswith('.md'):
            raw += '.md'
        safe = os.path.normpath(os.path.join(DIR, raw))
        if not safe.startswith(DIR + os.sep) and safe != DIR:
            return None
        rel = os.path.relpath(safe, DIR).replace(os.sep, '/')
        bad = ('/.' in '/' + rel) or rel.startswith('.') or rel.startswith('__pycache__')
        bad = bad or rel.startswith('.wiki-daemon/') or rel in ('server.py', 'index.html')
        bad = bad or not os.path.isfile(safe)
        if bad:
            return None
        return safe

    def _run_git(self, args):
        try:
            r = subprocess.run(args, capture_output=True, text=True, cwd=DIR, timeout=60)
            return {'ok': r.returncode == 0, 'output': (r.stdout or '') + (r.stderr or '')}
        except Exception as e:
            return {'ok': False, 'output': str(e)}

    def _git_or_fs(self, args, fallback):
        """git command with plain-filesystem fallback for untracked files."""
        r = self._run_git(args)
        if r['ok']:
            return r
        try:
            fallback()
            return {'ok': True, 'output': 'filesystem operation (untracked file)'}
        except Exception as e:
            r['output'] = (r['output'] + '\nfs fallback failed: %s' % e).strip()
            return r

    def _read_json_body(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            return json.loads(self.rfile.read(length).decode('utf-8')) if length else {}
        except Exception as e:
            self.send_json({'error': 'Invalid JSON body: %s' % e})
            return None

    def _check_auth(self) -> bool:
        """Verify the Authorization header matches the session token."""
        auth = self.headers.get('Authorization', '')
        if not auth.startswith('Bearer '):
            return False
        return secrets.compare_digest(auth[7:], SESSION_TOKEN)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        # All POST endpoints require auth (mutating operations)
        if not self._check_auth():
            self.send_response(401)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"error": "Missing or invalid Authorization header"}')
            return
        if parsed.path == '/api/v2/stubs/queue/plan':
            self.send_json(self._run_daemon_script('drain_stub_queue.py', ['--plan']))
            return
        if parsed.path == '/api/v2/stubs/queue/apply':
            self.send_json(self._run_daemon_script('drain_stub_queue.py', ['--apply']))
            return
        if parsed.path == '/api/v2/stubs/build':
            self.send_json(self._run_daemon_script('build_stub_audit.py', []))
            return

        if parsed.path == '/api/v2/guidance/plan':
            self.send_json(self._run_daemon_script('drain_guidance.py', ['--plan']))
            return
        if parsed.path == '/api/v2/guidance/apply':
            self.send_json(self._run_daemon_script('drain_guidance.py', ['--apply']))
            return

        # ── Article tools: edit / archive / delete ──
        if parsed.path == '/api/v2/file':
            body = self._read_json_body()
            if body is None:
                return
            safe = self._safe_md_path(body.get('path', ''))
            if not safe:
                self.send_json({'error': 'Unwritable or missing path'})
                return
            content = body.get('content')
            if content is None:
                self.send_json({'error': 'Missing content'})
                return
            try:
                with open(safe, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                rel = os.path.relpath(safe, DIR)
                print(f"   File saved: {rel}")
                self.send_json({'status': 'ok', 'path': rel})
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        if parsed.path == '/api/v2/file/archive':
            body = self._read_json_body()
            if body is None:
                return
            safe = self._safe_md_path(body.get('path', ''))
            if not safe:
                self.send_json({'error': 'Unwritable or missing path'})
                return
            rel = os.path.relpath(safe, DIR)
            today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
            dst = os.path.join(DIR, 'raw', 'archive', 'stub-audit-' + today, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            self.send_json(self._git_or_fs(
                ['git', 'mv', safe, dst],
                lambda: os.rename(safe, dst)))
            return
        if parsed.path == '/api/v2/file/delete':
            body = self._read_json_body()
            if body is None:
                return
            safe = self._safe_md_path(body.get('path', ''))
            if not safe:
                self.send_json({'error': 'Unwritable or missing path'})
                return
            self.send_json(self._git_or_fs(
                ['git', 'rm', '-q', safe],
                lambda: os.remove(safe)))
            return

        if parsed.path not in ('/api/v2/stubs/queue', '/api/v2/guidance/queue'):
            self.send_error(404, 'Not found')
            return

        try:
            length = int(self.headers.get('Content-Length', 0))
            payload = json.loads(self.rfile.read(length).decode('utf-8')) if length else {}
        except Exception as e:
            self.send_json({'error': 'Invalid JSON body: %s' % e})
            return
        items = payload.get('items', [])
        if not isinstance(items, list):
            self.send_json({'error': 'Body must be {"items": [...]}'})
            return

        def _save_queue(filename, label):
            try:
                buffer_dir = os.path.join(DIR, '.wiki-daemon', 'buffers')
                os.makedirs(buffer_dir, exist_ok=True)
                queue_path = os.path.join(buffer_dir, filename)
                payload.setdefault('queued_at', datetime.now(timezone.utc).isoformat(timespec='seconds'))
                payload['count'] = len(items)
                tmp = queue_path + '.tmp'
                with open(tmp, 'w', encoding='utf-8') as fh:
                    json.dump(payload, fh, indent=1, ensure_ascii=False)
                os.replace(tmp, queue_path)
                rel = os.path.relpath(queue_path, DIR)
                print(f"   {label} saved: {rel} ({len(items)} items)")
                return {'status': 'ok', 'path': rel, 'count': len(items)}
            except Exception as e:
                return {'error': str(e)}

        if parsed.path == '/api/v2/guidance/queue':
            self.send_json(_save_queue('guidance-queue.json', 'Guidance queue'))
            return
        self.send_json(_save_queue('stub-audit-queue.json', 'Stub queue'))

    def log_message(self, format, *args):
        print(f"  {args[0]} {args[1]} {args[2]}")

if __name__ == '__main__':
    # Check daemon buffer directory health
    buffer_dir = os.path.join(DIR, '.wiki-daemon', 'buffers')
    if not os.path.isdir(buffer_dir):
        print(f"   ⚠ Buffer dir missing: {buffer_dir}")
        print(f"     Run: mkdir -p {buffer_dir}")
    else:
        buffer_count = len(os.listdir(buffer_dir))
        print(f"   Daemon buffers: {buffer_dir} ({buffer_count} files)")
        signals_dir = os.path.join(buffer_dir, 'signals')
        if os.path.isdir(signals_dir):
            sig_count = len(os.listdir(signals_dir))
            print(f"   Pending signals: {sig_count}")
    
    # Count .md files
    count = sum(1 for root, dirs, files in os.walk(DIR) 
                for f in files if f.endswith('.md')
                if not any(d.startswith('.') for d in root.split(os.sep)))
    print(f"📄 md — Self-Contained Documentation Viewer")
    print(f"   Serving: {DIR}")
    print(f"   .md files: {count}")
    print(f"   URL: http://localhost:{PORT}")
    print(f"   Auto-discovers files recursively from all subdirectories")
    class ReuseAddrTCPServer(socketserver.TCPServer):
        allow_reuse_address = True
    with ReuseAddrTCPServer(('', PORT), Handler) as httpd:
        httpd.serve_forever()
