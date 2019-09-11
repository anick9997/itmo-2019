import unittest
from adulthood import *
from datetime import datetime


class TestAdulthood(unittest.TestCase):
    def test_is_adult(self):
        self.assertTrue(is_adult(
            lambda _: '1905.04.01',
            lambda: datetime(year=2019, month=9, day=1),
        )
        )
        self.assertFalse(is_adult(
            lambda _: '2018.04.01',
            lambda: datetime(year=2019, month=9, day=1),
        )
        )

# if __name__ == '__main__':
# 	unittest.main()
