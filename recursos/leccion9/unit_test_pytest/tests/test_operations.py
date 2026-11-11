"""Unit test using pytest for operations.py module"""

# import pytest
from operations import total_sum


def test_total_sum_positive():
    """Test total sum positive"""
    assert total_sum(1, 2) == 3

def test_total_sum_negative():
    """Test total sum negative"""
    assert total_sum(-2, -3) == -5
