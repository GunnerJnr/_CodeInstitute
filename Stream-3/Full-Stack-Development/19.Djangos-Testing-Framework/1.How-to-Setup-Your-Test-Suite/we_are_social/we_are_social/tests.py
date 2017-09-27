"""
Tests.py:
"""
from unittest import TestCase


class SimpleTest(TestCase):
    """
    SimpleTest():
    """
    def test_adding_something_simple(self):
        """
        test_adding_something_simple():
        """
        self.assertEqual(1 + 2, 3)

    def test_adding_something_not_equal(self):
        """
        test_adding_something_not_equal():
        """
        self.assertNotEqual(1 + 2, 4)
