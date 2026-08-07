"""StubDetector — real improvement-target scanning."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.signals.stub_detector import StubDetector


def write(root: Path, rel: str, text: str) -> Path:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def test_detects_pass_only_bodies(tmp_path):
    write(tmp_path, "rsis/demo.py", (
        "def do_work():\n"
        "    pass\n"
        "\n"
        "def real():\n"
        "    return 1\n"
    ))
    findings = StubDetector(tmp_path).scan()
    kinds = {(f.kind, f.name) for f in findings}
    assert ("pass_body", "do_work") in kinds
    assert ("pass_body", "real") not in kinds


def test_detects_not_implemented_but_skips_abstract(tmp_path):
    write(tmp_path, "rsis/base.py", (
        "import abc\n"
        "\n"
        "class Base(abc.ABC):\n"
        "    @abc.abstractmethod\n"
        "    def run(self):\n"
        "        raise NotImplementedError\n"
        "\n"
        "class Concrete:\n"
        "    def doit(self):\n"
        "        raise NotImplementedError\n"
    ))
    findings = StubDetector(tmp_path).scan()
    kinds = {(f.kind, f.name) for f in findings}
    assert ("not_implemented", "doit") in kinds
    assert ("not_implemented", "run") not in kinds


def test_detects_todo_comments(tmp_path):
    write(tmp_path, "rsis/mod.py", "# TODO: wire up retries\n\ndef f():\n    return 1\n")
    findings = StubDetector(tmp_path).scan()
    assert any(f.kind == "todo" and "retries" in f.pattern for f in findings)


def test_detects_dangling_imports_as_missing_module(tmp_path):
    write(tmp_path, "rsis/mod.py", "from rsis.ghost import Ghost\n\ndef f():\n    return 1\n")
    findings = StubDetector(tmp_path).scan()
    missing = [f for f in findings if f.kind == "missing_module"]
    assert any(f.name == "rsis.ghost" for f in missing)


def test_ignores_out_of_scope_files(tmp_path):
    write(tmp_path, "rsis/ok.py", "def f():\n    pass\n")
    write(tmp_path, "other/ok.py", "def f():\n    pass\n")
    findings = StubDetector(tmp_path).scan()
    assert len(findings) == 1


def test_priority_order(tmp_path):
    write(tmp_path, "rsis/a.py", "# TODO: later\n\ndef f():\n    pass\n")
    write(tmp_path, "rsis/b.py", "from rsis.nope import X\n")
    findings = StubDetector(tmp_path).scan()
    assert findings[0].kind == "missing_module"


def test_to_dict(tmp_path):
    write(tmp_path, "rsis/a.py", "def f():\n    pass\n")
    f = StubDetector(tmp_path).scan()[0]
    d = f.to_dict()
    for key in ("file", "name", "kind", "pattern", "line", "priority"):
        assert key in d
