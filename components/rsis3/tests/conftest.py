"""Pytest bootstrap: make the rsis package importable from the tests dir."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
