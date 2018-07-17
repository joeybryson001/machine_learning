import unittest

from example import sum_square_error

class TestRegression(unittest.TestCase):

    def test_sum_square_error(self):
        self.assertEqual(0, sum_square_error([], []))


if __name__ == '__main__':
    unittest.main()