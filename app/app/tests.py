from django.test import TestCase
from app.calc import add, substract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that the two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(substract(5, 11), 6)