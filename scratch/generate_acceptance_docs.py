#!/usr/bin/env python3
"""Compatibility entry point for current acceptance-document generation."""

import runpy
from pathlib import Path

SCRIPT = Path(__file__).with_name("update_current_acceptance_docs.py")
runpy.run_path(str(SCRIPT), run_name="__main__")
