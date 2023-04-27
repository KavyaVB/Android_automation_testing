import pytest
import sys

@pytest.mark.skip
def test_start():
    print("Welcome to my Project")

@pytest.mark.xfail
def test_login():
    print("Login")

@pytest.mark.skipif(sys.version_info<(3,11), reason="Python version not supported")
def test_logout():
    print("Logout")

