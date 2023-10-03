import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert num * num == 49

def check(x):
    return x
def test_check():
    x = 100
    assert x >= 100

def fun(x):
    return x
def test_fun():
    assert fun(10) + 2 == 12

def multiply(x, y):
    return x * y
def test_multiply():
    result = multiply(10, 12)
    assert result == 120