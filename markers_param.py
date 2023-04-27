import pytest

@pytest.mark.parametrize("a,b",
                        [(10,20)])
def test_addition(a,b):
    print(a+b)

@pytest.mark.parametrize("Firstname,Lastname",
                         [("Kavya","VB"),("Madhu","VB")])
def test_printname(Firstname,Lastname):
    print(Firstname+Lastname)