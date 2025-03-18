"""Unit test using unittest for operations.py module"""

import unittest
from operations import invoice_tax, total_sum


class TestSumFunction(unittest.TestCase):
    """Unit test of total_sum function"""

    def test_total_sum_positive(self):
        """Test total sum positive"""
        self.assertEqual(total_sum(1, 2), 3)

    def test_total_sum_negative(self):
        """Test total sum negative test"""
        self.assertEqual(total_sum(-2, -3), -5)

    def test_invoice_tax_positive(self):
        """Invoice tax test"""
        self.assertEqual(invoice_tax(total_sum(1, 2), 14), 0.42)


if __name__ == "__main__":
    unittest.main()
