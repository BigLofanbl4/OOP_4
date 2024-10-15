import unittest

from ind2 import Exponential, Linear


class TestLinear(unittest.TestCase):
    def setUp(self):
        self.linear = Linear(1, 5)  # a1=1, d=5

    def test_get_element(self):
        self.assertEqual(self.linear.get_element(4), 16)  # 1 + (4 - 1) * 5 = 16

    def test_get_sum(self):
        self.assertEqual(self.linear.get_sum(10), 235)  # n * (a1 + an) / 2


class TestExponential(unittest.TestCase):
    def setUp(self):
        self.exponential = Exponential(2, 3)  # a1=2, q=3

    def test_get_element(self):
        self.assertEqual(
            self.exponential.get_element(4), 54
        )  # 2 * 3^(4-1) = 54

    def test_get_sum(self):
        self.assertAlmostEqual(self.exponential.get_sum(10), 59048)

    def test_get_sum_q_equals_1(self):
        exp_q1 = Exponential(2, 1)  # Проверяем случай q = 1
        self.assertEqual(exp_q1.get_sum(5), 10)  # n * a1


if __name__ == "__main__":
    unittest.main()
