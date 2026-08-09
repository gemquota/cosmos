"""Phase 2 bridge test matrix — cosmos-envelope/1 hardening.

Covers the multi-phase roadmap exit criterion for Phase 2:
traversal denial, oversized artifacts, rate limiting, missing files,
text+image round-trip, plus structured/audio/PDF/video handling and the
origin guard.

Runs under pytest or stdlib unittest:

    cd components/rsis3 && python3 -m pytest tests/test_bridge.py
    cd components/rsis3 && python3 -m unittest tests.test_bridge -v
"""
import base64
import http.client
import json
import os
import shutil
import socket
import tempfile
import struct
import subprocess
import sys
import time
import unittest
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
RSIS3 = os.path.dirname(HERE)          # components/rsis3
NODE = os.environ.get('NODE_BIN', 'node')

FREE_PORT_SOCK = None


def free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port


def tiny_png():
    def chunk(t, d):
        c = struct.pack('>I', len(d)) + t + d
        return c + struct.pack('>I', zlib.crc32(t + d) & 0xFFFFFFFF)
    ihdr = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
    raw = b'\x00' + b'\xff\x00\x00'
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr)
            + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b''))


def tiny_pdf():
    content = b'BT /F1 12 Tf 72 720 Td (Hello Cosmos Bridge) Tj ET'
    objs = [
        b'1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj',
        b'2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj',
        b'3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] '
        b'/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj',
        b'4 0 obj << /Length %d >> stream\n' % len(content) + content + b'\nendstream endobj',
        b'5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj',
    ]
    out = b'%PDF-1.4\n'
    offsets = []
    for o in objs:
        offsets.append(len(out))
        out += o + b'\n'
    xref_pos = len(out)
    out += b'xref\n0 %d\n' % (len(objs) + 1)
    out += b'0000000000 65535 f \n'
    for off in offsets:
        out += b'%010d 00000 n \n' % off
    out += b'trailer << /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objs) + 1, xref_pos)
    return out


def data_url(mime, raw):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(raw).decode('ascii'))


def chat_payload(artifacts, question='ping', session_id=None):
    payload = {'messages': [{'role': 'user', 'content': question}], 'artifacts': artifacts}
    if session_id:
        payload['session_id'] = session_id
    return payload


