import unittest

from example import sum_square_error

class TestRegression(unittest.TestCase):

    def test_sum_square_error(self):
        # function should return None if no data is supplied
        actual = sum_square_error([], [])
        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()