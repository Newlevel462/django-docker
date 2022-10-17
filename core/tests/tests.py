from django.test import TestCase


# Create your tests here.

class TestCaseNumbers(TestCase):
    def test_check_works(self):
        self.assertEqual(1, 1)
        self.assertEqual(2, 2)
