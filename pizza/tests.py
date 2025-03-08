from django.test import TestCase
"""
Sample tests
"""
from django.test import SimpleTestCase

from pizza import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)