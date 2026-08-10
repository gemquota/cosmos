"""Phase 12 — collaborative ops tests (identities, tokens, authz chain)."""
import tempfile
import time
import unittest
from pathlib import Path

from rsis.users import (
    add_user, authorize, authenticate, capabilities_for, ensure_users,
    issue_token, load_users, verify_token,
)


class UsersTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.ws = Path(self._tmp.name)
        self.ws.joinpath(".rsis").mkdir()
        ensure_users(self.ws)
        add_user(self.ws, "alice", "Alice", "observer", projects=["cosmos"])
        add_user(self.ws, "bob", "Bob", "contributor", projects=["cosmos"])
        add_user(self.ws, "carol", "Carol", "approver",
                 projects=["cosmos", "other-repo"])

    def tearDown(self):
        self._tmp.cleanup()

    def test_token_roundtrip(self):
        tok = issue_token(self.ws, "alice", ttl_s=3600)
        self.assertTrue(tok)
        user = verify_token(self.ws, tok)
        self.assertEqual(user["id"], "alice")
        self.assertIsNone(verify_token(self.ws, tok + "x"))
        self.assertIsNone(issue_token(self.ws, "nobody"))

    def test_token_expiry(self):
        tok = issue_token(self.ws, "alice", ttl_s=1)
        self.assertTrue(verify_token(self.ws, tok))
        time.sleep(1.1)
        self.assertIsNone(verify_token(self.ws, tok))

    def test_authenticate(self):
        tok = issue_token(self.ws, "bob")
        self.assertEqual(authenticate(self.ws, tok)["id"], "bob")
        self.assertIsNone(authenticate(self.ws, None))

    def test_role_capabilities(self):
        self.assertEqual(capabilities_for({"role": "observer"}), {"read"})
        self.assertEqual(capabilities_for({"role": "contributor"}),
                         {"read", "propose"})
        self.assertEqual(capabilities_for({"role": "approver"}),
                         {"read", "propose", "approve", "rollback"})

    def test_authorize_chain(self):
        alice = load_users(self.ws)["users"][0]
        bob = load_users(self.ws)["users"][1]
        carol = load_users(self.ws)["users"][2]
        ok, _ = authorize(self.ws, alice, "read", "cosmos")
        self.assertTrue(ok)
        ok, reason = authorize(self.ws, alice, "approve", "cosmos")
        self.assertFalse(ok)  # observer cannot approve
        ok, reason = authorize(self.ws, bob, "approve", "cosmos")
        self.assertFalse(ok)  # contributor cannot approve
        ok, _ = authorize(self.ws, carol, "approve", "cosmos")
        self.assertTrue(ok)
        ok, reason = authorize(self.ws, carol, "approve", "other-repo")
        self.assertTrue(ok)   # member of other-repo
        ok, reason = authorize(self.ws, carol, "approve", "third-repo")
        self.assertFalse(ok)  # NOT a member — approver != all projects
        ok, reason = authorize(self.ws, None, "read", "cosmos")
        self.assertFalse(ok)  # no identity
        ok, _ = authorize(self.ws, carol, "rollback", "cosmos")
        self.assertTrue(ok)

    def test_policy_blocks_action(self):
        carol = load_users(self.ws)["users"][2]
        policy = self.ws / "rack" / "policy.json"
        policy.parent.mkdir(exist_ok=True)
        policy.write_text('{"version": 1, "capability_blocks": ["rollback"]}')
        ok, reason = authorize(self.ws, carol, "rollback", "cosmos")
        self.assertFalse(ok)  # policy wins over role
        ok, _ = authorize(self.ws, carol, "approve", "cosmos")
        self.assertTrue(ok)

    def test_add_update(self):
        add_user(self.ws, "dave", "Dave", "approver", projects=["*"])
        dave = [u for u in load_users(self.ws)["users"] if u["id"] == "dave"][0]
        ok, _ = authorize(self.ws, dave, "approve", "any-project")
        self.assertTrue(ok)  # "*" membership
        # update role downgrade
        add_user(self.ws, "dave", "Dave", "observer", projects=["*"])
        dave = [u for u in load_users(self.ws)["users"] if u["id"] == "dave"][0]
        self.assertEqual(dave["role"], "observer")


if __name__ == "__main__":
    unittest.main()
