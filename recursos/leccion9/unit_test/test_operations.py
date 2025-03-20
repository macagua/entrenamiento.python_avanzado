"""Unit test using unittest for operations.py module"""

import unittest
from operations import total_sum


class TestSumFunction(unittest.TestCase):
    """Unit test of total_sum function"""

    def test_total_sum_positive(self):
        """Test total sum positive"""
        self.assertEqual(total_sum(1, 2), 3)

    def test_total_sum_negative(self):
        """Test total sum negative"""
        self.assertEqual(total_sum(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
