"""
conftest.py

This file is automatically used by pytest to help set up and organise your tests.

What is conftest.py for?
- It lets you share code and settings across all your test files, so you don't have to
  repeat yourself.
- You can add 'fixtures' here, which are reusable bits of code that help
  prepare or clean up before and after tests run.
- You can also change how pytest behaves, or set up your test environment.

You don't need to import conftest.py in your test files—pytest finds and uses it
automatically.
"""

import os
import sys

# Add the src/ folder to Python's search path so tests can import your main code
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
)
