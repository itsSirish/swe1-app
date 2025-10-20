from django.test import TestCase


# Create your tests here.
class BasicTestCase(TestCase):
    """
    Basic test case to ensure testing infrastructure is working.
    You can add more specific tests here later.
    """

    def test_basic_assertion(self):
        """Test that basic assertions work"""
        self.assertEqual(1 + 1, 2)

    def test_true_is_true(self):
        """Test that True is True"""
        self.assertTrue(True)


# Test Travis CI via PR
