import unittest
from arithmetics import *


class TestMath(unittest.TestCase):
    def test_results(self):
        self.assertEqual(my_sum(1, 2), 3)
        self.assertEqual(my_sum(-1, -2), -3)
        self.assertEqual(round(my_sum(2.1, 4.2), 2), 6.3)
        self.assertEqual(my_mult(2, 2), 4)
        self.assertEqual(my_mult(1, 1), 1)
        self.assertEqual(my_mult(2, 0), 0)
        self.assertEqual(my_mult(-2, 2), -4)
        self.assertEqual(my_mult(2, -2), -4)
        self.assertEqual(my_mult(-2, -2), 4)
        self.assertEqual(my_div(1, 1), 1.0)
        self.assertEqual(my_div(5, 2), 2.5)
        self.assertEqual(my_div(0, 5), 0)

    def test_args(self):
        with self.assertRaises(TypeError):
            my_sum("hey", 1)
            my_sum(1, "hey")
            my_sum(1, 2, 3)
            my_sum(1)
            my_sum()
            my_mult("hey", 1)
            my_mult(1, "hey")
            my_mult(1, 2, 3)
            my_mult(1)
            my_mult()
            my_div("hey", 1)
            my_div(1, "hey")
            my_div(1, 2, 3)
            my_div(1)
            my_div()

    def test_forbidden_ops(self):
        with self.assertRaises(ZeroDivisionError):
            my_div(5, 0)

# if __name__ == '__main__':
# 	unittest.main()
