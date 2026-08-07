"""timeout — polling watchdog fallback."""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.timeout import TimeoutError, deadline


def test_polling_watchdog_raises_timeout():
    start = time.monotonic()
    try:
        with deadline(0.15, "test-polling"):
            time.sleep(2)
    except TimeoutError:
        elapsed = time.monotonic() - start
        assert 0.1 <= elapsed < 1.5
        return
    raise AssertionError("deadline did not fire")
