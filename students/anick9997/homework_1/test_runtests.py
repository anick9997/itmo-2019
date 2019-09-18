import unittest
from runtests import *


class TestRuntests(unittest.TestCase):
    def test_find_tests(self):
        with self.assertRaises(ValueError):
            find_tests("C:/I/do/not/exist")

    def test_run_tests(self):
        with self.assertRaises(ValueError):
            run_tests([])


# if __name__ == '__main__':
#     unittest.main()