class BridgeServer:
    """Spawn the stdlib bridge on a free port and wait for /health."""

    def __init__(self, env_extra=None):
        self.port = free_port()
        env = os.environ.copy()
        env.pop('GEMINI_API_KEY', None)
        env.update({'RSIS_BRIDGE_PORT': str(self.port)})
        env.update(env_extra or {})
        self.proc = subprocess.Popen(
            [NODE, 'rack/bridge/server.mjs'],
            cwd=RSIS3,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self._wait_health(15)

    def _wait_health(self, timeout):
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                status, _, data = self.request('GET', '/health')
                if status == 200 and json.loads(data).get('ok'):
                    return
            except Exception:
                pass
            if self.proc.poll() is not None:
                raise RuntimeError('bridge exited early:\n' + self.output())
            time.sleep(0.15)
        raise RuntimeError('bridge /health not ready:\n' + self.output())

    def output(self):
        try:
            return self.proc.stdout.read().decode('utf-8', 'replace') if self.proc.stdout else ''
        except Exception:
            return ''

    @staticmethod
    def header(hdrs, name):
        low = name.lower()
        for k, v in hdrs.items():
            if k.lower() == low:
                return v
        return None

    def request(self, method, path, payload=None, headers=None, raw=None):
        conn = http.client.HTTPConnection('127.0.0.1', self.port, timeout=60)
        h = {'Content-Type': 'application/json'}
        if headers:
            h.update(headers)
        body = raw if raw is not None else (json.dumps(payload) if payload is not None else None)
        conn.request(method, path, body=body, headers=h)
        res = conn.getresponse()
        data = res.read()
        conn.close()
        return res.status, dict(res.getheaders()), data

    def chat(self, artifacts, question='ping', headers=None, session_id=None):
        status, hdrs, data = self.request(
            'POST', '/api/chat', chat_payload(artifacts, question, session_id), headers=headers)
        return status, hdrs, data

    def stop(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()


class BridgeCase(unittest.TestCase):
    server = None

    @classmethod
    def setUpClass(cls):
        cls.server = BridgeServer(cls.server_env())

    @classmethod
    def tearDownClass(cls):
        if cls.server:
            cls.server.stop()

    @staticmethod
    def server_env():
        return {'RSIS_BRIDGE_RATE_LIMIT': '10000',
                'RSIS_BRIDGE_ALLOW_ORIGIN': 'http://good.example'}


class BridgeFunctionalTest(BridgeCase):
    """Core Phase 2 matrix: traversal, caps, missing files, round-trips."""

    def artifacts_of(self, data):
        return json.loads(data)['artifacts']

    def test_traversal_denied(self):
        for ref in ('../../../../etc/passwd', '/etc/passwd', 'C:\\windows\\win.ini'):
            status, _, data = self.server.chat([{'ref': ref}])
            self.assertEqual(status, 200)
            arts = self.artifacts_of(data)
            self.assertEqual(arts[0]['status'], 'denied', ref)

    def test_allowlist_deny_prefix(self):
        # Inside an allowed root but under an explicit deny prefix.
        status, _, data = self.server.chat([{'ref': '.rsis/telemetry/000.json'}])
        self.assertEqual(status, 200)
        self.assertEqual(self.artifacts_of(data)[0]['status'], 'denied')

    def test_allowlisted_ref_ok(self):
        status, _, data = self.server.chat([{'ref': '.rsis/strategies.json'}])
        self.assertEqual(status, 200)
        arts = self.artifacts_of(data)
        self.assertNotEqual(arts[0]['status'], 'denied')
        self.assertNotEqual(arts[0]['status'], 'missing')

    def test_missing_file(self):
        status, _, data = self.server.chat([{'ref': 'rack/no-such-file.json'}])
        self.assertEqual(status, 200)
        self.assertEqual(self.artifacts_of(data)[0]['status'], 'missing')

    def test_structured_schema_block(self):
        status, _, data = self.server.chat([{'ref': 'rack/goals_stack.json'}])
        self.assertEqual(status, 200)
        art = self.artifacts_of(data)[0]
        self.assertEqual(art['status'], 'schema')
        self.assertTrue(art['parsed'])
        self.assertGreaterEqual(art['schema']['keys'], 1)
        self.assertIn('goals_stack.json [schema]', json.loads(data)['reply'])

    def test_text_inlined(self):
        status, _, data = self.server.chat([{'ref': 'README.md'}])
        self.assertEqual(status, 200)
        self.assertEqual(self.artifacts_of(data)[0]['status'], 'inlined')

    def test_text_plus_image_round_trip(self):
        png = tiny_png()
        status, _, data = self.server.chat([
            {'ref': 'README.md'},
            {'name': 'dot.png', 'dataUrl': data_url('image/png', png)},
        ])
        self.assertEqual(status, 200)
        arts = self.artifacts_of(data)
        self.assertEqual(arts[0]['status'], 'inlined')
        self.assertEqual(arts[1]['status'], 'image')
        self.assertIn('Bridge offline', json.loads(data)['reply'])

    def test_ndjson_streaming_round_trip(self):
        png = tiny_png()
        status, hdrs, data = self.server.chat(
            [{'ref': 'README.md'}, {'name': 'dot.png', 'dataUrl': data_url('image/png', png)}],
            headers={'Accept': 'application/x-ndjson'},
        )
        self.assertEqual(status, 200)
        self.assertEqual(self.server.header(hdrs, 'Content-Type'), 'application/x-ndjson')
        events = [json.loads(line) for line in data.decode('utf-8').splitlines() if line.strip()]
        types = [e['type'] for e in events]
        self.assertEqual(types[0], 'meta')
        self.assertIn('delta', types)
        self.assertEqual(types[-1], 'done')
        self.assertIn('Bridge offline', events[-1]['reply'])

    def test_oversized_image_capped(self):
        big = b'\x00' * (4 * 1024 * 1024 + 200_000)   # ~4.2 MB raw > 4 MB media cap
        status, _, data = self.server.chat([{'name': 'big.png', 'dataUrl': data_url('image/png', big)}])
        self.assertEqual(status, 200)
        art = self.artifacts_of(data)[0]
        self.assertEqual(art['status'], 'too-large')

    def test_body_too_large_413(self):
        status, _, data = self.server.request(
            'POST', '/api/chat', raw='x' * (6 * 1024 * 1024 + 1024))
        self.assertEqual(status, 413)

    def test_video_rejected(self):
        status, _, data = self.server.chat([
            {'name': 'clip.mp4', 'dataUrl': data_url('video/mp4', b'\x00' * 64)}])
        self.assertEqual(status, 200)
        art = self.artifacts_of(data)[0]
        self.assertEqual(art['status'], 'unsupported')
        self.assertIn('video', (art.get('reason') or ''))

    def test_audio_inline(self):
        status, _, data = self.server.chat([
            {'name': 'note.wav', 'dataUrl': data_url('audio/wav', b'\x00' * 128)}])
        self.assertEqual(status, 200)
        self.assertEqual(self.artifacts_of(data)[0]['status'], 'audio')

    def test_pdf_text_extraction(self):
        status, _, data = self.server.chat([
            {'name': 'doc.pdf', 'dataUrl': data_url('application/pdf', tiny_pdf())}])
        self.assertEqual(status, 200)
        art = self.artifacts_of(data)[0]
        self.assertEqual(art['status'], 'pdf-text')

    def test_cosmos_snapshot_shape(self):
        status, _, data = self.server.request('GET', '/api/cosmos')
        self.assertEqual(status, 200)
        c = json.loads(data)
        for key in ('model', 'llm', 'kg', 'strategies', 'costs', 'artifacts'):
            self.assertIn(key, c)
        self.assertIn('traces', c['costs'])

    def test_origin_guard(self):
        status, _, _ = self.server.request('GET', '/health', headers={'Origin': 'http://evil.example'})
        self.assertEqual(status, 403)
        status, _, _ = self.server.request('GET', '/health', headers={'Origin': 'http://good.example'})
        self.assertEqual(status, 200)
        status, _, _ = self.server.request('GET', '/health', headers={'Origin': 'http://localhost:9999'})
        self.assertEqual(status, 200)


class BridgeRateLimitTest(BridgeCase):
    """Rate limit: RSIS_BRIDGE_RATE_LIMIT=5, window 60s."""

    @staticmethod
    def server_env():
        return {'RSIS_BRIDGE_RATE_LIMIT': '5', 'RSIS_BRIDGE_RATE_WINDOW_MS': '60000'}

    def test_rate_limit_429_with_retry_after(self):
        statuses = []
        retry_after = None
        for _ in range(6):
            status, hdrs, _ = self.server.chat([])
            statuses.append(status)
            if status == 429:
                retry_after = self.server.header(hdrs, 'Retry-After')
        self.assertEqual(statuses[:5], [200] * 5)
        self.assertEqual(statuses[5], 429)
        self.assertIsNotNone(retry_after)


class BridgeSessionTest(BridgeCase):
    """Phase 3: conversation persistence + chat memory loop."""

    _tmp = None

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.mkdtemp(prefix='cosmos-bridge-test-')
        cls.server = BridgeServer(cls.server_env())

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        if cls._tmp:
            shutil.rmtree(cls._tmp, ignore_errors=True)

    @classmethod
    def server_env(cls):
        return {
            'RSIS_BRIDGE_RATE_LIMIT': '10000',
            'RSIS_BRIDGE_MEMORY_N': '2',
            'RSIS_BRIDGE_MEMORY_DIR': os.path.join(cls._tmp, 'syntheses'),
            'RSIS_BRIDGE_SESSIONS_DIR': os.path.join(cls._tmp, 'sessions'),
        }

    def test_persist_and_resume(self):
        sid = 's-test-0001'
        for _ in range(2):
            status, _, data = self.server.chat([], question='hello bridge', session_id=sid)
            self.assertEqual(status, 200)
            self.assertEqual(json.loads(data).get('session_id'), sid)
        # resume endpoint returns the archived conversation
        status, _, data = self.server.request('GET', '/api/sessions/' + sid)
        self.assertEqual(status, 200)
        sess = json.loads(data)
        self.assertEqual(sess['id'], sid)
        self.assertEqual(sess['count'], 4)          # 2 user + 2 assistant
        self.assertEqual(sess['messages'][0]['role'], 'user')
        self.assertEqual(sess['messages'][1]['role'], 'assistant')
        self.assertEqual(sess['messages'][2]['content'], 'hello bridge')
        # list endpoint shows the session
        status, _, data = self.server.request('GET', '/api/sessions')
        self.assertEqual(status, 200)
        listed = json.loads(data)['sessions']
        self.assertTrue(any(x['id'] == sid for x in listed))

    def test_missing_session_404(self):
        status, _, _ = self.server.request('GET', '/api/sessions/s-nope-0000')
        self.assertEqual(status, 404)

    def test_memory_distillation(self):
        sid = 's-memory-0001'
        for _ in range(2):
            status, _, _ = self.server.chat([], question='distill me', session_id=sid)
            self.assertEqual(status, 200)
        note = os.path.join(self._tmp, 'syntheses', 'rsis3-bridge-session-' + sid + '.md')
        self.assertTrue(os.path.exists(note), 'memory note should exist after 2 exchanges')
        text = open(note).read()
        self.assertIn('type: "synthesis"', text)
        self.assertIn('distill me', text)
        # idempotent: a third exchange does not rewrite the note
        os.utime(note, None)
        status, _, _ = self.server.chat([], question='again', session_id=sid)
        self.assertEqual(status, 200)
        self.assertEqual(open(note).read(), text)


class BridgeAuthTest(BridgeCase):
    """Phase 3: optional bearer-token auth for /api/*."""

    @staticmethod
    def server_env():
        return {'RSIS_BRIDGE_RATE_LIMIT': '10000', 'RSIS_BRIDGE_TOKEN': 'secret-token'}

    def test_api_requires_token(self):
        status, _, _ = self.server.request('GET', '/api/cosmos')
        self.assertEqual(status, 401)
        status, _, _ = self.server.request('GET', '/api/cosmos', headers={'Authorization': 'Bearer wrong'})
        self.assertEqual(status, 401)

    def test_bearer_token_allowed(self):
        status, _, _ = self.server.request('GET', '/api/cosmos', headers={'Authorization': 'Bearer secret-token'})
        self.assertEqual(status, 200)

    def test_query_token_allowed(self):
        # EventSource cannot set headers; ?token= is the SSE escape hatch.
        status, _, _ = self.server.request('GET', '/api/cosmos?token=secret-token')
        self.assertEqual(status, 200)

    def test_health_stays_public(self):
        status, _, _ = self.server.request('GET', '/health')
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()
