import pytest

@pytest.mark.start
def test_start():
    print("Welcome to my Project")

@pytest.mark.login
def test_login():
    print("Login")

@pytest.mark.logout
def test_logout():
    print("Logout")

