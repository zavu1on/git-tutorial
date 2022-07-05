import unittest
from summer import summer


class SummerTestCase(unittest.TestCase):

    def test_plus(self):
        res = summer(9)(8)(1)()

        self.assertEqual(res, 18)

    def test_minus(self):
        res = summer(-9)(-8)(-1)()

        self.assertEqual(res, -18)

    def test_plus_and_minus(self):
        res = summer(-9)(-8)(1)()

        self.assertEqual(res, -16)

    def test_multiple_value(self):
        res = summer(-9)(-8)(-1, 8)()

        self.assertEqual(res, -10)


if __name__ == '__main__':
    unittest.main()
