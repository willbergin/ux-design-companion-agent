#!/usr/bin/env python3
"""One-command packaging and static test runner for the portable agent."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for command in (
    [sys.executable, str(ROOT / 'scripts/build.py'), '--check'],
    [sys.executable, '-m', 'unittest', 'discover', '-s', str(ROOT / 'tests'), '-v'],
):
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        raise SystemExit(result.returncode)
print('Static validation succeeded. Behavioral and accessibility tests still require a target harness/browser.')
