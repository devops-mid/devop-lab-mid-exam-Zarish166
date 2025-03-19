import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Import directly from app.py

import pytest
from app.app import app  # Ensure this path is correct

def test_sample():
    assert 1 + 1 == 2  # Simple test to verify pytest is working
