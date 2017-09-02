from unittest import TestCase

from foo.Solver import Solver


class TestSolver(TestCase):

    def test_divide_by_zero(self):
        s = Solver()
        self.assertRaises(Exception, s.divide, 4, 0)

    def test_normal_div(self):
        s = Solver()
        self.assertEqual(s.divide(4,2),2)

    def test_divide(self):
        self.fail()
