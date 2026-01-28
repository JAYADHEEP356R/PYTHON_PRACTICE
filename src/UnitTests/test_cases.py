

from unittest import TestCase

from math_utils.math_funcs import add,sub,multiply,divide

class UnitTests(TestCase):


    def test_add(self):

        self.assertEqual(add(5,7),12)

    def test_sub(self):

        self.assertEqual(sub(5,7),-2)

    def test_multiply(self):

        self.assertEqual(multiply(7,7),49)

    def test_divide(self):

        with self.assertRaises(ValueError):

            divide(5,0)

if __name__ == "__main__":
    import unittest
    unittest.main()
