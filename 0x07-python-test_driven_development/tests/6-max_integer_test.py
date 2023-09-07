#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """
        Test the max_integer function.
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([1, 5, 7, 7, 3, 5]), 7)
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 2.5]), 3.1)
        self.assertEqual(max_integer([1, 2.5, 3, 4.7]), 4.7)


if __name__ == "__main__":
    unittest.main()
