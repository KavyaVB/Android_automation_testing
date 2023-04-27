import pytest

@pytest.fixture
def test_welcome():
    print("Welcome to my application")
    yield
    print("Thanks for using this application")

def test_app1(test_welcome):
    print("Make use of the application")

def test_app2(test_welcome):
    print("Another app")

def test_app3(test_welcome):
    print("One more app")