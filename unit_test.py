import unittest

from linear_regression_final import regress

class TestRegression(unittest.TestCase):

    def test_regress(self):
        self.assertAlmostEqual(2, regress([[0,2],[1,2],[2,2],[3,2],[4,2],[5,2]],[6,2],0.001,0.001,0.0000001)[1],6)
    def test_regress2(self):
        self.assertAlmostEqual(1, regress([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7]],[6,8],0.001,0.001,0.0000001)[0],6)
    def test_regress3(self):
        self.assertAlmostEqual(None, regress([[0,2],[1,2],[2,2],[3,2],[4,2],[5,2]],[6,2],0.001,'string',0.0000001),6)


if __name__ == '__main__':
    unittest.main()