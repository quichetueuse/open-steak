import pytest
from calcul import add, substract, multiply, divide


def test_add():
    a: int = 10
    b: int = 5
    result = add(a, b)
    assert result == 15

def test_substract():
    a: int = 10
    b: int = 5
    result = substract(a, b)
    assert result == 5

def test_multiply():
    a: int = 10
    b: int = 5
    result = multiply(a, b)
    assert result == 50

def test_divide():
    a: int = 10
    b: int = 5
    result = divide(a, b)
    assert result == 2
    with pytest.raises(ZeroDivisionError):
        result_error = divide(a, 0)
