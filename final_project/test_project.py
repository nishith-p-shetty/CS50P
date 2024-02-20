import pytest
from support import add, subtract, multiply, divide, exponentiate, modulus, square_root
from project import add, subtract, multiply, divide, exponentiate, modulus, square_root

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0

    with pytest.raises(ValueError):
        divide(5, 0)

def test_exponentiate():
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 0) == 1
    assert exponentiate(4, 0.5) == 2

def test_modulus():
    assert modulus(7, 3) == 1
    assert modulus(10, 5) == 0
    assert modulus(17, 4) == 1

def test_square_root():
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(25) == 5
    with pytest.raises(ValueError):
        square_root(-1)