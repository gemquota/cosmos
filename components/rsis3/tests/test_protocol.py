"""Protocol conformance suite — cosmos-protocol/1 (Phase 17).

Unit-level conformance: fail-closed negotiation, capability handshake
shape, and spec presence. When a live verify-server is reachable, an
HTTP reference-client check drives ``GET /version`` / ``GET /health``
from the spec alone (skipped otherwise).
"""
import json
import unittest
import urllib.request
from pathlib import Path

from rsis.protocol import capabilities, negotiate, spec_path

BASE = Path(__file__).resolve().parents[1]


class ConformanceTests(unittest.TestCase):
    def test_negotiate_fail_closed(self):
        self.assertTrue(negotiate("cosmos-protocol/1"))
        self.assertTrue(negotiate("cosmos-protocol/1.2"))
        self.assertFalse(negotiate("cosmos-protocol/2"))
        self.assertFalse(negotiate("other-protocol/1"))
        self.assertFalse(negotiate("garbage"))
        self.assertFalse(negotiate(None))
        self.assertFalse(negotiate("cosmos-protocol/"))

    def test_capability_handshake_shape(self):
        caps = capabilities()
        self.assertEqual(caps["protocol"], "cosmos-protocol/1")
        self.assertEqual(caps["name"], "cosmos-protocol")
        self.assertTrue(caps["fail_closed"])
        for area in ("memory", "verification", "federation", "attestation"):
            self.assertIn(area, caps["endpoints"])
            self.assertTrue(caps["endpoints"][area])

    def test_spec_exists(self):
        self.assertTrue(spec_path(BASE).is_file(),
                        "docs/protocol.md must exist for the spec")


@unittest.skipUnless(
    (Path(BASE) / "rack" / "verify-server.pid").is_file(),
    "no live verify-server")
class LiveConformanceTests(unittest.TestCase):
    """Plain-HTTP reference client driven from the spec (no SDK)."""

    def test_version_and_health(self):
        with urllib.request.urlopen("http://127.0.0.1:8788/version",
                                    timeout=5) as r:
            caps = json.loads(r.read())
            self.assertEqual(caps["protocol"], "cosmos-protocol/1")
            self.assertTrue(caps["fail_closed"])
        with urllib.request.urlopen("http://127.0.0.1:8788/health",
                                    timeout=5) as r:
            self.assertEqual(r.status, 200)


if __name__ == "__main__":
    unittest.main()
