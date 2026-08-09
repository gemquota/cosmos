"""Phase 6 — distributed memory: MyKB note API + coordination lock tests."""
import sys
import tempfile
import unittest
from pathlib import Path

WIKI_DAEMON = Path(__file__).resolve().parents[2] / "mykb" / ".wiki-daemon"
sys.path.insert(0, str(WIKI_DAEMON))

from memory_api import (  # noqa: E402
    MemoryLock, list_notes, search_notes, sessions, write_note,
)


def make_root(tmp: str) -> Path:
    root = Path(tmp)
    (root / "wiki" / "syntheses").mkdir(parents=True)
    return root


class NoteWriteTests(unittest.TestCase):
    def test_create_only_blocks_foreign_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            write_note(root, rel="syntheses/a.md",
                       content="---\nsession_id: \"s1\"\n---\n# A\nbody",
                       session_id="s1")
            with self.assertRaises(FileExistsError):
                write_note(root, rel="syntheses/a.md", content="clobber",
                           session_id="s2")

    def test_owner_session_may_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            write_note(root, rel="syntheses/a.md",
                       content="---\nsession_id: \"s1\"\n---\n# A\nv1",
                       session_id="s1")
            write_note(root, rel="syntheses/a.md",
                       content="---\nsession_id: \"s1\"\n---\n# A\nv2",
                       session_id="s1")
            self.assertEqual(
                (root / "wiki" / "syntheses" / "a.md").read_text(),
                "---\nsession_id: \"s1\"\n---\n# A\nv2")

    def test_path_escape_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            with self.assertRaises(ValueError):
                write_note(root, rel="../../etc/passwd", content="x")

    def test_lock_is_advisory_and_exclusive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            with MemoryLock(root):
                lock2 = MemoryLock(root)
                try:
                    self.assertFalse(lock2.acquire())
                finally:
                    lock2.release()
            # after release the lock is free
            with MemoryLock(root):
                pass


class NoteReadTests(unittest.TestCase):
    def test_list_and_filter_by_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            write_note(root, rel="syntheses/a.md",
                       content="---\nsession_id: \"s1\"\n---\n# A", session_id="s1")
            write_note(root, rel="syntheses/b.md",
                       content="---\nsession_id: \"s2\"\n---\n# B", session_id="s2")
            self.assertEqual(len(list_notes(root)), 2)
            self.assertEqual(len(list_notes(root, session_id="s1")), 1)
            ss = sessions(root)
            self.assertEqual(len(ss), 2)
            self.assertEqual(ss[0]["notes"], 1)

    def test_search_token_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            write_note(root, rel="syntheses/alpha.md",
                       content="# Alpha\ndistributed memory coordination", session_id="s1")
            write_note(root, rel="syntheses/beta.md",
                       content="# Beta\ncost governance budgets", session_id="s2")
            hits = search_notes(root, "memory coordination")
            self.assertEqual(len(hits), 1)
            self.assertEqual(hits[0]["path"], "syntheses/alpha.md")
            self.assertEqual(search_notes(root, "nonexistent-term"), [])


if __name__ == "__main__":
    unittest.main()
