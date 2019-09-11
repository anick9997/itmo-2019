import sys


def my_sum(first, second):
    if len(sys.argv) != 2:
        raise TypeError
    if not isinstance(first, (int, float, complex)):
        raise TypeError
    if not isinstance(second, (int, float, complex)):
        raise TypeError
    return first + second


def my_mult(first, second):
    if len(sys.argv) != 2:
        raise TypeError
    if not isinstance(first, (int, float, complex)):
        raise TypeError
    if not isinstance(second, (int, float, complex)):
        raise TypeError
    return first * second


def my_div(first, second):
    if len(sys.argv) != 2:
        raise TypeError
    if not isinstance(first, (int, float, complex)):
        raise TypeError
    if not isinstance(second, (int, float, complex)):
        raise TypeError
    if second == 0:
        raise ZeroDivisionError
    return first / second
